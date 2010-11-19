# Hercules DJ Control Steel (page under construction)

[[/media/hardware/hercules_dj_control_steel.jpg|]]

The Hercules DJ Control Steel is a USB MIDI controller (very similar to
DJ Console RMX but without a built in sound card). It is compatible with
Mixxx versions 1.6.1+herc and later. It works in Linux 32/64 bits (from
kernel \~2.6.27+), Windows (XP, Vista, 7), and MAC OS X (10.4.11
(Tiger)/ 10.5.x (Leopard)/ 10.6.x (Snow Leopard) 32-bit)

## MIDI driver

The midi device on the Steel is NOT USB-midi class compliant. For that
reason it requires specific drivers to be working on each OS.

### MAC OS / Windows

Drivers for MAC OS X and Windows can be found on [Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=215&cid=1).

### Linux

Hercules has released a common MIDI-driver for their DJ controllers.
Read more on the page for [Hercules Linux kernel
module](Hercules%20Linux%20kernel%20module)

## MIDI Mappings

FIXME

## Mapping for Mixxx

You need to update the mapping with following files : [Link to mapping
files](http://slist.lilotux.net/linux/deejay/mixxx/)
[[/media/hercules_dj_control_steel_top_face.png|]]

### Hercules DJ Control Steel

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
<strong>Effect Shift</strong> when held down:<br />
-Shifts function of each decks Bass, Medium, Treble to control effect parameters</td>
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
<td>Sets the cue point if a track is stopped and not at the current cue point<br />
Stops track and returns to the current cue point if a track is playing.<br />
Plays preview if a track is stopped at the cue point for as long as it's held down</td>
</tr>
<tr class="even">
<td>Jog wheel</td>
<td>Seeks forwards and backwards in a stopped track<br />
Temporarily changes the playback speed for playing tracks<br />
Scratches both stopped and playing tracks when scratch mode is on<br />
Moves up / down in the track list if either Up or Down is held down</td>
</tr>
<tr class="odd">
<td>Forward / Backward</td>
<td>Seeks at high speed in a track</td>
</tr>
<tr class="even">
<td>Load Deck A/B</td>
<td>Loads the currently selected track in the track list to the related deck</td>
</tr>
<tr class="odd">
<td>Cue Select</td>
<td>Toggles this decks output to the monitor (headphones) on and off</td>
</tr>
<tr class="even">
<td>Pitch</td>
<td>Adjusts playback speed +/-10% (can be adjusted in the preferences)</td>
</tr>
<tr class="odd">
<td>Sync</td>
<td>Automatically sets pitch so the BPM of the other deck is matched</td>
</tr>
<tr class="even">
<td>Pitch Bend-</td>
<td>Resets the pitch to the tracks normal playback speed (FIXME)</td>
</tr>
<tr class="odd">
<td>Pitch Bend+</td>
<td>TODO</td>
</tr>
<tr class="even">
<td>Bass</td>
<td>Adjusts the volume of a channels low frequency content (ex. bass drum)<br />
Adjusts flanger period when Effect Shift is held down</td>
</tr>
<tr class="odd">
<td>Medium</td>
<td>Adjusts the volume of a channels mid frequency content (ex. vocals)<br />
Adjusts flanger delay when Effect Shift is held down</td>
</tr>
<tr class="even">
<td>Treble</td>
<td>Adjusts the volume of a channels high frequency content (ex. hi-hats)<br />
Adjusts flanger depth when Effect Shift is held down</td>
</tr>
<tr class="odd">
<td>Kill (Bass / Medium / Treble)</td>
<td>Toggles output of a frequency band on and off</td>
</tr>
<tr class="even">
<td>Gain</td>
<td>Controls a decks input volume</td>
</tr>
<tr class="odd">
<td>Vol. Deck A/B</td>
<td>Controls a decks output volume</td>
</tr>
<tr class="even">
<td>Stop</td>
<td><strong>Deck shift</strong> changes behavior of other controls related to this deck when held down</td>
</tr>
<tr class="odd">
<td>Forward / Backward</td>
<td>Adjusts position of loop in/out and hot cues when a loop / hot cue button is held down</td>
</tr>
<tr class="even">
<td>Bass</td>
<td>Adjusts the volume of a channels low frequency content (ex. bass drum)<br />
Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting<br />
Adjusts flanger period when Scratch is held down</td>
</tr>
<tr class="odd">
<td>Medium</td>
<td>Adjusts the volume of a channels mid frequency content (ex. vocals)<br />
Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting<br />
Adjusts flanger delay when Scratch is held down</td>
</tr>
<tr class="even">
<td>Treble</td>
<td>Adjusts the volume of a channels high frequency content (ex. hi-hats)<br />
Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting<br />
Adjusts flanger depth when Scratch is held down</td>
</tr>
</tbody>
</table>

| Hercules DJ Control Steel Controls |                       |                           |  |
| ---------------------------------- | --------------------- | ------------------------- |  |
| Control                            | Default Mixxx Mapping |                           |  |
|                                    | FX Wet/Dry Knobs (1)  | Unmapped                  |  |
|                                    | FX Apply Select (1)   | Unmapped                  |  |
|                                    | Bank Shift (2)        | Unmapped                  |  |
|                                    | Pitch Bend + (12)     | Temp Rate Up              |  |
|                                    | Pitch Bend - (13)     | Temp Rate Down            |  |
|                                    | Vol Main (23)         | Master Gain               |  |
|                                    | 1 (9)                 | Flanger on/off            |  |
|                                    | 2 (9)                 | Hotcue 1 set              |  |
|                                    | 3 (9)                 | Hotcue 2 set              |  |
|                                    | 4 (9)                 | Reverse                   |  |
|                                    | 5 (9)                 | Hotcue 1 goto             |  |
|                                    | 6 (9)                 | Hotcue 2 goto             |  |
|                                    | 7 (9)                 | loop in                   |  |
|                                    | 8 (9)                 | loop exit                 |  |
|                                    | 10 (9)                | loop out                  |  |
|                                    | 9,11,12 (9)           | Unmapped                  |  |
|                                    | Up (8)                | Select Prev Track in List |  |
|                                    | Down (8)              | Select Next Track in List |  |
|                                    | Right, Left (8)       | Navigate                  |  |
|                                    | Stop (19)             | stop                      |  |
|                                    | Scratch (7)           | Unmapped                  |  |
|                                    | Vol\_HP (11)          | Not Available in Mixxx    |  |

| Hercules DJ Control Steel Controls |                                                                                                                |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Control                            | Default Mixxx Mapping                                                                                          |
| Scratch (7)                        | MIDI Script: Toggle Jog (18) Scratch/Pitch Adjust behaviour (buggy)                                            |
| Stop (20)                          | MIDI Script: Stop + Reset Track to beginning                                                                   |
| Up (8)/Down (8) + Jog (18)         | MIDI Script: Rapid Track List scrolling (reported buggy on RMX, but no problem seen on Steel)                  |
| Cue (21) + Play (19)               | MIDI Script: Pushing Play while holding Cue will cause track to continue to play after Cue is released (buggy) |
