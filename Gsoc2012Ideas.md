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

### Suggested Minimum Deliverables

  - Implement a master-clock in the Mixxx engine
  - The master clock will have a BPM that it "beats" at.
  - Implement synchronization of decks to the master clock signals. 
  - Synchronization in this case is: 

<!-- end list -->

``` 
    * Adjusting the rate of each deck to match the master clock
    * Adjusting the "phase" or the alignment of the deck so that the beats of the deck line up with the beats of the master clock. 
* Create GUI widgets to control the master clock and assign a deck to synchronize to the master clock.
* Allow a deck to be set as the "master" deck 
* This is more open-ended -- think about the different ways to implement this and talk about it in your proposal.
* Bonus: Implement a metronome feature that ticks to the beat of the clock.
* Bonus: Implement a phase-meter that represents the sync of each deck to its target sync source. [[https://bugs.launchpad.net/mixxx/+bug/753301|Bug #753301]]
```

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

## Plug and Play MIDI Mode / Community MIDI Mappings

Mixxx currently supports a wide-range of hardware MIDI controllers that
DJs can use to perform with. Each supported MIDI controller has a
"mapping" file that is bundled with Mixxx, but this mapping must be
manually selected by the user before their controller works. The aim of
this project is to increase the usability for new users by automatically
selecting the correct MIDI mapping and to provide an intelligent
workflow for when an unsupported MIDI device is connected.

This project will involve a lot of time thinking about use cases,
dealing with users and understanding their requirements. It would be a
great opportunity for a student to get involved with the Mixxx
community. The student will also have the opportunity to borrow a MIDI
controller from the development team for the duration of the project.

### Suggested Minimum Deliverables

  - Automatically select an appropriate controller mapping when a user
    plugs in a device.
  - For unsupported devices, implement a UI and simple server-side
    functionality to:
    1.  Check mixxx.org for additional community-provided mappings.
    2.  Allow ratings and comments to be made on community-provided
        mappings.
    3.  Allow user-created mappings to be uploaded to mixxx.org.

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

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**

### Minimum Deliverables

  - Something awesome. We will work with you to define the deliverables.
