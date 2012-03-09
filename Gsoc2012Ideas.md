# Student Project Ideas for Google Summer of Code 2012

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of Code 2012](http://socghop.appspot.com/). Each
of these projects represents something that we think would make a really
big difference to our users and that we as a development team are really
excited about. For advice on how to get in touch and how to apply, you
should read [gsocadvice](gsocadvice).

## Synchronization Improvements

If you've used Mixxx, you know that our SYNC button does not work very
well\! All it does is match up the BPMs of the tracks that are being
mixed. There is tons of room for improvement here. The goal of this
project is to allow two decks to be synchronized such that they actively
check whether they are in sync with the other, and make adjustments to
stay in sync. Additionally, the creation of a master sync clock for
decks to sync to would be great as well, because then the DJ could set
the master clock at e.g. 130 BPM and all the songs they load would
automatically sync to the tick of that clock.

### Minimum Deliverables

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
```

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

### Minimum Deliverables

  - Implement auto-selection of MIDI mappings based on connected MIDI
    devices.
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
be the most useful for Mixxx, and implementing several of those.

For ideas, check out:

  - [Q7Goodies](http://www.strixcode.com/q7goodies/) 
  - [Features new to Windows 7
    (Wikipedia)](http://en.wikipedia.org/wiki/Features_new_to_Windows_7)
  - [Features new to Windows 8
    (Wikipedia)](http://en.wikipedia.org/wiki/Features_new_to_Windows_8)

### Suggested Minimum Deliverables

  - Implement support for [Mac OS X Lion fullscreen
    mode](https://developer.apple.com/library/mac/#documentation/General/Conceptual/MOSXAppProgrammingGuide/FullScreenApp/FullScreenApp.html#//apple_ref/doc/uid/TP40010543-CH6-SW1)
  - Other Windows 7 features

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**

### Minimum Deliverables

  - Something awesome. We will work with you to define the deliverables.
