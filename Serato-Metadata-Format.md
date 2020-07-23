For various file types, Serato [stores cue points in the metadata](http://serato.com/forum/discussion/345668) of the music files (e.g. as ID3 v 2.3 GEOB tags).

The format of these binary blobs has been partially documented [here](https://github.com/Holzhaus/serato-tags) and in [this blog post](http://homepage.ruhr-uni-bochum.de/jan.holthuis/posts/reversing-seratos-geob-tags).

Launchpad issue: <https://bugs.launchpad.net/mixxx/+bug/741613>

## Mixxx support status

This in an overview of which tags are currently read and parsed by Mixxx:

|              | ID3     | FLAC    | M4A     | Ogg Vorbis | *Description*
| ------------ | ------- | ------- | ------- | ---------- | ----------
| `Analysis`   | No      | No      | No      | No         | Serato Analysis version
| `Autotags`   | No      | No      | No      | No         | BPM and Gain values	
| `BeatGrid`   | *WIP*   | *WIP*   | *WIP*   | No         | Beatgrid Markers ([#2958](https://github.com/mixxxdj/mixxx/pull/2958))
| `Markers_`   | **Yes** | *n/a*   | **Yes** | No         | Hotcues, Saved Loops, etc.
| `Markers2`   | **Yes** | **Yes** | **Yes** | ?          | Hotcues, Saved Loops, etc.
| `Offsets_`   | No      | No      | No      | No         |
| `Overview`   | No      | No      | No      | No         | Overview Waveform data
| `RelVol`     | *n/a*   | No      | No      | *n/a*      |
| `VideoAssoc` | *n/a*   | No      | No      | *n/a*      |

See the [file format documentation](https://github.com/Holzhaus/serato-tags/blob/master/docs/fileformats.md) for details.

See also [serato\_database\_format](serato_database_format).
