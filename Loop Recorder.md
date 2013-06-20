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

There are many possible options for an implementation of a loop
recorder---everything from simple recording one section of audio into a
sample that repeats to a fully realized remix and slicing engine. As
Mixxx is targeted to both beginning and advanced DJs, the best approach
for a loop recorder in Mixxx is to create a very simple interface that
is easy to understand and use for beginning users, but that can be
combined with existing functionality (such as samplers) to give
professional users plenty of power and flexibility. Considering the
fairly limited time for GSoC and the complexity of the project, the
simpler the approach that I take is, the likelier it is that I’ll have a
polished product by the end of the Summer that DJs will actually be able
to use.

A loop recorder offers DJs several creative possibilities:

1\. Create new songs using existing loop libraries, by layering them
together.

Example: DJ B has a set of loops that she’d like to combine into a new
mix. She knows that there are a couple different grooves that she would
like to use throughout the song. She loads several loops into samplers
to create the basic groove for the first section of the song. She starts
recording the loop through the headphone out and records 16 beats into
the loop recorder. She adds several layers to the groove, then saves the
loop, loads it into a main deck and starts playing, while that's playing
she repeats the process for a several new grooves, until she has a
couple of different sections, which she transitions between to develop
the song. She uses more samplers to add extra layers and develop each
section.

2\. Make mashups/remixes on the fly by recording and layering loops from
several different songs/loop libraries.

DJ X has several different sections from different songs that he knows
he'd like to combine later in his set. While these songs are playing X
records segments from main output to the loop recorder and saves each
section he'd like to use. During the set he can also process and
recombine some of the recorded loops by using the cue output and
different signal processing. When the time comes to use the loops he can
load them into samplers to play them back.

3\. Create one-shot items from a song or loop on the fly to be triggered
by either a hot key (probably in a sampler deck in Mixxx).

### Requirements

  - Realtime Recording/Instant Playback
  - Loop is available to playback immediately
  - Multi-layer recording
  - Record unlimited number of layers in loop recorder (in practice it
    probably )
  - One level of undo/redo
  - Syncs with currently defined BPM (Merge with Owen's master sync
    branch?)
  - Export to library/disk
  - Save to disk
  - Export metadata to library
  - Export directly to samplers? - Useful for quick mixing

<!-- end list -->

``` 
    * Perhaps also work on code to record directly into samplers - separate from loop recorder, but related, this may be a good starting point for the project...
* GUI
* Simple to use and understand
* Incorporates with 
```

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

1.  Improve [developer documentation](developer_guide) for audio engine
    as I learn more about it.

## Current Progress

## Team

  - Carl Pillot (GSoC 2013 Student)
  - Owen Williams (GSoC 2013 Mentor)

## Comments
