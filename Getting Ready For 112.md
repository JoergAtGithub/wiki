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

## Effects

## Key Detection and Harmonic Mixing

## Vinyl Control Passthrough

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
