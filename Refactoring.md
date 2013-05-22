# Refactoring Tasks

Here is where `rryan` keeps track of (typically small) refactoring
tasks. This is doomed to become out-dated but oh well. As of 5/2013,
this is up to date.

  - Move keyboard processing into controller subsystem.
  - Timestamp all MIDI/HID messages
  - SoundSource API -\> floats (breaks plugin ABI)
  - SearchQueryParser -- SQL vs. internal
  - \#define all preference config keys
  - Header file includes cleanup 
  - Make menubar nicer, get it and all action handlers out of MixxxApp
  - If mix output is not used, don't calculate it in EngineMaster.
  - move scanning-related code out of TrackCollection
  - EngineObject API const-ness
  - Preferences dialogs need a huge overhaul.
  - Preferences depend trivially on PlayerManager. Also DlgPrefControls
    doesn't work with changeable \#s of decks or preview decks.
  - `PlayerManager` bindToLibrary is not changing-n-deck capable.
