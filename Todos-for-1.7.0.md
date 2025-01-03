# To do before v1.7.0 is released

(Please strike anything that has been completed. And put your handle by
it so we know who to thank\!)

Development of 1.7.0 has been moved to a Bzr branch. [See here for usage
details](https://code.launchpad.net/~mixxxdevelopers/mixxx/release-1.6.2)

## Tasks

  - **Non-coding tasks:**
  - Test MP3/OGG/FLAC/WAVs of varying sample rates [and report results
    here](sound%20file%20testing%20matrix)
  - Test everything in different versions of Windows, particularly
    Windows-only bugs [Compiling on Windows](compiling_on_windows)
  - [Test MIDI mappings](Supported-Controller-Test-Grid.md) for
    correct functionality for as many currently supported controllers as
    we can
  - Update the [Wikipedia entry](http://en.wikipedia.org/wiki/Mixxx)
  - ~~Finish website update~~ (Albert)
  - ~~Update user manual~~

<!-- end list -->

  - ~~Fix timecode LUT memory corruption~~ (Albert) -
    <https://bugs.launchpad.net/mixxx/+bug/382228>
  - ~~Fix pasuspender usage in all .desktop files~~ (Albert) -
    <https://bugs.launchpad.net/mixxx/+bug/388657>
  - ~~Ensure we bundle correct MSVC DLLs with Win32 and Win64
    installers~~ (Sean) -
    <https://bugs.launchpad.net/mixxx/1.7/+bug/376801>
  - ~~Make an executive decision about the output mapping table~~
    (Albert)
  - ~~Fix qt-opengl and qt-svg dependencies for Ubuntu~~ (Albert)
    <https://bugs.launchpad.net/mixxx/1.7/+bug/365609>
  - ~~Get Albert to look at possible performance hit:~~
    <https://bugs.launchpad.net/mixxx/+bug/379317>
  - ~~If possible, try to figure out Ubuntu ALSA stream freeze~~ - See
    [Mailing list
    thread](http://thread.gmane.org/gmane.comp.multimedia.mixxx.devel/2334/focus=2337)
    and [Bug entry](https://bugs.launchpad.net/mixxx/1.7/+bug/383431)
    Now we just need to nag people to offer a user-installable fix.
  - ~~MidiObjectALSASeq is missing a devClose implementation~~ - Pegasus
  - ~~Non-C++ task: Get the "res" directory to copy to the proper place
    (`prefix=`) on an `scons install` (python)~~
  - ~~Fix model issue where removing any row removes the last row as
    well. (midiinputmappingtablemodel.cpp, midimapping.cpp)~~ - Albert
  - ~~Fix model issue where completing the learning wizard doesn't list
    anything in the table until Mixxx is restarted~~ - Albert
  - ~~Get rid of MidiType enum, switch MIDI mapping format to use
    \<status\> for input blocks as well.~~ - Albert
  - ~~Migrate the range hacks out of SoundTouch's bpmdetect.cpp and into
    bpmdetector.cpp, then update bpmdetect.cpp from the SoundTouch
    repository~~ - rryan
  - ~~Multithreading guru task: Clean up and check MidiScriptEngine
    thread-safety~~ - rryan...give the man a beer\!
  - ~~Handle MIDI Pitch input messages (0xE\#, LSB, MSB)~~ - Gamegod,
    Pegasus & Lupin3rd
  - ~~Merge the Features\_MIDIScriptAutoReaction branch to trunk
    (currently waiting on the Qt team to see if our solution is a good
    one)~~ - RRyan and Pegasus
  - ~~Fix the version number in defs.h and all MIDI XML files~~ -
    Pegasus and Mad Jester
  - ~~Port old MIDI XML device files to the [new
    format](midi_controller_mapping_file_format) (basically just adding
    a header block.)~~ - Mad Jester
  - ~~Complete MIDI device selection & mapping dialog (see the
    [MidiMapping design
    spec](midi_scripting#midi_mapping_object_design_spec))~~
  - ~~Use tree view in preferences and display MIDI devices on left.~~ -
    gamegod
  - ~~Or select MIDI device, auto select the mapping (combobox)~~ -
    gamegod
  - ~~Reimplement MIDI Learning~~ (100% done - gamegod)
  - ~~Rewrite midiEvent() signal in MidiObject to emit a MidiMessage,
    and rename the signal to midiLearn()~~
  - ~~Connect midiLearn() signal to some learn() slot in MidiMapping
    object~~
  - ~~Write learn() slot in MidiMapping. learn() should update the
    mapping and emit(inputMappingChanged()) at the end.~~
  - \<del\>Create list of usable controls... \</del\> - gamegod
  - ~~Midi Scripting~~
  - ~~Clear scripting engine when new MIDI mapping preset is loaded in
    the Prefs.~~ - gamegod
  - ~~MidiInputMappingTableView - add delegate classes~~ - gamegod
  - ~~Display the MidiType (Key/CC/etc) (instead of those crappy
    enumerated integers)~~ - gamegod
  - ~~Combo boxes for group and control~~ - gamegod
  - ~~Values display in hexadecimal~~ - gamegod
  - \-\> MIDI output handling
  - ~~Create MidiOutputMappingTableModel~~ ~~and -View~~ - gamegod
  - ~~Write underlying data structure for output (OutputMidiMapping)~~ -
    Pegasus
  - Finish adding delegate classes and finish up output table (include
    correct columns) - targeted for v1.8 instead
  - ~~Fix up \<status\> and \<miditype\> mishandling in MidiMessage for
    outputs~~ - Albert
  - ~~Fix the segfault-on-close that's happening on Linux and Windows
    with Intel graphics drivers.~~ This may not be our problem. See [bug
    \#251128](https://bugs.launchpad.net/bugs/251128).
  - ~~Call MIDI script init function when opening the device, not
    before~~ - Pegasus
  - ~~Call MIDI script shutdown function (if one exists) just before
    closing the device~~ - Pegasus
  - ~~Write an upgrade function that moves mixxx.cfg and mixxxtrack.xml
    to their new homes (ffs)~~ - Pegasus
  - \-\> Clear up as many compiler warnings as we can ~~(give preference
    to the "depreciated function" ones so we don't get bitten later.)~~
    (kousu)
  - ~~Change version numbers everywhere to "1.7.0-beta1"~~ - Pegasus
  - ~~Windows: MIDI feedback on all but the first listed controller
    doesn't work with more than one connected. It's best to
    disconnect/remove all (real and virtual) devices except the one
    you're interested in working with.~~ - Pegasus
  - ~~Windows: You may need to tell Windows to send MIDI output to the
    correct device, especially if you hear random notes instead of see
    lights on your controller: Start-\>Settings-\>Control
    Panel-\>Classic View-\>Sounds and Audio Devices-\>Audio Tab, set
    "MIDI Music Playback" at the bottom to the device you're trying to
    use.~~ - Pegasus

## Bug fixes

<https://launchpad.net/mixxx/+milestone/1.7.0>

## Known Issues / Errata

  - MIDI Pitch messages are no longer processed internally and must be
    mapped to a script function. Fortunately
    [script.pitch](midi_scripting#available_common_functions) can be
    used very easily from your script.
  - Probably regressed like crazy with the M-Audio Xponent.
    Functionality needs to be rewritten using scripting. - lupin3rd has
    an input mapping
  - The use of multiple MIDI devices simultaneously is not yet
    supported.
  - SelectNextTrack, SelectPrevTrack and LoadSelected do not work in the
    Browse view. See [bug
    \#342120](https://bugs.launchpad.net/mixxx/+bug/342120).
  - SelectNextTrack & SelectPrevTrack cause the GUI to freeze for a few
    seconds when you try to scroll down beyond the current page. See
    [bug \#361170](https://bugs.launchpad.net/mixxx/+bug/361170).
  - Certain MIDI controllers' (Stanton SCS devices) scratching is
    directly tied to latency. As a result, users will need to tune the
    values at the top of the scripts in question for their particular
    system.
