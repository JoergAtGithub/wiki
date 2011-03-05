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

## Design

## Current Issues

  - ~~TrackInfoBeats is not stored in the Database~~ Implemented in the
    latest changes.
  - Analysis takes 90%+ CPU and around 15 seconds for a typical
    Psytrance Song (not good for live performance).
  - There is no fallback implementation to fill in TrackInfoBeats with
    SoundTouch.
