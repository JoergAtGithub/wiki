# Mixxx Macros - Google Summer of Code 2020 project

*By Janek Fischer (xerus/xerus2000)*

[Official GSoC Proposal](https://github.com/mixxxdj/mixxx/wiki/media/gsoc_2020_proposal_janek_fischer_-_mixxx_macros.pdf)


See [Macros](Macros) for a list of controls.

## Introduction

There are moves through which a DJ expresses himself - and there are
many other, sometimes tedious tasks that need to be done as groundwork.
Instead of having to juggle beatmatching, effects, cues and sliders all
at once, a DJ should be able to rely on his tools so he can focus on
what really matters. For some, beatmatching and keeping all tracks in
sync is an art in itself - for others, including me, it is something
happily delegated to the software - that is why there is a sync
function.

But sometimes, more sophisticated automation can be helpful - maybe you
want to skip a breakdown, shuffle around verses, loop an intro a
specific way or deliberately repeat certain parts. Handling that while
messing with effects and getting the next track ready can be tricky;
that is where Mixxx Macros come in. With this feature implemented, it
will be possible to record specific moves while playing a track and
store them in a rack, to be used when it gets hot.

## Requirements

### Personas

_Raptor_ is an experienced DJ who experiments with cue point drumming.

_Bob_ wants to prepare his track so he can DJ mostly hands-off at a
birthday party. For this he wants to censor his tracks as well prepare a
few transitions.

_Sona_ used to create custom versions of songs (extended & rearranged
parts) in Ableton Live, but would like to avoid the problems this
entails (duplication, quality loss through re-encoding, takes rather
long, can get lost in editing)

_Jannis_ wants to record Mash-ups in Mixxx, but currently has to
re-record them several times, and even then he doesn't get them exactly
how he wanted. He doesn't want to get into a DAW for that either.

### User Stories

#### As Raptor
- I want to
  - start a Macro recording
  - press cue points to create a beat
  - *if live* have it repeat immediately
  - save this as a looped Macro
  - assign it to a hotcue
- so that I have a cool custom beat based on a track, which I can invoke
anytime.
Requirements: everything on controller

### As Bob
- I want to create a very simple rearrangement and censoring of a track
- and save it to the track in enabled state
- so that the track is automatically played back in that arrangement.

Requirements: No controller

#### As Sona
- I want to be able to quickly recreate my Ableton Live edits in Mixxx
- so that I can eliminate the data duplication and speed up my workflow
for creating new edits.

#### As Jannis
- I want to record an edit to a track, potentially with cue point drumming
- so that I can play that back while creating a Mash-up.

I would appreciate the ability to edit a Macro so that I don't have to
re-record it if I made a small mistake

## Components

- database table to store Macros
- recording buttons (deck-independent)
- send info on cue jumps (but not on scrubbing)
- macro list for each deck with name, loop option, enable option

### Use cases

Adapted from
<https://m.facebook.com/story.php?story_fbid=10152750292038764&id=11864088763>

1.  Making edits
    1.  basic rearranging of tracks to create things like intros and
        outros, extend breaks, shorten or lengthen tracks, swap phrases
    2.  create "clean"/censored version of a track
    3.  create transition to another track e.g. double time version
    4.  create new beats from cue point drumming
2.  Live-looping of cue point drumming or tone play - being able to drum
    out a pattern using the cue points in a track and then seamlessly
    loop it at the touch of a button.

\-\> You never need the Macro recording controls and the audio recording
controls at the same time, so maybe they can be remapped.

### Data Format

A Macro needs to have a name and id, needs to be coupled to a track and
consists of an array of actions.

#### Actions

Each actions has some data and a type, the essential ones (as present in
Serato Flip) being censor and jump. Loop is also a consideration, but
bears some more questions: Should it use the same loop system the user
uses? If not, aren't jumps sufficient?

A big question is whether each action has its own start-point, or
whether there is a "wait" action that waits for a cue or timestamp to
occur. The latter may make sense in scripting, since it allows to easily
chain actions, but when recording there can hardly be a case where two
actions wouldn't be separated by a wait action. And if that is the case,
each action might as well have its own start-point - which might be a
hotcue or a timestamp, as outlined below.

#### Referencing cues vs timestamps

- timestamps: used by Serato Flip, persistent, but hardly editable;
    can break when track offset changes (when music file is swapped out)
- cues: can be moved, but that could also [accidentally mess up a flip](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197284228)
    and cues can't currently be shifted; add [confirmation dialog similar to when deleting a track in a playlist](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197283721)
    to avoid breaking things -\> but then cue needs to be aware of the
    Macros it's used in
- how relevant is editing afterwards, how can we facilitate it?
- Serato Flip ["just works"](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197286852)
  - Flip is locked after recording, not blocking any hotcues or any
    chance of breakage

### Name

"Macros" sounds like something to be triggered manually at any time -
the point of flips is that they usually happen automatically.

Suggestions: Spin, Routines, Twist, MicroFlow, Mow

"Routines" sounds nice, is
[descriptive](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197282607)
and [well-received](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197421948) - 
[we don't need to sell it either](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197282525).

It sounds a little bland though, and doesn't capture the whole idea of
using it to create non-destructive edits of a track. It also doesn't
blend well with other terms, such as "Routine Mode" (for recording a
routine).

I am now [against Routines, but not happy with Macros either](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/203376467).

### Discussion

- Recording could be implemented using [data emitted from the engine on cue jumps](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197293806)
    (not a signal, realtime\!)
- [Use developer window/shortcuts for debugging controls](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197532422),
    implement them first and then look at skins.
- [Macros are bound to one track - beware of scope creep](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197984243)
- [Should be usable from a controller - keep number of controls at minimum](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197984726)
- [Might activate actual loops - user can then disable it](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/198009610)
- [Reuse recording controls](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/199476162)

## Timeline

CW 21: Establish Timeline, work on open PRs, initial survey &
discussion
CW 22: Survey existing Serato Flip uses & collect input

**June**

Planned Deliverable: Format specification with examples

- CW 23: Work out details of the format
- CW 24: Start implementation of data structures, controls
- CW 25: Create recording infrastructure
- ~~CW 26~~ (blocked)

Result: Basic working recording implementation

**July**

Planned Deliverable: Macros can be recorded, saved and played back

- CW 27: Clean up, test & improve code
- CW 28: Refine architecture
- CW 29: Database
- (CW 30)

Result:
- Unit & end to end testing
- Macros can be saved

**August**

Planned Deliverables: Controls mapped to a skin and controller, Macros are automatically loaded on track load and can be enabled as well as invoked

- CW 31: Playback
- CW 32: Design controls & integrate into a skin

Result:
- Recording & Playback working correctly
- Added MacroControl with COs as major architectural redesign
- Unfortunately no visual feedback apart from controllers

Extras:
- Loop mode
- Enable Import from Serato & explore possibilities for sharing
- Waveform highlighting for upcoming jumps
- Record more controls
- Integration with other tools (Serato Flip, Export/Import, Edit Dialog, Auto DJ?)

## Log

### How I work

I tend to branch out to other open source contributions when I want to
work on something - I am almost unable to idle ;)
Evidence of that are regular reports on GitHub:
<https://github.com/search?q=xerus2000&s=created&type=Issues>
However, this can also lead to delays in what I was supposed to work on.

I currently use <https://notion.so> to take notes and may link some
pages here as proof of work - but these are personal working areas and
not optimized for general understanding. I will always incorporate
results into this wiki page when appropriate.

### CW 21 & 22

- Work on general PRs:
    <https://github.com/search?q=author%3Axerus2000+user%3Amixxxdj+updated%3A2020-05>
- Code Style discussions (Zulip & PRs)
- Planning & initial Research:
    <https://www.notion.so/xerus/Mixxx-Macros-GSoC-Research-5ab430eb8f0a41efafc075c220029560>

### CW 23

- revisited & summarized Zulip discussion in wiki page (timeline,
    details)
- sifted through [reddi]t(https://www.reddit.com/search?q=serato%20flip) -
    summary for now in Notion
- organized community call

### CW 24

- document data format ideas
- create & send out [survey](https://forms.gle/oUTHKUCQcczUZtHA8)
- finish remaining open PRs

### CW 25

Mo:
- Wiki Improvements
- [Get more acquainted with code](https://github.com/search?q=author%3Axerus2000+user%3Amixxxdj+updated%3A2020-06-15)
- Revisit [reddit post](https://www.reddit.com/r/DJs/comments/h8av2o/reimagining_serato_flip)
- Start writing [project-related code](https://github.com/mixxxdj/mixxx/pull/2873)

Tu: Specify required controls & format in [Macros](Macros) page

We: Architecture discussion & add [user stories](Mixxx-Macros-Requirements.md)

Th: Investigation of Mixxx code

Fr:
- Playing around with MacroManager
- More architecture considerations
- Trying to understand Controls, Signals & Slots

Sa:
- Connect a control
- Factor out RecordingManagerBase

### CW 26

Mo: Recording Macros works!

*Unfortunately I wasn't able to do any further this week for medical reasons.*

### CW 27

Mo: Getting back into code, wiki work

Tu: Make Macro recording realtime-proof

We: Some clean-up

Th: Work on wiki and start writing tests

Fr: Planning & Refocusing, Revamp architecture back out of Engine

### CW 28

Mo:
- Read about [Protobuf](https://developers.google.com/protocol-buffers/docs/proto) and created [initial Macro proto definition](https://github.com/mixxxdj/mixxx/blob/a30ecaa0b324e99946a0d35b6071e727c30c4879/src/proto/macro.proto)
- Wrote tests, investigated Mixxx E2E testing and wrote failing E2E test

Tu:
- Fix & Expand E2E tests
- ~Investigate database integration~

We:
- [Reviews](https://github.com/xerus2000/mixxx/pull/5)
- Look into database schema & [add documentation](https://github.com/mixxxdj/mixxx/pull/2925)
- Initial [storage format spec](Macros#storage)

Th & Fr:
- Refine Architecture

### CW 29

Mo:
- Proto serialization to database working
- Reviews

Tu:
- Implemented Macro deserialization
- Clean up & Improve code

*Holidays*

### CW 30

*Holidays*

- C++ Research (e.g. lambdas)
- Coding Style fixes & tests

### CW 31

Mo: Database & Side PR work

Tu: Research

We: Work on PlayerManager

Th: Code cleanups & clang-tidy investigation

Fr:
- Update call with Mentor
- Implemented Recording using SPSCQueue: https://github.com/mixxxdj/mixxx/commit/27b1d08546

Sa:
- Work on MacroManagerTest and its new parent abstraction MixxxDbTest

### CW 32

Mo:
- Work on side-PR reviews & personal tooling

Tu:
- Code update and merges, PR moved to https://github.com/mixxxdj/mixxx/pull/2989
- Work on side PRs
- Entered up work log for last 3 weeks
- Started Playback Implementation

We:
- Implement MacroDAO and integrate with TrackDAO
- Test MacroDAO
- Read Macro Actions from Track in Engine

Th:
- Research

Fr:
- Fix saving issue
- Macro Playback

### CW 33

Mo:
- Start implementing Macro Playback tests
- Fix local compilation issues

Tu:
- Fix Playback test
- Refactorings

We:
- Create MacroControl with Channel COs
- Cleanup

Th:
- Finish cleanup
- Implement COs & Playback in MacroControl
- Improve MacroDAO

Fr:
- Implement MacroControl ControlPushButtons
- Update Database

### CW 34

Mo: Save Macros via Track, add Playback to MacroControl & update COs

Tu: Implement MacroPtr & Improve DAO

We: Refactorings

Th: Improved controls & Added first MacroControl test

Fr: *Travel*


### CW 35

Mo: Debug MacroControl tests

Tu: MacroControl + Tests working!

We:
- Test MacroControl with controller (Traktor Kontrol F1)
- Final refactorings

Th:
- Work on blog post
- Macro & Track dirtiness
- Update controller mapping & COs
- Many misc fixes

Fr:
- Debug slots
- Make Status enum class & fix status checks

Sa:
- Debug failing tests
- Address reviews
- Document PR