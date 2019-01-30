# Student Project Ideas for Google Summer of Code 2019

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of
Code 2019](https://summerofcode.withgoogle.com/). Each of these projects
represents something that we think would make a really big difference to
our users and that we as a development team are really excited about. If
you are interested in applying to GSoC, read [GSoC Advice](gsocadvice)
before applying or getting involved.

A GSoC application that simply repeats the project description will
*NOT* be accepted. We expect you to think about the feature and how it
aligns with Mixxx's goals, describe potential use cases and propose a
plan for implementing a solution. Only students that are active members
of the Mixxx community are accepted. If this is not the case yet, just
say hello at <https://mixxx.zulipchat.com> and discuss your Ideas and
use cases with us.

# Measures, Downbeats, Bars and Phrases

Mixxx uses information about the tempo and location of beats for many
features including sync, looping, and quantize cue points.

For a smooth transition between tracks it is also required to sync the
bars, the first beat in a measure. Currently the DJ counts the beats 1 2
3 4 and places the CUE at such a beat 1 (downbeat) of the incoming track
by listening to the track in headphones. Now he can count the playing
track and hit play at beat 1. Mixxx can help and adjust this exactly to
the desired beat, but unfortunately not more. See: [video
tutorial](https://www.youtube.com/watch?v=Jy2s8C8mAiw)

Most tracks have a 4/4 measure but Mixxx should also allow less common
measures like 3/4 or 7/8. This would be major benefit compared to other
DJ software that assumes that all music has a 4/4 measure, which is
incorrect for lots of music. Currently Mixxx is not aware of bars and
measures. It would be part of the project to place bars on the auto
detected beat grids by a new editor and visualize them on the waveform.

Some preliminary work for drawing this information on the waveforms has
been [started](https://github.com/mixxxdj/mixxx/pull/1918). However, for
this to be really useful Mixxx needs a way to store the new time
signature and downbeat information in the database and an intuitive user
interface for users to edit this information.

The project might be extended towards a sync feature using this new info
or into a feature that auto detect bars and phases.

A strong application will list some specific tracks with different time
signatures that will be used for testing the new features. Students with
backgrounds in music theory and/or playing percussion instruments are
encouraged to apply for this project, but these are not requirements and
we welcome your application if you do not have that experience.

# Changing Tempo Tracks

Currently, Mixxx assumes either that tracks have a constant tempo for
their entire duration or always changing tempo. The first option works
nice for most electronic tracks, because it creates a reliable beat
grid, even if some beats are not detected. It fails for hand made track
where a drummer has no crystal clock in his head. In this case the
second approach works better. But if you try to sync an other track to
the hand made track it is yowling because it tries to exactly follow the
drummer.

In this project you should find an approach that is able to iron out a
small beat jitter of hand made tracks, but follow major tempo changes.
It should be also be aware of breaks and britches and other difficult to
detect elements.

One way to approach this would be to mark sections with changing tempos
by special markers. For example, this [video
tutorial](https://www.youtube.com/watch?v=oD9J7azlhrQ) demonstrates how
Serato DJ handles this.

The analyzer that Mixxx uses provides the exact locations of each beat.
This might be used to automatically guess whether to treat a part of a
track as a constant tempo or changing tempo.

A strong application will list some specific tracks with changing tempos
that will be used for testing the new features. These should include
both tracks played by live musicians and tracks produced on a grid in a
computer. Also, the application should propose how the new information
available in the beat grid could be edited by users in a fast, intuitive
way. Students with backgrounds in music theory and/or playing percussion
instruments are encouraged to apply for this project, but these are not
requirements and we welcome your application if you do not have that
experience.

# MusicBrainz Integration

Mixxx uses [AcoustID](https://acoustid.org/) to identify tracks by
fingerprinting their audio data. Subsequently the results are used to
query the [MusicBrainz](https://musicbrainz.org/) database for metdata
about the identified track. Currently we don't utilize the full
potential that the MusicBrainz database is providing. We are reading
just a few track properties to complement missing metadata.

#### MusicBrainz IDs

All entities in the MusicBrainz database are identified by
[UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier).
These UUIDs could be used for various purposes:

  - Detecting exact duplicates or variants of a track independent of the
    actual audio encoding. Use Case: When migrating your files from
    lower quality MP3 to higher quality FLAC encoding, obsolete MP3
    files could be identified based on their IDs and proposed for
    removal.
  - Relocating a track after it has been moved. Identifying tracks by
    their IDs will be much more reliable than by a combination of some
    properties. Use Case: You reorganize your files using a tool like
    [Beets](http://beets.io/) and don't want to lose all your carefully
    crafted crate/playlist/history contents when Mixxx is not able to
    asscociate your tracks in the library with the new file locations.

We recently implemented the import/export of MusicBrainz IDs according
to the [Picard Tag
Mapping](https://picard.musicbrainz.org/docs/mappings/) proposal. The
next step is extending the MusicBrainz client for retrieving and the
Mixxx database and storing those IDs. Afterwards your proposed features
can be added based on these IDs.

#### Custom Tags

One essential feature that Mixxx is missing is the ability to assign and
manage custom tags to tracks. We have already collected some ideas what
and how to store this information in [Launchpad
\#1743702](https://bugs.launchpad.net/mixxx/+bug/1743702). MusicBrainz
records user-provided tags and ratings in their libary which could be
used as a starting point and for synchronization. In the Mixxx database
simple textual tags could be stored in an inverse index Tag String -\>
Track ID. It should also be possible to attach the custom tags of a
track to the file by exporting/importing them as file tags.

# Aux Tracks

Currently Mixxx is able to play tracks from any other source like CD or
Record Players, or other desktop Applications. Unfortunately the only
visualization is a VU-Meter.

In this project, there should be some more features of the normal Decks
become available for the Aux input as well. These are first of all BPM
and Beat detection, waveform analysis loops and more.

This project may also streamline the setup to use the system sound as
Aux input. This is currently tricky depending on the used OS and sound
API.

# Transition Effects

Currently effects are basically applied to one channel only. If you like
to use them for transitions, you have to controls more than one knob at
a time. It would be nice to make effect transitions as easy as cross
fading.

During this project you need to define and implement an extensible way
to control transition effects with a single knob.

A simple example is a "EQ transition" The EQ knobs are used to avoid to
much bass during long cross fades. Currently the DJ has to turn various
EQ knobs play/pause and the cross fader simultaneously.

Once this project is implemented the DJ should only select "EQ
transition" and move the cross fader.

# Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. We recommend
spending more than a few days using Mixxx and participating in the
community to develop a better understanding nof areas where Mixxx could
use improvement. Our bug tracker is full of wishlist bugs and other
ideas scattered throughout, so if you browse through it, you may find
many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
