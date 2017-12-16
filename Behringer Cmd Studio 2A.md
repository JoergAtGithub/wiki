This is the Work in progress page of **Behringer CMD Studio 2a** mapping
for Mixxx 2.0.0

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
  - If the MODE button is active, pressing an already set HOT CUE button
    will clear that hot cue.

### Playback Pitch/Rate

  - The pitch knobs control the pitch sliders in Mixxx and change the
    tempo permanently.
  - The PITCH BEND +/- buttons step the playback rate up or down
    temporally while pressed.
  - The PITCH BEND +/- buttons reset the tempo to normal rate when both
    are pressed simultaneously.

### ASSIGN A and ASSIGN B Buttons

  - ASSIGN A button activates loop mode.
  - ASSIGN B button toggles loop enabled.
  - When loop mode is active, +/- buttons set loop in and loop out
    points.

### MODE button

  - The MODE button has three states: off, shifted and locked. When off,
    led is orange. When shifted, led is blinking blue. When locked, led
    is blue.
  - Pressing the MODE button once activates shifted mode. Pressing the
    button twice activates the locked mode. Pressing again toggles mode
    off.
  - When MODE is shifted, next action will determine a different MODE
    state. Navigation up or down into library sets the state to locked.
    Other actions sets to off.

Xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### Sample Buttons

  - When samples are loaded, deck A sample buttons trigger samples 1 to
    4 of bank 1 and deck B sample buttons trigger samples 1 to 4 of bank
    2. 

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
