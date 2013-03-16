# Student Project Ideas for Google Summer of Code 2013

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of
Code 2013](http://www.google-melange.com/gsoc/homepage/google/gsoc2013/).
Each of these projects represents something that we think would make a
really big difference to our users and that we as a development team are
really excited about. For advice on how to get in touch and how to
apply, you should read [GSoC Advice](gsocadvice).

**A GSoC application that simply repeats the project description will
NOT be accepted. We expect you to think about the feature and how it
aligns with Mixxx's goals, outline potential use-cases and propose a
plan for implementing a solution.**

## Mixxx Remote

There are many different options to achieve remote control of Mixxx for
different use cases.

It is up to you to propose a remote scenario that will be the scope of
your GSoC Project.

Hiere are some links:

  - \[<https://bugs.launchpad.net/mixxx/+bug/1108370>\]
  - \[<http://mixxx.org/forums/viewtopic.php?f=6&t=1477>\]
  - \[<https://play.google.com/store/apps/details?id=com.bti.djControl&hl=de>\]

## Cover Arts

It would be nice if Mixxx could display cover arts.

This project has two aspects:

  - Intigrate the cover views in a polished way into the Mixxx GUI 
  - tap the different cover sources 

## Library GUI Layout Redesign

The current library GUI needs to be polished and needs to give room for
new features.

Further links can be found here:

<https://blueprints.launchpad.net/mixxx/+spec/three-column-library-layout>

## Advanced Tagging

Currently Mixxx does not write metatdata back to the tracks. The tagging
capability of mixxx is low compared to current media players. It is a
good idea to catch up.

## Non-Blocking Database Access

Currently some database transactions are stalilng the GUI. This is
because som database actions are preformed from the GUI thread. This
project would make Mixxx more relyable by defining and implementing a
new concept how to deal with database actions.

## D-Bus Interface

This Project aims to integrate Mixxx into the Linux desktop. Mixxx
should be able to communicate with other Mediaplayers for exchanging
playlists and it should be able to control Mixxx by the audio controls
of the desktop environment.

\[<http://specifications.freedesktop.org/mpris-spec/latest/>\]

## Include Streaming services or webapps like Soundcloud/Last.fm/...

There are a lot of good online sites available to organize your library
or get new music, like soundcloud, last.fm and musicbrainz. Support for
tags correction with musicbrainz was implemented in last years GSOC and
will be integrated in 1.12. You can pick one service that you like and
implement it in GSOC 2013

Further Information can be found here:

  - \[<https://code.launchpad.net/~max-linke/mixxx/library_features>\]
  - \[<https://bugs.launchpad.net/mixxx/+bug/938180>\]
  - \[<https://bugs.launchpad.net/mixxx/+bug/894652>\]
  - \[<https://bugs.launchpad.net/mixxx/+bug/669273>\]
  - \[<https://bugs.launchpad.net/mixxx/+bug/889898>\]
  - \[<http://www.lastfm.at/api>\]
  - \[<http://developers.soundcloud.com/>\]

## Pick up or continue a GSoC 2012 project

The Ideas from 2013 can be viewed here: [GSoC 2012 Ideas](gsoc2012ideas)

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
