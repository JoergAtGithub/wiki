# Stanton SCS.1m

[[/media/hardware/stantonscs/scs1mproductshot.png|]]

Link to the website: <http://www.enterthesystem.com/system/scs1m_mixer/>

## Latest MIDI mapping & script files

### 1.6.1 & prior

Mapping for use with Mixxx up to v1.6.1:
[[/media/hardware/stantonscs/stanton_scs.1m_1.60.midi.xml.gz|]]

This is more of a preview release to get you started until we release
Mixxx 1.7.0 which will feature full support and customization for the
SCS.1m.

#### Instructions

1.  Unpack the above file into:

<!-- end list -->

  - Windows: C:\\Program Files\\Mixxx\\midi
  - OS X: /Applications/Mixxx.app/Contents/midi
  - Linux is waiting on protocol support for the SCS.1 series. As soon
    as that's ready, this'll work\!

<!-- end list -->

1.  Start Mixxx, open Preferences, choose Input Controllers, the
    "Stanton SCS.1m 1.60" mapping, and the "From SCS.1" device. Click
    OK, click OK on the 'Warning: No \<midino\> defined in MIDI map
    node: "control"' and you're good to go.

**If you don't see the device in the list or Mixxx doesn't respond to
it**, you may need to run DaRouter to get communication (this is true on
Windows.) In this case:

``` 
  - Download & unpack the {{:hardware:stantonscs:scs.1m_thru.bmtp.gz|SCS.1m_thru}} DaRouter preset
  - Start DaRouter and browse to where you saved it. Select & open it.
  - Follow from step 2 above.
```

#### Notes

  - The middle two channel columns are for decks 1 & 2. (Left for 1,
    Right for 2)
  - The buttons above the gain knobs at the top are the headphone cues
  - The encoder knobs act as jog wheels
  - Pressing the encoder knobs toggles the flange effect
  - A & B are REWind and FastForward, respectively
  - The long button at the bottom is Play/Pause
  - The short circle button beneath that is Cue.
  - The pan knob isn't assigned to anything (Mixxx doesn't support
    channel panning)
  - Channel columns 1 & 4 control things for decks 1 & 2 respectively:
  - The circle button at the top syncs the song with that on the other
    deck (assuming the BPM detector worked correctly on both)
  - Pressing the encoder knob toggles reverse playback (rotating it does
    nothing)
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

(all will be resolved in the next Mixxx release)

  - The big track select knob only goes forwards
  - The channel jog knobs are backwards

### 1.7.0+

The latest official MIDI mappings and script files will be available
here after Mixxx 1.7.0-beta1 is released.

[Mixxx user's guide for the SCS.1m](stanton_scs.1m_mixxx_user_guide)
