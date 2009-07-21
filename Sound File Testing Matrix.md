# Supported sound file format test grid

This grid is just used for verifying functionality of supported sound
file formats in the next version of Mixxx. (These tables can be
generated from the `mixxx/src/test/soundFileFormats/generateFiles.sh
table` script.)

Currently reporting for: **Mixxx 1.7.0-beta1**

**Simply state *yes* or *no* for formats you've tested.** If any do not
work correctly or at all, please report a bug containing the file
format, sample rate, bit depth, number of channels (stereo/mono,) and OS
to [our bug tracker](https://launchpad.net/mixxx/+filebug). (If you can
include a sample file, that would also be helpful.)

**NOTE:** 32-bit in these tables means <span class="underline">32-bit
integer</span>. (32-bit float files of any type do not currently work in
Mixxx.)

## Windows

### WAVE/AIFF

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     | 16-bit    | 22050 Hz    | Yes           |
| Mono     | 16-bit    | 32000 Hz    | Yes           |
| Mono     | 16-bit    | 44100 Hz    | Yes           |
| Mono     | 16-bit    | 48000 Hz    | Yes           |
| Mono     | 16-bit    | 96000 Hz    | Yes           |
| Mono     | 24-bit    | 22050 Hz    | Yes           |
| Mono     | 24-bit    | 32000 Hz    | Yes           |
| Mono     | 24-bit    | 44100 Hz    | Yes           |
| Mono     | 24-bit    | 48000 Hz    | Yes           |
| Mono     | 24-bit    | 96000 Hz    | Yes           |
| Mono     | 32-bit    | 22050 Hz    | Yes           |
| Mono     | 32-bit    | 32000 Hz    | Yes           |
| Mono     | 32-bit    | 44100 Hz    | Yes           |
| Mono     | 32-bit    | 48000 Hz    | Yes           |
| Mono     | 32-bit    | 96000 Hz    | Yes           |
| Stereo   | 16-bit    | 22050 Hz    | Yes           |
| Stereo   | 16-bit    | 32000 Hz    | Yes           |
| Stereo   | 16-bit    | 44100 Hz    | Yes           |
| Stereo   | 16-bit    | 48000 Hz    | Yes           |
| Stereo   | 16-bit    | 96000 Hz    | Yes           |
| Stereo   | 24-bit    | 22050 Hz    | Yes           |
| Stereo   | 24-bit    | 32000 Hz    | Yes           |
| Stereo   | 24-bit    | 44100 Hz    | Yes           |
| Stereo   | 24-bit    | 48000 Hz    | Yes           |
| Stereo   | 24-bit    | 96000 Hz    | Yes           |
| Stereo   | 32-bit    | 22050 Hz    | Yes           |
| Stereo   | 32-bit    | 32000 Hz    | Yes           |
| Stereo   | 32-bit    | 44100 Hz    | Yes           |
| Stereo   | 32-bit    | 48000 Hz    | Yes           |
| Stereo   | 32-bit    | 96000 Hz    | Yes           |

### MP3

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     |           | 22050 Hz    | Yes           |
| Mono     |           | 32000 Hz    | Yes           |
| Mono     |           | 44100 Hz    | Yes           |
| Mono     |           | 48000 Hz    | Yes           |
| Stereo   |           | 22050 Hz    | Yes           |
| Stereo   |           | 32000 Hz    | Yes           |
| Stereo   |           | 44100 Hz    | Yes           |
| Stereo   |           | 48000 Hz    | Yes           |

### OGG Vorbis

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     |           | 22050 Hz    | No            |
| Mono     |           | 32000 Hz    | No            |
| Mono     |           | 44100 Hz    | No            |
| Mono     |           | 48000 Hz    | No            |
| Mono     |           | 96000 Hz    | No            |
| Stereo   |           | 22050 Hz    | Yes           |
| Stereo   |           | 32000 Hz    | Yes           |
| Stereo   |           | 44100 Hz    | Yes           |
| Stereo   |           | 48000 Hz    | Yes           |
| Stereo   |           | 96000 Hz    | Yes           |

### FLAC

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     | 16-bit    | 22050 Hz    |               |
| Mono     | 16-bit    | 32000 Hz    |               |
| Mono     | 16-bit    | 44100 Hz    |               |
| Mono     | 16-bit    | 48000 Hz    |               |
| Mono     | 16-bit    | 96000 Hz    |               |
| Mono     | 24-bit    | 22050 Hz    |               |
| Mono     | 24-bit    | 32000 Hz    |               |
| Mono     | 24-bit    | 44100 Hz    |               |
| Mono     | 24-bit    | 48000 Hz    |               |
| Mono     | 24-bit    | 96000 Hz    |               |
| Stereo   | 16-bit    | 22050 Hz    |               |
| Stereo   | 16-bit    | 32000 Hz    |               |
| Stereo   | 16-bit    | 44100 Hz    |               |
| Stereo   | 16-bit    | 48000 Hz    |               |
| Stereo   | 16-bit    | 96000 Hz    |               |
| Stereo   | 24-bit    | 22050 Hz    |               |
| Stereo   | 24-bit    | 32000 Hz    |               |
| Stereo   | 24-bit    | 44100 Hz    |               |
| Stereo   | 24-bit    | 48000 Hz    |               |
| Stereo   | 24-bit    | 96000 Hz    |               |

## Mac OSX

### WAVE/AIFF

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     | 16-bit    | 22050 Hz    |               |
| Mono     | 16-bit    | 32000 Hz    |               |
| Mono     | 16-bit    | 44100 Hz    |               |
| Mono     | 16-bit    | 48000 Hz    |               |
| Mono     | 16-bit    | 96000 Hz    |               |
| Mono     | 24-bit    | 22050 Hz    |               |
| Mono     | 24-bit    | 32000 Hz    |               |
| Mono     | 24-bit    | 44100 Hz    |               |
| Mono     | 24-bit    | 48000 Hz    |               |
| Mono     | 24-bit    | 96000 Hz    |               |
| Mono     | 32-bit    | 22050 Hz    |               |
| Mono     | 32-bit    | 32000 Hz    |               |
| Mono     | 32-bit    | 44100 Hz    |               |
| Mono     | 32-bit    | 48000 Hz    |               |
| Mono     | 32-bit    | 96000 Hz    |               |
| Stereo   | 16-bit    | 22050 Hz    |               |
| Stereo   | 16-bit    | 32000 Hz    |               |
| Stereo   | 16-bit    | 44100 Hz    |               |
| Stereo   | 16-bit    | 48000 Hz    |               |
| Stereo   | 16-bit    | 96000 Hz    |               |
| Stereo   | 24-bit    | 22050 Hz    |               |
| Stereo   | 24-bit    | 32000 Hz    |               |
| Stereo   | 24-bit    | 44100 Hz    |               |
| Stereo   | 24-bit    | 48000 Hz    |               |
| Stereo   | 24-bit    | 96000 Hz    |               |
| Stereo   | 32-bit    | 22050 Hz    |               |
| Stereo   | 32-bit    | 32000 Hz    |               |
| Stereo   | 32-bit    | 44100 Hz    |               |
| Stereo   | 32-bit    | 48000 Hz    |               |
| Stereo   | 32-bit    | 96000 Hz    |               |

### MP3

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     |           | 22050 Hz    |               |
| Mono     |           | 32000 Hz    |               |
| Mono     |           | 44100 Hz    |               |
| Mono     |           | 48000 Hz    |               |
| Stereo   |           | 22050 Hz    |               |
| Stereo   |           | 32000 Hz    |               |
| Stereo   |           | 44100 Hz    |               |
| Stereo   |           | 48000 Hz    |               |

### OGG Vorbis

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     |           | 22050 Hz    |               |
| Mono     |           | 32000 Hz    |               |
| Mono     |           | 44100 Hz    |               |
| Mono     |           | 48000 Hz    |               |
| Mono     |           | 96000 Hz    |               |
| Stereo   |           | 22050 Hz    |               |
| Stereo   |           | 32000 Hz    |               |
| Stereo   |           | 44100 Hz    |               |
| Stereo   |           | 48000 Hz    |               |
| Stereo   |           | 96000 Hz    |               |

### FLAC

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     | 16-bit    | 22050 Hz    |               |
| Mono     | 16-bit    | 32000 Hz    |               |
| Mono     | 16-bit    | 44100 Hz    |               |
| Mono     | 16-bit    | 48000 Hz    |               |
| Mono     | 16-bit    | 96000 Hz    |               |
| Mono     | 24-bit    | 22050 Hz    |               |
| Mono     | 24-bit    | 32000 Hz    |               |
| Mono     | 24-bit    | 44100 Hz    |               |
| Mono     | 24-bit    | 48000 Hz    |               |
| Mono     | 24-bit    | 96000 Hz    |               |
| Stereo   | 16-bit    | 22050 Hz    |               |
| Stereo   | 16-bit    | 32000 Hz    |               |
| Stereo   | 16-bit    | 44100 Hz    |               |
| Stereo   | 16-bit    | 48000 Hz    |               |
| Stereo   | 16-bit    | 96000 Hz    |               |
| Stereo   | 24-bit    | 22050 Hz    |               |
| Stereo   | 24-bit    | 32000 Hz    |               |
| Stereo   | 24-bit    | 44100 Hz    |               |
| Stereo   | 24-bit    | 48000 Hz    |               |
| Stereo   | 24-bit    | 96000 Hz    |               |

## Linux

### WAVE/AIFF

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     | 16-bit    | 22050 Hz    | Yes           |
| Mono     | 16-bit    | 32000 Hz    | Yes           |
| Mono     | 16-bit    | 44100 Hz    | Yes           |
| Mono     | 16-bit    | 48000 Hz    | Yes           |
| Mono     | 16-bit    | 96000 Hz    | Yes           |
| Mono     | 24-bit    | 22050 Hz    | Yes           |
| Mono     | 24-bit    | 32000 Hz    | Yes           |
| Mono     | 24-bit    | 44100 Hz    | Yes           |
| Mono     | 24-bit    | 48000 Hz    | Yes           |
| Mono     | 24-bit    | 96000 Hz    | Yes           |
| Mono     | 32-bit    | 22050 Hz    | Yes           |
| Mono     | 32-bit    | 32000 Hz    | Yes           |
| Mono     | 32-bit    | 44100 Hz    | Yes           |
| Mono     | 32-bit    | 48000 Hz    | Yes           |
| Mono     | 32-bit    | 96000 Hz    | Yes           |
| Stereo   | 16-bit    | 22050 Hz    | Yes           |
| Stereo   | 16-bit    | 32000 Hz    | Yes           |
| Stereo   | 16-bit    | 44100 Hz    | Yes           |
| Stereo   | 16-bit    | 48000 Hz    | Yes           |
| Stereo   | 16-bit    | 96000 Hz    | Yes           |
| Stereo   | 24-bit    | 22050 Hz    | Yes           |
| Stereo   | 24-bit    | 32000 Hz    | Yes           |
| Stereo   | 24-bit    | 44100 Hz    | Yes           |
| Stereo   | 24-bit    | 48000 Hz    | Yes           |
| Stereo   | 24-bit    | 96000 Hz    | Yes           |
| Stereo   | 32-bit    | 22050 Hz    | Yes           |
| Stereo   | 32-bit    | 32000 Hz    | Yes           |
| Stereo   | 32-bit    | 44100 Hz    | Yes           |
| Stereo   | 32-bit    | 48000 Hz    | Yes           |
| Stereo   | 32-bit    | 96000 Hz    | Yes           |

### MP3

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     |           | 22050 Hz    | Yes           |
| Mono     |           | 32000 Hz    | Yes           |
| Mono     |           | 44100 Hz    | Yes           |
| Mono     |           | 48000 Hz    | Yes           |
| Stereo   |           | 22050 Hz    | Yes           |
| Stereo   |           | 32000 Hz    | Yes           |
| Stereo   |           | 44100 Hz    | Yes           |
| Stereo   |           | 48000 Hz    | Yes           |

### OGG Vorbis

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     |           | 22050 Hz    | No            |
| Mono     |           | 32000 Hz    | No            |
| Mono     |           | 44100 Hz    | No            |
| Mono     |           | 48000 Hz    | No            |
| Mono     |           | 96000 Hz    | No            |
| Stereo   |           | 22050 Hz    | Yes           |
| Stereo   |           | 32000 Hz    | Yes           |
| Stereo   |           | 44100 Hz    | Yes           |
| Stereo   |           | 48000 Hz    | Yes           |
| Stereo   |           | 96000 Hz    | Yes           |

### FLAC

| Channels | Bit depth | Sample Rate | Does it work? |
| -------- | --------- | ----------- | ------------- |
| Mono     | 16-bit    | 22050 Hz    |               |
| Mono     | 16-bit    | 32000 Hz    |               |
| Mono     | 16-bit    | 44100 Hz    |               |
| Mono     | 16-bit    | 48000 Hz    |               |
| Mono     | 16-bit    | 96000 Hz    |               |
| Mono     | 24-bit    | 22050 Hz    |               |
| Mono     | 24-bit    | 32000 Hz    |               |
| Mono     | 24-bit    | 44100 Hz    |               |
| Mono     | 24-bit    | 48000 Hz    |               |
| Mono     | 24-bit    | 96000 Hz    |               |
| Stereo   | 16-bit    | 22050 Hz    |               |
| Stereo   | 16-bit    | 32000 Hz    |               |
| Stereo   | 16-bit    | 44100 Hz    |               |
| Stereo   | 16-bit    | 48000 Hz    |               |
| Stereo   | 16-bit    | 96000 Hz    |               |
| Stereo   | 24-bit    | 22050 Hz    |               |
| Stereo   | 24-bit    | 32000 Hz    |               |
| Stereo   | 24-bit    | 44100 Hz    |               |
| Stereo   | 24-bit    | 48000 Hz    |               |
| Stereo   | 24-bit    | 96000 Hz    |               |
