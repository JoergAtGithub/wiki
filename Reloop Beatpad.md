[[/media/hardware/reloop/reloopbeatpadtp.png|]]

  - [Manufacturer's product page](http://www.reloop.com/reloop-beatpad)
  - [Forum thread : mapping to download, users feedback, installation
    notes](http://www.mixxx.org/forums/viewtopic.php?f=7&t=7581)

The **Reloop Beatpad** is a conventional 2 channel controller that is
primarily designed to work with algoriddim‘s djay on the iOS platformand
and more recently on the Android platform, but can work with computers
too via MIDI.

-----

(work in progress)

# Operation guide to use with Mixxx

## MIXER SECTION

### CrossFader

Blends audio between left and right mixer channels.

### Volume Faders

Adjust the Volume of each channel. If [Fader
Start](#1-and-2-\(Track-select-buttons\)) is enabled the deck will stop
at the previously used Cue if the Volume Fader reaches the minimum
position and will start playing if the Volume fader moves from the
minimum position.

### 1 and 2 (Track select buttons)

  - **Load a track :** Press these buttons to load the selected track
    from the Browser to left or right deck. The LED of the button will
    be on if the deck is loaded. 
  - **Eject :** Hold the same button for more than half of a second to
    unload the same deck.
  - **Fader Start :** Hold **[SHIFT](#SHIFT)** down and then press one
    of these buttons to enable the **Fader Start** on a deck. The LED of
    the button will blink if Fader Start is enabled. If Fader Start is
    enabled the deck will stop at the previously used Cue if the Volume
    Fader reaches the minimum position and will start playing if the
    Volume fader moves from the minimum position.

### PFL (symbolized by a headphone)

  - **PFL :**Press these buttons to send each channel to the Headphones
    Output channel for pre-listening.
  - **Slip mode :**Hold **[SHIFT](#shift)** down and then use these
    buttons to activate/desactvate Slip Mode.When active, the playback
    continues muted in the background during a loop, scratch etc. Once
    disabled, the audible playback will resume where the track would
    have been.

### Equalizer

  - **LOW :** Adjust the Low (Bass)frequencies for each mixer channel.
  - **MID :** Adjust the Mid frequencies for each mixer channel.
  - **HIGH :** Adjust the High (Treble) frequencies for each mixer
    channel.
  - **GAIN :** Adjust the Gain of each mixer channel.
  - **MASTER :** Adjust the level of the Master Output. Hardware
    operation - movement is not visible on the Mixxx GUI, it is
    independent from the software.
  - **Cue Mix (Hadphones mixing) :** Adjust how the Channels and the
    Master Output blend at the Headphones Channel.
  - **Phones (Hadphones level) :** Adjust the Volume Output of the
    Headphones Channel. Hardware operation – movement not visible on the
    Mixxx GUI, it is independent from the software.
  - **AUX :** Adjust the Volume of the AUX Input. Hardware operation –
    movement is not visible on the Mixxx GUI, it is independent from the
    software.

### REC

Use this button to start/stop record of your mixing session.

### Browse Knob

Scroll through files of folders.

  - **Turn** in order to select a track in the song list.
  - **Push** in order to load the selected track into first stop deck.
  - **[SHIFT](#shift)+Turn** in order to select a folder or subfolder in
    the left item list sidebar.
  - **[SHIFT](#shift)+Push** in order to open/close folders and
    subfolders in the left item list sidebar.

## DECK CONTROLS SECTION

### SHIFT

Press and hold one of those buttons to access secondary functions of
other controls on the Beatpad. The **SHIFT** buttons can operate as a
toggle or a momentary one depending on the **SHIFT LOCK** switch
position on the back side of the Reloop Beatpad.

### PLAY/PAUSE

  - **Play/pause :** Press to play/pause the track. If there was no
    track loaded into the dec and a track is selected in the song list
    windows, it is loade and the playback of this track starts
    immediatly.
  - **Censor :** Hold **[SHIFT](#shift)** down and then press this
    button to play the track in reverse. When released the track will
    continue to play from the position it would have been if the button
    was never pressed. In other words, it enables reverse and slip mode
    while held.

### JUMP

  - **While playing, or stopped :** If the Cue point is set, seeks the
    player to it and starts playback.
  - **Brake :** Hold **[SHIFT](#shift)** down and then press this button
    to stop the track with a gradual brake. If the **JUMP** button is
    released before the track has completely stopped, the track is then
    played back to its regular speed.
  - **Spinback:** see the **[Instant FX](#Instant-fx)** usage.

### SET

  - **While playing :** Seeks the track to the cue-point and stops.
  - **While stopped :** Sets the cue point (Pioneer/Mixxx mode) OR
    preview from it (Denon mode).  
    If the Cue point is already set at the current position of the
    track, hold this button to play the track and release it to return
    to the Cue point and pause it.To continue playback without returning
    to the Cue Point, press and hold the **SET** Button, then press and
    hold the **[Play/Pause](#Play/Pause)** Button and then release both
    buttons.
  - **Hint:** Change the default cue mode in Preferences -\> Interface.
    The Pioneer mode is the more consistent with the Reloop Beatpad. 
  - **Key lock :** Hold **[SHIFT](#shift)** down and then press this
    button to enable/disable the Key-lock.

### SYNC

  - **Press once** to synchronize the tempo (BPM) and phase to that of
    the other track.
  - **Press twice quickly** to play the track immediatly, synchronized
    to the tempo (BPM) and to the phase of the other track, if the track
    was paused.
  - **Sync Lock :** Hold for at least half of a second to enable **sync
    lock** for this deck. Decks with sync locked will all play at the
    same tempo, and decks that also have **quantize** enabled (wich is
    enabled by default by the mapping) will always have their beats
    lined up.  
    **Note :** the **quantize** mode is not mapped on the controller but
    can be enabled/desabled from Mixxx.

### JOGWHEEL

Touch sensitive platters for scratching (Scratch mode/iCut mode),
bending (Scratch mode/CD mode) or Seek mode.  
The jogwheel offers multi-color leds, which will show the playing marker
(Scratch mode), the song progress bar (in Seek mode), and other colored
combinations depending on the applied effect, loop, loop roll or Filter.
If no track is loaded, the jogwheel displays a red cross. At the end of
a track, the jogwheel is flashing red faster and faster until it reaches
the end of the track (full steady red).

#### Scratch mode

Toggle with the **JOG SCRATCH** button.  
Use the jogwheel to scratch and the outer ring to bend (like in [CD
mode](#CD-mode)).

  - **iCut mode :** Hold **[SHIFT](#shift)** down and scratch to scratch
    in "automagic" scratch mode. In Mixxx, we to stick with the reloop
    explanation : it is "as it is supposed to be done", i.e. : *this
    mode simulates a scratch routine. When the jog wheel is turned back
    the crossfader closes, when the jog wheel is turned forward the
    crossfader will open.*
  - **Note :**

<!-- end list -->

``` 
    * According to the Quick start guide :\\   iCut MODE :\\   DJAY will automatically cut your track with the cross fader when holding SHIFT and scratching with the jog wheel.
    * According to Reloop Website ( http://www.reloop.com/reloop-beatpad , Explorer tab) :\\ iCut :\\ this mode simulates a scratch routine. When the jog wheel is turned back the crossfader closes, when the jog wheel is turned forward the crossfader will open."
    * In Practice :\\ DJAY software is closing/opening the crossfader quicly without taking into account the direction of the whheel.\\ 
              
```

#### Seek mode

Toggle with the **JOG SEEK** button.  
Use the jogwheel to navigate through the track.

#### CD mode

Desactivate both the [Scratch mode](#Scratch-mode) and the [Seek
mode](#Seek-mode) to enable it.  
Use the jogwheel to temporarily bend the track wich has the effect of
temporary slow-down or speed up the tempo.

### PITCH BEND

  - **Pitch bend :** Use these buttons temporary slow-down/speed up the
    tempo of the track.  
    Once the buttons are released the track will continue to play at the
    tempo designated by the pitch fader.
  - **Beat Jump :**Hold **[SHIFT](#shift)** down and then use these
    buttons to jump 1 beat backwards or forward.

### PITCH

Controls the track's playback tempo. The red LED indicates that the
pitch fader of the unit is on zero (center) position.

## LOOPS SECTION

(see also **[Bounce Loop (Roll) mode](#Bounce-Loop-\(Roll\)-mode)**
section)

### Good to know for beginners

Two kinds of loops exist, the **regular loop** and the **roll loop**.

  - **Regular loop :** It loops the track for x amounts of beats and
    when you exit the loop the track is at the same place where the loop
    stopped.
  - **Roll loop :** It loops the track for x amount of beats - but the
    track continues playing in the background. Therefore, when you exit
    the loop roll the track is further into the song for the period of
    time the loop roll button was hold pressed.  
    As a matter of fact, it is a **regular loop** in **[slip
    mode](#PFL-\(symbolized-by-a-headphone\))** (see
    **[PFL](#PFL-\(symbolized-by-a-headphone\))** section).

### LOOP SIZE

  - **Loop size :** Turn the encoder anti-clockwise to half the size of
    the loop and clockwise to double it. 
  - **Loop move :** Hold **[SHIFT](#shift)** down and then use the
    encoder to move the triggered loop forward or backwards by 1 beat.
  - **Activate/desactivate :** (Acts exactly like the
    **[LOOP](#loop\\)** Button) 
  - **Regular loop mode :** Push (and release) the encoder to trigger
    the selected size loop in **regular loop mode**. 
  - **Roll loop mode :** Press (and keep down) to trigger a momentary
    Loop Roll of the selected size.
  - **Toggle loop mode :** Hold **[SHIFT](#shift)** down and then push
    the encoder to toggle between Regular and Roll Loop mode.

### LOOP

  - **Regular loop mode :** Press this button to trigger a loop of the
    selected size (toggle function).
  - **Roll loop mode :**When Roll loop mode is selected, the button will
    apply a temporary **Roll loop** (while pressed).

## EFFECT SECTIONS

(see also [Instant FX mode](#Instant-FX-mode) [Sampler
mode](#Sampler-mode) sections)

#### FX ON

Push (and relesae) this button to trigger the selected effect for the
corresponding deck (toggle function).

#### FX SELECT

  - **Select :** Use this encoder to select an effect for the current
    selected rack. 
  - **Temporary effect :** Push and hold the encoder to apply
    temporarily the effect of the current selected rack for the
    corresponding deck (while pressed).
  - **Quick Effect :** Hold **[SHIFT](#​shift)** down and then push the
    encoder Activate or Kill the **Quick Effect**. You can change the
    Quick effect assigned in Mixxx, via Options -\> Settings-\>​
    Equalizers -\> Quick Effect.

#### FX PARAM.

  - **SUPER :** Use this knob to control the **SUPER** parameter of the
    effect for the current selected rack.
  - **MIX :** Hold **[SHIFT](#​shift)** down and then use this knob to
    control the **MIX** parameter of the effect for the current selected
    rack.

#### FILTER

  - **Quick Effect :** Use this knob to apply the Quick effect (usually
    Filter, but you can change it) to the deck. In middle position no
    effect is applied.
  - **Key :** Hold SHIFT down and use this knob to adjust the key
    (pitch) of the track without changing the tempo. In middle position
    the track will have its original value.

## PADS SECTION

The 4 Performance Pads offer 4 different modes, depending on the 4 PAD
MODE buttons just above.

### HotCues mode

#### CUE

Press the **CUE** mode button to set the PADs to HOT CUE mode.

#### Pads

  - **Press** each one of the 4 pads to assign a Hot Cue Point (1 to 4)
    or returns the track to that Hot Cue Point. When a Hot Cue Button is
    unlit, you can assign a Hot Cue Point by pressing it at the desired
    point in your track. Once it is assigned, the Hot Cue Button will
    light up blue.
  - **[SHIFT](#SHIFT)+Press** to delete its assigned Hot Cue Point.

### Bounce Loop (Roll) mode

#### BOUNCE LOOP

Press the BOUNCE LOOP mode button to set the PADs to Loop Roll mode.

#### Pads

Press (and keep down) any of the 4 pads to trigger a momentary **[Loop
Roll](#Good-to-know-for-beginners)** of a different size (in beats) as
per the table.

|             |      |     |     |    |
| ----------- | ---- | --- | --- | -- |
|             | Pads |     |     |    |
| :::         | 1    | 2   | 3   | 4  |
| Press       | 1/8  | 1/4 | 1/2 | 1  |
| SHIFT+Press | 2    | 4   | 8   | 16 |

Once the PAD is released the track will continue to play from the
position it would have been if the Loop Roll was never triggered. The
size of the applied Loop Roll can be adjusted with the **[LOOP
SIZE](#LOOP-SIZE)** encoder as well. Pads change the "selected loop
size" introduced in **[LOOP SIZE](#LOOP-SIZE)** and **[LOOP](#LOOP)**
sections.

### Instant FX mode

#### Instant FX

  - **Press** this button to set the PADs to Effects mode.
  - **Spinback:** Hold **[SHIFT](#shift)** down and then press this
    button down in order to stop the track with a backward brake
    effect.If the **[Instant FX](#Instant-fx)** button is released
    before the track has completely stopped, the track is then played
    back to its regular speed, in the forward direction.
  - **Brake :** see **[JUMP](#jump)** button usage

#### Pads

### Sampler mode

#### SAMPLER

#### Pads
