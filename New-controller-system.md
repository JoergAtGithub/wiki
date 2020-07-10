The current controller system is clunky to program with. Now that we are using QJSEngine ([PR #2682](https://github.com/mixxxdj/mixxx/pull/2682)) which supports ES7 as of Qt 5.12 in master, we can build a whole new controller mapping system that will be nicer to work with and implement features we have wanted for years. This wiki page explains plans for making this new controller mapping system.

## C++ refactoring
https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/new.20jog.20wheel.20API

Currently, the C++ classes that handle controllers are arranged in this inheritance hierarchy:
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
Each ControllerMappingProcessor will be given at least one Controller* pointer upon construction by ControllerManager. From the controller polling thread, ControllerManager will call a `poll` method on each ControllerMappingProcessor. `ControllerMappingProcessor::poll` will call the `poll` method of each Controller* that it is using, then process the polled data as appropriate. For the ModularControllerMappingProcessor, this will simply be passing the polled data to a JS callback from the module as a QByteArray (turned into a Uint8Array in JS) plus a timestamp. LegacyControllerMapping will implement the legacy XML+JS system. Currently MidiController implements handling the XML mappings. This will be moved to LegacyMidiControllerMappingProcessor.

The Controller objects will be exposed to the JS environment via ControllerJSProxy wrappers like is currently done in master. By decoupling hardware I/O from handling the mapping, the new system allows multiple controllers to be mapped within one script. This will allow the scripts for different controllers to communicate with each other without requiring manipulating the state of Mixxx. For example, pressing a button on one controller could switch another controller to a different layer.

## New ControlObject JS API
https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/ControlObjects.20as.20JS.20objects

## New jog wheel scratching API
https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/new.20jog.20wheel.20API

## New JSON metadata format
https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/new.20jog.20wheel.20API

## Hotplug
https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Hotplugging

## Persistent state & preferences for mappings
https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/controller.20preferences.20design/

## New Components JS library
https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/ComponentsJS.20intercomponent.20communication
