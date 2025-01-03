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
code has been merged into trunk.**

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
it has an impact on the perception of our product. Accordingly, we are
transitioning to use the word "follower" internally. The user interface
only mentions "enabled" and "master".

## Design

### High-Level Overview

### Requirements

  - Synchronization Sources
  - Support standard Mixxx players (particularly decks and samplers) as
    synchronization sources.
  - Internal Clock synchronization source
  - (V2.0) MIDI clock synchronization source

## Control Interface

|  | Synchronization Source Controls |  |                |  |                                           |  |                                                                            |  |
|  | ------------------------------- |  | -------------- |  | ----------------------------------------- |  | -------------------------------------------------------------------------- |  |
|  | \[Group\]                       |  | Key/Control    |  | Range                                     |  | What it does                                                               |  |
|  | \[Group\]                       |  | sync\_master   |  | binary, read/write toggle-button          |  | Whether this group is the master. This is set in addition to sync\_enabled |  |
|  | \[Group\]                       |  | sync\_enabled  |  | binary, read/write latching toggle-button |  | Whether sync is enabled on this group.                                     |  |
|  | \[Group\]                       |  | sync\_mode     |  | enum, read-only                           |  | An enum representing the current master/follower sync mode.                |  |
|  | \[Group\]                       |  | rate           |  | binary, read/write slider                 |  | The current setting of the rate slider                                     |  |
|  | \[Group\]                       |  | bpm            |  | double, read-only                         |  | The current playback bpm value, regardless of scratch or play/stop         |  |
|  | \[Group\]                       |  | beat\_distance |  | double, read-only, 0.0-1.0                |  | The distance from the last beat from 0 to 1                                |  |
|  | Internal Clock Controls         |  |                |  |                                           |  |                                                                            |  |
|  | \[Group\]                       |  | Key/Control    |  | Range                                     |  | What it does                                                               |  |
|  | \[InternalClock\]               |  | sync\_master   |  | binary, read/write toggle-button          |  | Whether internal clock is the master.                                      |  |
|  | \[InternalClock\]               |  | bpm            |  | double, read/write                        |  | The BPM of the internal clock.                                             |  |
|  | \[InternalClock\]               |  | beat\_distance |  | double, read/write, 0.0-1.0               |  | The distance from the last clock beat from 0 to 1                          |  |

## User Interface

## Basic Usage

Master Sync preserves the old behavior that users might be used to -- if
the user taps a sync button, that track will match the BPM of an
already-playing track.

All of the new functionality occurs when the user presses and holds the
sync button. It becomes latched, the Internal Clock master light becomes
lit, and sync mode is on.

All decks that have sync mode enabled will match bpm at all times. If a
slider is adjusted on one deck, it will change on all synced decks.
Furthermore, decks that have quantize active will "nudge" their position
until they are perfectly aligned with the other tracks. Scratching
effects and play/stop actions are not synchronized between decks by
default.

The user can also manually assign master mode to a deck, even one under
vinyl control. When this mode is active, all rate information is synced
to other decks, including scratching and stopping the master deck. This
makes it possible to scratch multiple tracks simultaneously.

## Controller Impact Assessment

The Sync button is now a toggle button instead of a momentary
pushbutton.

Some users will want to designate certain decks as master specifically.
They will need a separate pushbutton for master mode.

## Work Breakdown

## Current Progress

**This project is active and slated for release in Mixxx 1.12.0. The
code is available in the [master\_sync branch on
github](https://github.com/mixxxdj/mixxx/tree/master_sync)**

## Team

  - Owen Williams
  - RJ Ryan

## Comments
