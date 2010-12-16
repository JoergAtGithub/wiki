# Stanton SCS.1m

[[/media/hardware/stantonscs/scs1mproductshot.png|]]

Link to the website: <http://www.enterthesystem.com/system/scs1m_mixer/>

## Latest MIDI mapping & script files

[Mixxx user's guide for the SCS.1m](stanton_scs.1m_mixxx_user_guide)

### 1.9.x

#### Instructions

**Stanton's DaRouter is not used with Mixxx 1.9.0 and up. Close it
before starting Mixxx.**

1.  Download the files below.
2.  Save the files into:

<!-- end list -->

  - Windows: `C:\Program Files\Mixxx\midi` (technically
    `%PROGRAMFILES%\Mixxx\midi`)
  - OS X: `/Applications/Mixxx.app/Contents/Resources/midi`
  - Linux: `/usr[/local]/share/mixxx/midi`

<!-- end list -->

1.  Turn the controller on.
2.  Start Mixxx
3.  Open Preferences
4.  Expand "MIDI Controllers"
5.  Select the "SCS.1m" device
6.  Click the Enable checkbox in the right pane
7.  Click the drop-down and choose the "Stanton SCS.1m" mapping
8.  Click OK and you're good to go. (The controller should initialize
    and light up.)

***Note:** the controller is not yet supported in Linux. We have a plan
to fix that in a future Mixxx version.*

The latest official MIDI mapping and script file are in the 1.9 release
branch and can be downloaded from here:

  - [Stanton
    SCS.1m.midi.xml](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.9.x/download/head%3A/stantonscs.1m.midi.x-20090413052950-0s8dvnvezkl3lrrh-1/Stanton%20SCS.1m.midi.xml)
  - [Stanton-SCS1m-scripts.js](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.9.x/download/head%3A/stantonscs1mscripts.-20090413052950-0s8dvnvezkl3lrrh-2/Stanton-SCS1m-scripts.js)

### 1.7.x-1.8x

[See a walk-through video\!](http://www.youtube.com/watch?v=crJksOEuTx0)

The latest official MIDI mapping and script file are in the 1.7 release
branch and can be downloaded from here:

  - [Stanton
    SCS.1m.midi.xml](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.6.2/download/head%3A/stantonscs.1m.midi.x-20090413052950-0s8dvnvezkl3lrrh-1/Stanton%20SCS.1m.midi.xml)
  - [Stanton-SCS1m-scripts.js](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.6.2/download/head%3A/stantonscs1mscripts.-20090413052950-0s8dvnvezkl3lrrh-2/Stanton-SCS1m-scripts.js)

Just drop them in the res/midi folder (see instructions above.)

### 1.6.1 & prior

Mapping for use with Mixxx up to v1.6.1:
[[/media/hardware/stantonscs/stanton_scs.1m_1.60.midi.xml.gz|]] ***Updated**
on May 23, 2009 to more closely match the mapping for 1.7.0*

**Using Mixxx 1.7.0 is *strongly* recommended as you will gain more
functionality.**

#### Instructions

1.  Unpack the above file into:

<!-- end list -->

  - Windows: C:\\Program Files\\Mixxx\\midi
  - OS X: /Applications/Mixxx.app/Contents/Resources/midi
  - Linux: /usr\[/local\]/share/mixxx/midi

<!-- end list -->

1.  Start Mixxx, open Preferences, choose Input Controllers, the
    "Stanton SCS.1m 1.60" mapping, and the "From SCS.1" device. Click
    OK, click OK on the 'Warning: No \<midino\> defined in MIDI map
    node: "control"' and you're good to go.

**If you don't see the device in the list or Mixxx doesn't respond to
it**:

  - **Windows & Mac**: you may need to run DaRouter to get communication
    1.  Download & unpack the
        [[/media/hardware/stantonscs/scs.1m_thru.bmtp.gz|SCS.1m\_thru]]
        DaRouter preset
    2.  Start DaRouter and browse to where you saved it. Select & open
        it.
    3.  Follow from step 2 above.
  - **Linux**, you'll need to install [FFADO](http://www.ffado.org)
    v2.1.
    1.  Follow [these
        instructions](http://subversion.ffado.org/wiki/InstallingFfadoFromSource),
        just steps 1-3 and 5 to install FFADO from trunk (until v2.1 is
        released.)
    2.  Run the `libffado/tests/test-scs` tool that will be built, then
        run Mixxx.

#### Notes

  - The middle two channel columns are for decks 1 & 2. (Left for 1,
    Right for 2)
  - The buttons above the gain knobs at the top are the headphone cues
  - The encoder knobs act as jog wheels
  - Pressing the encoder knobs toggles reverse playback
  - A & B are REWind and FastForward, respectively
  - The long button at the bottom is Play/Pause
  - The short circle button beneath that is Cue.
  - The pan knob isn't assigned to anything (Mixxx doesn't support
    channel panning)
  - Channel columns 1 & 4 control things for decks 1 & 2 respectively:
  - The circle button at the top syncs the song with that on the other
    deck (assuming the BPM detector worked correctly on both)
  - Pressing the encoder knob toggles the flange effect (rotating it
    does nothing)
  - A & B permanently lower/raise the pitch by 1%
  - The slider is the pitch slider
  - The long button at the bottom temporarily raises the pitch by 4% for
    as long as you hold it (pitch bend up.)
  - The short circle button beneath that temporarily lowers the pitch by
    4% for as long as you hold it (pitch bend down.)
  - Channel column 4's knobs affect global parameters:
  - High = Depth
  - Mid = Delay
  - Low = LFO
  - Pan = Balance (master)
  - Global knobs (upper right) do as they're labeled, except Zone which
    does nothing.
  - BPM tap buttons are just below the global knobs. Left one is for
    Deck 1, right one for Deck 2. (Middle one does nothing.)
  - Bank Down and Up select between Library, Play Queue, Browse and
    Playlists.
  - Track select:
  - The big knob scrolls through tracks (only forwards at the moment)
  - The Cancel button scrolls backwards one at a time
  - Pressing the knob loads the selected track into the first stopped
    deck

You can change which mixer controls get mapped to what Mixxx functions
just by editing the XML file. See the [MIDI Mapping file
format](midi_controller_mapping_file_format#old_format_before_schema_versioning_mixxx_1.6.1_and_prior)
for details.

#### Quirks

(all are resolved in Mixxx 1.7.0)

  - The big track select knob only goes forwards
  - The channel jog knobs are backwards
