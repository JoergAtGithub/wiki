# Rhythm Detector

**Student:** Cristiano Lacerda (cristiano.lacerda@usp.br)  
**Mentor:** Daniel Schürmann  
**Related Project:**
[measures\_downbeats\_bars\_and\_phrases](measures_downbeats_bars_and_phrases)  

## Summary

**Status:** Drafting (If you have any thoughts on this please join the
discussion on
[Zulip](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Rhythm.20Detector))

**Main idea**

Temporal and structural regularities - *I.e.* rhythm - are perhaps the
most prominent characteristic of music and offer people a huge incentive
and easy way to interact physically with the music. This can be being in
the form of just taping the foot or nodding the head to the beat or
dancing to elaborate piece-long choreographies. We define music rhythm
is a hierarchical structure as follows:

A beat is the smallest unit of rhythm.  
A measure is a combination of one or more beats.  
A phrase is a combination of one more measure.  
A section is a combination of one or more phrases.  
A track is a combination of one or more sections.

The beat and the measure are rigorously described by the time
signature.  
The length of the beat is the denominator and the numerator defines the
number of beats per measure.  
The definition of phrases and sections is rather subjective, both should
have a complete musical sense, the phrase is the smallest unit that does
that and the section is a major structural part of the track.
Intuitively the phrase is where a hard cut or a loop should not sound
wrong and the section is where there is a big change in the mood of the
track.  
To clear out any ambiguity we are going to arbitrarily define that a
phrase should be at most 8 bars while the section is at least that.

**Use cases**

As rhythm is perhaps the highest incentive for us to interact physically
with the music matching all levels of rhythm enable for the smoothest
transitions and highest impact transitions.  
It's a common technique for example for big room house DJs to hit play
on the drop (one section) of the incoming track as the build (another
section) of the current one reaches the end.  
Other styles of electronic dance music such as techno often rely on
extended smooth transitions in this case the DJs would usually mix the
outro (one section) of the current track with the intro (another
section) of the incoming one.  
The section detector should allow the DJ to easily recognize (and
navigate to) the places where one intuitively would mix in and out
tracks irrespectively of the style of transitions.

A phrase being on a level down in the hierarchy a phrase has a strong
relation to the track within and would work best for making live remixes
or edits of a track.  
A phrase marker should help DJs recognize (and navigate to) the places
where one would intuitively play with effects, loop the track, and jump
to a hot cue for example.  

\*\* Design \*\*

Rhythm Detector will have three main methods and algorithms that will
all perform sequentially on a beatList.

1.  beat and tempo detection

<!-- end list -->

  - Parameters: track mono samples and audio features, such as the
    onsetDetectionFunction,
  - Returns: a beatList. Each beat has a frame position. The first beat
    also has a bpm. If the track has a varying tempo each beat that has
    a different tempo also has a bpm. Note that a constant tempo should
    not be considered to be perfect, small unintended fluctuations
    should not be accounted for.

<!-- end list -->

1.  downbeat and time signature detection

<!-- end list -->

  - Parameters: audio features, such as the beatSpectrum, and a beatList
    returned by beat and tempo detection method
  - Returns: a new beatList where the first beats of each measure have a
    type set to downbeat. The first beat now also has a time signature.
    If the track has a varying time signature, each beat that has a
    different one also has a time signature.

<!-- end list -->

1.  phrases and sections detection

<!-- end list -->

  - Parameters: audio features such as ??? and a beatList returned by
    downbeat and time signature detection method
  - Returns a new beatList, where every beat that starts a phrase or a
    section have they type set accordingly.

**Bonus (nice to have if time allows):** Each beat should/could also
have a key, this would be especially useful for beats of type phrases
and sections.

## Schedule Planning

2 six-weeks sprints, both with 2 weeks working on each method.

**First sprint**

**Week 1:** Implement a multi-feature beat detector using a combination
of the OnSetFunctions provided by the QM library.  
This should not only provide better accuracy but also enables to output
the confidence of the tempo detection.

**Week 2:** Implement BPM Histogram and compute statistics
descriptors.  
This should enable handling tracks with varying tempo properly.

**Week 3:** Port [this meter detection
algorithm](https://github.com/pikrakis/Introduction-to-Audio-Analysis---a-MATLAB-approach/blob/master/library/musicMeterTempoInduction.m)
from MATLAB to C++.

**Week 4:** Extend the previous implementation to include the ideas
described in [this paper](https://arrow.tudublin.ie/argcon/52/), mainly
the beat similarity matrix.

**Week 5:** Implement section detection using the segmenter algorithm
provided by the QM library.

**week 6:** Implement phrases detection using also using segmenter.
