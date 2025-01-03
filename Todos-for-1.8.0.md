# Things to do for v1.8.0

  - Update sound file test script in src/test/soundFileFormats to
    include M4A file generation
  - Test MP3/OGG/FLAC/WAVs of varying sample rates [and report results
    here](sound%20file%20testing%20matrix)
  - Add MIDI controller mappings [from the
    forums](http://www.mixxx.org/forums/viewforum.php?f=7) to the
    branch.
  - [Test MIDI mappings](Supported-Controller-Test-Grid.md) for
    correct functionality for as many currently supported controllers as
    we can
  - Update the [Wikipedia entry](http://en.wikipedia.org/wiki/Mixxx)
  - Update [user manual](manual)

[Unresolved bugs targeted for this
release](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.milestone%3Alist=3246&field.tag=&field.tags_combinator=ANY&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&search=Search)

**Remaining blocker bugs for 1.8.0 final**

  - ~~Scaling ASSERTs - Haven't seen them in ages... still a problem?~~
  - ~~EngineBufferScaleLinear audio degradation (Phil, partially
    fixed)~~
  - ~~EngineBufferScaleST repeated buffers, sync loss (partially fixed.
    Still loses sync when looping.)~~
  - ~~"scratch" control is asymmetric -
    <https://bugs.launchpad.net/mixxx/+bug/519892>~~ - fixed in
    fixes\_scratch
  - ~~fixes\_scratch merge~~ - in beta2
  - ~~Sort out reference counting for TIOs in library caching layer
    (basesqltablemodel.cpp?)~~ (RJ rocks\!)
  - ~~Featured Artists agreement + stats~~

**Very important remaining tasks for beta2**:

  - ~~[Scratching crash since
    r2407](https://bugs.launchpad.net/mixxx/+bug/588729)~~
  - ~~Fix bugs introduced by ssplugin merge:~~

<!-- end list -->

``` 
    * <del>Build error on Win32</del>
    * <del>[[https://bugs.launchpad.net/mixxx/+bug/586774|Wrong track duration]]</del> - fixed except for VBR MP3s which are worked around for now (they show as '?' until first loaded)
    * <del>[[https://bugs.launchpad.net/mixxx/+bug/586755|Crash creating new library]]</del>
* <del>Merge sadness_ssplugin</del> and <del>test build plugins for each platform</del>
* <del>Merge features_sqlite into trunk</del>
* <del>Merge features_scriptTimers (with its MIDI thread fixes)</del>
* <del>M4A Plugin + Downloader (done)</del>
* <del>Update LibraryTableModel's rows when TrackDAO is accessed, without resetting it.</del> - in features_sqlite branch
```

**Very important remaining tasks for beta1**:

  - ~~Missing columns in playlist/crate/autodj views
    <https://bugs.launchpad.net/mixxx/+bug/500474>~~
  - ~~Schema versioning~~
  - ~~1.7.0 to 1.8.0 XML-\>DB Library importer (Patch from Zach)~~
  - ~~Playlist blurb~~
  - ~~Crate image blurb~~
  - Fix as many crashes as possible

<!-- end list -->

``` 
    * <del>SoundTouch timestretch</del>
    * <del>Reader ASSERT(s)</del> (haven't seen these in a while, might have been the same bug as below - Albert)
    * <del>MIDI script engine crash</del> (https://bugs.launchpad.net/mixxx/+bug/493793)
* <del>Crate/Playlist/MissingTracks need working location column.</del>
* <del>Analyze view text is not readable on dark skins.</del>
* <del>Escape Prepare view searches, use fetchMore(), search in the GUI thread</del>
```

### Library

Complete the rewrite for basic -- but stable -- functionality

  - Track DB

<!-- end list -->

``` 
    * <del>Needs blacklisting of removed songs.</del>
* <del>1.7.0 to 1.8.0 XML->DB Library importer (Zach)</del>
* Searching across library features
    * <del>Make sure search is case-insensitive everywhere</del>
    * <del>Search is saved and restored per-model</del>
    * Playlist models store the search per-playlist
    * <del>Searches occur in background thread.</del>
* Drag-n-drop across library features
    * Make sure you can drop tracks from any place (browse, external track source, mixxx library) into a Mixxx playlist and the <del>play queue</del> Auto DJ queue
    * Win/Mac/Linux drag of files from OS file browser into Mixxx?
    * Make explicit the cases in which a file outside the Mixxx library is added to the Mixxx library.
    * Show an indicator of where you are about to drop a file in the track-table or sidebar. This is a bug in Qt: http://bugreports.qt.nokia.com/browse/QTBUG-7107
* Context menus across the whole library 
    * Make sure context choices for tracks are appropriate to current state.
    * Menus for sidebar items
* UI Feedback  
    * <del>When a track is missing from the library (Missing Songs model done)</del>
    * <del>When a track failed to load</del>
    * When your results are filtered (i.e. a search is active) 
    * When you are about to add a track to your Mixxx library. Make any warnings disable-able via mixxx.cfg.
* Browse Mode
    * <del>Use a file-system model that polls in a background thread</del>
    * <del>Searches and sorting for the filesystem view</del>
    * <del>Always show .. as a choice</del>
    * <del>Always sort folders before files</del>
    * Needs header that shows you your current path
    * Sorting doesn't work in Size column (kb/mb treated as the same)
* Playlists 
    * <del>Playlist table headers show raw column names</del>
    * <del>Playlists need duration delegate</del>
    * <del>Dragging a file thats in a playlist to its own playlist results in many added copies.</del>
    * <del>Drag-and-drop reordering</del>    
    * <del>Invisible playlists so that e.g. the Auto-DJ playlist do not show under playlists.</del> 
* <del>Play Queue/AutoDJ</del>
    * <del>Make enable/disable button change text when its on/off so you know its state.</del>
    * Make 95% crossfade threshold configurable via preferences.
* Library Rescan
    * <del>Basic fast hashing rescan</del>
    * <del>Modify Library table to make orphan detection easier later (add extra track_locations table)</del>
    * <del>Add mixxx_deleted to Libray table and fs_deleted cols to track_locations table</del>
    * <del>Use mixxx_deleted to blacklist files "removed" from the Mixxx library.</del>
    * <del>Cancel rescan functionality (just needs to be fixed)</del>
* Tagging (not file metadata tagging)
    * <del>DAO for tags</del>
    * <del>Feature for tags</del>
    * <del>Drag-n-drop to sidebar</del>
    * <del>Tag table model</del>
    * <del>Context menu for track table</del>
    * <del>Context menus for tags in sidebar</del>
    * <del>Feature overview page</del>
    * <del>Prepare view</del>
    * Delegate for showing tags in library table
* Track Sources
    * <del>iTunes playlist TrackModel</del>
    * <del>iTunes needs duration delegate</del>
    * <del>Rhythmbox Need Date delegate</del>
    * <del>Sorting doesn't work in XML-sourced Playlists</del>
* Polish
    * <del>Sidebar icons for each feature</del>
    * Tooltips for sidebar items
* <del>MIDI Control of Library</del>
* <del>Track-table column header context menu to show/hide columns</del>
* Cue/Loop Storage in the DB - (this is really a mini-project in itself) 
    * <del>Write a CueDAO/Cue service.</del>
    * <del>Make TIO's have a list of Cue's</del>
    * <del>Make TrackCollection save a TIO's Cue's on track save (via CueDAO)</del>
    * <del>Ditch EngineBufferCue</del>
    * <del>Extend EngineBuffer to allow outside addition of EngineControls</del>
    * <del>Write CueControl, created by Player, added to EngineBuffer as an EngineControl</del>
    * <del>Restore track-editor, make it show hotcues</del>
    * Add custom widgets for hotcues -- not happening: skins will have to have hacked buttons instead
    * <del>Waveform / waveform overview loops and cues</del>
    * <del>Update skins</del>
* Minor Bugs
    * <del>Duration Delegate should format seconds as %02d.</del> 
    * <del>Sorting is not case insensitive (e.g. on Title)</del>
```

### Looping

  - ~~Complete the [looping](looping) feature, merge to trunk.~~
  - Update controller mappings with hot cue and looping controls
  - ~~SCS.3d~~ - done
  - ~~BCD-3000~~
  - ~~Hercules MK2~~
  - ~~Hercules RMX~~
  - ~~M-Audio Xponent~~
  - ~~Numark Total Control~~
  - ~~Reloop Digital Jockey 2~~

### M4A

  - Solve packaging issues
  - ~~Solve Windows X64 libfaad2 dll [building
    issues](build_windows_dependencies#libfaad2) (embedded asm vs
    intrinsics) - may be able to split the assembly code into its own
    file and assemble that separately~~ - Successfully worked around it
    by disabling the (5 lines (\!) of) assembly code and using the
    supplied C/C++ code
  - ~~Fix SoundSourceM4A decoder issues~~ 

### Misc

  - Bundle libsndfile's trunk code into Mixxx for FLAC fixes? (Since
    there's no scheduled release date for the fixed libsndfile)
  - Collect enhanced controller mappings from forum posts for wider
    testing
  - Fix compilation on Windows x64 to correctly use SoundTouch
    optimizations (or not depending on optimize flag) - Sean
  - Update user manual
  - ~~Can someone with some pull PLEASE tell C-Net to update their
    [Mixxx download
    page](http://download.cnet.com/Mixxx/3000-2170_4-10514911.html?tag=mncol)?\!
    82 downloads a week for Mixxx 1.5.0.2 does not make us look good.~~
    - Adam took care of it
  - Upload 1.8.0 final to C-Net and update our home page link there
    (still points to SF)
  - Update [our FreshMeat page](http://freshmeat.net/projects/mixxx)

### MIDI Sub-system tasks

*Remaining tasks here are just polish and are not required for release.*

  - ~~Move all PortMIDI calls to one thread (the script engines can not
    directly call send\*Msg anymore.) [See
    this.](http://lists.create.ucsb.edu/pipermail/media_api/2005-September/000422.html)~~
  - ~~Save multiple device files correctly, deleting previous .midi.xml
    files in .mixxx/~~ 

<!-- end list -->

``` 
    * Save the meta-data (<del>controller ID</del>, author, description, etc...)
      * First make a GUI object that lets the user modify the author and description
    * <del>Find a more appropriate place to save the files other than the MidiDeviceManager destructor</del> Now done (only) when OK is clicked in the prefs
    * <del>Need a way to keep track of duplicate devices so separate files can be saved: Have DlgPreferences::slotApply() call MidiDeviceManager::saveMappings() which does them all in one shot (and can thereby keep track of them)</del>
* <del>Load those files correctly</del>
    * <del>Load files for attached devices regardless of if they're activated or not.</del>
* Replace MidiCategory with MidiStatusByte permanently (see mididevice.cpp line 195.)
* MIDI Scripting: <del>Pass the <group> value from the XML to the script as an additional parameter (at the end of the list so existing scripts are not affected.)</del> - Done by Phil
* <del>Add MIDI script timers</del>
* <del>Implement alpha-beta smoothing filter in the Engine (currently in scratch.* functions in the common script file) with fixed-interval updates. (I.e. if no new data arrives in the interval, assume the control is stopped and feed that data to the smoothing function.)</del> - Done in the MidiScriptEngine for relative controls in 1.8.0
* GUI changes:
    * <del>Replace "Activate" button with an "Enabled" check box</del>
    * <del>Display enabled devices in the tree in bold text</del>
    * <del>Auto-change "Output" drop-down based on auto-selected output device in MidiDevice(Manager) when the device is enabled</del> - Albert
    * <del>Make "Output" drop-down take effect when changed</del> - not happening in 1.8. Output drop-down is disabled for now.
    * Persistent mapping preset drop-down (don't return to "..." unless Clear All is pressed. If the user tweaks the mapping, say "<custom>" or something.)
    * Also clear the list of MIDI scripts when Clear All is pressed
    * Do not commit changes to the MIDI mapping tables unless OK is pressed in the preferences window. (I.e. allow pressing the Cancel button or the X on the preferences window to restore the MIDI mappings to their previous states.)
```
