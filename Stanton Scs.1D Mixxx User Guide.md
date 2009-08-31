# Stanton SCS.1d & Mixxx User Guide

This guide explains how the SCS.1d is mapped by default in Mixxx 1.7.x.

[[/media/hardware/stantonscs/scs.1d_callouts.jpg|]]

*Image courtesy of [Stanton Magnetics, Inc.](http://www.stantondj.com)*

***Easy customization:*** We have provided the following customization
variables at the top of the script you can set to your liking:

  - **pitchRanges** - The pitch ranges selectable with the Range button
    (It's possible to add more if you need them but the .rangeButton
    function will need to be extended.)
  - **fastDeckChange** - If set to true, changes decks instantly by
    skipping the flashing lights. Useful for beat juggling on one unit.
  - **globalMode** - If true, the unit will stay in the current section
    modes on virtual deck changes (instead of switching to the modes you
    were in the last time you controlled that virtual deck.) The trigger
    pad section always stays in the current mode regardless of this
    setting.
  - **platterSpeed** - The speed of the platter at 0% pitch: 0=33 RPM,
    1=45 RPM
  - **deckChangeWait** - Time in milliseconds to hold the Deck Select
    button down to avoid changing decks
  - **padVelocity** - If set to true, uses the velocity values when
    recalling cues on the trigger pads (this is toggle-able with a
    button on the unit as well.)
  - **scratching**: *All of these values are heavily dependent on your
    latency setting. Adjust as needed.*
    1.  **sensitivity** - How much the audio moves for a given platter
        arc. Set this to a number between 0.01 (slow) to 0.99 (fast)
    2.  **stoppedMultiplier** - Correction to get the same platter
        sensitivity when the deck is stopped (set higher for higher
        latencies, e.g. 10ms = 1.7, 4ms = 1.0.)

Just open the `midi/Stanton-SCS1d-scripts.js` file in your favorite text
editor (Wordpad works too) and you'll see these variables right near the
top. Edit & save, then restart Mixxx and enjoy.

Now let's take a look at how the controls operate, starting in the upper
left and moving counter-clockwise:

## Mode switch buttons

  - ***Setup**: unused by Mixxx but will enter the deck's internal setup
    menu*
  - ***Control**: unused*
  - **Browse**: Allows browsing the library with the platter
  - **Vinyl**: Take a guess\! :-)

<!-- end list -->

  - **⇒/Enter**: Loads the currently selected track into the currently
    selected virtual deck
  - **Deck Select**: Switches to the other virtual deck
  - ***⇐/Cancel**: unused*

## Transport section

  - **circle button**: Toggles headphone cue
  - **«**: Fast rewind
  - **»**: Fast forward
  - **|«***: unused*
  - **»|***: unused*
  - **Cue, Sync, Play/Pause**: as labeled
  - **BPM**: BPM tap

## Trigger Pad section

The trigger pads are used to set and recall hot cues/samples. You can
use them as you would a sampler if the target deck is stopped (where it
will only play as long as you are pressing the pad) or as hot cues (if
the target deck is playing.) You set a cue simply by pressing an unlit
pad at the desired point. It lights green when there's a cue set and the
corresponding display shows the cue point in
`minutes:seconds.centiseconds` format.

  - ***circle buttons** above the displays: unused*
  - **circle button** at the top right of the section:
  - Velocity toggle: When lit red, the target deck's volume will be
    adjusted by how hard you strike the pads. Press this button to
    toggle the feature.
  - Delete cues: Hold this button down and press a pad to delete the cue
    stored there
  - **circle buttons** at the bottom right of the section: These select
    the cue bank for each deck. The top button chooses the bank for deck
    one and the bottom for deck two. There are three banks for each deck
    denoted by the button color: green (1), red (2), and amber (3). In
    this way you can recall cues/play samples on either deck at any time
    regardless of what the rest of the controller is doing.

## Pitch slider section

  - **Pitch slider**:
  - Pitch adjust: directly corresponds to the slider on screen for the
    currently selected virtual deck. Since the slider is motorized, it
    will move on its own if you change decks or adjust the slider on the
    screen.
  - Cross-fader adjust: will move to and allow adjustment of the
    on-screen cross-fader while the Range button is held down.
  - **Range button**:
  - Toggles between the pitch range values specified in the
    **pitchRanges** global variable mentioned at the top of this page
  - When held, allows the pitch slider to be used to adjust the
    cross-fader. If you do this, the pitch range will not be changed
    when you release the button.
  - **Reset button**: Resets the slider to the center position when
    adjusting pitch or the cross-fader.

## Preset section

This section is used for instant pitch changes for the current virtual
deck (and will also control looping in a future version of Mixxx.) It's
useful when using the pads as samplers to further vary the sounds.

They offer the following arrangements, increasing from left to right,
top to bottom:

  - **circle buttons** at the bottom of the section:
  - **Top: Fixed increment** - Each trigger button sets the pitch 3.33%
    above or below its horizontal neighbors.
  - **Middle: Key change** - Center row buttons are one semitone away
    from their vertical neighbors and the outside ones are three
    semitones away (for harmonic key changes.)
  - **Bottom: Notes** - Buttons correspond to major scale notes (ala
    Vestax Controller One.) This is most useful with a constant-pitch
    sound or chord. (You can generate one in Audacity.)

Remember you can return to the original pitch (tonic) by pressing Reset
just above the pitch slider.

Note that when you use one of these buttons, the pitch range is
automatically set to 100% in order for the values to be set correctly.

*Key change and Note modes were tuned with respect to 440Hz A (above
middle C.)*

## Encoder section

Pressing any of the encoders returns the parameter to the default value.

  - **circle button** to the left of the section: changes the parameter
    bank the encoders adjust:
  - **Green**:

<!-- end list -->

``` 
    * **1st encoder** (from the left): adjusts low frequency equalizer
    * **2nd encoder**: adjusts mid frequency equalizer
    * **3rd encoder**: adjusts high frequency equalizer
    * **4th encoder**: adjusts deck volume
    * **circle buttons** under each display: momentary kill buttons for the corresponding parameter
* **Red**:
    * **1st encoder** (from the left): adjusts flanger depth
    * **2nd encoder**: adjusts flanger delay
    * **3rd encoder**: adjusts flanger period (Low Frequency Oscillator)
    * **4th encoder**: adjusts pre-fader track gain
    * **circle button** under the 1st display: toggles the flange effect for the current deck.
    * //**circle buttons** under the other displays: unused//
* When holding down the **Deck Select** button:
    * **1st encoder** (from the left): adjusts the cue/main headphone mix
    * **2nd encoder**: adjusts the headphone volume
    * **3rd encoder**: adjusts the master balance (pan)
    * **4th encoder**: adjusts the master volume
```

*(Any unlabeled controls are not currently used.)*
