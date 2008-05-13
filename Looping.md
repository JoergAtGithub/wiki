# Looping

## Summary and Rationale

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

Add support for looping parts of songs. Looping parts of songs allows
DJs to perform more active mixes and also serve as an easy way to
prevent trainwrecks.

## Use Cases

  - DJ Bill is considering switching from CDJs to software. He doesn't
    like Mixxx because it lacks the looping functionality that he's used
    to.
  - DJ Jane wants to create better mashups with Mixxx, but finds herself
    limited to only beatmatching and playing with Mixxx's cueing.
    Looping would give her an extra tool to enhance her mashups.
  - DJ Fred is a novice DJ who finds that he is often unable to
    beatmatch properly before a song ends. Looping the last 4 beats or
    bars of a song would give him extra time to beatmatch.
  - **Your use case here**

## Design

#### Setting Loops

#### Toggling Looping

#### Preferences Dialog Considerations

  - If possible, should we try to keep this simple and avoid having any
    settings?

#### Internal Changes

There's some unfinished looping code hacked into EngineBuffer that needs
to be blown away. Once that's removed, you'd create something like a
"LoopingControl" class which manages the playback position. The
EngineBuffer objects would each have a LoopingControl object, and they
would ask their LoopingControl objects to update (ie. loop) the play
position for them. This "EngineBuffer asks object X to update the play
position" is precisely how the EngineBufferScale classes work. The
EngineBufferScale classes do pitch/time stretching, which affects rate
at which the playback position changes.

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

``` 
1. Looping
  1.1 Assess existing looping code
    1.1.1 See if we can reuse any ControlObjects
    1.1.2 Figure out how the old code moves the play position.
  1.2 Create LoopingControl class
    1.2.1 Implement skeleton class structure, following EngineBufferScale's structure 
    1.2.2 In process() (or similar) function, check if playpos == end of loop (and move playpos to start of loop)
    1.2.3 
    1.2.4 
    1.2.5 
```

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - **YOU**
