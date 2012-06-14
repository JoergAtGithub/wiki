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

# Specifications

## Transitions

Multiple transition styles will be added to AutoDJ. These different
styles will be selectable through a combobox that is part of the AutoDJ
controls. Users can select which specific transition they would like to
use, or they will have the option to let AutoDJ decide which transition
is used based on the two songs that are playing. If AutoDJ is deciding
which transition to use, it will make this decision based on the BPMs of
the two songs and the transition time that the user has set. For
instance, AutoDJ will use a smooth crossfade for two songs with similar
BPMs and a long transition time. For a short transition time and
different BPMs, AutoDJ might use a spinback transition. A
TrackTransition class will be used that contains a method for each type
of transition. AutoDJ will create an instance of the TrackTransition,
and will pass it ControlObjects for all of the buttons it needs, such as
the play button and the crossfader. AutoDJ can then call a specific
method of the TrackTransition object to use a specific transition. With
this class, more transitions can be added later, and they are separate
from the AutoDJ logic that decides which transition to use.

Some of the transition styles include:

  - Crossfade - This is what AutoDJ does now
  - Beatmatching crossfade - A long smooth crossfade that matches the
    two songs' BPMs
  - Cut - Cut Song A at the cue out and immediately start Song B 
  - Spinback - A short transition utilizing a spinback effect
  - Brake - Another short transition using a brake effect
  - Echo FadeOut - Echo one beat of Song A while decreasing the volume,
    then start Song B

More transitions can be added simply by creating a method for them in
the TrackTransition class. There are many types of transitions, such as
those using the EQ controls, that will not be added now, but could be
added at a later time.

## Cue Points

Cue in/out points that are used by AutoDJ are a feature that was
mentioned by people in the Mixxx community, and had already been
started, so it has been added to this project. It will be implemented
differently than the version that was already started, however, which
include fade in/out as well as cue in/out. The fade in/out option is
being removed. The transition time option that already exists adds the
same functionality that the fade in/out offered. The cue in would be
used to mark the point where AutoDJ will start playing a track, while
the cue out will mark the point where the next transition will start.
Decks currently load tracks at the cue point, so this will be the cue in
point for AutoDJ. This will help DJs who already have cue points defined
in their library. The cue out point will be added to the cue database,
and a button will be added to the GUI, so that users can set the AutoDJ
cue out point.

## AutoDJ Class

To allow for all of these changes, the AutoDJ logic is going to be moved
for dlgautodj.cpp to its own AutoDJ class. This allows for more
organized expansion and fixes issues that are caused by the AutoDJ being
linked to the GUI. The AutoDJ class will also be merged with the
EngineXFader class, creating a Fader class that can be controlled
through Control Objects. This also allows the AutoDJ access to the fader
without repeatedly polling the EngineXFader class.

## Crossfader

Users will be able to take control of the crossfader while AutoDJ is
transitioning if they choose to. If AutoDJ detects that the user is
moving the crossfader, it will give up control to the user. AutoDJ will
take back control for the next transition, or the user can use the Fade
Now option to transition at a later point in the song.

The Fade Now option of AutoDJ is going to be expanded to be usable all
of the time, not just when AutoDJ is enabled. This enables smooth
crossfades for users do not have an external mixer, or quick transitions
when needed.

## GUI Changes

The GUI changes are related to enabling the extra features that are
going to be implemented. A checkbox will be added to the AutoDJ controls
to decide if beatmatching is going to be enabled.

Fade Now buttons will be placed on either side of the crossfader. The
user can press either button to automatically fade the crossfader in the
chosen direction. These buttons will also act as AutoDJ indicators and
will light up when AutoDJ is in use.

A button will be added to set the AutoDJ cue out point.

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

# TO DO

  - Complete project specifications: INPROGRESS
  - Create AutoDJ class: INPROGRESS
  - Implement AutoDJ cue points
  - Transitions
  - Using cue points
  - Using beatmatching

# Discussion

Ideas that have been discussed but were decided against

### AutoDJ Cue In

An AutoDJ cue in button was discussed. This button would provide a cue
point for AutoDJ to start playing a song at that was different from the
default cue or the hot cues.

  - Pro: Would eliminate all ambiguity as to where AutoDJ would start a
    track
  - Con: Most DJs already have cues set, so adding an AutoDJ cue would
    largely be unnecessary

Use Hotcue 1 as the AutoDJ cue in

  - Pro: Many DJs use Hotcue 1 as the first entrance into the song
  - Con: Using hotcue 1 may seem unintuitive
  - Con: If DJs want to use a different place to enter into the song,
    they will have to change their hot cue that is already set

### Fade Now Control

The Fade Now controls could be placed as part of each deck's controls.
This control would be similar to the loop button, but instead of the
loop controls, would contain cue in, cue out, and Fade Now.

  - Pro: Would fit all controls in a small space
  - Con: Fade Now does not make sense as a deck control because it
    controls the Master crossfader. Also, this would not make sense in a
    layout with more than two decks.
  - Con: Cue in button is no longer needed, so the layout is not
    necessary
