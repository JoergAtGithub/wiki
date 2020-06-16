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

Temporal and structural regularities - *I.e.* rhythm - are together with
melody and harmony the most prominent characteristics of music, but the
rhythm is by far the one that offers the biggest incentive and easiest
way to interact physically with the music, which can be simple in the
form of just taping the foot or nodding the head to the beat to dancing
to elaborate piece-long choreographies or all night long on a
dancefloor. We define music rhythm is a hierarchical structure as
follows:

A beat is the smallest unit of rhythm.  
A measure is a combination of one or more beats.  
A phrase is a combination of one more measure.  
A section is a combination of one or more phrases.  
A track is a combination of one or more sections.

The beat and the measure are rigorously described by the time
signature.  
The length of the beat is the denominator and the numerator defines the
number of beats per measure.  
The definition of phrases and sections is rather subjective, music
theory states that both should have a complete musical sense, the phrase
being the smallest unit that does that, and the section being a major
structural part of the track.  
Intuitively the phrase is where a hard cut or a loop should not sound
wrong and the section is where there is a big change in the mood of the
track.  
To clear out any ambiguity we are going to arbitrarily define that a
phrase should be at most 8 bars while the section should be at least
that.

**Use cases**

Beatmatching is a quintessential DJ technique that allows us to listen
to more than one track simultaneously in a pleasant way, but as beats
represent the lowest level on the rhythm hierarchy, this is the bare
minimum of DJing and is not enough for good DJing and memorable sets.

The section detector should allow the DJ to easily recognize (and
navigate to) the places where one intuitively would mix in and out
tracks irrespectively of the style of transitions.  
For example, for highest impact transitions it's a common technique for
example for big room house DJs to hit play on the drop (one section) of
the incoming track as the build (another section) of the current one
reaches the end.  
Or for the smoothest transitions, other styles of electronic dance music
such as techno often rely on extended transitions, in this case, the DJs
would usually mix the outro (one section) of the current track with the
intro (another section) of the incoming one.

A phrase being on a level down in the rhythm hierarchy has a strong
relation to the track itself and work best for making live remixes or
edits of a track.  
A phrase marker should help DJs recognize (and navigate to) the places
where one would intuitively play with effects, loop the track, and jump
to a hot cue for example.

Downbeat matching is useful for more creative and out-of-the-box
performance and transitions giving more freedom to the DJ while still
getting keeping the flow of the tracks.

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

**Bonus (nice to have if time allows):** Each beat could also have a
key, this would be especially useful for beats of type phrases.

## Schedule Planning

3-1 month phases.

**First month**

~~**Week 1:** Implement a multi-feature beat detector using a
combination of the OnSetFunctions provided by the QM library.  
The available functions are "complex domain", which is the most
versatile and the one Mixxx current uses, "spectral difference" which is
appropriate for percussive recordings, "phase deviation" which performs
best on for non-percussive music, and "broadband energy rise" which is
for identifying percussive onsets in mixed music.  
The new detector will consider at least 2 more functions with a
combination of the default one and compare their outputs for deriving a
final and more reliable list of beat positions and a confidence value
for each beat based on the agreement of the different methods. ~~

**~~Week 2:~~ Week 1** Implement a BPM frequency histogram and compute
statistics descriptors. With the frequency of all tempo estimates and
dispersion measures, an algorithm should be able to infer unintended
fluctuations around a center value. It should only return the tempo of
these center values and anchor them to the first beat where this tempo
happens. If the track has a constant tempo this should be the only BPM
value, if the track has an accelerando or ritardando part the algorithm
will not able to identify a center value, and the fluctuation of the
tempo will be captured. When it stabilizes on a new tempo, or for sudden
changes the new value will be added to the first beat that has the new
tempo. **Done** [\#2847](https://github.com/mixxxdj/mixxx/pull/2847)

**Week 2:** Implement a draft of downbeat and measure detection with the
QM Downbeat plugin, at this point only 4/4 time signatures will be
considered. Explore how to simultaneous track beat and downbeat
positions, or at least share low-level audio processing between
analysis. ~~Update \#2847 and address review commentary~~. Created the
new rhythm detector class with downbeats and beats detection. Created
the preference window for the rhythm detector.

**Week 3:** Implement sections and phrases analyses using the QM
Segmenter plugin on the new rhythm detector. Actually use the
preferences of the new detector.

**Week 4:** Prepare the first-month deliverable. Also, do more research:

Dive into the SFFT, Note Onset Detection, and Hiden Markov Models. After
a quick glimpse of the code of all levels of the rhythm structure, I
will take the time to research more about the main algorithms at that
code and how to tie them all together in the next phase. The short-time
Fourier transform for example is a quintessential technique for audio
processing, and its resolution has a profound impact on the extraction
of audio features. The resulted spectogram can also be further processed
in several ways before extracting any features. With logarithmic
compression being an obvious idea because hearing and notes frequencies
are a log function. Another interesting idea is to have an adaptive
windowing with a step size the roughly map a beat periodicity. These
ideas are
presented[here](http://resources.mpi-inf.mpg.de/departments/d4/teaching/ss2010/mp_mm/2010_MuellerGrosche_Lecture_MusicProcessing_BeatTracking_handout.pdf)
and discussed in more details at the
[book](https://www.springer.com/gp/book/9783319219448) Audio features
are the input of the Note Onset Detection function which is the basis of
the beat tracking algorithm. A very large and comprehensive paper
discussing different audio features for computing it are discussed
[here](https://ieeexplore.ieee.org/document/1495485) Hidden Markov
Models are a powerful probabilistic method used by the QM segmenter and
it can be used for meter recognition and beat tracking as well as
described
[here](https://hal.archives-ouvertes.fr/hal-00655779v1/document).

**First Month deliverable** A pull request for the new rhythm detector
capable of detecting beats, downbeats, phrases, and sections, including
a complete description, production code, test code, and a comparative
benchmark in the form of a spreadsheet.

**Second month**

**Week 1:** Improvements on downbeat detection. Explore how to use code
from the beat detection (autocorrelation function and Viterbi algorithm)
for time signature recognition.

**Week 2:** Improvements on downbeat detection. Explore how to use code
from segmenter (hidden Markov models) for time signature recognition.

**Week 3:** Improvements on phrases detection.

**Week 4:** Improvements on sections detection.

**Second-month deliverable** A pull request with the improvements on the
rhythm detector, this version should be capable of handling time
signatures different from 4/4 and should have an overall better accuracy
and performance.

**Third month**

**Week 1:** Integration with Harshit progress.

**Week 2:** Code cleaning, performance optimization, accuracy
benchmarks.

**Week 3:** Finish up any pending work for the final deliverable.

**Week 4:** Write-up on this wiki and/or a blog post a
tutorial/introduction on beat/downbeat/phrases and section detection
with an overview of all the research and code done during summer.

**Final Deliverable** Update and work on the previous deliverable so
it's ready to merge.
