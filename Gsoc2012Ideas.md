# Student Project Ideas for Google Summer of Code 2012

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of Code 2012](http://socghop.appspot.com/). Each
of these projects represents something that we think would make a really
big difference to our users and that we as a development team are really
excited about. For advice on how to get in touch and how to apply, you
should read [GSoC Advice](gsocadvice).

**A GSoC application that simply repeats the project description will
NOT be accepted. We expect you to think about the feature and how it
aligns with Mixxx's goals, outline potential use-cases and propose a
plan for implementing a solution.**

## Point-And-Click Controller Mapping

Mixxx's MIDI-Learning wizard is not very usable. In order to map a
controller, you have to go through the entire wizard even if your
controller doesn't have the buttons that are hard-coded into the
wizard's learning process.

This project will replace the MIDI-Learning wizard with an intuitive and
easy-to-use point-and-click system for mapping a controller. When you
want to map a control, just click on the button or knob in the GUI that
you want to map and then turn the corresponding button or knob on your
controller.

  - How will you figure out what GUI element was clicked with Qt?
  - What do you do if the button isn't in the skin?
  - How do other DJ software apps allow MIDI mapping? 

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

## Library Preview Player

Selecting the next track to play is possibly the \#1 hardest part of
DJing. Today if you want to preview a track you have to load it to a
deck and use the PFL (pre-fader listen) to listen to the track in your
headphones. This project aims to provide a "preview" player that lets
DJs listen to tracks in their headphones without having to load them to
a deck.

## Vinyl Pass-through Mode

Mixxx allows you to DJ with timecode records and CDs. This project aims
to bring a vinyl pass-through mode to Mixxx. Pass-through mode is a
useful feature for DJs who still have part of their music collection on
vinyl or CDs. When pass-through is enabled for a deck, Mixxx takes the
input audio from the turntable or CDJ and outputs it directly as the
deck audio output.

## Key Detection for Harmonic Mixing

This feature aims to allow Mixxx users to simply and intuitively
incorporate [harmonic
mixing](http://en.wikipedia.org/wiki/Harmonic_mixing) into their
workflow.

Using an open-source key detector like
[KeyFinder](http://www.ibrahimshaath.co.uk/keyfinder/) or
[Chordata](http://clam-project.org/wiki/Chordata_tutorial), you will be
responsible for adding key detection support to Mixxx's current analysis
system.

After adding key-detection, you will have to change the way that Mixxx
uses the [SoundTouch](http://www.surina.net/soundtouch/) library to
enable changing the pitch independent of the tempo. Today, Mixxx uses
SoundTouch to change the tempo independent of the pitch (this is called
**keylock**). The opposite problem is changing the pitch independent of
the tempo. This is essential for harmonic mixing. If you have two tracks
that are in different keys, then you have to adjust their pitch until
they are in the same key. You do not have to implement pitch-shifting
yourself -- this is already done by the SoundTouch library. See also:
[pitch\_percentages\_for\_semitones\_and\_notes](pitch_percentages_for_semitones_and_notes)

Once you have done this infrastructure work then you will have to decide
how to expose these features to the user. This is an open-ended part of
your application that will show us you have thought about the DJ
use-cases and understand how the feature will be used. Make sure to
explain the user-facing changes you would make to Mixxx and how they
support the use-cases of this feature in your application.

## Enhanced Platform Integration

Thanks in large part to Qt and a number of other cross-platform
libraries, Mixxx runs on Windows, Mac OS X, and Linux. Although we're
able to provide a *consistent* user experience on Windows and Mac OS X,
we'd like to provide a better *integrated* experience on each of these
platforms. We want to take advantage of the unique features that each
platform provides, like the new fullscreen mode in OS X Lion or the new
jump list in Windows 7, so that Mixxx feels as *native* as possible.

Qt already provides a [small number of platform integration
features](http://qt-project.org/doc/qt-4.8/exportedfunctions.html), but
to take advantage of other newer features that Qt doesn't have,
platform-specific code for Windows and Mac OS X must be added to Mixxx.
This project will involve figuring out which platform-specific features
in Windows 7, Windows 8, Mac OS X Lion, and Mac OS X Mountain Lion would
be the most useful for Mixxx users, and implementing several of those.
(We don't expect students to have access to both Windows and Mac OS X,
so a proposal focusing on one particular OS is OK, but an awareness of
both platforms is a plus.)

This project could also include more basic polishing tasks, so if
there's some little inconsistencies about Mixxx that have been bugging
you, here's your chance to fix them.

For ideas, check out:

  - [Q7Goodies](http://www.strixcode.com/q7goodies/) 
  - [Features new to Windows 7
    (Wikipedia)](http://en.wikipedia.org/wiki/Features_new_to_Windows_7)
  - [Features new to Windows 8
    (Wikipedia)](http://en.wikipedia.org/wiki/Features_new_to_Windows_8)

## Library Database Management

Many Mixxx users initially start using it their desktop PC, saving cue
points and other metadata to Mixxx's database. When you actually get a
DJ gig though, you'll want to move that database to a laptop. There's
currently no official way to do this from inside Mixxx, nor is there a
way to migrate your library database or some subset of the data to an
external USB drive. There are several important use cases that we've
overlooked - Find out what they are by browsing our forum, bug tracker,
or just thinking about how DJs work, and propose fixing several of them.

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. Our bug tracker is
full of wishlist bugs and other ideas scattered throughout, so if you
browse through it, you may find many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
