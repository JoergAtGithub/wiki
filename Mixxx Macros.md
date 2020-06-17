# Mixxx Macros

*By Janek Fischer (xerus/xerus2000)*

![Official GSoC
Proposal](/gsoc_2020_proposal_janek_fischer_-_mixxx_macros.pdf)

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

## Details

[Macros](Macros)

[Macro Requirements](Macro%20Requirements)

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
  - cues: can be moved, but that could also [accidentally mess up a
    flip](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197284228)
    and cues can't currently be shifted; add [confirmation dialog
    similar to when deleting a track in a
    playlist](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197283721)
    to avoid breaking things -\> but then cue needs to be aware of the
    Macros it's used in
  - how relevant is editing afterwards, how can we facilitate it?
  - Serato Flip ["just
    works"](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197286852)
    - Flip is fixed after recording, not blocking any hotcues or any
    chance of breakage

### Name

"Macros" sounds like something to be triggered manually at any time -
the point of flips is that they usually happen automatically.

Suggestions: Spin, Routines, Twist, MicroFlow, Mow

"Routines" sounds nice, is
[descriptive](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197282607)
and
[well-received](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197421948)
- [we don't need to sell it
either](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197282525).  
It sounds a little bland though, and doesn't capture the whole idea of
using it to create non-destructive edits of a track. It also doesn't
blend well with other terms, such as "Routine Mode" (for recording a
routine).

### Discussion

  - Recording could be implemented using [data emitted from the engine
    on cue
    jumps](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197293806)
    (not a signal, realtime\!)
  - [Use developer window/shortcuts for debugging
    controls](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197532422),
    implement them first and then look at skins.
  - [Macros are bound to one track - beware of scope
    creep](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197984243)
  - [Should be usable from a controller - keep number of controls at
    minimum](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/197984726)
  - [Might activate actual loops - user can then disable
    it](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/198009610)
  - [Reuse recording
    controls](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Macros.2FSaved.20Hotcue.20Routines.2F.22Serato.20Flip.22/near/199476162)

## Timeline

CW 21: Establish Timeline, work on open PRs, initial survey &
discussion  
CW 22: Survey existing Serato Flip uses & collect input

**June**

CW 23: Work out details of the format  
CW 24: Start implementation of data structures, controls  
CW 25: Create recording infrastructure  
~~CW 26~~ (blocked)

Deliverable: Format specification with examples

**July**

CW 27: Design controls & integrate into a skin  
CW 28: Tie it all together  
CW 29: *Buffer*  
CW 30: *Buffer*

Deliverable: Implemented controls with mapping to a skin and controller,
working recording system

**August**

CW 31: Refine UX & Integrate into other Skins  
CW 32: Enable Import from Serato & explore possibilities for sharing  
CW 33: *Buffer*  
CW 34: *Buffer*

Deliverable: Integration with other tools (Serato Flip, Export/Import,
Edit Dialog, Auto DJ?)

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
  - sifted through reddit
    (<https://www.reddit.com/search?q=serato%20flip>) - summary for now
    in Notion
  - organized community call

### CW 24

  - document data format ideas
  - create & send out [survey](https://forms.gle/oUTHKUCQcczUZtHA8)
  - finish remaining open PRs

### CW 25

Mo:

  - Wiki Improvements
  - [Get more acquainted with
    code](https://github.com/search?q=author%3Axerus2000+user%3Amixxxdj+updated%3A2020-06-15)
  - Revisit [reddit
    post](https://www.reddit.com/r/DJs/comments/h8av2o/reimagining_serato_flip)
  - Start writing [project-related
    code](https://github.com/mixxxdj/mixxx/pull/2873)

Tu: Specify required controls & format in [Macros](Macros) page

We: Architecture discussion & add user stories

Thu:

Fr:

### CW 26

Mo:

Thu:

Fr:

### CW 27

Mo:

Tu:

We:

Thu:

Fr:
