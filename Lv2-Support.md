# LV2 support

Mixxx has now basic LV2 native support. The advantage of native LV2
integration is that every user can benefit from it, it works seamlessly
with Mixxx, no tweaks are required to make it functional. The normal
user won't see a diference between native effects and LV2 ones. Here is
the PR for LV2 support: <https://github.com/mixxxdj/mixxx/pull/316>

Pending issues (thanks Daniel for the ideas):  

  - Blacklist: We need to be able to blacklist plugins which are known
    to be useless for Mixxx like "Stereo to MS"
  - We need also an option to hide plugins from the GUI because they
    will not be used by the DJ (Nicu: isn't this the same as
    blacklisting a plugin?)
  - The same for the Parameters. We need an option to hide unwanted
    parameter knobs
  - We need a "More" popup for plugin with more than 8 useful parameters
  - We need a widget that deal with long effect or button names
  - The LV2 plugins in preferences should be listed in a list view
  - It should contain an "Info" button displaying exactly the info that
    is displayed by lv2info from the lilv2-utils package

### Developer's point of view

The steps towards basic LV2 integration are the following (I must thank
Ryan for his detailed description):

``` 
 * Create an LV2Backend class which inherits from EffectsBackend
   * This backend class is responsible for enumerating (finding) and instantiating effects
   * Source files: //src/effects/lv2/lv2backend.[cpp,h]//
 * Create a new class which receives an LV2 plugin manifest, parses it and obtains a Mixxx EffectManifest
   * This is an important step because Mixxx relies on EffectManifests when creating slots for effects and its parameters
   * Source files: //src/effects/lv2/lv2manifest.[cpp,h]//
 * Add an LV2 effect wrapper class
   * It has to send parameter updates to the plug in instantiation as well as processing audio samples using the plug in.
   * Source files: //src/effects/lv2/lv2effectprocessor.[cpp,h]//
 * Add a specialized instantiator for LV2 effects. It inherits from ''EffectInstatiator''
   * Class name: ''LV2EffectProcessorInstantiator''
      * Its responsibility is to pass information to ''LV2EffectProcessor'':
         * an //EngineEffect*//
         * a //LilvPlugin*//
         * two lists with audio and control port indices
   * Source file: //src/effects/effectinstantiator.h//
```

Below is a diagram of the LV2 architecture:  
[[/media/lv2_architecture.jpg|]]

For the first step (parsing the LV2 plugin manifest into an
EffectManifest) I used *lilv*. It is the recommended way for hosts to
add LV2 support. Audacity is already using it. Here are some useful lilv
functions:

  - Create the *world* which is responsible for plug in discovery
  - LilvWorld\* lilv\_world\_new();
  - Load all available plug ins
  - void lilv\_world\_load\_all(LilvWorld\*);
  - Get the loaded plug ins
  - const LilvPlugins\* lilv\_world\_get\_all\_plugins(LilvWorld\*);
  - Iterate through them
  - LILV\_FOREACH(plugins, iter, container);
  - *plugins* is a keyword, lilv's FOREACH macro takes into account this
    keyword and knows to call lilv\_*plugins*\_\* functions
  - Get the name of a plugin
  - LilvNode\* lilv\_plugin\_get\_name(const LilvPlugin\*);
  - const char\* lilv\_node\_as\_string(LilvNode\*);

##### Useful information for skin developers:

A new tag for buttons used inside the effects framework was introduced,
`EffectPushButton`. It shall be used by skin developers when they create
a new skin. It supports multi state parameters (LV2 enumeration
parameters) through a multi state button. States can be changed either
by left clicking on the button or by right clicking on it and choosing
an option from the menu. The config key for the newly added button
paramters has the following form:
`[EffectRackX_EffectUnitX_EffectX],button_parameterX`

  
  

### User's point of view

The user can run LV2 effects which are using stereo input / output audio
samples and don't require any features (examples: kn0ck0ut, Calf Phaser,
Calf Flanger, SWH karaoke, etc.). All he has to do is install the
desired LV2 plugin.

Here are some features our current implementation supports:

  - pop up menu display of available options for enumeration parameters
  - LV2 preferences menu
  - displays the discovered LV2 plugins
  - displays the reason why a plugin is disabled
  - lets the user select up to 8 parameters and button parameters to be
    displayed inside the skin
