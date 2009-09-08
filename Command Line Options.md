# Command line options

Mixxx is designed to be as user-friendly as possible. As such, its
command line options are only useful for development or debugging, as
they make these tasks easier. Here is an exhaustive list:

*These are case-sensitive*

## 1.7

| Option                                           | Description                                                                                                                            | Code location              |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `-``-resourcePath path`                          | Top-level directory where Mixxx should look for its resource files such as MIDI mappings, overriding the default installation location | configobject.cpp, line 301 |
| `-``-loadXMLfile // /path/to/mapping.midi.xml//` | Forces Mixxx to load the specified MIDI mapping on start-up instead of the last-used `MixxxMIDIBindings.xml`                           | midimapping.cpp, line 396  |
| `-``-midiDebug`                                  | Causes Mixxx to display/log all of the MIDI messages it receives *(Windows only, \>=1.7.1)*                                            | midiobjectwin.cpp, line 27 |
