## Summary

**Status**: This specification is **in drafting**. Please feel free to
edit this page and add your comments.

DJs often augment their mixes with effects. Mixxx is severely lacking in
this department, as released versions of Mixxx only offer EQs and a
flanger.

This project aims to bring effects to Mixxx, both via native effects and
effects plugins via LADSPA, LV2, or VST.

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

### Requirements

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
* EffectChain widget
    * Show selected EffectChain name
    * Parameter Knob
    * Channel Select buttons
* EffectChain Editor Library section
    * See existing chain presets
    * Create new preset
    * Add/remove effect to existing chain
    * Change value of parameter of effect in slot
    * Right-click hover overlay for tweaking ranges, defaults.
```

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

### Engine/Effect Interface

The EffectsManager uses the EffectsBackends to instantiate Effects from
EffectManifests. Once the EffectsManager instantiates an Effect, it is
able to ask the Effect to process a buffer of audio.

An EffectSlot is an abstraction over an Effect. It provides a
ControlObject interface for controlling the parameters of an Effect. To
a user, an EffectSlot is the equivalent of a "selected" effect. Knobs in
the GUI and MIDI controllers connect to the EffectSlot's controls, which
in turn are used to control the Effect that is loaded into the slot.
Similarly, an EffectChainSlot is an abstraction over an EffectChain. It
provides a ControlObject interface to controlling an EffectChain that is
loaded into it. To a user, an EffectChainSlot is an "effect unit" which
is a chain of EffectSlots.

One or more EffectSlots are grouped into an EffectChainSlot. The
EngineMaster and EngineChannels interact with the effects framework at
the level of EffectChains. Every EffectChain is conditionally applied to
multiple EngineChannel's (e.g. \[Channel1\], \[Channel2\], \[Sampler1\],
etc). In addition to EngineChannels, EffectChains are conditionally
applied to both the EngineMaster master output (\[Master\]) and the
headphone output (\[Headphone\]).

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

|  | \[Group\]                             |  | Key/Control            |  | Range              |  | What it does                                                                                          |  |
|  | ------------------------------------- |  | ---------------------- |  | ------------------ |  | ----------------------------------------------------------------------------------------------------- |  |
|  | \[EffectChainN\]                      |  | num\_effects           |  | integer, read-only |  | The number of Effects that this EffectChain has                                                       |  |
|  | \[EffectChainN\]                      |  | mix                    |  | 0.0..1.0           |  | The dry/wet mixing ratio for this EffectChain with the EngineChannels it is mixed with                |  |
|  | \[EffectChainN\]                      |  | enabled                |  | binary             |  | Whether the EffectChain is enabled                                                                    |  |
|  | \[EffectChainN\]                      |  | metaknob               |  | 0.0..1.0           |  | The EffectChain master control knob. Controls all parameters that are linked to the chain's metaknob. |  |
|  | \[EffectChainN\]                      |  | next\_chain            |  | binary             |  | Cycle to the next EffectChain preset after the currently loaded preset.                               |  |
|  | \[EffectChainN\]                      |  | prev\_chain            |  | binary             |  | Cycle to the previous EffectChain preset before the currently loaded preset.                          |  |
|  | \[EffectChainN\]                      |  | channel\_\[ChannelI\]  |  | binary             |  | Whether or not this EffectChain applies to Deck I                                                     |  |
|  | \[EffectChainN\]                      |  | channel\_\[SamplerJ\]  |  | binary             |  | Whether or not this EffectChain applies to Sampler J                                                  |  |
|  | \[EffectChainN\]                      |  | channel\_\[Master\]    |  | binary             |  | Whether or not this EffectChain applies to the Master output                                          |  |
|  | \[EffectChainN\]                      |  | channel\_\[Headphone\] |  | binary             |  | Whether or not this EffectChain applies to the Headphone output                                       |  |
|  | \[Group\]                             |  | Key/Control            |  | Range              |  | What it does                                                                                          |  |
|  | \[EffectChainN\_EffectM\]             |  | enabled                |  | binary, read-only  |  | Whether an Effect is loaded into this EffectSlot                                                      |  |
|  | \[EffectChainN\_EffectM\]             |  | num\_parameters        |  | integer, read-only |  | The number of parameters the currently loaded effect has. 0 if no effect is loaded                    |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | enabled                |  | binary, read-only  |  | Whether or not the Kth parameter is enabled.                                                          |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | linked                 |  | binary             |  | Whether or not the Kth parameter is linked to the EffectChain superknob.                              |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | value\_type            |  | integer, read-only |  | The type of the Kth parameter value. See the Parameter Value Types table.                             |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | value\_min             |  | double             |  | The minimum configured value of the Kth parameter.                                                    |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | value\_max             |  | double             |  | The maximum configured value of the Kth parameter.                                                    |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | value\_min\_limit      |  | double, read-only  |  | The minimum allowable value of the Kth parameter's minimum.                                           |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | value\_max\_limit      |  | double, read-only  |  | The maximum allowable value of the Kth parameter's minimum.                                           |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | value\_default         |  | double, read-only  |  | The default value of the parameter.                                                                   |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | value                  |  | double             |  | The raw value of the Kth parameter. See the Parameter Values section for more information.            |  |
|  | \[EffectChainN\_EffectM\_ParameterK\] |  | value\_normalized      |  | 0.0..1.0           |  | The value of the Kth parameter, normalized to the range of 0.0 to 1.0.                                |  |

In the above table,

  - N ranges from 1 to \[Effects\],num\_effectchains, inclusive. 
  - M ranges from 1 to \[EffectChainN\],num\_effectslots, inclusive.
    (For a given value of N)
  - K ranges from 1 to \[EffectChainN\_EffectM\],num\_parameters,
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

Brainstorming for now. Basing heavily off of Jus's mockups from Summer
2010: [Effects Units
Mockup](https://picasaweb.google.com/lh/photo/jjgZU45-DQWMdz0CCwEVbw)
[Effects Units Editor
Mockup](https://picasaweb.google.com/lh/photo/Yt8-LgZjQx2HIyn7nJ2O5Q)

Mockup of Effect-Chain Compact Interface. Only MetaKnobs are showing.
[[/media/effects-chains-mockup.png|]]

## Controller Impact Assessment

**TODO: Need to formalize what "Fit" means.** In general, a fit is good
if it matches the paradigm of effect-chains being

  - Selectable (usually with an FX select knob or button)
  - Controllable via 1 single parameter (usually a knob)
  - Allow selection of Decks that an effect-chain applies to either
    directly in the effects section or in the mixer section.
  - Optionally, enable via on/off button
  - Optionally, a wet/dry effect mix knob

| Controller                                                                                                                                                              | Effects? | Settings                                                                                                                                                                                                                                                            | Fit?           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [American Audio VMS4](http://www.digitaldjtips.com/wp-content/uploads/2010/11/american-audio-vms4.jpg)                                                                  | Y        | Per-deck effect-select knob, effect parameter knob, effect enable button, parameter toggle button?                                                                                                                                                                  | Good           |
| [Behringer BCD3000](http://www.digitaldjtips.com/wp-content/uploads/2010/11/behringer-bcd3000.jpg)                                                                      | Y        | 4-effect parameter knobs plus on/off button, FX select up/down buttons, and "action" button                                                                                                                                                                         | Good           |
| [Denon DN-MC6000](http://www.clynemedia.com/D_and_M/Denon_DJ/DN_MC6000/DN-MC6000_Top.jpg)                                                                               | Y        | Per-deck 4-effect parameter knob plus on/off button. Per-deck FX select for FX unit 1 and 2                                                                                                                                                                         | Good           |
| [Gemini CTRL-47](http://www.infomusic.pl/img/artykuly/zdjecia/2kgaXCd8IiMC45NDE2NjUwMCAxMjk1NTE4MDg1.jpg)                                                               | Y        | Per-deck 2 effects controls. Each control has FX select and 2 parameter knobs plus on/off button.                                                                                                                                                                   | Good           |
| [Hercules DJ Console RMX](http://www.skratchworx.com/images/hercules/rmx_top.jpg)                                                                                       | N        |                                                                                                                                                                                                                                                                     | N/A            |
| [Hercules DJ Console 4MX](http://www.dv247.com/assets/products/79891_l.jpg)                                                                                             | N        |                                                                                                                                                                                                                                                                     | N/A            |
| [Hercules DJ 4set](http://img.clubic.com/03913828-photo-hercules-dj-4set-3.jpg)                                                                                         | N        |                                                                                                                                                                                                                                                                     | N/A            |
| [Hercules DJ Console Mk4](http://maxborgesagency.com/wp-content/uploads/4780638-Hercules-DJConsole-Mk4-Top.jpg)                                                         | N        |                                                                                                                                                                                                                                                                     | N/A            |
| [Hercules DJ Control Steel](http://www.madmanaudio.com/images/madmanaudio%20%20Hercules%20DJ%20Control%20Steel%20Controller.jpg)                                        | N        |                                                                                                                                                                                                                                                                     | N/A            |
| [Hercules DJ Control MP3 e2](http://bestmixtrackreviews.com/blog/wp-content/themes/guitarreviewtheme/wordpressreviewtheme%20v1.4/images/hercules-dj-control-mp3-e2.jpg) | N        |                                                                                                                                                                                                                                                                     | N/A            |
| [M-Audio Torq Xponent](http://cachepe.samedaymusic.com/media/quality,85/brand,sameday/xponent_top-15f5539b4b7c7f1cad233509e0bfa895.jpg)                                 | Y        | 4 effect parameter knob + 4 enabled buttons per deck                                                                                                                                                                                                                | Medium         |
| [NI Traktor Kontrol S4](http://cachepe.zzounds.com/media/quality,85/brand,zzounds/NI_Traktor_Kontrol_S4_top-a19738755dd69761d1fb33f0e8ec7cad.jpg)                       | Y        | Per chain: 1 dry/wet knob, 3 effect parameter knobs, 1 chain on/off button, 3 effect option buttons, menu button (?). Per-deck effect chain (2x) enable buttons                                                                                                     | Good           |
| [NI Traktor Kontrol X1](http://turntabling.net/wp-content/uploads/2011/01/NI-TRAKTOR_KONTROL_X1_Controller.jpg)                                                         | Y        | Per chain: 1 dry/wet knob, 3 effect parameter knobs, 1 chain on/off button, 3 effect option buttons. Per-deck effect chain (2x) enable buttons                                                                                                                      | Good           |
| [Numark MIXTRACK](http://www.gearnuts.com/images/closeup/xl/1600-Mixtrack_top.jpg)                                                                                      | Y        | Per-deck effect enable, effect select knob, 2x parameter knob                                                                                                                                                                                                       | **Perfect**    |
| [Numark NS6](http://www.numark.com/stuff/contentmgr/files/27/54855ae10ce78345971f892114788cfd/large/ns6_ortho_lrg.jpg)                                                  | Y        | Per-deck effect selector, parameter, mix, source knobs. Effect on/off and tap buttons.                                                                                                                                                                              | **Perfect**    |
| [Numark NS7](http://www.meramani.com/bigpic/496/497/20091121015820.jpg)                                                                                                 | N        |                                                                                                                                                                                                                                                                     | N/A            |
| [Numark NSFX](http://www.tamtamonline.com/media/catalog/product/cache/3/image/5e06319eda06f020e43594a9c230972d/n/u/numark-nsfx.jpg)                                     | Y        | Per-deck effect selector, parameter, mix, source knobs. Effect on/off and tap buttons.                                                                                                                                                                              | **Perfect**    |
| [Numark V7](http://www.numark.com/stuff/contentmgr/files/24/830107e06e04bbc75e07e04e08a48e01/large/v7_top_lg.jpg)                                                       | Y        | Effect selector, parameter knobs. Effect Mix fader, Effect on/off button and tap buttons                                                                                                                                                                            | **Perfect**    |
| [Pioneer DDJ-S1](http://createdigitalmusic.com/files/2011/01/ddjs1.jpg)                                                                                                 | Y        | Serator ITCH style. Per-deck effect selector, parameter, mix, source knobs. Effect on/off and tap buttons.                                                                                                                                                          | **Perfect**    |
| [Pioneer DDJ-T1](http://createdigitalmusic.com/files/2011/01/ddjt1.jpg)                                                                                                 | Y        | Traktor style. 2 effects units. Per unit dry/wet, 3 parameters per unit, each with on/off buttons. Effect 1/2/3 select buttons. Advanced/Chained toggle button. Random button associated with the Dry/Wet knob. FX Unit selectors on the EQ section for FX unit 1/2 | Good           |
| [Reloop Digital Jockey 2](http://www.digitaldjtips.com/wp-content/uploads/2010/11/reloop-digital-jockey-2-master-edition.jpg)                                           | Y        | 3 effect enable/select/parameter knobs per deck                                                                                                                                                                                                                     | Medium         |
| [Reloop Digital Jockey 3 Master Edition](http://www.notape.net/files/eqs4/direop0013/DIREOP0013-b2823d9.jpg)                                                            | Y        | Effect enable/select/parameter knob for 2 effects units. 4 FX enable buttons for each deck.                                                                                                                                                                         | Medium         |
| [Stanton SCS.1d](http://qualityelectronics.net/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/c/scs1d_top.jpg)                                  | Y        | Four re-defineable pressable endless knobs each with LED rings, 8-char LCDs, and soft button, plus bank button and preset button section                                                                                                                            | **Perfect+++** |
| [Stanton SCS.1m](http://www.stantondj.com/pics/products/controllers-systems/lg-controllers/scs1m-front-lg.jpg)                                                          | Y        | Four re-defineable pressable endless knobs each with LED rings and 8-char LCDs, plus preset button section                                                                                                                                                          | **Perfect++**  |
| [Stanton SCS.3d](http://cachepe.samedaymusic.com/media/quality,85/brand,sameday/scs3d_top-884b39d66a53f1ba4cbe077d4840096f.jpg)                                         | Y        | Three pages each with three relative or absolute touch sliders (or one jog and one slider) and four soft buttons                                                                                                                                                    | **Perfect+**   |
| [Stanton SCS.3m](http://cachepe.zzounds.com/media/quality,85/brand,zzounds/scs3m_top_clipped-582ff9b8832ee7376a5b96cb8e37484e.jpg)                                      | Y        | Four touch sliders (relative or absolute) in FX mode plus four soft buttons, per deck                                                                                                                                                                               | **Perfect**    |
| [Vestax Spin](http://www.algoriddim.com/press/vestax-spin-top.jpg)                                                                                                      | Y        | 2 FX enabled buttons?? WTF                                                                                                                                                                                                                                          | Medium         |
| [Vestax Typhoon](http://www.agiprodj.com/images/vestax-typhoon-top-popup.jpg)                                                                                           | Y        | 2 wet/dry knobs + enabled buttons                                                                                                                                                                                                                                   | Good           |
| [Vestax VCI-100SE DJTT Edition](http://img183.imageshack.us/f/vci100seoverlay.png/)                                                                                     | Y        | Wet-dry, 3-effect parameter knobs per effects unit                                                                                                                                                                                                                  | Medium         |
| [Vestax VCI-100 MK2](http://www.keymusic.com/gfx_productcode/XL/98937/Vestax-VCI100-MK2-Silver.jpg)                                                                     | Y        | 2 effects units, 4 knobs per unit and 4 buttons. FX enable in the mixer section. Shift key addresses up to 4 effects units.                                                                                                                                         | Good           |
| [Vestax VCI-300](http://snatchthieves.files.wordpress.com/2010/07/vestax-vci-300.jpg)                                                                                   | N        |                                                                                                                                                                                                                                                                     | N/A            |
| [Xone:DX](http://blog.starproductions.com/wp-content/uploads/2009/12/xone_dx_very_big.jpg)                                                                              | Y        | Per-deck dry/wet, 3x parameter, knobs. Source select, on/off, tap, beats/free, and effect-select buttons.                                                                                                                                                           | Good           |

## Work Breakdown

1.  ~~Implement effect representation~~
    1.  ~~EffectManifest and its properties~~
        1.  ~~EffectManifestParameter and its properties~~
    2.  ~~Effect~~ 
2.  Implement backend framework classes
    1.  ~~EffectsBackend Interface~~
        1.  ~~Enumeration of EffectManifests~~
        2.  ~~Instantiation of Effects~~
    2.  Native Backend
        1.  Add backend to EffectsManager
        2.  Implement a bunch of cool effects
            1.  ~~Port Flanger from EngineFlanger to NativeBackend~~
            2.  Delay / Tape Echo
            3.  Stutter
            4.  Backspin
            5.  HPF / LPF
            6.  Bitcrusher
            7.  Gater
3.  Implement control layer
    1.  ~~EffectChain~~
        1.  ~~Control Interface~~
        2.  ~~EffectSlot lifecycle~~
        3.  ~~Effect loading/unloading logic~~
        4.  ~~Parameter sync between controls and loaded effect~~
        5.  Units tests for consistency of controls / state
    2.  ~~EffectSlot~~
        1.  ~~Control Interface~~
        2.  ~~EffectSlotParameter lifecycle~~
        3.  ~~Parameter sync between controls and loaded effect~~
        4.  Units tests for consistency of controls / state
    3.  ~~EffectSlotParameter~~ 
        1.  ~~Control Interface~~
        2.  ~~Effect loading/unloading logic~~
        3.  ~~Parameter sync between controls and loaded effect~~
        4.  Units tests for consistency of controls / state
4.  ~~Implement Engine representations of the control layer.~~
    1.  ~~TwoWayMessagePipe for sending EffectsRequest and
        EffectsResponse messages~~
    2.  ~~EngineEffectChain~~
    3.  ~~EngineEffect~~
    4.  ~~EngineEffectParameter~~
5.  Implement overall effect management layer
    1.  ~~EffectsManager~~
        1.  ~~Adding, management of lifecycle of EffectsBackends~~
        2.  ~~Adding, management of lifecycle of EffectChains~~
        3.  ~~Check that EffectManifest/EffectManifestParameter,
            Effect/EffectParameter,
            EffectChain/EffectSlot/EffectSlotParameter all get deleted~~
    2.  Preset Management
        1.  Implement loading/saving of EffectChain presets
        2.  Implement next/prev logic for EffectChains
6.  Implement EffectChain parameter linking
    1.  EffectSlotParameter's can be linked to the EffectChain's
        parameter
    2.  Propagate changes in the EffectChain's parameter to
        EffectSlotParameters that are connected to it
7.  ~~Implement actual audio processing~~ 
    1.  ~~EngineEffectChain processing~~
        1.  ~~INSERT/SEND processing~~
        2.  ~~DRY/WET proportional mixing~~
        3.  ~~enable/disable~~
        4.  ~~enable/disable per group~~
        5.  ~~ramping gain when enabled/disabled~~
    2.  ~~EngineEffect processing~~
    3.  ~~Engine/EngineChannel requests effect-chains enabled for a
        given channel as it processes them~~ 
    4.  ~~Engine/EngineChannel applies appropriate effect chains to
        buffers of audio that are enabled~~
    5.  Pre-fader vs. Post-fader processing
    6.  EffectParameter interpolation utilities for implementing Effect
        processing
8.  GUI Widgets
    1.  ~~EffectChain name widget~~
        1.  ~~Shows the name of the EffectChain that is loaded into
            EffectChainSlot X~~
    2.  EffectChain Editor Library section
        1.  See existing chain presets
        2.  Create new preset
        3.  Add/remove effect to existing chain
        4.  Change value of parameter of effect in slot
        5.  Right-click hover overlay for tweaking ranges, defaults.

## Current Progress

This feature has been attempted twice by two GSoC students. There is a
lot of old code lying around, and we will try to reuse whenever
possible. The current branch for work on this feature is the
[features\_effects](https://github.com/rryan/mixxx/tree/features_effects)
branch.

## Team

  - RJ Ryan

## Comments

### Lambolico's ideas:

It would be really cool if effects chains could be configured via a
script file, similar to midi mappings: you can configure your controller
using the options menu or with a script/xml files. This way we could
pre-configure sequences of effects and many more crazy things to be
controlled with few buttons or knobs, much like the wonderknob idea but
not limited to it.

For example, we could get things like a delay style build-up effect
controlled with a single button: when the button is pressed once, the
build-up effect starts; when the button is pressed again, the input to
the effect closes so the effect freezes; and finally when the effect
button is pressed a third time, the input opens again with a smooth
reverb effect that fades away gently.

Moreover, if the effects script could access to the song's clock, it
could be automated in ordre to go through this steps according to the
song's bars. So pressing the effect's button after the drop, 4 bars
before the beat starts, would execute this sequence of effects just to
perfectly enhance the song when the beat kicks again.

Another simpler example: maybe we want to control a complex effects
combination with a wonderknob but want to have a freeze button or a
specific parameter to be control independently.

I thought that a way to combine this flexibility with the skins is to
have a set of "dummy" knobs with a couple of buttons under each of them
(similar to the mockups above) that could pass their value/state to an
effects script function. This would be the same with midi controls.

To sum up: to have the horsepower of scripting with effects in addition
to this other great ideas you had.

### DJ Barney's ideas:

I wonder if the industry standard way of doing this has been considered
?

<http://www.ehow.com/about_6323793_fx-send-control_.html>

Mixxx can have built in FX, as of course many hardware DJ mixers already
have. Those hardware mixers often also have FX Send and Receive. Could
Mixxx have that tied into this feature as well ? That may also allow
more complex set-ups like scripting using possibly an OSC/MIDI routing
to external FX units (hardware and software one's). Handing off other
features to external units may allow better focus on the built in FX
(Mixxx custom filters, plus plugins).

Pre and Post fader is also important as that determines if the FX just
cuts off when turned off, or if it slowly fades away when turned off -
as an Echo or Reverb filter will do.

\#\#\#\#
