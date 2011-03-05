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

Currently it does:

  - Rendering of the Beats on the Waveform
  - Saving Tracked beats (column in library table as a bitmap)

Using the features to quantize cues, hotcues and loops is done by the
branch features\_beatcontrols;
<https://code.launchpad.net/~mixxxdevelopers/mixxx/features_beatcontrols>.

## Design

## Current Issues

  - ~~TrackInfoBeats is not stored in the Database~~ Implemented in the
    latest changes.
  - Analysis takes 90%+ CPU and around 15 seconds for a typical
    Psytrance Song (not good for live performance).

## Notes

  - We could easily avoid the CPU and time penalty for analysis by only
    using aubio in the analysis section.
  - Although the implementation so far deals with beat detection and
    quantization aubio also does other forms of analysis.
  - We could color waveforms on peaks (onset detection)
  - We could color waveforms according to pitch (pitch detection)
