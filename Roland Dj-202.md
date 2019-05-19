# Roland DJ-202

  - [Manufacturer's product
    page](https://www.roland.com/global/products/dj-202/)
  - [Forum
    thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=11664#p37423)

The Roland DJ-202 is an all-in-one USB MIDI controller with a built in
sound card. It has controls for 2 decks that can be toggled between
decks to play with 4 decks. As a special feature it's got an in-built
sequencer with 8 sounds from the TR-808 and the TR-909 drum machines
(TR-606 and TR-707 are available via firmware update).

## Drivers

### Windows & MacOS

You can download the latest drivers and firmware from
<https://www.roland.com/global/products/dj-202/downloads/>.

### Linux

The DJ-202 is a USB class compliant MIDI and audio device, so it's
plug-and-play on Linux.

#### Enabling generic mode

If the device is not properly detected as a MIDI device, you need to
enable generic mode in the system settings:

1.  Hold \[LOAD\] Button when plugging in the USB cable until the
    sequencer start/stop button blinks
2.  Press \[R channel performance pad 1\]
3.  Turn the rotary selector left, so only the upper left corner of the
    master level indicator is lit
4.  Press the blinking start/stop button
5.  Wait until all pads light up, then disconnect USB cable

## Mapping

A mapping is currently being developed, see
[Github](https://github.com/Lykos153/mixxx/tree/Mapping-DJ-202)

  - Pitch control
  - `Shift+Tempo Fader` – adjust pitch continuously
  - Jog wheel
  - `shift-jog` – strip search
  - FX
  - `FX1-3` (long) – focus FX1-3
  - `FX1-3` (short) – toggle effect 1-3 on/off
  - `(Shift-)FX tap` – Cycle focused effect forward/backward
  - `fx-level` – set FX meta depth
  - `shift-fx-level` – set effects rack dry/wet
  - `shift-fx1-3` – Routing mode - toggle sending respective deck output
    to fx1 on/off, fx2 on/off, headphones on/off
  - General
  - `Shift-Sync` – Toggle quantize on/off
  - `Slip` (double tap) – Latch slip mode
  - `Deck 3/4` (hold) – Toggle other deck temporarily, return to
    previous deck on release
  - `Deck 3/4` (press) – Toggle other deck
  - `Key lock-Param+/-` – Shift pitch up/down
  - `Key lock-Param+-Param` – Reset pitch
  - `Shift-cue` (long) – align beatgrid to other deck’s grid
  - `Shift-cue` (once) – align beatgrid to current play position
  - `Shift-cue` (tap multiple) – tap BPM
  - `Sync` (double tap) – Reset BPM
  - Performance pad groups
  - Hot cue mode

<!-- end list -->

``` 
    * ''Param+/-'' – beat jump forward/backward
    * ''Shift-Param+/-'' – increment/decrement beat jump distance
    * ''Pad 1-8'' – Save/jump to hot-cue
    * ''Shift-Pad 1-8'' (while playing) – Save hot-cue (overwrite existing)
    * ''Shift-Pad 1-8'' (while stopped) – Delete hot-cue
* Loop mode
    * ''Param+/-'' – move beatloop forward/backward
    * ''Shift-Param+/-'' – Double/halve beatloop size
    * ''Pad 1-4'' – toggle beatloop of length 1,2,4,8
    * ''Pad 5-8'' – Manual loop controls (in, out, exit, on/off)
```
