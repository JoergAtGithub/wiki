# Supported MIDI controller test grid

This grid is just used for verifying functionality of supported
controllers in the next version of Mixxx.

Currently reporting for: **Mixxx 1.7.0**

**Simply state *works* or *doesn't work* for controllers you've
tested.** If any buttons/sliders do not work as expected within Mixxx's
existing functionality, please fix them using the following information:

  - [MIDI controller mapping file
    format](midi_controller_mapping_file_format)
  - [MIDI Scripting](MIDI%20Scripting) if needed for tuning or complex
    behaviors

Otherwise report the reasons for not working to [our bug
tracker](https://launchpad.net/mixxx/+filebug).

(For details on a particular controller, please visit the [hardware
compatibility](hardware%20compatibility) page.)

|                                 |         |          |             |
| ------------------------------- | ------- | -------- | ----------- |
| Device                          | Windows | Mac OS X | Linux       |
| Hercules DJ Control Steel       |         |          |             |
| Hercules DJ Console RMX         | Works   | Works    | Works       |
| Hercules DJ Console Mk1         |         |          |             |
| Hercules DJ Console Mk2         | Works   | Works    | Works       |
| Hercules DJ Console Mac Edition |         |          |             |
| Hercules DJ Control MP3         | Works   | Works    | Works       |
| Stanton SCS.3d                  | Works   | Works    | Works       |
| Stanton SCS.1m                  | Works   |          | Works       |
| Mixman DM2                      |         |          | Works       |
| Tascam US-428                   |         |          |             |
| M-Audio X-Session Pro           |         | Works    | Works       |
| Evolution X-Session             |         |          |             |
| M-Audio Xponent                 |         |          | Works       |
| FaderFox DJ2                    |         |          |             |
| Vestax VCI-100                  |         |          |             |
| Numark Total Control            | Works   |          | Works \[1\] |
| Behringer BCD3000               |         |          | Works \[2\] |
| Akai MPD24                      |         | Works    | Works       |

1.  tested with 1.7. stable(opensuse-x86 11.0), No button lights
    (although alex markley's midi mapping for 1.6.2 worked nearly
    flawlessly) and crossfader needs inverting

2.  No button lights and jog wheels need tuning
