# Numark Mixtrack Pro 3

![http://www.numark.com/images/sized/images/product\_large/MixtrackProIII\_ortho\_web\_1200x750-624x390.jpg](http://www.numark.com/images/sized/images/product_large/MixtrackProIII_ortho_web_1200x750-624x390.jpg)

  - [Manufacturer's product
    page](http://www.numark.com/product/mixtrack-pro-3)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=7286)
  - [Download
    mapping](http://mixxx.org/forums/viewtopic.php?f=7&p=28103#p28103)

The Numark Mixtrack 3 and Numark Mixtrack Pro 3 are the same controller
except that the Pro version has an integrated 4 channel output sound
card and costs $100 more.

## Configuration options

Configuration options can be set in the mapping. You will need to edit
the values below at the very top of the JavaScript file
“Numark-Mixtrack-3-scripts.js” and save changes. Allowed values are
“**true**” or “**false**”

  - **TrackEndWarning**: whether the Wheel button flashes near the end
    of a track
  - **iCutEnabled**: iCut mode simulates a scratch routine with the jog
    wheel. When enabled, hold Shift when the Wheel button is on while
    moving the jog wheel to use iCut. When the jog wheel is turned back,
    the crossfader closes; when the jog wheel is turned forward the
    crossfader will open. As a visual reference, TAP LED and Wheel
    button LED will be ON.
  - **fastSeekEnabled**: Enables fast seek with Jog Wheel platter when
    the Wheel button is on and Shift is held
  - **smartPFL**: When the Load button is used, the Cue/PFL button is
    automatically activated on the deck being loaded and deactivated on
    the other deck
  - **printComments**: Used for debugging, print comments on prompt
    screen
  - **beatlooprollActivate**: Use beatlooproll (slip mode loop) instead
    of beatloop command when using pads in Autoloop mode.
  - **PADLoopButtonPressed**: whether to keep loops active only while a
    pad is held down when the pads are in Autoloop mode
  - **PADSampleButtonPressed**: whether to keep samplers playing only
    while a pad is held down when the pads are in Sample mode
  - **OnBeatActiveFlash**: whether the TAP LED will flash to the beat
    (except when Shift Lock is on)
  - **TapExpandLibrary**: If "true": TAP button will be used to
    expand/contract library view and Shift TAP will trigger TAP
    function; "false" will invert the functionality
  - **Skin**: Specify the Skin used for your installation. This is
    required in order for TapExpandLibrary option to work properly.
    Different code is required for each skin. Accepted values: 1 =
    "Deere" or "Shade"; 2 = "Late Night"; 3 = "Dark Metal" 
  - **BeatKnobAsSamplerVolume**: Use Beat knob to adjust Sampler Volume.
    If "true": Deck 1 adjusts Samplers 1-4; Deck 2 adjusts Samplers 5-8
    and Shift + Beat knob moves beat grid. If false: beat knob will
    adjust beatgrid, shift + knob will adjust grid size

## Mapping

[[/media/numarkmixtrackpro3mapping.gif|]]

#### 1\. Browser Knob

Rotate this knob to cycle through tracks in main library window. Press
the Knob to load selected track into first stopped deck.  
**Shift + Turn:** allows selecting Play Lists and side navigation bar
items.  
**Shift + Push:** opens / closes selected side navigation bar item.

#### 2\. Master Gain

Adjusts the master volume in the software.  
**Note**: This control does not affect the microphone volume which is
summed with the final output of the Master Gain to the Master Output.
Use the Mic Gain knob to control the microphone volume.

#### 3\. Cue Mix

Adjusts the software’s audio output to the headphones, mixing between
the cue output and the master mix output.

#### 4\. Cue Gain

Adjusts the volume for headphone cueing in the software.

#### 5\. Load

Press one of these buttons while a track is selected in the library
window to assign it to Deck 1 and 2, respectively, in the software.  
**Shift + Load:** Activates Fader Start mode for the corresponding (PFL
Button is then blinking). Fader start guide: In fader start mode, not
only you can press the play/pause button to play/pause the track, but if
you move up the level fader (the volume fader if you prefer) of the
deck, the track will be played and if you close it to zero, the track
will be paused.  
**Configurable option:**  
If the [smartPFL option](#configuration-options) is set to true, the
Cue/PFL button is automatically activated on the deck being loaded and
deactivated on the other deck.

#### 6-8 EQ Knobs

Adjust High/Mid/Low frequencies of the deck

#### 9\. Filter

Adjusts the amount of the filter effect. Turning the knob left controls
the low pass filter; turning it right controls the high pass filter.

#### 10\. Cue/PFL/Headphones

Sends pre-fader audio to the headphone output  
**SHIFT + press:** toggle slip mode  
**SHIFT + double press**: toggle quantize mode

#### 11\. Volume fader

Adjusts the volume of the deck

#### 12\. Crossfader

Controls the blend between the two decks

#### 13-14 Pitch Bend Down/Up

Press and hold to momentarily reduce the speed of the track.  
**Shift+Pitch Bend Down/Up:** Jump 1 beat backward/forward

#### 15\. Pitch Fader

Adjust the speed of the music (activate keylock to adjust tempo without
affecting pitch). Note that moving the fader down *increases* speed, as
marked by the "+" at the bottom of the fader on the controller. This can
be reversed in Mixxx's preferences under Interface \> Speed slider
direction

#### 16\. Touch Strip

**Left Strip:** Use the Touch Strip to adjust the Effect Rack 1
Superknob  
**Right Strip:** Use the Touch Strip to adjust the Effect Rack 1 Dry/Wet
mix ratio  
**Shift + Touch Strip:** search through a track’s timeline

#### 17\. Beats Multiplier

Moves the beat grid left (turn counterclockwise) or right (turn
clockwise)  
**Shift + Beats:** adjust beatgrid size **Configurable option:**  
If BeatKnobAsSamplerVolume is set to "true", use Beat knob to adjust
Sampler Volume. Deck 1 beat knob will adjusts Samplers 1-4; Deck 2 knob
will adjusts Samplers 5-8. Shift + Beat knob will move the beat grid.

#### 18-20 FX 1/2/3 On/Off

Assigns selected deck to Effect Rack 1, Unit 1/2/3  
**Shift + FX1/2/3** to select from the list of available effects for the
respective effect unit. Left deck selects the previous effect, right
deck selects the next effect.

#### 21\. Tap BPM

Press this 4 or more times on beat to manually enter a new BPM. The
software will ignore the track's BPM and follow your manually entered
tempo. **Configurable option:**  
If [TapExpandLibrary](#configuration-options) is set to "true", the TAP
button will expand the Library view and Shift TAP will trigger TAP
function

#### 22\. Wheel button

Activate this button to use the platter/jog wheel to grab and move the
audio, scratching the track like a vinyl record.

#### 23\. Platter/Jog Wheel

**Touch side:** Pitch bend if track is playing (Wheel On & Off) / track
positioning (Wheel On)  
**Wheel On + Touch platter:** scratching: touch the platter and move
it  
**Shift + Wheel On + Touch platter**: If iCutEnabled is true, iCut
feature is activated, else normal scratching  
**Wheel Button Off + Touch platter**: No action (Wheel is off\!)  
**Shift + Wheel Off + Touch platter**: if fastSeekEnabled is true, fast
seek is activated (navigate quickly thru track)

#### 24\. Shift

Allows multiple control commands to be triggered when pressed first
along with other buttons  
**Single Press** : Temporary SHIFT  
**Double press** (like a double click): SHIFT Lock enabled (TAP LED will
remain ON if Shift Lock is enabled)  
**Press and release**: toggle off SHIFT Lock if enabled

#### 25\. Pad Mode

This is used to change the [operation mode](#performance-pad-modes) of
the top 4 performance pads. Pressing this button will light the pad
indicating the currently active (Manual Loop, Auto Loop or Sampler)

#### 26\. Sync

Enables BPM syncing between decks.  
**Short Press:** Press once to synchronize the tempo (BPM) to that of to
that of the other track  
**Double Press:** press twice QUICKLY to play the track immediately
synchronized to the tempo (BPM) and to the phase of the other track, if
the track was paused  
**Long Press** (Sync Lock): Hold for at least half of a second to enable
sync lock for this deck. Decks with sync locked will all play at the
same tempo, and decks that also have quantize enabled will always have
their beats lined up. If the Sync Lock was previously activated, it just
deactivates it regardless of the Short press/Double Press  
**Shift + Sync:** Toggle Key Lock

#### 27\. Cue (Transport Control)

Behavior depends on the [cue
mode](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
set in the Mixxx preferences.  
**Shift + Cue:** return the play head to the start of the track.

#### 28\. Play/Pause

Starts and suspends playback. If no track is loaded, loads the selected
track (if any) and play.  
**Shift + Play/Pause:** stutter the track from the last set cue point.
If a cue point has not been set, the play head will return to the start
of the track.

#### 29\. Performance Pads

The top row of pads is for controlling loops and samples. See
[\#Performance Pad Modes](#Performance%20Pad%20Modes) section below for
a detailed description.

The bottom row of pads is used to trigger hotcue points. If a hotcue
point has not already been set for the loaded track, this control will
mark the hotcue point. If a hotcue point has already been set, this
control will jump to it.  
**Shift + Hot Cue**: Deletes the assigned hotcue point

#### 30\. Master Output LEDs

Displays the audio level going to the Master Output.

## Performance Pad Modes

The upper row of pads has different functions depending on their mode:
Manual Loop Mode, Auto Loop Mode, and Sample Mode. To select a mode,
hold down the Pad Mode button and press one of the upper pads. An LED
under the pad section indicates the currently selected Mode.  

### Manual Loop Mode

Hold Pad Mode and press the pad marked Manual Loop (silkscreened above
the pad) to assign the lower 4 pads to the functions listed below:  

  - **Loop In** – Sets the beginning of a loop  
  - **Loop Out** – Sets the end point for the loop  
  - **On/Off** – (De)activate the loop. If a loop has not been set, this
    button will have no effect.  
  - **Loop x1/2** – Halve the length of the loop. Press Shift + Loop
    x1/2 to double the length of the loop.  

### Auto Loop Mode

Hold Pad Mode and press the pad marked Autoloop to assign the lower 4
pads to the functions listed below: When assigned, the respective Pad
LED will blink Yellow  
\* **Auto 1** – Sets and starts playback of a 1/8-beat autoloop.  

  - **Auto 2** – Sets and starts playback of a 1/4-beat autoloop.  
  - **Auto 3** – Sets and starts playback of a 1/2-beat autoloop.  
  - **Auto 4** – Sets and starts playback of a 1-beat autoloop.  
  - **Shift + Auto 1** – Sets and starts playback of a 2-beat
    autoloop.  
  - **Shift + Auto 2** – Sets and starts playback of a 4-beat
    autoloop.  
  - **Shift + Auto 3** – Sets and starts playback of a 8-beat
    autoloop.  
  - **Shift + Auto 4** – Sets and starts playback of a 16-beat
    autoloop.  

**Configuration Option:** If the
[PADLoopButtonPressed](#configuration-options) option is set to true,
the loop will only be active while the pad is held down.

### Sample Mode

Hold Pad Mode and press the pad marked Sampler to assign the lower 4
pads to the functions listed below. When assigned, the respective Pad
LED will blink Purple  
Shift + Sample X will play loaded sample, but with Sampler unit Sync
disabled  

  - **Deck 1 - Sample 1** – Plays the sample assigned to Sample Pad 1
    with the unit Sync activated.  
  - **Deck 1 - Sample 2** – Plays the sample assigned to Sample Pad 2
    with the unit Sync activated.  
  - **Deck 1 - Sample 3** – Plays the sample assigned to Sample Pad 3
    with the unit Sync activated.  
  - **Deck 1 - Sample 4** – Plays the sample assigned to Sample Pad 4
    with the unit Sync activated.  
  - **Deck 2 - Sample 1** – Plays the sample assigned to Sample Pad 5
    with the unit Sync activated.  
  - **Deck 2 - Sample 2** – Plays the sample assigned to Sample Pad 6
    with the unit Sync activated.  
    \* **Deck 2 - Sample 3** – Plays the sample assigned to Sample Pad 7
    with the unit Sync activated.  
    \* **Deck 2 - Sample 4** – Plays the sample assigned to Sample Pad 8
    with the unit Sync activated.  

**Configuration Option:** If the
[PADSampleButtonPressed](#configuration-options) option is set to true,
the sample will only play as long as the pad is held down.
