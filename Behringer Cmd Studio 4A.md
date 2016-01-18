# Behringer CMD Studio 4a

![https://media.music-group.com/media/PLM/data/images/products/P0809/2000Wx2000H/CMD-STUDIO-4A\_P0809\_Top\_XL.png](https://media.music-group.com/media/PLM/data/images/products/P0809/2000Wx2000H/CMD-STUDIO-4A_P0809_Top_XL.png)

The Behringer CMD Studio 4a is a 2 deck controller that supports 4
virtual decks.

  - [Mixxx Forum
    Thread](http://www.mixxx.org/forums/viewtopic.php?f=7&t=7868)
  - [Manufacturer's product
    page](http://www.music-group.com/Categories/Behringer/Computer-Audio/DJ-Controllers/CMD-STUDIO-4a/p/P0809/Features)
  - [Manufacturer's
    manual](https://media.music-group.com/media/PLM/data/docs/P0809/CMD-STUDIO-4A_QSG_WW.pdf)

## Mixxx Sound Hardware Preferences

  - Master output: channels 1-2
  - Headphone output: channels 3-4

## Mapping Guide

Almost all functions are defined in the XML file alone and therefore can
be modified in the Mixxx preferences directly. Only the following
functions are scripted:

  - The Wheels.
  - The VU meters.
  - The DEL buttons (because they act as shift/mode buttons).
  - The SCRATCH buttons (because they also act as mode buttons).
  - The PLAY, HOT-CUE, and PITCH BEND buttons (because they are affected
    by one of the above mode buttons). 

The mapping files are well commented and clearly laid out so they can be
easily modified.

Most of the buttons and knobs on the controller behave as you would
expect. The only major departure form the norm are the 4 FX knobs and
buttons at the top of each deck (these are described below).

## Controller Guide

The controller functions as follows in Mixxx:

#### Mixer

  - The deck faders, cross-fader, master and phones (mix & volume) knobs
    all operate as you would expect.
  - Each deck also has a (pre)gain knob in position FX 1.
  - The PHONES button on each deck sends that deck's output to the
    headphone mix (PFL).

#### BROWSE

  - The BROWSE knob scrolls thorough the track list.
  - The BROWSE left and right buttons move through the library tree.
  - The BROWSE ENTER button expands/collapses a library tree item.

#### Mode Buttons

``` 
 * The DEL key under each deck operates as a mode button. i.e. one press and DEL mode is activated, another press and it deactivates (for that particular deck). The main function of the DEL button is to allow HOT-CUES to be cleared. i.e. When DEL is active, hitting a HOT-CUE button that has already been set will clear it. However DEL mode also alters some of the other button functions.
 * The SCRATCH buttons toggle the decks between normal (JOG) mode and SCRATCH mode.
 * The FX 1 button toggles the deck slip mode on/off.
 * The FX 4 button toggles the deck quantise mode on/off.
```

#### A/C B/D

  - The switch buttons (A,B,C,D) make the respective "virtual" deck
    active.
  - On the left deck A = Channel 1, Deck C = Channel 3.
  - On the right deck B = Channel 2, Deck D = Channel 4.

#### Deck Transport

  - The LOAD buttons will load the currently highlighted track in the
    library window into that deck.
  - The deck CUE, PLAY, SYNC, and LOOP buttons work as you would expect.
  - The deck wheels work as you would expect, (taking note of whether
    the top surface of the deck is being touched in both SCRATCH and JOG
    modes).
  - When DEL mode is active (see above) the PLAY button triggers reverse
    playback.

NB: Pressing the deck SYNC button will sync a decks BPM to the currently
playing track, and will also put the deck in SYNC mode. Decks in SYNC
mode will remain BPM locked at all times, (press SYNC again to disable
SYNC mode on that deck).

#### Playback Pitch/Rate

  - The pitch sliders operate as you would expect (i.e. they change the
    playback rate +/- 10%).
  - The PITCH BEND buttons step the playback rate +/- 0.5% per press.
  - The LOCK buttons lock the key so the pitch doesn't change when the
    playback rate changes (as you would expect).
  - If DEL mode is active the PITCH BEND buttons step the key up/down
    without altering the playback rate.
  - If both PITCH BEND buttons are pressed together, the playback rate
    (or key if DEL mode is active) are reset to their normal value.

#### Hot Cue

  - If not currently set, pressing a HOT CUE button sets that hot-cue at
    the current playback position.
  - If already set, pressing a HOT CUE button jumps to that HOT CUE
    position.
  - If DEL mode is active, pressing an already set HOT CUE button will
    clear that hot-cue.

#### Equalizer

  - The HIGH, MID, and LOW knobs (and kill buttons) operate as you would
    expect.

#### FX

  - The "Quick Effect" filter on each deck is assigned to the FX 4 knob.
  - The 2 FX ASSIGN buttons on each deck sends the deck's output to one
    of the first two effects in the effects rack. (The other two effects
    can't be assigned via the controller at this time).

#### Unassigned controls

  - The middle 2 FX knobs are currently unassigned.
  - The FX 2 button is currently unassigned.

NB: The usual Mixxx button hold behaviour is obeyed, e.g. When not
playing, holding the CUE button will start playback from the CUE point
until you release the button where the playback will stop, (but pressing
play while holding the CUE button will force playback to continue after
you release the CUE button). The HOT-CUE buttons work in a similar
manner.
