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

There is a demand to wireless remote control Mixxx.

There is already a great variety of remote control apps available in
your Mobile Phone App Store. Just search for "DAW Remote".

Unfortunately non of them works out of the Box.

In this project you need to find out how the majority interfaces to
their target DAW systems. Then implement the most common interface in
Mixxx, and add first class support for one of these remote, ideal with a
FOSS license.

# Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
