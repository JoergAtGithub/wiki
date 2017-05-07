# Pioneer DDJ-SX

The DDJ-SX delivers intuitive control of all MIXXX's exciting features.
Dedicated buttons and dials deliver plug-and-play control of 4 decks.
[[/media/hardware/pioneerddjsx_layout.png|]]

## Controller Configuration

The DDJ-SX provides several settings, which can be changed in a special
*Utility-Mode*.

### Utility-Mode

  - Disconnect USB-cable.
  - Switch off \[**STANDBY/ON**\] the unit.
  - Hold \[**SHIFT**\] button and \[**PLAY/PAUSE**\] button at the left
    deck while switching on the unit \[**STANDBY/ON**\].
  - Now *Utility-Mode* is activated.
  - For saving and exiting *Utility-Mode*, switch off the unit again
    \[**STANDBY/ON**\].

### Setting for usage of Serato DJ

To use the DDJ-SX with MIXXX, the controller must be configured for the
usage of Serato DJ. You can check/change this setting as follows:  
**Press the \[KEY LOCK\] button at the left deck:**

  - \[**KEY LOCK**\] button off: Controller is configured for using
    Serato DJ (default).
  - \[**KEY LOCK**\] button on (lit): Controller is configured for using
    different DJ-software.

## User Options

To change the mapping's user options, you have to open the script file
(\*.js). At the top of the file under **USER OPTIONS** the following
settings can be made:

  - **PioneerDDJSX.jogwheelSensivity**: Sets the jogwheel sensivity. 1 =
    default, 2 is twice as sensitive, 0.5 is half as sensitive.
  - **PioneerDDJSX.jogwheelShiftMultiplier**: Sets how much more
    sensitive the jogwheels get when holding \[**SHIFT**\]. Set it to 1
    to disable jogwheel sensitivity increase when holding \[**SHIFT**\].
  - **PioneerDDJSX.speedSliderRange**: Sets the default speed slider
    range (0.08 = 8%), set at controller init.
  - **PioneerDDJSX.cutVumeter**: Cuts level-meter low frequencies and
    expands upper frequencies.
  - **PioneerDDJSX.twinkleVumeterAutodjOn**: If true, level-meter
    twinkles if *AutoDJ* is enabled.
  - **PioneerDDJSX.autoDJAddTop**: If true, the selected track will be
    added to *AutoDJ* queue-top on pressing \[**ROTARY SELECTOR**\],
    else the selected track will be added to *AutoDJ* queue-bottom.
  - **PioneerDDJSX.autoDJTickInterval**: Sets the duration of sleeping
    between *AutoDJ* actions if *AutoDJ* is enabled \[ms\].
  - **PioneerDDJSX.autoDJMaxBpmAdjustment**: Sets the maximum adjustment
    of BPM allowed for beats to sync if *AutoDJ* is enabled \[BPM\].
  - **PioneerDDJSX.autoDJShuffleAfterSkip**: If true, *AutoDJ* queue is
    being shuffled after skipping a track.
  - **PioneerDDJSX.jumpPreviewEnabled**: If true, by releasing
    \[**ROTARY SELECTOR**\], track in preview player jumps forward to
    "jumpPreviewPosition".
  - **PioneerDDJSX.jumpPreviewPosition**: Sets the preview player
    absolute position, being set at releasing \[**ROTARY SELECTOR**\]
    and if "jumpPreviewEnabled" is enabled.
  - **PioneerDDJSX.samplerCueGotoAndPlay**: If true, pad press in
    \[**SAMPLER**\]-PAD-MODE repeatedly causes *sampler* to play loaded
    track from cue-point, else it causes to play loaded track from the
    beginning.
  - **PioneerDDJSX.autoPFL**: If true, PFL / Cue (headphone) is being
    activated by loading a track into certain deck.
  - **PioneerDDJSX.useNewLibraryControls**: If true, new in Mixxx 2.1
    introduced library controls will be used, else old playlist controls
    will be used.
  - **PioneerDDJSX.needleSearchShiftEnable**: If true, \[**SHIFT**\] has
    to be pressed to activate needle search control.

## General Functions

### Managed by Mixxx

| Group           | Figure     | \[**SHIFT**\]? | Button Name                   | Description                                                                                                         |
| --------------- | ---------- | -------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 5 - BROWSER     | 2, 3, 4, 5 | \-             | \[**LOAD**\]                  | Loads the selected track into the specific deck                                                                     |
| :::             | 2          | \[**SHIFT**\]  | \[**LOAD**\]                  | AutoDJ - Toggle BPM sync                                                                                            |
| :::             | 3          | \[**SHIFT**\]  | \[**LOAD**\]                  | AutoDJ - Toggle Key sync                                                                                            |
| :::             | 1          | \-             | \[**ROTARY SELECTOR**\]       | See user options: default = Select track in Playlist (alt. = MoveVertical)                                          |
| :::             | 1          | \-             | \[**ROTARY SELECTOR PRESS**\] | See user options: default = Add track to AutoDJ queue at bottom (alt. = at top)                                     |
| :::             | 1          | \[**SHIFT**\]  | \[**ROTARY SELECTOR**\]       | See user options: default = Select Playlist (alt. = MoveHorizontal)                                                 |
| :::             | 1          | \[**SHIFT**\]  | \[**ROTARY SELECTOR PRESS**\] | See user options: default = Toggle selected sidebar item (alt. = ChooseItem)                                        |
| :::             | 6          | \-             | \[**BACK**\]                  | See user options: default = AutoDJ - Skip next track in queue (alt. = MoveFocusBackward)                            |
| :::             | 6          | \[**SHIFT**\]  | \[**BACK**\]                  | Maximize view of Library                                                                                            |
| :::             | 7          | \-             | \[**LOAD PREPARE**\]          | Load selected track into PreviewDeck, jump to position (see user options) and play, else stop already playing track |
| 3 - MIXER       | 1          | \-             | Crossfader                    | Controls Mixxx crossfader, fades between deck 1, 3 and 2, 4                                                         |
| :::             | 2          | \-             | Channel fader                 | Controls deck volume                                                                                                |
| :::             | 2          | \[**SHIFT**\]  | Channel fader                 | Fader start (starts playing deck when rising deck volume)                                                           |
| :::             | 3          | \-             | TRIM                          | Controls deck gain                                                                                                  |
| :::             | 4          | \-             | EQ HIGH                       | Controls deck's equalizer/filter high frequencies                                                                   |
| :::             | 5          | \-             | EQ MID                        | Controls deck's equalizer/filter mid frequencies                                                                    |
| :::             | 6          | \-             | EQ LOW                        | Controls deck's equalizer/filter low frequencies                                                                    |
| :::             | 7          | \-             | \[**CUE**\]                   | Toggles PFL/Cue (headphones) for specific deck                                                                      |
| :::             | 7          | \[**SHIFT**\]  | \[**CUE**\]                   | BPM Tab function for specific deck                                                                                  |
| :::             | 9          | \[**SHIFT**\]  | \[**MASTER CUE**\]            | Toggles split cue (headphones)                                                                                      |
| :::             | 10         | \-             | Crossfader Assign             | Crossfader assignment - deck to crossfader (left (A), right (B) or center (THRU))                                   |
| :::             | 14         | \-             | SAMPLER VOLUME                | Controls volume of all available Sampler decks                                                                      |
| 4 - FRONT PANEL | 1          | \-             | Crossfader curve              | Controls Mixxx crossfader curve                                                                                     |
| 1 - DECK        | 25         | \-             | \[**PANEL SELECT**\]          | Show/hide Sampler decks / Effect rack                                                                               |

### Managed by the controller

The following functions are directly controlled by the controller
(Mixxx-independent):

| Group           | Figure | \[**SHIFT**\]? | Button Name         | Description                                     |
| --------------- | ------ | -------------- | ------------------- | ----------------------------------------------- |
| 3 - MIXER       | 8      | \-             | MASTER LEVEL        | Controls the master output volume               |
| :::             | 9      | \-             | \[**MASTER CUE**\]  | Toggles master cue                              |
| :::             | 13     | \-             | HEADPHONES MIX      | Controls headphone's audio source (cue, master) |
| :::             | 15     | \-             | BOOTH MONITOR LEVEL | Controls the booth output volume                |
| 4 - FRONT PANEL | 2      | \-             | INPUT SELECT        | Controls deck source (PC, MIC, CD, PHONO, LINE) |

## Deck Functions

### Managed by Mixxx

| Group                | Figure | \[**SHIFT**\]? | Button Name                            | Description                                                                                                                                                                                                                                                |
| -------------------- | ------ | -------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 - DECK             | 1      | \-             | \[**PLAY/PAUSE**\]                     | Toggles play/pause                                                                                                                                                                                                                                         |
| :::                  | 1      | \[**SHIFT**\]  | \[**PLAY/PAUSE**\]                     | Toggles play stutter                                                                                                                                                                                                                                       |
| :::                  | 2      | \-             | \[**CUE**\]                            | Toggles default cue (sets cue point/ goes to cue point)                                                                                                                                                                                                    |
| :::                  | 2      | \[**SHIFT**\]  | \[**CUE**\]                            | Toggles brake                                                                                                                                                                                                                                              |
| :::                  | 3      | \-             | Jog dial (Platter)                     | Vinyl-Mode enabled: performs scratching when pressed and rotated, Vinyl-Mode disabled: performs pitch bend                                                                                                                                                 |
| :::                  | 3      | \[**SHIFT**\]  | Jog dial (Platter)                     | Vinyl-Mode enabled: performs scratching considering user-options multiplier when touched and rotated, Vinyl-Mode disabled: performs pitch bend considering user-options multiplier                                                                         |
| :::                  | 3      | \-             | Jog dial (Wheel side)                  | Performs pitch bend when rotated                                                                                                                                                                                                                           |
| :::                  | 3      | \[**SHIFT**\]  | Jog dial (Wheel side)                  | Performs pitch bend when rotated considering user-options multiplier                                                                                                                                                                                       |
| :::                  | 4      | \-             | TEMPO                                  | Controls pitch/tempo ratio                                                                                                                                                                                                                                 |
| :::                  | 5      | \-             | \[**KEYLOCK**\]                        | Toggles keylock                                                                                                                                                                                                                                            |
| :::                  | 5      | \[**SHIFT**\]  | \[**KEYLOCK**\]                        | Changes TEMPO slider range: 8% -\> 16% -\> 32% -\> 64% -\> 100% -\> 8%...                                                                                                                                                                                  |
| :::                  | 5      | \-             | \[**KEYLOCK**\] (Long press)           | Toggles pitch/tempo reset                                                                                                                                                                                                                                  |
| :::                  | 6      | \-             | \[**NEEDLE SEARCH**\]                  | Jumps to equivalent absolute position in track                                                                                                                                                                                                             |
| :::                  | 13     | \-             | \[**SYNC**\]                           | Toggles deck sync                                                                                                                                                                                                                                          |
| :::                  | 13     | \[**SHIFT**\]  | \[**SYNC**\]                           | Toggles quantize function                                                                                                                                                                                                                                  |
| :::                  | 14     | \-             | \[**AUTO LOOP**\]                      | Toggles a 4-Beat loop                                                                                                                                                                                                                                      |
| :::                  | 14     | \[**SHIFT**\]  | \[**AUTO LOOP**\]                      | Toggles reloop                                                                                                                                                                                                                                             |
| :::                  | 15     | \-             | \[**LOOP 1/2X**\]                      | Halves active loop                                                                                                                                                                                                                                         |
| :::                  | 15     | \[**SHIFT**\]  | \[**LOOP 1/2X**\]                      | Moves active loop one beat backward (left)                                                                                                                                                                                                                 |
| :::                  | 16     | \-             | \[**LOOP 2X**\]                        | Doubles active loop                                                                                                                                                                                                                                        |
| :::                  | 16     | \[**SHIFT**\]  | \[**LOOP 2X**\]                        | Moves active loop one beat forward (right)                                                                                                                                                                                                                 |
| :::                  | 17     | \-             | \[**LOOP IN**\]                        | Toggles loop in                                                                                                                                                                                                                                            |
| :::                  | 18     | \-             | \[**LOOP OUT**\]                       | Toggles loop out                                                                                                                                                                                                                                           |
| :::                  | 18     | \[**SHIFT**\]  | \[**LOOP OUT**\]                       | Toggles reloop / exit loop                                                                                                                                                                                                                                 |
| :::                  | 19     | \-             | \[**VINYL**\]                          | Toggles vinyl (scratch) mode                                                                                                                                                                                                                               |
| :::                  | 20     | \-             | \[**CENSOR**\]                         | Toggles reverse roll play                                                                                                                                                                                                                                  |
| :::                  | 20     | \[**SHIFT**\]  | \[**CENSOR**\]                         | Toggles reverse play                                                                                                                                                                                                                                       |
| :::                  | 21     | \-             | \[**SLIP**\]                           | Toggles slip mode                                                                                                                                                                                                                                          |
| :::                  | 22     | \-             | \[**GRID ADJUST**\]                    | Hold and touch/rotate Jog dial to adjust beats faster/slower                                                                                                                                                                                               |
| :::                  | 22     | \[**SHIFT**\]  | \[**GRID ADJUST**\]                    | Set/translate beat grid to current track position (adjust position with Jog dial)                                                                                                                                                                          |
| :::                  | 23     | \-             | \[**GRID SLIDE**\]                     | Hold and touch/rotate Jog dial to set/translate beat grid earlier/later                                                                                                                                                                                    |
| :::                  | 24     | \-             | \[**SHIFT**\]                          | Switches to shifted controls, no direct function                                                                                                                                                                                                           |
| 6 - PERFORMANCE PADS | 1      | \-             | \[**PAD 1**\] (HOT CUE mode)           | Set/activate Hot cue 1                                                                                                                                                                                                                                     |
| :::                  | 1      | \[**SHIFT**\]  | \[**PAD 1**\] (HOT CUE mode)           | Clear Hot cue 1                                                                                                                                                                                                                                            |
| :::                  | 2      | \-             | \[**PAD 2**\] (HOT CUE mode)           | Set/activate Hot cue 2                                                                                                                                                                                                                                     |
| :::                  | 2      | \[**SHIFT**\]  | \[**PAD 2**\] (HOT CUE mode)           | Clear Hot cue 2                                                                                                                                                                                                                                            |
| :::                  | 3      | \-             | \[**PAD 3**\] (HOT CUE mode)           | Set/activate Hot cue 3                                                                                                                                                                                                                                     |
| :::                  | 3      | \[**SHIFT**\]  | \[**PAD 3**\] (HOT CUE mode)           | Clear Hot cue 3                                                                                                                                                                                                                                            |
| :::                  | 4      | \-             | \[**PAD 4**\] (HOT CUE mode)           | Set/activate Hot cue 4                                                                                                                                                                                                                                     |
| :::                  | 4      | \[**SHIFT**\]  | \[**PAD 4**\] (HOT CUE mode)           | Clear Hot cue 4                                                                                                                                                                                                                                            |
| :::                  | 5      | \-             | \[**PAD 5**\] (HOT CUE mode)           | Set/activate Hot cue 5                                                                                                                                                                                                                                     |
| :::                  | 5      | \[**SHIFT**\]  | \[**PAD 5**\] (HOT CUE mode)           | Clear Hot cue 5                                                                                                                                                                                                                                            |
| :::                  | 6      | \-             | \[**PAD 6**\] (HOT CUE mode)           | Set/activate Hot cue 6                                                                                                                                                                                                                                     |
| :::                  | 6      | \[**SHIFT**\]  | \[**PAD 6**\] (HOT CUE mode)           | Clear Hot cue 6                                                                                                                                                                                                                                            |
| :::                  | 7      | \-             | \[**PAD 7**\] (HOT CUE mode)           | Set/activate Hot cue 7                                                                                                                                                                                                                                     |
| :::                  | 7      | \[**SHIFT**\]  | \[**PAD 7**\] (HOT CUE mode)           | Clear Hot cue 7                                                                                                                                                                                                                                            |
| :::                  | 8      | \-             | \[**PAD 8**\] (HOT CUE mode)           | Set/activate Hot cue 8                                                                                                                                                                                                                                     |
| :::                  | 8      | \[**SHIFT**\]  | \[**PAD 8**\] (HOT CUE mode)           | Clear Hot cue 8                                                                                                                                                                                                                                            |
| :::                  | 1      | \-             | \[**PAD 1**\] (ROLL mode)              | Toggle Beatloop roll length index 1 (according parameter set)                                                                                                                                                                                              |
| :::                  | 2      | \-             | \[**PAD 2**\] (ROLL mode)              | Toggle Beatloop roll length index 2 (according parameter set)                                                                                                                                                                                              |
| :::                  | 3      | \-             | \[**PAD 3**\] (ROLL mode)              | Toggle Beatloop roll length index 3 (according parameter set)                                                                                                                                                                                              |
| :::                  | 4      | \-             | \[**PAD 4**\] (ROLL mode)              | Toggle Beatloop roll length index 4 (according parameter set)                                                                                                                                                                                              |
| :::                  | 5      | \-             | \[**PAD 5**\] (ROLL mode)              | Toggle Beatloop roll length index 5 (according parameter set)                                                                                                                                                                                              |
| :::                  | 6      | \-             | \[**PAD 6**\] (ROLL mode)              | Toggle Beatloop roll length index 6 (according parameter set)                                                                                                                                                                                              |
| :::                  | 7      | \-             | \[**PAD 7**\] (ROLL mode)              | Toggle Beatloop roll length index 7 (according parameter set)                                                                                                                                                                                              |
| :::                  | 8      | \-             | \[**PAD 8**\] (ROLL mode)              | Toggle Beatloop roll length index 8 (according parameter set)                                                                                                                                                                                              |
| :::                  | 1      | \-             | \[**PAD 1**\] (SLICER mode)            | Press: Jumps to beat position 1 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (slicer type 1 only): Jumps to actual play position in the background (slip). See [\#Slicer description](#Slicer%20description) |
| :::                  | 2      | \-             | \[**PAD 2**\] (SLICER mode)            | Press: Jumps to beat position 2 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (slicer type 1 only): Jumps to actual play position in the background (slip). See [\#Slicer description](#Slicer%20description) |
| :::                  | 3      | \-             | \[**PAD 3**\] (SLICER mode)            | Press: Jumps to beat position 3 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (slicer type 1 only): Jumps to actual play position in the background (slip). See [\#Slicer description](#Slicer%20description) |
| :::                  | 4      | \-             | \[**PAD 4**\] (SLICER mode)            | Press: Jumps to beat position 4 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (slicer type 1 only): Jumps to actual play position in the background (slip). See [\#Slicer description](#Slicer%20description) |
| :::                  | 5      | \-             | \[**PAD 5**\] (SLICER mode)            | Press: Jumps to beat position 5 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (slicer type 1 only): Jumps to actual play position in the background (slip). See [\#Slicer description](#Slicer%20description) |
| :::                  | 6      | \-             | \[**PAD 6**\] (SLICER mode)            | Press: Jumps to beat position 6 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (slicer type 1 only): Jumps to actual play position in the background (slip). See [\#Slicer description](#Slicer%20description) |
| :::                  | 7      | \-             | \[**PAD 7**\] (SLICER mode)            | Press: Jumps to beat position 7 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (slicer type 1 only): Jumps to actual play position in the background (slip). See [\#Slicer description](#Slicer%20description) |
| :::                  | 8      | \-             | \[**PAD 8**\] (SLICER mode)            | Press: Jumps to beat position 8 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (slicer type 1 only): Jumps to actual play position in the background (slip). See [\#Slicer description](#Slicer%20description) |
| :::                  | 1      | \-             | \[**PAD 1**\] (SAMPLER mode)           | Sample deck index 1 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck                                                                                               |
| :::                  | 1      | \[**SHIFT**\]  | \[**PAD 1**\] (SAMPLER mode)           | Sample deck index 1 (according sampler bank) - playing: stop deck, stopped: eject track                                                                                                                                                                    |
| :::                  | 2      | \-             | \[**PAD 2**\] (SAMPLER mode)           | Sample deck index 2 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck                                                                                               |
| :::                  | 2      | \[**SHIFT**\]  | \[**PAD 2**\] (SAMPLER mode)           | Sample deck index 2 (according sampler bank) - playing: stop deck, stopped: eject track                                                                                                                                                                    |
| :::                  | 3      | \-             | \[**PAD 3**\] (SAMPLER mode)           | Sample deck index 3 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck                                                                                               |
| :::                  | 3      | \[**SHIFT**\]  | \[**PAD 3**\] (SAMPLER mode)           | Sample deck index 3 (according sampler bank) - playing: stop deck, stopped: eject track                                                                                                                                                                    |
| :::                  | 4      | \-             | \[**PAD 4**\] (SAMPLER mode)           | Sample deck index 4 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck                                                                                               |
| :::                  | 4      | \[**SHIFT**\]  | \[**PAD 4**\] (SAMPLER mode)           | Sample deck index 4 (according sampler bank) - playing: stop deck, stopped: eject track                                                                                                                                                                    |
| :::                  | 5      | \-             | \[**PAD 5**\] (SAMPLER mode)           | Sample deck index 5 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck                                                                                               |
| :::                  | 5      | \[**SHIFT**\]  | \[**PAD 5**\] (SAMPLER mode)           | Sample deck index 5 (according sampler bank) - playing: stop deck, stopped: eject track                                                                                                                                                                    |
| :::                  | 6      | \-             | \[**PAD 6**\] (SAMPLER mode)           | Sample deck index 6 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck                                                                                               |
| :::                  | 6      | \[**SHIFT**\]  | \[**PAD 6**\] (SAMPLER mode)           | Sample deck index 6 (according sampler bank) - playing: stop deck, stopped: eject track                                                                                                                                                                    |
| :::                  | 7      | \-             | \[**PAD 7**\] (SAMPLER mode)           | Sample deck index 7 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck                                                                                               |
| :::                  | 7      | \[**SHIFT**\]  | \[**PAD 7**\] (SAMPLER mode)           | Sample deck index 7 (according sampler bank) - playing: stop deck, stopped: eject track                                                                                                                                                                    |
| :::                  | 8      | \-             | \[**PAD 8**\] (SAMPLER mode)           | Sample deck index 8 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck                                                                                               |
| :::                  | 8      | \[**SHIFT**\]  | \[**PAD 8**\] (SAMPLER mode)           | Sample deck index 8 (according sampler bank) - playing: stop deck, stopped: eject track                                                                                                                                                                    |
| :::                  | 1      | \-             | \[**PAD 1**\] (GROUP2 mode)            | Toggle Beatloop length index 1 (according parameter set)                                                                                                                                                                                                   |
| :::                  | 2      | \-             | \[**PAD 2**\] (GROUP2 mode)            | Toggle Beatloop length index 2 (according parameter set)                                                                                                                                                                                                   |
| :::                  | 3      | \-             | \[**PAD 3**\] (GROUP2 mode)            | Toggle Beatloop length index 3 (according parameter set)                                                                                                                                                                                                   |
| :::                  | 4      | \-             | \[**PAD 4**\] (GROUP2 mode)            | Toggle Beatloop length index 4 (according parameter set)                                                                                                                                                                                                   |
| :::                  | 5      | \-             | \[**PAD 5**\] (GROUP2 mode)            | Toggle Beatloop length index 5 (according parameter set)                                                                                                                                                                                                   |
| :::                  | 6      | \-             | \[**PAD 6**\] (GROUP2 mode)            | Toggle Beatloop length index 6 (according parameter set)                                                                                                                                                                                                   |
| :::                  | 7      | \-             | \[**PAD 7**\] (GROUP2 mode)            | Toggle Beatloop length index 7 (according parameter set)                                                                                                                                                                                                   |
| :::                  | 8      | \-             | \[**PAD 8**\] (GROUP2 mode)            | Toggle Beatloop length index 8 (according parameter set)                                                                                                                                                                                                   |
| :::                  | 9      | \-             | \[**HOT CUE**\] mode                   | Switches PAD control and illumination to HOT CUE mode                                                                                                                                                                                                      |
| :::                  | 10     | \-             | \[**ROLL**\] mode                      | Switches PAD control and illumination to BEATLOOP ROLL mode                                                                                                                                                                                                |
| :::                  | 10     | \[**SHIFT**\]  | \[**ROLL**\] mode                      | Switches PAD control and illumination to GROUP2 (BEATLOOP) mode                                                                                                                                                                                            |
| :::                  | 11     | \-             | \[**SLICER**\] mode                    | Switches PAD control and illumination to SLICER mode, in SLICER mode switches between slicer type 1 and 2 (see [\#Slicer description](#Slicer%20description))                                                                                              |
| :::                  | 12     | \-             | \[**SAMPLER**\] mode                   | Switches PAD control and illumination to SAMPLER mode                                                                                                                                                                                                      |
| :::                  | 12     | \-             | \[**SAMPLER**\] mode (long press)      | Toggles SAMPLER PADS velocity mode (velocity \~ volume)                                                                                                                                                                                                    |
| :::                  | 13     | \-             | \[**PARAMETER LEFT**\] (ROLL mode)     | Decrement active looproll-interval parameter set (0-3, see [\#Loop/Loop-Roll parameter sets](#Loop/Loop-Roll%20parameter%20sets)), button LED is illuminated at parameter set 2, 3                                                                         |
| :::                  | 13     | \-             | \[**PARAMETER LEFT**\] (SLICER mode)   | Decrement active slicer quantization (1/8, 1/4, 1/2, 1 beat loop), button LED is illuminated at quantization 1/2, 1                                                                                                                                        |
| :::                  | 13     | \-             | \[**PARAMETER LEFT**\] (SAMPLER mode)  | Decrement active sampler bank (0-3), button LED is illuminated at sampler bank 2, 3. Sampler bank 0: sampler 1-8, sampler bank 1: sampler 9-16, sampler bank 2: sampler 17-24, sampler bank 3: sampler 25-32                                               |
| :::                  | 13     | \-             | \[**PARAMETER LEFT**\] (GROUP2 mode)   | Decrement active loop-interval parameter set (0-3, see [\#Loop/Loop-Roll parameter sets](#Loop/Loop-Roll%20parameter%20sets)), button LED is illuminated at parameter set 2, 3                                                                             |
| :::                  | 14     | \-             | \[**PARAMETER RIGHT**\] (ROLL mode)    | Increment active looproll-interval parameter set (0-3, see [\#Loop/Loop-Roll parameter sets](#Loop/Loop-Roll%20parameter%20sets)), button LED is illuminated at parameter set 1, 3                                                                         |
| :::                  | 14     | \-             | \[**PARAMETER RIGHT**\] (SLICER mode)  | Increment active slicer quantization (1/8, 1/4, 1/2, 1 beat loop), button LED is illuminated at quantization 1/4, 1                                                                                                                                        |
| :::                  | 14     | \-             | \[**PARAMETER RIGHT**\] (SAMPLER mode) | Increment active sampler bank (0-3), button LED is illuminated at sampler bank 1, 3. Sampler bank 0: sampler 1-8, sampler bank 1: sampler 9-16, sampler bank 2: sampler 17-24, sampler bank 3: sampler 25-32                                               |
| :::                  | 14     | \-             | \[**PARAMETER RIGHT**\] (GROUP2 mode)  | Increment active loop-interval parameter set (0-3, see [\#Loop/Loop-Roll parameter sets](#Loop/Loop-Roll%20parameter%20sets)), button LED is illuminated at parameter set 1, 3                                                                             |

### Managed by the controller

The following functions are directly controlled by the controller
(Mixxx-independent):

| Group    | Figure | \[**SHIFT**\]? | Button Name       | Description                                                             |
| -------- | ------ | -------------- | ----------------- | ----------------------------------------------------------------------- |
| 1 - DECK | 7      | \-             | \[**DECK 1**\]    | Switches left deck to DECK 1 control and illumination                   |
| :::      | 8      | \-             | \[**DECK 2**\]    | Switches right deck to DECK 2 control and illumination                  |
| :::      | 9      | \-             | \[**DECK 3**\]    | Switches left deck to DECK 3 control and illumination                   |
| :::      | 10     | \-             | \[**DECK 4**\]    | Switches right deck to DECK 4 control and illumination                  |
| :::      | 11     | \-             | \[**DUAL DECK**\] | Toggles left deck to dual deck control and illumination (DECK 1 and 3)  |
| :::      | 12     | \-             | \[**DUAL DECK**\] | Toggles right deck to dual deck control and illumination (DECK 2 and 4) |

### Loop/Loop-Roll parameter sets

By using the \[**PARAMETER LEFT**\] and \[**PARAMETER RIGHT**\] buttons
in BEATLOOP ROLL (default parameter set: 2) or BEATLOOP mode (default
parameter set: 0), you can change the pad-assigned loop size. The
following table shows the possible assignments (unit: beats).

| Set No. | PAD1 | PAD2 | PAD3 | PAD4 | PAD5 | PAD6 | PAD7 | PAD8 |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0       | 1/4  | 1/2  | 1    | 2    | 4    | 8    | 16   | 32   |
| 1       | 1/8  | 1/4  | 1/2  | 1    | 2    | 4    | 8    | 16   |
| 2       | 1/16 | 1/8  | 1/4  | 1/2  | 1    | 2    | 4    | 8    |
| 3       | 1/32 | 1/16 | 1/8  | 1/4  | 1/2  | 1    | 2    | 4    |

### Slicer description

For a detailed explanation of the slicer mode, take a look at the
controller's
[manual](http://docs.pioneerdj.com/Manuals/DDJ_SX_DRI1096_manual/?_ga=1.221242769.826661553.1489418053).
A limited slicer functionality is implemented into the controller
mapping as described below.

There are two slicer types, 1 and 2, which can be selected by pressing
the \[**SLICER**\] mode button. If none or only one PAD (beat) is lit,
slicer type 1 is active. If you press \[**SLICER**\] mode button again,
slicer type 2 will be activated and all PADs, except one for the beat,
will light up.

Starting with the first beat marked on a playing track, the track is
divided into sections of 8 beats (not visible). If the first 8 beats are
reached, the next section starts. The PADs are assigned to one section,
each time the active section changes, the PADs will be assigned to the
new active section (PAD 1..8 = section beat 1..8).

#### Slicer type 1

The PAD lights show the active beat in the active section: The active
beat PAD is lit, all other PAD lights are off.

Slicer type 1 moves to the next section if the end of the previous
active section is reached.

[[/media/hardware/pioneerddjsx/pioneerddjsx_slicertype1.png|]]

By pressing PAD X, the play position jumps to the beat X of the active
section. If you have pressed the PAD on-beat and hold it, the play
position is playing in loop. The beat loop length depends on the
selected slicer quantization (changeable by pressing \[**PARAMETER
LEFT**\] or \[**PARAMETER RIGHT**\]). If you release the PAD, the
playback will resume where the track would have been if the slicer
wouldn't have been activated (slip mode).

#### Slicer type 2

The PAD lights show the active beat in the active section: The active
beat PAD light is off, all other PADs are lit.

As soon as slicer type 2 is activated, the active section is played in
loop (not visible). If the end of the active section is reached, the
play position jumps back to the beginning of the active section.

[[/media/hardware/pioneerddjsx/pioneerddjsx_slicertype2.png|]]

By pressing PAD X, the play position jumps to the beat X of the active
section. In slicer type 2 beat loop is not possible.

As soon as slicer type 2 is deactivated (by pressing \[**SLICER**\] mode
button again), the playback will resume where the track would have been
if the slicer wouldn't have been activated (slip mode).

## Effect Functions

| Group       | Figure         | \[**SHIFT**\]? | Button Name        | Description                                                  |
| ----------- | -------------- | -------------- | ------------------ | ------------------------------------------------------------ |
| 2 - EFFECTS | 1 (L)          | \-             | FX1-1              | Controls EffectRack1-EffectUnit1-Effect1 meta                |
| :::         | 1 (L)          | \[**SHIFT**\]  | FX1-1              | Controls EffectRack1-EffectUnit1 active effect's parameter 1 |
| :::         | 1 (R)          | \-             | FX2-1              | Controls EffectRack1-EffectUnit2-Effect1 meta                |
| :::         | 1 (R)          | \[**SHIFT**\]  | FX2-1              | Controls EffectRack1-EffectUnit2 active effect's parameter 1 |
| :::         | 2 (L)          | \-             | FX1-2              | Controls EffectRack1-EffectUnit1-Effect2 meta                |
| :::         | 2 (L)          | \[**SHIFT**\]  | FX1-2              | Controls EffectRack1-EffectUnit1 active effect's parameter 2 |
| :::         | 2 (R)          | \-             | FX2-2              | Controls EffectRack1-EffectUnit2-Effect2 meta                |
| :::         | 2 (R)          | \[**SHIFT**\]  | FX2-2              | Controls EffectRack1-EffectUnit2 active effect's parameter 2 |
| :::         | 3 (L)          | \-             | FX1-3              | Controls EffectRack1-EffectUnit1-Effect3 meta                |
| :::         | 3 (L)          | \[**SHIFT**\]  | FX1-3              | Controls EffectRack1-EffectUnit1 active effect's parameter 3 |
| :::         | 3 (R)          | \-             | FX2-3              | Controls EffectRack1-EffectUnit2-Effect3 meta                |
| :::         | 3 (R)          | \[**SHIFT**\]  | FX2-3              | Controls EffectRack1-EffectUnit2 active effect's parameter 3 |
| :::         | 4 (L)          | \-             | FX1 BEATS          | Controls EffectRack1-EffectUnit1 super1 knob                 |
| :::         | 4 (R)          | \-             | FX2 BEATS          | Controls EffectRack1-EffectUnit2 super1 knob                 |
| :::         | 4 (L)          | \[**SHIFT**\]  | FX1 BEATS          | Controls EffectRack1-EffectUnit1 mix                         |
| :::         | 4 (R)          | \[**SHIFT**\]  | FX2 BEATS          | Controls EffectRack1-EffectUnit2 mix                         |
| :::         | 5 (L)          | \-             | \[**FX1-1 ON**\]   | Toggles EffectRack1-EffectUnit1-Effect1                      |
| :::         | 5 (R)          | \-             | \[**FX2-1 ON**\]   | Toggles EffectRack1-EffectUnit2-Effect1                      |
| :::         | 5 (L)          | \[**SHIFT**\]  | \[**FX1-1 ON**\]   | Selects next effect for EffectRack1-EffectUnit1-Effect1      |
| :::         | 5 (R)          | \[**SHIFT**\]  | \[**FX2-1 ON**\]   | Selects next effect for EffectRack1-EffectUnit2-Effect1      |
| :::         | 6 (L)          | \-             | \[**FX1-2 ON**\]   | Toggles EffectRack1-EffectUnit1-Effect2                      |
| :::         | 6 (R)          | \-             | \[**FX2-2 ON**\]   | Toggles EffectRack1-EffectUnit2-Effect2                      |
| :::         | 6 (L)          | \[**SHIFT**\]  | \[**FX1-2 ON**\]   | Selects next effect for EffectRack1-EffectUnit1-Effect2      |
| :::         | 6 (R)          | \[**SHIFT**\]  | \[**FX2-2 ON**\]   | Selects next effect for EffectRack1-EffectUnit2-Effect2      |
| :::         | 7 (L)          | \-             | \[**FX1-3 ON**\]   | Toggles EffectRack1-EffectUnit1-Effect3                      |
| :::         | 7 (R)          | \-             | \[**FX2-3 ON**\]   | Toggles EffectRack1-EffectUnit2-Effect3                      |
| :::         | 7 (L)          | \[**SHIFT**\]  | \[**FX1-3 ON**\]   | Selects next effect for EffectRack1-EffectUnit1-Effect3      |
| :::         | 7 (R)          | \[**SHIFT**\]  | \[**FX2-3 ON**\]   | Selects next effect for EffectRack1-EffectUnit2-Effect3      |
| :::         | 8 (L)          | \-             | \[**FX1 TAP**\]    | Toggles EffectRack1-EffectUnit1                              |
| :::         | 8 (R)          | \-             | \[**FX2 TAP**\]    | Toggles EffectRack1-EffectUnit2                              |
| :::         | 8 (L)          | \[**SHIFT**\]  | \[**FX1 TAP**\]    | Selects next chain for EffectRack1-EffectUnit1               |
| :::         | 8 (R)          | \[**SHIFT**\]  | \[**FX2 TAP**\]    | Selects next chain for EffectRack1-EffectUnit2               |
| :::         | 9, 10, 11, 12  | \-             | \[**FX1 ASSIGN**\] | Assign EffectRack1-EffectUnit1 to specific deck              |
| :::         | 13, 14, 15, 16 | \-             | \[**FX2 ASSIGN**\] | Assign EffectRack1-EffectUnit2 to specific deck              |
| :::         | 17, 18, 19, 20 | \-             | FILTER             | Control QuickEffectRack1 super1 knob (e.g. moog filter)      |

## References

  - [Manufacturer's product
    page](https://www.pioneerdj.com/en-us/product/controller/ddj-sx/black/overview/)
  - [Forum thread](http://www.mixxx.org/forums/viewtopic.php?f=7&t=8310)
  - [Manual
    (multi-language)](http://docs.pioneerdj.com/Manuals/DDJ_SX_DRH1193_manual/)
  - [List of MIDI
    messages](https://pdj-ecom-cdn.azureedge.net/-/media/pioneerdj/software-info/controller/ddj-sx/ddj-sx_list_of_midi_messages_e.pdf?la=en)
  - [Controller Scripting](midi_scripting)
  - [Mixxx Controls](mixxxcontrols)
