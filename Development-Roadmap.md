# Development Roadmap

This page represents the opinion of the Mixxx development team, as such
it is not editable by general users. If you have comments or
suggestions, please [contact us](http://www.mixxx.org/support.php).

## Main Design Principles

These are some core goals which are critical for Mixxx to become a
world-class application, somewhat in order of importance:

  - **Stability** - Having a stable platform for DJs to work from is key
  - **Performance** - Optimize latency over throughput
  - Support a good level of latency for as many configurations as
    possible
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

### 2.2

  - [2.2.0 Milestone on
    Launchpad](https://launchpad.net/mixxx/+milestone/2.2.0)
  - Beta Date
  - Goal: July 1, 2017
  - Release Date
  - Goal: August 1, 2017

### 2.1

  - [2.1.0 Milestone on
    Launchpad](https://launchpad.net/mixxx/+milestone/2.1.0)
  - Beta Date
  - Goal: February 5, 2017
  - Release Date
  - Goal: April 1, 2017

#### Feature Targets

  - Bug fixes, polishing post 2.0.

### 1.12 / 2.0

  - [2.0.0 Milestone on
    Launchpad](https://launchpad.net/mixxx/+milestone/2.0.0)
  - Beta Date
  - April 29, 2015
  - Release Date
  - Goal: December \~20th, 2015

#### Feature Targets

  - Master Sync
  - 4 Decks
  - Effect Engine
  - Resizable UI
  - Harmonic Mixing / Key Detection
  - MIDI Binding GUI / Enhanced MIDI Learn
  - User Manual Translations
  - Much more\! -- check the milestone page.

### 1.11

  - [1.11.0 Milestone on
    Launchpad](https://launchpad.net/mixxx/+milestone/1.11.0)
  - Feature Freeze
  - Code: April 23, 2012
  - Strings: May 10th, 2012
  - GUI: May 10th, 2012
  - MIDI Scripts: May 25th, 2012
  - Beta Date
  - Goal: May 1st, 2012
  - Release Date
  - Goal: June 1, 2012

#### Feature Targets

  - Re-vamped Auto-DJ support
  - Session History Feature
  - Advanced Search Operators
  - Colored, tri-band waveforms
  - Drastically improved BPM and beat detection via VAMP plugins.
  - HID Controller Support via Scripting

### 1.10

  - More in-depth (and up-to-date) details on Launchpad:
    <https://launchpad.net/mixxx/+milestone/1.10.0>
  - Feature Freeze
  - Code: May 1st, 2011
  - Strings: May 16th, 2011
  - GUI: May 16th, 2011
  - MIDI Scripts: May 16th, 2011
  - Release Date
  - Goal: May 29th, 2011 
  - Actual: Dec 24th, 2011

#### Feature Targets

  - Vinyl Control rewrite
  - Library Improvements
  - Traktor/RB Feature Rewrites
  - Major Browse Improvements
  - Crate/Playlist Locking
  - Other misc improvements (crate export/import)
  - Library performance improvements
  - Sampler Units
  - Potentially without load/saving of presets
  - External Audio Passthrough
  - CoreAudio in Mixxx proper (instead of just AppStore)
  - Looping
  - Quantized Looping
  - Beat Loops
  - Loop Double/Halve
  - Other Stuff\!
  - Multiple Soundcard Synchronization improvements
  - Soft-takeover Support
  - [Internationalization](http://doc.trolltech.com/4.5/i18n.html)
  - Library Version Bumps
  - SoundTouch -\> 1.5.0
  - xwax -\> 0.8
  - gtest/gmock -\> 1.5.0

*Released February 19th, 2011*

### 1.9.0

  - More in-depth details on Launchpad:
    <https://launchpad.net/mixxx/+milestone/1.9.0>
  - Feature Freeze
  - Code: Nov 14th 2010
  - Strings: Nov 24th, 2010
  - GUI: Nov 30th, 2010
  - Release Date
  - [Beta1](http://mixxxblog.blogspot.com/2010/12/mixxx-190-beta1-and-182-released.html):
    Dec 5, 2010
  - Goal: December 25, 2010 
  - Actual: February 19, 2011

<!-- end list -->

  - Shoutcast/Icecast
  - SampleUtil / Hydra (optimizations)
  - External Mixer Mode
  - HSS1394 controller support
  - Random incremental improvements
  - Library improvements:
  - Taglib for faster scanning, better metadata
  - Fixes for iTunes/Rhythmbox slowness
  - Ratings widget, played column
  - Deprecated Qt3 code removal

Side projects:

  - ~~SConscript Refactor~~
  - ~~Build server - You can help by
    [donating](http://www.pledgie.com/campaigns/13624)\!~~
  - ~~Reading with Taglib~~

*Released October 5th, 2010*

### 1.8.0

// Release Schedule //

  - Nov 16 2009 -- Feature Freeze
  - Feb 5 2010 -- private(-ish) beta testing
  - Feb 15 2010 -- Mixxx 1.8.0 Beta 1
  - May-July -- Mixxx 1.8.0 Beta 2
  - ??? - Mixxx 1.8.0 Final 

Keep in mind that as we have no full-time developers, this schedule is
likely to change due to external pressures. Don't plan anything
important around it.

We tried to sync up with the Ubuntu release cycle, but were unable to
commit enough developer time to fixing bugs, despite our best efforts.
(Feature freeze for Lucid Lynx was February 18th, 2010.) *We did get
Mixxx 1.8.0 into Ubuntu 10.10 though\!* [To-do list](1.8.0_to_do_list)

New main features:

  - Looping
  - New Library
  - Ramping Pitchbend
  - Multiple MIDI device support
  - M4A support via SoundSource plugin architecture
  - Hot cues, multiple cue points
  - New skins

Side Projects

  - Unit Testing

Bugs fixed: <https://bugs.launchpad.net/mixxx/+milestone/1.8.0>

### 1.7.0

*Released August 6, 2009*

[1.7.0 to do list](1.7.0-to-do-list.md) (historical)

New features:

  - MIDI Learning
  - MIDI Scripting
  - Support for new controllers added, see the [hardware
    compatibility](hardware%20compatibility) page
  - Some [performance improvements](performance-improvements.md)

Bugs fixed: See <https://launchpad.net/mixxx/+milestone/1.7.0>

## Changelogs

Available on the [Mixxx blog](http://mixxxblog.blogspot.com)
