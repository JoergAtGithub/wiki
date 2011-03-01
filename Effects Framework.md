## Summary

**Status**: This specification is **in drafting**. Please feel free to
edit this page and add your comments.

DJs often augment their mixes with effects. Mixxx is severely lacking in
this department, as released versions of Mixxx only offer EQs and a
flanger.

This project aims to bring effects to Mixxx, both via native effects and
effects plugins via LADSPA, LV2, or VST.

## Requirements

  - A general EffectManifest interface which allows each effect to
    express:
  - The effect name (internationalizable)
  - A description of the effect (internationalizable)
  - The parameters each effect has, including:

<!-- end list -->

``` 
    * An internal identifier 
    * A human-readable name (internationalizable)
    * A prose description, with support for internationalization, suitable for display in a tooltip. (internationalizable)
    * Units and maximum/minimum/default values of the parameter
* A preferred ordering of parameters in order of importance
* Backend
* Support for multiple backends (plugin based or not)
* A reference implementation of a Mixxx-internal effects backend
    * Support for at least a flanger
* Effect Instances (known as "Effect")
* Support the customization of parameter ranges to a subset of the EffectManifest's min/max ranges 
* Support linking of individual parameters to the Effect Chain's meta-knob.
* **TODO: Each effect shall have an individual wet/dry parameter?**
* Effect Chains
* Support chaining multiple Effects together into an Effect Chain.
* **TODO: Each effect chain shall have a wet/dry parameter? Or an enabled button?**
* Each effect chain will have one "Meta/Super/Wonder/Master/Action/Crazy/Funky-Knob" which individual parameters of effects in the chain can be linked to.
* Must support loading and saving of effect-chains ("Presets")
* Support applying effect chains to multiple different audio sources (samplers, decks, master out, headphone out)
* Control (MIDI, etc) Interface
* MIDI scripts must be able to control loaded effects parameters
* MIDI scripts must be able to request that an effect be ejected or a next/previous effect be loaded. (support effect knobs on e.g. NS7)
* MIDI scripts must be able to observe effect chains and make changes.
* MIDI scripts must have a simple-mode by which they can treat parameters as 0.0 - 1.0 values so they do not have to deal with the complexity of min/max values, types, etc.
* GUI Widgets
* Per-deck single-effect widget. 
    * Pick selected effect
    * Shows up to 4 knobs to control that effect
    * Wet/Dry knob
* Multiple-effect chaining widget
    * Pick 3 effects, 1 parameter knob for each effect
    * Wet/Dry knob affects entire chain 
* A library-sized view for allocating available effects to effect chains
    * Support loading/saving effect presets
```

## Design

### High-Level Overview

The goal is that the DJ can enhance their performance through the use of
audio effects. To present this in a simple-to-use and powerful way, we
introduce the metaphor of "Effect Chains". An effect chain is nothing
more than a list of effects which are applied sequentially to audio. An
effect chain can be applied to decks, samplers, the headphone out, and
the master output.

The DJ configures effect chains by selecting effects that are available
to her from any variety of effect sources (native built-in plugins,
LADSPA plugins, LV2 plugins, VST plugins, etc.) and adding them to the
chain. She does this from a view called "Effect Chain Edit Mode" that
takes the place of where the Mixxx library normally sits.

Once the DJ has selected the effects that she desires to be in the
chain, then the parameters of that effect are made available to her to
tweak to her liking. Each parameter can be adjusted in the following
ways:

  - Change the value of the parameter
  - Change the minimum / maximum limits of the parameter
  - Invert the knob so that turning it clockwise goes from high to low
    instead of low to high.
  - In the case of a knob, change whether the parameter is controlled
    linearly or logarithmically
  - Assign the parameter to be controlled by the effect chain's "Wonder
    Knob". See the "Wonder Knob" section below.

Once the DJ is done configuring the effect chain and the parameters of
the effects that are in the effect chain, she may save the effect chain
and give it a name. Alternatively, she can also load a previously saved
chain from the Chain Edit Mode.

The key idea here is that the DJ should invest time in crafting and
creating the unique sounds she would like to make via Effect Chains
**prior** to her sets. While it will be possible to create Effect Chains
on the fly, it will be a lot less stressful if she has invested the time
beforehand.

#### The Wonder Knob

**TODO: Insert marketing name here :) Candidates: SuperKnob, WonderKnob,
MetaKnob, HyperKnob, AwesomeKnob, FunkyKnob, MagicKnob**

Every effect chain has a single knob called the "Wonder Knob". This knob
is meant to be the go-to knob for the DJ to tweak during her set to make
awesome effect noises happen. If you look at a lot of Ean Golden's
videos on [DJTechTools](http://djtechtools.com), this is how many of his
combinations of effects work. There is one knob to turn that produces
the desired effect. This is both a **huge** usability win (no knob soup)
and allows the DJ to focus on what she is doing. As previously outlined,
when creating an effect chain in Chain Edit Mode, the DJ can link one or
more of each effect's parameters to the chain's "Wonder Knob". This,
combined with with the ability to tweak the min/max ranges, and the
linear/log settings of the knobs, allows the DJ to create one knob that
does the work of what she would normally do by tweaking multiple knobs
simultaneously.

One benefit of having a "Wonder Knob" is that it maps very naturally to
many MIDI controllers, which often have a limited number of knobs
available for tweaking effets. One example of this is the Numark V7/NS7,
which only has a single effect-selector knob and an effect-parameter
knob. In this case, we would make the effect selector knob select the
active effect chain, and the effect-parameter knob tweak the "Wonder
Knob". In ITCH, the V7/NS6/NS7FX are limited to only a single effect at
a time, and these knobs are designed to reflect that. By mapping this
knob to effect chains, we will allow NS7/V7 owners to achieve a
categorically more flexible effect setup.

### Effect Representation

The properties of an effect are described by an EffectManifest object.
An EffectManifest is an immutable data type (should always be const)
that fully describes all of the effect's properties that are relevant to
user-facing aspects of effects. This includes a description of each
user-facing parameter of each effect, along with metadata describing
hints for how the parameter should be presented to the user, limits of
the parameter's values, and default values for the parameter. An
EffectManifest is strictly an abstract description of the effect, and
has nothing to do with an actual instantiation of an effect. An Effect
object is an instantiation of an EffectManifest, and manages actual
instance values for each parameter described in the EffectManifest.

| EffectManifest Properties |                                                                      |
| ------------------------- | -------------------------------------------------------------------- |
| Property                  | Description                                                          |
| name                      | Effect name (internationalizable)                                    |
| author                    | Author name                                                          |
| version                   | Effect version (string)                                              |
| description               | Effect description (internationalizable)                             |
| parameters                | A list of EffectParameter objects, describing user-facing parameters |

| EffectParameter Properties |                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Property                   | Description                                                                                                      |
| name                       | Effect name (internationalizable)                                                                                |
| description                | Effect description (internationalizable)                                                                         |
| defaultValue               | Parameter's default value                                                                                        |
| minimumValue               | Parameter's minimum value, if any                                                                                |
| maximumValue               | Parameter's maximum value, if any                                                                                |
| valueHint                  | A hint describing the type of the parameter's value (boolean, float, integer, etc.)                              |
| controlHint                | A hint describing the most logical control type for the parameter (potmeter, log-potmeter, toggle, slider, etc.) |
| semanticHint               | A hint describing the semantic type of the value (pitch, samples, time, duration)                                |
| unitsHint                  | A hint describing the units of the value (time, hertz, fraction of samplerate)                                   |

**NOTE:** The hints are still under development. Please give feedback\!

### Backend Implementation

The effects system will implement a backend model similar to Mixxx's
MIDI backend. Multiple backends will provide Effects that are aggregated
by an EffectsManager class. Each backend will provide effects either
loaded from a plugin system such as LADSPA, LV2, or VST. Alternatively,
a backend can implement effects natively and expose them via the same
Effect interface used by the plugin-based backends.

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

|  | \[Group\]                     |  | Key/Control                   |  | Range              |  | What it does                                                                                          |  |
|  | ----------------------------- |  | ----------------------------- |  | ------------------ |  | ----------------------------------------------------------------------------------------------------- |  |
|  | \[EffectChainN\]              |  | num\_effectslots              |  | integer, read-only |  | The number of EffectSlots that this EffectChain has                                                   |  |
|  | \[EffectChainN\]              |  | dry\_wet                      |  | 0.0..1.0           |  | The dry/wet mixing ratio for this EffectChain with the EngineChannels it is mixed with                |  |
|  | \[EffectChainN\]              |  | metaknob                      |  | 0.0..1.0           |  | The EffectChain master control knob. Controls all parameters that are linked to the chain's metaknob. |  |
|  | \[EffectChainN\]              |  | next\_chain                   |  | binary             |  | Cycle to the next EffectChain preset after the currently loaded preset.                               |  |
|  | \[EffectChainN\]              |  | prev\_chain                   |  | binary             |  | Cycle to the previous EffectChain preset before the currently loaded preset.                          |  |
|  | \[EffectChainN\]              |  | channel\_ChannelI             |  | binary             |  | Whether or not this EffectChain applies to Deck I                                                     |  |
|  | \[EffectChainN\]              |  | channel\_SamplerJ             |  | binary             |  | Whether or not this EffectChain applies to Sampler J                                                  |  |
|  | \[EffectChainN\]              |  | channel\_Master               |  | binary             |  | Whether or not this EffectChain applies to the Master output                                          |  |
|  | \[EffectChainN\]              |  | channel\_Headphone            |  | binary             |  | Whether or not this EffectChain applies to the Headphone output                                       |  |
|  | \[Group\]                     |  | Key/Control                   |  | Range              |  | What it does                                                                                          |  |
|  | \[EffectChainN\_EffectSlotM\] |  | enabled                       |  | binary, read-only  |  | Whether an Effect is loaded into this EffectSlot                                                      |  |
|  | \[EffectChainN\_EffectSlotM\] |  | num\_parameters               |  | integer, read-only |  | The number of parameters the currently loaded effect has. 0 if no effect is loaded                    |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_enabled           |  | binary, read-only  |  | Whether or not the Kth parameter is enabled.                                                          |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_type       |  | integer, read-only |  | The type of the Kth parameter value. See the Parameter Value Types table.                             |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_min        |  | double             |  | The minimum configured value of the Kth parameter.                                                    |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_max        |  | double             |  | The maximum configured value of the Kth parameter.                                                    |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_min\_limit |  | double, read-only  |  | The minimum allowable value of the Kth parameter's minimum.                                           |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_max\_limit |  | double, read-only  |  | The maximum allowable value of the Kth parameter's minimum.                                           |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_default    |  | double, read-only  |  | The default value of the parameter.                                                                   |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value             |  | double             |  | The raw value of the Kth parameter. See the Parameter Values section for more information.            |  |
|  | \[EffectChainN\_EffectSlotM\] |  | parameterK\_value\_normalized |  | 0.0..1.0           |  | The value of the Kth parameter, normalized to the range of 0.0 to 1.0.                                |  |

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

## Controller Impact Assessment

| Controller                                                                                                                                                              | Effects? | Settings                                                                                           | Fit?    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------- | ------- |
| [American Audio VMS4](http://www.digitaldjtips.com/wp-content/uploads/2010/11/american-audio-vms4.jpg)                                                                  | Y        | Per-deck effect-select knob, effect parameter knob, effect enable button, parameter toggle button? | Good    |
| [Numark NS7](http://www.meramani.com/bigpic/496/497/20091121015820.jpg)                                                                                                 | N        |                                                                                                    |         |
| [Numark NS7FX](http://www.tamtamonline.com/media/catalog/product/cache/3/image/5e06319eda06f020e43594a9c230972d/n/u/numark-nsfx.jpg)                                    | Y        | Per-deck effect selector, parameter, mix, source knobs. Effect on/off and tap buttons.             | Perfect |
| [Numark V7](http://www.numark.com/stuff/contentmgr/files/24/830107e06e04bbc75e07e04e08a48e01/large/v7_top_lg.jpg)                                                       | Y        | Effect selector, parameter knobs. Effect Mix fader, Effect on/off button and tap buttons           | Perfect |
| [Pioneer DDJ-S1](http://createdigitalmusic.com/files/2011/01/ddjs1.jpg)                                                                                                 | Y        | Per-deck effect selector, parameter, mix, source knobs. Effect on/off and tap buttons.             | Perfect |
| [Numark NS6](http://www.numark.com/stuff/contentmgr/files/27/54855ae10ce78345971f892114788cfd/large/ns6_ortho_lrg.jpg)                                                  | Y        | Per-deck effect selector, parameter, mix, source knobs. Effect on/off and tap buttons.             | Perfect |
| [Numark MIXTRACK](http://www.gearnuts.com/images/closeup/xl/1600-Mixtrack_top.jpg)                                                                                      | Y        | Per-deck effect enable, effect select knob, 2x parameter knob                                      | Perfect |
| [Stanton SCS.1d](http://qualityelectronics.net/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/c/scs1d_top.jpg)                                  | Y        | Highly programmable                                                                                | Medium  |
| [Native Instruments S4](http://cachepe.zzounds.com/media/quality,85/brand,zzounds/NI_Traktor_Kontrol_S4_top-a19738755dd69761d1fb33f0e8ec7cad.jpg)                       | Y        | 4-effect knobs per chain                                                                           | Good    |
| [NI Traktor Kontrol X1](http://turntabling.net/wp-content/uploads/2011/01/NI-TRAKTOR_KONTROL_X1_Controller.jpg)                                                         | Y        | 4-effect knobs per chain                                                                           | Good    |
| [Reloop Digital Jockey 2](http://www.digitaldjtips.com/wp-content/uploads/2010/11/reloop-digital-jockey-2-master-edition.jpg)                                           | Y        | 3 effect enable/select/parameter knobs per deck                                                    | Medium  |
| [Vestax VCI-300](http://snatchthieves.files.wordpress.com/2010/07/vestax-vci-300.jpg)                                                                                   | N        |                                                                                                    |         |
| [Vestax VCI-100SE DJTT Edition](http://img183.imageshack.us/f/vci100seoverlay.png/)                                                                                     | Y        | Wet-dry, 3-effect parameter knobs per effects unit                                                 | Medium  |
| [Vestax Typhoon](http://www.agiprodj.com/images/vestax-typhoon-top-popup.jpg)                                                                                           | Y        | 2 wet/dry knobs + enabled buttons                                                                  | Good    |
| [Vestax Spin](http://www.algoriddim.com/press/vestax-spin-top.jpg)                                                                                                      | Y        | 2 FX enabled buttons??                                                                             | Medium  |
| [M-Audio Torq Xponent](http://cachepe.samedaymusic.com/media/quality,85/brand,sameday/xponent_top-15f5539b4b7c7f1cad233509e0bfa895.jpg)                                 | Y        | 4 effect parameter knob + 4 enabled buttons per deck                                               | Medium  |
| [Hercules DJ Console RMX](http://www.skratchworx.com/images/hercules/rmx_top.jpg)                                                                                       | N        |                                                                                                    |         |
| [Hercules DJ Console 4MX](http://www.dv247.com/assets/products/79891_l.jpg)                                                                                             | N        |                                                                                                    |         |
| [Hercules DJ Console Mk4](http://maxborgesagency.com/wp-content/uploads/4780638-Hercules-DJConsole-Mk4-Top.jpg)                                                         | N        |                                                                                                    |         |
| [Hercules DJ Control Steel](http://www.madmanaudio.com/images/madmanaudio%20%20Hercules%20DJ%20Control%20Steel%20Controller.jpg)                                        | N        |                                                                                                    |         |
| [Hercules DJ Control MP3 e2](http://bestmixtrackreviews.com/blog/wp-content/themes/guitarreviewtheme/wordpressreviewtheme%20v1.4/images/hercules-dj-control-mp3-e2.jpg) | N        |                                                                                                    |         |

## Work Breakdown

## Current Progress

This feature has been attempted twice by two GSoC students. There is a
lot of old code lying around, and we will try to reuse whenever
possible. The current branch for work on this feature is the
[lp:\~mixxxdevelopers/mixxx/features\_effects](https://code.launchpad.net/~mixxxdevelopers/mixxx/features_effects)
branch.

## Team

  - RJ Ryan
