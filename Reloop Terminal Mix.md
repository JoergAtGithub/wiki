# Reloop Terminal Mix Series

  
  
  
[[/media/hardware/reloop/terminalmix2_top.jpg|Terminal Mix 2]] ![Terminal Mix
4](/hardware/reloop/terminalmix4_top.jpg)

*Images courtesy of [Reloop](http://www.reloop.com/). Click on either
for a larger version.*

  - [Terminal Mix 2 product
    page](http://www.reloop.com/reloop-terminal-mix-2)
  - [Terminal Mix 4 product
    page](http://www.reloop.com/reloop-terminal-mix-4)

The Reloop Terminal Mix 2 and Terminal Mix 4 use the same mapping in
Mixxx.

## Sound hardware

The Reloop Terminal Mix 2 and Terminal Mix 4 have integrated
multichannel sound cards.

<span class="underline">Inputs</span> Both have a microphone and a
switchable line/phono input that can be routed into Mixxx. The
Microphone jack is the front side of the controller, the RCA line jacks
are at the back next to the line/phono switch.  
For both inputs there is a gain knob and a switch on the controller's
front side that toggles between routing the signal to the computer
(`SW`) or mixing it directly with the master output (`MST`). `MST`
allows to play music from external sources without any software, for
example while setting up Mixxx software.  
Switch to `SW` if you want to use the line signal for vinyl control or
AUX input, or if you want to record the microphone input with Mixxx,
broadcast it, or put on effects.

<span class="underline">Outputs</span> At the front, there are two
headphone jacks (1/8" and 1/4"), both affected by the hard-wired `TONE`
knob.  
At the back, there are unbalanced outputs for booth and master (RCA), as
well as a balanced master output (1/4"). The output level of both master
ouputs, booth and headphone outputs are all controlled by respective
hard-wired knobs in the center column which can't be mapped to software.

## Mapping options

We have provided the following customization variables at the top of the
script you can set to your liking:

1.  **pitchRanges**: Set the pitch slider range each time you toggle it.

Just open the `controllers/Reloop Terminal Mix 2-4.js` file in your
favorite text editor and you'll see these variables right near the top.
Edit & save and Mixxx will automatically reload the preset.

## Deck controls

*The controls are the same on both sides of the controller. The left
side controls Deck 1 or 3 and the right side controls Deck 2 or 4.*

  - **Range** button - Toggles the pitch slider range. (See [Mapping
    Options](https://mixxx.org/wiki/doku.php/reloop_terminal_mix#mapping_options))
  - **Keylock** button - Toggles key lock. \[ToDo: map long-press to
    reset track key\]

### FX Controls

This mapping uses the [Standard Effects
Mapping](Standard%20Effects%20Mapping) via components-js to control the
FX units.  
Note: these knobs & buttons don't switch to decks 3 and 4.

  - **FX1/2/3** knobs
  - control the Meta knob of each effect
  - focused effect: control the first three knob parameters of the
    focused effect
  - **ON** buttons
  - Press: toggle the effects
  - Press & hold: temporarily toggle an effect
  - focused effect: control the first three button parameters of the
    focused effect
  - **Beats** encoder
  - Turn: adjust the Wet/Dry knob of the effect unit
  - Press repeatedly: adjust the BPM (not the pitch/speed\!) of the
    loaded track
  - Shift & Press: move the nearest beat marker to the current play
    position
  - **Tap** button
  - LED flashes on each beat
  - Press & hold, then press any ON button to focus the respective
    effect
  - Shift & Press: switch between FX units 1/3 (left FX section) and 2/4
    (right FX section)

### Loop Controls

  - **Loop length** knob
  - Turning this doubles or halves the current loop size visible in loop
    size spinbox in each skin.
  - Pressing it sets a loop of that size. Pressing it with Shift
    re-activates the previous loop and plays from loop in point.
  - **Loop in/halve** button
  - Sets the loop in point and flashes when a loop is active.
  - While a loop is active, press and hold it to drag the loop in point.
  - **Loop out/double** button
  - Sets the loop out point and flashes when a loop is active.
  - While a loop is active, press and hold it to drag the loop out
    point.
  - **Loop move knob**
  - Press and turn this to adjust the beatjump size visible in beatjump
    spinbox in each skin.
  - Turning without an active loop jumps back or forth by the size set
    in beatjump spinbox.
  - Turning with Shift pressed while a loop is active shifts the loop
    back or forth by the size set in beatjump spinbox.
  - Turning it while a loop is active and quantize is On, moves the
    position of the current loop by one beat per detent. This helps to
    correct the loop in point in case it snapped to the wrong beat
    marker.
  - Turning it while a loop is active and quantize is Off, moves the
    position of the current loop by 1/8 beat per detent. This helps to
    correct the loop in point in case it's set slightly too early or too
    late.

### Hot cues / Sampler buttons

  - **Hot cue buttons**
  - Press to set or recall a hot cue. The buttons light up when one is
    set.
  - Hold shift and press to delete the cue.
  - **Sampler** buttons - These light up when a sample is loaded to the
    corresponding sampler and flash when that sampler is playing. Press
    to play the sample from the beginning. When shifted, press to stop
    the sample.
  - **Scissor** button - Switches hot cue & sampler button grid for
    access to hot cues/samplers 5-8

### Wheel & Vinyl button

  - **Wheel**
  - Move the wheel while touching the top black area to scratch the
    current track like a vinyl record if vinyl mode is enabled
  - Move the wheel without touching the top (so on the gray sides) to
    perform a temporary pitch bend. With scratch mode disabled, all
    regions of the wheel can be touched and turned to perform a
    temporary pitch bend.
  - **Vinyl/Search** button
  - Press and release to toggle scratching with the wheel.
  - Hold down and turn the wheel to seek through the track.

### Transport buttons

  - **\>\< (Sync)** button - Synchronizes the tempo and beat phase of
    this deck to that of the other. \[ToDo: long-press to toggle master
    sync incl. LED feedback\]
  - **CUP** button - This stands for Cue-Play which starts playback from
    the cue point. This is also known as stutter play.
  - **Q (Cue)** button - Sets or recalls the main cue point on the
    track. Is lit or flashes when play position is at cue point. [set
    cue
    mode](https://mixxx.org/manual/2.1/chapters/user_interface.html#using-cue-modes)
  - **\> || (Play/Pause)** button - Toggles playback of the track.
  - **\>\< (Sync)** button (left deck) / **\> || (Play/Pause)** button
    (right deck)
  - Holding Shift and pressing one of those buttons initiates the [brake
    effect](https://www.mixxx.org/wiki/doku.php/midi_scripting#spinback_brake_and_soft_start_effect)
    for the respective deck: track slows down to full stop. This can be
    interrupted by touching the wheel when scratch mode is enabled:
    track speed jumps back to normal (considering th pitch slider) and
    playback continues as soon as the wheel is released. Open the
    `controllers/Reloop Terminal Mix 2-4.js` file and look for
    `TerminalMix.brake` to adjust parameters.

<!-- end list -->

``` 
  [ToDo: add sofStart function as well]
* **3** / **4** button - When lit all deck buttons (except FX controls) control deck 3 (deck 4 respectively).
```

## Mixer controls

### Channel strips

*The below controls adjust the specified parameter of the respective
virtual deck.*

  - **Gain** knob - Adjusts the pre-fader gain
  - **High/Mid/Low EQ** knobs - Adjust the volume of the respective
    frequency range
  - **Filter** knob - Adjust the QuickEffect Meta knob (default: filter)
  - **Headphone** button - Toggles hearing the deck in the headphone
    output
  - **Arrow** / **Number** button
  - Press to load the currently highlighted song into that deck.
  - Shift and press to toggle fader-start (on the channel fader and
    cross-fader when applicable.) The button flashes when fader-start is
    enabled on that deck.
  - **Channel slider** - Adjusts the output volume

*The below controls are not deck-specific.*

  - ***Master** knob - Adjusts the master output volume of the internal
    sound card. (Hard-wired knob. This is not mapped in Mixxx.)*
  - ***Booth** knob - Adjusts the booth output volume of the internal
    sound card. (Hard-wired knob. This is not mapped in Mixxx.)*
  - ***Phones** knob - Adjusts the headphone output volume of the
    internal sound card. (Hard-wired knob. This is not mapped in
    Mixxx.)*
  - **Cue mix** knob - Adjusts in hardware how much of the headphone bus
    vs the master output you hear in the headphones.
  - **Sampler volume** knob - Adjusts the volume of all of the samplers
    at once.
  - ***Crates** button - Does nothing at the moment. (Mixxx's library
    doesn't yet support direct panel selection.) Use the MIDI Learning
    Wizard to assign an action.*
  - ***View** button - Does nothing at the moment. Use the MIDI Learning
    Wizard to assign an action.*
  - ***Prep** button - Does nothing at the moment. Use the MIDI Learning
    Wizard to assign an action.*
  - **Back** button - Pressing moves the highlight in the active library
    panel to the right. With Shift it moves the highlight to the left.
  - **TRAX knob**
  - Turn to move the highlight up/down by one line.
  - Shift and turn to move the highlight one page up/down
  - Press while Tree panel has focus expands an item if possible. If
    item can't be expanded further, it is selected and and highight is
    shifted rightwarde to the respective tracks table.
  - Press while tracks table has focus performs the Track Load Action
    specified in *Preferences \> Library* (default: load track to next
    empty deck)

### Cross-fader section

Move the cross-fader to smoothly fade between the decks assigned to
either side.

#### Deck assign

*(Terminal Mix 4 only)* Use the four switches on the front of the unit
to choose on which side of the cross fader that deck will be heard.
(Note that the fader-start functionality correctly follows this
assignment.) If "thru" is selected, the cross-fader will not affect the
audio from that deck and it will always be heared.

#### Curve adjust

Use the knob to adjust the curve from a smooth fade to a fast cut.

*The remaining controls on the front of the unit adjust hardware
parameters and are not MIDI-mappable.*

## Effects controls

This mapping uses the [Standard Effects
Mapping](Standard%20Effects%20Mapping).

  - **FX1/2/3** knobs
  - Those control the Meta knob of each effect.
  - In focus mode they control the first three knob parameters of the
    focused effect.
  - **ON** buttons
  - Those toggle the effects. Press and hold to temporarily toggle an
    effect.
  - In focus mode they control the first three button parameters of the
    focused effect.
  - **Beats** encoder
  - Turning adjust the Wet/Dry knob of the effect unit
  - Pressing this repeatedly adjusts the BPM (not the pitch/speed\!) of
    the loaded track.
  - **Tap** button
  - Holding this and pressing any ON button focuses the respective
    effect
  - Pressing this with Shift switches between FX units 1/3 and 2/4
    respectively
