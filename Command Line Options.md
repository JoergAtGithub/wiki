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

## 1.8

You can load supported sound files directly into the virtual decks by
specifying them at the command line.

| Option                  | Description                                                                                                                            | Code location              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| *filename*              | Loads the specified music file at start-up (of the types Mixxx supports.) Each file you specify will be loaded into the next deck.     | main.cpp, line 281         |
| `-``-resourcePath path` | Top-level directory where Mixxx should look for its resource files such as MIDI mappings, overriding the default installation location | configobject.cpp, line 310 |
| `-``-midiDebug`         | Causes Mixxx to display/log all of the MIDI messages it receives and script functions it loads                                         | mididevice.cpp, line 52    |
| `-f`, `-``-fullScreen`  | Causes Mixxx to start in full-screen mode                                                                                              | main.cpp, line 276         |
| `-h`, `-``-help`        | Displays all current command line options                                                                                              | main.cpp, line 249         |
