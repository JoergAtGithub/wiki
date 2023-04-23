# Macro Format

This is the format specification for Mixxx Macros, a feature that allows
the recording and reproduction of jumps and particular control changes.

See [Mixxx Macros](https://github.com/mixxxdj/mixxx/wiki/Macros-Project) and [Mixxx Macros Requirements](https://github.com/mixxxdj/mixxx/wiki/Macros-Project#requirements)
for background on the project.

## Controls

### \[ChannelN\]

show_macros not yet implemented because GUI is very ad-hoc

| Key/Control        | Range             | What it does                                                                                                                |
|--------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------|
| show\_macros       | binary            | Whether to show the Macro Rack for this channel                                                                             |
| macro\_X\_status   | -1 - 4, read-only | -1=no track loaded, 0=empty, 1=recording armed, 2=recording, 3=recorded, 4=playing                                          |
| macro\_X\_record   | binary            | Whether Macro recording is active. When activated while state is recorded(3), the new recording will be appended. Can be toggled with a button. |
| macro\_X\_play     | binary            | Whether the Macro is playing. Can be toggled with a button.                                                                 |
| macro\_X\_enable   | binary            | Whether the Macro will automatically be started when the track is loaded. Automatically set to true on play. Can be toggled. |
| macro\_X\_loop     | binary            | Whether the Macro should loop infinitely.                                                            |
| macro\_X\_activate | binary            | If playing, seek to beginning and start over. If recorded, start playing. If unset, start recording.                               |
| macro\_X\_toggle   | binary            | Toggle playback or recording, whichever fits the current state.                              |
| macro\_X\_clear    | binary            | If status is recorded(3), remove all actions. Keeps the label unless it was auto-generated.                             |


## Storage

A Macro with its Actions is stored in the [protobuf format](https://github.com/xerus2000/mixxx/blob/macros/src/proto/macro.proto).

A table in the mixxxdb stores the binary blob of the Macro along with its name, the id of the corresponding track and its state (enabled, looped).