\======= Electrix Tweaker======
![http://electrixpro.com/wp-content/uploads/2014/09/Tweaker-Angle-570x380.jpg](http://electrixpro.com/wp-content/uploads/2014/09/Tweaker-Angle-570x380.jpg)

[Forum topic](http://mixxx.org/forums/viewtopic.php?f=7&t=7189)

The Electrix Tweaker is a flexible, well-built MIDI controller. It
wastes no space with jog wheels; instead, there are a plethora of
multicolor backlit buttons and eight velocity-sensitive buttons. Instead
of analog knobs for EQs, there are infinitely rotating encoders
surrounded by LED rings that are programmed to seemlessly switch modes.
It has no audio interface but includes 5-pin MIDI in and out ports. It
apparently did not sell well considering how little information there is
about it online. It initially sold for $400 in 2013 but is now available
for $100 with a free case from [the
manufacturer](http://electrixpro.com/).

The flexibility of the encoders with LED rings and the multicolor
buttons allows this mapping to fit *a lot* of functionality into a small
package. The encoders control EQs, gains, loops, and coarse seeking in
various modes. This mapping can control 4 decks by toggling between
decks 1/3 on the left and decks 2/4 on the right. Each deck shows 8
hotcues at a time and 4 pages of hotcues are available, providing access
to all 32 hotcues allowed by the Mixxx engine. This mapping also takes
advantage of slip mode, which is not yet available through any of
Mixxx's skins. With slip mode and all those hotcues, this mapping is
excellent for cue juggling.

The mapping requires at least Mixxx 1.12 beta. Use it with the Tweaker
MIDI 1 port (Tweaker MIDI 2 is the 5-pin MIDI I/O on the Tweaker).

# Mapping description

## Global controls

[[/media/hardware/Tweaker-global-controls.png|Tweaker-global-controls.png]]

    -Scroll through library. Push to load selected track into first stopped deck.
    -Scroll up left panel of library
    -Scroll down left panel of library
    -Samplers
    * Off when empty, red when loaded
    * Press a button to load the selected sample into a sampler and play it
    * Press a button to play a sample. When the button is released, the sample will stop playing.
    * Press top shift and a sampler button to eject a sample from a sampler
    * Samples will play with their volume proportional to how much force was used to strike the button. You can adjust the sensitivity or disable the velocity sensitivity (and make them work as on/off switches) by adjusting options at the top of the JavaScript file in a text editor.
    -Crossfader

### Top shift layer

[[/media/hardware/Tweaker-top-shift.png|Tweaker-top-shift.png]]

With the exception of the headphone mix encoder (\#7 in the diagram),
pressing the encoders resets the parameters they control to the default
value.

    -Top shift button
    -Scroll through library quickly. Press to toggle big library view
    -Eject left deck
    -Eject right deck
    -Expand/collapse selected item in left library pane
    -Expand/collapse selected item in left library pane
    -Headphone gain
    -Headphone cue/master mix in headphones. Press to toggle split cue mode. The blue LED below encoder is lit when split cue mode is enabled.
    -Channel gain for active deck on left side
    -Master output gain
    -Master output balance
    -Channel gain for active deck on right side
    -Eject sampler
    -Delete hotcue
    -Deck shift button. Press to enable [[#vinyl mode]] on left deck (press top shift button first, then this button while holding down top shift)
    -Deck shift button. Press to enable [[#vinyl mode]] on right deck (press top shift button first, then this button while holding down top shift)

## Deck controls

[[/media/hardware/Tweaker-deck-controls.png|Tweaker-deck-controls.png]]

The deck controls are the same on each half of the controller. Which
deck each side controls can be switched with the deck toggle button.
When controlling deck 1 or 2, the switches on that side are blue, as
shown on the left side of the diagram. When controlling deck 3 or 4, the
switches on that side are magenta, as shown on the right side of the
diagram.

    -Filter (low pass filter left of center; high pass filter right of center)
    -Load track selected in library into deck
    -Toggle encoders between EQ and loop mode (see [[#channel-encoder-layers|below]])
    -Headphone cueing
    -Volume
    -Play/pause
    -Hotcues. Press an unlit button to set a hotcue. When slip mode is disabled (see #9 below), pressing a hotcue simply jumps to that hotcue. When slip mode is on, hotcues can be previewed on a stopped deck. While previewing a hotcue, press the play button to let the track keep playing after the hotcue is released.
    -Jump 4 beats forward (with quantize enabled)
    -Slip mode. When active, loops and hotcues will only play as long as they are held down. When they are released, the track will jump to where it would have been if the loop or hotcue was not pressed. 
    -Deck shift
    -Deck toggle between decks 1 & 3 on the left and decks 2 & 4 on the right.
    -Jump 4 beats backward (with quantize disabled)
    -Quantize. When enabled, the navigation buttons are white as shown by 8 & 11 in the diagram. With quantize enabled, the navigation buttons jump by 4 beats or 1 beat with deck shift pressed. When disabled, the navigation buttons are green as shown by 15 & 16 in the diagram. With quantize disabled, the navigation buttons fast forward and rewind the track. When quantize is disabled and deck shift is pressed, the navigation buttons are temporary pitch bend buttons.
    -Key lock
    -Sync lock
    -Fast forward (with quantize disabled)
    -Rewind (with quantize disabled)

### Deck shift layer

[[/media/hardware/Tweaker-deck-shift.png|Tweaker-deck-shift.png]]

This layer is active while the yellow deck shift button is held down.

    -Inactive
    -Jump 32 beats forward or backward
    -Scroll through hotcue pages. The pages are color coded, in order, cyan, green, red, and white. The LED around the encoder indicates the hotcue page number.
    -Exit loop
    -Pitch
    -Cue
    -Move hotcue to current position
    -Jump forward 1 beat (with quantize enabled)
    -Manually place loop start point
    -Deck shift button
    -Manually place loop end point
    -Jump back 1 beat (with quantize enabled)
    -Align beatgrid with current position
    -Sync key. If key has been changed from track's original key, reset the key.
    -Reset tempo
    -Temporarily raise pitch while pressed (with quantize disabled)
    -Temporarily lower pitch while pressed (with quantize disabled)

### Channel encoder layers

[[/media/hardware/Tweaker-encoder-modes.png|Tweaker-encoder-modes.png]]

``` 
 -High EQ
 -Mid EQ
 -Low EQ
 -Encoder mode button. Press to switch to loop mode.
 -Loop move length
 -Move loop
 -Loop length. Press to toggle loop. When in slip mode, the loop is only active while this is held down. The blue LED below the encoder is lit while a loop is active.
 -Encoder mode button. Press to switch to EQ mode.
```

The left side is on EQ mode. In EQ mode, pressing encoders toggles EQ
that EQ's kill switch. The blue LED below the encoder is lit while the
kill switch is on. Pressing the encoder while holding deck shift (see
below) resets the EQ to 0.

The right side is on loop mode. The LEDs on the loop move length and
loop length encoders represent numbers of beats. Center means 1 beat.
Each step to the right doubles the beats and each step to the left
halves the beats. For example, the default loop length is 4 beats, so
the center LED and 2 LEDs to the right are lit.

### Vinyl mode

[[/media/hardware/Tweaker-vinyl-mode.png|Tweaker-vinyl-mode.png]]

Toggle vinyl mode by pressing deck shift (\#2 in the diagram) while
holding top shift (\#1 in the the diagram).

3: cycle through vinyl control modes: absolute (LED off), relative (LED
indicates cue mode), and constant (LED red). If the deck is in relative
mode and playing, pressing the button cycles through cue modes: off
(white), cue (yellow), hotcue (green). When the deck is playing in
relative mode, pressing the button with deck shift switches to constant
mode.

4: toggle vinyl control. Turns green when vinyl control is enabled. With
deck shift pressed, it toggles passthrough mode and turns white.
Pressing the button while passthrough mode is enabled turns passthrough
mode off (without toggling whether vinyl control is enabled).
