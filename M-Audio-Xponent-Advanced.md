# M-Audio Xponent (Advanced)

[[/media/hardware/m-audio/xponent/xponent.jpg|]]

This mapping expands on the stock 2.0 mapping by adding advanced
features such as:

  - Lights
  - Samplers
  - Effects
  - Beatgrid manipulation
  - Rolling beatloops
  - Soft-takeover for critical controls

Please refer to the following diagram for control numbers. Note: Items
1-9 refer to connections on the back of the controller.
[[/media/xponent-mapping-2.png|]]

<table>
<thead>
<tr class="header">
<th>Number</th>
<th>Name</th>
<th>Description</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 - 9</td>
<td>Connections (Not pictured)</td>
<td>Audio, power, and USB connections. These are located on the back of the unit.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>10</td>
<td>Touch Sensitivity</td>
<td>Enables or disables "scratch mode". When the button is lit, scratch mode is enabled.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>11</td>
<td>Jog Wheel</td>
<td>When the track is stopped, the jog wheel seeks forward and backward in the corresponding track.<br />
When the track is playing, the jog wheel speeds up or slows down the track.<br />
When scratch mode is enabled, moving the wheel by touching the top surface will scratch, while moving the wheel by touching the outer ring will act as a normal jog-wheel.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>PFL (Pre-fade listen)</td>
<td>Selects which track(s) are heard through the headphone output</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td>Master Output Volume</td>
<td>Controls the volume of the master audio output.<br />
<strong>Note:</strong> This is a hardware control, and changes will not be reflected in the Mixxx UI</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td>Booth Output Volume</td>
<td>Controls the volume of the booth audio output.<br />
<strong>Note:</strong> This is a hardware control, and changes will not be reflected in the Mixxx UI</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>15</td>
<td>Shift</td>
<td>Alters the behavior of certain controls. These will be mentioned in-line.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>16</td>
<td>Trackpad</td>
<td>Acts as a mouse input to the computer. The Midi mode (see #19) is not mapped at this time.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>17</td>
<td>Left Mouse Button</td>
<td>Used in conjunction with the Trackpad (see #16).</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>18</td>
<td>Right Mouse Button</td>
<td>Used in conjunction with the Trackpad (see #16).</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>19</td>
<td>MIDI Mode Button</td>
<td>Changes the Trackpad and mouse buttons (See #16, #17, #18) into an X/Y input and two additional note inputs.<br />
<strong>Note:</strong> These MIDI inputs are not used in this mapping.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>20</td>
<td>Channel Kills</td>
<td>The Gain kill (G), will momentarily silence the track entirely. The High (H), Mid (M) and Low (L) kills will cut that frequency band from the output.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>21</td>
<td>Brake / Play Backwards</td>
<td>The Big X button is tied to the Brake effect. Releasing the brake before the track has stopped will resume playing, while holding it until the track has stopped completely will leave the track paused.<br />
The Big Minus button momentarily plays the corresponding track backwards. Normal play will resume when it is released</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>22</td>
<td>Gain / EQ</td>
<td>The top knob controls the gain for that deck, while the lower three control the High, Mid, and Low EQ channels. All are soft-takeover enabled.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>23</td>
<td>VU Meters</td>
<td>Displays the current output level for the corresponding deck.<br />
<strong>Note:</strong> This behavior can be switched to behave as a master-out meter instead by setting the value of MaudioXponent.vuMeterMode to 1 in the M-Audio-Xponent-Advanced-scripts.js file</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>24 / 25</td>
<td>Samplers / Effects</td>
<td>The four knobs and buttons below each jogwheel perform different functions.<br />
<br />
The left-hand side controls the samplers, with the knobs controlling the volume, and the buttons firing off the samples.<br />
<br />
The right-hand side controls effects. Pressing one of the buttons will give the corresponding effect (1-4) the "focus", and light up accordingly. Once an effect has the focus, pressing the button again will toggle it on and off. The knobs will control the parameters of the effect that currently has the focus. The first three knobs will control the first three parameters for that effect. The fourth knob will always control the wet/dry mix. Any additional effect parameters beyond three will have to be controlled from the Mixx UI.<br />
<br />
<strong>Note:</strong> Due to limitations in the 2.0 release of Mixxx, the parameter knobs cannot perform a soft-takeover, so be aware of this if you are using multiple effects. This is expected to change in 2.1</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>26</td>
<td>Nudge</td>
<td>Temporarily speeds up or slows down the corresponding track. These buttons are mapped "backwards" with respect to the Mixxx UI. The "&lt;" button "nudges" the track to the left (looking at the waveform displays), while "&gt;" slows the track down, "nudging" it to the right.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>27</td>
<td>PFL Mix</td>
<td>Controls the headphone mix. All the way to the left sends only the track(s) selected by the PFL buttons (see #12) to the headphones. All the way to the right sends only the main output to the headphones</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>28</td>
<td>Headphone Volume</td>
<td>Controls the volume of the headphones.<br />
<strong>Note:</strong> This is a hardware control, and changes will not be reflected in the Mixxx UI.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>29</td>
<td>Progress meter</td>
<td>Indicates the progress through the corresponding track. At thirty seconds from the end of the track, the progress meter will flash to indicate that the end of the track is approaching.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>30</td>
<td>Seek</td>
<td>Fast-forward and fast-rewind.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>31</td>
<td>Loops and Beatgrid manipulation</td>
<td>The numbered buttons set or activate hotcues. Holding shift while pressing a hotcue button clears that hotcue.<br />
<br />
The</td>
<td>&lt; and &gt;</td>
<td>buttons shift the beatgrid left or right and can be used to make minor corrections on the fly. Holding shift while pressing either button will align the beatgrid to the current position.<br />
<br />
The lock button toggles Keylock on and off for that deck. Holding shift while pressing it toggles Quantize on and off for that deck.<br />
<br />
The + and - buttons increase or decrease the speed of the corresponding track.</td>
</tr>
<tr class="odd">
<td>32</td>
<td>Rate Slider</td>
<td>Affects the speed of the corresponding track. Soft-takeover is enabled for this control, so if you don't typically use the sliders, you can safely "stow" them at either extreme and then reset the track speed using the Mixxx UI.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>33</td>
<td>Channel Volume</td>
<td>Normal function, but with soft-takeover enabled.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>34</td>
<td>Sync</td>
<td>Normal function. Flashes on each beat of the corresponding track.<br />
<br />
<strong>Note:</strong> The flashing behavior can be customized by setting the MaudioXponent.syncFlashMode value in the M-Audio-Xponent-Advanced-scripts.js file. 0=No flash, 1=Simple flash, 2=Toggle flash. In Toggle mode, the button will toggle between lit and unlit with each beat.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>35</td>
<td>Cue</td>
<td>Normal function.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>36</td>
<td>Loops</td>
<td>The 1, 2, 4, and 8 buttons behave as normal, starting a loop of X beats at the current position. Pressing them again while looping will disable that loop. Holding shift while pressing them will do a rolling beat loop of 1, 1/2, 1/4, or 1/8th beats, continuing where the song would have been without the loop when they are released.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>37</td>
<td>Play/Pause</td>
<td>Normal function.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>38</td>
<td>Punch-In</td>
<td>Momentarily pulls the cross-fader to the center position while pressed. This only works when the cross-fader is far enough toward the opposite deck, and can be used to momentarily "punch-in" audio from the other deck.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>39</td>
<td>Cross-fader</td>
<td>Normal function, but with soft-takeover enabled.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
