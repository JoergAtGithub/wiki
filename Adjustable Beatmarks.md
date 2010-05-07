This page shall document how implementation of adjustable beatmarks
works.

# Description

Beatmarks and measuremarks help especially beginners to beatmatch two
songs and help to decide which track is ahead and should be delayed a
tip. Since in most cases the beat doesn't start counting from the
beginnig of the track, beatmarks require an offset. For this purpose
this feature adds a MIDI signal that places a special cue (the "beat
cue") at current play position if send. The beatmark renderer afterwards
calculates all marks foreward and backward to the beginning of the track
based on BPM. Measuremarks are aligned in a way that beat cue is a
measuremark.

Thus prior mixing someone adjusts beatmarks of both tracks by evaluating
beats and measures and mark them precisly similar to conventional cues.
Afterwards no trained ear is requiered to decide which track is ahead.

As hint by Lukas Smith: On a track with variable BPM it might be a good
idea to set the beat marker at your mix out position and adjusting the
songs BPM to the BPM at the mix out point, since at the mix in point you
have plenty of time to beat match by ear

# Signal flow

To adjust beatmarks send "beatmark\_set" e. g. via Standard.kbd.cfg

**Adjust beatmark**

  - signal "beatmark\_set" is send by ControlPushButton
  - slot BeatmarkSet is raised an signal "beatmark\_point" is trigger
    with current sample position
  - waveformrendererbeat.cpp receives signal "beatmark\_point" and
    adjusts beatmarks to current sample position

**Track loaded**

  - slot loadTrack is raised and cues are loaded from TrackInfoObject
  - beat type cue is sorted out and beatmark position is read and send
    to waveformrendererbeat.cpp

**Track unloaded**

  - slot unloadTrack is raised and cues are loaded from TrackInfoObject
  - beat type cue is sorted out and set to current beatmark position
  - cue dao should automatically save these changes in database

# Changes

**Touched files**

  - player.h
  - player.cpp
  - dlgmidilearning.cpp
  - waveform/waveformrendererbeat.h
  - waveform/waveformrendererbeat.cpp

\*\*Added files \*\*

  - engine/beatmarkcontrol.h
  - engine/beatmarkcontrol.cpp

# TODO

  - cues aren't saved after leaving MIXXX (general problem)
  - drawing button for skin
  - document about database issue beat type cue
  - mention files touched
  - describe what it's good for and how to use it
  - what about multiple beat type cues
  - managable cues? -\> change type
  - think about automatic beatmark adjust along bpm detection
