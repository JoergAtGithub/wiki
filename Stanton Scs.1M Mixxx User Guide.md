# Stanton SCS.1m & Mixxx User Guide

This guide explains how the SCS.1m is mapped by default in Mixxx.

[[/media/hardware/stantonscs/scs1m-map.png|]]

*Image courtesy of [Stanton Magnetics, Inc.](http://www.stantondj.com),
overlay (C) 2009 Sean M. Pappalardo*

***Easy customization:*** We have provided the following customization
variables at the top of the script you can set to your liking:

  - **slippage** - Slipperiness of the virtual slipmat when scratching
    with the select knob in Control mode. Set this to a number between
    0.0 (perfect turntable) and 0.95 (bent record.)

Just open the `midi/Stanton-SCS1m-scripts.js` file in your favorite text
editor (Wordpad works too) and you'll see these variables right near the
top. Edit & save, then restart Mixxx and enjoy.

## Deck controls

*Refer to the image above, top to bottom*

  - **a** buttons: Sync function: change the pitch of the deck so that
    its BPM matches that of the other deck (assuming the pitch range is
    sufficient)
  - **b** buttons: Toggle headphone cue
  - **Gain, High, Mid, Low** knobs: as labeled
  - ***Pan** knob: unused*
  - **c** encoders
  - Rotate to increase or decrease the pitch range in 1% steps
  - Press to toggle the flange effect
  - **c** displays: Show the current pitch adjustment percentage. The
    back light color changes with the pitch range:
  - Green = 1%-25%
  - Orange = 25%-50%
  - Red = 50% and above
  - **c** A buttons: Permanently lower the pitch by 1%
  - **c** B buttons: Permanently raise the pitch by 1%
  - **e** sliders: Pitch adjust
  - **e** buttons: Temporarily raise the pitch by 4% for as long as held
    (pitch bend up.)
  - **g** buttons: Temporarily lower the pitch by 4% for as long as held
    (pitch bend down.)
  - **d** encoders
  - Rotate to nudge the track either direction (akin to twisting a
    record spindle)
  - Press to toggle reverse playback
  - LEDs show current track position
  - **d** displays: Show the current track time remaining. They will
    flash slowly when less than 30 seconds remain, quickly when less
    than 15 seconds remain.
  - **d** A buttons: Rewind
  - **d** B buttons: Fast-forward
  - **f** sliders: Volume adjust
  - **f** buttons: Play/pause
  - **h** buttons: Cue

## Global controls

*Refer to the image above, top to bottom*

  - **z** button: Toggle cross fader start/cue
  - **Master, Headphones, Cue Mix** knobs: as labeled
  - ***Zone** knob: unused*
  - ***Gain** knob: unused*
  - **i** knob: Adjust flange effect depth
  - **j** knob: Adjust flange effect delay
  - **k** knob: Adjust flange effect period (Low Frequency Oscillator)
  - **l** knob: Adjust master pan (balance)
  - ***p** button: unused*
  - **m** button: BPM tap for Deck 1
  - ***n** button: unused*
  - **o** button: BPM tap for Deck 2
  - **Preset** buttons: Hot cue points for the selected deck (**q**
    button)
  - **Bank Down** button: select backward between Library, Playlist, and
    Browse views
  - **Bank Up** button: select foreward between Library, Playlist, and
    Browse views
  - **q** button: Change which deck's hot cues are active (**Preset**
    buttons.) Off is Deck 1, On (red) is Deck 2.
  - **r** jog wheel:
  - **Browse mode**:

<!-- end list -->

``` 
    * Rotate to move the track select highlight
    * Press to load the selected track into the first stopped deck, if any
* **Control mode**:
    * Rotate to scratch the song on the selected deck
    * //Pressing does nothing//
* **Cancel** button: **Control mode**: press to select Deck 1 for scratching
* **Enter** button: **Control mode**: press to select Deck 2 for scratching
* //**Setup** button: unused by Mixxx but will enter the mixer's internal setup menu//
* **Control** button: Selects scratching mode for the jog wheel
* **Browse** button: Selects track browse mode for the jog wheel
```

*(Any unlabeled controls are not currently used.)*
