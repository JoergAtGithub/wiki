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
the Xone K2 but without the built in audio interface and does not come
with the EVA travel case that the K2 comes with.

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
  - press and hold: load selected track into a deck by pressing the play
    button of the deck
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
    * supershift: set loop in point. Hold to move loop in point within an active loop.
* Bottom button 2 (green):
    * activate loop of selected size
    * shift: activate rolling loop of selected size
    * supershift: set loop out point. Hold to move loop out point within an active loop.
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

The fader acts as the dry/wet knob.

The bottom buttons assign the effect unit to different input channels
and light up red. On the two deck layouts, from top to bottom, they
assign the effect unit to deck 1, deck 2, master mix, and headphones. On
the four effect unit layouts, they assign the effect unit to decks 1-4
going down the column. You can look down a column to see which decks an
effect unit is assigned. You can look across a row to see which effect
units are assigned to a deck. When shift is pressed, the bottom two
buttons switch to controlling the routing buttons for the master and
headphones channels and light up amber.

The bottom encoders are not mapped in the 4 effect unit layout.

### Effect unit focusing

In addition to focusing one effect in a unit at a time with the
[Standard Effects Mapping](Standard%20Effects%20Mapping), the Xone K2/K1
has another mode for focusing a whole effect unit. This allows for
controlling the parameters of all 3 effects in the unit at a time. This
mode is only available on the 4 effect unit layouts. To access it, press
the Layer button in the bottom left. Press one of the top encoders to
choose which effect unit to focus.

In this mode, each horizontal row of knobs and buttons controls one
effect. The knobs control the parameters of the effects. Turning any of
the knobs with shift loads different effects. The button in the leftmost
column controls the enable button of the effect and turns amber when it
is on. The rest of the buttons control the button parameters of the
effect and turn green when active (not all effects have button
parameters). The faders still control the dry/wet knobs and the bottom
button grid still controls the routing buttons.

To get back to controlling all 4 effect units, press the Layer button
again. The next time Layer is pressed, the effect unit that was focused
before will be remembered (but it will not be remembered after
restarting Mixxx).

## Troubleshooting

If your K2 switches between 3 layers (amber, red, and green) instead of
2 (amber and red only) and supershift does not work, make sure Latching
Layers is turned off. Refer to the [Xone K2 product manual from Allen &
Heath](http://www.allen-heath.com/media/Xone+K2_UG_AP8509_2.pdf) for
details.

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
