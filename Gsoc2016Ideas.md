# Student Project Ideas for Google Summer of Code 2016

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of
Code 2016](https://developers.google.com/open-source/gsoc/). Each of
these projects represents something that we think would make a really
big difference to our users and that we as a development team are really
excited about. For advice on how to get in touch and how to apply, you
should read [GSoC Advice](gsocadvice).

**A GSoC application that simply repeats the project description will
NOT be accepted. We expect you to think about the feature and how it
aligns with Mixxx's goals, outline potential use-cases and propose a
plan for implementing a solution.**

## Track Meta Data Editor

Mixxx able to display various track meta data like cover, year and
genre. Once all these data are available and correct, it is a fun to
seek through the library to find a follower track.

Update all track metadata to a consistent state is currently a pain,
especially if the track are from different sources. This becomes worse
if the tracks have already meta data but wrong, like tracks from an
oldies sampler, dated to the release year of the sampler and not the
single release year.

Mixxx is already able to fetch meta data from MusicBrainz, but some meta
data data is still missing or of weak quality. Other music players or
tagging tools does a much better job here. They are able to display meta
data form different online source like last.fm, Discogs or similar. The
user can compare them and pick the suitable info. Some tools are also
able to identify issues like misspelled names or duplicates.

Your proposal should include a clear description of the shortcomings of
today's meta data edit features and how you plan to improve it. If
appropriate, please include mockups and diagrams illustrating your
plans.

## Track analysis view and editor

Mixxx already includes some analyses features, but is not able to
utilize all of the collected information. The current analysis view is
not very intuitive.

Beat and bars: Mixxx should be able to detect, visualize and edit beat
and bar information.

Key: Mixxx should be able to detect, visualize and edit changing keys
throughout the track.

Cue points: Mixxx should be able to detect, visualize and edit special
cue points. Like the first beat, Auto DJ fade start / end.

Your proposal should only focus on a set of features described above.
Please describe the issue you focus on. Define how the data will be
collected and used inside Mixxx. Include GUI markup of a new analysis
data editor.

## RTMP or WebRTC support

Mixxx already has Shoutcast support for streaming. But for wider
adoption it should at least have HTML5
[WebRTC](https://en.wikipedia.org/wiki/WebRTC) or more widely adopted
[RTMP-protocol](https://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol)
suppport. To achieve this Mixxx recording and streaming API should be
reshaped to plugin-style API.

## Keyboard Mapping GUI

Editing keyboard shortcuts is currently a pain point for users and
requires editing a text file.

This project will move keyboard mapping and processing into the new
controller sub-system as a new type of controller (alongside MIDI and
HID controller support) and introduce a user-friendly GUI for editing
keyboard presets. For backwards compatibility, the keyboard presets
should still be stored on-disk in the same text format.

We suggest you check out the MIDI mapping GUI and code in Mixxx 2.0 for
inspiration. Another very useful exercise is checking out the various
commercial DJ software offerings out there and examining how they allow
users to map MIDI controllers.

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
