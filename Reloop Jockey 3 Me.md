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

Set the Input 1 and Input 2 switches on the front side of the Jockey 3
ME to SW.

## Mixxx Sound Hardware Preferences

  - Master output: channels 1-2
  - Headphone output: channels 3-4
  - Auxiliary or vinyl input 1: channels 1-2
  - Auxiliary or vinyl input 2: channels 3-4
  - Microphone input: channels 5-6

## Mapping Guide

### Mixer Section

  - **Trax encoder**: scroll through library. With shift, scroll through
    sections on the left side of the library. Push to toggle big
    library.
  - **Load button**: load selected track into active deck
  - **Deck switches**: select between controlling deck 1/3 or analog
    input 1 on the left; select between controlling deck 2/4 or analog
    input 2 on the right. Note that the analog inputs are only affected
    by the mixer controls but not the other deck controls.
  - **Gain**: set [deck
    gain](http://mixxx.org/manual/latest/chapters/user_interface.html#equalizers-and-gain-knobs)
  - **High/mid/low**: adjust EQ for high/mid/low frequencies
  - **Master/booth/phones**: control the volume Jockey 3 ME's sound
    card's master/booth/headphone output. These knobs do not send MIDI
    messages or adjust values in Mixxx, so turning them will not change
    anything on screen. Use these but not the software knobs on screen
    in Mixxx (see [the Mixxx
    manual](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-gain-knob)
    for an explanation).
  - **Headphones**: play deck on headphone output
  - **Cuemix**: Fade between PFL and master output on headphones
  - **Vertical faders**: deck volume
  - **Level meter LEDs**: show the level of the deck
  - **Crossfader**: fade between decks
  - **Crossfader curve** (front side of controller): Adjust crossfader
    curve between fade and cut.

### Transport Section

  - **Play/pause**: play/pause or, with shift, toggle keylock
  - **Cue**: behavior depends on [cue mode set in Mixxx
    preferences](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
  - **Cup**: Like Cue, but it plays only after releasing the button.
  - **Sync**: toggle master sync

### Jogwheels

  - **Scratch mode**: If Active, you can Scratch the current loadet file
    in this Deck. If you touch the oudside Rubber ring, you can push or
    pull the speed of a playing file.
  - **Nudging mode**: Not Mapped. FIXME (No plans)
  - **Search mode**: Not Mapped. FIXME (In future planed)
  - **Note mode**: Not Mapped. FIXME (Plan to Control the SuperKnop on
    the EffectChain of the Deck)

#### Pitch Fader

  - Sets a new speedrate of the playing Deck.

### Hotcue Section

Press an unlit hotcue button to set that hotcue at the current position.
Press a lit hotcue button to jump to that hotcue. To delete a hotcue,
hold the Trash button while pressing a hotcue. To toggle between hotcues
1-4 and 5-8, press the 5-8 button.

### Loop Section

  - **Length encoder**: Press to activate a 4 beat loop. Double or half
    the beats of the loop by turning
  - **Move encoder**: Move a track 4 Beats forward or backward.
  - **Loop button**: ??? FIXME. With shift, sets the start position of a
    loop.
  - **Reloop button**: does not work as labeled; toggles quantize. With
    shift, sets the end position of a loop.

### Other controls

  - **Filter**: turn to apply a highpass or lowpass filter. On Deck A,
    press Shift and turn Filter to adjust the Gain of the Microphone
  - **Pan**: On Deck A, turn to fade between the left and right speakers
    on the master output. (Balance)
  - **\< Beat**: does not function as labeled. It aligns the beatgrid
    with the current play position. With shift, moves the beatgrid lines
    further from each other (lower BPM by 0.01)
  - **Beat \>**: Not as intended it do Microphone Talkover. With shift,
    moves beatgrid lines closer to each other (raise BPM by 0.01)

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
