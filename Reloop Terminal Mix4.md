# Reloop TerminalMix4 & Mixxx User Guide

This guide explains how the TerminalMix4 is mapped by default in Mixxx.

***Easy customization:*** We have provided the following customization
variables at the top of the script you can set to your liking:

1.  **pitchRanges**: Set the pitch slider range each time you toggle it.

Just open the `controllers/Reloop TerminalMix4.js` file in your favorite
text editor and you'll see these variables right near the top. Edit &
save and Mixxx will automatically reload the preset.

## Deck controls

*The controls are the same on both sides of the controller. The left
side controls Deck 1 or 3 and the right side controls Deck 2 or 4.*

  - **Range** button - Toggles the pitch slider range. (See top of page
    to customize.)
  - **Keylock** button - Toggles key lock.
  - **FX** knobs - These adjust the depth, delay and LFO period of the
    Flanger effect.
  - **FX** buttons - Toggle the flanger effect on Deck 1 or 2 (these
    don't switch to decks 3 and 4.)
  - **Beats knob** - Pressing this moves the beat grid to the current
    play position. (Turning it does nothing.)
  - **Tap** button - Tapping this in time with the music adjusts the BPM
    of the track to match. It also flashes on each beat.
  - **Loop length** knob - Turning this doubles or halves the current
    loop. Pressing it toggles the loop.
  - **Loop in/halve** button - Sets the loop in point. When shifted,
    halves the length of the current loop. Flashes when a loop is
    active.
  - **Loop out/double** button - Sets the loop out point. When shifted,
    doubles the length of the current loop. Flashes when a loop is
    active.
  - **Loop move knob** - Turning this moves the position of the current
    loop by a half beat per detent. Pressing it sets a 4-beat loop at
    the current position. Pressing it with shift held down toggles
    quantize (locking loop in/out and cue points to the nearest beat.)
  - **Hot cue buttons** - Press to set or recall a hot cue. The buttons
    light up when one is set. Hold shift and press to delete the cue.
  - **Scissor** button - Switches hot cue page for access to hot cues
    5-8
  - **Sampler** buttons - These light up when a sample is loaded to the
    corresponding sampler and flash when that sampler is playing. Press
    to play the sample from the beginning. When shifted, press to stop
    the sample.
  - **Vinyl/Search** button - Press and release to toggle scratching
    with the wheel (and the on-screen vinyl widget.) Hold down and turn
    the wheel to seek through the track.
  - **Wheel**
  - Move the wheel while touching the top black area to scratch the
    current track like a vinyl record if vinyl mode is enabled
  - Move the wheel without touching the top (so on the gray sides) to
    perform a temporary pitch bend.
  - **\>\< (Sync)** button - Synchronizes the tempo and beat phase of
    this deck to that of the other. (Only works between decks 1 & 2 in
    v1.11.x.)
  - **CUP** button - This stands for Cue-Play which starts playback from
    the cue point. This is also known as stutter play.
  - **Q (Cue)** button - Sets or recalls the main cue point on the track
  - **\> || (Play/Pause)** button - Toggles playback of the track.

## Mixer controls

### Channel strips

*The below controls adjust the specified parameter of the respective
virtual deck.*

  - **Gain** knob - Adjusts the pre-fader gain
  - **High/Mid/Low EQ** knobs - Adjust the volume of the respective
    frequency range
  - **Filter** knob - Performs a pseudo-filter effect by adjusting
    multiple EQ knobs at once (until Mixxx gets a proper filter effect.)
  - **Headphone** button - Toggles hearing the deck in the headphone
    output
  - **Number** button - Press to load the currently highlighted song
    into that deck. Shift and press to toggle fader-start (on the
    channel fader and cross-fader when applicable.) The button flashes
    when fader-start is enabled on that deck.
  - **Channel slider** - Adjusts the output volume

*The below controls are not deck-specific.*

  - ***Master** knob - Adjusts the master output volume of the internal
    sound card. (This is not mapped in Mixxx.)*
  - ***Booth** knob - Adjusts the booth output volume of the internal
    sound card. (This is not mapped in Mixxx.)*
  - ***Phones** knob - Adjusts the headphone output volume of the
    internal sound card. (This is not mapped in Mixxx.)*
  - ***Cue mix** knob - Adjusts in hardware how much of the headphone
    bus vs the master output you hear in the headphones. (This is not
    mapped in Mixxx.)*
  - **Sampler volume** knob - Adjusts the volume of all of the samplers
    at once.
  - ***Crates** button - Does nothing at the moment. (Mixxx's library
    doesn't yet support direct panel selection.)*
  - ***View** button - Does nothing at the moment.*
  - ***Prep** button - Does nothing at the moment.*
  - **Back** button - When lit, the Trax knob moves the highlight in the
    active library panel. When unlit, the knob moves the highlight in
    the left tree.
  - **TRAX knob** - Turn to move the highlight. Press to switch to the
    highlighted library panel (when the Back button is unlit,) or to
    load the currently selected track into the first stopped deck (when
    the Back button is lit.)

### Cross-fader section

Move the cross-fader to smoothly fade between the decks assigned to
either side.

#### Deck assign

Use the four switches on the front of the unit to choose on which side
of the cross fader that deck will be heard. (Note that the fader-start
functionality correctly follows this assignment.) If "thru" is selected,
the cross-fader will not affect the audio from that deck.

#### Curve adjust

Use the knob to adjust the curve from a smooth fade to a fast cut.

*The remaining controls on the front of the unit adjust hardware
parameters and are not MIDI-mappable.*
