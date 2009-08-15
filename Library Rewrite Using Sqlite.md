# Library Rewrite Using SQLite

## Summary and Rationale

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

This project is already in progress\! Check it out on launchpad in the
lp:\~mixxxdevelopers/mixxx/features\_sqlite branch.

## Use Cases

  - DJ Bill wants DJ software that has a good library. He's tried Mixxx
    but its library does not scale to his large collection of music. It
    is also buggy, and often gets corrupted so he cannot build up
    quality metadata about his music.
  - Meganerd Roger occasionally mixes music and also has a large
    collection of Music, all tagged and rated in Exaile (or RhythmBox,
    etc...). He likes mixxxx, especially since it was how he was
    introduced to mixing, but the current library cannot get to his
    metadata so he relies on his player for when he plays music at
    parties.
  - DJ Minimal does not understand tags or any of that Interweb 2 point
    O' stuff, but has a well sorted out collection of tagged music. He
    knows what he needs to mix, but he really needs to be able to sort
    and search through his library to get at it quickly.
  - DJ DarkPsyPhil programs in C/C++/PHP and Python and also mixes Dark
    Psytrance. He needs access to as much metadata as he can shake a
    stick at. His collection of music is pretty big and at this moment
    varies between MP3, FLAC and WAV. Most, if not all his music is
    sorted into directories by year and in their respective albums. With
    all the music he has not all of it is tagged properly but he still
    needs a quick handle on it.

## Design

The current library in Mixxx 1.7.0 leaves a lot to be desired. The
design of the new library will aim to bring a significant amount of new
functionality for all types of DJs in order to broaden our user
demographics and to retain existing users.

Using a database naturally solves the following issues with the current
library:

  - Inability of the QList-based TrackCollection to scale well for large
    libraries (in terms of both CPU time for searching and memory usage)
  - Start-up and shut-down times increasing with larger libraries
  - Inability to perform advanced data manipulation like tagging
  - Inability to sanely deal with playlists :)

These were all problems that were at the core of the old library code,
and not only has using a database solved them, but it's opened up a
tremendous amount of other possibilities for us. We've also got more
flexibility in how we display data in the WTrackTableView widget, as we
can now use delegate classes to do cool stuff with very little coding.

More to follow after a discussion on mixxx-devel and a Skype meeting...

#### Database Schemas

**Library Table (as of August 15, 2009)**

``` sql
    CREATE TABLE library (
          id INTEGER primary key,
          artist varchar(48),
          title varchar(48),
          album varchar(48),
          year varchar(16),
          genre varchar(32),
          tracknumber varchar(3),
          filename varchar(512),
          location varchar(512),
          comment varchar(20),
          url varchar(256),
          duration integer,
          length_in_bytes integer,
          bitrate integer,
          samplerate integer,
          cuepoint integer,
          bpm float,
          wavesummaryhex blob,
          channels integer
    )
```

**Library Table (proposed)**

| Field          | Datatype | Comments    |
| -------------- | -------- | ----------- |
| id             | integer  | Primary key |
| name           | varchar  |             |
| date\_created  | date     |             |
| date\_modified | date     |             |

**Playlist Table (proposed)**

| Field       | Datatype | Comments                              |
| ----------- | -------- | ------------------------------------- |
| id          | integer  | Primary key                           |
| library\_id | integer  | Foreign key from playlists table      |
| track\_id   | integer  | Foreign key from library table        |
| position    | integer  | Position of the track in the playlist |

**Tags Table (proposed)**

| Field       | Datatype | Comments                       |
| ----------- | -------- | ------------------------------ |
| id          | integer  | Primary key                    |
| tag         | varchar  | Name of the tag                |
| library\_id | integer  | Foreign key from library table |

### Notes

  - Not all DataSources will support all our column types
  - We won't want to modify external sources

#### Classes

**TrackSource**

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

## Current Progress

The meat of the project is done. There's still a solid body of work
left, but much of it is polish and restoring old features.

From the Mixxx 1.8.0 developer meeting, what Albert has done is:

  - Deleted track.cpp, the source of much pain and misery in our
    codebase. In other words, I complete ripped out everything to do
    with the old library code. I also took a sledge hammer to
    TrackInfoObject, though much of it survived. TIO should be cleaned
    up an renamed to something sane (like a new Track class) now.
  - Written a new WTrackTableView widget from scratch.
  - Written a new TrackCollection class from scratch, which talks to
    SQLite through Qt. This class should be renamed TrackDatabase for
    clarity.
  - Written a new LibraryTableModel class which subclasses
    QSqlTableModel, which talks to our database. This let's us display
    our track library using model-view without writing very much code.
  - A bunch of other little things like having the columns resize
    persistently, making the columns rearrangeable, etc.

From the Mixxx 1.8.0 developer meeting, some of the remaining issues
are:

  - rewrite the track editor (right click-\>properties dialog)
  - searches still block the GUI, make them asynchronous by making
    introducing some threading into the data models somehow.
  - Library rescanning needs work - Wes Idel sent Albert half a patch to
    do this in a really nice way. Status of his project is currently
    unknown though. 
  - Playlist support
  - Browse mode
  - tagging
  - abstraction of track sources (e.g. to allow for ipod source)
  - browse mode
  - Cue/loop storage in the DB
  - bling-bling delegates
  - XML migration strategy (is this even worth it?)
  - bulk BPM detection and other library-wide things

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - **YOU**
  - Albert Santoni
  - RJ Ryan
  - Sean Pappalardo
  - Phillip Whelan
