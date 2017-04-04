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

### Setting for usage of different DJ-software

To use the DDJ-SX with a different DJ-software than Serato and get
proper MIDI-messages, you have to change this setting (default is for
using Serato).  
**Press the \[KEY LOCK\] button at the left deck:**

  - \[**KEY LOCK**\] button off: Controller is configured for using
    Serato.
  - \[**KEY LOCK**\] button on (lit): Controller is configured for using
    different DJ-software.

## User Options

To change the mapping's user options, you have to open the script file
(\*.js). At the top of the file under **USER OPTIONS** the following
settings can be made:

  - **PioneerDDJSX.blinkingSync**: If true, the \[**SYNC**\] button
    blinks with the beat. If false, the \[**SYNC**\] button is lit when
    *sync* is enabled.
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
  - **PioneerDDJSX.samplerShowLoadDialog**: If true, LoadSamplerBank
    file dialog will show up at running init.
  - **PioneerDDJSX.samplerCueGotoAndPlay**: If true, pad press in
    \[**SAMPLER**\]-PAD-MODE repeatedly causes *sampler* to play loaded
    track from cue-point, else it causes to play loaded track from the
    beginning.
  - **PioneerDDJSX.autoPFL**: If true, PFL / Cue (headphone) is being
    activated by loading a track into certain deck.
  - **PioneerDDJSX.useNewLibraryControls**: If true, new in Mixxx 2.1
    introduced library controls will be used, else old playlist controls
    will be used.

## General Functions

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
| :::             | 14         | \-             | SAMPLER VOLUME                | Controls volume of all available Sampler decks                                                                      |
| 4 - FRONT PANEL | 1          | \-             | Crossfader curve              | Controls Mixxx crossfader curve                                                                                     |
| 1 - DECK        | 25         | \-             | \[**PANEL SELECT**\]          | Show/hide Sampler decks / Effect rack                                                                               |

The following functions are directly controlled by the controller
(Mixxx-independent):

| Group           | Figure | \[**SHIFT**\]? | Button Name         | Description                                                       |
| --------------- | ------ | -------------- | ------------------- | ----------------------------------------------------------------- |
| 3 - MIXER       | 8      | \-             | MASTER LEVEL        | Controls the master output volume                                 |
| :::             | 9      | \-             | \[**MASTER CUE**\]  | Toggles master cue                                                |
| :::             | 10     | \-             | Crossfader Assign   | Crossfader assignment to deck, useless when using deck with Mixxx |
| :::             | 13     | \-             | HEADPHONES MIX      | Controls headphone's audio source (cue, master)                   |
| :::             | 15     | \-             | BOOTH MONITOR LEVEL | Controls the booth output volume                                  |
| 4 - FRONT PANEL | 2      | \-             | INPUT SELECT        | Controls deck source (PC, MIC, CD, PHONO, LINE)                   |

## Deck Functions

| Group    | Figure | \[**SHIFT**\]? | Button Name                  | Description                                                                                                                                                                        |
| -------- | ------ | -------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 - DECK | 1      | \-             | \[**PLAY/PAUSE**\]           | Toggles play/pause                                                                                                                                                                 |
| :::      | 1      | \[**SHIFT**\]  | \[**PLAY/PAUSE**\]           | Toggles play stutter                                                                                                                                                               |
| :::      | 2      | \-             | \[**CUE**\]                  | Toggles default cue (sets cue point/ goes to cue point)                                                                                                                            |
| :::      | 2      | \[**SHIFT**\]  | \[**CUE**\]                  | Toggles brake                                                                                                                                                                      |
| :::      | 3      | \-             | Jog dial (Platter)           | Vinyl-Mode enabled: performs scratching when pressed and rotated, Vinyl-Mode disabled: performs pitch bend                                                                         |
| :::      | 3      | \[**SHIFT**\]  | Jog dial (Platter)           | Vinyl-Mode enabled: performs scratching considering user-options multiplier when touched and rotated, Vinyl-Mode disabled: performs pitch bend considering user-options multiplier |
| :::      | 3      | \-             | Jog dial (Wheel side)        | Performs pitch bend when rotated                                                                                                                                                   |
| :::      | 3      | \[**SHIFT**\]  | Jog dial (Wheel side)        | Performs pitch bend when rotated considering user-options multiplier                                                                                                               |
| :::      | 4      | \-             | TEMPO                        | Controls pitch/tempo ratio                                                                                                                                                         |
| :::      | 5      | \-             | \[**KEYLOCK**\]              | Toggles keylock                                                                                                                                                                    |
| :::      | 5      | \[**SHIFT**\]  | \[**KEYLOCK**\]              | Changes TEMPO slider range: 8% -\> 16% -\> 32% -\> 64% -\> 100% -\> 8%...                                                                                                          |
| :::      | 5      | \-             | \[**KEYLOCK**\] (Long press) | Toggles pitch/tempo reset                                                                                                                                                          |
| :::      | 6      | \-             | \[**NEEDLE SEARCH**\]        | Jumps to equivalent absolute position in track                                                                                                                                     |
| :::      | 13     | \-             | \[**SYNC**\]                 | Toggles deck sync                                                                                                                                                                  |
| :::      | 13     | \[**SHIFT**\]  | \[**SYNC**\]                 | Toggles quantize function                                                                                                                                                          |
| :::      | 14     | \-             | \[**AUTO LOOP**\]            | Toggles a 4-Beat loop                                                                                                                                                              |
| :::      | 14     | \[**SHIFT**\]  | \[**AUTO LOOP**\]            | Toggles reloop                                                                                                                                                                     |
| :::      | 15     | \-             | \[**LOOP 1/2X**\]            | Halves active loop                                                                                                                                                                 |
| :::      | 15     | \[**SHIFT**\]  | \[**LOOP 1/2X**\]            | Moves active loop one beat backward (left)                                                                                                                                         |
| :::      | 16     | \-             | \[**LOOP 2X**\]              | Doubles active loop                                                                                                                                                                |
| :::      | 16     | \[**SHIFT**\]  | \[**LOOP 2X**\]              | Moves active loop one beat forward (right)                                                                                                                                         |
| :::      | 17     | \-             | \[**LOOP IN**\]              | Toggles loop in                                                                                                                                                                    |
| :::      | 18     | \-             | \[**LOOP OUT**\]             | Toggles loop out                                                                                                                                                                   |
| :::      | 18     | \[**SHIFT**\]  | \[**LOOP OUT**\]             | Toggles reloop / exit loop                                                                                                                                                         |
| :::      | 19     | \-             | \[**VINYL**\]                | Toggles vinyl (scratch) mode                                                                                                                                                       |
| :::      | 20     | \-             | \[**CENSOR**\]               | Toggles reverse roll play                                                                                                                                                          |
| :::      | 20     | \[**SHIFT**\]  | \[**CENSOR**\]               | Toggles reverse play                                                                                                                                                               |
| :::      | 21     | \-             | \[**SLIP**\]                 | Toggles slip mode                                                                                                                                                                  |
| :::      | 22     | \-             | \[**GRID ADJUST**\]          | Hold and touch/rotate Jog dial to adjust beats faster/slower                                                                                                                       |
| :::      | 22     | \[**SHIFT**\]  | \[**GRID ADJUST**\]          | Set/translate beat grid to current track position (adjust position with Jog dial)                                                                                                  |
| :::      | 23     | \-             | \[**GRID SLIDE**\]           | Hold and touch/rotate Jog dial to set/translate beat grid earlier/later                                                                                                            |
| :::      | 24     | \-             | \[**SHIFT**\]                | Switches to shifted controls, no direct function                                                                                                                                   |

## Effect Functions

Todo

## References

  - Product page:
    <https://www.pioneerdj.com/en/product/controller/ddj-sx/black/overview/>
  - Manual:
    <http://docs.pioneerdj.com/Manuals/DDJ_SX_DRI1096_manual/?_ga=1.221242769.826661553.1489418053>
  - MIDI:
    <https://pdj-ecom-cdn.azureedge.net/-/media/pioneerdj/software-info/controller/ddj-sx/ddj-sx_list_of_midi_messages_e.pdf?la=en>
  - Forum: <http://www.mixxx.org/forums/viewtopic.php?f=7&t=8310>
  - [Controller Scripting](midi_scripting)
  - [Mixxx Controls](mixxxcontrols)
