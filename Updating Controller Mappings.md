This page has information for updating old controller mappings for the
latest version of Mixxx.

# Mixxx 2.3

Support for [colored hotcues](MIDI%20scripting#color%20API) was added.
Intro & outro cues were added too. These can be mapped the same way as
hotcues. Refer to [MixxxControls](MixxxControls) for details.

# Mixxx 2.2

There were no changes to the controller mapping system between Mixxx 2.1
and Mixxx 2.2.

# Mixxx 2.1

  - `engine.setParameter()` now works with `engine.softTakeover()`. If
    your script implemented its own soft takeover mechanism to get
    around that bug, change it to use Mixxx's soft takeover solution
    instead.
  - MIDI input handling functions are now called with the appropriate
    `this` object (instead of `this` being set to the global object),
    allowing script files to be written with a more object oriented
    organization.
  - Metaknobs, which act like superknobs for each effect within a chain,
    were introduced. Also, a new framework for focusing individual
    effects within a chain was introduced. Focusing an effect does not
    do anything by itself; it is up to controller mappings to do
    something different depending on the focused effect. The show\_focus
    ControlObject of an EffectUnit needs to be set to 1 for the focus to
    be shown in skins. Refer to [Mixxxcontrols\#Effects
    framework](Mixxxcontrols#Effects%20framework) for details.
  - [Components JS](Components%20JS) library was introduced to make
    writing JavaScript mappings easier. It provides an [Components
    JS\#EffectUnit](Components%20JS#EffectUnit) object that makes it
    easy to map the new effects interface to the common layout of 4
    knobs (or 3 knobs + 1 encoder) + 4 buttons for controlling effects
  - New [MixxxControls](MixxxControls) for looping and beatjumping were
    introduced. If your mapping has buttons mapped to fixed loop sizes,
    update it to use beatloop\_activate and beatlooproll\_activate.
    Replace reloop\_exit with reloop\_toggle, and add a mapping for the
    new reloop\_andstop Control. Replace loop\_move\_X\_forward/backward
    with beatjumping, which now acts to move the loop if there is a loop
    enabled.
  - TODO: document new library navigation interface
  - A new \[ChannelX\], track\_loaded ControlObject was added. If your
    script previously used track\_samples to detect if a track was
    loaded, switch to the more readable track\_loaded.
  - `<key>` elements in XML that are bound to script functions can now
    be any JavaScript expression that evaluates to a function in the
    global context. Just because you can embed a JavaScript function in
    the XML file does not mean you should though.

# Mixxx 2.0

Also see [Getting Ready for Mixxx 1.12](getting_ready_for_112)

## Sync Buttons

(Groups stay as `[ChannelX]`)

Name goes from `beatsync` to `sync_enabled`. Devs should test
push-and-hold for enabling master sync.

## Filter Knob

If the controller has a dedicated "filter knob", it should be set to:
`[QuickEffectRack1_[ChannelX]],super1`

## Button LEDs

Update these to ensure GUI sync with the different Cue modes in the
preferences.

(Groups stay as `[ChannelX]`)

Name goes from:

  - `cue_default` to `cue_indicator`
  - `play` to `play_indicator`

## Filter Control Objects

Group goes from `[ChannelX]` to `[EqualizerRack1_[ChannelX]_Effect1]`

Name goes from:

  - `filterLow` to `parameter1`
  - `filterMid` to `parameter2`
  - `filterHigh` to `parameter3`
  - `filterLowKill` to `button_parameter1`
  - `filterMidKill` to `button_parameter2`
  - `filterHighKill` to `button_parameter3`

## Effects Control Objects

(These replace `[Flanger]` group controls.)

Full list is on the [effects framework](effects_framework#controls)
page.

The VCI400 has two effects sections, so I did the following:

### Parameter adjustment

Individual knobs adjust parameters for that effect unit:
`[EffectRack1_EffectUnitX_Effect1],parameterY`. Where X is 1 or 2 (the
two effects sections), and Y is 1,2,3 (the three knobs).

If your controller has only one "parameter" knob, you can map it to
`[EffectRack1_EffectUnitX],super1` which will modify a number of effect
parameters at once. (Sean did this for the ADJ VMS4.)

### Wet/dry

Wet/dry is: `[EffectRack1_EffectUnitX],mix` (fourth knob in each
section)

### Activation

Per-channel buttons to activate a FX unit on that channel:
`[EffectRack1_EffectUnitX],group_[ChannelY]_enable`

### Change effect

Changing which effect is loaded in a section:
`[EffectRack1_EffectUnitX],next_chain`
