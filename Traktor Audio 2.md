The original version of the Native Instruments Traktor Audio 2 (the one
with two 1/4 inch/6.35 mm jacks; the one with 1/8" inch/3.5mm jacks is
the newer model) can work with Mixxx on Linux but it needs a bit of
configuration. This device presents to ALSA as two subdevices, but by
default PortAudio, the cross-platform library Mixxx uses to access sound
hardware, only lists one of the subdevices in Mixxx so the headphone
output can't be configured. To work around this, copy and paste the text
below to a file at `~/.asoundrc`. Select "TraktorAudio2Master" with
Channels 1-2 for Mixxx's Master output and "TraktorAudio2Headphones"
with channels 1-2 for Mixxx's Headphones output:

    pcm.TraktorAudio2Master { type plug; slave.pcm "hw:TraktorAudio2,0,0"; }
    pcm.TraktorAudio2Headphones { type plug; slave.pcm "hw:TraktorAudio2,0,1"; }
