The current controller system is clunky to program with. Now that we are using QJSEngine ([PR #2682](https://github.com/mixxxdj/mixxx/pull/2682)) which supports ES7 as of Qt 5.12 in master, we can build a whole new controller mapping system that will be nicer to work with and implement features we have wanted for years. This wiki page explains plans for making this new controller mapping system.


## Terminology

In an effort to make the communication during discussions of this new system more concise, we are
standardizing the meaning of certain terms in this glossary:

|     Term     |   Definition   |
| -----------: | :------------- |
| Script       | Everything running in Javascript running in a `QJSEngine` |
| Mapping      | A mapping is a sub-term of script. A script that whose purpose is to translate between messages sent by a controller and the behavior in mixxx is considered a "Mapping". So while a mapping is a script, a script is not necessarily a mapping |°


## C++ refactoring

Currently, the C++ classes that handle controllers and controller mappings are arranged in this inheritance hierarchy:
```
                           Controller
           MidiController              HidController BulkController
PortMidiController Hss1394Controller
```
These Controller classes couple hardware I/O with the implementation of the legacy mapping system. Scripting is handled by the ControllerEngine class, which is a private member of Controller. ControllerEngine both runs the JavaScript interpreter (QJSEngine in master, QScriptEngine in Mixxx <= 2.3) and provides the API for scripts to interact with Mixxx via the `engine` object in the JS environment.

In [PR #2868](https://github.com/mixxxdj/mixxx/pull/2868) we have started working towards a new mapping system in which mapping is done entirely by JavaScript modules. Although this worked as a proof-of-concept hack in the legacy controller system, it became apparent that bringing the new system to its full potential requires major reorganization of the C++ code architecture.

The first step is to decouple the `engine` API in the script environment from the ControllerEngine class which manages the JS interpreter. This facilitates decoupling the JS handling code for the legacy and new controller systems so we can have a fresh start in the new system with only the code necessary for the new features. This has already been implemented in [PR #2920](https://github.com/mixxxdj/mixxx/pull/2920).

The next step is to split mapping handling code from the Controller classes so the Controller classes will only handle hardware I/O. Mappings will be handled by the new ControllerMappingProcessor classes. The new class hierarchy will be:
```
                  ControllerMappingProcessor
ModularControllerMappingProcessor   LegacyControllerMappingProcessor
                                    LegacyMidiControllerMappingProcessor

                                   Controller
              MidiController  HidController  BulkController
PortMidiController Hss1394Controller

                      ScriptEngine
                ControllerScriptEngine
ModularControllerScriptEngine LegacyControllerScriptEngine
```
Each ControllerMappingProcessor will be given at least one Controller* pointer upon construction by ControllerManager. From the controller polling thread, ControllerManager will call a `poll` method on each ControllerMappingProcessor. `ControllerMappingProcessor::poll` will call the `poll` method of each Controller* that it is using, then process the polled data as appropriate. For the ModularControllerMappingProcessor, this will pass the polled data to a JS callback as a QByteArray (turned into a Uint8Array in JS) plus a timestamp. LegacyControllerMapping will implement the legacy XML+JS system. Currently MidiController implements handling the XML mappings. This will be moved to LegacyMidiControllerMappingProcessor.

[Zulip discussion](https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/C.2B.2B.20controller.20system.20refactoring)

## Connecting controllers to JS environment / JSON metadata format
The Controller objects will be exposed to the JS environment via ControllerJSProxy wrappers like is currently done in master. By decoupling hardware I/O from handling the mapping, the new system allows multiple controllers to be mapped within one script. The script would be responsible for registering a callback function with each ControllerJSProxy to handle all incoming data from that controller. This will allow the scripts for different controllers to communicate with each other without requiring manipulating the state of Mixxx. For example, pressing a button on one controller could switch another controller to a different layer.

The JSON metadata file would specify unique identifying information for each controller so Mixxx could automatically load mappings for controllers. This file would be in the same directory as the JS module and would need a specific name, for example `metadata.json`. Like in [Bitwig Studio](https://zulip-uploads.s3.amazonaws.com/2380/8u3DsrCwnzNLjsJUesBJ1oe6/scripting-guide.pdf?AWSAccessKeyId=AKIAIEVMBCAT2WD3M5KQ&Signature=UbpI%2Fymx8Bd3DY%2FCbrr6iWCMs5A%3D&Expires=1594430101), multiple identifiers can be used to match a controller. This can accommodate for MIDI port name differences between different OSes. It could also be used to match one mapping to multiple controllers, for example the Allen & Heath Xone K2 and K1 can share a mapping, and many Pioneer DDJ controllers share the same MIDI commands. The `manufacturer` and `model` strings would be shown in the controller preferences GUI.
```javascript
controllers: {
  midi: [
     xoneK2: {
      midiPort: ["XONE:K2", "XONE:K1"]
      manufacturer: "Allen & Heath"
      model: "Xone K2 or K1"
     },
     launchpad: {
      midiPort: ["LAUNCHPAD"],
      manufacturer: "Novation"
      model: "Launchpad"
     }
  ]
}
```

The JSON object name for the controller would be used as a unique identifier to retrieve the ControllerJSProxy object in the script module:
```javascript
export function init() {
  const xoneK2 = mixxx.getMidiController("xoneK2");
  xoneK2.registerInputCallback(...);
  const launchpad = mixxx.getMidiController("launchpad");
  launchpad.registerInputCallback(...);
}
```

## New ControlObject JS API

The old `engine.getValue`/`engine.setValue`/`engine.getParameter`/`engine.setParameter` API will be replaced by a new C++ class with a constructor inserted into the JS environment as `mixxx.Control`:
```javascript
const play = new mixxx.Control('[Channel1]', 'play');
play.setValue(1);
play.toggle();
console.log(play.getValue()); // 0
// connect callback
play.setCallback(control => console.log(control.getValue()));
// disconnect callback
play.setCallback(null);
// manually invoke callback
play.trigger();
// Change group or key -- callback is automatically reconnected to new CO and triggered.
// A second boolean parameter can be added to avoid automatically triggering the callback,
// but most of the time automatically triggering the callback is helpful.
play.setGroup('[Channel3]');
play.setKey('cue_default');
```

The callbacks would be passed the `mixxx.Control` as their first parameter. If access to other context (for example, a surrounding Component from the Components JS library) is required inside the callback, use an arrow function or `Function.prototype.bind` to bind `this` for the callback.

[Zulip discussion](https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/ControlObjects.20as.20JS.20objects)

## New jog wheel scratching API

https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/new.20jog.20wheel.20API

## New Timer API

```javascript
const timer = new mixxx.Timer(milliseconds /*number*/, oneshot /*boolean*/, callback /*function*/);
timer.stop();
console.log(timer.isActive()); // false
timer.trigger(); // execute callback now -- timer does not need to be running
timer.restart(); // timer runs again
console.log(timer.isActive()); // true
timer.reset(); // reset elapsed time to 0
```
No arguments are passed to the callback.

[Zulip discussion](https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/new.20timer.20API)

## New Components JS library
https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/ComponentsJS.20intercomponent.20communication

## Rendering screens with QML

This functionality involves two parts:
1. Introduction of a dynamic object shared between the `QJSEngine` and the `QQMLEngine`.
The QJSEngine is then able to change properties on that shared object which cause the associated
reactive expression bindings in the `QQMLEngine` to be reevaluated.
2. A `QMLRenderer` Proxy class thats supposed to communicate between the `QQMLEngine` responsible
for rendering a QML file and the JS environment responsible for sending the render result to the hardware. 

```javascript
// The numbers are just examples.
controllers: {
  hid: [
    kontrols4mk3: {
      vendor_id: 0x17cc,
      product_id: 0x1310,
      usage_page: 0xff01,
      usage: 0x1,
      interface_number: 0x4,
      manufacturer: "Native Instruments",
      model: "Kontrol S4 Mk3 (HID controller)",
    }
  ],
  bulk: [
    kontrols4mk3screen: {
      vendor_id: 0x17cc,
      product_id: 0x1310,
      interface_number: 0x5,
      endpoint_out: 0x2,
      manufacturer: "Native Instruments",
      model: "Kontrol S4 Mk3 (screen)"
    }
  ]
}
```

In the JS module:
```javascript
export function init() {
   const controller = mixxx.getHidController("kontrols4mk3");
   controller.registerInputHandler(...);
   const screen = mixxx.getBulkController("kontrols4mk3screen");
   const screenRenderer = new mixxx.QMLRenderer("./kontrolsScreen.qml");
   screenRenderer.setRenderCallback(res => screen.send(res));
}
```

[Zulip discussion](https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/Controller.20objects.20in.20JS.20environment)

## Show documentation in the application
to be discussed

## Hotplug
https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Hotplugging

## Persistent state & preferences for mappings
https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/controller.20preferences.20design/

## Track metadata + waveform APIs
https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/New.20plugins

## Backburner

This is a list of features that would be nice to have in the long run, but aren't required in the MVP.

### Reload scripts using keycombo
Even though we already reload scripts when they are modified, we currently don't have a way to listen for changes in imported modules ([QTBUG-85430](https://bugreports.qt.io/browse/QTBUG-85430)). It would be nice to have a keycombo for reloading the entire script manually similar to how we have a keycombo for reloading skins on-the-fly.
