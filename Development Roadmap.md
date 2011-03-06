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

### 1.10

  - Vinyl Control rewrite
  - Library Improvements
  - Traktor/RB Feature Rewrites
  - Major Browse Improvements
  - Crate/Playlist Locking
  - Sampler Units
  - Potentially without load/saving of presets
  - [Effects](effects_framework)
  - EffectChain infrastructure, simple UI improvements
  - External Audio Passthrough
  - CoreAudio in Mixxx proper (instead of just AppStore)
  - Looping
  - Quantized Looping
  - Beat Loops
  - Other Stuff\!
  - Multiple Soundcard Synchronization improvements
  - [Internationalization](http://doc.trolltech.com/4.5/i18n.html)
  - Library Version Bumps
  - SoundTouch -\> 1.5.0
  - xwax -\> 0.8

### Probably Longer Term

To add to the list of ideas that would be cool in Mixxx, add them to
[feature\_discussion](feature_discussion) or file a Wishlist bug at
Launchpad.

  - [Skinning Engine](Skinning%20Engine)
  - [Revamped Control System](Revamped%20Control%20System)

## Historical Release Roadmaps

*Released February 19th, 2011*

### 1.9.0

More in-depth details on Launchpad:
<https://launchpad.net/mixxx/+milestone/1.9.0> Release Date: Goal:
December 25, 2010 Actual: February 19, 2011

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
  - Feature freeze: November 14th
  - Strings freeze: November 24th
  - GUI freeze: November 30th
  - Beta1 Released: Dec 5th -
    <http://mixxxblog.blogspot.com/2010/12/mixxx-190-beta1-and-182-released.html>
  - Release: \~End of 2010

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

[1.7.0 to do list](1.7.0%20to%20do%20list) (historical)

New features:

  - MIDI Learning
  - MIDI Scripting
  - Support for new controllers added, see the [hardware
    compatibility](hardware%20compatibility) page
  - Some [performance improvements](performance%20improvements)

Bugs fixed: See <https://launchpad.net/mixxx/+milestone/1.7.0>

## Changelogs

Available on the [Mixxx blog](http://mixxxblog.blogspot.com)
