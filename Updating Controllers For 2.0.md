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

??? This is hard -- we went from one built-in effect to multiple racks
and things

## Master Sync Button

Should be called "sync\_enabled". Devs should test push-and-hold for
enabling master sync.
