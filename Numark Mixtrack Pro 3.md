# Numark Mixtrack Pro 3

![http://www.numark.com/images/sized/images/product\_large/MixtrackProIII\_ortho\_web\_1200x750-624x390.jpg](http://www.numark.com/images/sized/images/product_large/MixtrackProIII_ortho_web_1200x750-624x390.jpg)

  - [Manufacturer's product
    page](http://www.numark.com/product/mixtrack-pro-3)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=7286)

The Numark Mixtrack 3 and Numark Mixtrack Pro 3 are the same controller
except that the Pro version has an integrated sound card and costs $100
more.

## Controller Mapping by S.Morin - Version 1, beta 8

found in the following forum post:
<http://mixxx.org/forums/viewtopic.php?f=7&p=27997&sid=0ea9ad1cdef4e0a452f0c17aa113145c#p27991>

[[/media/numarkmixtrackpro3mapping.gif|]]

### Configuration options

-----

Configuration options can be set in the mapping. You will need to edit
the values below at the very top of the JavaScript file
“Numark-Mixtrack-3-scripts.js” and save changes. Allowed values are
“**true**” or “**false**”

**TrackEndWarning**: Default value: true When you reach the end of the
track, the jog wheel Button will flash. If value is "false": there will
be no flash of Jog Wheel Button at the end of the track.

**iCutEnabled**: Default value: true iCut mode simulates a scratch
routine with the jog wheel. When the jog wheel is turned back, the
crossfader closes; when the jog wheel is turned forward the crossfader
will open. Shift needs to be enabled and Wheel button is activated and
you are scratching. As a visual reference, TAP LED and Wheel button LED
will be ON.

**fastSeekEnabled**: Default value: true Enables fast seek with Jog
Wheel platter. This is available only when Wheel is Off and Shift is
enabled.

**smartPFL**: Default value: true When set to true, when the Load button
is used, the Cue channel of the track being loaded is activated and the
other Cue channel is deactivated. Cue channel can be activated directly
with Cue/PFL button.

**printComments**: Default value: true Used for debugging, print
comments on prompt screen

**beatlooprollActivate**: Default value: false Use beatlooproll instead
of beatloop command when using AutoLoop buttons (Performance Pads)

**PADLoopButtonPressed**: Default value: false When "false" is set, loop
will start on press and stop on 2nd press. When "True" is set: Loop
stops when finger release.

**PADSamplerButtonPressed**: Default value: false When "false" is set,
Sampler will start on press and stop on 2nd press. When "True" is set:
Sampler stops when finger release.

**OnBeatActiveFlash**: Default value: true When “true” is set: TAP LED
will flash to the beat if Shift Lock is not enabled

### Mapping

-----

#### 1.Browser Knob:

Rotate this knob to cycle through tracks in main library window. Press
the Knob to load selected track into first stopped deck.  
**Shift + Turn:** allows selecting Play Lists and side navigation bar
items.  
**Shift + Push:** opens / closes selected side navigation bar item.

#### 2.Master Gain:

Adjusts the master volume in the software.  
**Note**: This control does not affect the microphone volume which is
summed with the final output of the Master Gain to the Master Output.
Use the Mic Gain knob to control the microphone volume.

#### 3.Cue Mix:

Adjusts the software’s audio output to the headphones, mixing between
the cue output and the master mix output.

#### 4.Cue Gain:

Adjusts the volume for headphone cueing in the software.

#### 5.Load:

Press one of these buttons while a track is selected in the library
window to assign it to Deck 1 and 2, respectively, in the software.

**Shift + Load:** Activates Fader Start mode for the corresponding (PFL
Button is then blinking). Fader start guide: In fader start mode, not
only you can press the play/pause button to play/pause the track, but if
you move up the level fader (the volume fader if you prefer) of the
deck, the track will be played and if you close it to zero, the track
will be paused.

**Configurable option:** If smartPFL is set to true, the Cue channel of
the track being loaded is activated and the other Cue channel is
deactivated

#### 6.High EQ:

Controls the treble frequencies for the individual channels.

#### 7.Mid EQ:

Controls the mid range frequencies for the individual channels.

#### 8.Low EQ:

Controls the bass frequencies for the individual channels.

#### 9.Filter:

Adjusts the amount of the filter effect. Turning the knob left and right
will produce a Low Pass Filter or High Pass Filter.

#### 10.Cue/PFL:

Sends pre-fader audio to the Cue Channel for headphone monitoring.
**SHIFT + press:** toggle slip mode **SHIFT + double press**: toggle
quantize mode.

#### 11.Channel Volume:

Adjusts the volume of the individual channels in the software.

#### 12.Crossfader:

Controls the blend between the two decks.

#### 13.Pitch Bend Down:

Press and hold to momentarily reduce the speed of the track.

#### 14.Pitch Bend Up

Press and hold to momentarily increase the speed of the track.

#### 15.Pitch Fader:

This controls the speed of the music. Moving towards the "+" will speed
the music up, while moving towards the "–" will slow it down.

#### 16.Touch Strip:

**Left Strip:** Use the Touch Strip to adjust the Effect Rack 1 Super
button. **Right Strip:** Use the Touch Strip to adjust the Effect Rack 1
Dry/Wet mixing ratio **Shift + Touch Strip:** search through a track’s
timeline.

#### 17.Beats Multiplier:

Moves the beat grid left (turn counterclockwise) or right (turn
clockwise) **Shift + Beats:** adjust beatgrid size

#### 18.FX 1 On/Off:

Assigns (On) / removes (Off) selected deck to Effect Rack 1, Unit 1
**Shift + FX1** to select from the list of available effects: Left deck
: select previous effect, Right deck : select next effect

#### 19.FX 2 On/Off:

Assigns (On) / removes (Off) selected deck to Effect Rack 1, Unit 2
**Shift + FX2** to select from the list of available effects. Left deck
: select previous effect, Right deck : select next effect

#### 20.FX 3 On/Off:

Assigns (On) / removes (Off) selected deck to Effect Rack 1, Unit 3
**Shift + FX3** to select from the list of available effects. Left deck
: select previous effect, Right deck : select next effect

#### 21.Tap BPM:

Press this 4 or more times on tempo to manually enter a new BPM. The
software will ignore the track's BPM and follow your manually entered
tempo.

#### 22.Wheel Button:

Activate this button to use the platter/jog wheel to grab and move the
audio, "scratching" the track as you would with a vinyl record.

#### 23.Platter/Jog Wheel:

**Touch side:** Pitch bend / track positioning **Wheel Button On + Touch
platter:** scratching: touch the platter and move it **Shift + Wheel
Button On + Touch platter**: If iCutEnabled is true, iCut feature is
activated, else normal scratching **Wheel Button Off + Touch platter**:
No action mapped currently, pitch bend / track positioning to be mapped
in future release **Shift + Wheel Button Off + Touch platter**: if
fastSeekEnabled is true, fast seek is activated (navigate quickly thru
track).

#### 24.Shift:

Allows multiple control commands to be triggered when pressed first
along with other buttons. **Single Press** : Temporary SHIFT **Double
press** (like a double click) : SHIFT Lock enabled (TAP LED will remain
ON if Shift Lock is enabled) **Press and release** : toggle off SHIFT
Lock if enabled

#### 25.Pad Mode

This is used to change the operation of the top 4 performance pads.
Single press will lit the mode currently active (Manual Loop, Auto Loop
or Sampler)

....work in progress... to be continued
