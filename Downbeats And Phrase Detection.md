# Improve Beat Analyzer to recognize the meter, measures, phrases and sections

**Student:** Cristiano Lacerda (cristiano.lacerda@usp.br)  
**Mentor:** Daniel Schürmann  
**Related Project:**
[measures\_downbeats\_bars\_and\_phrases](measures_downbeats_bars_and_phrases)  

## Summary

**Status:** Drafting (If you have any thoughts on this please join the
discussion on Zulip)

**Motivation**

When mixing two or more tracks, beatmatching is an essential technique
that allows us to listen to more than a piece of music together in a
pleasant way. However, beatmatching alone is not enough for good and
memorable transactions since every track has many hierarchical
structures in time, in which the beat is the basic one. Thus for a
seamless blending of tracks ideally, all these structures should be
matched, this includes the measures, which is just a group of beats
determined by the meter of the song. After that, we got a phrase which
is quite an ambiguous terms but is nothing more than a group of measures
that makes sense together. And past that, we still have a section of the
track which, in an analogous way is a group of phrases that makes sense
as a whole.

Mixxx currently can detect beats and help the DJ by either automatically
quantizing beats or simply by providing visual aid through the scrolling
waveform in the form of a beatgrid. This project aims to improve that by
adding to the beat analyzer the tools to automatically detect the meter
and downbeats, and to segment phrases and sections of the track.

Meanwhile, Harshit Maurya will work on the related project to make use
of these features so they can enable better DJing either automatically
or by providing helpful visuals cues. Also, no auto-detection algorithms
are perfect so the UI should be able to allow the user to manually
specify these features and painless disregard wrong information.

**Design:**
