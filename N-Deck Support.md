# N-Deck Support

## Summary and Rationale

**Status**: This specification is **in drafting**. This is a
meta-specification which is dependent on the outcomes of other
specifications. Please feel free to add comments.

## Use Cases

  - DJ Bill is considering switching from Traktor to Mixxx. However, he
    makes heavy use of Traktor's 4-decks and cannot use Mixxx since it
    only allows 2. 
  - DJ Cassandra creates crazy mashups and sometimes wants more than 2
    songs to be playing at once. She needs Mixxx to support \>2 decks.
  - DJ Danny wants to prepare the next 2 songs he will mix while the
    first 2 are playing. To do this, he needs \>2 decks.
  - **Your use case here**

## Design

This project entails a complete revamp of many parts of Mixxx.

#### Engine Support

The internal mixing engine must be revamped to support more than 2 decks
being mixed together.

#### UI Support

The UI and skin file are heavily 2-deck centric. The skinning system
must be either heavily modified or re-written with N-decks in mind from
the start. A feature specification for this is in drafting: [Skinning
Engine](skinning_engine)

#### Preferences Dialog Considerations

Bill Good is currently working on [External Mixer
Mode](gsoc2010_dvs_mode). This will allow Mixxx users to detail where
they would like outputs to be routed and mixed. Pending his design,
there will be a flexible way for users to route additional sources to
their preferred sinks.

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
work that's been done so far.

  - The features\_hydra branch has completed steps 1.1 and parts of 1.2.
  - A feature specification for 1.4 is in drafting: [Skinning
    Engine](skinning_engine)
  - A GSOC 2010 project is addressing 1.3: [External Mixer
    Mode](gsoc2010_dvs_mode)

## List of Places in Mixxx That are 2-Deck Centric

**If you are looking for a place to contribute to this project, please
tackle making a part of Mixxx on this list flexible enough to handle
N-Decks.**

  - ~~Parts of mixxx.cpp~~
  - Now, only the "File -\> Load to Player" drop-downs.
  - Mixing Engine
  - EngineBuffer beat sync'ing is hard-coded to 2-decks. Working on this
    in features\_hydra.
  - Skinning engine
  - This project is looking for project lead\!
  - Library
  - The right-click context menus all only list players 1 and 2 to load
    a track.
  - widget/wbrowsetableview.cpp
  - MIDI Scripts
  - All MIDI scripts are only written for Player1 and Player2, but this
    is because most only have 2 decks worth of controls.

<!-- end list -->

``` 
    * The easiest way to tackle this is to make the two live decks on a MIDI device switchable to one of the 1-N decks.
* PlayerInfo class, which is used to share loaded-track metadata with things like Shoutcast. 
* LADSPA
* Bruno Buccolo is working on this. He will take the potential of N-Decks into account.
* External Mixer Mode
* Bill Good is working on this. He will take the potential of N-Decks into account.
* Vinyl Control is all 2-deck centric.
* Auto-DJ is 2-deck centric
* Preferences have some internal logic that hard-codes Channel1 and Channel2
* MIDI Learning has some hard-coded Channel1/Channel2 stuff
```

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - **YOU**
  - RJ Ryan
  - Albert Santoni
