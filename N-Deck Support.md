# N-Deck Support

## Summary and Rationale

**Status**: This specification is **in drafting**. This is a
meta-specification which is dependent on the outcomes of other
specifications. Please feel free to add comments.

## Use Cases

  - DJ Bill is considering switching from Traktor to Mixxx. However, he
    makes heavy use of Traktor's 4-decks and cannot use Mixxx since it
    only allows 2. 
  - **Your use case here**

## Design

This project entails a complete revamp of many parts of Mixxx.

#### Engine Support

The internal mixing engine must be revamped to support more than 2 decks
being mixed together.

#### UI Support

The UI and skin file are heavily 2-deck centric. The skinning system
must be either heavily modified or re-written with N-decks in mind from
the start.

#### Preferences Dialog Considerations

Bill Good is currently working on External Mixer Mode. This will allow
Mixxx users to detail where they would like outputs to be routed and
mixed. Pending his design, there will be a flexible way for users to
route additional sources to their preferred sinks.

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

    1. N-Deck Support
      1.1 Refactor the engine to support multiple decks / audio channels.
      1.2 Strip all 2-deck centric code out of random parts of the Mixxx codebase.
      1.3 Update preferences dialog to allow routing of each deck to an appropriate sink.
      1.4 Update/rewrite the skinning engine to allow for N-decks 
      1.5 Handle corner cases (e.g. what happens when the user wants more decks than a skin shows)
      1.6 Build a skin that has more than 2 decks in it.

## Current Progress

The lp:\~mixxxdevelopers/mixxx/features\_hydra branch contains all the
work that's been done so far. This branch has completed steps 1.1 and
parts of 1.2.

### List of Places in Mixxx That are 2-Deck Centric

If you are looking for a place to contribute to this project, please
tackle making a part of Mixxx on this list flexible enough to handle
N-Decks.

  - ~~Parts of mixxx.cpp~~

<!-- end list -->

``` 
    * Now, only the "File -> Load to Player" drop-downs.
* Skinning engine
    * This project is looking for project lead!
* Library
    * The right-click context menus all only list players 1 and 2 to load a track.
* MIDI Scripts
    * All MIDI scripts are only written for Player1 and Player2, but this is because most only have 2 decks worth of controls.
      * The easiest way to tackle this is to make the two live decks on a MIDI device switchable to one of the 1-N decks.
* PlayerInfo class, which is used to share loaded-track metadata with things like Shoutcast. 
* LADSPA
    * Bruno Buccolo is working on this. He will take the potential of N-Decks into account.
* External Mixer Mode
    * Bill Good is working on this. He will take the potential of N-Decks into account.

```

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - **YOU**
  - RJ Ryan
  - Albert Santoni
