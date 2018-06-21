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

[[/media/hardware/hercules-djconsole-rmx-2.png|]]

### Managed by Mixxx

| Figure     | \[**SHIFT**\]? | Long-press? | Control Name        | Description                                  |
| ---------- | -------------- | ----------- | ------------------- | -------------------------------------------- |
| 11         | ✘              | ✘           | \[**MAIN VOLUME**\] | Controls *Master* volume                     |
| 13         | ✘              | ✘           | \[**VINYL**\]       | Split headcue                                |
| 13         | ✔              | ✘           | \[**VINYL**\]       | Maximize library                             |
| 20         | ✘              | ✘           | \[**CROSS FADER**\] | Controls crossfader                          |
| 21         | ✘              | ✘           | \[**CUE TO MIX**\]  | Controls headmix                             |
| 7          | ✘              | ✘           | \[**MIC ON/OFF**\]  | Toggle microphone on/off and talkover on/off |
| 15 (Left)  | ✘              | ✘           | \[**FILES**\]       | Go To Item in Library                        |
| 15 (Left)  | ✔              | ✘           | \[**FILES**\]       | Add to bottom of Auto DJ playlist            |
| 15 (Right) | ✘              | ✘           | \[**FOLDERS**\]     | Move focus backward in Library               |
| 15 (Right) | ✔              | ✘           | \[**FOLDERS**\]     | Toggle Auto DJ                               |
| 15 (Up)    | ✘              | ✘           | \[**UP**\]          | Move vertically up in Library                |
| 15 (Up)    | ✘              | ✔           | \[**UP**\]          | Scroll vertically up in Library              |
| 15 (Down)  | ✘              | ✘           | \[**DOWN**\]        | Move vertically down in Library              |
| 15 (Down)  | ✘              | ✔           | \[**DOWN**\]        | Scroll vertically down in Library            |

### Managed by the controller

The following functions directly affect the controller's sound card, so
adjusting these will not change anything on screen in Mixxx:

| Figure | \[**SHIFT**\]? | Long-press? | Control Name      | Description                           |
| ------ | -------------- | ----------- | ----------------- | ------------------------------------- |
| 22     | \-             | \-          | HEADPHONES VOLUME | Controls the headphones output volume |
| 6      | \-             | \-          | MIC VOLUME        | Controls the microphone volume (gain) |

## Deck Functions

| Figure | \[**SHIFT**\]? | Long-press? | Control Name      | Description                           |
| ------ | -------------- | ----------- | ----------------- | ------------------------------------- |
| 22     | \-             | \-          | HEADPHONES VOLUME | Controls the headphones output volume |
| 6      | \-             | \-          | MIC VOLUME        | Controls the microphone volume (gain) |
