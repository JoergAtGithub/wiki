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

#### Behavior:

When a DJ clicks record for the first time the loop recorder locks the
beat number menu, so that it cannot be changed. This is necessary to
record second layers.

The recorder will record the specified number of beats then immediately
begin playing those recorded beats back through the main output. The
dry/wet knob controls the mix between the Main mix and the loop
recorder.

If the record button is pressed again, the loop recorder will record a
second layer that is punched into the first layer and can be of a length
of 0 up to the length of the original loop. The DJ will have to press
stop to stop recording the second layer, although I think that it might
be good to have it stop automatically when the loop repeats (I’m going
back and forth about this).

After a second layer is recorded, the undo button is activated and if
pressed it reverts the loop recorder to the previous state before the
most recent recording. If clicked, the undo button becomes a redo
button. There will be one level of undo/redo available in the loop
recorder. When the record button is clicked, the current state is
committed, and the new layer being recorded is now what will be
removed/restored by undo.

Once a DJ is satisfied with the loop she can save it to disk to be used
in a sampler or main deck using the save button. I’ve also toyed with
the idea of have a smart export feature which will automatically export
the loop and add it to a sampler, but I need to flesh this idea out
more.

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

#### New Classes:

`LoopRecorderManager` - Coordinates the UI and recording and playback of
the loop recorder.

`LoopRecorder` - Handles loop recording and is tied very closely to
Engine Master, which provides the mixed output to the recorder. All
loops will be recorded as LPCM audio for performance and quality
reasons.

`EngineLoopDeck` - subclass of EngineDeck for loop playback. Handles
special mixing of recorded audio.

#### Main changes required to Mixxx Engine:

Add audio routing to the loop recorder in Engine Master. This will need
to be done in realtime, so the code will probably differ from the
existing recording code, which does processing in side chains.

Modify buffering and channel code to allow continuous playback, which
switches between buffers. This will be a pretty challenging task.

Implement new SoundSource class for internally stored loops?

### Controls

| Key/Control     | What it Does                                                         |
| --------------- | -------------------------------------------------------------------- |
| Record          | On empty loop recorder, initiates loop recording.                    |
| Play            | Plays stored loop, disabled if nothing has been recorded.            |
| Undo/Redo       | By default undo 1 layer of changes. If clicked undo changes to redo. |
| Save            | Save the loop to the Mixxx library.                                  |
| Clear           | Clears all recorded loops.                                           |
| Number of Beats | Sets the number of beats to automatically record                     |
| Input source    | Toggles the Mixxx output that is directed into the loop recorder.    |
| Dry/Wet         | Controls level of recorder sent back into the main mix.              |

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
    3.  Loop Player
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

### GSoC 2013 Timeline

#### June (Program begins June 17)

  - Week 3: Flesh out structure and interface for loop controller
    objects, begin work on LoopRecorder, put together skeletal GUI
  - Week 4: Continue work on LoopRecorder class, get basic real time
    recording working

#### July

  - Week 1: Focus work on LoopPlayer and LoopRecorderManager
  - Week 2: Continue work on LoopPlayer and LoopRecorderManager,
    integrate with Loop Recorder
  - Week 3: Have a loop recorder that can record a single layer and play
    it back by midterm evaluations.
  - Week 4: Carl on vacation, may be able to work a few hours.
  - Week 5 (GSoC Midterm Evaluation Week): Take stock of project
    progress and revisit planning for the next phase of development.
    Begin implementing multiple layer support.

#### August

  - Week 1 (8/5-8/11):Implement multiple layer support, begin work on
    final GUI
  - Week 2: Continue implementation of multiple layer support
  - Week 3: Have fully function rough demo
  - Week 4: Implement library export feature and loop table view

#### September

  - Week 1: Finalize GUI, documentation and do extensive on final
    version.
  - Week 2: Finalize GUI, documentation and do extensive on final
    version.
  - Week 3 (GSoC Suggested pencils down date): Finalize GUI,
    documentation and do extensive on final version. Fix loose ends.
  - Week 4: All coding done, prepare final report.

## Team

  - Carl Pillot (GSoC 2013 Student)
  - Owen Williams (GSoC 2013 Mentor)

## Ideas

### Possible way to handle single-level undo/redo

Currently in Progress.

This is a short walkthrough of a possible implementation for recording
multiple layers and implementing single-level undo/redo support. It uses
three buffers to store the different recordings and manipulate the
mixing of the loop.

Loop recording must happen in realtime, I don't think that we can spin
off an extra process like the current recording code (this has
significant performance implications). Right now I'm assuming that the
loop recorder object will be updated directly by the Engine Master, so
that on each call it's updated with the latest output data from either
the master or PFL output streams.

I'm using two buffers referred to as buffer\_A, and buffer\_B. My idea
for controlling playback is to have a loop buffer pointer in the
LoopPlayer class, which changes depending on the recording state of the
buffer.

If at least one loop has already been recorder, copy buffer\_B to
buffer\_A (commits a previously recorded two layer mix).

set play pointer to buffer\_B

Record to buffer\_A mixing new audio with previously recorded audio

When recording is finished, set play pointer to buffer\_A and signal
that recording is done.

Undo functionality resets the play pointer to the buffer\_B redo resets
it to buffer\_A.

## Comments
