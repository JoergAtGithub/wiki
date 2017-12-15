This is the Work in progress page of **Behringer CMD Studio 2a** mapping
for Mixxx

# Behringer CMD Studio 2a

Ultra-Portable Dual-Deck DJ MIDI Controller with 4-Channel Audio
Interface

[[/media/cmd-studio-2a_p0avw_top_l.png|]]

The Behringer CMD Studio 2a is a 2 deck DJ MIDI controller and has a 4
channel (one stereo master, one stereo headphones) USB sound card built
in.

  - [Mixxx Forum
    Thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=9359)
  - [Manufacturer's product
    page](https://www.musictri.be/Categories/Behringer/Computer-Audio/DJ-Controllers/CMD-STUDIO-2A/p/P0AVW)
  - [Manufacturer's product downloads
    page](http://www.musictri.be/Categories/Behringer/Computer-Audio/DJ-Controllers/CMD-STUDIO-2A/p/P0AVW/downloads)
  - [Manufacturer's quick start
    guide](https://media.music-group.com/media/PLM/data/docs/P0AVW/CMD%20STUDIO%202A_QSG_WW.pdf)

## Mixxx Sound Hardware Preferences

  - Master output: channels 1-2
  - Headphone output: channels 3-4

## Mapping description

All the buttons and knobs on the controller behave as they are labelled:

[[/media/esquema2.png|]]

However, some buttons (Mode, Vinyl, Assign A and Assign B) require extra
explanations.

### Mixer

  - The HIGH, MID, and LOW EQ knobs, deck faders, crossfader, CUE A and
    CUE B buttons (headphone monitoring), and headphone knob (head
    gain), all operate as labelled.

### Navigation Control

  - The FOLDER button focus on folders tree and expand/collapses library
    items.
  - The FILE button focus on files list.
  - The UP and DOWN buttons change the selected item (file or folder) up
    or down one by one. If MODE button is active, file selection moves
    up or down ten by ten.

### Transport Control

  - The LOAD A and LOAD B buttons will load the currently highlighted
    track in the library window into deck A or B.
  - The deck CUE, PLAY and SYNC buttons work as labelled (SYNC toggles
    master sync for the deck).

### Wheels

  - While a track is playing, spinning the wheels temporarily speeds up
    or slows down the track.
  - When a track is stopped, spinning the wheels results in a fast
    search.
  - When the top wheel surface is touched the wheels act as as a
    precision jog.
  - When the VINYL button is activated, moving the wheel while touching
    the top surface scratches the track.

### Hot Cue Buttons

  - If not currently set, pressing a HOT CUE button sets that hot cue at
    the current playback position.
  - If already set, pressing a HOT CUE button jumps to that hot cue
    position.
  - If the DEL button is \*held\*, pressing an already set HOT CUE
    button will clear that hot cue.
  - Tapping the DEL button toggles [\#DEL-mode](#DEL-mode). The button
    will light up blue. DEL-mode alters some of the other button
    functions like a shift button on other controllers.

### Playback Pitch/Rate

  - The pitch knobs control the pitch sliders in Mixxx and change the
    tempo permanently.
  - The PITCH BEND +/- buttons step the playback rate up or down
    temporally while pressed.
  - The PITCH BEND +/- buttons reset the tempo to normal rate when both
    are pressed simultaneously.

### FX Control Buttons

These do not control effects; they have other functions:

  - FX Control button 1 toggles the deck slip-mode on/off, (button
    lights blue when active). Slip-mode is not available in any Mixxx
    skin yet so may be unfamiliar. When slip-mode is active, playback
    continues (muted in the background) during a loop/scratch etc. Once
    disabled, playback will resume where the track would have been if
    the loop/scratch has not taken place (thus preserving the track
    beat).
  - FX Control button 2 toggles the deck repeat mode, (button lights
    blue when active).
  - FX Control button 3 can be tapped to adjust the beat-grid position.
  - FX Control button 4 toggles the deck quantise mode on/off, (button
    lights blue when active).

### FX Control knobs

  - FX Control knob 1 = Deck gain.
  - FX Control knob 2 = FX 1 "super" control (FX unit 1 on left deck,
    unit 3 on right deck).
  - FX Control knob 3 = FX 2 "super" control (FX unit 2 on left deck,
    unit 4 on right deck).
  - FX Control knob 4 = Deck "quick effect" control (by default this is
    a filter effect but can be changed in Mixxx's preferences).

### FX Assign Buttons

  - Tapping either of the 2 FX ASSIGN buttons on each deck will toggle
    the deck's output to one (or both) of two effects in the (default)
    4-unit effects rack. The left deck (A or C) can be assigned to
    effect units 1 and/or 2. The right deck (B or D) can be assigned to
    effect units 3 and/or 4.
  - \*Holding\* an FX ASSIGN button allows the effect in that effect
    unit to be changed using the BROWSE LEFT/RIGHT buttons.

### DEL-mode

DEL-mode is activated by \*tapping\* the deck's hot cue DEL button (the
button will light up blue). This is equivalent to a shift button on
other controllers and so changes the behaviour of a number of the
controller buttons as follows:

  - The HOT CUE buttons act as auto-loop triggers (when \*held\*) in
    DEL-mode. The button layout follows the default "LateNight" skin
    (i.e. top row = \[1/8\] to \[1\], bottom row = \[2\] to \[16\]
    beats). Longer auto-loops can be "locked" (so the HOT CUE button
    doesn't have to be held) by pressing the LOOP ON/OFF button after an
    auto-loop is selected, (locked/playing auto-loops can also be
    resized by selecting a different auto-loop and then re-locking the
    new size with the LOOP ON/OFF button).
  - The CUE button triggers reverse playback (while \*held\*).
  - The PLAY button triggers reverse-slip playback (while \*held\*). NB:
    if you already have slip-mode activated before you trigger
    reverse-slip playback, (e.g. by having pressed FX-Control button 1),
    then slip-mode will be turned off as soon as you release the PLAY
    button (and you will return to the playback point where you would
    have been if you hadn't altered the playback).
  - The PITCH BEND +/- buttons step the key up/down without altering the
    playback rate. If both PITCH BEND buttons are pressed together, the
    playback key is reset to normal.

### Auto-Loops and Slip-Mode

There are no "slip-mode aware" skins in Mixxx yet so the auto-loop
behaviour of this controller (which \*is\* "slip-mode aware") may be a
little different than you might expect to take advantage of this
feature.

  - Auto-loop buttons are (by default) only active when held.
  - In slip-mode, releasing an auto-loop button will immediately
    "re-sync" playback (by disabling, then immediately re-enabling slip
    mode), you may see the slip-mode button flash briefly when this
    happens. This allows for some very interesting "slip-auto-loop"
    effects.
