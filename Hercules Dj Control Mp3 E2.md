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

## Mapping for Mixxx

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
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8</td>
<td>Arrow up/down</td>
<td>Scrolls to the prev/next track in the Playlist/tracktable</td>
</tr>
<tr class="even">
<td>6</td>
<td>Folder</td>
<td>Scrolls up to 10 tracks in the Playlist/tracktable</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Files</td>
<td>Scrolls down to 10 tracks in the Playlist/tracktable</td>
</tr>
<tr class="even">
<td>18</td>
<td>Load A/B</td>
<td>Loads the currently highlighted track into the corrisponding deck (A or B)</td>
</tr>
<tr class="odd">
<td>19</td>
<td>Crossfader</td>
<td>Fades between left and right deck</td>
</tr>
<tr class="even">
<td>7</td>
<td>Scratch</td>
<td>Enable or disable the scratch mode on both decks</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Automix</td>
<td>Used as a master shift button to obtain more controls than those provided by Hercules.<br />
For example: hold down the Automix button and than press the "pitchbend" buttons for adjust the pre-gain amplification</td>
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Pitchbend +/-</td>
<td>Holds the pitch 4% higher while pressed</td>
<td>Adjust the pre-gain amplification</td>
</tr>
<tr class="even">
<td>2</td>
<td>Master Tempo</td>
<td>Toggles a channels flanger effect on and off</td>
<td>Enable key-lock for the specified deck (rate changes only affect tempo, not key)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Pitch knobs</td>
<td>Adjusts playback pitch/speed</td>
<td>Deck A: adjust the headphone volume<br />
Deck B: adjust the cue/main mix in the headphone output</td>
</tr>
<tr class="even">
<td>4</td>
<td>Loop/Fx</td>
<td>Toggle the Loop/Hotcue mode for the keys buttons.<br />
When the button is not lit up the loop buttons are enabled, when the button is lit up the hotcue's buttons are enabled</td>
<td>Nothing</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Equalizer knobs</td>
<td>Adjusts the gain of the low/medium/high equalizer filter</td>
<td>Nothing</td>
</tr>
<tr class="even">
<td>11</td>
<td>1/2/3/4 buttons</td>
<td>Loop mode:<br />
1 - Sets the loop-in position to the current play position.<br />
2 - Sets the loop-out position to the current play position.<br />
3 and 4 - Toggles the current loop On or Off.<br />
Hotcue mode:<br />
1, 2, 3 and 4: If hotcue X is set, seeks the player to hotcue X's position. If hotcue X is not set, sets hotcue X to the current play position.</td>
<td>Loop mode:<br />
Clears the loop-in/out sets.<br />
Hotcue mode:<br />
If hotcue X is set, clears its hotcue status.</td>
</tr>
<tr class="odd">
<td>12</td>
<td>Forward \ Backward</td>
<td>Fast forward/backward</td>
<td>Nothing</td>
</tr>
<tr class="even">
<td>13</td>
<td>Sync</td>
<td>Automatically sets pitch so the BPM of the other deck is matched</td>
<td>Nothing</td>
</tr>
<tr class="odd">
<td>14</td>
<td>Play</td>
<td>Starts or stop a loaded track</td>
<td>Nothing</td>
</tr>
<tr class="even">
<td>15</td>
<td>Cue</td>
<td>Sets the cue point if a track is stoped and not at the current cue point<br />
Stops track and returns to the current cue point if a track is playing.<br />
Plays preview if a track is stopped at the cue point for as long as it's held down</td>
<td>Nothing</td>
</tr>
<tr class="odd">
<td>16</td>
<td>Jog wheel</td>
<td>Seeks forwards and backwards in a stopped track.<br />
Temporarily changes the playback speed for playing tracks</td>
<td>Absolute sync of the track speed to the jog wheel if the scratch mode is enabled</td>
</tr>
<tr class="even">
<td>17</td>
<td>Deck volume slider</td>
<td>Controls the deck output volume</td>
<td>Nothing</td>
</tr>
<tr class="odd">
<td>20</td>
<td>Headphone monitor</td>
<td>Toggles this deck output to the headphones monitor on/off</td>
<td>Nothing</td>
</tr>
</tbody>
</table>
