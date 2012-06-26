# Stanton SCS.3d "DaScratch"

[[/media/hardware/stantonscs/scs3dangle.jpg|scs3dangle.jpg]]

Link to the website: <http://www.enterthesystem.com/system/scs3d/>

[See a walk-through video\!](http://www.youtube.com/watch?v=8DUpTikA8u0)

**[Mixxx user's guide for the SCS.3d](stanton_scs.3d_mixxx_user_guide)**

## Latest MIDI mapping & script files

#### Instructions

**Stanton's DaRouter is not used with Mixxx 1.7.0 and up. Close it
before starting Mixxx.**

1.  Download the files for the applicable version of Mixxx below.
2.  Save the files into:

<!-- end list -->

  - Windows: `C:\Program Files\Mixxx\midi` (technically
    `%PROGRAMFILES%\Mixxx\midi`)
  - OS X: `/Applications/Mixxx.app/Contents/Resources/midi`
  - Linux: `/usr[/local]/share/mixxx/midi`

<!-- end list -->

1.  Plug the controller in and wait for it to settle to the all-blue
    state.
2.  Start Mixxx
3.  Open Preferences
4.  Expand "MIDI Controllers"
5.  Select the "Stanton SCS.3d" device (or "USB Audio Device" in
    Windows)
6.  Click the Enable checkbox in the right pane ("Activate" button on
    1.7)
7.  Click the drop-down and choose the "Stanton SCS.3d" mapping
8.  Click OK and you're good to go. (The controller should initialize
    and light up.)

### 1.10.x

The latest official MIDI mapping and script file are in the 1.10 release
branch and can be downloaded from here:

  - [Stanton
    SCS.3d.midi.xml](http://bazaar.launchpad.net/~mixxxdevelopers/mixxx/release-1.10.x/download/head:/mixxxresmidistantons-20090212032424-9h29294ehh1322b2-346/Stanton%20SCS.3d.midi.xml)
  - [Stanton-SCS3d-scripts.js](http://bazaar.launchpad.net/~mixxxdevelopers/mixxx/release-1.10.x/download/head:/mixxxresmidistantons-20090212032424-9h29294ehh1322b2-347/Stanton-SCS3d-scripts.js)

### 1.8.x

The latest official MIDI mapping and script file are in the 1.8 release
branch and can be downloaded from here:

  - [Stanton
    SCS.3d.midi.xml](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.8.x/download/head%3A/mixxxresmidistantons-20090212032424-9h29294ehh1322b2-346/Stanton%20SCS.3d.midi.xml)
  - [Stanton-SCS3d-scripts.js](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.8.x/download/head%3A/mixxxresmidistantons-20090212032424-9h29294ehh1322b2-347/Stanton-SCS3d-scripts.js)

### 1.7.x

The latest official MIDI mapping and script file are in the 1.7 release
branch and can be downloaded from here:

  - [Stanton
    SCS.3d.midi.xml](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.6.2/download/head%3A/mixxxresmidistantons-20090212032424-9h29294ehh1322b2-346/Stanton%20SCS.3d.midi.xml)
  - [Stanton-SCS3d-scripts.js](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.6.2/download/head%3A/mixxxresmidistantons-20090212032424-9h29294ehh1322b2-347/Stanton-SCS3d-scripts.js)

### 1.6.1 & prior

DaRouter mapping for use with Mixxx up to v1.6.1:
[[/media/hardware/stantonscs/stanton_scs.3d_darouter.midi.xml.gz|]]

**Using Mixxx 1.7.0 and later is *strongly* recommended as you will
realize full functionality.**

#### Instructions

  - Set DaRouter to the "GEN Single SCS.3d Dual Virtual" preset.
  - Unpack the above file into:
  - Windows: C:\\Program Files\\Mixxx\\midi
  - OS X: /Applications/Mixxx.app/Contents/midi
  - Then start Mixxx, open Preferences, choose Input Controllers, the
    "Stanton SCS.3d DaRouter" mapping, and the "From DaRouter" device.
    Click OK and you're good to go.

#### Notes

  - Loop mode zone buttons are used to select & load tracks from the
    playlist. The left two switch the view between Library, Play Queue,
    etc, the right two select tracks in the Library, and the center one
    loads the selected track into the first stopped deck.
  - Trigger mode zone buttons are used to fine-tune the pitch. The left
    two permanently raise/lower the pitch by 1%. The right two
    temporarily do so by 4% (pitch bend.)
  - Flanger is enabled/disabled by the button under the pitch slider in
    FX mode. (Both decks.)
  - Headphone cue is the button under the Gain slider in Vinyl mode.
  - Reverse play in the button under the pitch slider in Vinyl mode.
  - FF and REW are the buttons below the circle in Vinyl mode.

#### Quirks

(all are resolved in Mixxx 1.7.0)

  - Scratching doesn't work well so is disabled.
  - Circle C1 acts as a jog dial, but it's backwards (relative to a
    record,) and a bit sensitive.
  - Mixxx has just one set of adjustments for the flanger effect and
    track select, so you can only operate them with Deck A selected.
    (Functions can only be mapped to one control at the moment.)

You can change which SCS.3d controls get mapped to what Mixxx functions
just by editing the XML file. See the [MIDI Mapping file
format](midi_controller_mapping_file_format) for details.
