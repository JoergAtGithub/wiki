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

# Advanced Track Metadata

# Beatgrid enhancements

Mixxx currently assumes that tracks have a constant tempo for their
entire duration. There is an option to disable that assumption, but it
goes to the other extreme and treats the tempo as always changing. Both
of these do not work well for lots of music. Improve handling of tracks
with varying tempos like Serato
<https://www.youtube.com/watch?v=oD9J7azlhrQ>

Mixxx does not distinguish Beats from Downbeats. It has no indicator for
the track measure. This project should change this.

# Metadata Output

Mixxx has currently no interface to pass over metadata like the playing
track and artist to third party applications. This is required to
publish the current track via RDS or to a web service like Twitter or
just to the OS info area. This can be don by writing a file, rss feeds,
OSC or .... (Add your own ideas ..)

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

# Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**