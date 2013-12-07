## Summary

**Status**: This specification is **in drafting**. Please feel free to
edit this page and add your comments.

DJs frequently use a master sync tool to keep their their tracks in sync
while DJing. This frees the DJ from focusing on the mechanics of
beat-matching and enables her to devote attention to other aspects of
her performance.

This project aims to bring a master sync mechanism to Mixxx. Decks that
have high-quality timing information are eligible to be a
synchronization source. Additionally, we aim to support other
synchronization sources (e.g. internal and external clocks).

**This project is active and slated for release in Mixxx 1.12.0. The
code is available in the [master\_sync branch on
github](https://github.com/mixxxdj/mixxx/tree/master_sync)**

## Terminology

  - Synchronization Source
  - Any object that is capable of providing timing information.
  - Examples:

<!-- end list -->

``` 
    * A Mixxx deck or sampler.
    * An internal clock.
    * An external clock (e.g. MIDI or vinyl control).
* Timing Information
* Typically a BPM and offset or a list of beats at times as well as the current time. 
* Could be as little information as the current beat ratio. 
* The beat completion ratio (number from 0 to 1 indicating the current beat progress).
* A MIDI clock (24 pulses per quarter note).
```

**A note on the word "master" and "slave":** These words are used
frequently in computing but can tend to ruffle feathers. Other
commercial software does not use this pair of words, presumably due to
the charged history of the words. You'll often see the word "master"
used on its own but never with "slave". We should follow this lead since
it has an impact on the perception of our product.

## Design

### High-Level Overview

### Requirements

  - Synchronization Sources
  - Support standard Mixxx players (particularly decks and samplers) as
    synchronization sources.
  - Internal Clock synchronization source
  - (V2.0) MIDI clock synchronization source

### Open Questions

  - Master or Equals?
  - Should all decks be equals or should the master have the ultimate
    timing control?
  - What if you want to take a track out of the mix by spinning it back
    and stopping it? That shouldn't cause all decks to spinback. 
  - Distributing state across equals is very complicated.

## Control Interface

|  | Synchronization Source Controls |  |                |  |                               |  |                                                                    |  |
|  | ------------------------------- |  | -------------- |  | ----------------------------- |  | ------------------------------------------------------------------ |  |
|  | \[Group\]                       |  | Key/Control    |  | Range                         |  | What it does                                                       |  |
|  | \[Group\]                       |  | sync\_master   |  | binary, read/write pushbutton |  | Whether this group is the master.                                  |  |
|  | \[Group\]                       |  | sync\_slave    |  | binary, read/write pushbutton |  | Whether this group is the slave.                                   |  |
|  | \[Group\]                       |  | sync\_mode     |  | binary, read-only             |  | An enum representing the current master/slave sync mode            |  |
|  | \[Group\]                       |  | rate           |  | binary, read/write slider     |  | The current setting of the rate slider                             |  |
|  | \[Group\]                       |  | bpm            |  | double, read-only             |  | The current playback bpm value, regardless of scratch or play/stop |  |
|  | \[Group\]                       |  | rateEngine     |  | double, read-only             |  | The actual engine playback rate                                    |  |
|  | \[Group\]                       |  | beat\_distance |  | double, read-only             |  | The distance from the last beat from 0 to 1                        |  |
|  | \[Master\]                      |  | sync\_master   |  | binary, read/write pushbutton |  | Whether internal clock is the master.                              |  |
|  | \[Master\]                      |  | sync\_slider   |  | double, read/write slider     |  | Like Rate, a slider for adjusting internal clock rate              |  |
|  | \[Master\]                      |  | sync\_bpm      |  | double, read-only             |  | Current sync playback rate                                         |  |
|  | \[Master\]                      |  | beat\_distance |  | double, read-only             |  | The distance from the last beat from 0 to 1 of the internal clock  |  |

## User Interface

## Controller Impact Assessment

## Work Breakdown

## Current Progress

**This project is active and slated for release in Mixxx 1.12.0. The
code is available in the [master\_sync branch on
github](https://github.com/mixxxdj/mixxx/tree/master_sync)**

## Team

  - Owen Williams

## Comments
