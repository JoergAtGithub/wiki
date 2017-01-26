You can view the ControlObject connected to any part of a skin by
running Mixxx with the `--developer` command line option and hovering
your mouse cursor over part of the skin. If no tooltip appears, enable
tooltips for the Library and Skin in Options \> Preferences \>
Interface.

When running Mixxx in Developer Mode, you can manually set the state of
any ControlObject by going to Developer \> Developer Tools.

## List of Controls

The default range is 0.0 to 1.0, unless otherwise noted. Binary means
that it is either 'ON' (non-zero) or 'OFF' (zero).

*Please keep the controls in alphabetical order within each group.*

### \[Various\]

The following extensions add some features to ControlPotMeter controls
(volume, crossfader, ...). Use in conjunction with \[Channel*N*\],
\[Sampler*N*\], \[Master\] ... groups

|  | Key/Control            |  | Range   |  | What it does                                                                      |  | On-screen feedback                                                                              |  |
|  | ---------------------- |  | ------- |  | --------------------------------------------------------------------------------- |  | ----------------------------------------------------------------------------------------------- |  |
|  | \_up                   |  | default |  | Increases the value                                                               |  | e.g. "\[Channel*N*\],rate\_perm\_up" sets the speed one step higher (4 % default)               |  |
|  | \_down                 |  | default |  | Decreases the value                                                               |  | e.g. "\[Channel*N*\],rate\_perm\_down" sets the speed one step lower (4 % default)              |  |
|  | \_up\_small            |  | default |  | Increases the value by smaller step                                               |  | e.g. "\[Channel*N*\],rate\_perm\_up\_small" sets the speed one small step higher (1 % default)  |  |
|  | \_down\_small          |  | default |  | Decreases the value by smaller step                                               |  | e.g. "\[Channel*N*\],rate\_perm\_down\_small" sets the speed one small step lower (1 % default) |  |
|  | \_set\_one\[1\]        |  | default |  | Sets the value to 1.0                                                             |  | e.g. "\[Channel*N*\],volume\_set\_one" sets the channel volume to full                          |  |
|  | \_set\_minus\_one\[2\] |  | default |  | Sets the value to -1.0                                                            |  | e.g. "\[Channel*N*\],volume\_set\_minus\_one" sets the channel volume to zero                   |  |
|  | \_set\_default\[3\]    |  | default |  | Sets the control to its default                                                   |  | e.g. "\[Channel*N*\],waveform\_zoom\_set\_default" return to default waveform zoom level        |  |
|  | \_set\_zero\[4\]       |  | default |  | Sets the value to 0.0                                                             |  | e.g. "\[Master\],crossfader\_zero" put the crossfader in the middle again                       |  |
|  | \_toggle\[5\]          |  | default |  | Sets the value to 0.0 if the value was \> 0.0, and to 1.0 if the value was 0.0    |  | e.g. "\[Channel*N*\],volume\_toggle" will cut off/on a track while you're playing               |  |
|  | \_minus\_toggle\[6\]   |  | default |  | Sets the value to -1.0 if the value was \> -1.0, and to 1.0 if the value was -1.0 |  | e.g. "\[Master\],crossfader\_minus\_toggle" can tilt the crossfader from left to right          |  |

### \[Master\]

|  | Key/Control                          |  | Range          |  | What it does                                                                                                                                                        |  | On-screen feedback               |  |
|  | ------------------------------------ |  | -------------- |  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | -------------------------------- |  |
|  | audio\_latency\_usage\[7\]           |  | 0 .. 25 %      |  | Reflects fraction of latency, given by the audio buffer size, spend for audio processing inside Mixxx. At value near 25 % there is a high risk of buffer underflows |  | latency meter                    |  |
|  | audio\_latency\_overload\[8\]        |  | binary         |  | Indicates a buffer under or over-flow. Resets after 500 ms                                                                                                          |  | Overload indicator               |  |
|  | audio\_latency\_overload\_count\[9\] |  | 0 .. n         |  | Counts buffer over and under-flows. Max one per 500 ms                                                                                                              |  | Counter in hardware preferences  |  |
|  | balance                              |  | \-1.0..1.0     |  | Adjusts the left/right channel balance on the Master output                                                                                                         |  | Center Balance knob              |  |
|  | crossfader                           |  | \-1.0..1.0     |  | Adjusts the crossfader between players/decks (-1.0 is all the way left, Deck 1)                                                                                     |  | Crossfader slider                |  |
|  | crossfader\_down                     |  | binary         |  | Moves the crossfader left by 1/10th                                                                                                                                 |  | Crossfader slider                |  |
|  | crossfader\_down\_small\[10\]        |  | binary         |  | Moves the crossfader left by 1/100th                                                                                                                                |  | Crossfader slider                |  |
|  | crossfader\_up                       |  | binary         |  | Moves the crossfader right by 1/10th                                                                                                                                |  | Crossfader slider                |  |
|  | crossfader\_up\_small\[11\]          |  | binary         |  | Moves the crossfader right by 1/100th                                                                                                                               |  | Crossfader slider                |  |
|  | duckStrength\[12\]                   |  | 0.0..1.0       |  | Microphone ducking strength                                                                                                                                         |  | Strength knob                    |  |
|  | enabled\[13\]                        |  | binary         |  | Indicator that the master mix is processed                                                                                                                          |  | n/a                              |  |
|  | headEnabled\[14\]                    |  | binary         |  | Indicator that the headphone mix is processed                                                                                                                       |  | n/a                              |  |
|  | headVolume                           |  | 0.0..1.0..5.0  |  | Adjusts the headphone output volume                                                                                                                                 |  | Head Vol knob                    |  |
|  | headMix                              |  | \-1.0..1.0     |  | Adjusts the cue/main mix in the headphone output                                                                                                                    |  | Pre/Main knob                    |  |
|  | headSplit\[15\]                      |  | binary         |  | Splits headphone cueing into right = master mono and left = pfl mono.                                                                                               |  | Split Cue button                 |  |
|  | latency                              |  | absolute value |  | Latency setting (sound buffer size) in milliseconds (default 64)                                                                                                    |  | Latency slider in the prefs      |  |
|  | maximimze\_library\[16\]             |  | binary         |  | Toggle maximized view of library                                                                                                                                    |  | Toggle maximized view of library |  |
|  | num\_decks\[17\]                     |  | integer        |  | The number of decks currently enabled.                                                                                                                              |  | N/A                              |  |
|  | num\_samplers\[18\]                  |  | integer        |  | The number of samplers currently enabled.                                                                                                                           |  | N/A                              |  |
|  | num\_preview\_decks\[19\]            |  | integer        |  | The number of preview decks currently enabled.                                                                                                                      |  | N/A                              |  |
|  | PeakIndicator                        |  | binary         |  | Indicates when the signal is clipping (too loud for the hardware and is being distorted)                                                                            |  | Clip light                       |  |
|  | samplerate                           |  | absolute value |  | The current output sample rate in Hz (default 44100)                                                                                                                |  | (none)                           |  |
|  | talkoverDucking\[20\]                |  | FIXME          |  | Toggle microphone ducking mode (OFF, AUTO, MANUAL)                                                                                                                  |  | Ducking mode button              |  |
|  | volume                               |  | 0.0..1.0..5.0  |  | Adjusts the Master output volume                                                                                                                                    |  | Center Volume knob               |  |
|  | VuMeter                              |  | default        |  | Outputs the current instantaneous master volume (composite)                                                                                                         |  | Master meter (mono)              |  |
|  | VuMeterL                             |  | default        |  | Outputs the current instantaneous master volume for the left channel                                                                                                |  | Master meter L                   |  |
|  | VuMeterR                             |  | default        |  | Outputs the current instantaneous master volume for the right channel                                                                                               |  | Master meter R                   |  |

### \[ChannelN\]

Below, *N*=1 up to the number of active decks/samplers\[21\].

| Key/Control                              |  | Range                |  | What it does                                                                                                                                                                                                                                                                                      |  | On-screen feedback                                                                                                                                                           |  |
| ---------------------------------------- |  | -------------------- |  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| back                                     |  | binary               |  | Fast rewind (REW)                                                                                                                                                                                                                                                                                 |  | \< button                                                                                                                                                                    |  |
| beat\_active\[22\]                       |  | binary               |  | Indicates whether the player is currently positioned within 50 milliseconds of a beat or not.                                                                                                                                                                                                     |  | N/A                                                                                                                                                                          |  |
| beatjump\[23\]                           |  | real number          |  | Jump forward by X beats (positive) or backward by X beats (negative).                                                                                                                                                                                                                             |  | Player jumps forward or backward by X beats.                                                                                                                                 |  |
| beatjump\_X\_forward\[24\]               |  | binary               |  | Jump forward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                                                       |  | Player jumps forward by X beats.                                                                                                                                             |  |
| beatjump\_X\_backward\[25\]              |  | binary               |  | Jump backward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                                                      |  | Player jumps backward by X beats.                                                                                                                                            |  |
| beatloop\[26\]                           |  | positive real number |  | Setup a loop over the set number of beats.                                                                                                                                                                                                                                                        |  | A loop is shown over the set number of beats.                                                                                                                                |  |
| beatloop\_X\_activate\[27\]              |  | binary               |  | Activates a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                                                 |  | A loop is shown over X beats.                                                                                                                                                |  |
| beatloop\_X\_toggle\[28\]                |  | binary               |  | Toggles a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                                                   |  | A loop is shown over X beats.                                                                                                                                                |  |
| beatloop\_X\_enabled\[29\]               |  | binary               |  | 1 if beatloop X is enabled, 0 if not.                                                                                                                                                                                                                                                             |  | Beatloop X button in skin is lit.                                                                                                                                            |  |
| beatlooproll\_X\_activate\[30\]          |  | binary               |  | Activates a rolling loop over X beats. Once disabled, playback will resume where the track would have been if it had not entered the loop. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                     |  | Beatloop X button in skin is lit. A loop overlay is shown over X beats on waveform.                                                                                          |  |
| beats\_adjust\_faster\[31\]              |  | binary               |  | Adjust the average BPM up by +0.01                                                                                                                                                                                                                                                                |  | Beatgrid lines move closer to each other.                                                                                                                                    |  |
| beats\_adjust\_slower\[32\]              |  | binary               |  | Adjust the average BPM down by -0.01.                                                                                                                                                                                                                                                             |  | Beatgrid lines move further apart from each other.                                                                                                                           |  |
| beats\_translate\_curpos\[33\]           |  | binary               |  | Adjust beatgrid so closest beat is aligned with the current playposition.                                                                                                                                                                                                                         |  | Beatgrid moves to align with current playposition.                                                                                                                           |  |
| beats\_translate\_match\_alignment\[34\] |  | binary               |  | Adjust beatgrid to match another playing deck.                                                                                                                                                                                                                                                    |  | Instead of syncing the beatgrid to the current playposition, sync the beatgrid so the nearest beat lines up with the other track's nearest beat.                             |  |
| beats\_translate\_earlier\[35\]          |  | binary               |  | Move Beatgrid earlier                                                                                                                                                                                                                                                                             |  | Beatgrid moves left by a small amount.                                                                                                                                       |  |
| beats\_translate\_later\[36\]            |  | binary               |  | Move Beatgrid later                                                                                                                                                                                                                                                                               |  | Beatgrid moves right by a small amount.                                                                                                                                      |  |
| ~~beatsync~~                             |  | ~~binary~~           |  | ~~Syncs the BPM to that of the other track (if BPM is detected on both)~~                                                                                                                                                                                                                         |  | ~~SYNC button & Speed slider snaps to the appropriate value~~                                                                                                                |  |
| beatsync\[37\]                           |  | binary               |  | **changed behavior** Syncs the BPM and phase to that of the other track (if BPM is detected on both)                                                                                                                                                                                              |  | SYNC button & Speed slider snaps to the appropriate value                                                                                                                    |  |
| beatsync\_phase\[38\]                    |  | binary               |  | Syncs the phase to that of the other track (if BPM is detected on both)                                                                                                                                                                                                                           |  | SYNC button & Speed slider snaps to the appropriate value                                                                                                                    |  |
| beatsync\_tempo\[39\]                    |  | binary               |  | Syncs the BPM to that of the other track (if BPM is detected on both)                                                                                                                                                                                                                             |  | SYNC button & Speed slider snaps to the appropriate value                                                                                                                    |  |
| ~~bpm~~                                  |  | ~~absolute value~~   |  | ~~Reads or sets the track's current BPM (changing the pitch)~~                                                                                                                                                                                                                                    |  | ~~BPM value display~~                                                                                                                                                        |  |
| ~~bpm\[40\]~~                            |  | ~~real-valued~~      |  | ~~bpm now only reflects the bpm of the loaded track~~                                                                                                                                                                                                                                             |  | N/A                                                                                                                                                                          |  |
| bpm\[41\]                                |  | real-valued          |  | bpm reflects the perceived (rate-adjusted) BPM of the file loaded in ChannelN                                                                                                                                                                                                                     |  | BPM value display                                                                                                                                                            |  |
| ~~bpm\_tap\[42\]~~                       |  | ~~binary~~           |  | ~~When tapped repeatedly, adjusts the playback rate of ChannelN to match the tapped BPM~~                                                                                                                                                                                                         |  | ~~track playback rate shifts after 4 or more taps~~                                                                                                                          |  |
| bpm\_tap\[43\]                           |  | binary               |  | When tapped repeatedly, adjusts the BPM of ChannelN to match the tapped BPM                                                                                                                                                                                                                       |  | BPM value display (play speed doesn't change)                                                                                                                                |  |
| cue\_default                             |  | binary               |  | In CDJ mode, when playing, returns to the cue point & pauses. If stopped, sets a cue point at the current location. If stopped and at a cue point, plays from that point until released (set to 0.)                                                                                               |  | CUE button                                                                                                                                                                   |  |
| cue\_gotoandplay\[44\]                   |  | binary               |  | If the Cue point is set, seeks the player to it and starts playback.                                                                                                                                                                                                                              |  | Player may change position and start playing.                                                                                                                                |  |
| cue\_gotoandstop\[45\]                   |  | binary               |  | If the Cue point is set, seeks the player to it and stops.                                                                                                                                                                                                                                        |  | Player may change position.                                                                                                                                                  |  |
| cue\_indicator\[46\]                     |  | binary               |  | Provides information to be bound to the Cue Button e.g. blinking when next press will move the cue point                                                                                                                                                                                          |  | Cue button                                                                                                                                                                   |  |
| cue\_cdj\[47\]                           |  | binary               |  | Cue button, always in CDJ mode                                                                                                                                                                                                                                                                    |  | n/a                                                                                                                                                                          |  |
| cue\_play\[48\]                          |  | binary               |  | CUP button, Go to cue point and play after release. If stopped, sets a cue point at the current location.                                                                                                                                                                                         |  | n/a                                                                                                                                                                          |  |
| cue\_point                               |  | absolute value       |  | The current position of the cue point in samples                                                                                                                                                                                                                                                  |  | Cue point marker                                                                                                                                                             |  |
| cue\_preview                             |  | binary               |  | Plays from the current cue point                                                                                                                                                                                                                                                                  |  | CUE button lights & waveform moves                                                                                                                                           |  |
| cue\_set                                 |  | binary               |  | Sets a cue point at the current location                                                                                                                                                                                                                                                          |  | Cue mark appears on the waveform                                                                                                                                             |  |
| cue\_simple                              |  | binary               |  | If the player is not playing, set the cue point at the current location otherwise seek to the cue point.                                                                                                                                                                                          |  | CUE button                                                                                                                                                                   |  |
| duration                                 |  | absolute value       |  | Outputs the length of the current song in seconds                                                                                                                                                                                                                                                 |  | (none)                                                                                                                                                                       |  |
| eject\[49\]                              |  | binary               |  | Eject currently loaded track                                                                                                                                                                                                                                                                      |  | Eject button is lit. Be sure to set back to 0 with scripts so the button does not stay lit.                                                                                  |  |
| end                                      |  | binary               |  | Jump to end of track                                                                                                                                                                                                                                                                              |  | Track jumps to end                                                                                                                                                           |  |
| file\_bpm                                |  | positive value       |  | (Read-only) the detected BPM of the loaded track                                                                                                                                                                                                                                                  |  | N/A                                                                                                                                                                          |  |
| file\_key\[50\]                          |  | ?                    |  | (Read-only) the detected key of the loaded track                                                                                                                                                                                                                                                  |  | N/A                                                                                                                                                                          |  |
| fwd                                      |  | binary               |  | Fast forward (FF)                                                                                                                                                                                                                                                                                 |  | \> button                                                                                                                                                                    |  |
| hotcue\_X\_activate\[51\]                |  | binary               |  | If hotcue X is set, seeks the player to hotcue X's position. If hotcue X is not set, sets hotcue X to the current play position. To continue playing while any hotcues are activated, play must be set to 0, not 1.                                                                               |  | Player may change position. Hotcue X marker may change on waveform.                                                                                                          |  |
| hotcue\_X\_clear\[52\]                   |  | binary               |  | If hotcue X is set, clears its hotcue status.                                                                                                                                                                                                                                                     |  | Hotcue X marker changes on waveform.                                                                                                                                         |  |
| hotcue\_X\_enabled\[53\]                 |  | read-only, binary    |  | 1 if hotcue X is active, (position is not -1), 0 otherwise.                                                                                                                                                                                                                                       |  |                                                                                                                                                                              |  |
| hotcue\_X\_goto\[54\]                    |  | binary               |  | If hotcue X is set, seeks the player to hotcue X's position.                                                                                                                                                                                                                                      |  | Player may change position.                                                                                                                                                  |  |
| hotcue\_X\_gotoandplay\[55\]             |  | binary               |  | If hotcue X is set, seeks the player to hotcue X's position and starts playback.                                                                                                                                                                                                                  |  | Player may change position.                                                                                                                                                  |  |
| hotcue\_X\_gotoandstop\[56\]             |  | binary               |  | If hotcue X is set, seeks the player to hotcue X's position and stops.                                                                                                                                                                                                                            |  | Player may change position.                                                                                                                                                  |  |
| hotcue\_X\_position\[57\]                |  | positive integer     |  | The position of hotcue X in samples, -1 if not set.                                                                                                                                                                                                                                               |  | Hotcue X marker changes on waveform.                                                                                                                                         |  |
| hotcue\_X\_set\[58\]                     |  | binary               |  | Set hotcue X to the current play position. If hotcue X was previously set, clears its hotcue status.                                                                                                                                                                                              |  | Hotcue X marker changes on waveform.                                                                                                                                         |  |
| key\[59\]                                |  | real-valued          |  | Current key of the track                                                                                                                                                                                                                                                                          |  |                                                                                                                                                                              |  |
| keylock\[60\]                            |  | binary               |  | Enable key-lock for the specified deck (rate changes only affect tempo, not key)                                                                                                                                                                                                                  |  | key-lock button activates                                                                                                                                                    |  |
| LoadSelectedTrack                        |  | binary               |  | Loads the currently highlighted track into the deck                                                                                                                                                                                                                                               |  | Track name & waveform change                                                                                                                                                 |  |
| LoadSelectedTrackAndPlay\[61\]           |  | binary               |  | Loads the currently highlighted track into the deck and starts playing                                                                                                                                                                                                                            |  | Track name & waveform change & Play/pause button                                                                                                                             |  |
| loop\_double\[62\]                       |  | binary               |  | Doubles the current loop's length by moving the end marker. Must be set back to 0 after setting to 1 or the "+" button on screen will stay lit.                                                                                                                                                   |  | Loop length doubles on waveform                                                                                                                                              |  |
| loop\_enabled\[63\]                      |  | read-only, binary    |  | Indicates whether or not a loop is enabled. Read-only, do not set.                                                                                                                                                                                                                                |  | Loop in waveform is active.                                                                                                                                                  |  |
| loop\_end\_position\[64\]                |  | positive integer     |  | The player loop-out position in samples, -1 if not set.                                                                                                                                                                                                                                           |  | Loop-out marker shows on waveform.                                                                                                                                           |  |
| loop\_halve\[65\]                        |  | binary               |  | Halves the current loop's length by moving the end marker. Player immediately loops if past the new endpoint. Must be set back to 0 after setting to 1 or the "-" button on screen will stay lit.                                                                                                 |  | Loop length halves on waveform                                                                                                                                               |  |
| loop\_in\[66\]                           |  | binary               |  | Sets the player loop in position to the current play position.                                                                                                                                                                                                                                    |  | Loop-in marker changes on waveform.                                                                                                                                          |  |
| loop\_out\[67\]                          |  | binary               |  | Sets the player loop out position to the current play position.                                                                                                                                                                                                                                   |  | Loop-out marker changes on waveform.                                                                                                                                         |  |
| loop\_move\[68\]                         |  | real number          |  | Move loop forward by X beats (positive) or backward by X beats (negative).                                                                                                                                                                                                                        |  | Loop moves forward or backward by X beats.                                                                                                                                   |  |
| loop\_move\_X\_forward\[69\]             |  | binary               |  | Moves the loop in and out points forward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                           |  | Loop moves forward by X beats.                                                                                                                                               |  |
| loop\_move\_X\_backward\[70\]            |  | binary               |  | Loop moves by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                                                                                                                                                                         |  | Loop moves backward by X beats.                                                                                                                                              |  |
| loop\_scale\[71\]                        |  | 0.0 - infinity       |  | Scale the loop length by the value scale is set to by moving the end marker.                                                                                                                                                                                                                      |  | Loop length is scaled by given amount on waveform.                                                                                                                           |  |
| loop\_start\_position\[72\]              |  | positive integer     |  | The player loop-in position in samples, -1 if not set.                                                                                                                                                                                                                                            |  | Loop-in marker changes on waveform.                                                                                                                                          |  |
| orientation\[73\]                        |  | 0-2                  |  | Set channel's mix orientation, 0 = left side of crossfader, 1 = center, 2 = right side of crossfader                                                                                                                                                                                              |  | N/A                                                                                                                                                                          |  |
| passthrough\[74\]                        |  | binary               |  | Connects the vinyl control input for vinyl control on that deck to the channel output. Allows to mix external media into DJ sets.                                                                                                                                                                 |  | GUI control currently missing FIXME                                                                                                                                          |  |
| PeakIndicator                            |  | binary               |  | Indicates when the signal is clipping (too loud for the hardware and is being distorted)                                                                                                                                                                                                          |  | Clip light                                                                                                                                                                   |  |
| pfl                                      |  | binary               |  | Toggles headphone cueing                                                                                                                                                                                                                                                                          |  | Headphone button                                                                                                                                                             |  |
| pitch\[75\]                              |  | \-6.0..6.0           |  | Changes the track pitch independent of the tempo.                                                                                                                                                                                                                                                 |  | Key display                                                                                                                                                                  |  |
| pitch\_adjust\[76\]                      |  | \-3.0..3.0           |  | Adjust the pitch in addition to the speed slider pitch.                                                                                                                                                                                                                                           |  | Key display                                                                                                                                                                  |  |
| play                                     |  | binary               |  | Toggles playing or pausing the track. Feedback: 1.0 if track is playing or play command is adopted and track will be played after loading                                                                                                                                                         |  | Play/pause button                                                                                                                                                            |  |
| play\_indicator\[77\]                    |  | binary               |  | Provides information to be bound with the a Play/Pause button e.g blinking when play is possible                                                                                                                                                                                                  |  | Play/pause button                                                                                                                                                            |  |
| play\_stutter\[78\]                      |  | binary               |  | A play button without pause. Pushing while playing, starts play at cue point again (Stutter).                                                                                                                                                                                                     |  | Play/Stutter button                                                                                                                                                          |  |
| playposition                             |  | default              |  | Sets the absolute position in the track. The Range is -0.14 to 1.14 (0 = beginning -\> Midi 14, 1 = end -\> Midi 114)                                                                                                                                                                             |  | Waveform                                                                                                                                                                     |  |
| pregain                                  |  | 0.0..1.0..4.0        |  | Adjusts the pre-fader gain of the track (to avoid clipping)                                                                                                                                                                                                                                       |  | GAIN knob                                                                                                                                                                    |  |
| quantize\[79\]                           |  | binary               |  | Aligns Hot-cues and Loop In & Out to the next beat from the current position.                                                                                                                                                                                                                     |  | Hot-cues or Loop In/Out markers                                                                                                                                              |  |
| quantize\_beat\[80\]                     |  | deprecated           |  | ?                                                                                                                                                                                                                                                                                                 |  | Is used internally by CueControl (CUEs & Hotcues) and LoopingControl for quantization.                                                                                       |  |
| rate                                     |  | \-1.0..1.0           |  | Speed control                                                                                                                                                                                                                                                                                     |  | Speed slider                                                                                                                                                                 |  |
| rate\_dir                                |  | \-1 or 1             |  | indicates orientation of speed slider.                                                                                                                                                                                                                                                            |  | ?                                                                                                                                                                            |  |
| rate\_perm\_down                         |  | binary               |  | Sets the speed one step lower (4 % default) lower                                                                                                                                                                                                                                                 |  | Perm down button & Speed slider                                                                                                                                              |  |
| rate\_perm\_down\_small                  |  | binary               |  | Sets the speed one small step lower (1 % default)                                                                                                                                                                                                                                                 |  | Perm down button & Speed slider                                                                                                                                              |  |
| rate\_perm\_up                           |  | binary               |  | Sets the speed one step higher (4 % default)                                                                                                                                                                                                                                                      |  | Perm up button & Speed slider                                                                                                                                                |  |
| rate\_perm\_up\_small                    |  | binary               |  | Sets the speed one small step higher (1 % default)                                                                                                                                                                                                                                                |  | Perm up button & Speed slider                                                                                                                                                |  |
| rate\_temp\_down                         |  | binary               |  | Holds the speed one step lower while active                                                                                                                                                                                                                                                       |  | Temp down button & Speed slider                                                                                                                                              |  |
| rate\_temp\_down\_small                  |  | binary               |  | Holds the speed one small step lower while active                                                                                                                                                                                                                                                 |  | Temp down button & Speed slider                                                                                                                                              |  |
| rate\_temp\_up                           |  | binary               |  | Holds the speed one step higher while active                                                                                                                                                                                                                                                      |  | Temp up button & Speed slider                                                                                                                                                |  |
| rate\_temp\_up\_small                    |  | binary               |  | Holds the speed one small step higher while active                                                                                                                                                                                                                                                |  | Temp up button & Speed slider                                                                                                                                                |  |
| rateRange                                |  | 0.0..3.0             |  | Sets the range of the Speed slider (0.08 = 8%)                                                                                                                                                                                                                                                    |  | none, until you move the Speed slider                                                                                                                                        |  |
| rateEngine                               |  |                      |  | Actual rate (used in visuals, not for control)                                                                                                                                                                                                                                                    |  |                                                                                                                                                                              |  |
| reloop\_exit\[81\]                       |  | binary               |  | Toggles the current loop on or off.                                                                                                                                                                                                                                                               |  | Loop range in waveform activates or deactivates.                                                                                                                             |  |
| repeat\[82\]                             |  | binary               |  | Enable repeat-mode for the specified deck                                                                                                                                                                                                                                                         |  | when track finishes, song loops to beginning                                                                                                                                 |  |
| reset\_key\[83\]                         |  | binary               |  | Resets the key to the original track key.                                                                                                                                                                                                                                                         |  |                                                                                                                                                                              |  |
| reverse                                  |  | binary               |  | Toggles playing the track backwards                                                                                                                                                                                                                                                               |  | REV button                                                                                                                                                                   |  |
| reverseroll\[84\]                        |  | binary               |  | Enables reverse and slip mode while held (Censor)                                                                                                                                                                                                                                                 |  | REV button                                                                                                                                                                   |  |
| scratch2\[85\]                           |  | \-3.0..3.0           |  | Affects **absolute** play speed & direction whether currently playing or not when *scratch2\_enabled* is active. (multiplicative). Use [JavaScript engine.scratch functions](MIDI%20scripting#scratching) to manipulate in controller mappings.                                                   |  | Waveform                                                                                                                                                                     |  |
| scratch2\_enable\[86\]                   |  | binary               |  | Takes over play speed & direction for *scratch2*.                                                                                                                                                                                                                                                 |  | Waveform                                                                                                                                                                     |  |
| slip\_enabled\[87\]                      |  | binary               |  | Toggles slip mode. When active, the playback continues muted in the background during a loop, scratch etc. Once disabled, the audible playback will resume where the track would have been.                                                                                                       |  | GUI control currently missing FIXME                                                                                                                                          |  |
| start                                    |  | binary               |  | Jump to start of track                                                                                                                                                                                                                                                                            |  | Track jumps to start                                                                                                                                                         |  |
| start\_play\[88\]                        |  | binary               |  | Start playback from the beginning of the deck.                                                                                                                                                                                                                                                    |  | Deck plays from beginning                                                                                                                                                    |  |
| start\_stop\[89\]                        |  | binary               |  | Seeks a player to the start and then stops it.                                                                                                                                                                                                                                                    |  | Deck stops at the beginning                                                                                                                                                  |  |
| stop\[90\]                               |  | binary               |  | Stops a player.                                                                                                                                                                                                                                                                                   |  | Pause Button. Deck pauses at the current position                                                                                                                            |  |
| sync\_enabled\[91\]                      |  | binary               |  | Syncs the BPM and phase to that of the other track (if BPM is detected on both)                                                                                                                                                                                                                   |  | SYNC button & Speed slider snaps to the appropriate value                                                                                                                    |  |
| sync\_master\[92\]                       |  | binary               |  | Sets deck as master clock                                                                                                                                                                                                                                                                         |  |                                                                                                                                                                              |  |
| sync\_mode\[93\]                         |  | binary               |  | SYNC\_NONE = 0; SYNC\_FOLLOWER = 1; SYNC\_MASTER = 2,                                                                                                                                                                                                                                             |  |                                                                                                                                                                              |  |
| sync\_key\[94\]                          |  | ?                    |  | Match musical key                                                                                                                                                                                                                                                                                 |  | Key value widget                                                                                                                                                             |  |
| track\_loaded\[95\]                      |  | binary               |  | (Read-only) Whether a track is loaded in the specified deck                                                                                                                                                                                                                                       |  | Waveform and track metadata shown in deck                                                                                                                                    |  |
| track\_samplerate\[96\]                  |  | absolute value       |  | (Read-only) Sample rate of the track loaded on the specified deck                                                                                                                                                                                                                                 |  | n/a                                                                                                                                                                          |  |
| track\_samples                           |  | absolute value       |  | (Read-only) Number of sound samples in the track loaded on the specified deck                                                                                                                                                                                                                     |  | n/a                                                                                                                                                                          |  |
| volume                                   |  | default              |  | Adjusts the channel volume fader                                                                                                                                                                                                                                                                  |  | VOL fader                                                                                                                                                                    |  |
| mute\[97\]                               |  | binary               |  | Mutes the channel                                                                                                                                                                                                                                                                                 |  | Mute button                                                                                                                                                                  |  |
| vinylcontrol\_enabled\[98\]              |  | binary               |  | Toggles whether a deck is being controlled by digital vinyl                                                                                                                                                                                                                                       |  | When enabled, a vinyl indication should appear onscreen indicating green for Enabled                                                                                         |  |
| vinylcontrol\_cueing\[99\]               |  | 0.0-2.0              |  | Determines how cue points are treated in vinyl control Relative mode                                                                                                                                                                                                                              |  | Off - cue points ignored; One Cue - If needle is dropped after the cue point, track will seek to that cue point; hot cue - track will seek to nearest previous hot cue point |  |
| vinylcontrol\_mode\[100\]                |  | 0.0-2.0              |  | Determines how vinyl control interprets needle information: absolute mode - track position equals needle position and speed; relative mode - track speed equals needle speed regardless of needle position; constant mode - track speed equals last known-steady speed regardless of needle input |  | 3-way button indicates status                                                                                                                                                |  |
| vinylcontrol\_status\[101\]              |  | 0.0-3.0 (read-only)  |  | Provides visual feedback with regards to vinyl control status                                                                                                                                                                                                                                     |  | Off for control disabled, green for control enabled, blinking yellow for when the needle reaches the end of the record, and red for needle skip detected                     |  |
| visual\_bpm\[102\]                       |  | ?                    |  | BPM to display in the UI (updated more slowly than the actual bpm)                                                                                                                                                                                                                                |  | BPM value widget                                                                                                                                                             |  |
| visual\_key\[103\]                       |  | ?                    |  | Current musical key after pitch shifting to display in the UI using the notation selected in the preferences                                                                                                                                                                                      |  | Key value widget                                                                                                                                                             |  |
| visual\_key\_distance\[104\]             |  | \-0.5..0.5           |  | The distance to the nearest key measured in cents                                                                                                                                                                                                                                                 |  | Key value widget                                                                                                                                                             |  |
| VuMeter                                  |  | default              |  | Outputs the current instantaneous deck volume                                                                                                                                                                                                                                                     |  | Deck VU meter                                                                                                                                                                |  |
| VuMeterL                                 |  | default              |  | Outputs the current instantaneous deck volume for the left channel                                                                                                                                                                                                                                |  | Deck VU meter L                                                                                                                                                              |  |
| VuMeterR                                 |  | default              |  | Outputs the current instantaneous deck volume for the right channel                                                                                                                                                                                                                               |  | Deck VU meter R                                                                                                                                                              |  |
| waveform\_zoom\[105\]                    |  | 1.0 - 6.0            |  | Zooms the waveform to look ahead or back as needed.                                                                                                                                                                                                                                               |  | Waveform zoom buttons                                                                                                                                                        |  |
| waveform\_zoom\_up\[106\]                |  | ?                    |  | Waveform Zoom Out                                                                                                                                                                                                                                                                                 |  | Waveform zoom buttons                                                                                                                                                        |  |
| waveform\_zoom\_down\[107\]              |  | ?                    |  | Waveform Zoom In                                                                                                                                                                                                                                                                                  |  | Waveform zoom buttons                                                                                                                                                        |  |
| waveform\_zoom\_set\_default\[108\]      |  | ?                    |  | Return to default waveform zoom level                                                                                                                                                                                                                                                             |  | Waveform zoom buttons                                                                                                                                                        |  |
| wheel                                    |  | \-3.0..3.0           |  | Affects relative play speed & direction persistently (additive offset & must manually be undone)                                                                                                                                                                                                  |  | Waveform                                                                                                                                                                     |  |

### \[SamplerN\]

All Sampler controls are the same as for *Channel* above. Just replace
`[ChannelN]` with `[SamplerN]`.

|  | Key/Control                        |  | Range  |  | What it does                                                                                               |  | On-screen feedback                                            |  |
|  | ---------------------------------- |  | ------ |  | ---------------------------------------------------------------------------------------------------------- |  | ------------------------------------------------------------- |  |
|  | \[Sampler\],SaveSamplerBank\[109\] |  | binary |  | Save sampler configuration. Make currently loaded tracks in samplers instantly available at a later point. |  | Opens file dialog. Configuration file can be named and saved. |  |
|  | \[Sampler\],LoadSamplerBank\[110\] |  | binary |  | Load saved sampler configuration file and add tracks to the available samplers.                            |  | Opens file dialog. Select configuration file.                 |  |

### \[PreviewDeck\]

PreviewDeck controls are the same as for *Channel above*. Just replace
`[ChannelN]` with `[PreviewDeckN]`.

### \[VinylControl\]

|  | Key/Control   |  | Range  |  | What it does                                                                                                          |  | On-screen feedback                                                                                                                                                                                                                                                                                                                            |  |
|  | ------------- |  | ------ |  | --------------------------------------------------------------------------------------------------------------------- |  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
|  | Toggle\[111\] |  | binary |  | Moves control by a vinyl control signal from one deck to another if using the single deck vinyl control (VC) feature. |  | If VC isn't enabled on any decks, enable it on the first one we're receiving samples for. If VC is enabled on a single (exclusive) deck, and another deck is setup to receive samples, disable it on the former deck and enable it on the next eligible deck (ordered by deck number). If VC is enabled on multiple decks, don't do anything. |  |

### \[MicrophoneN\]

Below, *N*=2 up to the number of active microphones. e.g
\[Microphone2\], for Mic \#1 just use \[Microphone\]\[112\].

|  | Key/Control          |  | Range         |  | What it does                                                                                                          |  | On-screen feedback              |  |
|  | -------------------- |  | ------------- |  | --------------------------------------------------------------------------------------------------------------------- |  | ------------------------------- |  |
|  | enabled\[113\]       |  | binary        |  | 1 if a microphone input is enabled, 0 if not.                                                                         |  | Microphone is enabled.          |  |
|  | orientation\[114\]   |  | 0-2           |  | Set microphone orientation, 0 = left side of crossfader, 1 = center, 2 = right side of crossfader. Default is center. |  | N/A                             |  |
|  | PeakIndicator\[115\] |  | binary        |  | Indicates when the signal is clipping (too loud for the hardware and is being distorted)                              |  | Microphone Clip light           |  |
|  | talkover\[116\]      |  | binary        |  | Hold value at 1 to mix microphone input into the master output.                                                       |  | Talk button                     |  |
|  | volume\[117\]        |  | default       |  | Adjusts the microphone volume fader                                                                                   |  | Microphone volume fader changes |  |
|  | pregain              |  | 0.0..1.0..4.0 |  | Adjusts the gain of the mic input                                                                                     |  | Microphone gain knob            |  |
|  | mute\[118\]          |  | binary        |  | Mutes the channel                                                                                                     |  | Mute button                     |  |
|  | VuMeter\[119\]       |  | default       |  | Outputs the current instantaneous microphone volume                                                                   |  | Microphone VU meter changes     |  |

### \[Recording\]

|  | Key/Control       |  | Range  |  | What it does                                    |  | On-screen feedback |  |
|  | ----------------- |  | ------ |  | ----------------------------------------------- |  | ------------------ |  |
|  | toggle\_recording |  | binary |  | Turns recording on or off.                      |  | Recording icon     |  |
|  | status            |  | binary |  | Indicates whether Mixxx is currently recording. |  | Recording icon     |  |

### \[AutoDJ\]

|  | Key/Control              |  | Range  |  | What it does                                  |  | On-screen feedback                                 |  |
|  | ------------------------ |  | ------ |  | --------------------------------------------- |  | -------------------------------------------------- |  |
|  | enabled\[120\]           |  | binary |  | Turns Auto DJ on or off.                      |  | AutoDJ button                                      |  |
|  | shuffle\_playlist\[121\] |  | binary |  | Shuffles the content of the Auto DJ playlist. |  | Order of tracks in the AutoDJ playlist changes.    |  |
|  | skip\_next\[122\]        |  | binary |  | Skips the next track in the Auto DJ playlist. |  | Skipped track is removed from the AutoDJ playlist. |  |
|  | fade\_now\[123\]         |  | binary |  | Triggers the transition to the next track.    |  | Crossfader slider moves to the other side.         |  |

### \[Library\]

| Key/Control                  |  | Range    |  | What it does                                                                                                                      |  | On-screen feedback                   |  |
| ---------------------------- |  | -------- |  | --------------------------------------------------------------------------------------------------------------------------------- |  | ------------------------------------ |  |
| MoveUp\[124\]                |  | Binary   |  | Equivalent to pressing the UP key on the keyboard                                                                                 |  | Currently selected item changes      |  |
| MoveDown\[125\]              |  | Binary   |  | Equivalent to pressing the DOWN key on the keyboard                                                                               |  | Currently selected item changes      |  |
| MoveVertical\[126\]          |  | Relative |  | Move UP or DOWN the specified number of locations (negative for UP). Intended to be mapped to an encoder knob.                    |  | Currently selected item changes      |  |
| ScrollUp\[127\]              |  | Binary   |  | Equivalent to pressing the PAGEUP key on the keyboard                                                                             |  | Currently selected item changes      |  |
| ScrollDown\[128\]            |  | Binary   |  | Equivalent to pressing the PAGEDOWN key on the keyboard                                                                           |  | Currently selected item changes      |  |
| ScrollVertical\[129\]        |  | Relative |  | Scroll UP or DOWN the specified number of pages (negative for UP). Intended to be mapped to an encoder knob.                      |  | Currently selected item changes      |  |
| MoveLeft\[130\]              |  | Binary   |  | Equivalent to pressing the LEFT key on the keyboard                                                                               |  | Currently selected item changes      |  |
| MoveRight\[131\]             |  | Binary   |  | Equivalent to pressing the RIGHT key on the keyboard                                                                              |  | Currently selected item changes      |  |
| MoveHorizontal\[132\]        |  | Relative |  | Move LEFT or RIGHT the specified number of locations (negative for LEFT). Intended to be mapped to an encoder knob.               |  | Currently selected item changes      |  |
| MoveFocusForward\[133\]      |  | Binary   |  | Equivalent to pressing the TAB key on the keyboard                                                                                |  | Currently focused pane changes       |  |
| MoveFocusBackward\[134\]     |  | Binary   |  | Equivalent to pressing the SHIFT+TAB key on the keyboard                                                                          |  | Currently focused pane changes       |  |
| MoveFocus\[135\]             |  | Relative |  | Move focus forward or backwards the specified number of panes (negative for SHIFT+TAB). Intended to be mapped to an encoder knob. |  | Currently focused pane changes       |  |
| ChooseItem\[136\]            |  | Binary   |  | Equivalent to double clicking the currently selected item                                                                         |  | Context dependent                    |  |
| AutoDjAddBottom\[137\]       |  | Binary   |  | Add selected track(s) to Auto DJ Queue (bottom).                                                                                  |  | Append track(s) to Auto DJ playlist  |  |
| AutoDjAddTop\[138\]          |  | Binary   |  | Add selected track(s) to Auto DJ Queue (top).                                                                                     |  | Prepend track(s) to Auto DJ playlist |  |
| font\_size\_increment\[139\] |  | Binary   |  | Increase the size of the library font. If the row height is smaller than the font-size the larger of the two is used.             |  | Library view                         |  |
| font\_size\_decrement\[140\] |  | Binary   |  | Decrease the size of the library font                                                                                             |  | Library view                         |  |
| font\_size\_knob\[141\]      |  | Relative |  | Increase or decrease the size of the library font                                                                                 |  | Library view                         |  |

### \[Controls\]

|  | Key/Control         |  | Range  |  | What it does                                                                                                                                                                                           |  | On-screen feedback |  |
|  | ------------------- |  | ------ |  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |  | ------------------ |  |
|  | touch\_shift\[142\] |  | binary |  | Once enabled, all touch tab events are interpreted as right click. This control has been added to provide touchscreen compatibility in 2.0 and might be replaced by a general modifier solution in 2.1 |  | All Widgets        |  |

### Effects framework

The effects framework was introduced in Mixxx 2.0.

| EffectRack Controls                           |  |                              |  |                      |  |                                                                                                                                                                                                    |  |
| --------------------------------------------- |  | ---------------------------- |  | -------------------- |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| \[Group\]                                     |  | Key/Control                  |  | Range                |  | What it does                                                                                                                                                                                       |  |
| \[EffectRack1\]                               |  | num\_effectunits             |  | integer, read-only   |  | The number of EffectUnits in this rack                                                                                                                                                             |  |
| EffectUnit Controls                           |  |                              |  |                      |  |                                                                                                                                                                                                    |  |
| \[Group\]                                     |  | Key/Control                  |  | Range                |  | What it does                                                                                                                                                                                       |  |
| \[EffectRack1\_EffectUnitN\]                  |  | chain\_selector              |  | \+1/-1               |  | Select EffectChain preset. \> 0 goes one forward; \< 0 goes one backward.                                                                                                                          |  |
| \[EffectRack1\_EffectUnitN\]                  |  | clear                        |  | binary               |  | Clear the currently loaded EffectChain in this EffectUnit.                                                                                                                                         |  |
| \[EffectRack1\_EffectUnitN\]                  |  | enabled                      |  | binary, default true |  | If true, the EffectChain in this EffectUnit will be processed. Meant to allow the user a quick toggle for the effect unit.                                                                         |  |
| \[EffectRack1\_EffectUnitN\] \[143\]          |  | focused\_effect              |  | 0..num\_effects      |  | 0 indicates no effect is focused; \>0 indicates the number of the focused effect. Focusing an effect only does something if a controller mapping changes how it behaves when an effect is focused. |  |
| \[EffectRack1\_EffectUnitN\]                  |  | group\_\[ChannelI\]\_enable  |  | binary               |  | Whether or not this EffectChain applies to Deck I                                                                                                                                                  |  |
| \[EffectRack1\_EffectUnitN\]                  |  | group\_\[Headphone\]\_enable |  | binary               |  | Whether or not this EffectChain applies to the Headphone output                                                                                                                                    |  |
| \[EffectRack1\_EffectUnitN\]                  |  | group\_\[Master\]\_enable    |  | binary               |  | Whether or not this EffectChain applies to the Master output                                                                                                                                       |  |
| \[EffectRack1\_EffectUnitN\]                  |  | group\_\[SamplerJ\]\_enable  |  | binary               |  | Whether or not this EffectChain applies to Sampler J                                                                                                                                               |  |
| \[EffectRack1\_EffectUnitN\]                  |  | loaded                       |  | binary, read-only    |  | Whether an EffectChain is loaded into the EffectUnit                                                                                                                                               |  |
| \[EffectRack1\_EffectUnitN\]                  |  | mix                          |  | 0.0..1.0             |  | The dry/wet mixing ratio for this EffectChain with the EngineChannels it is mixed with                                                                                                             |  |
| \[EffectRack1\_EffectUnitN\]                  |  | next\_chain                  |  | binary               |  | Cycle to the next EffectChain preset after the currently loaded preset.                                                                                                                            |  |
| \[EffectRack1\_EffectUnitN\]                  |  | num\_effects                 |  | integer, read-only   |  | The number of Effects that this EffectChain has                                                                                                                                                    |  |
| \[EffectRack1\_EffectUnitN\]                  |  | num\_effectslots             |  | integer, read-only   |  | The number of effect slots available in this EffectUnit.                                                                                                                                           |  |
| \[EffectRack1\_EffectUnitN\]                  |  | prev\_chain                  |  | binary               |  | Cycle to the previous EffectChain preset before the currently loaded preset.                                                                                                                       |  |
| \[EffectRack1\_EffectUnitN\] \[144\]          |  | show\_focus                  |  | binary               |  | Whether to show focus buttons and draw a border around the focused effect in skins. This should not be manipulated by skins; it should only be changed by controller mappings.                     |  |
| \[EffectRack1\_EffectUnitN\] \[145\]          |  | show\_parameters             |  | binary               |  | Whether to show all the parameters of each effect in skins or only show metaknobs.                                                                                                                 |  |
| \[EffectRack1\_EffectUnitN\]                  |  | super1                       |  | 0.0..1.0             |  | The EffectChain superknob. Moves the metaknobs for each effect in the chain.                                                                                                                       |  |
| Effect Controls                               |  |                              |  |                      |  |                                                                                                                                                                                                    |  |
| \[Group\]                                     |  | Key/Control                  |  | Range                |  | What it does                                                                                                                                                                                       |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | clear                        |  | binary               |  | Clear the currently loaded Effect in this Effect slot from the EffectUnit.                                                                                                                         |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | effect\_selector             |  | \+1/-1               |  | Select Effect -- \>0 goes one forward, \<0 goes one backward.                                                                                                                                      |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | enabled                      |  | binary, default true |  | If true, the effect in this slot will be processed. Meant to allow the user a quick toggle for this effect.                                                                                        |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | loaded                       |  | binary, read-only    |  | Whether an Effect is loaded into this EffectSlot                                                                                                                                                   |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | next\_effect                 |  | binary               |  | Cycle to the next effect after the currently loaded effect.                                                                                                                                        |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | num\_parameters              |  | integer, read-only   |  | The number of parameters the currently loaded effect has. 0 if no effect is loaded                                                                                                                 |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | num\_parameterslots          |  | integer, read-only   |  | The number of parameter slots available.                                                                                                                                                           |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | num\_button\_parameters      |  | integer, read-only   |  | The number of button parameters the currently loaded effect has. 0 if no effect is loaded                                                                                                          |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | num\_button\_parameterslots  |  | integer, read-only   |  | The number of button parameter slots available.                                                                                                                                                    |  |
| \[EffectRack1\_EffectUnitN\_EffectM\] \[146\] |  | meta                         |  | 0-1                  |  | Controls the parameters that are linked to the metaknob.                                                                                                                                           |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | prev\_effect                 |  | binary               |  | Cycle to the previous effect before the currently loaded effect.                                                                                                                                   |  |
| EffectParameter Controls                      |  |                              |  |                      |  |                                                                                                                                                                                                    |  |
| \[Group\]                                     |  | Key/Control                  |  | Range                |  | What it does                                                                                                                                                                                       |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | parameterK                   |  | double               |  | The scaled value of the Kth parameter. See the Parameter Values section for more information.                                                                                                      |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | parameterK\_link\_inverse    |  | bool                 |  | The link direction of the Kth parameter to the effect's metaknob.                                                                                                                                  |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | parameterK\_link\_type       |  | enum                 |  | The link type of the Kth parameter to the effects's metaknob.                                                                                                                                      |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | parameterK\_loaded           |  | binary, read-only    |  | Whether or not the Kth parameter slot has an effect parameter loaded into it.                                                                                                                      |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | parameterK\_type             |  | integer, read-only   |  | The type of the Kth parameter value. See the Parameter Value Types table.                                                                                                                          |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | button\_parameterK           |  | double               |  | The value of the Kth parameter. See the Parameter Values section for more information.                                                                                                             |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | button\_parameterK\_loaded   |  | binary, read-only    |  | Whether or not the Kth parameter slot has an effect parameter loaded into it.                                                                                                                      |  |
| \[EffectRack1\_EffectUnitN\_EffectM\]         |  | button\_parameterK\_type     |  | integer, read-only   |  | The type of the Kth parameter value. See the Parameter Value Types table.                                                                                                                          |  |

In the above table,

  - EffectRack1 leaves room for future expansion to multiple
    EffectRacks.
  - N ranges from 1 to \[EffectRack1\],num\_effectunits, inclusive. 
  - M ranges from 1 to \[EffectRack1\_EffectUnitN\],num\_effectslots,
    inclusive. (For a given value of N)
  - K ranges from 1 to
    \[EffectRack1\_EffectUnitN\_EffectM\],num\_parameters, inclusive.
    (For given values of N and M)
  - I ranges from 1 to \[Master\],num\_decks, inclusive.
  - J ranges from 1 to \[Master\],num\_samplers, inclusive.

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
controlled by \[EqualizerRack1\_\[Channel*N*\]\_Effect1\] and the filter
knob is controlled by \[QuickEffectRack1\_\[Channel*N*\]\]. Users can
choose between several options for the effects loaded in these racks in
the Equalizers section of the Preferences window.

### Deprecated controls

| \[Group\]      |  | Key/Control                      |  | Range          |  | What it does                                                                                                                                   |  | On-screen feedback            |  | Replacement                                                                         |  |
| -------------- |  | -------------------------------- |  | -------------- |  | ---------------------------------------------------------------------------------------------------------------------------------------------- |  | ----------------------------- |  | ----------------------------------------------------------------------------------- |  |
| \[Channel*N*\] |  | jog                              |  | \-3.0..3.0     |  | Affects relative play speed & direction for short instances (additive & is automatically reset to 0)                                           |  | waveform                      |  | [JavaScript engine.scratch functions](MIDI%20scripting#scratching)                  |  |
| \[Channel*N*\] |  | scratch                          |  | \-3.0..3.0     |  | Affects play speed & direction ([differently whether currently playing or not](https://bugs.launchpad.net/mixxx/+bug/530281)) (multiplicative) |  | Waveform                      |  | [JavaScript engine.scratch functions](MIDI%20scripting#scratching)                  |  |
| \[Channel*N*\] |  | filter\[147\],\[148\]            |  | binary         |  | Toggles the filter effect                                                                                                                      |  | Filter button                 |  | [\[QuickEffectRack1\_\[ChannelN](#effects-framework)\], enabled                     |  |
| \[Channel*N*\] |  | filterDepth\[149\],\[150\]       |  | default        |  | Adjusts the intensity of the filter effect                                                                                                     |  | Filter depth knob             |  | [\[QuickEffectRack1\_\[ChannelN](#effects-framework)\], super1                      |  |
| \[Channel*N*\] |  | filterLow\[151\]                 |  | 0.0..1.0..4.0  |  | Adjusts the gain of the low EQ filter                                                                                                          |  | LOW knob                      |  | [\[EqualizerRack1\_\[ChannelN\]\_Effect1](#effects-framework)\], parameter1         |  |
| \[Channel*N*\] |  | filterLowKill\[152\]             |  | binary         |  | Holds the gain of the low EQ to -inf while active                                                                                              |  | LOW kill knob                 |  | [\[EqualizerRack1\_\[ChannelN\]\_Effect1](#effects-framework)\], button\_parameter1 |  |
| \[Channel*N*\] |  | filterMid\[153\]                 |  | 0.0..1.0..4.0  |  | Adjusts the gain of the mid EQ filter                                                                                                          |  | MID knob                      |  | [\[EqualizerRack1\_\[ChannelN\]\_Effect1](#effects-framework)\], parameter2         |  |
| \[Channel*N*\] |  | filterMidKill\[154\]             |  | binary         |  | Holds the gain of the mid EQ to -inf while active                                                                                              |  | MID kill knob                 |  | [\[EqualizerRack1\_\[ChannelN\]\_Effect1](#effects-framework)\], button\_parameter2 |  |
| \[Channel*N*\] |  | filterHigh\[155\]                |  | 0.0..1.0..4.0  |  | Adjusts the gain of the high EQ filter                                                                                                         |  | HIGH knob                     |  | [\[EqualizerRack1\_\[ChannelN\]\_Effect1](#effects-framework)\], parameter3         |  |
| \[Channel*N*\] |  | filterHighKill\[156\]            |  | binary         |  | Holds the gain of the high EQ to -inf while active                                                                                             |  | HIGH kill knob                |  | [\[EqualizerRack1\_\[ChannelN\]\_Effect1](#effects-framework)\], button\_parameter3 |  |
| \[Flanger\]    |  | lfoDepth\[157\]                  |  | default        |  | Adjusts the intensity of the flange effect                                                                                                     |  | Depth knob                    |  | No direct replacement. See [\#effects frameworks](#effects%20frameworks) section    |  |
| \[Flanger\]    |  | lfoDelay\[158\]                  |  | 50..10000      |  | Adjusts the phase delay of the flange effect in microseconds                                                                                   |  | Delay knob                    |  | No direct replacement. See [\#effects frameworks](#effects%20frameworks) section    |  |
| \[Flanger\]    |  | lfoPeriod\[159\]                 |  | 50000..2000000 |  | Adjusts the wavelength of the flange effect in microseconds                                                                                    |  | LFO knob                      |  | No direct replacement. See [\#effects frameworks](#effects%20frameworks) section    |  |
| \[Channel*N*\] |  | flanger\[160\]                   |  | binary         |  | Toggles the flange effect                                                                                                                      |  | FLANGER button                |  | No direct replacement. See [\#effects frameworks](#effects%20frameworks) section    |  |
| \[Channel*N*\] |  | beatloop\_X\[161\]               |  | toggle         |  | Setup a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64                                  |  | A loop is shown over X beats. |  | \[Channel*N*\], beatloop\_X\_activate                                               |  |
| \[Channel*N*\] |  | Hercules1                        |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Channel*N*\] |  | Hercules2                        |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Channel*N*\] |  | Hercules3                        |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Channel*N*\] |  | Hercules4                        |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Channel*N*\] |  | NextTask                         |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Channel*N*\] |  | NextTrack                        |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Channel*N*\] |  | PrevTask                         |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Channel*N*\] |  | PrevTrack                        |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Channel*N*\] |  | transform                        |  | ?              |  | deprecated                                                                                                                                     |  | ?                             |  |                                                                                     |  |
| \[Playlist\]   |  | LoadSelectedIntoFirstStopped     |  | binary         |  | Loads the currently highlighted song into the first stopped deck                                                                               |  | Waveform view                 |  | \[Library\] ChooseItem                                                              |  |
| \[Playlist\]   |  | SelectNextPlaylist               |  | binary         |  | Switches to the next view (Library, Queue, etc.)                                                                                               |  | Library sidebar               |  | \[Library\] MoveDown                                                                |  |
| \[Playlist\]   |  | SelectPrevPlaylist               |  | binary         |  | Switches to the previous view (Library, Queue, etc.)                                                                                           |  | Library sidebar               |  | \[Library\] MoveUp                                                                  |  |
| \[Playlist\]   |  | SelectPlaylist                   |  | relative value |  | Scrolls the given number of items (view, playlist, crate, etc.) in the side pane (can be negative for reverse direction).                      |  | Library sidebar               |  |                                                                                     |  |
| \[Playlist\]   |  | ToggleSelectedSidebarItem\[162\] |  | binary         |  | Toggles (expands/collapses) the currently selected sidebar item.                                                                               |  | Library sidebar               |  | \[Library\] ChooseItem or \[Library\] MoveRight                                     |  |
| \[Playlist\]   |  | SelectNextTrack                  |  | binary         |  | Scrolls to the next track in the track table.                                                                                                  |  | Library track table highlight |  | \[Library\] MoveDown                                                                |  |
| \[Playlist\]   |  | SelectPrevTrack                  |  | binary         |  | Scrolls to the previous track in the track table.                                                                                              |  | Library track table highlight |  | \[Library\] MoveUp                                                                  |  |
| \[Playlist\]   |  | SelectTrackKnob                  |  | relative value |  | Scrolls the given number of tracks in the track table (can be negative for reverse direction).                                                 |  | Library track table highlight |  | \[Library\] MoveVertival                                                            |  |

1.  introduced in Mixxx v1.11.0

2.  introduced in Mixxx v1.11.0

3.  introduced in Mixxx v1.11.0

4.  introduced in Mixxx v1.11.0

5.  introduced in Mixxx v1.11.0

6.  introduced in Mixxx v1.11.0

7.  introduced in Mixxx v2.0.0

8.  introduced in Mixxx v2.0.0

9.  introduced in Mixxx v2.0.0

10. introduced in Mixxx v1.10.0

11. introduced in Mixxx v1.10.0

12. introduced in Mixxx v2.0.0

13. introduced in Mixxx v2.0.0

14. introduced in Mixxx v2.0.0

15. introduced in Mixxx v2.0.0

16. introduced in Mixxx v2.0.0

17. introduced in Mixxx v1.9.0

18. introduced in Mixxx v1.9.0

19. introduced in Mixxx v1.11.0

20. introduced in Mixxx v2.0.0

21. changed in Mixxx v1.10.0

22. introduced in Mixxx v1.10.0

23. introduced in Mixxx v2.0.0

24. introduced in Mixxx v2.0.0

25. introduced in Mixxx v2.0.0

26. introduced in Mixxx v1.10.0

27. introduced in Mixxx v1.10.0

28. introduced in Mixxx v1.10.0

29. introduced in Mixxx v1.10.0

30. introduced in Mixxx v1.11.0

31. introduced in Mixxx v2.0.0

32. introduced in Mixxx v2.0.0

33. introduced in Mixxx v1.10.0

34. introduced in Mixxx v2.0.0

35. introduced in Mixxx v2.0.0

36. introduced in Mixxx v2.0.0

37. changed in Mixxx v1.10.0

38. introduced in Mixxx v1.10.0

39. introduced in Mixxx v1.10.0

40. introduced in Mixxx v1.9.0

41. changed in Mixxx v1.10.0

42. introduced in Mixxx v1.9.0

43. introduced in Mixxx v1.9.2

44. introduced in Mixxx v1.11.0

45. introduced in Mixxx v1.11.0

46. introduced in Mixxx v2.0.0

47. introduced in Mixxx v1.10.0

48. introduced in Mixxx v2.1.0

49. introduced in Mixxx v1.9.0

50. introduced in Mixxx v2.0.0

51. introduced in Mixxx v1.8.0

52. introduced in Mixxx v1.8.0

53. introduced in Mixxx v1.8.0

54. introduced in Mixxx v1.8.0

55. introduced in Mixxx v1.11.0

56. introduced in Mixxx v1.8.0

57. introduced in Mixxx v1.8.0

58. introduced in Mixxx v1.8.0

59. introduced in Mixxx v2.0.0

60. introduced in Mixxx v1.9.0

61. introduced in Mixxx v1.11.0

62. introduced in Mixxx v1.10.0

63. introduced in Mixxx v1.8.0

64. introduced in Mixxx v1.8.0

65. introduced in Mixxx v1.10.0

66. introduced in Mixxx v1.8.0

67. introduced in Mixxx v1.8.0

68. introduced in Mixxx v2.0.0

69. introduced in Mixxx v2.0.0

70. introduced in Mixxx v2.0.0

71. introduced in Mixxx v1.10.0

72. introduced in Mixxx v1.8.0

73. introduced in Mixxx v1.9.0

74. introduced in Mixxx v2.0.0

75. introduced in Mixxx v2.0.0

76. introduced in Mixxx v2.0.0

77. introduced in Mixxx v2.0.0

78. introduced in Mixxx v2.0.0

79. introduced in Mixxx v1.10.0

80. introduced in Mixxx v1.10.0

81. introduced in Mixxx v1.8.0

82. introduced in Mixxx v1.9.0

83. introduced in Mixxx v2.0.0

84. introduced in Mixxx v2.0.0

85. introduced in Mixxx v1.8.0

86. introduced in Mixxx v1.8.0

87. introduced in Mixxx v1.11.0

88. introduced in Mixxx v1.10.0

89. introduced in Mixxx v1.10.0

90. introduced in Mixxx v1.10.0

91. introduced in Mixxx v2.0.0

92. introduced in Mixxx v2.0.0

93. introduced in Mixxx v2.0.0

94. introduced in Mixxx v2.0.0

95. introduced in Mixxx v2.1.0

96. introduced in Mixxx v1.9.0

97. introduced in Mixxx v2.0.0

98. introduced in Mixxx v1.10.0

99. introduced in Mixxx v1.10.0

100. introduced in Mixxx v1.10.0

101. introduced in Mixxx v1.10.0

102. introduced in Mixxx v2.0.0

103. introduced in Mixxx v2.0.0

104. introduced in Mixxx v2.0.0

105. introduced in Mixxx v1.11.0

106. introduced in Mixxx v1.11.0

107. introduced in Mixxx v1.11.0

108. introduced in Mixxx v1.11.0

109. introduced in Mixxx v2.0.0

110. introduced in Mixxx v2.0.0

111. introduced in Mixxx v1.10.0

112. introduced in Mixxx v2.0.0

113. introduced in Mixxx v1.10.0

114. introduced in Mixxx v1.10.0

115. introduced in Mixxx v1.10.0

116. introduced in Mixxx v1.10.0

117. introduced in Mixxx v1.10.0

118. introduced in Mixxx v2.0.0

119. introduced in Mixxx v1.10.0

120. introduced in Mixxx v1.11.0

121. introduced in Mixxx v1.11.0

122. introduced in Mixxx v1.11.0

123. introduced in Mixxx v1.11.0

124. introduced in Mixxx v2.1.0

125. introduced in Mixxx v2.1.0

126. introduced in Mixxx v2.1.0

127. introduced in Mixxx v2.1.0

128. introduced in Mixxx v2.1.0

129. introduced in Mixxx v2.1.0

130. introduced in Mixxx v2.1.0

131. introduced in Mixxx v2.1.0

132. introduced in Mixxx v2.1.0

133. introduced in Mixxx v2.1.0

134. introduced in Mixxx v2.1.0

135. introduced in Mixxx v2.1.0

136. introduced in Mixxx v2.1.0

137. introduced in Mixxx v2.0.0

138. introduced in Mixxx v2.0.0

139. introduced in Mixxx v2.0.0

140. introduced in Mixxx v2.0.0

141. introduced in Mixxx v2.0.0

142. introduced in Mixxx v2.0.0

143. introduced in Mixxx v2.1.0

144. introduced in Mixxx v2.1.0

145. introduced in Mixxx v2.1.0

146. introduced in Mixxx v2.1.0

147. introduced in Mixxx v2.0.0

148. deprecated in Mixxx v2.0.0

149. introduced in Mixxx v2.0.0

150. deprecated in Mixxx v2.0.0

151. deprecated in Mixxx v2.0.0

152. deprecated in Mixxx v2.0.0

153. deprecated in Mixxx v2.0.0

154. deprecated in Mixxx v2.0.0

155. deprecated in Mixxx v2.0.0

156. deprecated in Mixxx v2.0.0

157. deprecated in Mixxx v2.0.0

158. deprecated in Mixxx v2.0.0

159. deprecated in Mixxx v2.0.0

160. deprecated in Mixxx v2.0.0

161. introduced in Mixxx v1.10.0

162. introduced in Mixxx v1.11.0
