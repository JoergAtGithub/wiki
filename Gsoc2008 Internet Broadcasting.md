# Internet Broadcasting (GSoC 2008 project)

  - Student: **Wesley Stessens**
  - Mentor: **Adam Davison**

### Abstract

Implementing Shoutcast, Icecast and Icecast2 integration will allow
users to broadcast their mix in real-time over the world wide web on any
platform. At the moment this is only possible on Linux by using JACK
(Jack Audio Connection Kit), but this has a lot of limitations. By
implementing this functionality into Mixxx itself it will make tighter
integration between Shoutcast/Icecast and Mixxx possible. Think about
features like advanced metadata tagging or multiple streams. What’s more
important is that this will make it possible for users to broadcast
their mix over the internet on any platform supported by Mixxx. An MP3
and Ogg Vorbis encoder will have to be written for this project as well.
Metadata for the tracks will be sent separately for MP3 tracks or merged
into the Ogg-container for Ogg Vorbis-tracks.

### Detailed Application

A detailed application is available in Portable Document Format here:
<http://85.17.105.113/~wesley/mixxx_gsoc2008_broadcast_application.pdf>
- This document contains an implementation analysis, information about
my experience, my ideas about community interaction and personal
information about myself.

### Milestones

These milestones will keep track of the development process.

  - **Bold items** are items that have been implemented for the most
    part.
  - ***Italic/Bold items*** are items that are currently being worked
    on.

#### Milestone 1: Encoding

  - develop MP3 encoder using liblame
  - abstract a generic encoder class for both encoders
  - finish up the encoders
  - tweak and clean up code
  - write API documentation

#### Milestone 2: Broadcasting

  - find out why libshout is messing up
  - if we can't fix libshout: write own implementation instead
  - tweak and clean up code
  - write API documentation

#### Milestone 3: Release

  - put everything in broadcast/ subdir
  - enable by default (if code is stable)
  - write user documentation

#### Milestone 4: TAFT

  - Test, Analyze, Fix, Test again...
