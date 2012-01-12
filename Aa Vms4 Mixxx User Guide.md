# American Audio VMS4 & Mixxx User Guide

## Setup

*Recommended setup for Mixxx v1.9.0 and up:*

**Important: Mixxx expects the VMS4 to be set to "Post EQ" mode for best
sound quality.** Do this by holding down the Cue button on Midilog 4
while powering on the unit. You only need to do this once. (Each time
you do it, it changes the mode back and forth.) Consult the [user
manual](http://vms4dj.com/Files/vms4.pdf) for more information. (To
check the status of this in Linux, at a console, issue the command
`lsusb -v|grep 'iSerial\|iProduct'` and look at the serial number under
the VMS4 device per the instructions in the user manual.)

1.  Make sure the VMS4 is off
2.  Slide the switch on the front of the VMS4 to "4 OUT"
3.  Turn on the unit (and plug in the USB cable if you haven't yet)
4.  Start Mixxx
5.  Open Preferences
6.  Click Sound Hardware. In the right pane:
    1.  Set the sample rate to 44100Hz
    2.  Set the Master output to **None**
    3.  Set the Headphone output to **None**
    4.  Set the Deck 1 output to the **VMS4** device and **Channel 1-2**
        (may show as "USB Audio Device" on Windows)
    5.  Set the Deck 2 output to the **VMS4** device and **Channel 3-4**
7.  Plug your headphones into the VMS4's jack on the front. You will use
    the VMS4's CUE buttons and knobs for headphone control.
8.  Still in the Preferences, expand "MIDI Controllers" on the left
9.  Select the "VMS4 MIDI" device (may show as "USB Audio Device" on
    Windows)
10. Click the Enable checkbox in the right pane
11. Click the drop-down and choose the "American Audio VMS4" mapping
12. Click OK and the controller should light up. (In 1.9.x, the
    controller will light up when you load a track to a deck.)
13. Continue reading below to know how everything is mapped

## Control

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
    light up red when one is set.
  - 1.9.x: You can only access hot cues 1-4. Hold shift and press to
    delete the cue.
  - 1.10.x: Hold shift and press to access hot cues 5-8. (The buttons
    light up blue for these.) Hold Vinyl and press to delete the cue.
    (Note: there is a bug in some firmware versions that causes hot cues
    5 and 6 to be deleted simultaneously. We are in communication with
    AA about the issue.)
  - **Loop In** - Set the in point of a loop
  - **Loop Out** - Set the out point of a loop
  - **Reloop** - Toggle a previously-set loop. Lights red when a loop is
    active.
  - **Loop/Smart**
  - 1.9.x: Toggle track repeat mode
  - 1.10.x: Start a 4-beat loop. Hold Shift and press to toggle
    quantization (locking to the nearest beat.)
  - **Vinyl/Keylock** - *(Does nothing on its own when un-shifted at the
    moment.)* When shifted, toggles key lock.
  - **\<\< Search/ /2** - Fast-rewind
  - 1.10.x: Hold Shift and press to halve the current loop length
  - **Search \>\>/ \*2** - Fast-forward
  - 1.10.x: Hold Shift and press to double the current loop length
  - **Wheel**
  - Move the wheel while touching the top to scratch the current track
    like a vinyl record
  - Move the wheel without touching the top (so on the sides) to perform
    a temporary pitch bend

### Effects section

  - **Select knob** - Adjusts the LFO period for the Flanger effect
  - **Control knob** - Adjusts the depth of the Flanger effect
  - **On/Off** - Toggles the Flanger effect on this deck
  - ***Parameter** - Currently does nothing*

### Sample section

// **1.9.x:** This section is currently unused. //

**1.10.x:** The left side of the controller controls Sampler 1, and the
right, Sampler 2.

  - **Select knob**
  - Rotate to move the highlight in the library.
  - Press to load the currently highlighted track into the sampler.
  - Hold Shift and press to eject the current track from the sampler
    (when the sampler is not playing.)
  - **Volume knob** - Adjusts the volume of the sampler
  - **Play**
  - Press to play the sample from the beginning. Press while playing for
    a stutter-play effect (play again from the beginning.)
  - Hold Shift and press to stop playing.
  - ***Rec** - Currently does nothing*

## Mixer controls

  - ***Midilog 1** - used only for analog source control, unused by
    Mixxx*
  - **Midilog 2** - In "4 out" mode, this strip is used to control Deck
    1
  - **Midilog 3** - In "4 out" mode, this strip is used to control Deck
    2
  - ***Midilog 4** - used only for analog source control, unused by
    Mixxx*
