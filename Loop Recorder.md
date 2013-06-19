## Summary

**Status**: This specification is **in drafting**, however active work
will begin immediately and continue through the summer. Please feel free
to leave comments.

DJs often may wish to record loops and samples live from available
output streams, which can then be used again in samplers and the main
decks to play back later. This project aims to implement an easy to use,
but powerful loop recorder for Mixxx, which will give DJs another tool
to be creative in their live mixes.

This project is being undertaken by Carl Pillot for the Google Summer of
Code 2013.

## Design

### High-Level Overview

### Requirements

### Engine Modifications

### Controls

### User Interface

## Work Breakdown

1.  Core Loop Code
    1.  Loop Recorder Manager
        1.  Connections to UI controls
        2.  Connect signals between controls, LoopRecorder and
            LoopPlayer
        3.  Export to library handling
            1.  Database metadata storage
            2.  Save audio data to file (can probably reuse some of the
                existing codebase for this)
    2.  Loop Recorder
        1.  Buffer Processing (recording and layering)
        2.  Undo Operations 
        3.  Clear operations
        4.  BPM Matching
    3.  Loop Player (EngineChannel subclass)
        1.  Read audio from buffers and implement switching between the
            buffers.
        2.  Integrate with Engine Master, so that audio is routed back
            into the mix after it is recording.
        3.  Slots for receiving updates from loop recorder and manager
        4.  New SoundSource class for internally recorded sounds. (Maybe
            should be classified as a separate entity in the structure)
2.  GUI integration
    1.  Theme modifications
    2.  New loop table view for saved loops (could be added as a section
        in the recordings view)
3.  Documentation
    1.  New manual entry for loop recorder

Extras:

1.  Improve Documentation on web for audio engine as I learn more about
    it.

## Current Progress

## Team

  - Carl Pillot (GSoC 2013 Student)
  - Owen Williams (GSoC 2013 Mentor)

## Comments
