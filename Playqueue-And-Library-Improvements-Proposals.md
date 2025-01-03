This page describe the changes I would like to add into the mixxx 1.6.x
trunk in order to improve Play Queue and Library views

# 1\) Play Queue Improvements

## Current Problems:

1.   the DJ can easily add several tracks on the play queue, but if he
    goes to this view, the tracks will not be displayed by play order,
    but by track name order for instance.

## Solutions:

1.  display the order the track will be played (1, 2, 3, ...)
2.  make the items in the Play Queue view reorderable

# 2\) Easilly listen music in the headset:

## The Problem:

1.  the user has to perform several confusing steps in order to listen
    one track in his headset : 

<!-- end list -->

  - stop current listing track in the headset table
  - double click on a track which load it in the headset table
  - then press "play" on this table.

## Solution:

1.  double click on a track when in the configuration "one Player output
    on the master soundcard + one Player on the headset" instanteously
    stops the track played in the headset, load it in this player and
    start playback.

## Note:

this is not a modification of the NEXT mode system, it is just a way to
quickly loads a track in the headset Player in order to play without too
much steps.

# 3\) Library view Improvements

## Current Problems:

1.  the DJ cannot know easilly when browsing the Library view if a given
    song has already be played during his mix.
2.  the user cannot easy know the Genre or the rating of a given song

## Solutions

1.  Display a little tag (or a leading asterisk, or change the text
    color) on any already played track in Playlist, Browse(?) and
    Library views (to prevent choosing several time the same track
    during one session). This may be based on the "TimesPlayed" value of
    the trackinfoobject or a similar one, like "TimesPlayedInThisMix". A
    button or a "reset played track" menu item may be required to be
    added in the interface in order to reset all these
    TimesPlayedInThisMix value to 0.
2.  **\[DONE\]** Display a column in Library, Playqueue and Playlists
    with the Genre ID3 tag. On click on this column, tracks will be
    sorted by Genre, then by artist then by title.
3.  Display a column with rating of the song in the Library, Playqueue
    and Playlists view (read only for the first step, then read/write)
4.  Implements a Facet-like view for the "Library" (three column
    Genre/Artist/Album like in rythmbox)

## Known issue:

1.  Mixxx doesn't have ID3/ogg writing support. So rating of track must
    be performed by another software. I propose using Amarok rating
    system (a change in Amarok source/plugins would be required in order
    to write this rating value in the mp3/ogg file itself, instead of
    just using the Amarok database).

# 3\) Minor bugs to fix

1.  the Library view is not well sorted by default on startup, tracks
    are in the order read from .mixxxtracks.xml
2.  user cannot type keyboard shortcut when the focus is on one item in
    the paylist view. Event doesn't seem to be propagated to parent
    window
