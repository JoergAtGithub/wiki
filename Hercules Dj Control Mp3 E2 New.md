# Hercules DJ Control MP3 e2

[[/media/16445_.jpg|]]

The Hercules DJ Control MP3 e2 is a USB MIDI controller without a built
in sound card. It is compatible with Mixxx versions 1.8+ herc and later.
It works in Linux 32/64 bits (from kernel \~2.6.27+), Windows (XP,
Vista, 7), and MAC OS X (10.4.11 (Tiger)/ 10.5.x (Leopard)/ 10.6.x (Snow
Leopard) 32-bit)

## MIDI driver

The midi device on the MP3 e2 is NOT USB-midi class compliant. For that
reason it requires specific drivers to be working on each OS.

### MAC OS / Windows

Drivers for MAC OS X and Windows can be found on [Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=61&pid=241&cid=1).

### Linux

Hercules has released a common MIDI-driver for their DJ controllers.
Read more on the page for [Hercules Linux kernel
module](Hercules%20Linux%20kernel%20module)

## USB HID

As of Mixxx v1.11-beta2 this controller is supported through USB HID.
This works without any additional kernel drivers. If the Hercules driver
causes a kernel panic on your linux distribution you can use this
feature.

Enable the controller in Ubuntu by following the steps below:

1.  Remove the hdjmod-dkms driver if installed: `sudo apt-get remove
    hdjmod-dkms`
2.  Add the Mixxx v1.11 repositories (use the mixxxbetas ppa until v1.11
    final is released). `sudo add-apt-repository ppa:mixxx/mixxxbetas
    sudo apt-get update` 
3.  Install Mixxx (remove older version prior to install): `sudo apt-get
    install mixxx`
4.  Plug-in the controller and run mixxx
5.  Go to Preferences, select and enable "Hercules .." device listed
    under Controllers (do not select Midi Through\!)

If the device is still not visible as a separate entry under
"Controllers" you need to modify the device permissions using udev
rules. First create the rule file:

    sudo nano /etc/udev/rules.d/hercules-usb.rules

Add following lines to this file:`SUBSYSTEM=="usb_device",
SYSFS{idVendor}=="06f8", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="06f8", MODE="0666"` Save the
contents and restart udev:`sudo /etc/init.d/udev restart`

Pull out the controller and plug it in again. Run mixxx and select
"Preferences" -\> "Controllers" and you should be able to select and
enable the controller.

## Mapping for Mixxx 1.12+ (by knob/button)

The Hercules MP3 e2 mapping for Mixxx is integrated in Mixxx so you
don't have to download or install nothing.

[[/media/hercules_mappa.png|]]

#### Global controls

<table>
<thead>
<tr class="header">
<th>Number</th>
<th>Control</th>
<th>Function</th>
<th>shifted</th>
<th>Supershifted</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8</td>
<td>Arrow up/down</td>
<td>Up : goes one track down<br />
Down : Microphone TalkOver</td>
<td>Up : Goes one track up<br />
Down : Nothing</td>
<td>Nothing</td>
</tr>
<tr class="even">
<td>6</td>
<td>Folder</td>
<td>Toggles (expands/collapses) the currently selected library sidebar item</td>
<td>Play/Stutter sampler 1/3</td>
<td>Stop sampler 1/3</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Files</td>
<td>Toggles (expands/collapses) the currently selected library sidebar item</td>
<td>Play/Stutter sampler 2/4</td>
<td>Stop sampler 2/4</td>
</tr>
<tr class="even">
<td>18</td>
<td>Load A/B</td>
<td>Loads the currently highlighted track into the corresponding deck (A or B)</td>
<td>Loads the current highlighted track into the corresponding sampler (1 or 2)</td>
<td>Switch deckA between Channel 1 &amp; 3 and deckB between 2 &amp;4</td>
</tr>
<tr class="odd">
<td>19</td>
<td>Crossfader</td>
<td>Fades between left (channel 1 &amp; 3) and right (channel 2 &amp; 4) deck</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>Automix</td>
<td>Used as a master shift button to obtain more controls than those provided by Hercules. Press &amp; Hold automix, then press corresponding button to obtain shifted behavior.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Scratch</td>
<td>Enable or disable the scratch mode on both decks</td>
<td>Used as a master supershift button to obtain a third level of controls. Press &amp; Hold Automix, then press &amp; Hold Scratch, then press corresponding button to obtain supershifted behavior</td>
<td></td>
</tr>
</tbody>
</table>

#### Deck / Channel specific controls

<table>
<thead>
<tr class="header">
<th>Number</th>
<th>Control</th>
<th>Simple function</th>
<th>Shifted function</th>
<th>Supershifted function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Pitchbend +/-</td>
<td>Temporary Holds the pitch 4% higher while pressed</td>
<td>+ double loop<br />
- half loop</td>
<td>+ Filter High Kill<br />
- Filter Low Kill</td>
</tr>
<tr class="even">
<td>2</td>
<td>Master Tempo</td>
<td>Syncs the BPM and phase to that of the other track (if BPM is detected on both).<br />
Led blink: master<br />
Fixed led: follower<br />
Led off: none</td>
<td>Enable key-lock for the specified deck (rate changes only affect tempo, not key)</td>
<td>Magnet</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Pitch knobs</td>
<td>Adjusts playback pitch/speed</td>
<td>Deck A: adjust the headphone volume<br />
Deck B: adjust the cue/main mix in the headphone output</td>
<td>Quick Filter knob</td>
</tr>
<tr class="even">
<td>4</td>
<td>Loop/Fx</td>
<td>Toggle the Loop/Hotcue mode for the keys buttons.<br />
When the button is not lit up the loop buttons are enabled, when the button is lit up the hotcue's buttons are enabled</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Equalizer knobs</td>
<td>Adjusts the gain of the low/medium/high equalizer filter</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>1/2/3/4 buttons</td>
<td>Loop mode:<br />
1 - loop-in<br />
2 - loop-out<br />
3 - Toggles current loop On or Off<br />
4 - Loop 4<br />
<br />
Hotcue mode:<br />
1, 2, 3 and 4: If hotcue X is set, seeks the player to hotcue X's position. If hotcue X is not set, sets hotcue X to the current play position.</td>
<td>Loop mode:<br />
1 - Loop 1/4<br />
2 - Loop 1/2<br />
3 - Loop 1<br />
4 - Loop 2<br />
<br />
Hotcue mode:<br />
If hotcue X is set, clears its hotcue status.</td>
<td>Loop mode:<br />
1 - Clear loop<br />
2 - Loop 1/8<br />
3 - Loop 8<br />
4 - Loop 16<br />
<br />
Hotcue mode:<br />
Nothing</td>
</tr>
<tr class="odd">
<td>12</td>
<td>Forward \ Backward</td>
<td>Fast forward/backward</td>
<td>Adjust pregain</td>
<td></td>
</tr>
<tr class="even">
<td>13</td>
<td>Sync</td>
<td>Automatically sets pitch so the BPM of the other deck is matched</td>
<td>Adjust BeatGrid</td>
<td>Kill Mid</td>
</tr>
<tr class="odd">
<td>14</td>
<td>Play</td>
<td>Starts or stop a loaded track</td>
<td>Backward Play</td>
<td>Repeat</td>
</tr>
<tr class="even">
<td>15</td>
<td>Cue</td>
<td>Sets the cue point if a track is stoped and not at the current cue point<br />
Stops track and returns to the current cue point if a track is playing.<br />
Plays preview if a track is stopped at the cue point for as long as it's held down</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>Jog wheel</td>
<td>Seeks forwards and backwards in a stopped track.<br />
Temporarily changes the playback speed for playing tracks<br />
Absolute sync of the track speed to the jog wheel if the scratch mode is enabled</td>
<td></td>
<td>Deck A: Select prev/next playlist<br />
Deck B: select prev/next track</td>
</tr>
<tr class="even">
<td>17</td>
<td>Deck volume slider</td>
<td>Controls the deck output volume.<br />
There is soft takeover after deck switch (1/3 or 2/4) to prevent wide parameter changes when the on-screen control diverges from the hardware control. Manipulating the control on the hardware will have no effect until the position of the hardware control is close to that of the software, at which point it will take over and operate as usual.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>20</td>
<td>Headphone monitor</td>
<td>Toggles this deck output to the headphones monitor on/off</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
