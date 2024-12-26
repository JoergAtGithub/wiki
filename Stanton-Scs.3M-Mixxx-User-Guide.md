# Stanton SCS.3m & Mixxx User Guide

This guide explains how the SCS.3m is mapped by default in Mixxx.

[[/media/hardware/stantonscs/scs3m_main.png|]]

The left side of the controller controls deck 1. The right side is for
deck 2. We'll walk through the controller from top to bottom and explain
the features.

## Deck select buttons

These are used only as modifier buttons in Mixxx for now. Hold them down
to access different functions for that side of the controller (Deck A/C
for the left side virtual deck 1, Deck B/D for the right side, deck 2,)
detailed for each control below.

## Top horizontal sliders

These adjust the pitch control.

  - Touching near the edges will do a temporary pitch bend in that
    direction.
  - Hold the current mode button down (EQ/FX) and touch the slider on
    that side to reset it to 0%.
  - Hold the applicable Deck select button down when using these sliders
    to perform fine-grained pitch adjustment.

When the Master button is held down:

  - The left slider adjusts the Pre/Main headphone mix
  - The right slider adjusts Master Balance
  - Also hold the current mode button and touch the slider on that side
    to reset it to center

## FX/EQ sliders

From left to right, for each side:

  - in EQ mode these adjust Low, Mid, and High frequency filters
  - in FX mode these adjust Depth, Delay, and LFO for the flanging
    effect

Hold down the current mode button (FX/EQ) and touch one of these sliders
to reset it to center.

## FX/EQ mode buttons

Press these to choose what the sliders above them control. (See above.)

  - Hold Deck and press FX to toggle the flange effect for that deck
  - Hold Deck and press EQ to auto-adjust the pitch to sync the BPM on
    this deck with the other one (assuming it was detected correctly on
    both)

## Volume sliders

These adjust the channel volume as on a traditional mixer.

  - Holding Deck causes these to adjust the pre-fader gain for the deck

When the Master button is held down:

  - The left slider adjusts the Headphone volume
  - The right slider adjusts Master volume

## Soft buttons

From top to bottom on both sides:

  - Rewind
  - Fast forward
  - Cue
  - Play

Headphone buttons toggle that deck in the headphone mix.

## Cross-fader

Adjusts the cross-fade between the virtual decks

  - Needle drop function: Hold a Deck button to use the cross-fader
    strip to search through the track loaded on that deck

## Level Meters

These normally show the pre-fader signal for the respective deck. When
holding down the Master button, they show the stereo master output
meters: left side for the left channel, right side for the right
channel.

**NOTE:** The LEDs are calibrated to the VU meters on-screen. If you see
a red LED flicker, <span class="underline">you are clipping</span> and
need to reduce the volume or gain to avoid distorted sound and/or
speaker damage.

# Proposed changes for 1.12

This section explains the extensions proposed for Mixxx 1.12.

### Deck switching buttons

When touching the "A C" or "B D" buttons, the mixer switches between
decks. On the left side, touching "A C" will switch between decks 1 and
3. On the right side, touching "B D" will switch between decks 2 and 4.
All controls except for the crossfader then control the selected deck.

Connected SCS.3d modules will follow deck changes. For example if you
switch from deck 1 to deck 3 on a SCS.3m, all connected SCS.3d modules
who are on deck 1 will also switch to deck 3.

### EQ mode

This is the standard mixing mode where the three EQ sliders control
low/mid/high. The top slider controls the filter knob.

Touching EQ will return to EQ mode from the FX modes. Holding EQ and
touching a slider will reset it to its preset position. (Unfortunately
this doesn't work for MASTER modes.)

### FX modes

In FX mode you can control an effect unit. The three vertical sliders
control the first three effect parameters and the top slider controls
dry/wet mix. The four buttons below EQ refer to the four effect units,
we'll call them FX1, FX2, FX3, and FX4. Top button (FX1) selects first
effect chain and so forth.

To enter FX mode you can either press FX to switch to the preselected
effect unit, or press FX1 through FX4 to switch directly to the desired
effect unit. You can assign FX chains to the deck by holding FX and
pressing FX1 through FX4 to assign these effects to the deck. So to
assign FX unit 1 to the current deck, hold FX and press the top button
(right below EQ).

You can change the effect loaded into an effect unit by holding its
button (FX1 through FX4) and tapping left/right on the top slider to
cycle through the effects.

### MASTER mode

When holding the central MASTER button, the left side controls the
headphone channel, while the right side controls the master channel.

  - Left top slider: Pre/main mix on headphone
  - Right top slider: main balance
  - Left slider: head gain
  - Right slider: master gain
  - Buttons: The buttons assign effects to head and master

### 

*Images courtesy of Stanton Magnetics, Inc.*
