# Stanton SCS.1m

[[/media/hardware/stantonscs/scs1mproductshot.png|]]

Link to the website: <http://www.enterthesystem.com/system/scs1m_mixer/>

## Latest MIDI mapping & script files

### 1.6.1 & prior

Mapping for use with Mixxx up to v1.6.1 *Coming soon*

This is more of a preview release to get you started until we release
Mixxx 1.6.2 which will feature full support and customization for the
SCS.1m.

#### Instructions

1.  Unpack the above file into:

<!-- end list -->

  - Windows: C:\\Program Files\\Mixxx\\midi
  - OS X: /Applications/Mixxx.app/Contents/midi

<!-- end list -->

1.  Then start Mixxx, open Preferences, choose Input Controllers, the
    "Stanton SCS.1m 1.6.0" mapping, and the "From SCS.1" device. Click
    OK and you're good to go.

**If you don't see the device in the list or Mixxx doesn't respond to
it**, you may need to run DaRouter to get communication (this is true on
Windows.) In this case:

``` 
  - Download the "SCS.1m_thru" preset from Stanton
  - Start DaRouter and browse to where you saved it. Select & open it.
  - Follow from step 2 above.
```

#### Notes

  - Channel strips 1 & 2 are for decks 1 & 2.
  - The buttons above the gain knobs are the headphone cues
  - Pressing the encoder knobs toggles the flange effect (rotating the
    knob does nothing)
  - A & B are REWing and FastForward, respectively
  - The long button at the bottom is Play/Pause
  - The short circle button beneath that is Cue.
  - The pan knob isn't assigned to anything (Mixxx doesn't support
    channel panning)
  - Channel strips 3 & 4 control things for decks 1 & 2 respectively:
  - The circle buttons at the top sync the song with that on the other
    deck (assuming the BPM detector worked correctly)
  - Pressing the encoder knobs toggles reverse playback
  - A & B permanently lower/raise the pitch by 1%
  - The long button at the bottom temporarily raises the pitch by 4% for
    as long as you hold it (pitch bend up.)
  - The short circle button beneath that temporarily lowers the pitch by
    4% for as long as you hold it (pitch bend down.)
  - Channel strip 4's knobs affect global parameters:
  - High = Depth
  - Mid = Delay
  - Low = LFO
  - Pan = Balance
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

  - The one-way knob

### 1.6.2+

The latest official 1.6.2 MIDI mappings and script files will be
available here after Mixxx 1.6.2 is released.

[Mixxx user's guide for the SCS.1m](stanton_scs.1m_mixxx_user_guide)
