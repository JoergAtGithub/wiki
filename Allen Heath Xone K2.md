\======= Allen & Heath Xone:K2/K1 ======
![http://www.allen-heath.com/media/XoneK2\_Front\_Main-463x1024.jpg](http://www.allen-heath.com/media/XoneK2_Front_Main-463x1024.jpg)

  - [Manufacturer's product
    page](http://www.allen-heath.com/ahproducts/xonek2/)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=3776)
  - [Manufacturer's User
    Guide](http://www.allen-heath.com/media/Xone+K2_UG_AP8509_2.pdf)
  - [Blank template
    diagrams](http://www.allen-heath.com/media/Xone+K2+Blank+Overlays.zip)

The Allen & Heath Xone:K2 is set up like a 4 channel mixer plus a grid
of buttons. It also has an integrated 4 channel audio interface with 2
RCA jacks and an 1/8" stereo headphone jack. The Xone K1 is the same as
the Xone K2 but without the built in audio interface.

# Audio setup

Configure channels 1-2 for Mixxx's Headphones output and channels 3-4
for the Master output (this is the opposite of most DJ controllers with
an integrated audio interface).

There are no hardware controls for the volume; they are always at full
volume. You can adjust the volume of the master and headphone outputs by
adjusting the gain controls for those outputs in Mixxx with the
controller mapping.

# Mixxx 2.1 mapping

## Setup

This mapping can used with one or multiple Xone K2s/K1s. Multiple Xone
K2s/K1s can be connected to each other via X-Link with one of them
connected to the computer via USB. Alternatively, when using 2 K2s/K1s,
they can both be connected with their own USB cable and this same
mapping can be loaded for each.

The layout of the mapping depends on the configured MIDI channel of the
controller. Change the MIDI channel of the controller by pressing the
bottom right encoder (labeled "Power On Setup/Scroll/Set") while
plugging in the controller. Scroll with the encoder to select a MIDI
channel. The letter in parentheses corresponds to the last lit button
when selecting the channel:

  - Channel 15 (O, default out of the box): two decks + two effect units
    with decks in the middle
  - Channel 14 (N): two decks + two effect units with effect units in
    the middle
  - Channel 13 (M): two decks + two effect units with decks on left
  - Channel 12 (L): two decks + two effect units with decks on right
  - Channel 11 (K): four decks ordered 3 1 2 4
  - Channel 10 (J): four decks ordered 1 2 3 4
  - Channel 9 (I): four effect units ordered 3 1 2 4
  - Channel 8 (H): four effect units ordered 1 2 3 4

If you are using K2s, they must have Latching Layers turned off, which
is the default (the K1 does not have Latching Layers). Refer to the
[Xone K2/K1 product manual from Allen &
Heath](http://www.allen-heath.com/media/Xone+K2_UG_AP8509_2.pdf) for
details.

## Global controls

These are available on any configuration with decks, but not the 4
effect unit layout.

  - Bottom left encoder:
  - adjust tempo of all decks with sync enabled
  - press and turn: PFL/master mix in headphones
  - shift: headphone gain
  - press with shift: toggle split cue mode
  - Bottom right encoder
  - scroll through tracks in library
  - press and release: load selected track into first stopped deck
  - press and hold: load selected track into a deck by pressing the top
    button of the deck (headphones/PFL)
  - shift: master gain

## Decks

The bottom right button is the shift button. The bottom left button
toggles the bottom button grid between a loop layer (amber) and a hotcue
layer (red). Holding shift then holding the bottom left layer button at
the same time activates supershift mode.

  - Top encoder:
  - jog
  - shift: key
  - supershift: gain
  - Top encoder press:
  - sync
  - shift: reset key
  - supershift: reset tempo
  - Knobs: high/mid/low equalizer knobs
  - Top button 1:
  - headphones/PFL
  - supershift: set beatgrid to current position
  - Top button 2:
  - cue
  - shift: go to beginning of track and stop
  - supershift: keylock
  - Top button 3:
  - play
  - shift: reverse
  - supershift: quantize
  - Fader: volume
  - Bottom buttons (loop layer):
  - Bottom button 1 (red):

<!-- end list -->

``` 
    * reloop/disable loop
    * shift: jump to to beginning of loop, stop playback, and activate loop
* Bottom button 2 (green):
    * activate loop of selected size
    * shift: activate rolling loop of selected size
* Bottom button 3 (amber):
    * double loop size
    * shift: beatjump forward by selected size if no loop is enabled. If loop is enabled, move the loop forward by the beatjump size.
    * supershift: double beatjump size
* Bottom button 4 (amber):
    * halve loop size
    * shift: beatjump backward by selected size if no loop is enabled. If loop is enabled, move the loop backward by the beatjump size.
    * supershift: halve beatjump size
* Bottom buttons (hotcue layer, red):
* activate hotcues 1-4 or set the hotcue if the is not one set yet
* shift: delete hotcues 1-4
```

## Effects

The top part of the column uses the [Standard Effects
Mapping](Standard%20Effects%20Mapping). Pressing the top encoder acts as
the effect focus button. When no effect is focused, the buttons are red.
When holding the top encoder to choose an effect to focus, the buttons
are green. When an effect is focused, the buttons are amber.

The fader acts as the dry/wet knob. The bottom buttons assign the effect
unit to the corresponding deck.

The bottom left layer button currently does nothing to effects columns.
Also, the bottom encoders are not mapped in the 4 effect unit layout.

# Mixxx 2.0 mapping

For the mapping to work correctly, the device must be set to operate on
MIDI channel 16 and Latching Layers must be set to "Switch Matrix" (2nd
state). For information on how to do that read the [manual from Allen &
Heath](http://www.allen-heath.com/media/Xone+K2_UG_AP8509_2.pdf).
Latching Layers is not available on the Xone K1, so this mapping is not
compatible with the Xone K1.

The behavior of the grid buttons depends on which layer is active, which
is changed by pressing the Layer button in the bottom left. The color of
the text background indicates what the button does in that layer, e.g.
the buttons of the last row activate hotcue 4 when the green layout is
selected, but act as the play button when the red layer is selected.

Text in blue describes secondary functions accessible when the shift
button is held down.

[[/media/xone_k2_mapping.svg|Xone K2 Mapping]]
