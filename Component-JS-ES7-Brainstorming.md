# Component JS ES7 Brainstorming

## Purpose

This Document aims to document some design goals and decisions made for an updated ComponentsJS version.

## Lessons learned from ``midi-components-0.0.js`

### What was great?

* Lifecycle management. Making your controller work correctly on shutdown, startup, switching layers etc was quite easy because of the semantic mapping of components to their outputs.
* QML-like design (Objects inheriting from other objects, etc).
* Semantic reasoning about behavior makes it much easier to review contributed mappings.

### What is suboptimal?

* Creating reusable components is difficult without in-depth JS knowledge because of verbose and difficult to understand prototypical inheritance, mixed with our own `Object.assign` magic.
* Some implicit design decisions lead to incompatibilities down the road. These are mentioned in a separate section below.
* Each component needs manual mapping of its input handler. This is mostly a limitation of the current midi controller mapping API, though the current components API also doesn't properly allow defining those. 
* layering was confusing and inconsistent often times. ComponentContainers and `shift` often fighting, we should opt for a universal approach (ditching `shift` in favor of using layering everywhere). How would changing these affect elegance of the API / Dryness?
* Recursively iterating the component hierarchy is intrusive and not customizable by child component(containers) further down the tree. 

## Design goals

* QML-like design (Objects inheriting from other objects, etc). This is somewhat incompatible with the syntax sugar of ES6 Class syntax

* Protocol agnostic. The lifecycle management should be unrelated to underlying protocol. 
  For this to work, we need a little more abstraction, which is difficult to do while keeping it easy to use, but I believe it to be doable.  
  For that, we abstract the input away from the component. For example, a Button just needs to know whether its currently pressed or not, but not on what protocol its based. The same applies to output. 
* Statically typed by use of jsdoc type annotations with type checking using the typescript-compiler. Should allow to detect issues in libraries earlier. 
* Possibly ES6-module based (needs new controller mapping format). 

## Necessary semantic breaks in `midi-components-0.0.js` API:

* Obviously, the protocol independence is a break in API though most of the time though that is largely textual and less in terms of different semantics. 
* Hotcue buttons should use the `hotcue_X_status` instead of `hotcue_X_enabled`. This is a breaking API change since current controller mappings depend on the values of that CO in their own `outValueScale` implementations. We should also reorganize the API to properly signal unset, set, and active hotcues/loops. 
* `Pot`s with different resolutions need explicit handling (7-/14-/N-bit resolution), respective ordering when those values are spread over different messages. 

## Implementation Sketch

* Create 3 libraries: `ComponentsJS 2.0` (protocol agnostic) state and lifetime management, "Midi IO Library" (midi implementations for the input abstractions for each of the components), "HID IO Library" (same as the midi, but this time taking care of HID packet parsing, etc). 

## Open questions

* While I'd like the API generic over the underlying protocol, my experience with anything but Midi is certainly limited. Greatly appreciate opinions here.
* MIDI and HID have a different data exchange model, MIDI is more event-based (sending differences when they occur) while HID is more state-based (sending the entire state of the controller very frequently). We somehow need to be generic over these two approaches, so we can map to the event-based approach used in Mixxx (COs). 
* We should evaluate the frameworks introduced in other controller mappings. See [MiniMixxx](https://github.com/mixxxdj/mixxx/blob/main/res/controllers/Yaeltex-MiniMixxx-scripts.js), [Behringer DDM4000](https://github.com/mixxxdj/mixxx/blob/main/res/controllers/Behringer-DDM4000-scripts.js), [Launchpad](https://github.com/dszakallas/mixxx-launchpad/)