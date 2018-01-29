# Student Project Ideas for Google Summer of Code 2018

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of
Code 2018](https://summerofcode.withgoogle.com/). Each of these projects
represents something that we think would make a really big difference to
our users and that we as a development team are really excited about.
For advice on how to get in touch and how to apply, you should read
[GSoC Advice](gsocadvice).

**A GSoC application that simply repeats the project description will
NOT be accepted. We expect you to think about the feature and how it
aligns with Mixxx's goals, outline potential use-cases and propose a
plan for implementing a solution.**

**Also, an application from a student who we are not familiar with will
NOT be accepted. You must have some interaction with the Mixxx community
before the days leading up to the application deadline for your
application to be accepted.**

# Beatgrid enhancements

Mixxx uses information about the tempo and location of beats for many
features including sync, looping, and quantizing cue points. Currently,
Mixxx assumes that tracks have a constant tempo for their entire
duration. There is an option to disable that assumption, but it goes to
the other extreme and treats the tempo as always changing. Both of these
do not work well for lots of music. There should be an intermediate
solution that allows for marking sections of a constant tempo and
sections where the tempo is changing.

Sections with changing tempos could be marked by indicating which beats
are downbeats and how many beats are in each measure. Then Mixxx could
place the beat markers by dividing the space between the downbeats by
the beats per measure. This would allow the tempo to change between
downbeats (gradually or suddenly). For example, this [video
tutorial](https://www.youtube.com/watch?v=oD9J7azlhrQ) demonstrates how
Serato DJ handles this. However, Serato and other DJ software assumes
that all music has a 4/4 time signature, which is incorrect for lots of
music. A proposal for this project should allow for handling tracks that
change time signatures.

Adding this information to the beatgrid would allow existing features
that rely on the beatgrid to work better for a wider variety of music.
Additionally, new features that rely on knowing the location of
downbeats and beats per measure could be implemented. You are encouraged
to propose some possibilities for new features relying on this new
beatgrid information in your application.

Ideas for algorithms to detect downbeats and beats per measure
automatically are welcome if you already have a strong background in
signal processing, but this should come last after completing the rest
of the project. If you do not have this experience, we welcome
applications that would assume 4/4 by default and allow users to adjust
this manually.

A strong application will list some specific tracks with changing tempos
that will be used for testing the new features. These should include
both tracks played by live musicians and tracks produced on a grid in a
computer. Also, the application should propose how the new information
available in the beat grid could be edited by users in a fast, intuitive
way. Students with backgrounds in music theory and/or playing percussion
instruments are encouraged to apply for this project, but these are not
requirements and we welcome your application if you do not have that
experience.

# Ableton Link Support

[Ableton Link](https://www.ableton.com/en/link/) is a relatively new
protocol for synchronizing music software running on multiple computers.
It has already been adopted fairly widely by proprietary music programs
including DJ programs, DAWs, software synthesizers, and sequencers.
Ableton has published [documentation](https://ableton.github.io/link/)
and [a reference C++ library](https://github.com/Ableton/link) that
could be used to synchronize Mixxx's [Master Sync
feature](https://mixxx.org/manual/latest/chapters/djing_with_mixxx.html#master-sync)
with Ableton Link compatible applications, including Mixxx running on
another computer.

# Metadata Output

Mixxx has currently no interface to pass over metadata like the playing
track and artist to third party applications. This is required to
publish the current broadcasted track via RDS or to a web service like
the upcoming <https://listenbrainz.org>, Twitter or just to the OS info
area. This can be done by writing a file, rss feeds, OSC or .... (Add
your own ideas ..) Ideally, this should be done in a cross-platform and
extensible way.

Since we will probably have the demand to interface a great variety of
services, you should consider how to implement this in a extensible way.
In the project you may focus to interface one service, in a way that it
can be easily extended for other services.

# MusicBrainz Integration

Mixxx uses [AcoustID](https://acoustid.org/) to identidy tracks by
fingerprinting their audio data. Subsequently the results are used to
query the [MusicBrainz](https://musicbrainz.org/) database for metdata
about the identified track. Currently we don't utilize the full
potential that the MusicBrainz database is providing. We are reading
just a few track properties to complement missing metadata.

MusicBrainz IDs All entities in the MusicBrainz database are identified
by UUIDs. These UUIDs could be used for various purposes: \* Detecting
exact duplicates or variants of a track independent of the actual audio
encoding. Use Case: When migrating your files from lower quality MP3 to
higher quality FLAC encoding, obsolete MP3 files could be identified
based on their IDs and proposed for removal. \* Relocating a track after
it has been moved. Identifying tracks by their IDs will be much more
reliable than by a combination of some properties. Use Case: You
reorganize your files using a tool like [Beets](http://beets.io/) and
don't want to lose all your carefully crafted crate/playlist/history
contents when Mixxx is not able to asscociate your tracks in the library
with the new file locations.

We recently implemented the import/export of MusicBrainz IDs according
to the [Picard Tag
Mapping](https://picard.musicbrainz.org/docs/mappings/) proposal. The
next step is extending the MusicBrainz client for retrieving and the
Mixxx database and storing those IDs. Afterwards your proposed features
can be added based on these IDs.

# Cue point enhancements

Currently, Mixxx's hotcues are limited. They cannot store any
information other than a position in a track. It would be helpful to
expand the capabilities of this in a number of ways. For example,
letting users label hotcues with custom text and set their own color
coding for hotcues. Setting specially marked mix in and mix out markers
would be helpful both for live performance and for telling AutoDJ when
to start automatic crossfading. Storing multiple loops per track that
could be activated with a hotcue would be helpful too.

A collection of ideas for improving cue points can be found in the
[Launchpad
blueprint](https://blueprints.launchpad.net/mixxx/+spec/cuepoints-2.0-new).

A strong application will include mockups for how these new features
could be accessed by users in an intuitive user interface that does not
clutter the screen with an excess of information.

# Wireless Remote

There is a demand for wireless remote controling Mixxx.

There is already a great variety of remote control apps available in
your Mobile Phone App Store. Just search for "DAW Remote".

Unfortunately non of them works out of the Box.

In this project you need to find out how the majority interfaces to
their target DAW systems. Then implement the most common interface in
Mixxx, and add first class support for one of these remote apps, ideal
with a FOSS license.

# Cartwall Player

In a broadcasting show, it is required to have a set of jingles and
background sounds under a finger tip. Currently you can use Mixxx's
sampler decks for this.

Unfortunately there are some shortcomings compared to specialised
dedicated cartwall player.

In this project you need to compare various existing solutions and
propose how to implement the most important features with Mixxx.

A highly requested feature is to automate these carts in a way. What are
the requirements for automation? How can this be implemented along this
projects,

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
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
