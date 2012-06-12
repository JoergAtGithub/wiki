# AutoDJ Feature Enhancement

  - Student: Scott Stewart
  - email: smstewart91@gmail.com
  - IRC: smstewart
  - Mentor: Daniel Schurmann

# Abstract

The main goal of this project is to make AutoDJ sound more like a real
DJ. The main feature that would allow this is beatmatching support in
AutoDJ. Currently, AutoDJ only crossfades between two songs over a
certain time interval, much like iTunes or other media players can do. I
plan to use the power that Mixxx already has, such as BPM sync and beat
detection, to improve the way that AutoDJ handles transitions.

# Proposed Changes

## Beatmatching

Beatmatching will be used to transition between songs. This will be
enabled/disabled by a checkbox that will be a part of the AutoDJ
controls. The "sync" abilities of Mixxx will be used, along with various
transition techniques, to handle transitioning between songs that have
different BPMs.

## Cue Points

Cue in/out points that are used by AutoDJ are a feature that was
mentioned by people in the Mixxx community, and had already been
started, so it has been added to this project. The cue in would be used
to mark the point where AutoDJ will start playing a track, while the cue
out will mark the point where the next transition will start. Decks
currently load tracks at the cue point, so this will be the cue in point
for AutoDJ. This will help DJs who already have cue points defined in
their library. The cue out point will be added to the cue database, and
a button will be added to the GUI, so that users can set the AutoDJ cue
out point.

## AutoDJ Class

To allow for all of these changes, the AutoDJ logic is going to be moved
for dlgautodj.cpp to its own AutoDJ class. This allows for more
organized expansion and fixes issues that are caused by the AutoDJ being
linked to the GUI.

## Fade Now

The Fade Now option of AutoDJ is going to be expanded to be usable all
of the time, not just when AutoDJ is enabled. This enables smooth
crossfades for users do not have an external mixer, or quick transitions
when needed.

## GUI Changes

The GUI changes are related to enabling the extra features that are
going to be implemented. A checkbox will be added to the AutoDJ controls
to decide if beatmatching is going to be enabled. Fade Now buttons will
be placed on either side of the crossfader. The user can press either
button to automatically fade the crossfader in the chosen direction. The
cue points will have buttons to set the in/out positions.

# Additional Features

These features have been discussed and could be added later

## Preview Deck Cue Points

Being able to set cue in/out points from the preview deck would allow
users to quickly manage their AutoDJ playlist by previewing a song,
adding in/out points, and then placing the song in their AutoDJ
playlist.

## Silence Detection

Silence at the beginning or end of a track would be detected and
automatically not included in the song. AutoDJ would start the song
after the silence (if it is at the beginning of the track) or transition
before the silence (when the silence is at the end of the track). This
would be beneficial when the user does not have any cue points set, so
the entire track is played.
