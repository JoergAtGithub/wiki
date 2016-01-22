# Behringer CMD Studio 4a

[[/media/hardware/cmd-studio-4a_p0809_top_l.png|]]

The Behringer CMD Studio 4a is a 2 deck controller that supports 4
virtual decks and had a built in 4 channel (one stereo master, one
stereo phones) USB "sound-card" built in.

  - [Mixxx Forum
    Thread](http://www.mixxx.org/forums/viewtopic.php?f=7&t=7868)
  - [Manufacturer's product
    page](http://www.music-group.com/Categories/Behringer/Computer-Audio/DJ-Controllers/CMD-STUDIO-4a/p/P0809/Features)
  - [Manufacturer's
    manual](https://media.music-group.com/media/PLM/data/docs/P0809/CMD-STUDIO-4A_QSG_WW.pdf)

## Mixxx Sound Hardware Preferences

  - Master output: channels 1-2
  - Headphone output: channels 3-4

## Controller Guide

Most of the buttons and knobs on the controller behave as you would
expect:

[[/media/hardware/cmd-studio-4a-layout.png|]]

The only major departure form the above are the 4 "FX Control" knobs and
buttons at the top of each deck.

#### Mixer

  - The deck faders, cross-fader, master, and headphone monitoring (mix
    & volume) knobs all operate as you would expect.
  - Each deck also has a (pre)gain knob (leftmost "FX Control" knob).

#### Navigation Control

  - The BROWSE knob scrolls thorough the track list in the library
    panel.
  - The left and right buttons move through the library tree.
  - The ENTER button expands/collapses library tree items.
  - The LOAD buttons in the top of the center of the controller load the
    currently highlighted track in the library window into that deck.

#### Hot Cue Buttons

  - If not currently set, pressing a HOT CUE button sets that hot-cue at
    the current playback position.
  - If already set, pressing a HOT CUE button jumps to that HOT CUE
    position.
  - Pressing DEL toggles DELETE-mode.
  - If DELETE-mode is active, pressing an already set HOT CUE button
    will clear that hot-cue. 
  - The main function of the DEL button is to toggle DELETE-mode to
    allow HOT CUEs to be cleared, however DELETE-mode also alters some
    of the other button functions (see below).

#### Deck Select Buttons

  - The deck select buttons (A, B, C, D) make the respective "virtual"
    deck active.
  - On the left deck: A = Channel 1, C = Channel 3.
  - On the right deck: B = Channel 2, D = Channel 4.

#### Transport Control

  - The LOAD buttons will load the currently highlighted track in the
    library window into that deck.
  - The deck CUE, PLAY, SYNC, and LOOP buttons work as you would expect
    in Mixxx, (SYNC toggles master sync mode).
  - The deck wheels work as you would expect, (including the touch
    sensitive platter changing the behaviour in both SCRATCH and JOG
    modes).

Additionally:

  - FX Control button 1 toggles the deck slip mode on/off.
  - FX Control button 2 toggles the deck repeat mode.
  - FX Control button 3 can be tapped to adjust the beat-grid position.
  - FX Control button 4 toggles the deck quantise mode on/off.

Also, when DELETE-mode is active (see above) the PLAY and CUE buttons
behave differently:

  - The PLAY button triggers reverse-slip playback in DELETE-mode (while
    the PLAY button is held down). This actually temporarily turns
    slip-mode on with reverse playback, then turns slip-mode off and
    reverts to forward playback when the PLAY button is released. This
    means that if you already have slip-mode activated, e.g. by having
    pressed FX-Control button 1 earlier (see above), then slip-mode will
    be turned off as soon as you release the PLAY button (and you will
    return to the playback point where you would have been if you hadn't
    altered the playback).
  - The CUE button triggers normal reverse playback in DELETE-mode
    (while the CUE button is held down), unless slip-mode is already
    active, e.g. by having pressed FX-Control button 1 earlier (see
    above), in which case reverse-slip playback will be triggered while
    CUE is held down. In this case slip-mode won't be deactivated when
    the CUE button is released, (you can repeatedly flip between forward
    and reverse-slip playback by holding and releasing the CUE button),
    then when you finally want to deactivate slip (and return to the
    playback point where you would have been if you hadn't altered the
    playback), you just hit FX Control button 1 again.

#### Playback Pitch/Rate

  - The pitch sliders operate as you would expect.
  - The PITCH BEND buttons step the playback rate up or down.
  - The LOCK buttons turn on key lock so the pitch doesn't change when
    the playback rate changes (as you would expect).
  - If DELETE-mode is active the PITCH BEND buttons step the key up/down
    without altering the playback rate.
  - If both PITCH BEND buttons are pressed together, the playback rate
    (or key if DELETE-mode is active) are reset to their normal value.
  - The lights of the PITCH BEND buttons will indicate whether the
    current pitch is higher or lower than normal for that track.

#### 3-Band EQ and Kill Buttons

  - The HIGH, MID, and LOW knobs (and kill buttons) operate as you would
    expect.

#### FX

  - The "Quick Effect" on each deck is assigned to rightmost "FX
    Control" knob. By default this is a filter effect but can be changed
    in Mixxx's preferences.
  - The 2 FX ASSIGN buttons on each deck send the deck's output to one
    (or both) of two effects in the (default) 4-unit effects rack. The
    left deck (A or C) can be assigned to effect units 1 and/or 2. The
    right deck (B or D) can be assigned to effect units 3 and/or 4.
  - The middle two "FX Control" knobs on each deck act as the effect
    "super" controls for each of the two effects that the deck can be
    assigned to, (most effects should respond sensibly to these
    controls).
