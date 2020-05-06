# Measures, Downbeats, Bars and Phrases

**Author:** Harshit Maurya (hacksdump)

**Email:** [hmaurya999@gmail.com](hmaurya999@gmail.com)

**Mentors:** Be (Be-ing), Jan Holthuis (Holzhaus), Uwe Klotz (uklotzde)

This is the final
[proposal](https://drive.google.com/file/d/1Micg2kqdE-XpCIgcjb58CrZoqrgIHUnv/view?usp=sharing)
that got accepted in GSoC 2020.

For this project, I will be collaborating with Cristiano Lacerda
(crisclacerda). We will be working on making a new beatgrid format that
marks bars, meter, and phrases. Cristiano will focus on implementing
autodetection of this information from tracks while I will focus on
creating the UI for editing the beatgrid and using this information in
other Mixxx features (waveforms, looping, beatjump, quantize, etc).

## Original Proposal

### Abstract

The project aims at improving the audio track analysis features to
compute information such as downbeat, time signature, measures, and
phrases.

Currently, in mixxx and most DJing software, track synchronization is
more of a manual process for a DJ as the downbeat of the incoming track
has to be matched with the downbeat of the other track. This process can
be aided if the starting beat is predetermined by mixxx and the DJ can
freely press the play button while the two tracks automatically get
matched to the closest downbeats.

Downbeat detection will pave the way for bar detection and time
signature computation. This feature is necessary since a song can be in
a time signature other than 4/4, which will render most beat and
time-related features such as looping and quantization inconsistent with
the track. Overall smarter quantization can be achieved with the added
information.

Waveform viewer will also benefit from this feature as downbeats,
accented beats and time-signature can be visualized from the waveform
for added intuition to the DJ. This will be helpful to set cues visually
since phrases become more apparent to the player.

## Design and UI changes

### Downbeat markers

### Bar Counter

### Phrase divisions

### Time signature editor

### Implementation

To be added soon.

### End goal

Added support for variable bpm, variable time signature, downbeat
markers, phrase divisions and accordingly changed/added UI and
controller interactions for features such as looping, beat jumps, etc.

## Timeline

Will be updated soon

### Weekly logs/blogs

To be added per week.
