# American Audio VMS4 & Mixxx User Guide

This guide explains how the VMS4 is mapped by default in Mixxx.

[[/media/hardware/american_audio/vms4_top.jpg|]]

*Image courtesy of [American Audio](http://www.adjaudio.com/)*

***Easy customization:*** We have provided the following customization
variables at the top of the script you can set to your liking:

1.  **RateRanges**: Set the pitch slider range each time you toggle it
    with Shift+Sync.

Just open the `midi/American-Audio-VMS4-scripts.js` file in your
favorite text editor (Wordpad works too) and you'll see these variables
right near the top. Edit & save, then restart Mixxx and enjoy.

**Important: Mixxx expects the VMS4 to be set to "Post EQ" mode for best
sound quality.** Do this by holding down the Cue button on Midilog 4
while powering up the unit. You only need to do this once. (Each time
you do it, it changes the mode back and forth.) Consult the [user
manual](http://vms4dj.com/Files/vms4.pdf) for more information.

## Deck controls

**Note that there are a number of different face plates in the wild so
these images and control descriptions may not exactly match yours. The
locations of the controls are the key things to pay attention to.**

*The controls are the same on both sides of the controller. The left
side controls Deck 1 and the right side controls Deck 2.*

  - **Sync/Range/Hot Cue** button - Changes the BPM of this deck to
    match that of the other. When shifted, toggles the pitch slider
    range. (See top of page to customize.)
  - **Hot cue buttons** - Press to set or recall a hot cue. The buttons
    light up red when one is set. Hold shift and press to delete the
    cue. (We may change this in the future to provide access to 8 hot
    cues.)
  - **Loop In** - Set the in point of a loop
  - **Loop Out** - Set the out point of a loop
  - **Reloop** - Toggle a pre-set loop. Lights red when a loop is
    active.
  - **Loop/Smart** - Toggle track repeat mode
  - **Vinyl/Keylock** - *(Does nothing when un-shifted at the moment.)*
    When shifted, toggles key lock.
  - **\<\< Search/ /2** - Fast-rewind
  - **Search \>\>/ \*2** - Fast-forward

### Effects section

  - **Select knob** - Adjusts the LFO period for the Flanger effect
  - **Control knob** - Adjusts the depth of the Flanger effect
  - **On/Off** - Toggles the Flanger effect on this deck
  - ***Parameter** - Currently does nothing*

### Sample section

// This section is currently unused. //

## Mixer controls

  - ***Midilog 1** - used only for analog source control*
  - **Midilog 2** - In "4 out" mode, this strip is used to control Deck
    1
  - **Midilog 3** - In "4 out" mode, this strip is used to control Deck
    2
  - ***Midilog 4** - used only for analog source control*
