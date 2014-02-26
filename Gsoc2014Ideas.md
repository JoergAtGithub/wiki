# Student Project Ideas for Google Summer of Code 2014

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of
Code 2014](http://www.google-melange.com/gsoc/homepage/google/gsoc2014).
Each of these projects represents something that we think would make a
really big difference to our users and that we as a development team are
really excited about. For advice on how to get in touch and how to
apply, you should read [GSoC Advice](gsocadvice).

**A GSoC application that simply repeats the project description will
NOT be accepted. We expect you to think about the feature and how it
aligns with Mixxx's goals, outline potential use-cases and propose a
plan for implementing a solution.**

## Cover Art Support

Over the years a highly requested feature has been for Mixxx to support
displaying cover art. This is a great project that combines both
aesthetics/design and engineering. Can you think of awesome, playful
ways to display cover art?

Some topics your proposal should cover:

  - Supporting loading cover art (from metadata tags, from cover images
    in album directories, etc.)
  - Deciding where and how to display the cover art in the GUI. 
  - Downloading cover art from metadata sources on the Internet if it is
    not available locally.

Your proposal should at the very least include details of how you will
accomplish each of these parts of the project but the project is by no
means limited to these topics. Make sure to think through the whole
design and implementation and be sure to include details of anything you
think may be relevant.

Since this project is small in scope, we expect that you will have
plenty of time to polish it and make it shine.

Links to Launchpad bugs:

  - <https://bugs.launchpad.net/mixxx/+bug/661459>
  - <https://bugs.launchpad.net/mixxx/+bug/890421>
  - <https://bugs.launchpad.net/mixxx/+bug/1015894>

## Keyboard / MIDI Mapping GUI

In Mixxx 1.11.0 we removed the old MIDI mapping GUI as we re-wrote the
controller subsystem to support HID devices. Now it's time to rewrite
the mapping GUI\! This GUI should be modular enough to support an HID
mapping GUI in the future. In previous versions of Mixxx the keyboard
mapping was accomplished via a text file. This project will move
keyboard mapping and processing into the new controller sub-system as a
new type of controller and introduce a user-friendly GUI for editing
keyboard presets and MIDI presets. For backwards compatibility, the
keyboard presets should still be stored on-disk in the same text format.

We suggest you check out the MIDI mapping GUI present in Mixxx 1.10.0
and think of ways to improve on it. For example, one very
user-unfriendly aspect of it was that you had to know the ControlObject
names of the controls you wanted to connect to a MIDI message. The
point-and-click MIDI mapping wizard in 1.11.0 now includes a drop-down
of all mappable controls. This is a much better way for users to decide
on what control to map a message to. Another very useful exercise is
checking out the various commercial DJ software offerings out there and
examining how they allow users to map MIDI controllers.

## Advanced Track Management / Organization Tools

Today, Mixxx provides DJs with limited tools for organizing their
library. Mixxx reads file metadata and stores track information in its
SQLite-based library. DJs are able to sort and search through their
music and organize the tracks into Crates and Playlists.

Editing of metadata can be done inline in the library and with the Track
Properties editor. These are fine for simple edits, but they should
allow the DJ to do much more.

This project aims to massively improve/replace the track metadata editor
built into Mixxx and make single or bulk editing of tracks much easier.

Your proposal should include a clear description of the shortcomings of
today's editor and how you plan to improve it. If appropriate, please
include mockups and diagrams illustrating your plans.

Some important questions to consider:

  - What information does Mixxx store about tracks (both DJ-related and
    non-DJ-related)?
  - For example: Crates, hotcues, loops, album, artist, etc.
  - What is the simplest user interface to allow the DJ to edit this
    metadata?
  - How will you handle single-track editing versus bulk editing?

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
