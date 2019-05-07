The Auto DJ should be an assistant that allows seamless interaction with
a real DJ finally.

In Mixxx 2.3 we will add additional CUEs and load modes to allow more
automatized use-cases.

The Mayor use cases are:

### CD Mode

This mode should allow to play tracks gpples as if they are played in a
home stereo CD player.

The AutoDJ loads the track at 0:00 and starts it when the previous track
reaches the end. In ideal case there should be no gap at all (important
for live CDs).

Proposed Parameter:

  - Load at 0:00
  - Transition end at Track End 
  - Transition time = 0 s (can be changed)

### Juke-Box / Radio Mode

This mode should allow to play tracks from start to end as they are
played on the radio, or in bars. The Transition should allow no silence,
a equal silence gap or a short cross fade. The intro should be marked to
allow talk over with a warning when the track vocals start. This mode
makes use of the "Intro Start" and "Outro End" cues which are
automatically set by silence detection. Both can can be adjusted to skip
unusable garbage. In addition there is "Intro End" and "Outro Start"
cues surrounding the region that should not be touched in any
circumstances.

Proposed Parameter:

  - Load at Intro Start 
  - Transition end at Outro End 
  - Transition starts not before reaching Outro Start (if set) 
  - Transition time = 0 s ... X s but ends at Into End or Outro End
    which comes first. 

### DJing Mode

This mode should support the DJ cross fading the track with a nice
transition or beat matching. The Track is load at a usable Downbeat of
the track inside the intro region. In Mixxx 2.2 this was the CUE point,
which was identified to be too volatile depending on the DJ style. The
"Intro End" and "Outro Start" cues are also respected to not destroy the
main part of a track.

Proposed Parameter:

  - Load at CUE, a new Load CUE, at "Intro End - Transition time", at
    "Intro End - Outro druation";
  - Once Mixxx is aware of downbeats it should load at a downbeat. 
  - Transition starts at Outro start if set, else Transition end at
    Outro End 
  - Transition time = 0 s ... X s but ends at Into End or Outro End
    which comes first. 

Extra feature: One click beat loop starting at Outro Start, do have
unlimited time to cue the track in.
