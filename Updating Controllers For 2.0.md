# Updating Controller Configurations for 2.0

## Filter Control Objects

Group goes from "\[ChannelX\]" to
"\[EqualizerRack1\_\[ChannelX\]\_Effect1\]"

Name goes from:

  - filterLow to parameter1
  - filterMid to parameter2
  - filterHigh to parameter3
  - filterLowKill to button\_parameter1
  - filterMidKill to button\_parameter2
  - filterHighKill to button\_parameter3

## Effects Control Objects

This is very hard, and we may change how we do this. The VCI400 has two
effects sections, so I did the following:

Individual knobs adjust parameters for the first effect:
\[EffectRack1\_EffectUnitX\_Effect1\],parameterY. Where X is 1 or 2, and
Y is 1,2,3.

Wet/dry is: \[EffectRack1\_EffectUnitX\],mix

## Master Sync Button

Should be called "sync\_enabled". Devs should test push-and-hold for
enabling master sync.

## Filter Knob

If the controller has a dedicated "filter knob", it should be set to:
\[QuickEffectRack1\_\[ChannelX\]\],super1
