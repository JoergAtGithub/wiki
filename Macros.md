# Macro Format

This is the format specification for Mixxx Macros, a feature that allows
the recording and reproduction of jumps and particular control changes.

See [Mixxx Macros](Mixxx%20Macros) and [Mixxx Macros Requirements](Mixxx%20Macros%20Requirements)
for background on the project.

## Controls

### \[ChannelN\]

Currently implemented: status, activate, toggle, clear

| Key/Control        | Range              | What it does                                                                                  |
| ------------------ | ------------------ | --------------------------------------------------------------------------------------------- |
| show\_macros       | binary             | Whether to show the Macro Rack for this channel                                               |
| macro\_X\_status   | -1 - 4, read-only  | -1=no track loaded, 0=empty, 1=recording armed, 2=recording, 3=recorded, 4=playing            |
| macro\_X\_enabled  | binary             | Whether this Macro will automatically be started when the track is loaded                     |
| macro\_X\_loop     | binary             | Whether this Macro should loop infinitely                                                     |
| macro\_X\_activate | binary             | If playing, seek to beginning and start over. If recorded, enable. If unset, start recording. |
| macro\_X\_toggle   | binary             | If playing, stop. If recorded, enable. If unset, start recording.                             |
| macro\_X\_clear    | binary             | If Macro X is set, delete it and remove it from the Rack                                      |

## Storage

A Macro with its Actions is stored in the [protobuf format](https://github.com/xerus2000/mixxx/blob/macros/src/proto/macro.proto).

A table in the mixxxdb stores the binary blob of the Macro along with its name, the id of the corresponding track and its state (enabled/looped).