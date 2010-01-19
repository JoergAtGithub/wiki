# Development Roadmap

## Main Design Principles

These are some core goals which are critical for Mixxx to become a
world-class application, somewhat in order of importance:

  - **Stability** - Having a stable platform for DJs to work from is key
  - **Performance** - Optimize latency over throughput
  - Support a good level of latency for as many configurations as
    possible
  - Follow [Real-time application design
    principles](http://rt.wiki.kernel.org/index.php/HOWTO:_Build_an_RT-application)
    which will result in optimal latency even on non-RT systems.
  - Follow the [C++ software optimization
    guide](http://www.agner.org/optimize/optimizing_cpp.pdf) to choose
    data and program structures that will compile into the most
    efficient code.
  - **Usability** - Most functions must be bonehead-easy to use. The
    manual must not be required reading\!
  - Good hardware support
  - For as many devices as possible
  - With easiest possible setup
  - Support all likely input formats
  - Features
  - Should be guided by feedback from DJs
  - Great care should be taken to ensure that stability is not
    compromised by new features
  - Mixxx doesn't need to make the coffee, features should demonstrably
    improve the user experience

## Release Schedule

### 1.7.3

Bug-fix release. See <https://launchpad.net/mixxx/+milestone/1.7.3>

### 1.8.0

// Release Schedule //

  - Nov 16 2009 -- Feature Freeze
  - Jan 2010 -- Mixxx 1.8.0 Beta 1
  - Feb 10 2010 -- Mixxx 1.8.0 Final 

We're trying to sync up with the Ubuntu release cycle. Feature freeze
for Lucid Lynx is approximately February 14th, 2010.

[To-do list](1.8.0_to_do_list)

New main features:

  - Looping
  - New Library
  - True Pitchbend
  - Multiple MIDI device support
  - Shoutcast
  - M4A support

Side Projects

  - Build Server\!
  - Test Evangelism
  - SConscript Refactor

Bugs fixed: <https://bugs.launchpad.net/mixxx/+milestone/1.8.0>

### 1.8.5 .. 1.9.0 ?

Release Date: September 2010

Under the Hood Improvements

  - [Revamped Control System](Revamped%20Control%20System)
  - SSE Enhanced Engine
  - Timing engine 
  - Rubber Band support
  - BPM detection rework

New Features

  - LADSPA/LV2 Effects
  - [DVS mode](DVS%20mode)
  - n-Deck
  - External Mixer Mode
  - Incremental Library Enhancements (e.g. inline track previews)

### ???.???

Please don't add new features here unless there is a specification for
them. To add to the list of ideas that would be cool in Mixxx, add them
to [feature\_discussion](feature_discussion) or file a Wishlist bug at
Launchpad.

Random ideas for new features:

  - [Skinning Engine](Skinning%20Engine)
  - [Single-Deck Vinyl Control](Single-Deck%20Vinyl%20Control)
  - [Internationalization](http://doc.trolltech.com/4.5/i18n.html), see
    also [Qt
    Linguist](http://doc.trolltech.com/4.5/linguist-manual.html) and
    [Launchpad
    translations](https://help.launchpad.net/Translations/YourProject)
  - [Performance improvements](Performance%20improvements)
  - Macro/script playback
  - Sampler
  - Inline track previews

## Previous Release Roadmaps

### 1.7.0

*Released August 6, 2009*

[1.7.0 to do list](1.7.0%20to%20do%20list) (historical)

New features:

  - MIDI Learning
  - MIDI Scripting
  - Support for new controllers added, see the [hardware
    compatibility](hardware%20compatibility) page
  - Some [performance improvements](performance%20improvements)

Bugs fixed: See <https://launchpad.net/mixxx/+milestone/1.7.0>

## Changelog

Since Mixxx 1.6.0 was released, the following changes have been made:

  - MIDI Scripting functionality has been added
  - MIDI Learning functionality has been added

-----

Since Mixxx 1.5.0 was released (March 4th, 2007), the following changes
have been made:

  - New MIDI mappings for Tascam US-428, M-Audio X-Session Pro,
    Evolution X-Session, FaderFox DJ2, and the M-Audio Torq Xponent
  - ALSA Sequencer MIDI support courtesy of Cedric Gestes
  - A couple of MIDI bug fixes (knobs now center properly, thanks to
    Sacha Berger)
  - Added support for 14-bit MIDI pitch wheel controllers (thanks to
    Adam Sugerman)
  - Hercules support on Linux improved (jog wheels work again)
  - New nCut skin from Frank Willascheck
  - (Trancer skin?)
  - Big stability improvements (3 bug fixes)
  - Multiple soundcards can now be used for output (master/headphones),
    in case you don't have a soundcard with 4 outputs on it.
  - Adam's wicked colour scheme support for skins
  - Can now change skins without restarting Mixxx (more hard work from
    Adam)
  - Channel VU meters are now pre-fader
  - VU meters are now much more smooth
  - Added clipping indicators (courtesy of John Sully)
  - Higher quality EQs and other sound quality improvements (also from
    John Sully)
  - Adjustable EQ shelves
  - New MIDI mapping format now in XML, supports controlling LEDs
  - Better Hercules support on Windows and Linux
  - Initial support for recording output
  - New BPM detection algorithm (Micah Lee/GSoC)
  - New media library (Nathan Prado/GSoC)
  - LADSPA effects support (Pawel Bartkiewicz/GSoC)
  - BPM Tap tempo 
  - Library search function
  - Ported to QT4 (\!)
  - Moved build system to SCONS
  - Redesigned preferences dialogs
  - Rewritten audio core (Albert)
  - Vinyl control support for Serato, Traktor Scratch, and FinalScratch
    (FS needs work, but the others are good)
  - Software preamp for vinyl control (can use turntables without a
    preamp)
  - Track info editor (double-click in library)
  - New library browse mode (CTAF)
  - Starts in fullscreen mode if launched with the -f flag.
  - Several MP3 decoder performance and stability improvements (John
    Sully)
  - Support for merengue
  - Reorganized "File" menu
  - NEXT mode now works as expected (plays the next track in the table)
  - Lots of little OS X improvements
  - Improved consistency of fullscreen mode
  - Customizable constant power crossfader curve
  - Slow fade and fast cut crossfader curves
  - Play queue
  - Revamped playlist interface, editing
  - Experimental Shoutcast support
  - Somewhat intelligent library rescanning
