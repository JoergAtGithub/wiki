# Implementing an improved MIDI control system into the Mixxx project (GSoC 2008 project)

  - Student: **Thomas Lachlan Care**
  - Mentor: **Garth Dahlstrom**

### Abstract from GSoC Application

I am an undergraduate Software Engineer who believes he can contribute
significantly to the Mixxx project on both a short term and long term
basis. I aim to implement a combination of major and minor features, as
well as paving the way to implement features beyond the Google SOC 2008.
The main feature I wish to improve is general MIDI support – a task well
suited to me, due to my personal hardware and experience with industry
DJ equipment as a performer. I also plan to implement small features as
a secondary objective, building on the well-designed feature set of
Mixxx. Most of these features come from my experience as a Trance DJ –
e.g. CDJ like interface, general customisability extensions (pitch
increments, for example), and jog dial sensitivity. My lack of
satisfaction with current DJ software and personal desire to experiment
with my hardware will result in me being a long-term contributor to this
project. I am a reliable person who is a pleasure to work with and I
hope I can benefit the project in any way possible.

### About this page

This page will be used during the GSoC 2008 to let the community know
the status of the project, in addition to getting feedback on aspects of
the project. Tom believes that community input is essential\!

**Current status of the project:** Forming basic use cases, general
brainstorming, preparing ideas for community feedback.

### About Tom

You can contact Tom or read about him at this page:
<http://soc.corrodedreality.org/>

### Project Overview

The basic goal of the project is to improve MIDI support in Mixxx. MIDI
in Mixxx should be:

  - Effortless to configure

<!-- end list -->

``` 
   * A MIDI learning system will mean that if a user can use the controller, they can use Mixxx!
   * Support for a range of common MIDI controls (knobs, faders, encoders, jog wheels, buttons, etc)
      * (idea) Support for learning non-standard controls, eg custom controls: a keyboard key as a button or trigger
   * A GUI for the learning system, as well as an easy way to see current bindings and import/export settings
      * MIDI message debug could be helpful here, eg for determining behaviour of a control
* Have support for common hardware 'out of the box'
   * Creation of intuitive profiles/presets for hardware
   * Clear indication of extent of support for hardware (comments in MIDI presets?)
* Be capable of supporting even the weirdest hardware combinations
   * Multiple MIDI controllers
   * Multiple ways of controlling a single function, eg transition to rotary faders should be seamless
* Reliable
   * MIDI response should always be predictable and usable
   * MIDI cannot stop working halfway through a performance!
* Maintainable
   * Code quality
   * Commenting
```

### Basic Use Cases

**Name:** MIDI Learn

**Description:** The user wishes to add a binding for a MIDI control.

1.  The user opens the MIDI Bindings dialog.
2.  The user selects 'Add new binding'.
3.  The user selects which aspect of the program they would like to bind
    to the control.
4.  The user uses their desired MIDI Control, and the program provides
    visual feedback that it has detected the control.
5.  The user enters in additional information, such as parameters, a
    custom name, and the control type.
6.  The user saves the binding and it works instantly.

**Name:** Change MIDI Binding by Learn

**Description:** The user wishes to change an existing binding using
learning.

1.  The user opens the MIDI Bindings dialog.
2.  The user selects the binding they wish to change.
3.  The user selects 'Change existing binding'.
4.  The user uses their desired MIDI Control, and the program provides
    visual feedback that it has detected the control.
5.  The user enters in additional information, such as parameters, a
    custom name, and the control type.
6.  The user saves the binding and it works instantly.

**Name:** Export MIDI Bindings to file

**Description:** The user wishes to export some or all of the bindings
to a reusable format.

1.  The user opens the MIDI Bindings dialog.
2.  The user selects the bindings they wish to export, perhaps with the
    help of 'Select/Deselect All' buttons and/or keyboard shortcuts.
3.  The user selects 'Export bindings to XML'.
4.  A file save dialog is displayed, and the user selects a destination
    path.
5.  The selected bindings are exported, exporting all of the bindings if
    none were originally selected.

**Name:** Import MIDI Bindings from file

**Description:** The user wishes to import a list of MIDI bindings.

1.  The user opens the MIDI Bindings dialog.
2.  The user selects 'Import bindings from XML'.
3.  A file open dialog is displayed, and the user selects a source path.
4.  A prompt appears asking if the user would like to merge or overwrite
    the existing bindings ('Yes/No/Cancel')
5.  The bindings are appropriately imported and the interface is
    updated.
