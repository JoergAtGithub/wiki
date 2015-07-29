![http://electrixpro.com/wp-content/uploads/2014/09/Tweaker-Angle-570x380.jpg](http://electrixpro.com/wp-content/uploads/2014/09/Tweaker-Angle-570x380.jpg)

[Forum topic](http://mixxx.org/forums/viewtopic.php?f=7&t=7189)

[Manufacturer's website](http://electrixpro.com/): this is the best
place to buy one. It comes with a free case and free shipping for $100.

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

## Deck controls

[[/media/hardware/Tweaker-deck-controls.png|Tweaker-deck-controls.png]]

    -Filter (low pass filter left of center; high pass filter right of center)
    -Load track selected in library into deck
    -Toggle encoders between EQ and loop mode (see below)
    -Headphone cueing
    -Volume
    -Play/pause
    -Hotcues
    -Jump 4 beats forward
    -Slip mode
    -Deck shift
    -Deck toggle between decks 1 & 3 on the left and decks 2 & 4 on the right. When controlling deck 1 or 2, the switches on that side are blue, as shown on the left side of the diagram. When controlling deck 3 or 4, the switches on that side are magenta, as shown on the right side of the diagram.
    -Jump 4 beats backward
    -Quantize
    -Key lock
    -Sync lock

## Channel encoder modes

[[/media/hardware/Tweaker-encoder-modes.png|Tweaker-encoder-modes.png]]

``` 
 -High EQ
 -Mid EQ
 -Low EQ
 -Encoder mode button. Press to switch to loop mode.
 -Loop move length
 -Move loop
 -Loop length. Press to toggle loop. When in slip mode, the loop is only active while this is held down.
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

### Deck shift layer

[[/media/hardware/Tweaker-deck-shift.png|Tweaker-deck-shift.png]]

This layer is active while the yellow deck shift button is held down.

    -Inactive
    -Jump 32 beats forward or backward
    -Scroll through hotcue pages
    -Exit loop
    -Pitch
    -Cue
    -Move hotcue to current position
    -Jump forward 1 beat
    -Loop in
    -Deck shift button
    -Loop out
    -Jump back 1 beat
    -Align beatgrid with current position
    -Sync key. If key has been changed from track's original key, reset the key.
    -Reset tempo
    -Temporarily raise pitch while pressed
    -Temporarily lower pitch while pressed
