# Updating Controller Configurations for 2.0

## Sync Buttons

(Groups stay as `[ChannelX]`)

Name goes from `beatsync` to `sync_enabled`. Devs should test
push-and-hold for enabling master sync.

## Filter Knob

If the controller has a dedicated "filter knob", it should be set to:
`[QuickEffectRack1_[ChannelX]],super1`

## Button LEDs

Update these to ensure GUI sync.

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

This is very hard, and we may change how we do this. The VCI400 has two
effects sections, so I did the following:

Individual knobs adjust parameters for that effect unit:
\[EffectRack1\_EffectUnitX\_Effect1\],parameterY. Where X is 1 or 2 (the
two effects sections), and Y is 1,2,3 (the three knobs).

Wet/dry is: \[EffectRack1\_EffectUnitX\],mix (fourth knob in each
section)

Per-channel buttons to activate a FX unit on that channel:
\[EffectRack1\_EffectUnitX\],group\_\[ChannelY\]\_enable

Changing which effect is loaded in a section:
\[EffectRack1\_EffectUnitX\],next\_chain
