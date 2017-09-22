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

| Column | Type    | Meaning                   |
| ------ | ------- | ------------------------- |
| id     | INTEGER | Surrogate primary key     |
| title  | TEXT    | Short title for the crate |
| path   | TEXT    | **??**                    |

### `CrateHierarchy`

Each row represents an optional relationship between a parent and child
crate.

| Column       | Type    | Meaning                                 |
| ------------ | ------- | --------------------------------------- |
| crateId      | INTEGER | Parent crate, foreign key to `Crate.id` |
| crateIdChild | INTEGER | Child crate, foreign key to `Crate.id`  |

### `CrateParentList`

Each row represents **???**

| Column        | Type    | Meaning                            |
| ------------- | ------- | ---------------------------------- |
| crateOriginId | INTEGER | **???**, foreign key to `Crate.id` |
| crateParentId | INTEGER | **???**, foreign key to `Crate.id` |

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

| Column                 | Type    | Meaning                                                                                                                                                                                                                                                                     |
| ---------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                     | INTEGER | Surrogate primary key                                                                                                                                                                                                                                                       |
| uuid                   | TEXT    | Unique identifier for this Engine Library, in order to distinguish from other Engine Prime libraries on other media.                                                                                                                                                        |
| schemaVersionMajor     | INTEGER | Major part of the three-part version number for the Engine Prime library schema.                                                                                                                                                                                            |
| schemaVersionMinor     | INTEGER | Minor part of the three-part version number for the Engine Prime library schema.                                                                                                                                                                                            |
| schemaVersionPatch     | INTEGER | Patch part of the three-part version number for the Engine Prime library schema.                                                                                                                                                                                            |
| currentPlayedIndicator | INTEGER | A hash of some kind, in the form of an 18 or 19-digit number, which can be used to find all tracks that have been played in the most recent 'playthrough' of tracks from the current database. The number will appear in the `MetaDataInteger` table for values of type 10. |

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

1.  \*Unused - no entries should be made in `Metadata` for this value of
    `type`\*
2.  **TBC** - seems to always be set to 1
3.  **TBC** - seems to always be set to 1

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
  - 24 =\> 8B / C major (**TBC** confirm this is 24, as opposed to 0)

<!-- end list -->

1.  **TBC** - unsure, seems to be set to zero for all sample tracks
2.  **TBC** - unsure, not populated for any sample tracks
3.  **TBC** - unsure, not populated for any sample tracks
4.  **TBC** - unsure, not populated for any sample tracks
5.  **TBC** - unsure, not populated for any sample tracks
6.  A 18 or 19-digit number acting as a hash that indicates which tracks
    have been played in the most recent 'playthrough' of songs from this
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
| path                      | TEXT    | Path to the audio file on disk, \*relative to the Engine Library directory\*                                                                   |
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
| currentPlayedIndicator | INTEGER | **TBC** - appears to be set to 0 for the `p.db` database                                                             |

### `PerformanceData`

Each row represents information about a track that has been determined
by track analysis and preparation, such as the location of hot cues,
loops, the beat grid, as well as waveform data.

| Column                     | Type    | Meaning                                                                              |
| -------------------------- | ------- | ------------------------------------------------------------------------------------ |
| id                         | INTEGER | Track identifier; soft foreign key to `Track.id` in `m.db`                           |
| isAnalyzed                 | NUMERIC | 1 if the track has been analysed, 0 if not                                           |
| isRendered                 | NUMERIC | **TBC** - seems to always be set to 0                                                |
| trackData                  | BLOB    |                                                                                      |
| highResolutionWaveFormData | BLOB    |                                                                                      |
| overviewWaveFormData       | BLOB    |                                                                                      |
| beatData                   | BLOB    |                                                                                      |
| quickCues                  | BLOB    |                                                                                      |
| loops                      | BLOB    |                                                                                      |
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
