# Configurable Cue Behaviour

## Summary and Rationale

**Status**: This specification is in the **planning and design** stage,
and edits are welcome.

Add support for two switchable cue behaviours. Many users are familiar
with a particular cue behaviour, and it would make it easier for users
to transition to Mixxx if they configure the cue button to work they way
they expect it.

## Use Cases

  - DJ Bill is considering switching from CDJs to software. He doesn't
    like Mixxx's cue behaviour because it is different from what he's
    used to using.
  - DJ Paul uses the cue button for quickly jumping to a spot and
    stopping. He would like the ability to jump to a cue point and stop
    without having to hit multiple buttons and seeking.

## Design

#### CDJ Mode

  - When stopped, pressing CUE sets the cue point.
  - When playing, pressing CUE jumps to the cue point and stops there.
  - Holding down CUE plays from the cue point for as long as it's held,
    then when released it jumps straight back to cue point and stops
    there.
  - Have the ability to have it continue playing if cue is held down for
    a while/play is pressed at the same time/something like that? ---
    *Robin*
  - Yeah, making it just play if you held down cue for more than 3
    seconds or something might be cool. We could probably hack that into
    EngineBufferCue without too much trouble. -- *Albert*
  - Current CDJs do this if play is pressed while cue is being held
    down, and that makes more sense than it happening automatically or
    after some time period imo. Principle of Least Surprise: Software
    should do what DJ tells it to, not try to be helpful :) -- *Ben*

#### Simple Mode

  - ???
  - (Should this be what we already have coded in Mixxx?) --- *Albert*

#### Preferences Dialog

Each mode will be selectable via the Preferences dialog (which pane? -
Albert). The dialog should explain what each behaviour does (as in the
explanation above), so users don't have to dig through documentation.

The default mode will be CDJ.

#### Internal Changes

Both modes must be supported when using MIDI hardware and the Hercules.
In order to facilitate this, we probably need to create a new
ControlObject like "cue\_generic", whose behaviour gets changed
depending on what's selected in the prefs. It looks like the cueing code
is already nicely abstracted in a file called EngineBufferCue.cpp, with
slots that get called when existing controls like "cue\_simple" get
fired. Each slot takes a parameter of type "double", which hopefully
indicates whether it was a button up/down event. If it doesn't, then
we'll have to look into adding that.

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

    1. Configurable Cue Behaviour
      1.1 Modify Preferences dialog
      1.2 Modify EngineBufferCue
        1.2.1 Implement basic slotControlCueCDJ/CDJ behaviour
        1.2.2 [Implement the link between the preferences and EngineBufferCue - need to figure this out first]
        1.2.3 Implement slotControlCueProxy (?) that calls the correct slot (simple, CDJ) based on the prefs
        1.2.4 Implement "play after 3 seconds" behaviour in slotControlCueCDJ
        1.2.5 Refactor slotControlCueSimple, if necessary

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - Albert Santoni
  - Robin Sheat
