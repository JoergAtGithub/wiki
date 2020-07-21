For various file types, Serato [stores cue points in the metadata](http://serato.com/forum/discussion/345668) of the music files (e.g. as ID3 v 2.3 GEOB tags).

The format of these binary blobs has been partially documented [here](https://github.com/Holzhaus/serato-tags) and in [this blog post](http://homepage.ruhr-uni-bochum.de/jan.holthuis/posts/reversing-seratos-geob-tags).

Launchpad issue: <https://bugs.launchpad.net/mixxx/+bug/741613>

## Mixxx support status

This in an overview of which tags are currently read and parsed by Mixxx:

|            | ID3     | FLAC    | M4A     | Ogg Vorbis |
| ---------- | ------- | ------- | ------- | ---------- |
| `Analysis` | No      | No      | No      | No         |
| `Autotags` | No      | No      | No      | No         |
| `BeatGrid` | [#2958](https://github.com/mixxxdj/mixxx/pull/2958)   | No      | No      | No         |
| `Markers_` | **Yes** | *n/a*   | **Yes** | No         |
| `Markers2` | **Yes** | **Yes** | **Yes** | ?          |
| `Offsets_` | No      | No      | No      | No         |
| `Overview` | No      | No      | No      | No         |

See the [file format documentation](https://github.com/Holzhaus/serato-tags/blob/master/docs/fileformats.md) for details.

See also [serato\_database\_format](serato_database_format).
