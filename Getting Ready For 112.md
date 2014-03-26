# Getting Controller Presets Ready for Mixxx 1.12.0

Script authors\! Mixxx 1.12.0 is almost here. Here is what you need to
know to get your controller presets ready.

## MIDI Script API Additions

### getParameter / setParameter

Your MIDI scripts no longer have to care about the minimum and maximum
value of potmeter/knob controls\! "Parameter" values range from 0 to 1.
If you set a parameter to 1 then the value of the control becomes the
maximum value. If you set the parameter to 0 then the value of the
control becomes the minimum value.

  - `engine.setParameter(group, item, parameter)`
  - `engine.getParameter(group, item)`

Example:

    engine.setParameter("[Channel1]", "rate", 0);

Is the same as:

    engine.setValue("[Channel1]", "rate", -1);

You don't have to build assumptions about the control into your scripts
now. **This is particularly important for effect parameters.** Since you
do not know ahead of time what the valid values of an effect parameter
are, you should always set effect parameters using `setParameter`.

### getParameterForValue

You can also call `getParameterForValue` to get the parameter for a
given value:

    // Returns 0
    engine.getParameterForValue("[Channel1]", "rate", -1)
    // Returns 1
    engine.getParameterForValue("[Channel1]", "rate", 1)

### reset

Calling `reset(group, item)` resets the control to its default value.

    // Resets the rate control to 0. (its default value)
    engine.reset("[Channel1]", "rate");
    
    // Resets the Master volume to 1. (its default value)
    engine.reset("[Master]", "volume");

## Master Sync

Mixxx finally has a master sync system\! There are two ways sync can
work:

  - Internal master
  - Deck master

When internal master is active, then all decks track an internal master
clock. A change to the rate of one deck changes the rate of all decks so
they stay in sync. You can also elect a particular deck as the master
deck.

### New Controls

|  | \[Group\]         |  | Key/Control   |  | Range       |  | What it does                                         |  | On-screen feedback                                               |  |
|  | ----------------- |  | ------------- |  | ----------- |  | ---------------------------------------------------- |  | ---------------------------------------------------------------- |  |
|  | \[InternalClock\] |  | bpm           |  | real-valued |  | The BPM of the internal master clock                 |  | Internal Clock BPM changes                                       |  |
|  | \[InternalClock\] |  | sync\_master  |  | binary      |  | Sets internal clock as master clock                  |  | MASTER button lights on internal master                          |  |
|  | \[Channel*N*\]    |  | sync\_enabled |  | binary      |  | Press: instant sync Hold: enable sync mode           |  | SYNC button lights & Pitch slider snaps to the appropriate value |  |
|  | \[Channel*N*\]    |  | sync\_master  |  | binary      |  | Sets deck as master clock                            |  | MASTER button lights                                             |  |
|  | \[Channel*N*\]    |  | sync\_mode    |  | toggle      |  | SYNC\_NONE = 0, SYNC\_FOLLOWER = 1, SYNC\_MASTER = 2 |  |                                                                  |  |

### Recommended Behavior

If your controller has a dedicated sync button, that button should be
mapped to `[ChannelN],sync_enabled`. This button will instant sync when
you press it and holding it will enable sync mode for the deck. You
should also bind this to your output so that the SYNC light on the
controller matches the deck's sync mode.

## Key Detection and Harmonic Mixing

Mixxx 1.12.0 detects the musical key of all tracks and allows pitch
adjustment independent of the player speed.

### New Controls

|  | \[Group\]      |  | Key/Control        |  | Range      |  | What it does                                                                                                  |  | On-screen feedback                        |  |
|  | -------------- |  | ------------------ |  | ---------- |  | ------------------------------------------------------------------------------------------------------------- |  | ----------------------------------------- |  |
|  | \[Channel*N*\] |  | sync\_key          |  | pushbutton |  | Adjust the key of the target deck to match that of the master deck.                                           |  | pitch knob adjusts, audible pitch changes |  |
|  | \[Channel*N*\] |  | pitch              |  | \-1.0..1.0 |  | Pitch adjust. -1 is a full octave shift down, +1 is a full octave shift up. Steps of 0.042 shift by semitones |  | Pitch knob                                |  |
|  | \[Channel*N*\] |  | pitch\_up          |  | pushbutton |  | Shift pitch up by one full step (2 semitones).                                                                |  | Pitch knob                                |  |
|  | \[Channel*N*\] |  | pitch\_up\_small   |  | pushbutton |  | Shift pitch up by one half step / semitone.                                                                   |  | Pitch knob                                |  |
|  | \[Channel*N*\] |  | pitch\_down        |  | pushbutton |  | Shift pitch down by one full step (2 semitones).                                                              |  | Pitch knob                                |  |
|  | \[Channel*N*\] |  | pitch\_down\_small |  | pushbutton |  | Shift pitch down by one half step / semitone.                                                                 |  | Pitch knob                                |  |
|  | \[Channel*N*\] |  | key                |  | 0 - 24     |  | Current musical key after pitch shifting.                                                                     |  | Key value widget                          |  |
|  | \[Channel*N*\] |  | file\_key          |  | 0 - 24     |  | File's musical key                                                                                            |  | Key value widget                          |  |

Key value definitions can be found here:
[keys.proto](https://github.com/mixxxdj/mixxx/blob/master/src/proto/keys.proto#L11)

### Recommended Behavior

  - If your controller has a pitch adjust knob for harmonic mixing, map
    it to `pitch`. 
  - If there is a sync key button, map it to `sync_key`.
  - If there are pitch adjust buttons, map them to the individual
    semitone pitch adjust buttons.

## Effects

## Vinyl Control Passthrough

Mixxx now supports passing through audio from vinyl control inputs into
the corresponding deck. This overrides the playing track in the deck
with whatever audio is coming from the turntable or CD player configured
for input.

### New Controls

|  | \[Group\]      |  | Key/Control |  | Range  |  | What it does                                                                                                    |  | On-screen feedback                  |  |
|  | -------------- |  | ----------- |  | ------ |  | --------------------------------------------------------------------------------------------------------------- |  | ----------------------------------- |  |
|  | \[Channel*N*\] |  | passthrough |  | toggle |  | Connects the vinyl control input for the deck to the channel output. Allows to mix external media into DJ sets. |  | GUI control currently missing FIXME |  |

### Recommended Behavior

  - If you expect your controller to be used by Vinyl Control users,
    consider mapping a spare button combination to the `passthrough`
    toggle control.

## Microphones and Auxiliary Inputs

### Microphone Ducking

## Mixer Changes

### Headphone Split Cueing

### Headphone and Master Delay

### Mute

## Deck Changes

### Beat Jump

### Loop Move

### Reverse Roll / Censor

### BPM Adjust Up/Down

## Library Changes

### Playlist / Sidebar Selector Knob

### Headline
