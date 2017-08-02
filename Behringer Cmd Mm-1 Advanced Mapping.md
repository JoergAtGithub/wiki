# Behringer CMD MM-1 Advanced Mapping

This is my Advanced mapping for the Behringer CMD MM-1. Its main focus
was not to make a complete mapping for the whole CMD series, but instead
to add the features that the mapping for the Novation Launchpad MK2 is
missing. [Mixxx mapping for Novation Launchpad
🦄](novation_launchpad_mapping_by_szdavid92) Thanks to Mevsme for the
3D-Model of the controller.

[[/media/hardware/behringer/behringercmdmm1overview.png|]]

### The concept

Similar to the mentioned Launchpad Mapping, this mapping features two
modifiers: \[*SHIFT*\] and \[**CTRL**\] These allow each button to have
up to four functionalities. They behave like the normal shift and
control keys on your PC-Keyboard. Most of the features can be explained
via the renderings where the functionalities are marked via the
formatting of the Text (\[*SHIFT*\] and \[**CTRL**\])

### Global variables

There are four global variables at the top of the script:

  - CHANNELNUMBER: The standard channelnumber of the CMD MM-1 is 5 but
    it can differ. If thats the case you can change it here
  - INVERTCOLOR: Swaps the colors which suits certain skins more
  - STANDARDCHANNELSEQUENCE: Defines if the channels laid out in
    \[1,2,3,4\] or \[3,1,2,4\] sequence by default.
  - STANDARDKNOBBEHAVIOR: Defines the default mapping of the knobs.

### The top row

[[/media/hardware/behringer/behringercmdmm1-toprowlabeled.png|]]

The Out1 and Out2 buttons didn't have any obvious functionality so they
control the knobs of the EffectUnits. You can see that they control the
super-knobs of FxUnit1 & FxUnit2 in normal mode (no formating), The
mix-knobs of FxUnit1 & FxUnit2 in shift mode (*italic*), the super-knobs
of FxUnit3 & FxUnit4 in ctrl mode (**bold**) and the mix-knobs of
FxUnit3 & FxUnit4 in thirdMode (***bold\&italic***).

You can see the L/R buttons besides the encoder as shift- and
ctrlbuttons.

The Encoder in the middle is able to browse the library and jump on the
previewdeck (16 steps) while holding shift. When pressing the encoder,
the selected/highlighted track in the library gets loaded into the
previewdeck. The Previewdeck can be played/paused when holding shift
while pressing the encoder down.

The Cue Vol/Mix knobs have no alternative functionality.

### Knob unit

[[/media/hardware/behringer/behringercmdmm1-knoboptionslabeled.png|]]

The Knobs have three different mappings which can be cycled while in
operation. (more on that later) The first one is the standard
\[High,Mid,Low,Quickeffect\]-Combo. The second one shifts everything up
and is mapped to \[Gain,High,Mid,Low\] which some DJs might prefer. The
third one controls the EffectUnits \[Meta1,Meta2,Meta3,Mix\]. The
Effectunit is based on the channel/deck number, so the channel that
controls the knobs/buttons/faders of channel 1 also controls the knobs
of EffectUnit1, Channel 2 controls EffectUnit2, etc.

### MiddleButton/exShift ;-)

[[/media/hardware/behringer/behringercmdmm1-knobslabeled.png|]]

Normal: toggle maximize library, Shift: recenter Crossfader Ctrl: Cycle
Knob assignment (swaps the mapping of the knobs as mentioned earlier.
Third: Reassing Channel Sequence (Swaps between \[3,1,2,4\] to
\[1,2,3,4\])

### Buttons

[[/media/hardware/behringer/behringercmdmm1-buttonslabeled.png|]]

\[1\]&\[2\] Buttons:

  - Normal: Toggle Fx1&2 for desired Channel
  - Shift: Change Crossfaderside (Orientation)
  - Ctrl: Toggle Fx3&4 for desired Channel

\[CUE\] Buttons:

  - Pre-Fader-Listening
  - Load selected Track to Deck
  - Enable Fx-PFL for Unit according to channel number.
  - reset BPM-Fader FIXME

### Faders

[[/media/hardware/behringer/behringercmdmm1-fadeslabeled.png|]]

  - Normal: Volume Fader
  - Shift: Rate-/BPM-Faders
