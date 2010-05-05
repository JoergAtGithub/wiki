This page shall document how implementation of adjustable beatmarks
works.

# Signal flow

To adjust beatmarks send "beatmark\_set"

**Adjust beatmark**

  - signal "beatmark\_set" is send by ControlPushButton (or
    Standard.kbd.cfg)
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

# TODO

  - cues aren't saved after leaving MIXXX (general problem)
  - drawing button for skin
  - document about database issue beat type cue
  - mention files touched
