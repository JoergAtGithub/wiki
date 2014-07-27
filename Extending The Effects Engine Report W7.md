Hello,

This week I started with fixing some bugs on the branch\[1\] responsible
for replacing the default equalizers with a dedicated EffectRack. One of
them was causing Mixxx not to shutdown properly, it wasn't getting all
the way down to *return 0* line in *main.cpp*. The problem was that
inside *DlgPrefEQ*'s destructor I was deleting the data from
*m\_pConfig*, which is a pointer to Mixxx's configurations. As you'd
expect, the same data was being deleted inside *MixxxMainWindow* because
that's where it was initialized in the first place. This double deletion
of the same data leaded to abnormal termination of the program.

My next task was displaying human readable names inside the QComboBoxes
for selecting which effect is active for a specific deck. Each item from
the QComboBox has an additional *data* field which I used to store the
effect ID. The Preference page has a check box which switches between
showing all the effects or only the equalizer ones. To avoid coupling
between *DlgPrefEq* and effects I introduced a flag for each effect
which is set to *true* if the effect is an equalizer. Inside
*EffectsManager* there are separate methods for retrieving either all
the available effects or only the equalizers which are used to populate
the drop down lists. To set the name and data for each entry I used two
separate lists: one for names and one for IDs. I wrongly assumed that
each effect had the same index in both lists because the routine for
obtaining them was similar. This was not true because a QSet was
involved in the process. I did some research and a QSet is implemented
with a QHash which does not guarantee that its items are stored in the
same order they are introduced. I fixed this issue by storing both the
name and the ID of an effect inside the same QSet.

The second part of my GSoC project is adding LV2 support to Mixxx. I
started with testing Calf\[2\] plug inside Audacity and Ardour. Audacity
2.0.5 which is the last released version does not support them, so I had
to compile Audacity 2.0.6 from sources. After installing and
uninstalling libraries, resolving conflicts between packages I managed
to get it up and running. Afterwards I found two Jack hosts for LV2:
*calfjackhost* (comes with calf plug ins) and *jalv* (written by the
creator of LV2). I installed *jack*, *qjackctl* and after fixing an
issue with jack server not being able to start, I was able to route
Mixxx's sound through LV2 plug ins and then back to speakers. I tested
*jack* on Windows too and it seems to work as expected which is good
news for us. This made me and Daniel consider another approach to adding
LV2 support to Mixxx. Rather than making Mixxx an LV2 host, use an
existing one to process the sound. Roughly, Mixxx will feature an effect
which routes the sound samples to a Jack host, get them back modified
and output them to Mixxx's master output. This approach has the
advantage of being more stable and less error prone.

As a side task I took on the quest to implement a FFT Graphic Equalizer
for Mixxx, based on Audacity's Equalization\[3\]. After days of reading
about the Fourier transform, FFT windowing\[4\] and overlapping\[5\], I
was disappointed to conclude that is not worth having such an Equalizer.
Audacity has a window size of \~16000 samples and it is filtering
samples in chunks to use the overlap add method. However, since Mixxx is
doing real time equalization, we don't have access to many samples (I
did some tests and I got 8192 samples when I chose the largest audio
buffer from preferences). This implied to set the window size to our
buffer size and further divide this buffer into chunks. Consequently we
applied FFT on a small number of samples which gave us poor frequency
range (FFT\_sample\_len / 2 frequency bins were accessible). This\[6\]
post gives some arguments against frequency domain equalizers. As we
were aiming for an efficient equalizer, here is a quote from that blog
post which is proving the contrary: *The FFT, though efficient compared
to the DFT (which is the FFT without the "fast" part), performs worse
than linear time, and we need to do both the FFT and it's inverse, which
is computationally similar. EQing with the FFT is therefore generally
very inefficient compared to comparable time-domain filters.*

I was confused by the terms PortAudio, PulseAudio, Jack, ALSA and so on.
Playing with *jack*, Mixxx preferences and talking with a few guys on
IRC made me learn new and interesting things about Linux sound
architecture. I found out that PortAudio is a cross-platform library for
controlling various lower level components such as PulseAudio, Jack,
Alsa, etc. PulseAudio is similar with Jack. They do their job through
ALSA or another low level piece of software like the older OSS.

[[/media/lxf130.audio.layers.png|]]

Yours truly,  
Nicu Badescu

\[1\] - https:*github.com/badescunicu/mixxx/tree/kill\_buttons  
\[2\] - http:*calf.sourceforge.net/  
\[3\] -
https:*github.com/mcpierce/audacity/blob/master/src/effects/Equalization.cpp  
\[4\] -
http:*www.physik.uni-wuerzburg.de/\~praktiku/Anleitung/Fremde/ANO14.pdf  
\[5\] - http:*www.zytrax.com/tech/audio/equalization.html\#fft  
\[6\] -
http:*blog.bjornroche.com/2012/08/why-eq-is-done-in-time-domain.html  
  
[Back to the main page\!](extending_the_effects_engine)
