# Mixxx Controls

## What is a control?

Nearly every knob, button, or fader you see in Mixxx's interface is
controllable via Mixxx's "control" system. The control system allows
skins, MIDI controllers, and HID controllers to control Mixxx via a
single interface.

A control is identified by a "group" (which is used for grouping
associated controls) and a "key" (the name of the individual control).

For example, the volume fader for Deck 1 is identified by the group
`[Channel1]` and key `volume`. Similarly, the volume fader for Sampler 1
is identified by the group `[Sampler1]` and key `volume`.

The group is used to collect all the controls that affect one component
of Mixxx into one collection. Some groups have a high overlap of
controls in common (e.g. samplers, decks, and the preview deck all share
the same control keys).

In addition to controlling Mixxx, the control system can be used to
inspect Mixxx's state. For example, the sample rate of the track loaded
in Deck 1 can be accessed via the `[Channel1]`, `track_samplerate`
control. You can read the `[Channel3]`, `play` control to determine
whether Deck 3 is playing.

The following tables list the keys associated with each group.

## Tip: Discovering Controls used in Skins

You can view the control connected to any part of a skin by running
Mixxx with the `--developer` command line option and hovering your mouse
cursor over part of the skin. If no tooltip appears, enable tooltips for
the Library and Skin in Options \> Preferences \> Interface.

## Tip: Changing any control from the GUI in Developer Mode

When running Mixxx in Developer Mode (with the `--developer` command
line option), you can view and manually set the state of any control in
Mixxx by going to Developer \> Developer Tools.

## Naming Conventions

The keys of existing controls use different naming conventions, namely

  - ***PascalCase***: `VuMeter`, `MoveUp`, ...
  - ***camelCase***: `headSplit`, `duckStrength`, ...
  - ***snake\_case***: `beatjump_forward`, `cue_indicator`

Newly added controls should use the ***snake\_case*** naming
convention\[1\].

## List of Controls

The default range is 0.0 to 1.0, unless otherwise noted. Binary means
that it is either 'ON' (non-zero) or 'OFF' (zero).

*Please keep the controls in alphabetical order within each group.*

### `[Various]`

The following extensions add some features to ControlPotMeter controls
(volume, crossfader, ...). Use in conjunction with `[Channel*N*]`,
`[Sampler*N*]`, \[Master\] ... groups. Please note, this doesn't work in
JavaScript files, so you can not do, for example,
`engine.setValue('MyController', 'keylock_toggle')`.

| Key/Control           | Range   | What it does                                                                      | On-screen feedback                                                                              |
| --------------------- | ------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `_up`                 | default | Increases the value                                                               | e.g. "`[Channel*N*]`,rate\_perm\_up" sets the speed one step higher (4 % default)               |
| `_down`               | default | Decreases the value                                                               | e.g. "`[Channel*N*]`,rate\_perm\_down" sets the speed one step lower (4 % default)              |
| `_up_small`           | default | Increases the value by smaller step                                               | e.g. "`[Channel*N*]`,rate\_perm\_up\_small" sets the speed one small step higher (1 % default)  |
| `_down_small`         | default | Decreases the value by smaller step                                               | e.g. "`[Channel*N*]`,rate\_perm\_down\_small" sets the speed one small step lower (1 % default) |
| `_set_one`\[2\]       | default | Sets the value to 1.0                                                             | e.g. "`[Channel*N*]`,volume\_set\_one" sets the channel volume to full                          |
| `_set_minus_one`\[3\] | default | Sets the value to -1.0                                                            | e.g. "`[Channel*N*]`,volume\_set\_minus\_one" sets the channel volume to zero                   |
| `_set_default`\[4\]   | default | Sets the control to its default                                                   | e.g. "`[Channel*N*]`,waveform\_zoom\_set\_default" return to default waveform zoom level        |
| `_set_zero`\[5\]      | default | Sets the value to 0.0                                                             | e.g. "`[Master]`,crossfader\_set\_zero" put the crossfader in the middle again                  |
| `_toggle`\[6\]        | default | Sets the value to 0.0 if the value was \> 0.0, and to 1.0 if the value was 0.0    | e.g. "`[Channel*N*]`,volume\_toggle" will cut off/on a track while you're playing               |
| `_minus_toggle`\[7\]  | default | Sets the value to -1.0 if the value was \> -1.0, and to 1.0 if the value was -1.0 | e.g. "`[Master]`,crossfader\_minus\_toggle" can tilt the crossfader from left to right          |

### `[Master]`

The `[Master]` group generally corresponds to controls that affect the
mixing engine. This will bear some similarity to what you will find on a
DJ mixer (e.g. crossfader controls, headphone cueing controls, etc.).

| Key/Control                          | Range              | What it does                                                                                                                                                        | On-screen feedback               |
| ------------------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| `audio_latency_usage`\[8\]           | 0 .. 25 %          | Reflects fraction of latency, given by the audio buffer size, spend for audio processing inside Mixxx. At value near 25 % there is a high risk of buffer underflows | latency meter                    |
| `audio_latency_overload`\[9\]        | binary             | Indicates a buffer under or over-flow. Resets after 500 ms                                                                                                          | Overload indicator               |
| `audio_latency_overload_count`\[10\] | 0 .. n             | Counts buffer over and under-flows. Max one per 500 ms                                                                                                              | Counter in hardware preferences  |
| `balance`                            | \-1.0..1.0         | Adjusts the left/right channel balance on the Master output                                                                                                         | Center Balance knob              |
| `booth_enabled`\[11\]                | binary             | Indicates whether a Booth output is configured in the Sound Hardware Preferences                                                                                    | Booth gain knob shown or hidden  |
| `booth_gain`\[12\]                   | 0.0...1.0...5.0    | Adjusts the gain of the Booth output                                                                                                                                | Booth gain knob                  |
| `crossfader`                         | \-1.0..1.0         | Adjusts the crossfader between players/decks (-1.0 is all the way left, Deck 1)                                                                                     | Crossfader slider                |
| `crossfader_down`                    | binary             | Moves the crossfader left by 1/10th                                                                                                                                 | Crossfader slider                |
| `crossfader_down_small`\[13\]        | binary             | Moves the crossfader left by 1/100th                                                                                                                                | Crossfader slider                |
| `crossfader_up`                      | binary             | Moves the crossfader right by 1/10th                                                                                                                                | Crossfader slider                |
| `crossfader_up_small`\[14\]          | binary             | Moves the crossfader right by 1/100th                                                                                                                               | Crossfader slider                |
| `duckStrength`\[15\]                 | 0.0..1.0           | Microphone ducking strength                                                                                                                                         | Strength knob                    |
| `enabled`\[16\]                      | binary             | Indicator that the master mix is processed                                                                                                                          | n/a                              |
| `gain`\[17\]                         | 0.0..1.0..5.0      | Adjusts the gain for the master output as well as recording and broadcasting signal                                                                                 | Master Vol knob                  |
| `headEnabled`\[18\]                  | binary             | Indicator that the headphone mix is processed                                                                                                                       | n/a                              |
| `headGain`\[19\]                     | 0.0..1.0..5.0      | Adjusts the headphone output gain                                                                                                                                   | Head Vol knob                    |
| `headMix`                            | default         | Adjusts the cue/main mix in the headphone output                                                                                                                    | Pre/Main knob                    |
| `headSplit`\[20\]                    | binary             | Splits headphone cueing into right = master mono and left = pfl mono.                                                                                               | Split Cue button                 |
| `latency`                            | absolute value     | Latency setting (sound buffer size) in milliseconds (default 64)                                                                                                    | Latency slider in the prefs      |
| `maximize_library`\[21\]             | binary             | Toggle maximized view of library                                                                                                                                    | Toggle maximized view of library |
| `num_decks`\[22\]                    | integer            | The number of decks currently enabled.                                                                                                                              | N/A                              |
| `num_effectsavailable`\[23\]         | integer, read-only | The number of available effects that can be selected in an effect slot.                                                                                             | N/A                              |
| `num_samplers`\[24\]                 | integer            | The number of samplers currently enabled.                                                                                                                           | N/A                              |
| `num_preview_decks`\[25\]            | integer            | The number of preview decks currently enabled.                                                                                                                      | N/A                              |
| `PeakIndicator`                      | binary             | Indicates when the signal is clipping (too loud for the hardware and is being distorted)                                                                            | Clip light                       |
| `samplerate`                         | absolute value     | The current output sample rate in Hz (default 44100)                                                                                                                | (none)                           |
| `talkoverDucking`\[26\]              | FIXME              | Toggle microphone ducking mode (OFF, AUTO, MANUAL)                                                                                                                  | Ducking mode button              |
| `VuMeter`                            | default            | Outputs the current instantaneous master volume (composite)                                                                                                         | Master meter (mono)              |
| `VuMeterL`                           | default            | Outputs the current instantaneous master volume for the left channel                                                                                                | Master meter L                   |
| `VuMeterR`                           | default            | Outputs the current instantaneous master volume for the right channel                                                                                               | Master meter R                   |

### `[ChannelN]`

The `[ChannelN]` group is for each deck in Mixxx. Whenever you see
`[ChannelN]`, think "Deck N". N can range from 1 to the number of active
decks in Mixxx.\[27\]

| Key/Control                             | Range                         | What it does                                                                                                                                                                                                                                                                                      | On-screen feedback                                                                                                                                                                 |
| --------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `back`                                  | binary                        | Fast rewind (REW)                                                                                                                                                                                                                                                                                 | \< button                                                                                                                                                                          |
| `beat_active`\[28\]                     | binary                        | Indicates whether the player is currently positioned within 50 milliseconds of a beat or not.                                                                                                                                                                                                     | N/A                                                                                                                                                                                |
| `beatjump`\[29\]                        | real number                   | Jump forward by X beats (positive) or backward by X beats (negative). If a loop is active, the loop is moved by X beats.                                                                                                                                                                          | Player jumps forward or backward by X beats.                                                                                                                                       |
| `beatjump_size`\[30\]                   | positive real number          | Set the number of beats to jump with beatjump\_forward/backward.                                                                                                                                                                                                                                  | Beatjump size spinbox                                                                                                                                                              |
| `beatjump_forward`\[31\]                | binary                        | Jump forward by beatjump\_size. If a loop is active, the loop is moved forward by X beats.                                                                                                                                                                                                        | Player jumps forward by beatjump\_size.                                                                                                                                            |
| `beatjump_backward`\[32\]               | binary                        | Jump backward by beatjump\_size. If a loop is active, the loop is moved backward by X beats.                                                                                                                                                                                                      | Player jumps backward by beatjump\_size.                                                                                                                                           |
| `beatjump_X_forward`\[33\]              | binary                        | Jump forward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64. If a loop is active, the loop is moved forward by X betas.                                                                                                                           | Player jumps forward by X beats.                                                                                                                                                   |
| `beatjump_X_backward`\[34\]             | binary                        | Jump backward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64. If a loop is active, the loop is moved backward by X beats.                                                                                                                         | Player jumps backward by X beats.                                                                                                                                                  |
| `beatloop_activate`\[35\]               | binary                        | Set a loop that is beatloop\_size beats long and enables the loop                                                                                                                                                                                                                                 | A loop is shown over beatloop\_size beats                                                                                                                                          |
| `beatloop_X_activate`\[36\]             | binary                        | Activates a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                                                 | A loop is shown over X beats.                                                                                                                                                      |
| `beatloop_size`\[37\]                   | positive real number          | Set the length of the loop in beats that will get set with beatloop\_activate and beatlooproll\_activate. Changing this will resize an existing loop if the length of the loop matches beatloop\_size.                                                                                            | Beatloop size spinbox and possibly loop section on waveform                                                                                                                        |
| `beatloop_X_toggle`\[38\]               | binary                        | Toggles a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                                                   | A loop is shown over X beats.                                                                                                                                                      |
| `beatloop_X_enabled`\[39\]              | binary                        | 1 if beatloop X is enabled, 0 if not.                                                                                                                                                                                                                                                             | Beatloop X button in skin is lit.                                                                                                                                                  |
| `beatlooproll_activate`\[40\]           | binary                        | Activates a rolling loop over beatloop\_size beats. Once disabled, playback will resume where the track would have been if it had not entered the loop.                                                                                                                                           | A loop overlay is shown over beatloop\_size beats on waveform.                                                                                                                     |
| `beatlooproll_X_activate`\[41\]         | binary                        | Activates a rolling loop over X beats. Once disabled, playback will resume where the track would have been if it had not entered the loop. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                     | Beatloop X button in skin is lit. A loop overlay is shown over X beats on waveform.                                                                                                |
| `beats_adjust_faster`\[42\]             | binary                        | Adjust the average BPM up by +0.01                                                                                                                                                                                                                                                                | Beatgrid lines move closer to each other.                                                                                                                                          |
| `beats_adjust_slower`\[43\]             | binary                        | Adjust the average BPM down by -0.01.                                                                                                                                                                                                                                                             | Beatgrid lines move further apart from each other.                                                                                                                                 |
| `beats_translate_curpos`\[44\]          | binary                        | Adjust beatgrid so closest beat is aligned with the current playposition.                                                                                                                                                                                                                         | Beatgrid moves to align with current playposition.                                                                                                                                 |
| `beats_translate_match_alignment`\[45\] | binary                        | Adjust beatgrid to match another playing deck.                                                                                                                                                                                                                                                    | Instead of syncing the beatgrid to the current playposition, sync the beatgrid so the nearest beat lines up with the other track's nearest beat.                                   |
| `beats_translate_earlier`\[46\]          | binary                        | Move Beatgrid earlier                                                                                                                                                                                                                                                                             | Beatgrid moves left by a small amount.                                                                                                                                             |
| `beats_translate_later`\[47\]            | binary                        | Move Beatgrid later                                                                                                                                                                                                                                                                               | Beatgrid moves right by a small amount.                                                                                                                                            |
| ~~`beatsync`~~                           | ~~binary~~                    | ~~Syncs the BPM to that of the other track (if BPM is detected on both)~~                                                                                                                                                                                                                         | ~~SYNC button & Speed slider snaps to the appropriate value~~                                                                                                                      |
| `beatsync`\[48\]                         | binary                        | **changed behavior** Syncs the BPM and phase (depending on quantize) to that of the other track (if BPM is detected on both)                                                                                                                                                                      | SYNC button & Speed slider snaps to the appropriate value                                                                                                                          |
| `beatsync_phase`\[49\]                   | binary                        | Syncs the phase to that of the other track (if BPM is detected on both)                                                                                                                                                                                                                           | SYNC button & Speed slider snaps to the appropriate value                                                                                                                          |
| `beatsync_tempo`\[50\]                   | binary                        | Syncs the BPM to that of the other track (if BPM is detected on both)                                                                                                                                                                                                                             | SYNC button & Speed slider snaps to the appropriate value                                                                                                                          |
| ~~`bpm`~~                                | ~~absolute value~~            | ~~Reads or sets the track's current BPM (changing the pitch)~~                                                                                                                                                                                                                                    | ~~BPM value display~~                                                                                                                                                              |
| ~~`bpm`\[51\]~~                          | ~~real-valued~~               | ~~bpm now only reflects the bpm of the loaded track~~                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                |
| `bpm`\[52\]                              | real-valued                   | bpm reflects the perceived (rate-adjusted) BPM of the file loaded in ChannelN                                                                                                                                                                                                                     | BPM value display                                                                                                                                                                  |
| ~~`bpm_tap`\[53\]~~                      | ~~binary~~                    | ~~When tapped repeatedly, adjusts the playback rate of ChannelN to match the tapped BPM~~                                                                                                                                                                                                         | ~~track playback rate shifts after 4 or more taps~~                                                                                                                                |
| `bpm_tap`\[54\]                          | binary                        | When tapped repeatedly, adjusts the BPM of ChannelN to match the tapped BPM                                                                                                                                                                                                                       | BPM value display (play speed doesn't change)                                                                                                                                      |
| `CloneFromDeck`\[55\]                    | integer                       | Clone the given deck number, copying the play state, position, rate, and key. If 0 or a negative number is given, Mixxx will attempt to select the first playing deck as the source for the clone.                                                                                                | The channel will start playing at the rate and position of the source deck.                                                                                                        |
| `cue_default`                            | binary                        | In CDJ mode, when playing, returns to the cue point & pauses. If stopped, sets a cue point at the current location. If stopped and at a cue point, plays from that point until released (set to 0.)                                                                                               | CUE button                                                                                                                                                                         |
| `cue_gotoandplay`\[56\]                  | binary                        | If the Cue point is set, seeks the player to it and starts playback.                                                                                                                                                                                                                              | Player may change position and start playing.                                                                                                                                      |
| `cue_gotoandstop`\[57\]                  | binary                        | If the Cue point is set, seeks the player to it and stops.                                                                                                                                                                                                                                        | Player may change position.                                                                                                                                                        |
| `cue_indicator`\[58\]                    | binary                        | Provides information to be bound to the Cue Button e.g. blinking when next press will move the cue point                                                                                                                                                                                          | Cue button                                                                                                                                                                         |
| `cue_cdj`\[59\]                          | binary                        | Cue button, always in CDJ mode                                                                                                                                                                                                                                                                    | n/a                                                                                                                                                                                |
| `cue_play`\[60\]                         | binary                        | CUP button, Go to cue point and play after release. If stopped, sets a cue point at the current location.                                                                                                                                                                                         | n/a                                                                                                                                                                                |
| `cue_point`                              | absolute value                | The current position of the cue point in samples                                                                                                                                                                                                                                                  | Cue point marker                                                                                                                                                                   |
| `cue_preview`                            | binary                        | Plays from the current cue point                                                                                                                                                                                                                                                                  | CUE button lights & waveform moves                                                                                                                                                 |
| `cue_set`                                | binary                        | Sets a cue point at the current location                                                                                                                                                                                                                                                          | Cue mark appears on the waveform                                                                                                                                                   |
| `cue_simple`                             | binary                        | If the player is not playing, set the cue point at the current location otherwise seek to the cue point.                                                                                                                                                                                          | CUE button                                                                                                                                                                         |
| `duration`                               | absolute value                | Outputs the length of the current song in seconds                                                                                                                                                                                                                                                 | (none)                                                                                                                                                                             |
| `eject`\[61\]                            | binary                        | Eject currently loaded track                                                                                                                                                                                                                                                                      | Eject button is lit. Be sure to set back to 0 with scripts so the button does not stay lit.                                                                                        |
| `end`                                    | binary                        | Jump to end of track                                                                                                                                                                                                                                                                              | Track jumps to end                                                                                                                                                                 |
| `end_of_track`                           | binary, read-only             | Switches to "1" if the play osition is within the 'end' range defined in Preferences \> Waveforms \> "End of track warning"                                                                                                                                                                       | Waveform and Overview widgets show a flashing border                                                                                                                               |
| `file_bpm`                               | positive value, read-only     | the detected BPM of the loaded track                                                                                                                                                                                                                                                              | N/A                                                                                                                                                                                |
| `file_key`\[62\]                         | ?, read-only                  | the detected key of the loaded track                                                                                                                                                                                                                                                              | N/A                                                                                                                                                                                |
| `fwd`                                    | binary                        | Fast forward (FF)                                                                                                                                                                                                                                                                                 | \> button                                                                                                                                                                          |
| `hotcue_X_activate`\[63\]                | binary                        | If hotcue X is set, seeks the player to hotcue X's position. If hotcue X is not set, sets hotcue X to the current play position. To continue playing while any hotcues are activated, play must be set to 0, not 1.                                                                               | Player may change position. Hotcue X marker may change on waveform.                                                                                                                |
| `hotcue_X_clear`\[64\]                   | binary                        | If hotcue X is set, clears its hotcue status.                                                                                                                                                                                                                                                     | Hotcue X marker changes on waveform.                                                                                                                                               |
| `hotcue_X_color`\[65\]                   | 3-Byte RGB color code (or -1) | Color of hotcue X or -1 if the hotcue is not set.                                                                                                                                                                                                                                                 | Color of Hotcue X button and waveform marker changes.                                                                                                                              |
| `hotcue_X_enabled`\[66\]                 | binary, read-only             | 1 if hotcue X is active, (position is not -1), 0 otherwise.                                                                                                                                                                                                                                       |                                                                                                                                                                                    |
| `hotcue_X_goto`\[67\]                    | binary                        | If hotcue X is set, seeks the player to hotcue X's position.                                                                                                                                                                                                                                      | Player may change position.                                                                                                                                                        |
| `hotcue_X_gotoandplay`\[68\]             | binary                        | If hotcue X is set, seeks the player to hotcue X's position and starts playback.                                                                                                                                                                                                                  | Player may change position.                                                                                                                                                        |
| `hotcue_X_gotoandstop`\[69\]             | binary                        | If hotcue X is set, seeks the player to hotcue X's position and stops.                                                                                                                                                                                                                            | Player may change position.                                                                                                                                                        |
| `hotcue_X_position`\[70\]                | positive integer              | The position of hotcue X in samples, -1 if not set.                                                                                                                                                                                                                                               | Hotcue X marker changes on waveform.                                                                                                                                               |
| `hotcue_X_set`\[71\]                     | binary                        | Set hotcue X to the current play position. If hotcue X was previously set, clears its hotcue status.                                                                                                                                                                                              | Hotcue X marker changes on waveform.                                                                                                                                               |
| `hotcue_focus`\[72\]                     | positive integer (or -1)      | Contains the number of the most recentlly used hotcue (or -1 if no hotcue was used)                                                                                                                                                                                                               | N/A                                                                                                                                                                                |
| `hotcue_focus_color_prev`\[73\]          | binary                        | If there is a focused hotcue, sets its color to the previous color in the palette.                                                                                                                                                                                                                | Color of focused hotcue button and waveform marker changes.                                                                                                                        |
| `hotcue_focus_color_next`\[74\]          | binary                        | If there is a focused hotcue, sets its color to the next color in the palette.                                                                                                                                                                                                                    | Color of focused hotcue button and waveform marker changes.                                                                                                                        |
| `intro_end_activate`\[75\]               | binary                        | If the intro end cue is set, seeks the player to the intro end position. If the intro end is not set, sets the intro end to the current play position.                                                                                                                                            | Player may change position. Intro end marker may change on waveform.                                                                                                               |
| `intro_end_clear`\[76\]                  | binary                        | If the intro end cue is set, clears its status.                                                                                                                                                                                                                                                   | Intro end marker changes on waveform.                                                                                                                                              |
| `intro_end_enabled`\[77\]                | binary, read-only             | 1 if intro end cue is set, (position is not -1), 0 otherwise.                                                                                                                                                                                                                                     | Intro end button lights up.                                                                                                                                                        |
| `intro_end_position`\[78\]               | positive integer              | The position of the intro end in samples, -1 if not set.                                                                                                                                                                                                                                          | Intro end marker changes on waveform.                                                                                                                                              |
| `intro_end_set`\[79\]                    | binary                        | Set intro end to the current play position. If intro end was previously set, it is moved to the new position.                                                                                                                                                                                     | Intro end marker changes on waveform.                                                                                                                                              |
| `intro_start_activate`\[80\]             | binary                        | If the intro start cue is set, seeks the player to the intro start position. If the intro start is not set, sets the intro start to the current play position.                                                                                                                                    | Player may change position. Intro start marker may change on waveform.                                                                                                             |
| `intro_start_clear`\[81\]                | binary                        | If the intro start cue is set, clears its status.                                                                                                                                                                                                                                                 | Intro start marker changes on waveform.                                                                                                                                            |
| `intro_start_enabled`\[82\]              | binary, read-only             | 1 if intro start cue is set, (position is not -1), 0 otherwise.                                                                                                                                                                                                                                   | Intro start button lights up.                                                                                                                                                      |
| `intro_start_position`\[83\]             | positive integer              | The position of the intro start in samples, -1 if not set.                                                                                                                                                                                                                                        | Intro start marker changes on waveform.                                                                                                                                            |
| `intro_start_set`\[84\]                  | binary                        | Set intro start to the current play position. If intro start was previously set, it is moved to the new position.                                                                                                                                                                                 | Intro start marker changes on waveform.                                                                                                                                            |
| `key`\[85\]                              | real-valued                   | Current key of the track                                                                                                                                                                                                                                                                          |                                                                                                                                                                                    |
| `keylock`\[86\]                          | binary                        | Enable key-lock for the specified deck (rate changes only affect tempo, not key)                                                                                                                                                                                                                  | key-lock button activates                                                                                                                                                          |
| `LoadSelectedTrack`                      | binary                        | Loads the currently highlighted track into the deck                                                                                                                                                                                                                                               | Track name & waveform change                                                                                                                                                       |
| `LoadSelectedTrackAndPlay`\[87\]         | binary                        | Loads the currently highlighted track into the deck and starts playing                                                                                                                                                                                                                            | Track name & waveform change & Play/pause button                                                                                                                                   |
| `loop_double`\[88\]                      | binary                        | Doubles beatloop\_size. If beatloop\_size equals the size of the loop, the loop is resized. \[89\]                                                                                                                                                                                                | beatloop\_size spinbox changes                                                                                                                                                     |
| `loop_enabled`\[90\]                     | binary, read-only             | Indicates whether or not a loop is enabled.                                                                                                                                                                                                                                                       | Loop in waveform is active.                                                                                                                                                        |
| `loop_end_position`\[91\]                | positive integer              | The player loop-out position in samples, -1 if not set.                                                                                                                                                                                                                                           | Loop-out marker shows on waveform.                                                                                                                                                 |
| `loop_halve`\[92\]                       | binary                        | Halves beatloop\_size. If beatloop\_size equals the size of the loop, the loop is resized. \[93\]                                                                                                                                                                                                 | beatloop\_size spinbox changes                                                                                                                                                     |
| `loop_in`\[94\]                          | binary                        | If loop is disabled, sets the player loop in position to the current play position. If loop is enabled, press and hold to move loop in position to the current play position. If quantize is enabled, beatloop\_size will be updated to reflect the new loop size. \[95\]                         | Loop-in marker changes on waveform.                                                                                                                                                |
| `loop_in_goto`\[96\]                     | binary                        | Seek to the loop in point.                                                                                                                                                                                                                                                                        | Waveform position jumps                                                                                                                                                            |
| `loop_out`\[97\]                         | binary                        | If loop is disabled, sets the player loop out position to the current play position. If loop is enabled, press and hold to move loop out position to the current play position. If quantize is enabled, beatloop\_size will be updated to reflect the new loop size. \[98\]                       | Loop-out marker changes on waveform.                                                                                                                                               |
| `loop_out_goto`\[99\]                    | binary                        | Seek to the loop out point.                                                                                                                                                                                                                                                                       | Waveform position jumps                                                                                                                                                            |
| `loop_move`\[100\]                       | real number                   | Move loop forward by X beats (positive) or backward by X beats (negative).                                                                                                                                                                                                                        | Loop moves forward or backward by X beats.                                                                                                                                         |
| `loop_move_X_forward`\[101\]             | binary                        | Moves the loop in and out points forward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                           | Loop moves forward by X beats.                                                                                                                                                     |
| `loop_move_X_backward`\[102\]            | binary                        | Loop moves by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                                                         | Loop moves backward by X beats.                                                                                                                                                    |
| `loop_scale`\[103\]                      | 0.0 - infinity                | Scale the loop length by the value scale is set to by moving the end marker. beatloop\_size is not updated to reflect the change.                                                                                                                                                                 | Loop length is scaled by given amount on waveform.                                                                                                                                 |
| `loop_start_position`\[104\]             | positive integer              | The player loop-in position in samples, -1 if not set.                                                                                                                                                                                                                                            | Loop-in marker changes on waveform.                                                                                                                                                |
| `orientation`\[105\]                     | 0-2                           | Crossfader assignment. 0 = left side of crossfader, 1 = center (not affected by crossfader), 2 = right side of crossfader                                                                                                                                                                         | N/A                                                                                                                                                                                |
| `outro_end_activate`\[106\]              | binary                        | If the outro end cue is set, seeks the player to the outro end position. If the outro end is not set, sets the outro end to the current play position.                                                                                                                                            | Player may change position. Outro end marker may change on waveform.                                                                                                               |
| `outro_end_clear`\[107\]                 | binary                        | If the outro end cue is set, clears its status.                                                                                                                                                                                                                                                   | Outro end marker changes on waveform.                                                                                                                                              |
| `outro_end_enabled`\[108\]               | binary, read-only             | 1 if outro end cue is set, (position is not -1), 0 otherwise.                                                                                                                                                                                                                                     | Outro end button lights up.                                                                                                                                                        |
| `outro_end_position`\[109\]              | positive integer              | The position of the outro end in samples, -1 if not set.                                                                                                                                                                                                                                          | Outro end marker changes on waveform.                                                                                                                                              |
| `outro_end_set`\[110\]                   | binary                        | Set outro end to the current play position. If outro end was previously set, it is moved to the new position.                                                                                                                                                                                     | Outro end marker changes on waveform.                                                                                                                                              |
| `outro_start_activate`\[111\]            | binary                        | If the outro start cue is set, seeks the player to the outro start position. If the outro start is not set, sets the outro start to the current play position.                                                                                                                                    | Player may change position. Outro start marker may change on waveform.                                                                                                             |
| `outro_start_clear`\[112\]               | binary                        | If the outro start cue is set, clears its status.                                                                                                                                                                                                                                                 | Outro start marker changes on waveform.                                                                                                                                            |
| `outro_start_enabled`\[113\]             | binary, read-only             | 1 if outro start cue is set, (position is not -1), 0 otherwise.                                                                                                                                                                                                                                   | Outro start button lights up.                                                                                                                                                      |
| `outro_start_position`\[114\]            | positive integer              | The position of the outro start in samples, -1 if not set.                                                                                                                                                                                                                                        | Outro start marker changes on waveform.                                                                                                                                            |
| `outro_start_set`\[115\]                 | binary                        | Set outro start to the current play position. If outro start was previously set, it is moved to the new position.                                                                                                                                                                                 | Outro start marker changes on waveform.                                                                                                                                            |
| `passthrough`\[116\]                     | binary                        | Connects the vinyl control input for vinyl control on that deck to the channel output. Allows to mix external media into DJ sets.                                                                                                                                                                 | GUI control currently missing FIXME                                                                                                                                                |
| `PeakIndicator`                          | binary                        | Indicates when the signal is clipping (too loud for the hardware and is being distorted)                                                                                                                                                                                                          | Clip light                                                                                                                                                                         |
| `pfl`                                    | binary                        | Toggles headphone cueing                                                                                                                                                                                                                                                                          | Headphone button                                                                                                                                                                   |
| `pitch`\[117\]                           | \-6.0..6.0                    | The total adjustment to the track's pitch, including changes from the rate slider if keylock is off as well as pitch\_adjust. Do not map this to knobs or sliders on controllers; map pitch\_adjust instead.                                                                                      | Key display                                                                                                                                                                        |
| `pitch_up`\[118\]                        | binary                        | Changes the track pitch up one half step, independent of the tempo.                                                                                                                                                                                                                               | Key display                                                                                                                                                                        |
| `pitch_down`\[119\]                      | binary                        | Changes the track pitch down one half step, independent of the tempo.                                                                                                                                                                                                                             | Key display                                                                                                                                                                        |
| `pitch_adjust`\[120\]                    | \-3.0..3.0                    | Adjust the pitch in addition to the speed slider pitch.                                                                                                                                                                                                                                           | Key display                                                                                                                                                                        |
| `play`                                   | binary                        | Toggles playing or pausing the track. Feedback: 1.0 if track is playing or play command is adopted and track will be played after loading                                                                                                                                                         | Play/pause button                                                                                                                                                                  |
| `play_indicator`\[121\]                  | binary                        | Provides information to be bound with the a Play/Pause button e.g blinking when play is possible                                                                                                                                                                                                  | Play/pause button                                                                                                                                                                  |
| `play_stutter`\[122\]                    | binary                        | A play button without pause. Pushing while playing, starts play at cue point again (Stutter).                                                                                                                                                                                                     | Play/Stutter button                                                                                                                                                                |
| `playposition`                           | default                       | Sets the absolute position in the track. The Range is -0.14 to 1.14 (0 = beginning -\> Midi 14, 1 = end -\> Midi 114)                                                                                                                                                                             | Waveform                                                                                                                                                                           |
| `pregain`                                | 0.0..1.0..4.0                 | Adjusts the pre-fader gain of the track (to avoid clipping)                                                                                                                                                                                                                                       | GAIN knob                                                                                                                                                                          |
| `quantize`\[123\]                        | binary                        | Aligns Hot-cues and Loop In & Out to the next beat from the current position.                                                                                                                                                                                                                     | Hot-cues or Loop In/Out markers                                                                                                                                                    |
| `quantize_beat`\[124\]                   | deprecated                    | ?                                                                                                                                                                                                                                                                                                 | Is used internally by CueControl (CUEs & Hotcues) and LoopingControl for quantization.                                                                                             |
| `rate`                                   | \-1.0..1.0                    | Speed control                                                                                                                                                                                                                                                                                     | Speed slider                                                                                                                                                                       |
| `rate_dir`                               | \-1 or 1                      | indicates orientation of speed slider.                                                                                                                                                                                                                                                            | ?                                                                                                                                                                                  |
| `rate_perm_down`                         | binary                        | Sets the speed one step lower (4 % default) lower                                                                                                                                                                                                                                                 | Perm down button & Speed slider                                                                                                                                                    |
| `rate_perm_down_small`                   | binary                        | Sets the speed one small step lower (1 % default)                                                                                                                                                                                                                                                 | Perm down button & Speed slider                                                                                                                                                    |
| `rate_perm_up`                           | binary                        | Sets the speed one step higher (4 % default)                                                                                                                                                                                                                                                      | Perm up button & Speed slider                                                                                                                                                      |
| `rate_perm_up_small`                     | binary                        | Sets the speed one small step higher (1 % default)                                                                                                                                                                                                                                                | Perm up button & Speed slider                                                                                                                                                      |
| `rate_temp_down`                         | binary                        | Holds the speed one step lower while active                                                                                                                                                                                                                                                       | Temp down button & Speed slider                                                                                                                                                    |
| `rate_temp_down_small`                   | binary                        | Holds the speed one small step lower while active                                                                                                                                                                                                                                                 | Temp down button & Speed slider                                                                                                                                                    |
| `rate_temp_up`                           | binary                        | Holds the speed one step higher while active                                                                                                                                                                                                                                                      | Temp up button & Speed slider                                                                                                                                                      |
| `rate_temp_up_small`                     | binary                        | Holds the speed one small step higher while active                                                                                                                                                                                                                                                | Temp up button & Speed slider                                                                                                                                                      |
| `rateRange`                              | 0.0..3.0                      | Sets the range of the Speed slider (0.08 = 8%)                                                                                                                                                                                                                                                    | none, until you move the Speed slider                                                                                                                                              |
| `rateSearch`                             | \-300..300                    | Seeks forward (positive values) or backward (negative values) at a speed determined by the value                                                                                                                                                                                                  | Deck seeks                                                                                                                                                                         |
| `rateEngine`                             |                               | Actual rate (used in visuals, not for control)                                                                                                                                                                                                                                                    |                                                                                                                                                                                    |
| `reloop_andstop`\[125\]                  | binary                        | Activate current loop, jump to its loop in point, and stop playback.                                                                                                                                                                                                                              | Loop range in waveform activates or deactivates and play position moves to loop in point.                                                                                          |
| `reloop_toggle`\[126\]                   | binary                        | Toggles the current loop on or off. If the loop is ahead of the current play position, the track will keep playing normally until it reaches the loop.                                                                                                                                            | Loop range in waveform activates or deactivates.                                                                                                                                   |
| `repeat`\[127\]                          | binary                        | Enable repeat-mode for the specified deck                                                                                                                                                                                                                                                         | when track finishes, song loops to beginning                                                                                                                                       |
| `reset_key`\[128\]                       | binary                        | Resets the key to the original track key.                                                                                                                                                                                                                                                         |                                                                                                                                                                                    |
| `reverse`                                | binary                        | Toggles playing the track backwards                                                                                                                                                                                                                                                               | REV button                                                                                                                                                                         |
| `reverseroll`\[129\]                     | binary                        | Enables reverse and slip mode while held (Censor)                                                                                                                                                                                                                                                 | REV button                                                                                                                                                                         |
| `scratch2`\[130\]                        | \-3.0..3.0                    | Affects **absolute** play speed & direction whether currently playing or not when *scratch2\_enabled* is active. (multiplicative). Use [JavaScript engine.scratch functions](MIDI%20scripting#Scratching%20and%20jog%20wheels) to manipulate in controller mappings.                              | Waveform                                                                                                                                                                           |
| `scratch2_enable`\[131\]                 | binary                        | Takes over play speed & direction for *scratch2*.                                                                                                                                                                                                                                                 | Waveform                                                                                                                                                                           |
| `slip_enabled`\[132\]                    | binary                        | Toggles slip mode. When active, the playback continues muted in the background during a loop, scratch etc. Once disabled, the audible playback will resume where the track would have been.                                                                                                       | Slip mode button                                                                                                                                                                   |
| `stars_up`\[133\]                        | binary                        | Increase the rating of the currently loaded track (if the skin has star widgets in the decks section)                                                                                                                                                                                             | Star count is increased in the deck's star widget and in the library table                                                                                                         |
| `stars_down`\[134\]                      | binary                        | Decrease the rating of the currently loaded track (if the skin has star widgets in the decks section)                                                                                                                                                                                             | Star count is decreased in the deck's star widget and in the library table                                                                                                         |
| `start`                                  | binary                        | Jump to start of track                                                                                                                                                                                                                                                                            | Track jumps to start                                                                                                                                                               |
| `start_play`\[135\]                      | binary                        | Start playback from the beginning of the deck.                                                                                                                                                                                                                                                    | Deck plays from beginning                                                                                                                                                          |
| `start_stop`\[136\]                      | binary                        | Seeks a player to the start and then stops it.                                                                                                                                                                                                                                                    | Deck stops at the beginning                                                                                                                                                        |
| `stop`\[137\]                            | binary                        | Stops a player.                                                                                                                                                                                                                                                                                   | Pause Button. Deck pauses at the current position                                                                                                                                  |
| `sync_enabled`\[138\]                    | binary                        | Syncs the BPM and phase (depending on quantize) to that of the other track (if BPM is detected on both). Click & hold for at least one second activates Master sync on that deck.                                                                                                                 | SYNC button & Speed slider snaps to the appropriate value. If pressed and held, SYNC button stays lit and slider adjustments are linked on all decks that have SYNC enabled.       |
| `sync_master`\[139\]                     | binary                        | Sets deck as master clock. (NOTE: Through version 2.3 this button just enables master sync mode (similar to sync\_enabled), it does not actually guarantee the deck will be master. This will be fixed in a future version)                                                                       | SYNC button will light up and stay lit & Speed slider snaps to the appropriate value. SYNC button stays lit and slider adjustments are linked on all decks that have SYNC enabled. |
| `sync_mode`\[140\]                       | binary                        | SYNC\_NONE = 0; SYNC\_FOLLOWER = 1; SYNC\_MASTER = 2,                                                                                                                                                                                                                                             |                                                                                                                                                                                    |
| `sync_key`\[141\]                        | ?                             | Match musical key                                                                                                                                                                                                                                                                                 | Key value widget                                                                                                                                                                   |
| `track_color`\[142\]                     | 3-Byte RGB color code (or -1) | Color of the currently loaded track or -1 if no track is loaded or the track has no color.                                                                                                                                                                                                        | Track color changes in the library view.                                                                                                                                           |
| `track_loaded`\[143\]                    | binary, read-only             | Whether a track is loaded in the specified deck                                                                                                                                                                                                                                                   | Waveform and track metadata shown in deck                                                                                                                                          |
| `track_samplerate`\[144\]                | absolute value, read-only     | Sample rate of the track loaded on the specified deck                                                                                                                                                                                                                                             | n/a                                                                                                                                                                                |
| `track_samples`                          | absolute value, read-only     | Number of sound samples in the track loaded on the specified deck                                                                                                                                                                                                                                 | n/a                                                                                                                                                                                |
| `volume`                                 | default                       | Adjusts the channel volume fader                                                                                                                                                                                                                                                                  | VOL fader                                                                                                                                                                          |
| `mute`\[145\]                            | binary                        | Mutes the channel                                                                                                                                                                                                                                                                                 | Mute button                                                                                                                                                                        |
| `vinylcontrol_enabled`\[146\]            | binary                        | Toggles whether a deck is being controlled by digital vinyl                                                                                                                                                                                                                                       | When enabled, a vinyl indication should appear onscreen indicating green for Enabled                                                                                               |
| `vinylcontrol_cueing`\[147\]             | 0.0-2.0                       | Determines how cue points are treated in vinyl control Relative mode                                                                                                                                                                                                                              | Off - cue points ignored; One Cue - If needle is dropped after the cue point, track will seek to that cue point; hot cue - track will seek to nearest previous hot cue point       |
| `vinylcontrol_mode`\[148\]               | 0.0-2.0                       | Determines how vinyl control interprets needle information: absolute mode - track position equals needle position and speed; relative mode - track speed equals needle speed regardless of needle position; constant mode - track speed equals last known-steady speed regardless of needle input | 3-way button indicates status                                                                                                                                                      |
| `vinylcontrol_status`\[149\]             | 0.0-3.0, read-only            | Provides visual feedback with regards to vinyl control status                                                                                                                                                                                                                                     | Off for control disabled, green for control enabled, blinking yellow for when the needle reaches the end of the record, and red for needle skip detected                           |
| `visual_bpm`\[150\]                      | ?                             | BPM to display in the UI (updated more slowly than the actual bpm)                                                                                                                                                                                                                                | BPM value widget                                                                                                                                                                   |
| `visual_key`\[151\]                      | ?                             | Current musical key after pitch shifting to display in the UI using the notation selected in the preferences                                                                                                                                                                                      | Key value widget                                                                                                                                                                   |
| `visual_key_distance`\[152\]             | \-0.5..0.5                    | The distance to the nearest key measured in cents                                                                                                                                                                                                                                                 | Key value widget                                                                                                                                                                   |
| `VuMeter`                                | default                       | Outputs the current instantaneous deck volume                                                                                                                                                                                                                                                     | Deck VU meter                                                                                                                                                                      |
| `VuMeterL`                               | default                       | Outputs the current instantaneous deck volume for the left channel                                                                                                                                                                                                                                | Deck VU meter L                                                                                                                                                                    |
| `VuMeterR`                               | default                       | Outputs the current instantaneous deck volume for the right channel                                                                                                                                                                                                                               | Deck VU meter R                                                                                                                                                                    |
| `waveform_zoom`\[153\]                   | 1.0 - 10.0                    | Zooms the waveform to look ahead or back as needed.                                                                                                                                                                                                                                               | Waveform zoom buttons                                                                                                                                                              |
| `waveform_zoom_up`\[154\]                | ?                             | Waveform Zoom Out                                                                                                                                                                                                                                                                                 | Waveform zoom buttons                                                                                                                                                              |
| `waveform_zoom_down`\[155\]              | ?                             | Waveform Zoom In                                                                                                                                                                                                                                                                                  | Waveform zoom buttons                                                                                                                                                              |
| `waveform_zoom_set_default`\[156\]       | ?                             | Return to default waveform zoom level                                                                                                                                                                                                                                                             | Waveform zoom buttons                                                                                                                                                              |
| `wheel`                                  | \-3.0..3.0                    | Affects relative play speed & direction persistently (additive offset & must manually be undone)                                                                                                                                                                                                  | Waveform                                                                                                                                                                           |

### `[SamplerN]`

Sample decks ("samplers") in Mixxx are identical to decks, they simply
have a different purpose (playing samples). Any control listed above for
`[ChannelN]` will work for a sampler, just replace `[ChannelN]` with
`[SamplerN]`.

| Key/Control                       | Range  | What it does                                                                                               | On-screen feedback                                            |
| --------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `[Samplers],show_samplers`        | binary |                                                                                                            | Shows Sampler bank(s)                                         |
| `[Sampler],SaveSamplerBank`\[157] | binary | Save sampler configuration. Make currently loaded tracks in samplers instantly available at a later point. | Opens file dialog. Configuration file can be named and saved. |
| `[Sampler],LoadSamplerBank`\[158] | binary | Load saved sampler configuration file and add tracks to the available samplers.                            | Opens file dialog. Select configuration file.                 |

### `[AuxiliaryN]`

You can map audio interface's inputs to mixxx's auxiliary input channels
and connect external audio source to it (cellphone, mp3 player). Then
you can use your midi controller to control its volume and some other
parameters (orientation, gain, volume), apply effects and use listen
function.

### `[PreviewDeckN]`

Preview decks in Mixxx are identical to regular decks. Any control
listed above for `[ChannelN]` will work for a preview deck, just replace
`[ChannelN]` with `[PreviewDeckN]`.

### `[VinylControl]`

| Key/Control     | Range  | What it does                                                                                                          | On-screen feedback                                                                                                                                                                                                                                                                                                                            |
| --------------- | ------ | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Toggle`\[159\] | binary | Moves control by a vinyl control signal from one deck to another if using the single deck vinyl control (VC) feature. | If VC isn't enabled on any decks, enable it on the first one we're receiving samples for. If VC is enabled on a single (exclusive) deck, and another deck is setup to receive samples, disable it on the former deck and enable it on the next eligible deck (ordered by deck number). If VC is enabled on multiple decks, don't do anything. |

### `[MicrophoneN]`

Below, *N*=2 up to the number of active microphones. e.g
`[Microphone2]`, for Mic \#1 just use \[Microphone\]\[160\].

| Key/Control            | Range         | What it does                                                                                                          | On-screen feedback              |
| ---------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `enabled`\[161\]       | binary        | 1 if a microphone input is enabled, 0 if not.                                                                         | Microphone is enabled.          |
| `orientation`\[162\]   | 0-2           | Set microphone orientation, 0 = left side of crossfader, 1 = center, 2 = right side of crossfader. Default is center. | N/A                             |
| `PeakIndicator`\[163\] | binary        | Indicates when the signal is clipping (too loud for the hardware and is being distorted)                              | Microphone Clip light           |
| `talkover`\[164\]      | binary        | Hold value at 1 to mix microphone input into the master output.                                                       | Talk button                     |
| `volume`\[165\]        | default       | Adjusts the microphone volume fader                                                                                   | Microphone volume fader changes |
| `pregain`              | 0.0..1.0..4.0 | Adjusts the gain of the mic input                                                                                     | Microphone gain knob            |
| `mute`\[166\]          | binary        | Mutes the channel                                                                                                     | Mute button                     |
| `VuMeter`\[167\]       | default       | Outputs the current instantaneous microphone volume                                                                   | Microphone VU meter changes     |

### `[Recording]`

| Key/Control          | Range         | What it does                                                                                                          | On-screen feedback              |
| -------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `toggle_recording`   | binary        | Turns recording on or off.                                                                                            | Recording icon                  |
| `status`             | 0-2           | Indicates whether Mixxx is currently recording: 0 = recording stopped, 1 = initialize recording, 2 = recording active | Recording icon                  |

### `[AutoDJ]`

| Key/Control               | Range  | What it does                                  | On-screen feedback                                 |
| ------------------------- | ------ | --------------------------------------------- | -------------------------------------------------- |
| `enabled`\[168\]          | binary | Turns Auto DJ on or off.                      | AutoDJ button                                      |
| `shuffle_playlist`\[169\] | binary | Shuffles the content of the Auto DJ playlist. | Order of tracks in the AutoDJ playlist changes.    |
| `skip_next`\[170\]        | binary | Skips the next track in the Auto DJ playlist. | Skipped track is removed from the AutoDJ playlist. |
| `fade_now`\[171\]         | binary | Triggers the transition to the next track.    | Crossfader slider moves to the other side.         |

### `[Library]`

| Key/Control                  | Range           | What it does                                                                                                                                                      | On-screen feedback                                         |
| ---------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `MoveUp`\[172\]              | Binary          | Equivalent to pressing the UP key on the keyboard                                                                                                                 | Currently selected item changes                            |
| `MoveDown`\[173\]            | Binary          | Equivalent to pressing the DOWN key on the keyboard                                                                                                               | Currently selected item changes                            |
| `MoveVertical`\[174\]        | Relative        | Move UP or DOWN the specified number of locations (negative for UP). Intended to be mapped to an encoder knob.                                                    | Currently selected item changes                            |
| `ScrollUp`\[175\]            | Binary          | Equivalent to pressing the PAGEUP key on the keyboard                                                                                                             | Currently selected item changes                            |
| `ScrollDown`\[176\]          | Binary          | Equivalent to pressing the PAGEDOWN key on the keyboard                                                                                                           | Currently selected item changes                            |
| `ScrollVertical`\[177\]      | Relative        | Scroll UP or DOWN the specified number of pages (negative for UP). Intended to be mapped to an encoder knob.                                                      | Currently selected item changes                            |
| `MoveLeft`\[178\]            | Binary          | Equivalent to pressing the LEFT key on the keyboard                                                                                                               | Currently selected item changes                            |
| `MoveRight`\[179\]           | Binary          | Equivalent to pressing the RIGHT key on the keyboard                                                                                                              | Currently selected item changes                            |
| `MoveHorizontal`\[180\]      | Relative        | Move LEFT or RIGHT the specified number of locations (negative for LEFT). Intended to be mapped to an encoder knob.                                               | Currently selected item changes                            |
| `MoveFocusForward`\[181\]    | Binary          | Equivalent to pressing the TAB key on the keyboard                                                                                                                | Currently focused pane changes                             |
| `MoveFocusBackward`\[182\]   | Binary          | Equivalent to pressing the SHIFT+TAB key on the keyboard                                                                                                          | Currently focused pane changes                             |
| `MoveFocus`\[183\]           | Relative        | Move focus forward or backwards the specified number of panes (negative for SHIFT+TAB). Intended to be mapped to an encoder knob.                                 | Currently focused pane changes                             |
| `GoToItem`\[184\]            | Binary          | Equivalent to double clicking the currently selected item                                                                                                         | Context dependent                                          |
| `AutoDjAddBottom`\[185\]     | Binary          | Add selected track(s) to Auto DJ Queue (bottom).                                                                                                                  | Append track(s) to Auto DJ playlist                        |
| `AutoDjAddTop`\[186\]        | Binary          | Add selected track(s) to Auto DJ Queue (top).                                                                                                                     | Prepend track(s) to Auto DJ playlist                       |
| `show_coverart`              | Binary          | Toggle the Cover Art in Library                                                                                                                                   |                                                            |
| `font_size_increment`\[187\] | Binary          | Increase the size of the library font. If the row height is smaller than the font-size the larger of the two is used.                                             | Library view                                               |
| `font_size_decrement`\[188\] | Binary          | Decrease the size of the library font                                                                                                                             | Library view                                               |
| `font_size_knob`\[189\]      | Relative        | Increase or decrease the size of the library font                                                                                                                 | Library view                                               |
| `sort_column`\[190\]         | See table below | Indicates the sorting column the track table                                                                                                                      | Sorting indicator in the column headers of the track table |
| `sort_column_toggle`\[191\]  | See table below | Equivalent to clicking on column headers. A new value sets sort\_column to that value and sort\_order to 0, setting the same value again will toggle sort\_order. | Sorting indicator in the column headers of the track table |
| `sort_order`\[192\]          | Binary          | Indicate the sort order of the track table (0 for ascending, 1 for descending)                                                                                    | Sorting indicator in the column headers of the track table |
| `track_color_prev`\[193\]    | Binary          | Set color of selected track to previous color in palette.                                                                                                         | Track color changes in the library view.                   |
| `track_color_next`\[194\]    | Binary          | Set color of selected track to next color in palette.                                                                                                             | Track color changes in the library view.                   |

#### Allowed values for sort\_column/sort\_column\_toggle

|       |                    | Availability |          |       |        |
| ----- | ------------------ | ------------ | -------- | ----- | ------ |
| Index | Description        | Library      | Playlist | Crate | Browse |
| 0     | Artist             | X            | X        | X     | X      |
| 1     | Title              | X            | X        | X     | X      |
| 2     | Album              | X            | X        | X     | X      |
| 3     | Albumartist        | X            | X        | X     | X      |
| 4     | Year               | X            | X        | X     | X      |
| 5     | Genre              | X            | X        | X     | X      |
| 6     | Composer           | X            | X        | X     | X      |
| 7     | Grouping           | X            | X        | X     | X      |
| 8     | Tracknumber        | X            | X        | X     | X      |
| 9     | Filetype           | X            | X        | X     | X      |
| 10    | Native Location    | X            | X        | X     | X      |
| 11    | Comment            | X            | X        | X     | X      |
| 12    | Duration           | X            | X        | X     | X      |
| 13    | Bitrate            | X            | X        | X     | X      |
| 14    | BPM                | X            | X        | X     | X      |
| 15    | ReplayGain         | X            | X        | X     | X      |
| 16    | Datetime Added     | X            | X        | X     | X      |
| 17    | Times Played       | X            | X        | X     | X      |
| 18    | Rating             | X            | X        | X     | X      |
| 19    | Key                | X            | X        | X     | X      |
| 20    | Preview            | X            | X        | X     | X      |
| 21    | Coverart           | X            | X        | X     |        |
| 22    | Position           |              | X        |       |        |
| 23    | Playlist ID        |              | X        |       |        |
| 24    | Location           |              | X        |       |        |
| 25    | Filename           |              |          |       | X      |
| 26    | File Modified Time |              |          |       | X      |
| 27    | File Creation Time |              |          |       | X      |

### `[Playlist]`

This group is going to be deprecated at some point, with its controls
added to `[Library]` above. (See [bug
\#1772184](https://bugs.launchpad.net/mixxx/+bug/1772184) for the
current status.)

| Key/Control       | Range          | What it does                                                                                                              | On-screen feedback            |
| ----------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `SelectPlaylist`  | relative value | Scrolls the given number of items (view, playlist, crate, etc.) in the side pane (can be negative for reverse direction). | Library sidebar highlight     |
| `SelectTrackKnob` | relative value | Scrolls the given number of tracks in the track table (can be negative for reverse direction).                            | Library track table highlight |

### `[Controls]`

| Key/Control               | Range  | What it does                                                                                                                                                                                                   | On-screen feedback |
| ------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `touch_shift`\[195\]      | binary | Once enabled, all touch tab events are interpreted as right click. This control has been added to provide touchscreen compatibility in 2.0 and might be replaced by a general modifier solution in the future. | All Widgets        |
| `AutoHotcueColors`\[196\] | binary | If enabled, colors will be assigned to newly created hot cue points automatically.                                                                                                                             | N/A                |

### Effects framework

The effects framework was introduced in Mixxx 2.0.

#### EffectRack Controls

| Group                                         | Key/Control                  | Range                | What it does                                                                                                                                                                                       |
| --------------------------------------------- | ---------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[EffectRack1]`                               | num\_effectunits             | integer, read-only   | The number of EffectUnits in this rack                                                                                                                                                             |
| `[EffectRack1]`                               | show                         | binary               | Show the Effect Rack                                                                                                                                                                               |

#### EffectUnit Controls
| Group                                         | Key/Control                  | Range                | What it does                                                                                                                                                                                       |
| --------------------------------------------- | ---------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[EffectRack1_EffectUnitN]`                   | chain\_selector              | \+1/-1               | Select EffectChain preset. \> 0 goes one forward; \< 0 goes one backward.                                                                                                                          |
| `[EffectRack1_EffectUnitN]`                   | clear                        | binary               | Clear the currently loaded EffectChain in this EffectUnit.                                                                                                                                         |
| `[EffectRack1_EffectUnitN]`                   | enabled                      | binary, default true | If true, the EffectChain in this EffectUnit will be processed. Meant to allow the user a quick toggle for the effect unit.                                                                         |
| `[EffectRack1_EffectUnitN]` \[197\]           | focused\_effect              | 0..num\_effects      | 0 indicates no effect is focused; \> 0 indicates the index of the focused effect. Focusing an effect only does something if a controller mapping changes how it behaves when an effect is focused. |
| `[EffectRack1_EffectUnitN]`                   | group\_\[ChannelI\]\_enable  | binary               | Whether or not this EffectChain applies to Deck I                                                                                                                                                  |
| `[EffectRack1_EffectUnitN]`                   | group\_\[Headphone\]\_enable | binary               | Whether or not this EffectChain applies to the Headphone output                                                                                                                                    |
| `[EffectRack1_EffectUnitN]`                   | group\_\[Master\]\_enable    | binary               | Whether or not this EffectChain applies to the Master output                                                                                                                                       |
| `[EffectRack1_EffectUnitN]`                   | group\_\[SamplerJ\]\_enable  | binary               | Whether or not this EffectChain applies to Sampler J                                                                                                                                               |
| `[EffectRack1_EffectUnitN]`                   | loaded                       | binary, read-only    | Whether an EffectChain is loaded into the EffectUnit                                                                                                                                               |
| `[EffectRack1_EffectUnitN]`                   | mix                          | 0.0..1.0             | The dry/wet mixing ratio for this EffectChain with the EngineChannels it is mixed with                                                                                                             |
| `[EffectRack1_EffectUnitN]`                   | next\_chain                  | binary               | Cycle to the next EffectChain preset after the currently loaded preset.                                                                                                                            |
| `[EffectRack1_EffectUnitN]`                   | num\_effects                 | integer, read-only   | The number of Effects that this EffectChain has                                                                                                                                                    |
| `[EffectRack1_EffectUnitN]`                   | num\_effectslots             | integer, read-only   | The number of effect slots available in this EffectUnit.                                                                                                                                           |
| `[EffectRack1_EffectUnitN]`                   | prev\_chain                  | binary               | Cycle to the previous EffectChain preset before the currently loaded preset.                                                                                                                       |
| `[EffectRack1_EffectUnitN]` \[198\]           | show\_focus                  | binary               | Whether to show focus buttons and draw a border around the focused effect in skins. This should not be manipulated by skins; it should only be changed by controller mappings.                     |
| `[EffectRack1_EffectUnitN]` \[199\]           | show\_parameters             | binary               | Whether to show all the parameters of each effect in skins or only show metaknobs.                                                                                                                 |
| `[EffectRack1_EffectUnitN]`                   | super1                       | 0.0..1.0             | The EffectChain superknob. Moves the metaknobs for each effect in the chain.                                                                                                                       |

#### Effect Controls

| Group                                         | Key/Control                  | Range                | What it does                                                                                                                                                                                       |
| --------------------------------------------- | ---------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[EffectRack1_EffectUnitN_EffectM]`           | clear                        | binary               | Clear the currently loaded Effect in this Effect slot from the EffectUnit.                                                                                                                         |
| `[EffectRack1_EffectUnitN_EffectM]`           | effect\_selector             | \+1/-1               | Select Effect -- \>0 goes one forward, \<0 goes one backward.                                                                                                                                      |
| `[EffectRack1_EffectUnitN_EffectM]`           | enabled                      | binary, default true | If true, the effect in this slot will be processed. Meant to allow the user a quick toggle for this effect.                                                                                        |
| `[EffectRack1_EffectUnitN_EffectM]`           | loaded                       | binary, read-only    | Whether an Effect is loaded into this EffectSlot                                                                                                                                                   |
| `[EffectRack1_EffectUnitN_EffectM]`           | next\_effect                 | binary               | Cycle to the next effect after the currently loaded effect.                                                                                                                                        |
| `[EffectRack1_EffectUnitN_EffectM]`           | num\_parameters              | integer, read-only   | The number of parameters the currently loaded effect has. 0 if no effect is loaded                                                                                                                 |
| `[EffectRack1_EffectUnitN_EffectM]`           | num\_parameterslots          | integer, read-only   | The number of parameter slots available.                                                                                                                                                           |
| `[EffectRack1_EffectUnitN_EffectM]`           | num\_button\_parameters      | integer, read-only   | The number of button parameters the currently loaded effect has. 0 if no effect is loaded                                                                                                          |
| `[EffectRack1_EffectUnitN_EffectM]`           | num\_button\_parameterslots  | integer, read-only   | The number of button parameter slots available.                                                                                                                                                    |
| `[EffectRack1_EffectUnitN_EffectM]` \[200\]   | meta                         | 0..1                 | Controls the parameters that are linked to the metaknob.                                                                                                                                           |
| `[EffectRack1_EffectUnitN_EffectM]`           | prev\_effect                 | binary               | Cycle to the previous effect before the currently loaded effect.                                                                                                                                   |

#### EffectParameter Controls

| Group                                         | Key/Control                  | Range                | What it does                                                                                                                                                                                       |
| --------------------------------------------- | ---------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[EffectRack1_EffectUnitN_EffectM]`           | parameterK                   | double               | The scaled value of the Kth parameter. See the [Parameter Values](https://github.com/mixxxdj/mixxx/wiki/Effects-Framework#parameter-values) section for more information.                                                                                                      |
| `[EffectRack1_EffectUnitN_EffectM]`           | parameterK\_link\_inverse    | bool                 | The link direction of the Kth parameter to the effect's metaknob.                                                                                                                                  |
| `[EffectRack1_EffectUnitN_EffectM]`           | parameterK\_link\_type       | enum                 | The link type of the Kth parameter to the effects's metaknob.                                                                                                                                      |
| `[EffectRack1_EffectUnitN_EffectM]`           | parameterK\_loaded           | binary, read-only    | Whether or not the Kth parameter slot has an effect parameter loaded into it.                                                                                                                      |
| `[EffectRack1_EffectUnitN_EffectM]`           | parameterK\_type             | integer, read-only   | The type of the Kth parameter value. See the Parameter Value Types table.                                                                                                                          |
| `[EffectRack1_EffectUnitN_EffectM]`           | button\_parameterK           | double               | The value of the Kth parameter. See the Parameter Values section for more information.                                                                                                             |
| `[EffectRack1_EffectUnitN_EffectM]`           | button\_parameterK\_loaded   | binary, read-only    | Whether or not the Kth parameter slot has an effect parameter loaded into it.                                                                                                                      |
| `[EffectRack1_EffectUnitN_EffectM]`           | button\_parameterK\_type     | integer, read-only   | The type of the Kth parameter value. See the Parameter Value Types table.                                                                                                                          |

In the above table,

  - EffectRack1 leaves room for future expansion to multiple
    EffectRacks.
  - N ranges from 1 to `[EffectRack1]`,num\_effectunits, inclusive.
  - M ranges from 1 to `[EffectRack1\_EffectUnitN]`,num\_effectslots,
    inclusive. (For a given value of N)
  - K ranges from 1 to
    `[EffectRack1\_EffectUnitN\_EffectM]`,num\_parameters, inclusive.
    (For given values of N and M)
  - I ranges from 1 to `[Master]`,num\_decks, inclusive.
  - J ranges from 1 to `[Master]`,num\_samplers, inclusive.

#### Linking Values

Effect parameters can be linked to the effect's metaknob. This linkage
can be user-controlled by changing the `link_type` and the
`link_inverse` control of the parameter. The default link type is loaded
from the effect parameter's manifest's `linkHint` property.

| Link Type         | Integer Value | Intepretation                                |
| ----------------- | ------------- | -------------------------------------------- |
| None              | 0             | Not controlled by the metaknob               |
| Linked            | 1             | Controlled by the metaknob as it is          |
| Linked Left       | 2             | Controlled by the left side of the metaknob  |
| Linked Right      | 3             | Controlled by the right side of the metaknob |
| Linked Left Right | 4             | Controlled by both sides of the metaknob     |

| Link Inverse | Integer Value | Intepretation                  |
| ------------ | ------------- | ------------------------------ |
| Normal       | 0             | Linked in equal relation       |
| Inverse      | 1             | Linked in an inverse relation. |

### EQs and filters

Starting in Mixxx 2.0, the equalizers and filter controls have been
moved to special [effects units](#effects-framework). The EQs are
controlled by `[EqualizerRack1_[ChannelN]_Effect1]` and the filter
knob is controlled by `[QuickEffectRack1_[ChannelN]]`,super1 and
`[QuickEffectRack1_[ChannelN]_Effect1],enabled`. Users can choose
between several options for the effects loaded in these racks in the
Equalizers section of the Preferences window.

### Deprecated controls

| `[Group]`    | Key/Control                        | Range                | What it does                                                                                                                                           | On-screen feedback                               | Replacement                                                                             |
| ------------ | ---------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ | --------------------------------------------------------------------------------------- |
| `[ChannelN]` | `beatloop`                         | positive real number | Setup a loop over the set number of beats.                                                                                                             | A loop is shown over the set number of beats.    | `beatloop_size` and `beatloop_toggle`                                                   |
| `[ChannelN]` | `jog`                              | \-3.0..3.0           | Affects relative play speed & direction for short instances (additive & is automatically reset to 0)                                                   | waveform                                         | [JavaScript engine.scratch functions](MIDI%20scripting#Scratching%20and%20jog%20wheels) |
| `[ChannelN]` | `reloop_exit`                      | binary               | Toggles the current loop on or off. If the loop is ahead of the current play position, the track will keep playing normally until it reaches the loop. | Loop range in waveform activates or deactivates. | `reloop_toggle`                                                                         |
| `[ChannelN]` | `scratch`                          | \-3.0..3.0           | Affects play speed & direction ([differently whether currently playing or not](https://bugs.launchpad.net/mixxx/+bug/530281)) (multiplicative)         | Waveform                                         | [JavaScript engine.scratch functions](MIDI%20scripting#Scratching%20and%20jog%20wheels) |
| `[ChannelN]` | `filter`\[201\],\[202\]            | binary               | Toggles the filter effect                                                                                                                              | Filter button                                    | [`[QuickEffectRack1_[ChannelN]_Effect1]],enabled`                                       |
| `[ChannelN]` | `filterDepth`\[203\],\[204\]       | default              | Adjusts the intensity of the filter effect                                                                                                             | Filter depth knob                                | [`[QuickEffectRack1_[ChannelN]],super1`                                                 |
| `[ChannelN]` | `filterLow`\[205\]                 | 0.0..1.0..4.0        | Adjusts the gain of the low EQ filter                                                                                                                  | LOW knob                                         | [`[EqualizerRack1_[ChannelN]_Effect1]],parameter1`                                      |
| `[ChannelN]` | `filterLowKill`\[206\]             | binary               | Holds the gain of the low EQ to -inf while active                                                                                                      | LOW kill knob                                    | [`[EqualizerRack1_[ChannelN]_Effect1]],button_parameter1`                               |
| `[ChannelN]` | `filterMid`\[207\]                 | 0.0..1.0..4.0        | Adjusts the gain of the mid EQ filter                                                                                                                  | MID knob                                         | [`[EqualizerRack1_[ChannelN]_Effect1]],parameter2`                                      |
| `[ChannelN]` | `filterMidKill`\[208\]             | binary               | Holds the gain of the mid EQ to -inf while active                                                                                                      | MID kill knob                                    | [`[EqualizerRack1_[ChannelN]_Effect1]],button_parameter2`                               |
| `[ChannelN]` | `filterHigh`\[209\]                | 0.0..1.0..4.0        | Adjusts the gain of the high EQ filter                                                                                                                 | HIGH knob                                        | [`[EqualizerRack1_[ChannelN]_Effect1]],parameter3`                                      |
| `[ChannelN]` | `filterHighKill`\[210\]            | binary               | Holds the gain of the high EQ to -inf while active                                                                                                     | HIGH kill knob                                   | [`[EqualizerRack1_[ChannelN]_Effect1]],button_parameter3`                               |
| `[Flanger]`  | `lfoDepth`\[211\]                  | default              | Adjusts the intensity of the flange effect                                                                                                             | Depth knob                                       | No direct replacement. See [Effects Framework](#effects-framework) section              |
| `[Flanger]`  | `lfoDelay`\[212\]                  | 50..10000            | Adjusts the phase delay of the flange effect in microseconds                                                                                           | Delay knob                                       | No direct replacement. See [Effects Framework](#effects-framework) section              |
| `[Flanger]`  | `lfoPeriod`\[213\]                 | 50000..2000000       | Adjusts the wavelength of the flange effect in microseconds                                                                                            | LFO knob                                         | No direct replacement. See [Effects Framework](#effects-framework) section              |
| `[ChannelN]` | `flanger`\[214\]                   | binary               | Toggles the flange effect                                                                                                                              | FLANGER button                                   | No direct replacement. See [Effects Framework](#effects-framework) section              |
| `[ChannelN]` | `beatloop_X`\[215\]                | toggle               | Setup a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                          | A loop is shown over X beats.                    | `[ChannelN],beatloop_X_activate`                                                        |
| `[ChannelN]` | `Hercules1`                        | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[ChannelN]` | `Hercules2`                        | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[ChannelN]` | `Hercules3`                        | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[ChannelN]` | `Hercules4`                        | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[ChannelN]` | `NextTask`                         | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[ChannelN]` | `NextTrack`                        | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[ChannelN]` | `PrevTask`                         | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[ChannelN]` | `PrevTrack`                        | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[ChannelN]` | `transform`                        | ?                    | deprecated                                                                                                                                             | ?                                                |                                                                                         |
| `[Master]`   | `headVolume`                       | 0.0..1.0..5.0        | adjust headphone volume                                                                                                                                | Headphone Gain knob                              | `[Master],headGain`                                                                     |
| `[Master]`   | `volume`                           | 0.0..1.0..5.0        | adjust master volume                                                                                                                                   | Master Gain knob                                 | `[Master],gain`                                                                         |
| `[Playlist]` | `LoadSelectedIntoFirstStopped`     | binary               | Loads the currently highlighted song into the first stopped deck                                                                                       | Waveform view                                    | `[Library],GoToItem`                                                                    |
| `[Playlist]` | `SelectNextPlaylist`               | binary               | Switches to the next view (Library, Queue, etc.)                                                                                                       | Library sidebar                                  | `[Library],MoveDown`                                                                    |
| `[Playlist]` | `SelectPrevPlaylist`               | binary               | Switches to the previous view (Library, Queue, etc.)                                                                                                   | Library sidebar                                  | `[Library],MoveUp`                                                                      |
| `[Playlist]` | `ToggleSelectedSidebarItem`\[216\] | binary               | Toggles (expands/collapses) the currently selected sidebar item.                                                                                       | Library sidebar                                  | `[Library],GoToItem`                                                                    |
| `[Playlist]` | `SelectNextTrack`                  | binary               | Scrolls to the next track in the track table.                                                                                                          | Library track table highlight                    | `[Library],MoveDown`                                                                    |
| `[Playlist]` | `SelectPrevTrack`                  | binary               | Scrolls to the previous track in the track table.                                                                                                      | Library track table highlight                    | `[Library],MoveUp`                                                                      |

1.  [GitHub PR \#2118 - Naming conventions for new
    controls](https://github.com/mixxxdj/mixxx/pull/2118#issuecomment-498126595)

2.  introduced in Mixxx v1.11.0

3.  introduced in Mixxx v1.11.0

4.  introduced in Mixxx v1.11.0

5.  introduced in Mixxx v1.11.0

6.  introduced in Mixxx v1.11.0

7.  introduced in Mixxx v1.11.0

8.  introduced in Mixxx v2.0.0

9.  introduced in Mixxx v2.0.0

10. introduced in Mixxx v2.0.0

11. introduced in Mixxx v2.1.0

12. introduced in Mixxx v2.1.0

13. introduced in Mixxx v1.10.0

14. introduced in Mixxx v1.10.0

15. introduced in Mixxx v2.0.0

16. introduced in Mixxx v2.0.0

17. introduced in Mixxx v2.0.0

18. introduced in Mixxx v2.0.0

19. introduced in Mixxx v2.0.0

20. introduced in Mixxx v2.0.0

21. introduced in Mixxx v2.0.0

22. introduced in Mixxx v1.9.0

23. introduced in Mixxx v2.1.0

24. introduced in Mixxx v1.9.0

25. introduced in Mixxx v1.11.0

26. introduced in Mixxx v2.0.0

27. changed in Mixxx v1.10.0

28. introduced in Mixxx v1.10.0

29. introduced in Mixxx v2.0.0

30. introduced in Mixxx v2.1.0

31. introduced in Mixxx v2.1.0

32. introduced in Mixxx v2.1.0

33. introduced in Mixxx v2.0.0

34. introduced in Mixxx v2.0.0

35. introduced in Mixxx v2.1.0

36. introduced in Mixxx v1.10.0

37. introduced in Mixxx v2.1.0

38. introduced in Mixxx v1.10.0

39. introduced in Mixxx v1.10.0

40. introduced in Mixxx v2.1.0

41. introduced in Mixxx v1.11.0

42. introduced in Mixxx v2.0.0

43. introduced in Mixxx v2.0.0

44. introduced in Mixxx v1.10.0

45. introduced in Mixxx v2.0.0

46. introduced in Mixxx v2.0.0

47. introduced in Mixxx v2.0.0

48. changed in Mixxx v1.10.0

49. introduced in Mixxx v1.10.0

50. introduced in Mixxx v1.10.0

51. introduced in Mixxx v1.9.0

52. changed in Mixxx v1.10.0

53. introduced in Mixxx v1.9.0

54. introduced in Mixxx v1.9.2

55. introduced in Mixxx v2.3.0

56. introduced in Mixxx v1.11.0

57. introduced in Mixxx v1.11.0

58. introduced in Mixxx v2.0.0

59. introduced in Mixxx v1.10.0

60. introduced in Mixxx v2.1.0

61. introduced in Mixxx v1.9.0

62. introduced in Mixxx v2.0.0

63. introduced in Mixxx v1.8.0

64. introduced in Mixxx v1.8.0

65. introduced in Mixxx v2.3.0

66. introduced in Mixxx v1.8.0

67. introduced in Mixxx v1.8.0

68. introduced in Mixxx v1.11.0

69. introduced in Mixxx v1.8.0

70. introduced in Mixxx v1.8.0

71. introduced in Mixxx v1.8.0

72. introduced in Mixxx v2.3.0

73. introduced in Mixxx v2.3.0

74. introduced in Mixxx v2.3.0

75. introduced in Mixxx v2.3.0

76. introduced in Mixxx v2.3.0

77. introduced in Mixxx v2.3.0

78. introduced in Mixxx v2.3.0

79. introduced in Mixxx v2.3.0

80. introduced in Mixxx v2.3.0

81. introduced in Mixxx v2.3.0

82. introduced in Mixxx v2.3.0

83. introduced in Mixxx v2.3.0

84. introduced in Mixxx v2.3.0

85. introduced in Mixxx v2.0.0

86. introduced in Mixxx v1.9.0

87. introduced in Mixxx v1.11.0

88. introduced in Mixxx v1.10.0

89. Changed in Mixxx v2.1.0

90. introduced in Mixxx v1.8.0

91. introduced in Mixxx v1.8.0

92. introduced in Mixxx v1.10.0

93. Changed in Mixxx v2.1.0

94. introduced in Mixxx v1.8.0

95. Changed in Mixxx v2.1.0

96. introduced in Mixxx v2.1.0

97. introduced in Mixxx v1.8.0

98. Changed in Mixxx v2.1.0

99. introduced in Mixxx v2.1.0

100. introduced in Mixxx v2.0.0

101. introduced in Mixxx v2.0.0

102. introduced in Mixxx v2.0.0

103. introduced in Mixxx v1.10.0

104. introduced in Mixxx v1.8.0

105. introduced in Mixxx v1.9.0

106. outroduced in Mixxx v2.3.0

107. outroduced in Mixxx v2.3.0

108. outroduced in Mixxx v2.3.0

109. outroduced in Mixxx v2.3.0

110. outroduced in Mixxx v2.3.0

111. outroduced in Mixxx v2.3.0

112. outroduced in Mixxx v2.3.0

113. outroduced in Mixxx v2.3.0

114. outroduced in Mixxx v2.3.0

115. outroduced in Mixxx v2.3.0

116. introduced in Mixxx v2.0.0

117. introduced in Mixxx v2.0.0

118. introduced in Mixxx v2.0.0

119. introduced in Mixxx v2.0.0

120. introduced in Mixxx v2.0.0

121. introduced in Mixxx v2.0.0

122. introduced in Mixxx v2.0.0

123. introduced in Mixxx v1.10.0

124. introduced in Mixxx v1.10.0

125. introduced in Mixxx v2.1.0

126. introduced in Mixxx v2.1.0

127. introduced in Mixxx v1.9.0

128. introduced in Mixxx v2.0.0

129. introduced in Mixxx v2.0.0

130. introduced in Mixxx v1.8.0

131. introduced in Mixxx v1.8.0

132. introduced in Mixxx v1.11.0

133. introduced in Mixxx v2.3.0

134. introduced in Mixxx v2.3.0

135. introduced in Mixxx v1.10.0

136. introduced in Mixxx v1.10.0

137. introduced in Mixxx v1.10.0

138. introduced in Mixxx v2.0.0

139. introduced in Mixxx v2.0.0

140. introduced in Mixxx v2.0.0

141. introduced in Mixxx v2.0.0

142. introduced in Mixxx v2.3.0

143. introduced in Mixxx v2.1.0

144. introduced in Mixxx v1.9.0

145. introduced in Mixxx v2.0.0

146. introduced in Mixxx v1.10.0

147. introduced in Mixxx v1.10.0

148. introduced in Mixxx v1.10.0

149. introduced in Mixxx v1.10.0

150. introduced in Mixxx v2.0.0

151. introduced in Mixxx v2.0.0

152. introduced in Mixxx v2.0.0

153. introduced in Mixxx v1.11.0

154. introduced in Mixxx v1.11.0

155. introduced in Mixxx v1.11.0

156. introduced in Mixxx v1.11.0

157. introduced in Mixxx v2.0.0

158. introduced in Mixxx v2.0.0

159. introduced in Mixxx v1.10.0

160. introduced in Mixxx v2.0.0

161. introduced in Mixxx v1.10.0

162. introduced in Mixxx v1.10.0

163. introduced in Mixxx v1.10.0

164. introduced in Mixxx v1.10.0

165. introduced in Mixxx v1.10.0

166. introduced in Mixxx v2.0.0

167. introduced in Mixxx v1.10.0

168. introduced in Mixxx v1.11.0

169. introduced in Mixxx v1.11.0

170. introduced in Mixxx v1.11.0

171. introduced in Mixxx v1.11.0

172. introduced in Mixxx v2.1.0

173. introduced in Mixxx v2.1.0

174. introduced in Mixxx v2.1.0

175. introduced in Mixxx v2.1.0

176. introduced in Mixxx v2.1.0

177. introduced in Mixxx v2.1.0

178. introduced in Mixxx v2.1.0

179. introduced in Mixxx v2.1.0

180. introduced in Mixxx v2.1.0

181. introduced in Mixxx v2.1.0

182. introduced in Mixxx v2.1.0

183. introduced in Mixxx v2.1.0

184. introduced in Mixxx v2.1.0

185. introduced in Mixxx v2.0.0

186. introduced in Mixxx v2.0.0

187. introduced in Mixxx v2.0.0

188. introduced in Mixxx v2.0.0

189. introduced in Mixxx v2.0.0

190. introduced in Mixxx v2.3.0

191. introduced in Mixxx v2.3.0

192. introduced in Mixxx v2.3.0

193. introduced in Mixxx v2.3.0

194. introduced in Mixxx v2.3.0

195. introduced in Mixxx v2.0.0

196. introduced in Mixxx v2.3.0

197. introduced in Mixxx v2.1.0

198. introduced in Mixxx v2.1.0

199. introduced in Mixxx v2.1.0

200. introduced in Mixxx v2.1.0

201. introduced in Mixxx v2.0.0

202. deprecated in Mixxx v2.0.0

203. introduced in Mixxx v2.0.0

204. deprecated in Mixxx v2.0.0

205. deprecated in Mixxx v2.0.0

206. deprecated in Mixxx v2.0.0

207. deprecated in Mixxx v2.0.0

208. deprecated in Mixxx v2.0.0

209. deprecated in Mixxx v2.0.0

210. deprecated in Mixxx v2.0.0

211. deprecated in Mixxx v2.0.0

212. deprecated in Mixxx v2.0.0

213. deprecated in Mixxx v2.0.0

214. deprecated in Mixxx v2.0.0

215. introduced in Mixxx v1.10.0

216. introduced in Mixxx v1.11.0
