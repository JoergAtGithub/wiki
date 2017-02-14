# Student Project Ideas for Google Summer of Code 2017

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of
Code 2017](https://developers.google.com/open-source/gsoc/). Each of
these projects represents something that we think would make a really
big difference to our users and that we as a development team are really
excited about. For advice on how to get in touch and how to apply, you
should read [GSoC Advice](gsocadvice).

**A GSoC application that simply repeats the project description will
NOT be accepted. We expect you to think about the feature and how it
aligns with Mixxx's goals, outline potential use-cases and propose a
plan for implementing a solution.**

# Live Broadcasting Improvements

Live broadcasting is a very important use case for many users of Mixxx.
This allows DJs to stream their performances online via Internet radio
stations and other venues (e.g. SecondLife).

## Multiple Broadcasting Profiles

Live broadcasters use Mixxx to stream to their listeners via an Icecast
or Shoutcast server. Mixxx currently supports a single "profile" of
settings. For broadcasters that frequently stream to multiple services
(e.g. if they are a DJ on multiple internet radio stations) they have to
re-enter their login and stream configuration details every time they
switch stations. This project entails adding support for multiple live
broadcasting profiles or presets.

## Multiple Connections at Once

Live broadcasters have requested the ability to stream to multiple
stations at once.

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
blueprint](https://blueprints.launchpad.net/mixxx/+spec/cuepoints-2.0).

# Crate improvements

Mixxx's crates allow DJs to create their own organization system for
their music library. It could become an even more powerful tool by
[letting crates be organized in a
hierarchy](https://bugs.launchpad.net/mixxx/+bug/671632) and [adding a
search filter for
crates](https://bugs.launchpad.net/mixxx/+bug/1402133). These
improvements would turn crates into a system that would allow DJs to
arbitrarily tag and search their library in complex ways that uniquely
fit their workflow.

# Effects

## Microphone effects

Mixxx could use some effects specifically for applying to microphone
inputs, for example a gate and acoustic echo cancellation. Consider
looking for third party libraries like the [WebRTC AEC
library](http://webrtc.org/) that can help with these and using them in
Mixxx. If you choose to implement this, you will need a microphone to
test with. You do not need an expensive microphone; any microphone
should work.

## Beat synchronized effects

Synchronizing temporal effects with the rhythm of their input signals is
important for making them sound musical. Currently, only the autopan
effect is capable of this. It would be really helpful to add this
functionality to the echo and reverb effects. Also, a beatmasher effect
would be fun. Refer to the [Launchpad
ticket](https://bugs.launchpad.net/mixxx/+bug/1518185) for previous
discussion about this.

# Sample sets

Currently, samples have to be loaded to sample decks one-by-one each
time Mixxx is restarted to load the samples. It would be helpful to save
collections of samples to Mixxx's database so they could all be loaded
together. It would also be helpful to let users separate audio files
used as short samples from full tracks in the library.

# Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
