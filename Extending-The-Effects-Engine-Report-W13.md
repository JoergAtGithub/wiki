Hello,

During this week I worked on adding two new features to LV2 support
branch. One of them was displaying why an LV2 plugin is not available,
more specifically, why the button for a specific plugin is disabled
inside LV2 Preferences. In order to do this, I did some refactoring
inside `LV2Backend` class. Previously, only the valid LV2 plugins were
added to `LV2Backend::m_registeredEffects` and `getEffectIds()` returned
`m_registeredEffects.keys().toSet()`. Information about all the
discovered plugins was stored in a separate list which was built inside
`enumeratePlugins()`. The major flaw with this desing was that
information about plugins which were not valid could be stored only when
the list was built. I solved this issue by adding all the discovered
plugins to `LV2Backend::m_registeredEffects`, even if they were not
valid. This way, we have access to a plugin's `EffectManifest` and
`LV2Manifest` from the backend regardless if the plugin is valid or not.
`getEffectIds()` method was modified to return only the valid LV2
Effects, because effect instantiation is based on it. Another method
which returns all the discovered plugins' IDs was used inside LV2
Preferences. `LV2Manifest` was modified too, it now features a new
private `Status` field which is set upon manifest's construction.
`Status` is an enum with the following options:

  - AVAILABLE --\> the plugin is valid
  - IO\_NOT\_STEREO --\> the plugin is not valid because input and
    output samples are not in stereo format
  - HAS\_REQUIRED\_FEATURES --\> the plugin is not valid becuase it
    requires some features we are not currently supported

Inside `dlgpreflv2.cpp` I cycled through the discovered LV2 plugins,
extracted the `LV2Manfiest` and set a tooltip for plugins which were not
valid based on their `Status`.

A nice small addition was using the LV2 logo as an icon for LV2
Preferences.

The second feature I added was remembering the selected parameters and
button paramters for each LV2 plugin across Mixxx's lifetime. Before
this feature, every time we wanted to modify the displayed parameters
for an effect we had to do it from scratch, because all check boxes were
empty. This was an issue because the menu was misleading the user into
thinking that no parameters were displayed for that effect. In fact, the
first 8 parameters and button parameters were active. Now everything
works as expected:

  - if an effect's settings were not modified, the first 8 parameters
    and button parameters are checked;
  - if the user modifies an effect's settings: the next time he will
    attempt to modify the same effect's settings, the previously
    selected paramters are checked.

I also worked together with Daniel on improving the Graphic EQ Effect.
We had some problems because the equalizer was not flat and bit perfect
when the filters were in neutral position. Thanks to Daniel who found
the "magic" center frequencies for the filters, the effect seems to be
working as it should. If we decide the equalizer based on these filters
(low shelving, high shelving, peaking biquad) is good, we can easily
create a 3 band or a 20 band version of it.

I polished the EQ Rack branch by removing debug comments across the code
and making it ready for merging (fixed conflicts with master). These are
the ideas behind the EQ Rack:

  - another EffectRack is added which dynamically gets populated with
    EffectChains, each time the control responsible for the number of
    decks is changed
  - each EffectChain contains only one EffectSlot, is set to fully wet
    and is active on a specific \[Channel\];
  - inside Equalizer Preferences we can choose which EQ Effect should be
    active on each Deck
  - skins don't need to be modified because aliases are created
    dynamically when the number of decks is changed
  - example: "\[ChannelX\],filterLow" is an alias for
    "\[EffectRackY\_EffectUnitX\_Effect1\],parameter1", where Y is the
    index of the last Effect Rack (the EQ Rack)
  - the "Bypass" check box is equivalent to loading an empty effect on
    the EQ Effect spot for each Deck
  - a nice feature is offering the advanced user the possibility to load
    any available effect on the EQ Effect spot; this is done via a "Show
    all effects" check box
  - `EngineFilterBlock` is no longer used because all sound processing
    is done by the `EngineEffectsManager`

LV2 support summary:

  - can run LV2 effects which are using stereo input / output audio
    samples and don't require any features (examples: kn0ck0ut, Calf
    Phaser, Calf Flanger, SWH karaoke, etc.)
  - pop up menu display of available options for enumeration parameters
  - LV2 preferences menu
  - displays the discovered LV2 plugins
  - displays the reason why a plugin is disabled
  - lets the user select up to 8 parameters and button parameters to be
    displayed inside the skin

Google Summer of Code has come to an end. It was a great experience for
me and if I were to choose I'd do it all over again. I've learned a lot
of new useful things, including both the technical and the soft skills
required for working on an open source project. I am highly indebted to
my mentor Daniel for constantly watching my back and giving precious
advice to me. I also want to thank the entire Mixxx community for
supporting me. I will continue contributing to Mixxx because a lot of
fun new stuff lies ahead. Thank you\!

Yours sincerely,  
Nicu Badescu  
  
[Back to the main page\!](extending_the_effects_engine)
