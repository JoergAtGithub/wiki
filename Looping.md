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

**Ben's idea:** The "In" point of a loop is the Cue Point (or we could
implement it that they're separate, but by default the In point is set
to the Cue point when a track is loaded). The "Out" point you set in
real-time and as soon as it's set, it starts looping. You can move
either point by pressing the relevant button and using the search
buttons or jog wheel to move it, which updates it in realtime, then
press again to store the new position. Then there's a cancel/reloop
button, to escape from the loop (when it ends) or to restart looping
again.

Important considerations:

  - How to cancel/escape from looping
  - What happens when someone clicks on the waveform summary to seek
    outside of the loop? (cancel the looping?)
  - How can we make this as easy and as obvious as possible to use?

For reference, here are the looping buttons on the Pioneer CDJ-1000MK3:

[[/media/wiki/cdj1000mk3-loop-buttons.jpg|]]

#### Mixxx Skin Considerations

What buttons would we need to add to the main GUI (ie. all skins)?

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

    1. Looping
      1.1 Assess existing looping code
        1.1.1 See if we can reuse any ControlObjects
        1.1.2 Figure out how the old code moves the play position.
      1.2 Create LoopingControl class
        1.2.1 Implement skeleton class structure, following EngineBufferScale's structure 
        1.2.2 In process() (or similar) function, check if playpos == end of loop (and move playpos to start of loop)
        1.2.3 If seeking occurs outside of loop, cancel the looping (?)
        1.2.4 
      1.3 Code hooks into waveform view and waveform summary
        1.3.1 Talk to RJ Ryan to make sure new waveform makes this easy
        1.3.1 Get loop in/out pos and paint highly visible markers

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - **YOU**
  - RJ Ryan
  - Albert Santoni
