# Engine Prime File/Database Format

## Overview

This document aims to describe the file format and database schema used
by Denon DJ's Engine Prime software. The same format is also used by
Denon DJ's standalone SC5000 Prime professional DJ players.

The purpose of the data written is to capture information about audio
tracks that may be played through SC5000 Prime players. Either an SC5000
player itself, or the Engine Prime software running on a normal
computer, can identify and write this analysis data.

The SC5000 player accepts either a USB stick or SD card as media.

## Filesystem Structure

On a USB stick, the filesystem structure is as follows:

> /
> 
> /Engine Library
> 
> /Engine Library/m.db
> 
> /Engine Library/m.db-journal
> 
> /Engine Library/p.db
> 
> /Engine Library/p.db-journal
> 
> /Engine Library/sm.db
> 
> /Engine Library/sm.db-journal
> 
> /Engine Library/sp.db
> 
> /Engine Library/sp.db-journal

The `.db` files are SQLite database files. The `.db-journal` files
appear to be rollback journals, which are supposed to be temporary
files, but for some reason are retained. Further information about
[temporary files used by SQLite](https://sqlite.org/tempfiles.html) is
available on the SQLite website.

## `m.db` Database Schema

The 'm' database is the main location for storing metadata about
music/audio tracks.

### `AlbumArt`

Each row represents a single image that can be used as 'album art' for
any number of audio tracks.

By default, there is always an entry with `id` equal 1, with `hash` and
`albumArt` set to NULL, which represents 'no album art'. So, a track
which does not have any art would have `track.idAlbumArt` set to 1.

As the image data is embedded in the database `albumArt` column as a
BLOB directly, the hash field is used to avoid duplication of identical
album art across multiple tracks. If multiple tracks have the same album
art (as determined by hashing the image data), then only one entry
should be written in `AlbumArt` and all such tracks should set their
`track.idAlbumArt` column to point to it.

**TBC** - unsure how the hash is computed. It appears to be an SHA1 hash
from the length, but not sure what it is a hash of.

| Column   | Type    | Meaning               |
| -------- | ------- | --------------------- |
| id       | INTEGER | Surrogate primary key |
| hash     | TEXT    | Hash of image data    |
| albumArt | BLOB    | Binary image data     |

### `CopiedTrack`

**TODO** - unsure what a row represents. Perhaps when a track is played
from a linked media device (e.g. USB stick on another SC5000 player
connected via network cable), the track is copied into the local
database? Is the file copied too (assume not, because of space reasons)?

| Column                    | Type    | Meaning                                           |
| ------------------------- | ------- | ------------------------------------------------- |
| trackId                   | INTEGER | Primary key, and also a foreign key to `Track.id` |
| uuidOfSourceDatabase      | TEXT    | **???**                                           |
| idOfTrackInSourceDatabase | INTEGER | **???**                                           |

### `Crate`

Each row represents a 'Crate', i.e. a unique subset of unordered tracks
in the overall collection, grouped together for DJ convenience.

| Column | Type    | Meaning                                                              |
| ------ | ------- | ---------------------------------------------------------------------|
| id     | INTEGER | Surrogate primary key                                                |
| title  | TEXT    | Short title for the crate                                            |
| path   | TEXT    | Parent crate(s) separated by semicolons ending with the crate's name |

### `CrateHierarchy`

Each row represents an optional relationship between a parent and child
crate.

| Column       | Type    | Meaning                                 |
| ------------ | ------- | --------------------------------------- |
| crateId      | INTEGER | Parent crate, foreign key to `Crate.id` |
| crateIdChild | INTEGER | Child crate, foreign key to `Crate.id`  |

### `CrateParentList`

Each row represents **???**

| Column        | Type    | Meaning                                                                        |
| ------------- | ------- | ------------------------------------------------------------------------------ |
| crateOriginId | INTEGER | ID of crate in the Crate view, foreign key to `Crate.id`                       |
| crateParentId | INTEGER | ID the the crate's IMMEDIATE parent from Crate view, foreign key to `Crate.id` |

### `CrateTrackList`

Each row represents a statement that a given track is part of a given
crate. A track may belong to any number of crates

| Column  | Type    | Meaning                          |
| ------- | ------- | -------------------------------- |
| crateId | INTEGER | Crate, foreign key to `Crate.id` |
| trackId | INTEGER | Track, foreign key to `Track.id` |

### `Historylist`

Each row represents an instance when the media containing the current
database was played on a compatible player.

| Column | Type    | Meaning                                                                                                                                              |
| ------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| id     | INTEGER | Surrogate primary key                                                                                                                                |
| title  | TEXT    | Title of the 'instance' when this database was loaded on a player, which on Denon SC5000 players appears to be titled "History 1", "History 2", etc. |

### `HistorylistTrackList`

Each row represents a track that was loaded and played from the current
database.

**TBC** - how much of a track needs to be played before it appears in
this table?

**TBC** - if tracks from another database are played on the same player
that the media holding this database is plugged into, are those foreign
tracks recorded in this table?

| Column                  | Type    | Meaning                                                                                                                                                    |
| ----------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| historylistId           | INTEGER | Foreign key to `Historylist.id`                                                                                                                            |
| trackId                 | INTEGER | The track that was played, foreign key to `Track.id`                                                                                                       |
| trackIdInOriginDatabase | INTEGER | **???** appears to be the same as `trackId` for tracks on the same database; presumably holds the 'foreign' track id if the track is from another database |
| databaseUuid            | TEXT    | Unique identifier for the track's database, as held in `Information.uuid`                                                                                  |
| date                    | INTEGER | Date/time, expressed as a UNIX timestamp, when the track was played                                                                                        |

### `Information`

Single-row table containing metadata about the current Engine Library
database.

The schema is versioned according to a typical three-part version
indicator (presumably according to [Semantic
Versioning](http://semver.org)). When the original author of this
document tried this out on a newly-bought Denon SC5000 Prime purchased
in August 2017, the schema version created by the player was v1.6.0.

| Column                 | Type    | Meaning                                                                                                                                                                                                                                                             |
| ---------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                     | INTEGER | Surrogate primary key                                                                                                                                                                                                                                               |
| uuid                   | TEXT    | Unique identifier for this Engine Library, in order to distinguish from other Engine Prime libraries on other media.                                                                                                                                                |
| schemaVersionMajor     | INTEGER | Major part of the three-part version number for the Engine Prime library schema.                                                                                                                                                                                    |
| schemaVersionMinor     | INTEGER | Minor part of the three-part version number for the Engine Prime library schema.                                                                                                                                                                                    |
| schemaVersionPatch     | INTEGER | Patch part of the three-part version number for the Engine Prime library schema.                                                                                                                                                                                    |
| currentPlayedIndicator | INTEGER | A hash of some kind, in the form of an 64-bit number, which can be used to find all tracks that have been played in the most recent 'playthrough' of tracks from the current database. The number will appear in the `MetaDataInteger` table for values of type 10. |

### `MetaData`

Each row represents some kind of textual (non-numeric) track meta-data,
as distinguished by a reference to the track and a reference to the type
of metadata for that row.

Meanings of the `type` column:

1.  Title
2.  Artist
3.  Album
4.  Genre
5.  Comment
6.  Publisher
7.  Composer
8.  **TBC** - seems to always be set to `NULL`
9.  **TBC** - seems to always be set to `NULL`
10. Duration in MM:SS
11. \*Unused - no entries should be made in `Metadata` for this value of
    `type`\*
12. Whether the track has ever been played and added to
    `HistorylistTrackList`; set to 1 if it has, or `NULL` if not
13. File extension, one of:

<!-- end list -->

  - wav
  - aiff
  - mp3
  - flac
  - m4a
  - ogg

<!-- end list -->

14.  \*Unused - no entries should be made in `Metadata` for this value of
    `type`\*
15.  Analysed flag. Is set to 1 if track is analyzed. Setting this to 0 triggers track analysis (when automatic is set in preferences)
16.  **TBC** - seems to always be set to 1

| Column | Type    | Meaning                                                          |
| ------ | ------- | ---------------------------------------------------------------- |
| id     | INTEGER | Track identifier, part of primary key, foreign key to `Track.id` |
| type   | INTEGER | Type of metadata, part of primary key.                           |
| text   | TEXT    | Textual value of metadata                                        |

### `MetaDataInteger`

Each row represents some kind of whole-number numeric track meta-data,
as distinguished by a reference to the track and a reference to the type
of metadata for that row.

Meanings of the `type` column:

1.  Date/time, expressed as a UNIX timestamp, when the track was last
    played (will match the entry in `HistorylistTrackList`); set to
    `NULL` if not ever played
2.  Date/time, expressed as a UNIX timestamp, of the file's last *status
    change*
3.  Date, expressed as a UNIX timestamp, of the file's last load
    (rounded to midnight GMT) **TBC** - confirm exactly what file time
    property this refers to, i.e. is it load, play, prepare, something
    else?
4.  The musical key of the track, as determined by track analysis; the
    values should be interpreted as follows:

<!-- end list -->
  - 0 =\> 8B / C major
  - 1 =\> 8A / A minor
  - 2 =\> 9B / G major
  - 3 =\> 9A / E minor
  - 4 =\> 10B / D major
  - 5 =\> 10A / B minor
  - 6 =\> 11B / A major
  - 7 =\> 11A / F\# minor
  - 8 =\> 12B / E major
  - 9 =\> 12A / Db minor
  - 10 =\> 1B / B major
  - 11 =\> 1A / Ab minor
  - 12 =\> 2B / F\# major
  - 13 =\> 2A / Eb minor
  - 14 =\> 3B / Db major
  - 15 =\> 3A / Bb minor
  - 16 =\> 4B / Ab major
  - 17 =\> 4A / F minor
  - 18 =\> 5B / Eb major
  - 19 =\> 5A / C minor
  - 20 =\> 6B / Bb major
  - 21 =\> 6A / G minor
  - 22 =\> 7B / F major
  - 23 =\> 7A / D minor


<!-- end list -->

5.  Rating, a value in [0, 20, 40, 60, 80, 100, 120]. 100 and 120 both relate to 5 stars, so 120 is probably a bug from Engine Prime's user interface.
2.  **TBC** - unsure, not populated for any sample tracks
3.  **TBC** - unsure, not populated for any sample tracks
4.  **TBC** - unsure, not populated for any sample tracks
5.  **TBC** - unsure, not populated for any sample tracks
6.  A 64-bit number acting as a hash that indicates which tracks have
    been played in the most recent 'playthrough' of songs from this
    database. See the `currentPlayedIndicator` column in the
    `Information` table. The field is not populated if a track hasn't
    ever been played (i.e. doesn't appear in the `HistorylistTrackList`
    table). Unsure if the number has any inherent meaning other than for
    hashing.
7.  **TBC** - unsure, seems to be set to 1 for all sample tracks

| Column | Type    | Meaning                                                          |
| ------ | ------- | ---------------------------------------------------------------- |
| id     | INTEGER | Track identifier, part of primary key, foreign key to `Track.id` |
| type   | INTEGER | Type of metadata, part of primary key.                           |
| value  | INTEGER | Integer value of metadata                                        |

### `Playlist`

Each row represents a playlist.

| Column | Type    | Meaning               |
| ------ | ------- | --------------------- |
| id     | INTEGER | Surrogate primary key |
| title  | TEXT    | Name of the playlist  |

### `PlaylistTrackList`

Each row represents a track in a particular playlist.

| Column                  | Type    | Meaning                                                                                      |
| ----------------------- | ------- | -------------------------------------------------------------------------------------------- |
| playlistId              | INTEGER | Playlist identifier, foreign key to `Playlist.id`                                            |
| trackId                 | INTEGER | Track identifier, foreign key to `Track.id`                                                  |
| trackIdInOriginDatabase | INTEGER | **TBC** - presumably holds the 'foreign' track id if the track is from another database      |
| databaseUuid            | TEXT    | **TBC** - presumably the UUID of the foreign database, if the track is from another database |
| trackNumber             | INTEGER | **TBC**                                                                                      |

### `Preparelist`

There is normally just one row in the `Preparelist` table, representing
a list of tracks that are being 'prepared' for playback.

| Column | Type    | Meaning                                                        |
| ------ | ------- | -------------------------------------------------------------- |
| id     | INTEGER | Surrogate primary key                                          |
| title  | TEXT    | Name of the prepare list; the default list is called "Prepare" |

### `PreparelistTrackList`

Each row represents a track that has been 'prepared' for later playing.

Note that after a track in the prepare list is loaded onto a player, the
SC5000 Prime removes it from the prepare list.

| Column                  | Type    | Meaning                                                                                                  |
| ----------------------- | ------- | -------------------------------------------------------------------------------------------------------- |
| playlistId              | INTEGER | Prepare list identifier, foreign key to `Preparelist.id`; column name clearly a copy/paste typo          |
| trackId                 | INTEGER | Track identifier, foreign key to `Track.id`                                                              |
| trackIdInOriginDatabase | INTEGER | **TBC** - presumably holds the 'foreign' track id if the track is from another database                  |
| databaseUuid            | TEXT    | **TBC** - presumably the UUID of the foreign database, if the track is from another database             |
| trackNumber             | INTEGER | **TBC** - presumably an sorting key to put tracks in a given order within a given `Preparelist.id` value |

### `Track`

Each row in the table represents a single audio track that is already
stored as a file.

| Column                    | Type    | Meaning                                                                                                                                        |
| ------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| id                        | INTEGER | Surrogate primary key                                                                                                                          |
| playOrder                 | INTEGER | Set to the track number embedded in the audio file's metadata, or `NULL` if not available                                                      |
| length                    | INTEGER | Length of the track, in seconds (rounded up), as reported by the file's metadata                                                               |
| lengthCalculated          | INTEGER | Length of the track, in seconds (rounded up), as determined by track analysis                                                                  |
| bpm                       | INTEGER | Whole-number tempo of the track, as reported by the audio file's metadata                                                                      |
| year                      | INTEGER | Year of the track, as reported by the audio file's metadata                                                                                    |
| path                      | TEXT    | Path to the audio file on disk, *relative to the Engine Library directory*                                                                     |
| filename                  | TEXT    | Name of the audio file (without any directory prefix)                                                                                          |
| bitrate                   | INTEGER | Bitrate of the audio file                                                                                                                      |
| bpmAnalyzed               | REAL    | Real number tempo of the track, as determined by track analysis, and usually (but not always) rounded to 1 decimal place                       |
| trackType                 | INTEGER | **TBC** - always set to 1                                                                                                                      |
| isExternalTrack           | NUMERIC | **TBC** - presumably for 'importing' tracks from linked media on other SC5000 decks into the local database? For local tracks, always set to 0 |
| uuidOfExternalDatabase    | TEXT    | **TBC** - presumably the UUID of the external database, if the track is external (or `NULL` if `isExternalTrack` is zero)                      |
| idTrackInExternalDatabase | INTEGER | **TBC** - presumably the id of the track in the external database, if the track is external (or `NULL` if `isExternalTrack` is zero)           |
| idAlbumArt                | INTEGER | Foreign key to `AlbumArt.id`                                                                                                                   |

## `p.db` Database Schema

The 'p' database is the main location for persisting analysed
performance information about tracks, such as cues, beat grids, and
waveforms.

### `Information`

Single-row table containing metadata about the current Engine Library
database.

The schema is versioned according to a typical three-part version
indicator (presumably according to [Semantic
Versioning](http://semver.org)). When the original author of this
document tried this out on a newly-bought Denon SC5000 Prime purchased
in August 2017, the schema version created by the player was v1.6.0.

Note that the UUID in the `p.db` database will not be the same as that
in the `m.db` database.

| Column                 | Type    | Meaning                                                                                                              |
| ---------------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| id                     | INTEGER | Surrogate primary key                                                                                                |
| uuid                   | TEXT    | Unique identifier for this Engine Library, in order to distinguish from other Engine Prime libraries on other media. |
| schemaVersionMajor     | INTEGER | Major part of the three-part version number for the Engine Prime library schema.                                     |
| schemaVersionMinor     | INTEGER | Minor part of the three-part version number for the Engine Prime library schema.                                     |
| schemaVersionPatch     | INTEGER | Patch part of the three-part version number for the Engine Prime library schema.                                     |
| currentPlayedIndicator | INTEGER | Always set to 0 for the `p.db` database                                                                              |

### `PerformanceData`

Each row represents information about a track that has been determined
by track analysis and preparation, such as the location of hot cues,
loops, the beat grid, as well as waveform data.

| Column                     | Type    | Meaning                                                                              |
| -------------------------- | ------- | ------------------------------------------------------------------------------------ |
| id                         | INTEGER | Track identifier; soft foreign key to `Track.id` in `m.db`                           |
| isAnalyzed                 | NUMERIC | 1 if the track has been analysed, 0 if not                                           |
| isRendered                 | NUMERIC | **TBC** - seems to always be set to 0                                                |
| trackData                  | BLOB    | Compressed track data (see below)                                                    |
| highResolutionWaveFormData | BLOB    | Compressed detailed waveform data (see below)                                        |
| overviewWaveFormData       | BLOB    | Compressed high-level waveform data (see below)                                      |
| beatData                   | BLOB    | Compressed beat data (see below)                                                     |
| quickCues                  | BLOB    | Compressed hot cue data (see below)                                                  |
| loops                      | BLOB    | Loop data (not compressed, see below)                                                |
| hasSeratoValues            | NUMERIC | **TBC** - presumably 1 if the track was imported from a Serato database, or 0 if not |

## `sm.db` Database Schema

On a sample USB stick, the 'sm' database is apparently identical to the
'm' database in schema, but with no values populated in any tables apart
from the Information table.

**TBC** - perhaps the 's' in 'sm' stands for Serato?

## `sp.db` Database Schema

On a sample USB stick, the 'sp' database is apparently identical to the
'p' database in schema, but with no values populated in any tables apart
from the Information table.

**TBC** - perhaps the 's' in 'sp' stands for Serato?

## `PerformanceData` Encoding Format

The `PerformanceData` table in the `p.db` database contains a number of
`BLOB` columns, most of which are a compressed binary format. These are
described below.

### Compression

With the exception of the `loops` column, the `BLOB`s are compressed
using zlib, but the compressed data payload is prefixed with an unsigned
32-bit integer containing the uncompressed data length. This is the
format used by the `qCompress` and `qUncompress` [convenience
methods](http://doc.qt.io/qt-5/qbytearray.html#qUncompress) of the
`QByteArray` class from the QT library, a library which is used by
Engine Prime. If you extract compressed `BLOB` data directly from the
SQLite database, you *will* need to uncompress it first to examine the
contents.

An example C++ program which can do this is shown below:

``` cpp
#include <iostream>
#include <QtCore>

int main(int argc, char**argv)
{
    if (argc != 2)
    {
        std::cerr << "Usage:" << std::endl;
        std::cerr << argv[0] << " hexstring" << std::endl;
        return 1;
    }
    
    QByteArray blob = QByteArray::fromHex(argv[1]);

    // Uncompress
    QByteArray uncompressed = qUncompress(blob);
    if (uncompressed.isEmpty())
    {
        std::cerr << "Corrupt input, unable to uncompress" << std::endl;
        return 1;
    }

    // Print hexdump of the buffer
    std::cout << uncompressed.toHex().data() << std::endl;
}
```

Example usage (assuming the above source file is compiled to a binary
called "ep\_uncompress"):

``` bash
$ sqlite3 p.db "select hex(trackData) from PerformanceData where id = 1;" | xargs ./ep_uncompress 
40e58880000000000000000001337a003fe2342ca00000000000000b
$
```

### Note on track positions

A number of fields in the PerformanceData `BLOB`s refer to positions
within the track. These positions are usually measured in *samples*,
rather than elapsed time. To convert to seconds, you will need to divide
by the track's sample rate, which is stored in both `trackData` and
`beatData`. The vast majority of tracks downloaded from the internet
will have 44100Hz as their sample rate, although 48000Hz makes an
appearance on occasion too.

Furthermore, some position fields (for example, in `beatData` and
`loops`) are stored as doubles but in *little-endian* format, and so the
endianness will need to be changed before working with the numbers. The
below function can do this for a 64-bit integer (containing the bits
that will subsequently be interpreted as a double):

``` cpp
uint64_t change_endianness(uint64_t v)
{
    uint64_t result = 0;
    result |= (v & 0x00000000000000ff) << 56;
    result |= (v & 0x000000000000ff00) << 40;
    result |= (v & 0x0000000000ff0000) << 24;
    result |= (v & 0x00000000ff000000) << 8;
    result |= (v & 0x000000ff00000000) >> 8;
    result |= (v & 0x0000ff0000000000) >> 24;
    result |= (v & 0x00ff000000000000) >> 40;
    result |= (v & 0xff00000000000000) >> 56;
    return result;
}
```

#### Standard Cue/Loop Colours

The standard cue/loop colours are shown below:

[[/media/standardcuecolours.png|]]

| Cue/Loop No. | RGB ([Hex triplet](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet)) |
| ------------ | ------------------------------------------------------------------------- |
| 1            | EAC532                                                                    |
| 2            | EA8F32                                                                    |
| 3            | B855BF                                                                    |
| 4            | BA2A41                                                                    |
| 5            | 86C64B                                                                    |
| 6            | 20C67C                                                                    |
| 7            | 00A8B1                                                                    |
| 8            | 158EE2                                                                    |

### `trackData` Format

| Field                                                                        | Type   | Values                                  |
| ---------------------------------------------------------------------------- | ------ | --------------------------------------- |
| Sample rate of track (in Hz)                                                 | double | Usually 44100                           |
| Length of track (in samples)                                                 | uint64 | Positive number                         |
| **TODO** - Average track loudness, calculation unsure (RMS?), 0 if not known | double | Range 0-1                               |
| Analysed key of track                                                        | uint32 | As per MetadataInteger (for `type` = 4) |

### `highResolutionWaveFormData` Format

**TODO** - not documented yet

### `overviewWaveFormData` Format

**TODO** - not documented yet

### `beatData` Format

The `beatData` format has two sub-structures nested within it: the beat
grid, and a beat grid marker. There are two beat grids in each field:
one for the *default* beat grid (as analyzed by Engine Prime or an
SC5000) and an *adjusted* beat grid (if you mess around with it by
hand). Each beat grid contains a number of beat grid markers, of which
there are a minimum of two.

The *first* beat marker in any beat grid is always "beat -4", i.e. four
beats before the first usable beat in the track. Hence, its sample
offset in the file is negative (before the start of the track\!).
Naturally, it is not possible to actually play any audio from a period
in time before the track has actually begun, but the position is still
useful to allow for the beat grid to be manually adjusted by up to 4
beats.

The *last* beat marker in any beat grid is always "beat N + 1", i.e. one
beat past the last usable beat in the track. Hence, its sample offset in
the file is beyond the last sample in the track.

Also note that when discussing the index/number of any given beat, the
`beatData` format always assumes that the first beat in the file is beat
0, and the last is beat N. The index/number of a given beat is not shown
to the end user in either Engine Prime or an SC5000's display.

Note that the BPM can be calculated from the information in `beatData`
as follows:

> BPM = SampleRate \* 60 \* (LastMarkerBeatIndex - FirstMarkerBeatIndex)
> / (LastMarkerSampleOffset - FirstMarkerSampleOffset)

Main `beatData` format:

| Field                                        | Type     | Values          |
| -------------------------------------------- | -------- | --------------- |
| Sample Rate (in Hertz)                       | double   | usually 44100   |
| Track length (in samples)                    | double   | positive number |
| Is beat data set (always 1)                  | byte     | always 1        |
| Default beatgrid                             | beatgrid | see below..     |
| Adjusted beatgrid (same as default if unadj) | beatgrid | see below..     |

`beatgrid` format:

| Field                                  | Type      | Values            |
| -------------------------------------- | --------- | ----------------- |
| Number N of "markers" in this beatgrid | uint64    | 2 or 3, usually 2 |
| Beat grid marker (repeated N times)    | marker\*N | see below..       |

`marker` format:

| Field                                         | Type                     | Values               |
| --------------------------------------------- | ------------------------ | -------------------- |
| Sample offset                                 | double (little-endian\!) | \-ve or +ve number\! |
| Beat number/index                             | int64 (little-endian\!)  | \-ve or +ve number\! |
| Number of beats until next marker (0 if done) | uint32 (little-endian\!) | \+ve, or 0 if done   |
| Unknown field?\!?                             | uint32 (little-endian\!) | ???                  |

**TODO** - there is still an unknown value in the beat grid marker
sub-structure. This is populated with varying values, but its exact form
and function is not currently known.

#### Example `beatData` field

As `beatData` is one of the more complex fields in the Engine Library
format, an example always helps. The below is from an example track,
where the beatgrid has been adjusted in Engine Prime to correct a
mis-identified tempo (wrongly thought to be 97, but was actually 108.3):

| Field                              | Value       |
| ---------------------------------- | ----------- |
| Sample Rate (in Hertz)             | 44100       |
| Track length (in samples)          | 16988686    |
| Is beat data set (always 1)        | 1           |
| **Default beatgrid**               |             |
| Num markers                        | 2           |
| 1st marker offset                  | \-88813.78  |
| 1st marker beat index              | \-4         |
| 1st marker beats until next marker | 628         |
| 1st marker unknown field           | ???         |
| 2nd marker offset                  | 17000758.37 |
| 2nd marker beat index              | 624         |
| 2nd marker beats until next marker | 0           |
| 2nd marker unknown field           | ???         |
| **Adjusted beatgrid**              |             |
| Num markers                        | 2           |
| 1st marker offset                  | \-57722.04  |
| 1st marker beat index              | \-4         |
| 1st marker beats until next marker | 698         |
| 1st marker unknown field           | ???         |
| 2nd marker offset                  | 16995906.29 |
| 2nd marker beat index              | 694         |
| 2nd marker beats until next marker | 0           |
| 2nd marker unknown field           | ???         |

Using the adjusted beatgrid values above, the BPM can be calculated as:

> BPM = 44100 \* 60 \* (694 + 4) / (16995906.29 + 57722.04) = 108.3

### `quickCues` Format

Note that the `quickCues` format has the hot cue label length, label,
position, and colour fields 8 times sequentially, for each of the 8 hot
cues. This is shown in the below table as a 'repeating frame', for
brevity. Also note that since cue labels can be of varying length, each
repeating frame can also be of varying length.

| Field                                                | Type      | Values              |
| ---------------------------------------------------- | --------- | ------------------- |
| Num Hot Cues                                         | uint64    | Always 8            |
| *(begin repeating frame)*                            |           |                     |
| Hot Cue Label Length (0 = no cue point set)          | byte      | 1-255               |
| Hot Cue Label (no null terminator)                   | char \* N | e.g. "Cue 1"        |
| Hot Cue position (in samples, or -1 if none)         | double    | real number         |
| Hot Cue Colour - Alpha                               | byte      | Always 255          |
| Hot Cue Colour - Red                                 | byte      | 0-255 (dark-bright) |
| Hot Cue Colour - Green                               | byte      | 0-255 (dark-bright) |
| Hot Cue Colour - Blue                                | byte      | 0-255 (dark-bright) |
| *(end repeating frame)*                              |           |                     |
| Main cue position (i.e. using cue button)            | double    | real number         |
| Whether main cue position is overridden from default | byte      | 0 or 1              |
| Default auto-detected cue position                   | double    | real number         |

### `loops` Format

Note that the `loops` format has the loop label length, label, position,
and colour fields 8 times sequentially, for each of the 8 loops. This is
shown in the below table as a 'repeating frame', for brevity. Also note
that since labels can be of varying length, each repeating frame can
also be of varying length.

Note also that, unlike the other fields in `PerformanceData`, `loops` is
not compressed.

| Field                                       | Type                     | Values              |
| ------------------------------------------- | ------------------------ | ------------------- |
| Num Loops                                   | byte                     | Always 8            |
| Padding                                     | byte \* 7                | Always 0            |
| *(begin repeating frame)*                   |                          |                     |
| Loop Label Length (0 = no loop set)         | byte                     | 1-255               |
| Loop Label (no null terminator)             | char \* N                | e.g. "Loop 1"       |
| Start position (in samples, -1 = not set)   | double (little-endian\!) | \+ve number         |
| End position (in samples, -1 = not set)     | double (little-endian\!) | \+ve number         |
| Loop start point set (0 = not set, 1 = set) | byte                     | 0 or 1              |
| Loop end point set (0 = not set, 1 = set)   | byte                     | 0 or 1              |
| Loop Colour - Alpha                         | byte                     | Always 255          |
| Loop Colour - Red                           | byte                     | 0-255 (dark-bright) |
| Loop Colour - Green                         | byte                     | 0-255 (dark-bright) |
| Loop Colour - Blue                          | byte                     | 0-255 (dark-bright) |
| *(end repeating frame)*                     |                          |                     |
