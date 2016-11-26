# Hercules DJ Console 4-Mx

![](http://ecx.images-amazon.com/images/I/81mADkcz9wL._SL1500_.jpg)

  - [Manufacturer's product
    page](http://www.hercules.com/us/DJ-Music/bdd/p/141/dj-console-4-mx/)

The Hercules DJ Console 4-Mx is a USB controller with a built in sound
card. It is very similar to the [Hercules DJ Console
RMX](Hercules%20DJ%20Console%20RMX), but with switches for 4 decks.

The DJ Console 4-Mx is not a USB class compliant MIDI or audio device.
It does not work on Linux. Drivers for Mac OS X and Windows can be found
on the [Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=263&cid=1).

## Audio

The sound card has 4 inputs and 4 outputs (2 stereo in/out). The inputs
are switchable between line-in and phono, and also is possible to select
different line levels (consumer -10dBV, Pro +4dBu and boost +8dBu ), so
you can connect both CD players and turntables on the inputs.

  - Inputs are RCA.
  - Outputs are RCA or 1/4" TRS balanced.
  - Microphone input is 1/4" TS
  - Headphone jack is 1/4" (6.35 mm) TRS stereo

# Mapping

Note: A mapping existed in Mixxx 1.11 which does not work correctly.  
Note2: Those functions marked as (2.1) are implemented in a new mapping
released the 26th of September of 2016.

## Options

There are several options that can be configured for this mapping. You
can edit these by opening the Hercules-DJ-Console-4-Mx-scripts.js file
in a text editor like Notepad, TextEdit, or gEdit and editing the values
at the top of the file.

  - **autoHeadMix**: Indicates if the Headphone/Master mix should
    automatically be set to master when none of the headphone cue
    buttons are activated.
  - **autoHeadcueOnLoad**: Automatically enable the headphone cue select
    (PFL) of the deck when a song is loaded. (Like in virtual-dj)
  - **beatFlashLed**: set which LED, if any, blinks with the beat
  - **useVuMeters**: Simulate vuMeters using the kill and source
    buttons' LEDs. If enabled, shows master VUs, or deck VU depending if
    prefader listen button is enabled or not.
  - **naviScrollSpeed**: KeyRepeat speed for navigating up/down, in
    milliseconds. 100 is a good value. Lower values make it scroll
    faster.
  - **crossfaderScratchCurve**: The controller has two modes to report
    the crossfader position. The default/beatmix curve, and the scratch
    curve. The default curve reports the real position of the control.
    The scratch curve just crossfades on the edges. Setting this setting
    to true, the curve will change to scratch curve when the scratch
    mode is on (scratch button). Setting it to false will not change it,
    so it will use the setting configured in the DJHercules Tray-icon
    configuration.
  - **vinylSpeed**: Playback speed of the virtual vinyl that is being
    scratched. 45.00 and 33.33 are the common speeeds. (Lower number
    equals faster scratch)
  - **sensitivity**: Jog wheel sensitivity. You should configure this
    setting to the same value than in the DJHercules tray icon
    configuration. (Normal means 1/1). If crossfaderScratchCurve is
    true, or the setting is changed while Mixxx is active, this value
    will be detected automatically.
  - **alpha**: alpha value for the scratch filter (start with 1/8
    (0.125) and tune from there)
  - **beta**: beta value for the scratch filter (start with alpha/32 and
    tune from there)
  - **deckButtonMode**: This controls the function of the deck C/deck D
    buttons (changes the setting in the tray-icon configuration, avanced
    tab). deckmode=0 2 Decks only, deckmode=1 2 Decks with deck switch
    button command, deckmode=2 4 decks.
  - **FXbuttonsSetup**: This indicates which mapping for the FX buttons
    should Mixxx use. The possible values are: mixxx21, mixxx20, and
    original (Hercules Manual and the default setup in Virtual DJ 7 LE)

### Master / Global controls

<table>
<thead>
<tr class="header">
<th>Control</th>
<th>Mode</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Cross-Fader</td>
<td></td>
<td>Fades between left and right decks</td>
</tr>
<tr class="even">
<td>Vol. Main</td>
<td></td>
<td>Controls the Master volume knob of Mixxx.</td>
</tr>
<tr class="odd">
<td>Scratch</td>
<td></td>
<td>Toggles scratch mode. When scratch mode is enabled, pressing a jog wheel controls scratching</td>
</tr>
<tr class="even">
<td>Auto</td>
<td></td>
<td>Enable AutoDJ.<br />
Stop decks 1 and 2 to disable it using the controller.</td>
</tr>
<tr class="odd">
<td>Auto</td>
<td>AutoDJ on</td>
<td>Fade to next song.</td>
</tr>
<tr class="even">
<td>Folders / Files</td>
<td></td>
<td>Switches between browsing the sidebar in the library, or the list.<br />
If Folders is pressed twice, opens/closes the tree branch</td>
</tr>
<tr class="odd">
<td>Files</td>
<td>AutoDJ on</td>
<td>The next song in the Auto DJ cue is skipped</td>
</tr>
<tr class="even">
<td>Up / Down</td>
<td></td>
<td>Moves up and down in the library track list.<br />
If held down and any of the jog wheels is moved, then the jog wheel takes over the cursor movement until the up/down button is released</td>
</tr>
<tr class="odd">
<td>Cue/Mix</td>
<td></td>
<td>Control mix of master and PFL (cue) output in headphones</td>
</tr>
<tr class="even">
<td>Mic On/Off</td>
<td></td>
<td>Enables or disables the microphone.<br />
The microphone is always mixed in hardware. The trayicon driver configuration allows to choose between direct mixing, or mix it only when enabled with the button. \\(2.1) It no longer tries to activate Mixxx microphone talkover.</td>
</tr>
</tbody>
</table>

Note: The Microphone volume and the Headphone volume controls are
hardware controls (i.e. they don't control Mixxx's interface)

### Deck / Channel specific controls

<table>
<thead>
<tr class="header">
<th>Control</th>
<th>Mode</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Shift key</td>
<td></td>
<td>When this button is pressed and released, it toggles between keypad functions 1-6 to keypad functions 7-12. When keypad functions 7-12 are active, the shift button is lit orange.</td>
</tr>
<tr class="even">
<td>Shift key</td>
<td>Hold it</td>
<td>This button has an additional functionality in Mixxx: If you keep the button pressed while pressing one of the other buttons that have the "Shift" mode, it triggers that action.</td>
</tr>
<tr class="odd">
<td>Play/Pause</td>
<td></td>
<td>Play track if it is not playing; pause it if track is playing</td>
</tr>
<tr class="even">
<td>Play/Pause</td>
<td>Shift</td>
<td>(2.1) Play backwards. If slip mode is enabled (triangle image in deere skin), it will resume beyond the previous position (i.e. the playback continues muted until the button is released)</td>
</tr>
<tr class="odd">
<td>Stop</td>
<td></td>
<td>Moves the cursor to the beginning, or to the cue point if it is set, and stops playing it, if it was playing.</td>
</tr>
<tr class="even">
<td>Stop</td>
<td>Shift</td>
<td>(2.1) Brake (Slow it down progressively). Releasing it will continue playing, except if it has slowed a lot, in which case it stops.</td>
</tr>
<tr class="odd">
<td>Cue</td>
<td></td>
<td>Depends on the cue mode set in Mixxx preferences</td>
</tr>
<tr class="even">
<td>Jog wheel</td>
<td></td>
<td>Seeks forwards and backwards in a stopped track<br />
Temporarily changes the playback speed for playing tracks</td>
</tr>
<tr class="odd">
<td>Jog wheel</td>
<td>Scratch on and jog pressed</td>
<td>If Scratch is on and the jog is pressed, moving it will do a scratch effect</td>
</tr>
<tr class="even">
<td>Jog wheel</td>
<td>Up/Down presssed</td>
<td>Moves up / down in the tracklist if either Up or Down are held down</td>
</tr>
<tr class="odd">
<td>Jog wheel</td>
<td>LED</td>
<td>If the beatflash led has been set to jogwheel in the JavaScript file, the light of this button will be flashing following the beats of the song.</td>
</tr>
<tr class="even">
<td>Forward / Backward</td>
<td></td>
<td>(2.0) Seeks at high speed.</td>
</tr>
<tr class="odd">
<td>Forward / Backward</td>
<td></td>
<td>(2.1) Seeks forward or backward in the track in steps of 4 beats (when the beatgrid has already been detected).</td>
</tr>
<tr class="even">
<td>Forward / Backward</td>
<td>Pressed for 500ms</td>
<td>(2.1) seeks at high speed.</td>
</tr>
<tr class="odd">
<td>Forward / Backward</td>
<td>Shift</td>
<td>(2.1) Seeks forward or backward in the track in steps of 1 beats</td>
</tr>
<tr class="even">
<td>Sync</td>
<td></td>
<td>Automatically sets the pitch fader speed to match the BPM of the other deck.</td>
</tr>
<tr class="odd">
<td>Sync</td>
<td>LED</td>
<td>If the beatflash led has been set to Sync in the JavaScript file, the light of this button will be flashing following the beats of the song.</td>
</tr>
<tr class="even">
<td>Sync</td>
<td>Pressed for 500ms</td>
<td>(2.1) Activates master sync for this deck.</td>
</tr>
<tr class="odd">
<td>Sync</td>
<td>Shift</td>
<td>(2.1) Activates the beatgrid edit mode</td>
</tr>
<tr class="even">
<td>Sync</td>
<td>Beatgrid edit mode</td>
<td>(2.1) When the track is stopped, aligns the beatgrid with the current playback position. If playing, synchronizes the beatgrid to align with that of the other playing track.</td>
</tr>
<tr class="odd">
<td>Pitch fader</td>
<td></td>
<td>Adjusts playback speed (range and direction can be adjusted in Mixxx preferences)</td>
</tr>
<tr class="even">
<td>Pitch bend +/-</td>
<td></td>
<td>Adjusts playback speed temporarily (range can be adjusted in Mixxx preferences)</td>
</tr>
<tr class="odd">
<td>Pitch bend +/-</td>
<td>Beatgrid edit mode</td>
<td>(2.1) Increases or decreases the BPM of the track (the detected one).</td>
</tr>
<tr class="even">
<td>Pitch Scale +/-</td>
<td></td>
<td>These controls have a different meaning in Mixxx: They have been mapped to change the musical key</td>
</tr>
<tr class="odd">
<td>Pitch Scale +/-</td>
<td>Beatgrid edit mode</td>
<td>(2.1) Move the beatgrid to the left or to the right</td>
</tr>
<tr class="even">
<td>Pitch Scale -</td>
<td>Shift</td>
<td>(2.1) Activates or deactivates the (musical) keylock mode</td>
</tr>
<tr class="odd">
<td>Pitch Scale +</td>
<td>Shift</td>
<td>(2.1) Activates or deactivates the quantize (to beat) mode</td>
</tr>
<tr class="even">
<td>Pitch Reset</td>
<td></td>
<td>This is triggered when both pitch scale buttons are pressed at the same time. This control has a different meaning in Mixxx: It resets the musical key to the track's default.</td>
</tr>
<tr class="odd">
<td>Pitch Reset</td>
<td>LED</td>
<td>This led has a different meaning in Mixxx: If the beatflash led has been set to pitchreset in the JavaScript file, the light of this button will be flashing following the beats of the song.<br />
Else, the led is on if the key lock button is enabled for this deck.</td>
</tr>
<tr class="even">
<td>Deck A/C, B/D</td>
<td></td>
<td>Switches the deck to control between Deck A/C or between Deck B/D. Lights are changed accordingly</td>
</tr>
<tr class="odd">
<td>Vol. Deck</td>
<td></td>
<td>Controls a deck's output volume</td>
</tr>
<tr class="even">
<td>Cue Select Deck</td>
<td></td>
<td>Toggles on and off this deck's output to the monitor/prefader listen (headphones)<br />
By default, it is configured in the JavaScript to activate it automatically when a new track is loaded in the deck.</td>
</tr>
<tr class="odd">
<td>Load On Left/Right Deck</td>
<td></td>
<td>Loads the currently selected track in the track list to the corresponding deck</td>
</tr>
<tr class="even">
<td>Bass knob</td>
<td></td>
<td>EQ low frequencies</td>
</tr>
<tr class="odd">
<td>Medium knob</td>
<td></td>
<td>EQ mid frequencies</td>
</tr>
<tr class="even">
<td>Treble knob</td>
<td></td>
<td>EQ high frequencies</td>
</tr>
<tr class="odd">
<td>Gain</td>
<td></td>
<td>Controls a deck's gain before the volume fader</td>
</tr>
<tr class="even">
<td>Kill (Bass/ Medium/ Treble)</td>
<td></td>
<td>Toggles that frequency band completely off</td>
</tr>
<tr class="odd">
<td>Kill (Bass/ Medium/ Treble)</td>
<td>LED</td>
<td>(2.1) If the useVuMeters option is activated in the JavaScript file, these LEDs will simulate a VU meter of the master or the deck (if prefader-listen is on).<br />
They will flicker if the sound clips.<br />
If EQ kill is enabled, the vumeter is temporarily disabled</td>
</tr>
<tr class="even">
<td>Source 1/2</td>
<td></td>
<td>Toggles the deck to use the input channel 1/2 as its audio source instead of Mixxx's deck. Concretely, it activates vinyl passthrough mode.</td>
</tr>
<tr class="odd">
<td>Source 1/2</td>
<td>LED</td>
<td>(2.1) If the vumeter is activated in the JavaScript file, they will show a vumeter of the master or the deck (if prefader-listen is on). If kill is enabled, the vumeter is temporarily disabled</td>
</tr>
<tr class="even">
<td>Keypad 1 to 4</td>
<td></td>
<td>(2.0) Set/Unset a beatloop of 0.5, 1, 2 or 4 beats. They act like the corresponding buttons in Mixxx.<br />
When a loop is set that isn't one of these four main cases, buttons 3 and 4 will light to indicate a loop is present</td>
</tr>
<tr class="odd">
<td>Keypad 1 to 4</td>
<td>Shift</td>
<td>(2.0) Set/Unset a beatloop. buttons 1 and 2 use a beatloop size of 0.125 and 0.25, and buttons 3 and 4 act as loop end/reloop button.</td>
</tr>
<tr class="even">
<td>Keypad 5 to 6</td>
<td></td>
<td>(2.0) Reveses playback direction when held down. keypad 6 does it with audio roll (censor-like)</td>
</tr>
<tr class="odd">
<td>Keypad 7 to 10</td>
<td></td>
<td>(2.0) Set/Unset the hotcues 1 to 4</td>
</tr>
<tr class="even">
<td>Keypad 7 to 10</td>
<td>Shift</td>
<td>(2.0) The corresponding hotcue is cleared</td>
</tr>
<tr class="odd">
<td>Keypad 11 to 12</td>
<td></td>
<td>(2.0) Enables the effect rack 1 and 2 for this specific deck</td>
</tr>
<tr class="even">
<td>Keypad 1</td>
<td></td>
<td>(2.1) Sets the loop begin and Activates the loop edit mode</td>
</tr>
<tr class="odd">
<td>Keypad 1</td>
<td>Shift</td>
<td>(2.1) Same as click, but it will be a rolling loop (slip mode)</td>
</tr>
<tr class="even">
<td>Keypad 1</td>
<td>Loop edit mode</td>
<td>(2.1) Exits the loop edit mode</td>
</tr>
<tr class="odd">
<td>Keypad 1</td>
<td>Loop active</td>
<td>(2.1) Disable the loop</td>
</tr>
<tr class="even">
<td>Keypad 1</td>
<td>LED</td>
<td>(2.1) The led is on if the loop is active</td>
</tr>
<tr class="odd">
<td>Keypad 2</td>
<td></td>
<td>(2.1) Reloop (Enable or disable the previously existing loop)</td>
</tr>
<tr class="even">
<td>Keypad 2</td>
<td>Loop edit mode</td>
<td>(2.1) Sets the loopend and exits the loop edit mode</td>
</tr>
<tr class="odd">
<td>Keypad 2</td>
<td>LED</td>
<td>(2.1) The led is on if a loop exists</td>
</tr>
<tr class="even">
<td>Keypad 3 to 4</td>
<td></td>
<td>(2.1) Sets a loop of 4 or 16 beats.</td>
</tr>
<tr class="odd">
<td>Keypad 3 to 4</td>
<td>Shift</td>
<td>(2.1) Same as click, but it will be a rolling loop (slip mode)</td>
</tr>
<tr class="even">
<td>Keypad 3 to 4</td>
<td>LED</td>
<td>(2.1) If a beatloop of 1 or 4 beats is enabled.</td>
</tr>
<tr class="odd">
<td>Keypad 5 to 6</td>
<td></td>
<td>(2.1) starts or stops a sampler 1 or 2 (buttons on the left deck), or the sampler 3 or 4 (buttons on the right deck)</td>
</tr>
<tr class="even">
<td>Keypad 3 to 6</td>
<td>Loop edit mode</td>
<td>(2.1) Sets a beatloop of 2, 8, 16 or 32 beats</td>
</tr>
<tr class="odd">
<td>Keypad 7 to 10</td>
<td></td>
<td>(2.1) Set/Unset the hotcues 1 to 4</td>
</tr>
<tr class="even">
<td>Keypad 7 to 10</td>
<td>Shift</td>
<td>(2.1) The corresponding hotcue is cleared</td>
</tr>
<tr class="odd">
<td>Keypad 11 to 12</td>
<td></td>
<td>(2.1) Enables the effect rack 1 or 2 for this specific deck</td>
</tr>
<tr class="even">
<td>Fx knob</td>
<td></td>
<td>Filter knob (the Quick Effect set in the equalizer preferences)</td>
</tr>
<tr class="odd">
<td>Fx knob</td>
<td>Shift</td>
<td>Move the filter knob slowly (the Quick Effect set in the equalizer preferences)</td>
</tr>
<tr class="even">
<td>Fx knob</td>
<td>Beatgrid edit mode</td>
<td>(2.1) Move the beatgrid position</td>
</tr>
<tr class="odd">
<td>Fx knob</td>
<td>Loop edit mode</td>
<td>(2.1) Increase or decrease the loop size</td>
</tr>
<tr class="even">
<td>Fx knob</td>
<td>audio effect pressed</td>
<td>(2.1) If a keypad number is mapped to an audio effect, holding such button and moving the knob changes the "super" knob of that effect</td>
</tr>
<tr class="odd">
<td>Fx knob</td>
<td>pitch Scale +/- pressed</td>
<td>(2.1) Increases or decreases the musical key (it doesn't matter which of the pitch scale numbers is pressed)</td>
</tr>
<tr class="even">
<td>Fx knob</td>
<td>Loop edit mode</td>
<td>(2.1) Move the loop forward or backward in steps of one beat</td>
</tr>
<tr class="odd">
<td>Fx knob</td>
<td>keypad 1 held down</td>
<td>(2.1) Increase or decrease the loop size</td>
</tr>
</tbody>
</table>

Note: (2.1) The actions of the Keypad buttons can be changed from the
JavaScript. There are three preconfigured presets corresponding to
Manual/Virtual DJ LE, Mixxx 2.0 and Mixxx 2.1.
