# Feature Discussion

This page is to discuss possible future features along with some
implementation details. Lengthy discussions will get moved to their own
page.

## Specifications for planned features

  - [Revamped Control System](Revamped%20Control%20System)
  - [Single-Deck Vinyl Control](Single-Deck%20Vinyl%20Control)
  - [N-Deck Support](N-Deck%20Support)
  - [Skinning Engine](Skinning%20Engine)
  - [DVS mode](DVS%20mode)
  - [Aubio (misnamed Beat
    Juggling)](Aubio%20\(misnamed%20Beat%20Juggling\))
  - [Library Metadata Rewrite using
    TagLib](Library%20Metadata%20Rewrite%20using%20TagLib)
  - [OSC Backend](OSC%20Backend)

## Implemented Specifications

  - [Looping](Looping)
  - [Configurable Cue Behaviour](Configurable%20Cue%20Behaviour)
  - [Code Organization and Cleanup](Code%20Organization%20and%20Cleanup)
  - [Library Rewrite Using SQLite](Library%20Rewrite%20Using%20SQLite)

## Abandoned Specifications

  - [Waveform Thread Refactor](Waveform%20Thread%20Refactor)
  - [Play queue and Library Improvements
    Proposals](playqueue_and_library_improvements_proposals)
  - [SoundSource Refactor/Merge](SoundSource%20Refactor/Merge)

## Good Intro Projects

**Looking to contribute to Mixxx? Here are some projects we think could
be done in a weekend, and would be a great introduction to the Mixxx
codebase.**

  - "Loading" animation for the waveforms
  - adjustable drag sensitivity on visual waveform view
  - also a way to change the direction ("scratching motion")
  - Visual 'track ending' indicator for visual waveform

## Other Ideas

[All Wishlist bugs on
Launchpad](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=-importance&search=Search&field.importance:list=WISHLIST&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.omit_dupes.used=&field.omit_dupes=on&field.has_patch.used=&field.has_cve.used=&field.tag=&field.tags_combinator=ANY)
[Blueprints on Launchpad](https://blueprints.launchpad.net/mixxx)

(Copied from [feature\_wishlist](feature_wishlist))

**If you think of a feature that we need to implement at some time, jot
it down here so you don't forget.**

Some of these are copied over from the forums and the old wiki, so they
may be done already or irrelevant.

  - Button in Auto DJ to start fading into new track (could come in
    handy if the current piece isn't going down to well).
  - Slider in Auto DJ to determine length of time of crossfade (e.g. 1s
    - 20s).
  - If song can not be loaded in Auto DJ, it might be good to
    automatically play the next track instead of displaying message and
    stopping the mix.
  - Track section marking with import/export support for DJ Notation
    (<http://www.djnotation.org/>)
  - Could also be used to mark loops?
  - Feature should be unobtrusive and it should be possible to disable
    the displaying temporarily
  - Since the markup will probably not be accurate (especially when
    using times out of DJ notation) the visualization should not imply
    it as 100% accurate, this also implies that these markers/sections
    will not really double as cue points
  - ~~Split cue/master headphone support~~ - Done: Pre/Main knob
    (\[Master\] headMix MixxxControl)
  - Effects panel integration with UI
  - 'Online' BPM detection so that visual waveform beat marks can
    actually be accurate. - BpmDJ engine being considered
  - ~~M4A support~~ - In progress
  - hotkey support (maybe configurable?)
  - Cheap mode (main out left, cue out right) so users can get started
    using mixxx without any extra soundcard.
  - [Effect plugins](PluginIdeas)
  - Live input (switchable input at first, maybe a delay/pitchable input
    later)
  - generic usb hid input support.
  - some more physically modeled turntable styles, with concepts of
    inertia, slipmat vector, and motor drive. [Details from Old
    Wiki](http://mixxx.sourceforge.net/wiki/index.php/Deck_Remodeling)
  - Normalize to the waveform, track volume and output (over longer
    period in the master output)
  - Channel gain to affect the waveform
  - BPM sync lock like in virtual dj (keep tracks in sync)
  - Play lock feature so that you can't change a track that is currently
    playing - Some MIDI scripts do this already
  - A button to switch between the vinyl emulation & pitch independent
    time stretch ("Master Tempo" on CDJs, "Key lock" or "Key correction"
    on others)
  - Adjustable key when key lock is active (as on the Numark
    CDX/HDX/X^2)
  - ~~Remain / played time display switch~~ - Already in
    Preferences-\>Interface-\>Position display
  - Would be nice if this could be done by just clicking the time field
    and would not require opening the preferences
  - Clipping light to stay on (dimmer?) after clipping, reset by
    clicking
  - Add a single deck view optimized for track setup (as in setting cue
    points and loops, potentially beat grid markers once we get some
    concept of beats with the beat detection feature planned for
    1.8.5/1.9)
  - Split file browser into two lists/columns -\> 1. Browser and 2.
    Playlist/Crates/Auto-DJ(all sorts of playlists). Songs can be drag
    and dropped more convenient, dj can see if song is already in the
    list. This should be optional.
  - Display a warning before a song can be dragged onto a running deck.
    This should be optional.
  - Auto-dj button should not be hidden, should be on the top layer of
    the interface so one can always see if it is activated.
