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

The properties of an Effect provided by an EffectsBackend are described
by an EffectManifest object. An EffectManifest is an immutable data type
(should always be const) that fully describes all of the Effect's
properties that are relevant to user-facing aspects of effects. This
includes a description of each user-facing parameter of each effect,
along with metadata describing hints for how the parameter should be
presented to the user, limits of the parameter's values, and default
values for the parameter. An EffectManifest is strictly an abstract
description of the effect, and has nothing to do with an actual
instantiation of an effect. An Effect object is an instantiation of an
EffectManifest, and manages actual instance values for each parameter
described in the EffectManifest.

| EffectManifest Properties |                                                                      |
| ------------------------- | -------------------------------------------------------------------- |
| Property                  | Description                                                          |
| name                      | Effect name (internationalizable)                                    |
| author                    | Author name                                                          |
| version                   | Effect version (string)                                              |
| description               | Effect description (internationalizable)                             |
| parameters                | A list of EffectParameter objects, describing user-facing parameters |

| EffectParameter Properties |                                          |
| -------------------------- | ---------------------------------------- |
| Property                   | Description                              |
| name                       | Effect name (internationalizable)        |
| description                | Effect description (internationalizable) |
| defaultValue               | Parameter's default value                |
| minimumValue               | Parameter's minimum value, if any        |
| maximumValue               | Parameter's maximum value, if any        |
| valueHint                  |                                          |
| controlHint                |                                          |
| semanticHint               |                                          |
| unitsHint                  |                                          |

Given an Effect instance, a buffer of audio can be processed given the
parameter settings in the instance.

**TODO: Should Effect be renamed EffectInstance?**

### Engine/Effect Interface

The EffectsManager uses the EffectsBackends to instantiate Effects from
EffectManifests. Once the EffectsManager instantiates an Effect, it is
able to ask the Effect to process a buffer of audio.

An EffectSlot is an abstraction over an Effect. It provides a
ControlObject interface for controlling the parameters of an Effect. To
a user, an EffectSlot is the equivalent of a "selected" effect. Knobs in
the GUI and MIDI controllers connect to the EffectSlot's controls, which
in turn are used to control the Effect that is loaded into the slot.

One or more EffectSlots are grouped into EffectChains. The EngineMaster
and EngineChannels interact with the effects framework at the level of
EffectChains. Every EffectChain is conditionally applied to multiple
EngineChannel's (e.g. \[Channel1\], \[Channel2\], \[Sampler1\], etc). In
addition to EngineChannels, EffectChains are conditionally applied to
both the EngineMaster master output (\[Master\]) and the headphone
output (\[Headphone\]).

**TODO: Should EffectChain be named EffectUnit?**

### Controls

The EffectsManager class provides the following global information
controls:

|  | \[Group\]   |  | Key/Control       |  | Range              |  | What it does                          |  |
|  | ----------- |  | ----------------- |  | ------------------ |  | ------------------------------------- |  |
|  | \[Effects\] |  | num\_effectchains |  | integer, read-only |  | The number of EffectChains that exist |  |

EffectChains and EffectSlots both provide a ControlObject interface for
both the GUI and MIDI controllers to interact with. At creation time,
all EffectChains are assigned a sequential, unique ID starting at 1. All
EffectChains have the group `[EffectChainN]` where N is the
EffectChain's ID.

|  | \[Group\]                     |  | Key/Control                   |  | Range              |  | What it does                                                                               |  |
|  | ----------------------------- |  | ----------------------------- |  | ------------------ |  | ------------------------------------------------------------------------------------------ |  |
|  | \[EffectChainN\]              |  | num\_effectslots              |  | integer, read-only |  | The number of EffectSlots that this EffectChain has                                        |  |
|  | \[EffectChainN\]              |  | dry\_wet                      |  | 0.0..1.0           |  | The dry/wet mixing ratio for this EffectChain with the EngineChannels it is mixed with     |  |
|  | \[EffectChainN\]              |  | channel\_ChannelI             |  | binary             |  | Whether or not this EffectChain applies to Deck I                                          |  |
|  | \[EffectChainN\]              |  | channel\_SamplerJ             |  | binary             |  | Whether or not this EffectChain applies to Sampler J                                       |  |
|  | \[EffectChainN\]              |  | channel\_Master               |  | binary             |  | Whether or not this EffectChain applies to the Master output                               |  |
|  | \[EffectChainN\]              |  | channel\_Headphone            |  | binary             |  | Whether or not this EffectChain applies to the Headphone output                            |  |
|  | \[Group\]                     |  | Key/Control                   |  | Range              |  | What it does                                                                               |  |
|  | \[EffectChainN\_EffectSlotM\] |  | enabled                       |  | binary, read-only  |  | Whether an Effect is loaded into this EffectSlot                                           |  |
|  | \[EffectChainN\_EffectSlotM\] |  | num\_parameters               |  | integer, read-only |  | The number of parameters the currently loaded effect has. 0 if no effect is loaded         |  |
|  | \[EffectChainN\_EffectSlotM\] |  | eject                         |  | binary             |  | Eject the loaded Effect from this EffectSlot                                               |  |
|  | \[EffectChainN\_EffectSlotM\] |  | next\_effect                  |  | binary             |  | Cycle to the next Effect after the currently loaded Effect                                 |  |
|  | \[EffectChainN\_EffectSlotM\] |  | prev\_effect                  |  | binary             |  | Cycle to the previous Effect before the currently loaded Effect                            |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_enabled           |  | binary, read-only  |  | Whether or not the Kth parameter is enabled.                                               |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_type       |  | integer, read-only |  | The type of the Kth parameter value. See the Parameter Value Types table.                  |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_min        |  | double, read-only  |  | The minimum value of the Kth parameter.                                                    |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_max        |  | double, read-only  |  | The maximum value of the Kth parameter.                                                    |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_default    |  | double, read-only  |  | The default value of the parameter.                                                        |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value             |  | double             |  | The raw value of the Kth parameter. See the Parameter Values section for more information. |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_normalized |  | 0.0..1.0           |  | The value of the Kth parameter, normalized to the range of 0.0 to 1.0.                     |  |

In the above table,

  - N ranges from 1 to \[Effects\],num\_effectchains, inclusive. 
  - M ranges from 1 to \[EffectChainN\],num\_effectslots, inclusive.
    (For a given value of N)
  - K ranges from 1 to \[EffectChainN\_EffectSlotM\],num\_parameters,
    inclusive. (For given values of N and M)
  - I ranges from 1 to \[Master\],num\_decks, inclusive.
  - J ranges from 1 to \[Master\],num\_samplers, inclusive.

**NOTE:** The reason for 1-indexing versus 0-indexing is the significant
precedent within the Control system for 1-indexing. (e.g. hotcues,
Deck/Sampler names, etc.)

#### Parameter Values

Since the Control system is not capable of representing values other
than numeric values, for the first iteration of the effects system, we
must use a numeric coding system for representing the parameter types.
If the GUI or MIDI Script author does not care about choosing correct
values, he or she can use the parameterK\_value\_normalized control,
which will always represent the parameter value as normalized to the
range of 0.0 to 1.0. To use the parameterK\_value control, the setter
must check the value against parameterK\_type (see the Parameter Types
table below), parameterK\_value\_min, and parameterK\_value\_max to
ensure the value is within the correct range. Invalid settings of any
parameterK\_value controls will be ignored.

| Parameter Value Type | Integer Value | Intepretation                               |
| -------------------- | ------------- | ------------------------------------------- |
| Boolean              | 0             | Set only to values of 0 (false) or 1 (true) |
| Integer              | 1             | Set to any integral value                   |
| Double               | 2             | Set to any double value.                    |

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
