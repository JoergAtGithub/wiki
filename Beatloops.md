## Summary

**Status**: There is a branch which has most of these features
implemented. Testing is still needed.

Mixxx has BPM detection but not beat detection. Beat detection would
allow us to do man cool tricks including:

  - Jump from beat to beat
  - Quantize Effects
  - Create Beat Quantized loops
  - Do full Automatic Beat Syncing
  - Beat Smashing/Splicing (ala Aphex Twin)

## Current Status

There is currently a branch at
<https://code.launchpad.net/~mixxxdevelopers/mixxx/features_trackbeats>.

Current Status:

  - \[ChannelN\],beatloop CO implemented
  - I've also implemented \[ChannelN\],beatloop\_(SIZE) CO's for skins.
    Need to reimplement a thread safe version of QSignalMapper.
  - \[ChannelN\],beatseek CO implemented (untested)

## Design

Most of these features use Engine Controls which interact and
communicate amongst each other. Beat loops, for instance, are done by
querying the track's beats and then setting the loop in and loop out
positions with that information.

### Beat loops

I use both a straight \[ChannelN\],beatloop CO which will take the
argument in set as the number of beats the loop should have. Fractional
and negative values work.

The behaviour of beat loops varies whether or not the value is above or
below zero (absolute) and whether it is positive or negative.

  - If the number is not a fraction and is positive it will create a
    loop starting at the next loop and ending N loops after.
  - if it is a fraction it will end the loop at a fraction of the beat's
    length after the next beat.
  - If the number is negative it will set the end of the loop at the
    next beat and the beginning at N beats before.
  - if it is a fraction it will begin the loop at a fraction of the
    beat's length before the next beat.

### Beat Seeking

Beat seeking is done by calling the \[ChannelN\],beatseek CO and setting
the value to the number of beats to jump. The jump will occur on the
next beat.

### Quantization for Loops, Cues & Hotcues

I have added a new Engine Control; QuantizeControl, which has the
following CO's:

  - \[ChannelN\],quantize: enables quantization on the deck.
  - \[ChannelN\],quantize\_beat: is always set as the next beat if
    quantization is enabled.

It also has a pushbutton, for skins; \[ChannelN\],quantize\_enable.

These CO's are then queried when setting up loop points and cues. If
quantization is enabled, ie: \[ChannelN\],quantize == 1.0, then the
function queries \[ChannelN\],quantize\_beat and uses that as it's new
position instead of the current play position.

## Current Issues

None that I know of (madjester).

## Notes

  - We could easily avoid the CPU and time penalty for analysis by only
    using aubio in the analysis section.
  - Although the implementation so far deals with beat detection and
    quantization aubio also does other forms of analysis.
  - We could color waveforms on peaks (onset detection)
  - We could color waveforms according to pitch (pitch detection)
