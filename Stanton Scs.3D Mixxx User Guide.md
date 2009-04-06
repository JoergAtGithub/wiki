# Stanton SCS.3d & Mixxx User Guide

This guide explains how the SCS.3d is mapped by default in Mixxx.

[[/media/hardware/stantonscs/scs3d_preset.jpg|]]

***Easy customization:*** We have provided the following customization
variables at the top of the script you can set to your liking:

  - **pitchRanges** - Set the pitch slider range when the Pitch LED is
    off, blue, purple and red (in decimal values. E.g. 0.08 = 8%, 0.5 =
    50%)
  - **fastDeckChange** - If set to true, changes decks instantly by
    skipping the flashing lights. Useful for beat juggling on one unit.
  - **spinningPlatter** - If set to true, uses the circle LEDs to show
    the track position in vinyl and vinyl2 modes (also useful for
    juggling.)
  - **markHotCues** - Set to `"blue"` or `"red"` (with quotes) to choose
    which LEDs mark the stored positions in TRIG & LOOP modes
  - **jogOnLoad** - If true, the unit will automatically change to Vinyl
    (jog) mode after loading a track (from Track Select mode)
  - **globalMode** - If true, the unit will stay in the current mode on
    deck changes (instead of switching to the mode you were in the last
    time you controlled that deck.)

Just open the `midi/Stanton-SCS3d-scripts.js` file in your favorite text
editor (Wordpad works too) and you'll see these variables right near the
top. Edit & save, then restart Mixxx and enjoy.

## Mode buttons

[[/media/hardware/stantonscs/modebuttons.jpg|]]

  - FX - Adjust & toggle Flanger effect, toggle reverse effect
  - EQ - Adjust channel EQ parameters
  - Loop - Instant pitch changes (until Mixxx supports looping.)
  - Trig - Hot cues
  - Vinyl - Toggle between pitch bend, vinyl manipulation & scratching,
    and track selection
  - Deck - Adjust cross-fader and switch to the other virtual deck

#### Common to all modes:

(except where noted)

  - Gain slider (S1) adjusts deck volume
  - Pitch slider (S2) adjusts deck pitch control
  - B11 toggles headphone cue
  - B12 toggles pitch range (black=8%, blue=12%, purple=50%, red=100%)
  - B13 Rewind (REW)
  - B14 Fast Forward (FFWD)

**While holding down the current mode button:**

  - Gain slider (S1) adjusts pre-fader gain
  - Pitch slider (S2) finely adjusts pitch control
  - B12 resets pitch to center 0%

**While holding down Deck button:**

  - Center slider (S4) adjusts the cross-fader
  - B12 resets cross-fader to center position

## FX Mode

[[/media/hardware/stantonscs/slidermode.jpg|]]

  - Left slider (S3) adjusts flanger depth
  - Center slider (S4) adjusts flanger delay
  - Right slider (S5) adjusts flanger period (Low Frequency Oscillator)
  - B11 plays track in reverse while held down
  - B12 toggles flanger effect

## EQ Mode

[[/media/hardware/stantonscs/slidermode.jpg|]]

  - Left slider (S3) adjusts low frequency equalizer
  - Center slider (S4) adjusts mid frequency equalizer
  - Right slider (S5) adjusts high frequency equalizer

## Loop Mode

This will control looping in a future version of Mixxx. For now, it
offers instant pitch change buttons in the following arrangements:

**Fixed increment (red)** - Each button sets the pitch 3.33% above or
below its vertical neighbors.

**Key change (purple)** - Center buttons are one half tone away from
their vertical neighbors and the outside ones are three half tones away
(for harmonic key changes.)

**Notes (black)** - Buttons correspond to major scale notes (ala Vestax
Controller One.) This is most useful with a constant-pitch sound or
chord. (You can generate one in Audacity.)

Remember you can return to the original pitch (tonic) by holding down
LOOP and pressing B12 (under the pitch slider.)

Note that when you switch to Loop mode, the pitch range is automatically
set to 100% in order for these buttons to work correctly.

*Key change and Note modes were tuned with respect to 440Hz A (above
middle C.)*

## Trig Modes

These modes configure the surface as 9 buttons (lit up dim red for
visibility.)

The red LEDs flash when you press the corresponding button. The outer
blue LEDs light when a cue point is set on that button.

  - To set a cue, just press a free button at the desired time.
  - To recall a cue, just press a button that has a cue point set
  - To erase a cue, hold TRIG while pressing the button(s) you want to
    erase

## Vinyl Modes

[[/media/hardware/stantonscs/circlemode.gif|]] **Vinyl mode (red)**

  - Outer circle (C1) allows you to bend the song's pitch, akin to
    dragging your finger on the record
  - Center slider (S4) allows you to "scratch" the song

**Vinyl2 Mode (purple)**

  - Outer circle (C1) allows you to "scratch" the song and perform
    juggles
  - Center slider (S4) allows you to "scratch" the song

**Track Select Mode (black)**

  - Outer circle (C1) allows you to scroll through your Library
  - Center button (anywhere on S4) loads the currently highlighted song
    into the first stopped deck
  - B11 selects backward between Library, Playlist, and Browse views
  - B12 selects forward between Library, Playlist, and Browse views
  - B13 moves the highlight up one item
  - B14 moves the highlight down one item

## 

*Images courtesy of Stanton Magnetics, Inc.*
