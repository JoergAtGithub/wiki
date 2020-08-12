# Macro Format

This is the format specification for Mixxx Macros, a feature that allows
the recording and reproduction of jumps and particular control changes.

See [Mixxx Macros](Mixxx%20Macros) and [Mixxx Macros Requirements](Mixxx%20Macros%20Requirements)
for background on the project.

## Controls

### \[MacroRecording\]

| Key/Control | Range          | What it does                                                                                              | On-screen feedback |
|-------------|----------------|-----------------------------------------------------------------------------------------------------------|--------------------|
| record      | binary         | Arms Macro recording & stops it                                                                           | Recording icon     |
| status      | 0-2, read-only | Indicates whether a Macros is being recorded: 0 = no recording, 1 = recording armed, 2 = recording active | Recording icon     |
| deck?       | integer        | The deck the Macro is being recorded to (0 if the recording\_status \!= 2)                                | Toggle Button      |

### \[ChannelN\]

| Key/Control        | Range              | What it does                                                                                           |
| ------------------ | ------------------ | ------------------------------------------------------------------------------------------------------ |
| macros\_show(?)    | binary             | Whether to show the Macro Rack for this channel                                                        |
| macro\_X\_status   | -1 - 2, read-only  | -1=unset, 0=off, 1=armed, 2=running |
| macro\_X\_enabled  | binary             | Whether this Macro will automatically be started when the track is loaded                              |
| macro\_X\_loop     | binary             | Whether this Macro should loop infinitely                                                              |
| macro\_X\_activate | binary             | If Macro X exists, seek to the first action and start it. If Macro X is unset, start recording for it. |
| macro\_X\_set      | binary             | Record a Macro to slot X                                                                               |
| macro\_X\_clear    | binary             | If Macro X is set, delete it and remove it from the Rack                                               |

## Storage

A Macro with its Actions is stored in the [protobuf format](https://github.com/xerus2000/mixxx/blob/macros/src/proto/macro.proto).

A table in the mixxxdb will store the binary blob of the Macro along with its name, the corresponding track and its state (enabled/looped).