# Hercules DJ Control Compact

[[/media/hercules-djcontrol-compact_angle.jpg|]]

[[/media/hercules-djcontrol-compact_top.jpg|]]

  - [Manufacturer's product
    page](https://www.hercules.com/us/DJ-Music/bdd/p/253/djcontrol-compact/)
  - Mapping download: [XML
    file](https://raw.githubusercontent.com/mixxxdj/mixxx/master/res/controllers/Hercules%20DJControl%20Compact.midi.xml)
    and [JS
    file](https://raw.githubusercontent.com/mixxxdj/mixxx/master/res/controllers/Hercules-DJControl-Compact-scripts.js)
    (compatible with Mixxx 2.0)

The Hercules DJ Control Compact is a simple controller for basic
two-channel mixing. This device does not have a built in sound card, so
it would require a [splitter
cable](hardware%20compatibility#splitter%20cables) or [separate sound
card](hardware%20compatibility#usb%20sound%20cards) to be able to
preview tracks in headphones. It also does not have buttons for routing
decks to headphones.

Thanks to Hercules for supporting the development of this mapping by
providing a controller.

## Mapping description

The play/pause buttons, EQ knobs, volume knobs, and crossfader all
behave as labeled. If you would like to change the mapping of the EQ
knobs (for example to change the volume knob to control the high EQ and
use the crossfader for volume), use the [MIDI Mapping
Wizard](http://mixxx.org/manual/latest/chapters/advanced_topics.html#controller-wizard)
or [edit the XML file](MIDI%20controller%20mapping%20file%20format).

Shift + Play jumps to the beginning of the track and stops playback.

The cue button behaves differently depending on the [cue mode set in
Mixxx's
Preferences](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes).

The sync button synchronizes the tempo to the other deck. Press and hold
sync to engage [Master
Sync](http://mixxx.org/manual/latest/chapters/djing_with_mixxx.html#master-sync).

There is only one each of the Mode, Shift, and Scratch buttons, so they
affect both decks.

Shift + Scratch (Automix) toggles AutoDJ on/off.

### Jog Wheels

When Scratch is off, turning a jog wheel bends the pitch of the track.
When Scratch is on, turning a jog wheel scratches that deck. Holding
Shift and turning a jog wheel adjusts the playback rate (tempo). Enable
keylock on a deck by clicking the music note button on screen if you do
not want the pitch to change when adjusting the tempo.

### Pad Grid

Press the MODE button to cycle through each pad mode.

#### Loop mode

In loop mode, the buttons are mapped in a way that's more artistically
expressive:

  - Button 1 enables and disables the loop
  - Button 2 enables an 8 beat loop
  - Button 3 divides the current loop in half
  - Button 4 doubles the length of the current loop
  - Shift + Button 1 performs an 1/8th beat roll
  - Shift + Button 2 performs an 1/4th beat roll
  - Shift + Button 3 performs an 1/2th beat roll
  - Shift + Button 4 performs an 1 beat roll

#### FX mode

  - Button 1 enables and disables the first FX chain for Channel 1
  - Button 2 enables and disables the second FX chain for Channel 1
  - Button 1 enables and disables the first FX chain for Channel 2
  - Button 2 enables and disables the second FX chain for Channel 2

Shift-FX buttons are not mapped.

#### Sampler mode

  - Left side buttons play Sample Decks 1 through 4
  - Right side buttons play Sample Decks 5 through 8
  - Shift + Buttons stops Sample Deck and puts the playhead at the cue
    point

#### Cue mode

  - Each button activates the hotcue with that number
  - Shift + button clears the hotcue with that number

## MIDI Mapping Reference

Much of the Compact's behavior is hard-coded into its firmware,
including shift button messages and button mode selections.

<http://ts.hercules.com/download/sound/manuals/DJC_Compact/DJC_Compact_MIDI_Mapping.pdf>
