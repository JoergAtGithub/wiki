# Student Project Ideas for Google Summer of Code 2013

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of
Code 2013](http://www.google-melange.com/gsoc/homepage/google/gsoc2013).
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

## Plug and Play MIDI Mode / Community MIDI Mappings

Mixxx currently supports a wide-range of hardware MIDI controllers that
DJs can use to perform with. Each supported MIDI controller has a
"mapping" file that is bundled with Mixxx, but this mapping must be
manually selected by the user before their controller works. The aim of
this project is to increase the usability for new users by automatically
selecting the correct MIDI mapping and to provide an intelligent
workflow for when an unsupported MIDI device is connected.

When a mapping for a MIDI device is not present, the user should not be
left out in the cold. She should have the option of connecting to
mixxx.org to see if there are any official or user-contributed mappings
available for download. It's easy to imagine the various interesting
turns this could take.

Since there is a server-side component to this project we ask that
applicants be familiar with a web development framework that would be
suitable for writing an API for mixxx.org. We suggest
[Django](http://djangoproject.com).

This project will involve a lot of time thinking about use cases,
dealing with users and understanding their requirements. It would be a
great opportunity for a student to get involved with the Mixxx
community. The student will also have the opportunity to borrow a MIDI
controller from the development team for the duration of the project.

## Loop Recorder

A Loop Recorder is a module that allows the DJ to record short segments
of the audio output (decks, cue/headphones, main output, etc.) and then
play-back and remix the recorded segment into their mix. This is a key
element of many controllerist and scratch routines.

This project will involve mostly architectural changes to the Mixxx
mixing engine so digital signal processing experience is not a
pre-requisite. In the process of writing up your proposal, we expect you
to flesh out the different use cases you can think of for the loop
recorder. Make sure to explore the Internet a little bit to find out
more about what people use loop recorders for, specifically in a DJing
context.

Some related bugs on Mixxx's bug tracker can be found here:

  - <https://bugs.launchpad.net/mixxx/+bug/692926>
  - <https://bugs.launchpad.net/mixxx/+bug/774808>
  - <https://bugs.launchpad.net/mixxx/+bug/878549>
  - <https://bugs.launchpad.net/mixxx/+bug/408111>
  - <https://bugs.launchpad.net/mixxx/+bug/717841>

## Streaming Services Support (SoundCloud, Last.fm, YouTube, Spotify, Grooveshark, etc.)

There are many music discovery services which give users access to a
broad library of music. Many of these services have APIs that allow
3rd-party clients to access the services and stream music on the behalf
of the user. We think these services will be a powerful tool for our
users to explore how songs fit in their mixes.

Your application should include details of which streaming services you
plan to integrate and how you will make use of their APIs (if they
exist). In the very least, your proposal should define a modular system
for plugging in new streaming services so that in the future all that is
required to add more is defining how to search and stream from the API
of the new service.

Some related bugs on Mixxx's bug tracker can be found here:

  - <https://code.launchpad.net/~max-linke/mixxx/library_features>
  - <https://bugs.launchpad.net/mixxx/+bug/938180>
  - <https://bugs.launchpad.net/mixxx/+bug/894652>
  - <https://bugs.launchpad.net/mixxx/+bug/669273>
  - <https://bugs.launchpad.net/mixxx/+bug/889898>
  - <https://bugs.launchpad.net/mixxx/+bug/918222>

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

## Enhanced Platform Integration

Thanks in large part to Qt and a number of other cross-platform
libraries, Mixxx runs on Windows, Mac OS X, and Linux. Although we're
able to provide a *consistent* user experience on all three platforms,
we'd like to provide a better *integrated* experience. We want to take
advantage of the unique features that each platform provides, like the
new fullscreen mode in OS X Lion or the new jump list in Windows 7 or
gvfs in Linux, so that Mixxx feels as *native* as possible.

Qt already provides a [small number of platform integration
features](http://qt-project.org/doc/qt-4.8/exportedfunctions.html), but
to take advantage of other newer features that Qt doesn't have,
platform-specific code for Windows, Mac OS X und Linux must be added to
Mixxx. This project will involve figuring out which platform-specific
features in Windows 7, Windows 8, Mac OS X Lion, and Mac OS X Mountain
Lion would be the most useful for Mixxx users, and implementing several
of those. (We don't expect students to have access to both Linux and
Windows and Mac OS X, so a proposal focusing on one particular OS is OK,
but an awareness of all platforms is a plus.)

This project could also include more basic polishing tasks, so if
there's some little inconsistencies about Mixxx that have been bugging
you, here's your chance to fix them.

For ideas, check out:

  - [Q7Goodies](http://www.strixcode.com/q7goodies/) 
  - [Features new to Windows 7
    (Wikipedia)](http://en.wikipedia.org/wiki/Features_new_to_Windows_7)
  - [Features new to Windows 8
    (Wikipedia)](http://en.wikipedia.org/wiki/Features_new_to_Windows_8)
  - <https://codereview.qt-project.org/#change,48152>

## Intelligent Track Suggestions / Smart Crates

Sometimes it can be useful to have a song suggested based on the
currently playing one or just search the library with a set of
parameters (BPM/Year/Key/...). This could be used to build playlists and
find some songs on the go. There has been some work on this last year
already, you can find it in the launchpad repo. A lot of mediaplayers
can already do that (smart playlists) based on BPM/Genre/year/Artist/...
and use information saved in the file or on the Internet (see exaile as
an example).

Your proposal should include how this feature will be included in the
GUI, if and how the tracks are ranked. What information you want to use
to make the suggestions.

Related Links:

  - <https://code.launchpad.net/~mr-unwell2006/mixxx/track_selector_feature>
  - <https://bugs.launchpad.net/mixxx/+bug/889898>

## Advanced Tagging

Finding the right track at the right time is a key for beeing a good DJ.
While the "Intelligent Track Suggestions" focuses on the live GUI. This
projekt aims to the Metadata of the track itselve and the GUI to edit
them.

Currently Mixxx does not write metatdata back to the tracks. The tagging
capability of mixxx is low compared to current media players. It is a
good idea to catch up.

But since Mixxx is a DJ Software, we might go a step ahead and allow
also editting other track related data in a fast and intuitive editor.
This is much more than Artist, Album and Bmp.

You proposal should include a clear view about the track related Metada
a DJ is focusing on. You should point out the different to other Tools
and a GUI scribble is also helpfull.

For me, the main focus of this project and the place for your ideas the
user experience while editing meta date.

## Non-Blocking Database Access

Currently some database transactions are stalling the GUI. This is
because some database queries are preformed from the GUI thread.

This should be solved during the project by something like a standard
non blocking interface to sqlite. All Database queries should be issued
though this new interface.

This project would make Mixxx more reliable by this new concept how to
deal with database actions.

Your proposal should include a draft proposal how do you will achieve
the goal. You should have already have experience in parallel processing
and sqlite.

## Library GUI Layout Redesign

The current library GUI needs to be polished and needs to give room for
new features.

You find everything relevant collected here
<https://blueprints.launchpad.net/mixxx/+spec/three-column-library-layout>.

The current GUI proposals at
<https://bugs.launchpad.net/mixxx/+bug/986704> are the result from our
last design work. It should give a clue what direction we will go. But
please make them to your own. What do we need most form your experience
with Mixxx?

The current code driving the library is hard to maintain because it was
growing along with Mixxx. Here is a concept required, how we could make
it again maintainable and extendable. You should have Qt experience and
a clue about Qt's implementation of the MVC pattern.

A great source for design hints is also the code from Qt based media
players e.g Clementine or Tomahawk,

The difficulty of this project is focus on the daily DJ Us cases, but
allow also crazy new features, without clutter the GUI. Maybe you should
tell the story how the GUI will be used.

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
