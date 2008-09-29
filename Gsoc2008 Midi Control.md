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

### About Tom

You can contact Tom or read about him at this page:
<http://soc.corrodedreality.org/>

### Merge to Trunk and Beyond... clean up work

**Bold** must be completed before merge...

  - \*\*Need a working "Add Control", minimal - just add an empty row
    \*\*, nice-to-have some kind of list of available bindings which can
    be added i.e. "\[Channel1\] Play", "\[Master\] Crossfader", etc
  - **Fix Linux crash on midi learn caused by "emit(midiEvent(new
    ConfigValueMidi(type,control,channel), device));" \~ 165 of
    src/midiobject.cpp**
  - Two different controllers in one mapping doesn't work (1 overwrites
    the other's config object), this should be fixed or at least a
    warning should be added.
  - Write numbers in mapping files as hex values like old mapping format
    (to help make for cut-and-paste transition of mappings)
  - Hide unused buttons:

<!-- end list -->

``` 
    * Load/Import Default Bindings
    * Group Learn Selected
    * Set Advanced Options...
    * Change MIDI Binding...  
* Fix Remove to support removing multiple bindings at once... refer to note at bottom of void DlgPrefMidiBindings::slotRemoveBinding() in src/dlgprefmidibindings.cpp ~ #352
```

### Project Status

**Current status of the project:**

\* Week 1: ~~Forming basic use cases~~, general brainstorming, preparing
ideas for community feedback, reading existing MIDI code.

\* Week 2: ~~UML proposal, class design, XML format proposal.~~
**NOTE:** I am away from Wednesday the 4th-Monday the 9th, attending
Rock am Ring in Germany. I can only be contacted by phone during this
time.

\* Week 3: (Unplanned) Move back to Australia and recover from jetlag.

\* Week 4: GUI Design, write class structure, begin XML changes, ~~try
to get MIDI device dialog working~~, ~~look at proposed MIDI patches~~.

\* Week 5: Add working GUI Elements (a little unproductive this week due
to moving house and having no internet whilst getting stuck on a stupid
bug. Thanks Garth for finding it\! :))

\* Week 6: ~~Fix GUI on Mac, Get devices showing up~~,
~~Investigate/Change MIDI Device data storage~~, Work on
dlgprefmididevice

\* Week 7: Work on dlgprefmidibindings, Work on dlgprefmididevice

\* Week 8: ~~Complete Google Midterm Evaluations
[Student](http://groups.google.com/group/google-summer-of-code-announce/web/student-survey-questions)
|
[Mentor](http://groups.google.com/group/google-summer-of-code-announce/web/midterm-mentor-survey-questions),
midibindings: implement table 'feel' in gui, mididevice: preset
detection~~

\* (Week 9) Start a TODO list of things that need to be implemented to
target an early August (week 12 or 13) community test release, Single
MIDI learn, Group MIDI Learn, dlgprefmidibindings small dialogs

\* (Week 10) Multiple device support (delays due to IRL stuff / bindings
dialog problems)

\* (Week 11) Multiple device support, Bindings Dialog fixes, Testing

\* (Week 12) Code cleanup, testing

Now: fixing up loose ends, testing, code cleanup, documentation.

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

**Description:** The user wishes to add a binding for a single MIDI
control.

1.  The user opens the MIDI Bindings dialog.
2.  The user selects 'Add new binding'.
3.  The user selects which aspect of the program they would like to bind
    to the control.

<!-- end list -->

  - Albert's suggestion: Have a table with detailed info on the control.
    This will reduce ambiguity and help advanced users.

<!-- end list -->

1.  The user uses their desired MIDI Control, and the program provides
    visual feedback that it has detected the control.
2.  The user enters in additional information, such as parameters, a
    custom name, and the control type.
3.  The user saves the binding and it works instantly.

**Name:** Change MIDI Binding by Single Learn

**Description:** The user wishes to change an existing binding using
learning.

1.  The user opens the MIDI Bindings dialog.
2.  The user selects the binding they wish to change.
3.  The user selects 'Change existing binding(s)'.

<!-- end list -->

  - What about a MIDI learn toggle button, Traktor style? Would this
    make more sense? This could be a different style of behaviour that
    could work in unison with the group learn style.

<!-- end list -->

1.  The dialog provides visual feedback that the current control is
    ready to be changed. (Fluro highlighting\!?)
2.  The user uses their desired MIDI Control, and the program provides
    visual feedback that it has detected the control.
3.  The user saves the binding and it works instantly.

**Name:** Change MIDI Binding by Group Learn

**Description:** The user wishes to change a group of existing bindings
sequentially using learning.

1.  The user opens the MIDI Bindings dialog.
2.  The user selects several bindings they wish to change at one time.
3.  The user selects 'Change existing binding(s)'.
4.  The dialog provides visual feedback that the current control is
    ready to be changed. (Fluro highlighting\!?)
5.  The user uses their desired MIDI Control, and the program provides
    visual feedback that it has detected the control.
6.  Steps 4-5 are repeated for every control selected, unless the user
    cancels (using the same button that started it)?
7.  The user saves the binding and it works instantly.

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

**Name:** Set up new MIDI controller for the first time

**Description:** User starts Mixxx with a new MIDI controller never
previously used (thanks G\!)

1.  The user first plugs in the new midi device and starts Mixxx.
2.  Dialog: New MIDI device found, would you like to set it up now?
3.  User's device training mapping is populated with default values from
    the midi mapping files that ship with Mixxx
4.  User is invited to return to the training config screen to retrain /
    adjust control behavior of the device
5.  Option to restore defaults for current device (user warned to save
    existing configuration)

<!-- end list -->

``` 
   * G's original suggestion: Separate checkbox + warning to disable user configured training / use defaults only (<- not sure about this)
```

### UML Diagrams

[[/media/mixxx_midi_system.jpg|]]

(needs to be updated) [[/media/class_diagram1.jpg|]]

### New Dialog Changes

Forms:

  - MIDI Device Selection
  - DlgMidiDevice
  - [[/media/midi-device-dialog-draft.jpg|]]
  - A list of MIDI devices
  - Status of each MIDI device: Active? Enabled? Send? Receive? Working
    correctly?

<!-- end list -->

``` 
    * Enabled: Probably better to let the user choose enabled for midi in and out only rather than having a redundant device enable option. If they don't want the device to be used, they can disable both midi in and out...
* Detect new MIDI devices
* Example Table
    * {{:mididevicedlg.png|}}
* MIDI Bindings
* DlgMidiBindings
* {{:midi-bindings-dialog-draft.jpg|}}
* Table of bindings
    * Friendly name (eg. Channel 1 pitch fader)
    * Control name
    * MIDI Assignment
      * Channel, key, or pitch bend
    * MIDI Device
    * Example Table
      * {{:midibindingdlg.png|}}
      * Too big! Shrinkage required.
* Import, export
* Add binding/change binding 'wizard' buttons
* Group learn
* Single learn
* Sandbox Mode?
    * When adjusting MIDI settings in the dialog, will the program be affected? Or will the MIDI window stop all events going to the program?
    * Maybe an option (checkbox) for this? "Block MIDI messages going to the program while preferences are open"
    * Make it block MIDI messages only when the MIDI prefs pane is open. If that's too much work, then just make it block MIDI messages while whole prefs dialog is open.  --- //[[albert@santoni.ca|Albert Santoni]] 2008/06/01 23:12//
```

### MIDI XML Format Changes

  - Header (Program name, version)
  - Comments (about the controller, links to specs, etc)
  - Nicer control (key) names, more human readable
  - (new 3/7) Device names for the preset detection
  - Proposal: <http://soc.corrodedreality.org/newmidi.txt> (23/7 needs
    to be updated)

### TODO

  - Current Priorities
  - Functionality

<!-- end list -->

``` 
    * Finish the two dialogs (code)
    * Get to a working state where presets can loaded/saved/etc easily
    * Multiple device support
    * Cosmetic changes
    * Prepare for community release
    * Documentation!
    * Prepare for 1.6.1 code merge
* Testing
    * Everything!
    * From different points of view: SVN update, fresh install, end user upgrade...
    * Bugfixes
* Design (most likely post-GSoC)
    * Refactoring
    * Overhaul of MIDI structures
    * Performance analysis
* The Future
    * What is needed next?
```

``` 
    * Generalised support for weird, non-midi devices eg mouse/kb/custom controllers, design review
* Address bug 234923: https://bugs.launchpad.net/mixxx/+bug/234923
* LADSPA
* Implementation
* Sandbox mode
* Classes needing changing/updating:
    * ConfigMIDI
      * Currently, MIDI values here are stored in a string. I would like a nicer OO approach to this.
      * Class has to be updated to the new control type system. Generalised OO approach would be nicer than a whole bunch of ifelse's.
      * Not a priority - probably post-gsoc.
    * MIDI_____
      * Why is the receive function called send, when we have functions to send called send____? Very confusing when first reading the code!
        * Propose we change this to recieve...
      * Refactoring - not a priority at the moment
    * DlgPrefsMIDIDevice
      * Device names (currently broken, waiting on multiple device support)
      * Detect preset by keywords
    * DlgPrefsMIDIBindings
      * Helper functions (outlined in the cpp in svn)
      * Idea: row highlighting for non-active bindings due to device unavailable/disabled
      * Options currently broken
      * Lights
      * Hercules etc
    * New device detection: implementation and design required
      * Probably in the device dialog.
    * ConfigKeys: if they need square brackets to work in a configobject, why isnt this enforced or done automatically?
* MIDI Option overhaul
* Change ConfigObjectMIDI
     * Multiple Option Support
     * String of options, use contains()
     * Implement controller types
     * Use class structure
```
