# Student Project Ideas for Google Summer of Code 2012

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of Code 2012](http://socghop.appspot.com/). Each
of these projects represents something that we think would make a really
big difference to our users and that we as a development team are really
excited about. For advice on how to get in touch and how to apply, you
should read [gsocadvice](gsocadvice).

A GSoC application that simply copy/pastes these deliverables will NOT
be accepted. We expect you think about the feature and how it aligns
with Mixxx's goals, outline potential use-cases and propose a plan for
implementing a solution.

## Key Detection for Harmonic Mixing

This feature aims to allow Mixxx users to simply and intuitively
incorporate harmonic mixing into their workflow.

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

## Synchronization Mode

If you've used Mixxx, then you know that our SYNC button is only a
one-time sync. All it does is match up the beats of the tracks that are
being mixed the moment you press the button.

There is tons of room for improvement here. The goal of this project is
to allow decks to be synchronized such that they actively check whether
they are in sync with the other, and make adjustments to stay in sync.

Additionally, a common feature in other DJ software is the ability to
set a master-clock to a desired BPM. When Sync-mode is on, decks should
also be able to synchronize themselves to the master-clock. This is
useful because the DJ can set a goal BPM for their set and make sure
they stay on tempo instead of gradually getting faster or slower.

Finally, Mixxx is missing useful widgets that inform the DJ of the
current state of their synchronization. For example, "phase meters" or
"peak-scopes" are useful tools for visualizing the current state of the
mix.

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

### Minimum Deliverables (Example)

  - Implement support for [Mac OS X Lion fullscreen
    mode](https://developer.apple.com/library/mac/#documentation/General/Conceptual/MOSXAppProgrammingGuide/FullScreenApp/FullScreenApp.html#//apple_ref/doc/uid/TP40010543-CH6-SW1)
  - Implement Windows 7 jumplist actions for deck playback controls
  - Implement file type handling (eg. "Open with.... Mixxx") 
  - Implement busy cursor or dock bouncing until Mixxx has finished
    loading

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**
