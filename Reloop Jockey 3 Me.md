# Reloop Jockey 3 Master Edition

![http://www.reloop.com/media/catalog/product/2/2/4/224649\_Reloop\_TP.jpg](http://www.reloop.com/media/catalog/product/2/2/4/224649_Reloop_TP.jpg)

The Reloop Jockey 3 Master Edition is a 2 Channel Controller with the
option to control 4 Channels. It is Designed for Traktor Pro 1. This is
a Documentation to use this Controller with Mixxx.

  - [Mixxx Forum
    Thread](http://mixxx.org/forums/viewtopic.php?f=7&t=5418)
  - [Manufacturer's product
    page](http://www.reloop.com/reloop-jockey-3-me)
  - [Manufacturer's
    manual](http://www.reloop.com/media/catalog/product/pdf/2/2/4/224649_Reloop_IM.pdf)
  - [Review from
    Digitaldjtips.com](http://www.digitaldjtips.com/2011/05/review-video-reloop-jockey-iii-me-controller/2/)

# Setup

The Mixxx mapping uses the same settings as Reloop's Traktor mapping.
Leave the MIDI channels as the default 1-4. If you have problems with
the jogwheels, set the jogwheel resolution to 2048. (Please read the
manual of this Controller section **5.1** and **5.1.2**)

## Mixxx Sound Hardware Preferences

  - Master output: channels 1-2
  - Headphone output: channels 3-4
  - Auxiliary or vinyl input 1: channels 1-2
  - Auxiliary or vinyl input 2: channels 3-4
  - Microphone input: channels 5-6

## Mapping Guide

### Mixer Section

  - Trax Knob: scroll through library. With shift, scroll through
    sections on the left side of the library. Push to toggle big
    library.
  - Load button: load selected track into active deck
  - Deck switches: select between controlling deck 1/3 or analog input 1
    on the left; select between controlling deck 2/4 or analog input 2
    on the right. Note that the analog inputs are only affected by the
    mixer controls but not the other deck controls.
  - Gain: set [deck
    gain](http://mixxx.org/manual/latest/chapters/user_interface.html#equalizers-and-gain-knobs)
  - High/mid/low: adjust EQ for high/mid/low frequencies
  - Master/booth/phones: control the Jockey 3 ME's sound card. These
    knobs do not send MIDI messages or adjust values in Mixxx, so
    turning them will not change anything on screen. Use these but not
    the software knobs on screen in Mixxx (see [the Mixxx
    manual](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-gain-knob)
    for an explanation).
  - Headphones: play deck on headphone output
  - Cuemix: Fade between PFL and master output on headphones
  - Vertical faders: deck volume
  - Level meter LEDs: show the level of the deck
  - Crossfader: fade between decks
  - Crossfader curve (front side of controller): Adjust crossfader curve
    between fade and cut.

### Transport Section

#### Play/Pause

  - Play/Pause chosen Deck

#### Cue

  - If Pushed while Playing or the playposition is allready on Cue
    point, the Deck will Jump to the last Cue point and play while
    holding it. If released it jumps back to cue point. Otherwise it
    will set a Cue point.

#### Cup

  - Like Cue, but it plays only after releasing the button.

#### Sync

  - Sets the Pitch to the Speed of the opposite Deck.

#### Keylock

  - Push Shift and Play/Pause to set Keylock. If set the pitch dosn't
    effect the Key of the file but the speed.

#### Jogwheels

  - **Scratchmode**: If Active, you can Scratch the current loadet file
    in this Deck. If you touch the oudside Rubber ring, you can push or
    pull the speed of a playing file.
  - **Nudgingmode**: Not Mapped. FIXME (No plans)
  - **Searchmode**: Not Mapped. FIXME (In future planed)
  - **Notemode**: Not Mapped. FIXME (Plan to Control the SuperKnop on
    the EffectChain of the Deck)

#### Pitch Fader

  - Sets a new speedrate of the playing Deck.

### Hotcue Section

  - Like Cue or Cup you can set 8 Hotcues per deck on this Controller.
    If you want to Delete a Hotcue push and hold the Trash Button and
    push now the Hotcues you want to delete. Hotcue 5-8 must be
    aktivated on "5-8".

### Loop Section

#### Length turning

  - By turning double or half the Beats of a active Loop.

#### Move turning

  - Move a track 4 Beats forward or backward.

#### Length push

  - By pushing the Length knop you apply a 4 Beat Loop.

#### Filter

  - Turn it to apply a highpass or lowpass filter.

#### Shift Filter

  - On Deck A you can press Shift and turn Filter to adjust the Gain of
    the Microphone

#### Pan

  - On Deck A you can turn Pan to fade to the left or right Speaker for
    Master output. (Balance)

#### Loop

"reloop\_exit" FIXME

#### Loop In

  - Sets of a new Loop the beginning position of a loop.

#### Reloop

  - This Button don't work as intended. It Sets Quantize instaed.

#### Loop Out

  - Sets the end position of a Loop if "Loop In" was pressed.

#### \<Beat

  - Not as intended it sets the Beatgrid aligne to the Playposition.

#### \<Grid

  - As intended adjusts the Beadgrid lower, means the Grid gets more
    space to echother.

#### Beat\>

  - Not as intended it do Microphone Talkover.

#### Grid\>

  - Beadgrid higher. Grid gets less space to echother.

### Effect Section

  - Deck A has EffectChain1
  - Deck B has EffectChain2
  - Deck C has EffectChain3
  - Deck D has EffectChain4

#### FX Sel. (Adv)

  - To Select a Effect Hold Shift and turn "Dry/Wet" means "FX Sel.
    (Adv)" to select a Effect.

#### Preset1 - Preset4

  - To chose the Deck you want to apply the Effect, press and hold shift
    and then Preset1 for Deck A, Preset2 for Deck B and so on.

#### Dry/Wet

  - If you turn Dry/Wet you Control the Volume of this Effect or in
    Software the "mix" knop.

#### FX on

  - Press this Button to enable or disable the EffectChain. (Default
    enabled)

#### FX Param

  - Turn a Parameter in Effect Chain. The fourth is actualy not Mapped.
    FIXME

#### FX Sel.X (Cha)

  - FIXME (Plan to Select the EffectX. And for Pushing a Selection mode
    for Linking the SuperKnop on Jogmode)
