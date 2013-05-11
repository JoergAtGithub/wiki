# Refactoring Tasks

Here is where `rryan` keeps track of (typically small) refactoring
tasks. This is doomed to become out-dated but oh well. As of 5/2013,
this is up to date.

  - Move keyboard processing into controller subsystem.
  - Timestamp all MIDI/HID messages
  - Engine sidechain -- FIFO
  - SoundSource API -\> floats (breaks plugin ABI)
  - SearchQuery threading mess
  - SearchQueryParser -- SQL vs. internal
  - ShoutcastManager -- get all shoutcast code out of MixxxApp and some
    out of EngineShoutcast
  - \#define all preference config keys
  - Header file includes cleanup 
  - Make menubar nicer, get it out of MixxxApp
  - If mix output is not used, don't calculate it in EngineMaster.
  - move scanning-related code out of TrackCollection
  - EngineObject API const-ness
