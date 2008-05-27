# Development Roadmap

## Main Design Principles

These are some core goals which would seem to be critical for Mixxx,
somewhat in order of importance:

  - Stability
  - Having a stable platform for DJs to work from is key
  - Good hardware support
  - For as many devices as possible
  - With easiest possible setup
  - Support a good level of latency for as many configurations as
    possible
  - Support all likely input formats
  - Features
  - Should be guided by feedback from DJs
  - Great care should be taken to ensure that stability is not
    compromised by new features
  - Mixxx doesn't need to make the coffee, features should demonstrably
    improve the user experience

## Release Schedule

### 1.5.2

Depending on developer time, we may backport some bugfixes to 1.5.0 and
do a maintenance release of the 1.5 series while 1.6.0 is becoming
stable.

### 1.6.0

This will be the next feature release and will include (hopefully) all
the stuff in the changelog below. Fast pace of development has meant
lots of work originally slated for 1.7 will make it into this release.
The huge number of new features mean it will probably stay in beta for
several months. In addition to the features in the changelog, it will
hopefully also have:

  - More hardware controller support
  - Build system moved to scons
  - Vinyl control
  - Anything else exciting we have time for...

#### Remaining TODO For 1.6.0 Final

  - Fix critical bugs: <https://bugs.launchpad.net/mixxx/1.6/+bugs>

### 1.7.0

This will be the feature release following 1.6.0 and will probably go
into beta some time in 2008. No fixed plans this far into the future but
rough targets are:

  - Macro/script playback
  - Sampler
  - [Internationalization?](http://doc.trolltech.com/4.3/i18n.html)

## Changelog

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
