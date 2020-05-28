# Elastic Beatgrids

This page groups info relevant to tracks with multiple BPMs.

## MIXXX support

\* Mapping commands: [mixxxcontrols?\#master](mixxxcontrols?#master) \*
Manual (Preferences):
<https://www.mixxx.org/manual/latest/en/chapters/preferences.html?highlight=analyse#beat-detection>
\* Forum post: <https://www.mixxx.org/forums/viewtopic.php?f=3&t=11629>
\* GSOC project 2020:
[measures\_downbeats\_bars\_and\_phrases](measures_downbeats_bars_and_phrases)
\* GSOC project 2018:
[gsoc2018ideas?\#beatgrid\_enhancements](gsoc2018ideas?#beatgrid_enhancements)
\* Zulip Chat:
<https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Rhythm.20Detector>
\* Serato Comparison:
[here](https://www.reddit.com/r/DJs/comments/gs49z6/serato_or_rekordbox_now_that_rekordbox_needs_a/fs313ck/)

## Definitions

### Tracks with multiple BPMs

There are two types of tracks that have multiple BPMs: \* **a) Unsteady
BPMs:**

  - Definition: these tracks floats around a single BPM (+-1% range).
    Examples:
  - Live drummers: [Guns N' Roses - Sweet Child O'
    Mine](https://www.youtube.com/watch?v=1w7OgIMMRc4)
  - Old disco / 80s Pop tracks: [Matia Bazar - Ti
    Sento](https://www.youtube.com/watch?v=uk7bR54G2BA)

\* **b) Transition Tracks:**

  - Definition: these tracks have clear BPM changes (+-10% range).
    Examples:
  - Abrupt 85-\>115 bpm: [Magic Drum Orchestra - Drop it like its
    Hot](https://youtu.be/W-nrHptw4Ow)
  - Smooth 126-\>98 bpm: [Planet Soul - Set me
    Free](https://www.youtube.com/watch?v=v5HEfbxk7Mw)

more lists:
[list1](https://www.reddit.com/r/DJs/comments/2hmtgc/do_you_know_of_any_house_songs_that_increase_in/)
[list2](https://www.reddit.com/r/DJs/comments/ybt30/transition_tracks/)

### Elastic Beatgrid use cases

"Elastic beatgrids" is a feature that explicitly allows **multiple
BPMs** in each track.

Without elastic beatgrids, the following becomes impossible to perform
without the audience noticing: \* **Beatjumps:**

  - Impossible to fix in advance because the jump happens
    instantaneously

\* **FX BPM-synced effects:** (eg delay)

  - Impossible to fix in any situation, because FX fully depend on the
    beatgrid

\* **AutoLoops:**

  - IN point: with quantize off, you have to enable the loop at
    precisely the right time
  - OUT point: In this case you have to immediately enter "loop out
    adjust mode" to fix the out point as fast as you can 

\* **Sync beatmatch:**

  - In this case you HAVE to compensate continuously using the jogwheels
    on the whole transition (manual beatmatch)
