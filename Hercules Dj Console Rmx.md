# Hercules DJ Console RMX

The Hercules DJ Console RMX is a USB MIDI controller with a built in
sound card. Both audio and MIDI works in Linux (from kernel \~2.6.27+),
Windows (XP, Vista, 7), and MAC OS X (10.4.11 (Tiger)/ 10.5.x (Leopard)/
10.6.x (Snow Leopard) 32-bit)

## Audio

The sound card has 4 inputs and 4 outputs (2 stereo in/out). The inputs
are switchable between line-in and phono, so you can connect both
cd-players and turntables on the inputs. The inputs require a high input
signal (\~10mV+) for turntables if you want to record audio or mix it to
the output. Time-coded vinyls, for Vinyl Control, should work ok with
lower input signal.

### Linux

The audio device on the RMX is USB-audio class compliant and works well
with the ordinary ALSA [USB-audio
driver](http://www.alsa-project.org/main/index.php/Matrix:Module-usb-audio).
This should work out of the box on most distributions.

### MAC OS / Windows

Drivers for MAC OS X and Windows can be found on [Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=215&cid=1).
Same package for both Audio and MIDI.

## MIDI

The midi device on the RMX is NOT USB-midi class compliant. For that
reason it requires specific drivers to be working on each OS.

### Linux

Hercules has released a common MIDI-driver for their DJ controllers.
Read more on the page for [Hercules Linux kernel
module](Hercules%20Linux%20kernel%20module)

### MAC OS / Windows

Drivers for MAC OS X and Windows can be found on [Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=215&cid=1).
Same package for both Audio and MIDI.

## MIDI Mappings

### Hercules DJ Console RMX

#### Global controls

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
<td>Fades between left and right deck</td>
</tr>
<tr class="even">
<td>Vol. Main</td>
<td>Controls output volume of your mix</td>
</tr>
<tr class="odd">
<td>Balance</td>
<td>Controls balance between left and right audio channel of your mix</td>
</tr>
<tr class="even">
<td>Scratch</td>
<td>Toggles scratch on and off which changes the function of the deck jog wheels<br />
Effect Shift function when held down.Shifts function of each decks Bass, Medium, Treble to control effect parameters</td>
</tr>
<tr class="odd">
<td>Up / Down</td>
<td>Moves up and down in the library track list<br />
When held down changes the jog wheels behaviour to scroll the library list</td>
</tr>
<tr class="even">
<td>Left / Right</td>
<td>Moves up and down between the library sections</td>
</tr>
<tr class="odd">
<td>Monitor</td>
<td>Fades monitor output (headphones) between cue selected tracks output and the main mix</td>
</tr>
</tbody>
</table>

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
<td>Starts playing a loaded track if stopped. If track is currently playing it stops the track</td>
</tr>
<tr class="even">
<td>Stop</td>
<td>Stops a currently playing track and moves to the beginning.</td>
</tr>
<tr class="odd">
<td>Cue</td>
<td>Sets the cue point if a track is stoped and not at the current cue point<br />
Stops track and returns to the current cue point if a track is playing.<br />
Plays preview if a track is stopped at the cue point</td>
</tr>
</tbody>
</table>

### Hercules DJ Console RMX Advanced
