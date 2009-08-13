# Library Rewrite Using SQLite

## Summary and Rationale

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

This project is already in progress\! Check it out on launchpad in the
lp:\~mixxxdevelopers/mixxx/features\_sqlite branch.

## Use Cases

  - DJ Bill wants DJ software that has a good library. He's tried Mixxx
    but its library does not scale to his large collection of music. It
    is also buggy, and often gets corrupted so he cannot build up
    quality metadata about his music.
  - **Your use case here**

## Design

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

## Current Progress

The meat of the project is done. There's still a solid body of work
left, but much of it is polish and restoring old features.

From the Mixxx 1.8.0 developer meeting, some of the remaining issues
are:

  - rewrite the track editor
  - searches still block the GUI, make them asynchronous
  - Library rescanning needs work
  - Playlist support
  - Crate support
  - Browse mode
  - tagging
  - abstraction of track sources (e.g. to allow for ipod source)
  - browse mode
  - Cue/loop storage in the DB
  - bling-bling delegates
  - XML migration strategy (is this even worth it?)
  - bulk BPM detection and other library-wide things

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - Albert Santoni
  - RJ Ryan
