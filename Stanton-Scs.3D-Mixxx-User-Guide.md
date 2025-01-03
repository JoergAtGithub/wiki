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
  - **spinningPlatter** - If set to true, uses the circle LEDs to
    *accurately* (<span class="underline">no sticker drift\!</span>)
    show the track position in record revolutions, also useful for
    juggling.
  - **spinningPlatterOnlyVinyl** - If set to true, only shows the
    spinning platter LED in vinyl modes. Otherwise shows in all modes
    except Loop, Instant Pitch Change and TRIG (because they're used for
    other things in those modes.)
  - **spinningLights**<sup>1</sup> - The number of lights used for the
    spinning platter effect, 1 or 2. (1 is best for juggling.)
  - **VUMeters** - If set to true, shows a VU meter in the circular area
    for the currently selected deck when in vinyl mode. (Left for deck
    1, right for deck 2.)
  - **markHotCues** - Set to `"blue"` or `"red"` (with quotes) to choose
    which LEDs mark the stored positions in TRIG & LOOP modes
  - **jogOnLoad** - If true, the unit will automatically change to Vinyl
    (jog) mode after loading a track (from Track Select mode)
  - **globalMode** - If true, the unit will stay in the current mode on
    deck changes (instead of switching to the mode you were in the last
    time you controlled that deck.)
  - **singleDeck**<sup>1</sup> - If you've got more than one MIDI
    controller, set this to true to have the SCS.3d stay on one deck and
    make Deck mode non-temporary. [More on this here](#deck-mode).
  - **deckChangeWait** - Time in milliseconds to hold the DECK button
    down to avoid changing decks
  - **pitchAdjustment**<sup>2</sup> - Adjusts the coarseness of the
    pitch slider (1=coarse, 3=normal, 5=fine)
  - **finePitchAdjustment**<sup>2</sup> - Adjusts the coarseness of the
    pitch slider in fine mode (1=coarser, 3=normal, 5=finer)
  - **finePitchDefault**<sup>2</sup> - If true, swaps normal and fine
    pitch modes so you can use fine pitch mode unshifted

<sup>1</sup> Introduced in Mixxx v1.8.0 <sup>2</sup> Introduced in Mixxx
v1.9.1

Just open the `midi/Stanton-SCS3d-scripts.js` file in your favorite text
editor (Wordpad works too) and you'll see these variables right near the
top. Edit & save, then restart Mixxx and enjoy.

**The following were present in 1.7 but are now obsolete:**

  - **scratching**: *All of these values are heavily dependent on your
    latency setting. Adjust as needed.*
    1.  **slippage** - Slipperiness of the virtual slipmat when
        scratching with the circle and slider in Vinyl2 mode. Set this
        to a number between 0.2 (perfect turntable) and 0.99 (bent
        record.)
    2.  **sensitivity** - How much the audio moves for a given circle
        arc. Set this to a number between 0.01 (slow) to 0.99 (fast)
    3.  **stoppedMultiplier** - Correction to get the same circle
        sensitivity when the deck is stopped (set higher for higher
        latencies, e.g. 10ms = 1.7, 2ms = 1.5.)

## Mode buttons

[[/media/hardware/stantonscs/modebuttons.jpg|]]

  - FX - Adjust & toggle Flanger effect, toggle reverse effect
  - EQ - Adjust channel EQ parameters
  - Loop - Loop controls and Instant pitch changes
  - Trig - Hot cues
  - Vinyl - Toggle between pitch bend, vinyl manipulation & scratching,
    and track selection
  - Deck - Adjust global controls and switch to the other virtual deck

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
  - B11 resets pre-fader gain to center
  - B12 resets pitch to center 0%

## FX Mode

[[/media/hardware/stantonscs/slidermode.jpg|]]

  - Left slider (S3) adjusts flanger depth
  - Center slider (S4) adjusts flanger delay
  - Right slider (S5) adjusts flanger period (Low Frequency Oscillator)
  - B11 plays track in reverse while held down
  - B12 toggles flanger effect

Hold the FX button down and touch any slider to reset it to center.

## EQ Mode

[[/media/hardware/stantonscs/slidermode.jpg|]]

  - Left slider (S3) adjusts low frequency equalizer
  - Center slider (S4) adjusts mid frequency equalizer
  - Right slider (S5) adjusts high frequency equalizer

Hold the EQ button down and touch any slider to reset it to center.

## Loop mode (red)

### 1.10.1+

The surface is configured as 11 buttons:

| Left          | Middle      | Right        |
| ------------- | ----------- | ------------ |
| 1/8-beat loop | Loop In     | 2-beat loop  |
| 1/4-beat loop | Reloop/Exit | 4-beat loop  |
| 1/2-beat loop | Reloop/Exit | 8-beat loop  |
| 1-beat loop   | Loop Out    | 16-beat loop |

The Reloop/Exit button lights up when a loop is active. If it happens to
be an exact number of beats, the corresponding beat loop button will
light up as well.

Also:

  - **B11** (under the Gain slider) halves the length of the current
    loop
  - **B12** (under the Pitch slider) doubles the length of the current
    loop

You can exit any loop by pressing Reloop/Exit (or a lit beat loop
button.)

### 1.8.0-1.10.0

The surface is configured as three giant buttons:

  - Left: Loop In (mark the start of a loop)
  - Middle: Reloop/Exit (toggle looping)
  - Right: Loop Out (mark the end of a loop)

## Instant-pitch change modes (Loop button)

This offers instant pitch change buttons in the following arrangements:

**Key change (purple)** - Center buttons are one semitone away from
their vertical neighbors and the outside ones are three semitones away
(for harmonic key changes.)

**Notes (black)** - Buttons correspond to major scale notes (ala Vestax
Controller One.) This is most useful with a constant-pitch sound or
chord. (You can generate one in Audacity.)

Remember you can return to the original pitch (tonic) by pressing B12
(under the pitch slider.)

Note that when you use one of these buttons, the pitch range is
automatically set to 100% in order for the values to be set correctly.

*Key change and Note modes were tuned with respect to 440Hz A (above
middle C.)*

**1.7 also offered the following** since looping was not available:

**Fixed increment (red)** - Each button sets the pitch 3.33% above or
below its vertical neighbors.

## Trig Modes

These modes configure the surface as three separate banks of 12 buttons
(lit up dim red for visibility) giving you a total of THIRTY-SIX hot
cues\! (Mixxx 1.8.0-1.9.0 internally supports just 32, so the center 4
buttons and the lower right one in the third bank (black) are
inoperative. Mixxx 1.9.1+ supports 36 again.) The TRIG button will be
red in bank 1, purple in bank 2, and black in bank 3.

The red LEDs flash when you press the corresponding button. The outer
blue LEDs light when a cue point is set on that button. (Changeable with
the **markHotCues** option mentioned at the top of this page.)

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
  - Scratch & cue toogle: Hold the VINYL button and press CUE when in
    Vinyl2 mode to toggle recalling the cue point when you touch either
    C1 or S4. This makes juggling really easy since you don't have to
    back-cue.

**Track Select Mode (black)**

  - Outer circle (C1) allows you to scroll through your Library
  - Center button (anywhere on S4) loads the currently highlighted song
    into the current deck, as long as it's not live (playing to the
    master output.)
  - B11 selects backward between Library, Playlist, and Browse views
  - B12 selects forward between Library, Playlist, and Browse views
  - B13 moves the highlight up one item
  - B14 moves the highlight down one item

## Deck Mode

[[/media/hardware/stantonscs/slidermode.jpg|]] You are in this mode only
**while holding down the Deck button**, unless the controller is in
single-deck mode\*:

  - Gain slider (S1) adjusts master volume
  - Pitch slider (S2) adjusts master balance (pan)
  - B11 resets master volume knob to the middle
  - B12 resets master balance to center
  - Left slider (S3) adjusts the cue/main headphone mix
  - Center slider (S4) adjusts the cross-fader
  - Right slider (S5) adjusts the headphone volume
  - TAP resets cross-fader to center position (only in multi-deck mode)

<!-- end list -->

  - Press Deck + Sync together to toggle between multi- and single-deck
    modes
  - In single-deck mode:
  - Hold the Deck button down and touch any slider to reset it to its
    default value
  - Press Deck + Play together to change the active deck

\* Introduced in v1.8.0

## 

*Images courtesy of Stanton Magnetics, Inc.*
