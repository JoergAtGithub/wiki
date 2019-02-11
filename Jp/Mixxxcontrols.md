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

## List of Controls

The default range is 0.0 to 1.0, unless otherwise noted. Binary means
that it is either 'ON' (non-zero) or 'OFF' (zero).

*Please keep the controls in alphabetical order within each group.*
