# Stanton SCS.3d "DaScratch"

[[/media/hardware/stantonscs/scs3dangle.jpg|scs3dangle.jpg]]

Link to the website: <http://www.enterthesystem.com/system/scs3d/>

## Latest MIDI mapping & script files

### 1.6.1 & prior

DaRouter mapping for use with Mixxx up to v1.6.1:
[[/media/hardware/stantonscs/stanton_scs.3d_darouter.midi.xml.gz|]]

This is more of a preview release to get you started until we release
Mixxx 1.7.0 which will feature full native support and customization for
the SCS.3d.

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

You can change which SCS.3d controls get mapped to what Mixxx functions
just by editing the attached file. See the [MIDI Mapping file
format](midi_controller_mapping_file_format#old_format_before_schema_versioning_mixxx_1.6.1_and_prior)
for details.

#### Quirks

(all will be resolved in the next Mixxx release)

  - Scratching doesn't work well so is disabled.
  - Circle C1 acts as a jog dial, but it's backwards (relative to a
    record,) and a bit sensitive.
  - Mixxx has just one set of adjustments for the flanger effect and
    track select, so you can only operate them with Deck A selected.
    (Functions can only be mapped to one control at the moment.)

### 1.7.0+

The latest official MIDI mappings and script files will be available
here after Mixxx 1.7.0-beta1 is released.

[Mixxx user's guide for the SCS.3d](stanton_scs.3d_mixxx_user_guide)
