# Hercules DJ Console 4-Mx

![](http://ecx.images-amazon.com/images/I/81mADkcz9wL._SL1500_.jpg)

  - [Manufacturer's product
    page](http://www.hercules.com/us/DJ-Music/bdd/p/141/dj-console-4-mx/)

The Hercules DJ Console 4-Mx is a USB MIDI controller with a built in
sound card. It is very similar to the [Hercules DJ Console
RMX](Hercules%20DJ%20Console%20RMX), but with switches for 4 decks

## Audio

The sound card has 4 inputs and 4 outputs (2 stereo in/out). The inputs
are switchable between line-in and phono, and also is possible to select
different line levels (consumer -10dBV, Pro +4dBu and boost +8dBu ), so
you can connect both cd-players and turntables on the inputs.

  - Inputs are RCA.
  - Outputs are RCA or 1/4" TRS balanced.
  - Microphone input is 1/4" TS
  - Headphone jack is 1⁄4" (6.35 mm) TRS stereo

### MAC OS / Windows

Drivers for MAC OS X and Windows can be found on [Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=263&cid=1).
Same package for both Audio and MIDI. On Windows, the newest drivers
support Windows 10.

### Mapping configuration in Mixxx 2.0

#### Master / Global controls

<table>
<thead>
<tr class="header">
<th>Control</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Cross-Fader</td>
<td>Fades between left and right decks</td>
</tr>
<tr class="even">
<td>Vol. Main</td>
<td>Controls the Master volume knob of Mixxx.</td>
</tr>
<tr class="odd">
<td>Scratch</td>
<td>Toggles scratch mode. When scratch mode is enabled, pressing a jog wheel controls scratching</td>
</tr>
<tr class="even">
<td>Auto</td>
<td>Enable AutoDJ or fade to next song if AutoDJ is already enabled.<br />
In the future this could do autofading in live mode too</td>
</tr>
<tr class="odd">
<td>Folders / Files</td>
<td>Switches between browsing the sidebar in the library, or the list.<br />
If Folders is pressed twice, opens/closes the tree branch<br />
If Files is pressed when in AutoDJ mode, the next song in the Auto DJ cue is skipped</td>
</tr>
<tr class="even">
<td>Up / Down</td>
<td>Moves up and down in the library track list.<br />
If held down and a jog wheel is moved, then the jog wheel takes over the cursor movement until the up/down button is released</td>
</tr>
<tr class="odd">
<td>Cue/Mix</td>
<td>Control mix of master and PFL (cue) output in headphones</td>
</tr>
<tr class="even">
<td>Mic On/Off</td>
<td>Enables or disables the microphone.<br />
This is configured by default to be mixed in hardware. The controller's driver allows to change this to use it as an input channel</td>
</tr>
</tbody>
</table>

Note: The Microphone volume and the Headphone volume controls are
hardware controls (i.e. they don't control Mixxx's interface)

#### Deck / Channel specific controls

<table>
<thead>
<tr class="header">
<th>Control</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Play/Pause</td>
<td>Play track if paused; pause if track is playing</td>
</tr>
<tr class="even">
<td>Stop</td>
<td>Stops a currently playing track and moves to the beginning.<br />
If in AutoDJ mode, pressing this button on decks 1 &amp; 2 will disable AutoDJ</td>
</tr>
<tr class="odd">
<td>Cue</td>
<td>Depends on cue mode set in Mixxx preferences</td>
</tr>
<tr class="even">
<td>Jog wheel</td>
<td>Seeks forwards and backwards in a stopped track<br />
Temporarily changes the playback speed for playing tracks<br />
Scratches when pressed and scratch mode is on (whether or not track is playing)<br />
Moves up / down in the tracklist if either Up or Down are held down</td>
</tr>
<tr class="odd">
<td>Forward / Backward</td>
<td>Seeks at high speed in a track. In the future this might skip 4 beats at a time instead of simply seeking.</td>
</tr>
<tr class="even">
<td>Pitch fader</td>
<td>Adjusts playback speed (range and direction can be adjusted in Mixxx preferences)</td>
</tr>
<tr class="odd">
<td>Pitch bend +/-</td>
<td>Adjusts playback speed temporarily (range can be adjusted in Mixxx preferences)</td>
</tr>
<tr class="even">
<td>Pitch Scale +/-</td>
<td>These controls have a different meaning in Mixxx. They have been mapped to changing the musical key</td>
</tr>
<tr class="odd">
<td>Pitch Reset</td>
<td>This is triggered when both pitch scale buttons are pressed at the same time. This control has a different meaning in Mixxx. It resets the musical key to the track's default</td>
</tr>
<tr class="even">
<td>Sync</td>
<td>Automatically sets pitch so the BPM of the other deck is matched. Also, when playing, it flashes to the following the rythm</td>
</tr>
<tr class="odd">
<td>Deck A/C, B/D</td>
<td>Switches the deck to control Deck A/C or Deck B/D. Lights are changed accordingly</td>
</tr>
<tr class="even">
<td>Shift key</td>
<td>Switches between the first or second group of 6 effect controls<br />
When it is lit, the 6 fx buttons do the actions defined below as keypad 7 to 13. Else they do the actions defined as keypad 1 to 6<br />
This button has an additional function in Mixxx. If you keep the button pressed while pressing another of the fx buttons, it will trigger the shift-pressed action described for that button</td>
</tr>
<tr class="odd">
<td>Keypad 1 to 4</td>
<td>Set/Unset a beatloop of 0.5, 1, 2 and 4 beats. They act like the corresponding buttons in Mixxx.<br />
If Shift-pressed, buttons 1 and 2 use a beatloop size of 0.125 and 0.25, and buttons 3 and 4 act as loop end/reloop button.<br />
When a loop is set that isn't one of these four main cases, buttons 3 and 4 will be lit to indicate a loop is present</td>
</tr>
<tr class="even">
<td>Keypad 5 to 6</td>
<td>Reveses playback direction when held down. keypad 6 does it with audio roll (censor-like)</td>
</tr>
<tr class="odd">
<td>Keypad 7 to 10</td>
<td>Set/Unset the hotcues 1 to 4<br />
If Shift-pressed, the corresponding hotcue is cleared</td>
</tr>
<tr class="even">
<td>Keypad 11 to 12</td>
<td>Enables the effect rack 1 and 2 for this specific deck</td>
</tr>
<tr class="odd">
<td>Fx knob</td>
<td>Filter knob (the filter setup in the equalizer preferences)<br />
When shift is held, the knob will move slowly</td>
</tr>
<tr class="even">
<td>Vol. Deck A/B</td>
<td>Controls a deck's output volume</td>
</tr>
<tr class="odd">
<td>Cue Select Deck</td>
<td>Toggles this deck's output to the monitor (headphones) on and off<br />
When a new track is loaded in a deck, the cue Select of that deck will get activated automatically.</td>
</tr>
<tr class="even">
<td>Load On Deck A/B</td>
<td>Loads the currently selected track in the track list to the respective deck</td>
</tr>
<tr class="odd">
<td>Bass knob</td>
<td>EQ low frequencies</td>
</tr>
<tr class="even">
<td>Medium knob</td>
<td>EQ mid frequencies</td>
</tr>
<tr class="odd">
<td>Treble knob</td>
<td>EQ high frequencies</td>
</tr>
<tr class="even">
<td>Kill (Bass / Medium / Treble)</td>
<td>Toggles frequency band completely off</td>
</tr>
<tr class="odd">
<td>Gain</td>
<td>Controls a deck's gain before the volume fader</td>
</tr>
<tr class="even">
<td>Source 1/2</td>
<td>Toggles the deck to use the input channel 1/2 as its audio source instead of Mixxx's deck</td>
</tr>
</tbody>
</table>
