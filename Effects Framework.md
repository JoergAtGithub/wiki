## Summary

**Status**: This specification is **in drafting**. Please feel free to
edit this page.

DJs often augment their mixes with effects. Mixxx is severely lacking in
this department, as released versions of Mixxx only offer EQs and a
flanger.

This project aims to bring effects to Mixxx, both via native effects and
effects plugins via LADSPA, LV2, or VST.

## Requirements

  - Backend
  - Support for multiple backends
  - A general Effect interface which allows each effect to express:

<!-- end list -->

``` 
    * The effect name
    * A description of the effect
    * The parameters each effect has, including:
      * An internal identifier
      * A human-readable name
      * A prose description, with support for internationalization, suitable for display in a tooltip
      * Units and ranges of the parameter
    * A preferred ordering of parameters in order of importance
* A reference implementation of a backend implementing LADSPA support
* A reference implementation of a Mixxx-internal effects backend
    * Support for at least a flanger
* Effects / Engine Interface
* Multiple effects "slots" per-EngineChannel
* An Effect provided by an EffectsBackend can be allocated to a slot
* Controller (MIDI, etc) Interface
* MIDI scripts will interact with effects via the effects-slot abstraction.
* MIDI scripts can instruct an effects slot to cycle to the next or previous plugin
* GUI Widgets
* Per-deck single-effect widget. 
    * Pick selected effect
    * Shows up to 4 knobs to control that effect
    * Wet/Dry knob
* Multiple-effect chaining widget
    * Pick 3 effects, 1 parameter knob for each effect
    * Wet/Dry knob affects entire chain 
* A library-sized view for allocating available effects to slots
    * Support loading/saving effect presets
```

## Design

### Backend Implementation

The effects system will implement a backend model similar to Mixxx's
MIDI backend. Multiple backends will provide Effects that are aggregated
by an EffectsManager class. Each backend will provide effects either
loaded from a plugin system such as LADSPA, LV2, or VST. Alternatively,
a backend can implement effects natively and expose them via the same
Effect interface used by the plugin-based backends.

The EffectManager class provides an interface to the rest of Mixxx to
enumerate available plugins and get a new instance of that effect.

### Engine/Effect Interface

The EffectsManager uses the EffectsBackends to instantiate Effects from
EffectManifests. Once the EffectsManager instantiates an Effect, it is
able to ask the Effect to process a buffer of audio.

An EffectSlot is an abstraction over an Effect. It provides a
ControlObject interface for controlling the parameters of an Effect. To
a user, an EffectSlot is the equivalent of a "selected" effect. Knobs in
the GUI and MIDI controller connect to the EffectSlot's controls, which
in turn are used to control the Effect that is loaded into the slot.

One or more EffectSlots are grouped into EffectChains. The EngineMaster
and EngineChannels interact with the effects framework at the level of
EffectChains. Every EffectChain is conditionally applied to multiple
EngineChannel's (e.g. \[Channel1\], \[Channel2\], \[Sampler1\], etc). In
addition to EngineChannels, EffectChains are conditionally applied to
both the EngineMaster master output (\[Master\]) and the headphone
output (\[Headphone\]).

### Controllers

### User Interface

## Work Breakdown

## Current Progress

This feature has been attempted twice by two GSoC students. There is a
lot of old code lying around, and we will try to reuse whenever
possible. The current branch for work on this feature is the
[lp:\~mixxxdevelopers/mixxx/features\_effects](https://code.launchpad.net/~mixxxdevelopers/mixxx/features_effects)
branch.

## Team

  - RJ Ryan
