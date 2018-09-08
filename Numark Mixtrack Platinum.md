# Numark Mixtrack Platinum

[[/media/undefined/mixtrackplatinum_ortho_3000x1875_web.jpg|]]

  - [Manufacturer's product
    page](https://www.numark.com/product/mixtrack-platinum)
  - [Forum
    thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8863)
  - [Download mapping for
    Mixxx 2.1](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8863&p=34041#p34041)
    

The Numark Mixtrack Platinum is a 2 channel (with 4 channel layering)
entry level DJ controller with an integrated sound card. The stand out
feature of the Mixtrack Platinum is the LCD displays integrated into the
jog wheels.

The microphone input on this controller is not available to the computer
through the controller's sound card. It is mixed with the master output
in hardware, so this controller's sound card is not suitable for
broadcasting or recording the inputs. If you want to use the controller
for broadcasting or recording, a separate [USB audio
interface](Hardware%20Compatibility#USB%20Audio%20Interfaces) with a
microphone input is suggested.

## Soundcard

The **master** output of the Mixtrack Platinum maps to channels 1 and 2
of the soundcard and the \*\*headphone \*\* output maps to channels 3
and 4.

## Configuration Options

Configuration options can be set in the mapping. You will need to edit
the values below at the very top of the JavaScript file
`Numark-Mixtrack-Platinum-scripts.js` and save changes. Allowed values
are “true” or “false” unless specified.

  - **EnableWheel:** if true, wheel/vinyl mode will be enabled by
    default (defaults to true)
  - **ShowTimeElapsed:** if true, time elapsed will be show by default
    on the displays, otherwise time remaining will be displayed
    (defaults to true)

## Mapping

[[/media/hardware/mixtrack_platinum_labeled.png|]]

1\. **Browse Knob:** Rotate this knob clockwise to scroll down, counter
clockwise to scroll up. Press the Knob to load tracks into the inactive
deck, expand entries in the library view, and select playlists and
crates.  
**Shift + Turn:** Page down/page up, allows you to scroll by page
instead of by item.  
**Shift + Push:** Focus next library pane, allows you to toggle between
the left and right panes.

2\. **\*Master Gain:** Adjusts the master volume in the software.  
**Note:** This control does not affect the microphone volume which is
summed with the final output of the Master Gain to the Master Output.
Use the Mic Gain knob to control the microphone volume.

3\. **Cue Mix:** Adjusts the software’s audio output to the headphones,
mixing between the cue (PFL) output and the master mix output.

4\. **Cue Gain:** Adjusts the volume for headphone cueing in the
software.  
**Shift+Cue Gain:** adjust the volume of the first 4 sampler banks

5\. **VU Meter:** Monitor the volume levels of the master output and
each channel. When cue/pfl is active on any channel, the meter shows the
levels for each channel. Otherwise the meter shows the levels of the
master outpt.

6\. **Load:** Press one of these buttons while a track is selected in
the library window to assign it to Deck 1 and 2 (or 3 and 4),
respectively, in the software.  
7\. **Gain Knobs:** Adjust the gain of the deck.  
**Shift + Gain:** Adjust parameter 2 of the currently focused effect on
this deck.

8\. **High EQ Knobs:** Adjust the volume of the high frequencies of the
deck.  
**Shift + High:** Adjust parameter 3 of the currently focused effect on
this deck.

9\. **Mid EQ Knobs:** Adjust the volume of the mid frequencies of the
deck.  
**Shift + Mid:** Adjust parameter 3 of the currently focused effect on
this deck.

10\. **Low EQ Knobs:** Adjust the volume of the low frequencies of the
deck.  
**Shift + Low:** Adjust parameter 3 of the currently focused effect on
this deck.

11\. **Filter:** Adjusts the amount of the filter effect. Turning the
knob left controls the low pass filter; turning it right controls the
high pass filter. The effect applied here can be configured (the Quick
Effect option in the Equalizer preferences).  
**Shift + Filter:** Adjust parameter 1 of the currently focused effect
on this deck.

12\. **Cue/PFL/Headphones:** Sends pre-fader audio to the headphone
output. If any channels have the cue button active, the VU meter will
show channel output levels instead of master output levels on all decks.

13\. **Volume fader:** Adjusts the volume of the deck.

14\. **Crossfader:** Controls the blend between the two decks.

15-16. **Pitch Bend Down/Up:** Press and hold to momentarily reduce the
speed of the track.

17\. **Pitch Fader:** Adjust the speed of the music (activate keylock to
adjust tempo without affecting pitch). Note that moving the fader down
*increases* speed, as marked by the "+" at the bottom of the fader on
the controller. This can be reversed in Mixxx's preferences under
Interface \> Speed slider direction.

18\. **Touch Strip:** Use the Touch Strip to adjust the deck’s Effect
Unit Superknob. When an effect is focused, the touch strip controls that
effect's meta knob.  
**Shift + Touch Strip:** search through a track’s timeline

19\. **Beats Knob:** Adjusts the Dry/Wet mix of the deck’s Effect Unit.

20\. **FX 1 On/Off:** Toggle FX 1 of the deck’s Effect Unit  
**Shift + FX 1:** Cycle to the next effect.  
**Hold + FX 1:** Enable this effect in instant mode, after the button is
released the effect will be disabled again.  
**Tap + FX 1:** Focus this effect to allow adjusting it's parameters.

21\. **FX 2 On/Off:** Toggle FX 2 of the deck’s Effect Unit  
**Shift + FX 2:** Cycle to the next effect.  
**Hold + FX 2:** Enable this effect in instant mode, after the button is
released the effect will be disabled again.  
**Tap + FX 2:** Focus this effect to allow adjusting it's parameters.

22\. **FX 3 On/Off:** Toggle FX 3 of the deck’s Effect Unit  
**Shift + FX 3:** Cycle to the next effect.  
**Hold + FX 3:** Enable this effect in instant mode, after the button is
released the effect will be disabled again.  
**Tap + FX 3:** Focus this effect to allow adjusting it's parameters.

23\. **Tap BPM:** Press this button several times on beat to manually
enter a new BPM. The software will ignore the track's BPM and follow
your manually entered tempo.  
24\. **Wheel button:** If active you can use the platter/jog wheel to
grab and move the audio, scratching the track like a vinyl record.  
**Shift + Wheel:** Toggle elapsed time or time remaining on the deck's
display.

25\. **Platter/Jog Wheel:** If Wheel is enabled, touching the platter
will result in vinyl scratching, when disabled, nothing will happen and
the entire jog wheel behaves as if the side was touched.  
**Touch side:** Pitch bend (nudging) if track is playing  
**Wheel On + Touch platter:** scratching: touch the platter and move
it  
**Shift + Touch platter:** Quickly scroll through the track  
**Shift + Touch side:** Beat jump  
26\. **Jog Wheel Display:** The display is fully functional with this
mapping. It will display the position of the spinner, play position,
bpm, and keylock status.

27\. **Deck Switch:** Allows switching between decks 1/3 and 2/4.

28\. **Shift:** Allows alternate options to be activated for various
controls.

29\. **Sync:** Set the BPM of this deck to match the opposite deck.
**Press:** Press once to synchronize the tempo (BPM) to that of to that
of the other track  
**Long Press:** Enable master sync. Press again to disable.  
**Shift + Sync:** Toggle quantize mode.

30\. **Cue (Transport Control):** Behavior depends on the [cue
mode](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
set in the Mixxx preferences.  
**Shift + Cue:** return the play head to the start of the track.

31\. **Play/Pause:** Starts and stops playback.  
**Shift + Play/Pause:** stutter the track from the last set cue point.
If a cue point has not been set, the play head will return to the start
of the track.

32\. **Pad Mode:** Hold this button to see the currently selected pad
mode, while holding select between Manual Loop, Auto Loop, and Sampler
modes.

33\. **Performance Pads:**

The top row of pads is for controlling loops and samples. To select a
mode, hold down the Pad Mode button and press one of the upper pads. An
LED under the pad section indicates the currently selected mode. See the
subsections below for details about each mode.

The bottom row of pads is used to trigger hotcue points. If a hotcue
point has not already been set for the loaded track, this control will
mark the hotcue point. If a hotcue point has already been set, this
control will jump to it.  
**Shift + Hot Cue**: Deletes the assigned hotcue point

#### Manual Loop Mode

Hold Pad Mode and press the pad marked Manual Loop (silkscreened above
the pad) to assign the upper 4 pads to the functions listed below:  

  - **Loop In** – Sets the beginning of a loop: When assigned, the Pad
    LED will light blue  
  - **Loop Out** – Sets the end point for the loop: When assigned, the
    Pad LED will light blue  
  - **On/Off** – (De)activate the loop. If a loop has not been set, this
    button will have no effect.: When assigned, the Pad LED will light
    blue  
  - **Loop x1/2** – Halve the length of the loop. Press Shift + Loop
    x1/2 to double the length of the loop.

#### Auto Loop Mode

Hold Pad Mode and press the pad marked Auto Loop to assign the upper 4
pads to the functions listed below:  
\* **Auto 1:** – Sets and starts playback of a 1-beat autoloop.  

  - **Auto 2:** – Sets and starts playback of a 2-beat autoloop.  
  - **Auto 3:** – Sets and starts playback of a 4-beat autoloop.  
  - **Auto 4:** – Sets and starts playback of a 8-beat autoloop.  
    \* **Shift + Auto 1:** – Sets and starts playback of a 1/16-beat
    autoloop.  
  - **Shift + Auto 2:** – Sets and starts playback of a 1/8-beat
    autoloop.  
  - **Shift + Auto 3:** – Sets and starts playback of a 1/4-beat
    autoloop.  
  - **Shift + Auto 4:** – Sets and starts playback of a 1/2-beat
    autoloop.  

#### Sample Mode

Hold Pad Mode and press the pad marked Sampler to enter sampler mode. A
press of any of the sample buttons will load a sample if non are loaded.
Shift + sample pad will unload a sample if it is not playing. Pressing a
pad when a sample is loaded will play the sample, pressing shift +
sample pad while a sample is playing will stop it.

Use shift+cue gain to adjust the volume of the sampler.

Note: there are 4 sample slots for the entire controller. The sampler on
each deck controls the same 4 slots.