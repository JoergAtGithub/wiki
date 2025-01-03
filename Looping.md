# Looping

## Summary and Rationale

**Status**: This specification is **complete**. Please do not edit this
page. The implementation was finished in October 2009 and is pending
merge into trunk.

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
  - DJ Dan2600 Recently started using Mixxx, its incredibly impressed by
    it's functionality, and the lack of looping is one of the only few
    things that set its apart from "professional" retail software. 
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

**DJ Maniax's thoughts:**

AtomixMP3 has the easiest and most effective looping and beat match I
have used, which is to say that these functions are easy to use occur
automatically to the actual beat, not just the beat timing. A looping
setup similar in function would be GREAT in Mixxx\! I've no idea about
the technical issues involved, but AtomixMP3's functions work fine even
through WINE if that helps?

**Elysion's thoughts:** Have a mode where the looping would start at the
next beat / end of the bar and would jump x beats \_backwards\_ when
starting to loop

#### Mixxx Skin Considerations

What buttons would we need to add to the main GUI (ie. all skins)?

#### Preferences Dialog Considerations

  - If possible, should we try to keep this simple and avoid having any
    settings?
  - I agree, again re' AtomixMP3 format is hard to beat. . .

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

#### Architectural Issues

##### The Sound Engine

The way that the Mixxx sound engine works is that we process audio
buffers at a time. The length of these buffers is determined by the
latency of your soundcard. The soundcard driver asks us for audio
buffers at a time, so we respond that way. Once we ship a buffer of
samples off to the soundcard, we have no way of knowing exactly when a
given sample in that buffer will actually be played. The only way to
compensate for this is to aim for very low latency. With lower latency
and lower buffer sizes, we can be more flexible with changes in the
audio. Once the soundcard has asked for a section of audio, it is too
late to go seeking through the file stream to a different place because
that would take too long and the sound coming out of the soundcard would
skip. Thus, we have to be ready with the data that needs to be played
when the soundcard asks for it.

##### EngineBuffer / Reader Interaction

Another issue with looping is that there is no good way to ask the
Reader to cache a given range of a song. The Reader class does buffering
of wave audio for the EngineBuffer so that when the soundcard asks for
the next section of data, the data is ready. If a seek happens to a
different part of the currently playing song, then the Reader has to
start over and buffer that region.

When a loop occurs, we /know/ that once we reach the loops end we are
going to want to jump to the start. What is desirable for the looping
machinery is a flexible way to express that to the Reader. "Please cache
this region of the song, because I'm going to need to loop over it".

The Reader was completely ditched and rewritten as CachingReader, which
implements this functionality. EngineBuffer was rewritten to work with
this new reader.

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
    1.2.3 If seeking occurs outside of loop, cancel the looping (?)
  1.3 Code hooks into waveform view and waveform summary
    1.3.1 Talk to RJ Ryan to make sure new waveform makes this easy
    1.3.2 Get loop in/out pos and paint highly visible markers
    1.3.3 Make waveform more flexible in how it represents markers so that you can tell the difference between a loop and cue
  1.4 Replace Reader with CachingReader
  1.5 Rewrite EngineBuffer, remove old junk
    1.5.1 Refactor rate control into RateControl, bpm into BpmControl, looping into LoopingControl, etc
    1.5.2 Enable hinting of cues, loops, etc to CachingReader -- currently not done. 
  1.6 Update the EngineBufferScale objects to work with the new system.
    1.6.1 Use ReadAheadManager to manage reading forward in the song given looping, reverse, etc.
    1.6.2 Need to rewrite them to no longer use a ring-buffer, but rather work in a streaming fashion.
  1.7 Update all official skins to have loop buttons. 
```

## Current Progress

The ~~Features\_rryan-looping~~
lp:\~mixxxdevelopers/mixxx/features\_looping branch contains all the
work that's been done so far.

The LoopingControl class has the following Control Objects:

  - \[ChannelX\], loop\_in 
  - \[ChannelX\], loop\_out
  - \[ChannelX\], reloop\_exit 
  - \[ChannelX\], loop\_start\_position
  - \[ChannelX\], loop\_end\_position

The WaveformRenderer is setup to render WaveformRenderMarks of the
loop\_start\_position and loop\_end\_position control objects.

The outlineNetbook skin has been changed to have loop in/out/reloop
buttons.

### Remaining Work

  - Change loop/cue controls to hint the CachingReader
  - Ensure audio quality for EngineBufferScaleLinear/SoundTouch
  - Experiment with EngineBufferScaleRubberBand
  - Add tests

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - **YOU**
  - RJ Ryan
  - Albert Santoni
