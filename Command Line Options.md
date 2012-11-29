# Command line options

Mixxx is designed to be as user-friendly as possible. As such, its
command line options are only useful for development or debugging, as
they make these tasks easier. Here is an exhaustive list:

*These are case-sensitive*

## 1.11

You can load supported sound files directly into the virtual decks by
specifying them at the command line.

| Option                                                                                                               | Description                                                                                                                                 | Code location              |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| *filename*                                                                                                           | Loads the specified music file at start-up (of the types Mixxx supports.) Each file you specify will be loaded into the next deck.          |                            |
| `-``-resourcePath path`                                                                                              | Top-level directory where Mixxx should look for its resource files such as controller presets, overriding the default installation location | configobject.cpp, line     |
| `-``-pluginPath path`                                                                                                | Top-level directory where Mixxx should look for for sound source plugins in addition to default locations                                   | soundsourceproxy.cpp, line |
| `-``-settingsPath path`                                                                                              | Top-level directory where Mixxx should look for settings.                                                                                   |                            |
| `-``-controllerDebug`                                                                                                | Causes Mixxx to display/log all of the MIDI/HID/etc. messages it receives and script functions it loads                                     |                            |
| `-`''-locale LOCALE `\|Use a custom locale for loading translations (e.g 'fr')\|main.cpp, line \| \|`-'`'-developer` | Enables a Developer menu item in the menu bar                                                                                               |                            |
| `-f`, `-``-fullScreen`                                                                                               | Causes Mixxx to start in full-screen mode                                                                                                   | main.cpp, line             |
| `-h`, `-``-help`                                                                                                     | Displays all current command line options                                                                                                   | main.cpp, line             |

## 1.10

You can load supported sound files directly into the virtual decks by
specifying them at the command line.

| Option                                                                                                                         | Description                                                                                                                            | Code location                 |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| *filename*                                                                                                                     | Loads the specified music file at start-up (of the types Mixxx supports.) Each file you specify will be loaded into the next deck.     | main.cpp, line FIXME          |
| `-``-resourcePath path`                                                                                                        | Top-level directory where Mixxx should look for its resource files such as MIDI mappings, overriding the default installation location | configobject.cpp, line 326    |
| `-``-pluginPath path`                                                                                                          | Top-level directory where Mixxx should look for for sound source plugins in addition to default locations                              | soundsourceproxy.cpp, line 78 |
| `-``-midiDebug`                                                                                                                | Causes Mixxx to display/log all of the MIDI messages it receives and script functions it loads                                         | mididevice.cpp, line 52       |
| `-`''-locale LOCALE `\|Use a custom locale for loading translations (e.g 'fr')\|main.cpp, line 229\| \|`-f'', `-``-fullScreen` | Causes Mixxx to start in full-screen mode                                                                                              | main.cpp, line 227            |
| `-h`, `-``-help`                                                                                                               | Displays all current command line options                                                                                              | main.cpp, line 183            |

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

## 1.7

| Option                                           | Description                                                                                                                            | Code location              |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `-``-resourcePath path`                          | Top-level directory where Mixxx should look for its resource files such as MIDI mappings, overriding the default installation location | configobject.cpp, line 301 |
| `-``-loadXMLfile // /path/to/mapping.midi.xml//` | Forces Mixxx to load the specified MIDI mapping on start-up instead of the last-used `MixxxMIDIBindings.xml`                           | midimapping.cpp, line 396  |
| `-``-midiDebug`                                  | Causes Mixxx to display/log all of the MIDI messages it receives *(Windows only, \>=1.7.1)*                                            | midiobjectwin.cpp, line 27 |
