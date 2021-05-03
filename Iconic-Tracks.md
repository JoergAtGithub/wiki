# Iconic Tracks

Collection of tracks, useful for discussing Mixxx features. They have been either used in community discussions, pushing one musical property to the max or are well known for a particular feature.

## ABBA - Dancing Queen

https://www.youtube.com/watch?v=xFrGuyw1V8s

This 1976 Disco track is a typical manually played 100 bpm track at that
time. It is interesting, because we Mixxx 2.3 beat detector can handle
it well. The non const beat mode cycles around 100 bpm makes it useless
for auto sync and the a const beat grid is heavily off at many places of
the track.

## Already Maged - Circle Dance Of Cold Constellations

https://sanatonrecords.bandcamp.com/track/already-maged-circle-dance-of-cold-constellations

This is a challenging track for the beat detector, because it is 10:46 long, but has many regions of different BPMs detected by the original QM beat detector. A perfect beat grid hat fully 151 BPM

## Atenna - Zorba The Greek

https://www.youtube.com/watch?v=nrCu94kpE1Q

This is a 1995 Club Mix of Sirtaki, taken from the 1965 movie with the
same name. It starts with gentle 105 bpm and speeds up to 180 bpm. It
has clear sections, some with constant bpm and some with increasing
tempo.

## Dave Brubeck - Take Five

https://www.youtube.com/watch?v=vmDDOFXSgAs

This 1959 Cool Jazz tracks, is the icon for a 5/4 tracks.

The Wikipedia contains a detailed description of the section and phrases
structure of the track. <https://en.wikipedia.org/wiki/Take_Five>

Key: E♭ minor Tempo: 174 bpm

## Green Day - Holiday

https://www.youtube.com/watch?v=A1OqtIqzScI

This 2004 Punk track is one of the loudest recorded tracks. A mp3
version of this track is clipping after decoding due to the additional
noise added by the compression algorithm. The calculated replay gain is
-12 dB where a typical values are around -6 dB.

## Kashmir - Led Zeppelin

https://www.youtube.com/watch?v=sfR_HWMzgyc

This 1975 Classic Rock track, is an icon for a polymetre track where two
metrics are played simultaneously. In this case, the drummer plays a 4/4
measure while the rest of the band is at 3/4.

## Michael Jackson - Man In The Mirror

https://www.youtube.com/watch?v=PivWY9wn5ps

This 1987 Electronic Pop track has on of the most famous key change. It
comes along with a "CHANGE" in the lyrics at \~2:45. The key changes
from G Major to A♭ Major.

## Procs - Frigolitpuffens Magiska Trampdyna 

https://sanatonrecords.bandcamp.com/track/procs-frigolitpuffens-magiska-trampdyna

This is a challenging track for the beat detector, because it is has 139.98 BPM instead, and must not be rounded to 140,00 BPM for an optimal beat grid. This track is a good example why too aggressive rounding is not always a good solution.

## Subjoi - Empty Nights

https://subjoi.bandcamp.com/track/empty-nights

Mixxx 2.3 beat detection fails to detect downbeat and places beatgrid on offbeats instead. BPM 126.0 correct. Key falsely detected as Bb while it is Gm (parallel minor). Track changes between chords Gm and Dm. Stacking both chords and using Bb as root that results in Bbmaj713. So maybe stronger emphasis on root tone could help identify correct key in this case.

## The Winstons - Amen Brother

https://www.youtube.com/watch?v=GxZuq57_bYM

This is the b-side of the chart single "Color Him Father" from 1969. It contains the most used sample (> 2000 times) of all: the "Amen Break". It consists of just 8 beats starting at 1:27.

After these breaks, a odd measure follows that shift the downbeat by a half beat. A normal 4/4 measure is played and that a odd measure shifts the downbeat back to the original position.

# External Sources

Key changes:

https://www.classicfm.com/discover-music/music-theory/best-key-changes-pop-song

Skipped or added beats:

https://www.youtube.com/watch?v=ec7wiBkHLC4