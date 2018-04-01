# Behringer CMD MM-1

[[/media/hardware/behringer/behringer_cmd_mm-1-overall.jpg|behringer\_cmd\_mm-1-overall.jpg]]
[[/media/hardware/behringer/behringer_cmd_mm-1-overall-irl.jpg|behringer\_cmd\_mm-1-overall-irl.jpg]]

  - [Forum
    thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=9276)

The Behringer CMD MM-1 is a flexible controller that controls 4 decks by
default. The mapping can be easily configured to control any combination
of decks and effect units. The [Behringer CMD DC-1](behringer_cmd_dc-1)
and [Behringer CMD DV-1](behringer_cmd_dv-1) are designed to be used
together with the CMD MM-1, but the CMD MM-1 can be used alone or with
other controllers.

The pictures above are a render and a real life photo. All following
examples will be made with a help of a [3D
model](http://stunkit.com/data/files/etc/cmd-mm-1.blend.zip).

This demonstration video shows how the mapping works by default with
every channel in Deck mode:
[[[/media/hardware/behringer/behringer_cmd_mm-1-youtube.jpg|behringer\_cmd\_mm-1-youtube.jpg]]](https://www.youtube.com/watch?v=33t6J1hUFjM)

## Mapping description

### Mapping options

There are a few user configurable options available for you to
customize. You can change these by opening the
`Behringer-CMD-MM-1-scripts.js` file in your [controller mapping file
locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder)
with your text editor of choice (such as Notepad, TextEdit, Kate, or
gEdit) and editing the lines at the very top of the file.

  - channelNumber: The standard MIDI channel number of the CMD MM-1 is 5
    but it can differ. If that is the case, you can change it here.
  - invertColor: Swaps the colors which suits certain skins more
  - defaultChannelSequence: Defines how the channels are mapped when
    Mixxx starts
  - channelMode: Defines if a channel is in Deck or FX Mode when Mixxx
    starts
  - standardKnobBehavior: Defines the mapping of the knobs when Mixxx
    starts

### Top row

[[/media/hardware/behringer/behringercmdmm1-toprowlabeled.png|]]

The top left knobs control the Master balance and Master gain. The top
right knobs control the headphone gain and cue mix (PFL/master mix in
Headphones output).

You can see the L/R buttons besides the encoder as \[*SHIFT*\] and
\[**CTRL**\] buttons. These allow each button to have up to four
functionalities. They behave like the Shift and Control keys on a
computer keyboard. Most of the features can be explained via the
renderings where the functionalities are marked by the formatting of the
Text (\[*SHIFT*\] and \[**CTRL**\]).

The encoder in the middle is able to browse the library and jump on the
preview deck (16 steps) while holding shift. When pressing the encoder,
the selected/highlighted track in the library gets loaded into the
preview deck. The preview deck can be played/paused when holding shift
while pressing the encoder down.

### Knobs

[[/media/hardware/behringer/behringercmdmm1-knoboptionslabeled.png|]]

The Knobs have three different modes which can be cycled while in
operation. The knobs in each mode, from top to bottom, control:

1.  Deck: High, Mid, Low, QuickEffect (filter by default)
2.  Deck: Gain, High, Mid, Low
3.  Effect Unit: Meta 1, Meta 2, Meta 3, Mix

The Effect Unit number is the same as the channel/deck number, so the
channel that controls the knobs/buttons/faders of deck 1 also controls
the knobs of EffectUnit1, Channel 2 controls EffectUnit2, and so on.

### FX Mode

[[/media/hardware/behringer/channelstriplabeled-min.png|]]

The Knobs in FxMode overwrite the assigned mapping and are mapped as
\[Effect 1 Meta, Effect 2 Meta, Effect 3 Meta, Super\] and the fader is
also mapped to the mix of the EffectUnit. The buttons are documented in
their own section.

#### MiddleButton/exShift

[[/media/hardware/behringer/behringercmdmm1-knobslabeled.png|]]

  - Normal: toggle maximize library
  - Shift: recenter Crossfader
  - Ctrl: Cycle Knob assignment (swaps the mapping of the knobs as
    mentioned earlier.
  - Third: Reassing Channel Sequence (resets mapping back do the global
    defaults (look at global vars))

#### Buttons

#### Deck Mode

[[/media/hardware/behringer/buttons_orientationlabeled-min.png|]]

\[1\]&\[2\] Buttons:

  - Normal: Change Crossfader side (Orientation)
  - Shift: Toggle Fx1&2 for desired Channel
  - Ctrl: Toggle Fx3&4 for desired Channel
  - Third: Change ChannelNumber/Assignment

\[CUE\] Buttons:

  - Normal: Pre-Fader-Listening
  - Shift: Load selected Track to Deck
  - Ctrl: Enable Fx-PFL for Unit according to channel number.
  - Third: Change Channelmode

#### FX Mode

[[/media/hardware/behringer/buttonsofflabeledfxmode-min.png|]]

\[1\]&\[2\] Buttons:

  - Normal: Toggle Channel1&2 for desired FxUnit
  - Shift: Toggle Channel3&4 for desired FxUnit
  - Ctrl: Toggle Effect 1&2 in desired FxUnit
  - Third: Change ChannelNumber/Assignment

\[CUE\] Buttons:

  - Normal: Pre-Fader-Listening for FxUnit
  - Shift: assign to master
  - Ctrl: Toggle Effect 3 for desired FxUnit
  - Third: Change Channelmode

### Faders

[[/media/hardware/behringer/behringercmdmm1-fadeslabeled.png|]]

DeckMode:

  - Normal: Volume Fader
  - Shift: Rate-/BPM-Faders

FxMode:

  - EffectUnit Mix (dry/wet)

### Reassigning channel mode and number

The channel modes and numbers can be set by changing the [\#mapping
options](#mapping%20options) at the top of the script. They can also be
changed while using the controller when in ***thirdMode***. Pressing the
cue- button toggles between Deck and FX Mode. The Channel number is
assigned with the \[1\]&\[2\] buttons.

They are mapped in a sort of two bit encoded system:

  - \[ \] & \[ \] = Channel 1
  - \[x\] & \[ \] = Channel 2
  - \[ \] & \[x\] = Channel 3
  - \[x\] & \[x\] = Channel 4

So you can change between channel 1&3 by pressing the \[1\] button, and
channel 2&4 by pressing the \[2\] button.

## Troubleshooting

### Controller does not light up

The issue is probably the MIDI channel of your MM-1. Behringer has a
tool that can set the controller to a different MIDI channel. So your
controller is probably set to the wrong channel. The easiest way to fix
this is to use Behringers tool and set it do MIDI channel 5.
<https://musicgroup-prod.mindtouch.us/04_BEHRINGER/CMD-_How_Do_I_Change_MIDI_Channel_On_My_CMD_Controller%3F>
If you can't do that for some reason, you have to find out the channel
your MM-1 is sending on at the time. Once you know that you should go
change the line where it says "var CHANNELNUMBER = 5;" of the file
"Behringer-CMD-MM-1-Advanced.js" in the folder with the mappings so
there is the number of your channel instead of the 5. (IMPORTANT: NO
PARENTHESES). The you have to find the file "Behringer
CMD-MM-1.midi.xml" in the same folder and replace the 4 at the end of
0x94, 0x84 and 0xB4 with your CHANNEL-NUMBER MINUS 1. Restart Mixxx and
then it should work.
