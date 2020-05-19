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

2 six-weeks sprints.

**First sprint:** Up and running  
**Main objectives:**  
Create instanciable rhythm detector analyzer class and add related
preferences for tempo detector, the user should be able to turn on/off
beat detection, downbeat detection, phrase detection, and section
detection.  
Solid, testable, and self-contained improvements on the current beat and
tempo detector. Currently, the underlying beatmap feature does not work
well. It struggles with constant tempos as it does not account for small
unintended fluctuations in time. Having the BPM jumping around is a
terrible user-experience and it also messes with the sync feature. It
also struggles by detecting a different tempo than the intended one on
parts without a steady drum.  
Implement proof-of-concept of the other methods with minimum
modifications of the underlying QM library.

**Week 1:** Implement a multi-feature beat detector using a combination
of the OnSetFunctions provided by the QM library.  
The available functions are "complex domain", which is the most
versatile and the one Mixxx current uses, "spectral difference" which is
appropriate for percussive recordings, "phase deviation" which performs
best on for non-percussive music, and "broadband energy rise" which is
for identifying percussive onsets in mixed music.  
The new detector will consider at least 2 more functions with a
combination of the default one and compare their outputs for deriving a
final and more reliable list of beat positions and a confidence value
for each beat based on the agreement of the different methods.

**Week 2:** Implement a BPM frequency histogram and compute statistics
descriptors. With the frequency of all tempo estimates and dispersion
measures, an algorithm should be able to infer unintended fluctuations
around a center value. It should only return the tempo of these center
values and anchor them to the first beat where this tempo happens. If
the track has a constant tempo this should be the only BPM value, if the
track has an accelerando or ritardando part the algorithm will not able
to identify a center value, and the fluctuation of the tempo will be
captured. When it stabilizes on a new tempo, or for sudden changes the
new value will be added to the first beat that has the new tempo.

**Week 3:** Implement a draft of section and phrases detection using the
QM Segmenter plugin and measure detection with the QM Downbeat plugin,
at this point only 4/4 time signatures will be considered.

**Week 4:** Prepare a Pull Request with the new features. This will have
a complete description, production code, unit tests, and accuracy
benchmarks. This will be used as an objective measure for the first
evaluation of Google.

**Week 5:** Implement an algorithm that programmatically optimizes the
Segmenter parameters for section detection. The first step is
determining the minimum length of the segments by using the tempo
information and the arbitrary rule that a section should be at least 8
bars. Then optimize the number of segments types with the silhouette
method.

**week 6:** Implement an algorithm that optimizes Segmenter for phrase
detection. The chosen approach will be to use the segments detected in
the previous step and fed them in as independent inputs, constraining
the minimum length at the measure length, and optimizing the number of
segments types iteratively.

**Second sprint:** An holistic approach to rhythm detection  
**Main objectives:**  
Implement a reasonable accurately meter detection algorithm to complete
the features of the rhythm analyzer.  
Explore the synergy of all levels of the rhythm analyzer to improve
accuracy and optimize running time and memory usage.

**Week 1:** Dig into the Segmenter code. Use downbeat positions for
starting new segments. Explore if adding new parameters such as a
maximum segment length or a maximum number of segments improves the
phrase and section detection.

**Week 2:** Prepare a PR for improved section and phrase detection. This
will have a complete description, production code, unit tests, and
accuracy benchmarks. This will be used as an objective measure for the
second evaluation of Google.

**Week 3:** Implement meter detection by modifying the QM downbeat
plugin. Using it's already computed autocorrelation functions and
dynamic programming to find the best time signature.

**Week 4:** Benchmark and accuracy tunning. Test the meter and downbeat
detection against professional drummers annotations on the GTZAN
dataset. See what kind of mistakes are happening and fix them if
possible.

**Week 5:** Optimize the analyzers to remove redundancies and shared
computations that can be reutilized between them.

**Week 6:** Prepare final PR for the complete rhythm detection analyzer.
This will have a complete description, production code, unit tests, and
accuracy benchmarks. This will be used as an objective measure for the
final evaluation of Google.
