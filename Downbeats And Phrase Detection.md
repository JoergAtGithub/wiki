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

A beat is the smallest unit of rhythm.

A measure is a combination of one or more beats. Determined by the
number of beats in the bar, this is the upper part of the time
signature.

A phrase is a combination of one more measure that has a complete
musical sense. This is rather vague and ambiguous a more restrictive but
still subjective rule is that a phrase is a place you can hardly cut or
loop a track without it sounding "wrong". An arbitrary rule is that a
phrase should have at maximum 16 bars.

A section is a combination of one or more phrases that also has a
complete musical sense. A more restrictive rule is that a section a
major structural part of the track, or where a DJ would intuitively mix
for a smooth transition. An arbitrary rule is that a section should have
at minimum 16 bars.

A track is a combination of one or more sections.

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
