# Feature Discussion

This page is to discuss possible future features along with some
implementation details. Lengthy discussions will get moved to their own
page.

## Specifications for planned features

  - [Revamped Control System](Revamped%20Control%20System)
  - [Configurable Cue Behaviour](Configurable%20Cue%20Behaviour)
  - [Looping](Looping)
  - [Library Rewrite Using SQLite](Library%20Rewrite%20Using%20SQLite)
  - [Code Organization and Cleanup](Code%20Organization%20and%20Cleanup)
  - [Single-Deck Vinyl Control](Single-Deck%20Vinyl%20Control)
  - [Waveform Thread Refactor](Waveform%20Thread%20Refactor)
    \*abandoned\*
  - [Play queue and Library Improvements
    Proposals](playqueue_and_library_improvements_proposals)
    \*abandoned\*
  - [Skinning Engine](Skinning%20Engine)
  - [DVS mode](DVS%20mode)
  - [SoundSource Refactor/Merge](SoundSource%20Refactor/Merge)

## Other Ideas

[All Wishlist bugs on
Launchpad](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=-importance&search=Search&field.importance:list=WISHLIST&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.omit_dupes.used=&field.omit_dupes=on&field.has_patch.used=&field.has_cve.used=&field.tag=&field.tags_combinator=ANY)

(Copied from [feature\_wishlist](feature_wishlist))

If you think of a feature that we need to implement at some time, jot it
down here so you don't forget.

Some of these are copied over from the forums and the old wiki, so they
may be done already or irrelevant.

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
  - Visual 'track ending' indicator for visual waveform
  - Effects panel integration with UI
  - 'Online' BPM detection so that visual waveform beat marks can
    actually be accurate. - BpmDJ engine being considered
  - ~~M4A support~~ - In progress
  - hotkey support (maybe configurable?)
  - adjustable drag sensitivity on visual waveform view
  - also a way to change the direction ("scratching motion")
  - direct outs (table 1, table 2, master, headphones)
  - [Effect plugins](PluginIdeas)
  - Live input (switchable input at first, maybe a delay/pitchable input
    later)
  - OSC controlled backend [Details from Old
    Wiki](http://mixxx.sourceforge.net/wiki/index.php/OSC_Backend)
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
  - "Loading" animation for the waveforms
  - Clipping light to stay on (dimmer?) after clipping, reset by
    clicking
  - Add a single deck view optimized for track setup (as in setting cue
    points and loops, potentially beat grid markers once we get some
    concept of beats with the beat detection feature planned for
    1.8.5/1.9)
