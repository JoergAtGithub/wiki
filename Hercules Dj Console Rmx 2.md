# Hercules DJ Console RMX 2

[[/media/hardware/Hercules-DJ-Console-RMX-2.png|Hercules-DJ-Console-RMX-2.png]]

  - [Manufacturer's product
    page](http://www.hercules.com/us/DJ-Music/bdd/p/193/djconsole-rmx-2/)
  - [Manual / Midi
    commands](https://support.hercules.com/de/product/djconsolermx2-de)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=11860)
  - [Previous forum
    thread](http://mixxx.org/forums/viewtopic.php?f=7&t=4541)

This all-in-one DJ controller features a built in 4 channel sound card
with balanced XLR master outputs and a balanced microphone input. It is
a USB class compliant MIDI and audio device (unlike older Hercules
controllers).

## User Options

To change the mapping's user options, you have to open the script file
(\*.js). At the top of the file under **USER OPTIONS** the following
settings can be made:

  - **DJCRMX2.jogwheelSensivity**: Sets the jogwheel sensivity. 1 =
    default, 2 is twice as sensitive, 0.5 is half as sensitive.
  - **DJCRMX2.jogwheelShiftMultiplier**: Sets how much more sensitive
    the jogwheels get when holding \[**SHIFT**\]. Set it to 1 to disable
    jogwheel sensitivity increase when holding \[**SHIFT**\].
  - **DJCRMX2.twinkleVumeterAutodjOn**: If true, level-meter twinkles if
    *AutoDJ* is enabled.
  - **DJCRMX2.autoPFL**: If true, PFL / Cue (headphone) is being
    activated by loading a track into certain deck.
  - **DJCRMX2.vuMeterOutputMaster**: If true, deck vu meters show master
    output (L = Deck A, R = Deck B). If false, deck vu meter shows deck
    output (mono).
  - **DJCRMX2.showHideSamplersEffectsOnPadMode**: If true, *Samplers*
    and *EffectRack* get shown or hidden in dependance of Pad-Mode.

## General Functions

### Managed by Mixxx

| Group           | Figure     | \[**SHIFT**\]? | Button Name                   | Description                                                                                                         |
| --------------- | ---------- | -------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 5 - BROWSER     | 2, 3, 4, 5 | \-             | \[**LOAD**\]                  | Loads the selected track into the specific deck                                                                     |
| :::             | 2          | \[**SHIFT**\]  | \[**LOAD**\]                  | AutoDJ - Toggle BPM sync                                                                                            |
| :::             | 3          | \[**SHIFT**\]  | \[**LOAD**\]                  | AutoDJ - Toggle Key sync                                                                                            |
| :::             | 1          | \-             | \[**ROTARY SELECTOR**\]       | Move UP or DOWN the specified number of locations in Library (MoveVertical function)                                |
| :::             | 1          | \-             | \[**ROTARY SELECTOR PRESS**\] | Equivalent to double clicking the currently selected item in Library (GoToItem function)                            |
| :::             | 1          | \[**SHIFT**\]  | \[**ROTARY SELECTOR**\]       | Move LEFT or RIGHT the specified number of locations in Library (MoveHorizontal function)                           |
| :::             | 1          | \[**SHIFT**\]  | \[**ROTARY SELECTOR PRESS**\] | Add track from Library to AutoDJ queue at top/bottom (see user options: default = at bottom)                        |
| :::             | 6          | \-             | \[**BACK**\]                  | Currently focused pane changes in Library - previously focused pane will be focused (MoveFocusBackward function)    |
| :::             | 6          | \[**SHIFT**\]  | \[**BACK**\]                  | Maximize view of Library                                                                                            |
| :::             | 7          | \-             | \[**LOAD PREPARE**\]          | Load selected track into PreviewDeck, jump to position (see user options) and play, else stop already playing track |
| 3 - MIXER       | 1          | \-             | Crossfader                    | Controls Mixxx crossfader, fades between deck 1, 3 and 2, 4                                                         |
| :::             | 2          | \-             | Channel fader                 | Controls deck volume                                                                                                |
| :::             | 2          | \[**SHIFT**\]  | Channel fader                 | Fader start (starts playing deck when rising deck volume)                                                           |
| :::             | 3          | \-             | TRIM                          | Controls deck gain                                                                                                  |
| :::             | 4          | \-             | EQ HIGH                       | Controls deck's equalizer/filter high frequencies                                                                   |
| :::             | 5          | \-             | EQ MID                        | Controls deck's equalizer/filter mid frequencies                                                                    |
| :::             | 6          | \-             | EQ LOW                        | Controls deck's equalizer/filter low frequencies                                                                    |
| :::             | 7          | \-             | \[**CUE**\]                   | Toggles PFL/Cue (headphones) for specific deck                                                                      |
| :::             | 7          | \[**SHIFT**\]  | \[**CUE**\]                   | BPM Tab function for specific deck                                                                                  |
| :::             | 9          | \[**SHIFT**\]  | \[**MASTER CUE**\]            | Toggles split cue (headphones)                                                                                      |
| :::             | 10         | \-             | Crossfader Assign             | Crossfader assignment - deck to crossfader (left (A), right (B) or center (THRU))                                   |
| :::             | 14         | \-             | SAMPLER VOLUME                | Controls volume of all available Sampler decks                                                                      |
| 4 - FRONT PANEL | 1          | \-             | Crossfader curve              | Controls Mixxx crossfader curve                                                                                     |
| 1 - DECK        | 25         | \-             | \[**PANEL SELECT**\]          | Show/hide Sampler decks / Effect rack                                                                               |

### Managed by the controller

The following functions directly affect the controller's sound card, so
adjusting these will not change anything on screen in Mixxx:

| Group           | Figure | \[**SHIFT**\]? | Button Name         | Description                                     |
| --------------- | ------ | -------------- | ------------------- | ----------------------------------------------- |
| 3 - MIXER       | 8      | \-             | MASTER LEVEL        | Controls the master output volume               |
| :::             | 9      | \-             | \[**MASTER CUE**\]  | Toggles master cue                              |
| :::             | 13     | \-             | HEADPHONES MIX      | Controls headphone's audio source (cue, master) |
| :::             | 15     | \-             | BOOTH MONITOR LEVEL | Controls the booth output volume                |
| 4 - FRONT PANEL | 2      | \-             | INPUT SELECT        | Controls deck source (PC, MIC, CD, PHONO, LINE) |

## Deck Functions

## Mapping

[[/media/hardware/hercules-djconsole-rmx-2.png|hercules-djconsole-rmx-2.png]]

1.  Jog wheel: Scratch when pressed, seek while paused, pitchbend while
    playing
2.  Fast-forward/rewind, with shift: jump to start/end
3.  Pitch Bend -/+
4.  Speed control, Tempo and pitch, depending on keylock 
5.  Microphone jack
6.  Microphone volume (controls the built in sound card, not software
    microphone gain in Mixxx)
7.  Enable/disable microphone (controls the built in sound card, not
    microphone control in Mixxx)
8.  Effect Super knob, with shift: Dry/Wet 
9.  Source 1/2 unused 
10. Gain
11. Master Gain (controls software gain in Mixxx)
12. EQ Kill
13. Vinyl (unused)
14. Mixing EQ
15. Library navigation
16. Load selected track to deck A/deck B
17. Pre-fader listening (PFL) to deck A/deck B
18. Volume meter
19. Deck volume
20. Crossfader
21. Headphone mix
22. Headphone volume (controls the built in sound card, not software
    headphone gain in Mixxx)
23. Headphone jack
24. Multifunctional pads for loops, effects, samples, and hot-cues.
    (pressure sensitivity unused)
25. Multifunctional pads mode display (hardwired)
26. Multifunctional pads mode selection (hardwired)
27. Shift
28. Sync enable
29. Cue
30. Play/pause
