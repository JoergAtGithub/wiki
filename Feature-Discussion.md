# Feature Discussion

This page is to discuss possible future features along with some
implementation details. Lengthy discussions will get moved to their own
page.

## Specifications for planned features

  - [Registering MIDI input handlers from
    JavaScript](Registering%20MIDI%20input%20handlers%20from%20JavaScript)
  - [Controller Preferences](Controller%20Preferences)
  - [Mixxx Init Refactor](Mixxx%20Init%20Refactor)
  - [Controller Script Modules](Controller%20Script%20Modules)
  - [hid\_device\_api](hid_device_api)
  - [Revamped Control System](Revamped%20Control%20System)
  - [Skinning Engine](Skinning%20Engine)
  - [DVS mode](DVS%20mode)
  - [OSC Backend](OSC%20Backend)
  - [Multi-channel file mixing](Multi-channel%20file%20mixing)
  - [Modifier System](Modifier%20System)
  - [nonblockingdb\_status](nonblockingdb_status)
  - [Loop Recorder](Loop%20Recorder)
  - [Timing](Timing)
  - [Touch](Touch)
  - [Cues and loops 2.0](Cues%20and%20loops%202.0)
  - [OSC-Client](OSC-Client)
  - [Ctlra Support](Ctlra%20Support)
  - [Auto DJ Cues](Auto%20DJ%20Cues)
  - [Beat and Bar Edit Workflow](Beat%20and%20Bar%20Edit%20Workflow)

## Implemented Specifications

  - [Looping](Looping)
  - [Configurable Cue Behaviour](Configurable%20Cue%20Behaviour)
  - [Code Organization and Cleanup](Code%20Organization%20and%20Cleanup)
  - [Library Rewrite Using SQLite](Library%20Rewrite%20Using%20SQLite)
  - [Library Metadata Rewrite using
    TagLib](Library%20Metadata%20Rewrite%20using%20TagLib)
  - [Beatloops](Beatloops) as well as quantization for setting loops,
    cues and hotcues
  - [Aubio (misnamed Beat
    Juggling)](Aubio%20\(misnamed%20Beat%20Juggling\))
  - [Single-Deck Vinyl Control](Single-Deck%20Vinyl%20Control)
  - [N-Deck Support](N-Deck%20Support)
  - [Effects Framework](Effects%20Framework)

## Abandoned Specifications

  - [Waveform Thread Refactor](Waveform%20Thread%20Refactor)
  - [Play queue and Library Improvements
    Proposals](playqueue_and_library_improvements_proposals)
  - [SoundSource Refactor/Merge](SoundSource%20Refactor/Merge)

## Good Intro Projects

**[Looking to contribute to
Mixxx?](http://mixxx.org/manual/latest/chapters/getting_involved.html)
Here are some projects we think could be done in a weekend, and would be
a great introduction to the Mixxx codebase.**

Just pick a bug off of the [Easy Bug
List](https://bugs.launchpad.net/mixxx/+bugs?field.tag=easy)

## Other Ideas

[All Wishlist bugs on
Launchpad](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=-importance&search=Search&field.importance:list=WISHLIST&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.omit_dupes.used=&field.omit_dupes=on&field.has_patch.used=&field.has_cve.used=&field.tag=&field.tags_combinator=ANY)
[Blueprints on Launchpad](https://blueprints.launchpad.net/mixxx)

**If you think of a feature that we need to implement at some time,
[file a new wishlist bug](https://bugs.launchpad.net/mixxx/+filebug) if
it did not already exist on Launchpad.**

**DO NOT ADD ANYTHING TO THIS LIST -- File a bug instead. We are slowly
migrating this list to Launchpad**

Some of these are copied over from the forums and the old wiki, so they
may be done already or irrelevant.

  - ~~Button in Auto DJ to start fading into new track (could come in
    handy if the current piece isn't going down to well).~~ Targeted for
    Mixxx 1.11, implemented in
    <https://code.launchpad.net/~daschuer/mixxx/autodj>
  - ~~Slider in Auto DJ to determine length of time of crossfade (e.g.
    1s - 20s).~~ Targeted for Mixxx 1.11, implemented in
    <https://code.launchpad.net/~daschuer/mixxx/autodj>
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
  - ~~M4A support~~ - Implemented in Mixxx 1.10.
  - ~~hotkey support (maybe configurable?)~~ Hotcues implemented in
    Mixxx 1.10.
  - Cheap mode (main out left, cue out right) so users can get started
    using mixxx without any extra soundcard.
  - [Effect plugins](PluginIdeas)
  - Live input (switchable input at first, maybe a delay/pitchable input
    later)
  - generic usb hid input support.
  - some more physically modeled turntable styles, with concepts of
    inertia, slipmat vector, and motor drive. [Details from Old
    Wiki](http://mixxx.sourceforge.net/wiki/index.php/Deck_Remodeling)
  - ~~Normalize to the waveform, track volume and output (over longer
    period in the master output)~~ ReplayGain implemented in Mixxx 1.10
  - ~~Channel gain to affect the waveform~~ Implemented in Mixxx 1.10.
  - BPM sync lock like in virtual dj (keep tracks in sync)
  - Play lock feature so that you can't change a track that is currently
    playing - Some MIDI scripts do this already
  - ~~A button to switch between the vinyl emulation & pitch independent
    time stretch ("Master Tempo" on CDJs, "Key lock" or "Key correction"
    on others)~~ Implemented in Mixxx 1.10.
  - Adjustable key when key lock is active (as on the Numark
    CDX/HDX/X^2)
  - ~~Remain / played time display switch~~ - Already in
    Preferences-\>Interface-\>Position display
  - ~~Would be nice if this could be done by just clicking the time
    field and would not require opening the preferences~~ Implemented in
    Mixxx 1.10.
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
  - ~~Display a warning before a song can be dragged onto a running
    deck. This should be optional.~~ Implemented in Mixxx 1.10.
    Preferences-\>Interface-\>Track load behavior
  - Auto-dj button should not be hidden, should be on the top layer of
    the interface so one can always see if it is activated.
  - ~~Should be possible to drag and drop the song everywhere on the
    deck, not only on the waveform.~~ Implemented in Mixxx 1.10 .
    Draggable to waveform, waveform summary & Spinny widget in decks and
    samplers
