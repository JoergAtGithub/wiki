# Configurable Cue Behaviour

## Summary and Rationale

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

**CDJ Mode**

When stopped, pressing CUE sets the cue point. When playing, pressing
CUE jumps to the cue point and stops there. Holding down CUE plays from
the cue point for as long as it's held, then when released it jumps
straight back to cue point and stops there.

**Simple Mode**

??? (Should this be what we already have coded in Mixxx?) --- *[Albert
Santoni](albert@santoni.ca) 2008/02/21 18:35*

Each mode will be selectable via the Preferences dialog (which pane? -
Albert). The dialog should explain what each behaviour does (as in the
explanation above), so users don't have to dig through documentation.

The default mode will be CDJ.

Both modes must be supported when using MIDI hardware and the Hercules.
In order to facilitate this, we probably need to create a new
ControlObject like "cue\_generic", whose behaviour gets changed
depending on what's selected in the prefs.

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

    1. Configurable Cue Behaviour
      1.1 Modify Preferences dialog
      1.2 Modify engine ???

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - Albert Santoni
