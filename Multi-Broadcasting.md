# Multi-broadcasting

by Stéphane Lepin

**Current State**: project technical planning

## Useful info about the student

  - School project from May 18th to 26th
  - Another school project from June 22th to June 30th
  - School Year end: July 12th 2017

## Project description

This project for Mixxx aims to add several features potentially useful
for users willing to broadcast live with Mixxx. Two new features will be
implemented : broadcasting profiles and multiple broadcasting outputs.

### Broadcasting profiles

The broadcast profile selection will be integrated under the “Live
Broadcasting” section of Mixxx’s preferences as a dropdown list, with
three buttons (or a dropdown menu) at its right to create, delete and
rename the currently selected profile, integrated within the existing
GUI of the panel and reusing its widgets. A newly created profile will
have default values.

[[/media/wiki/broadcasting_profiles.png|]]

### Multiple broadcasting outputs

The new “Live Broadcasting” settings panel will consist of a list of
broadcasting outputs. The existing GUI for Live Broadcasting settings is
to be moved to a dedicated dialog, which will be spawned when the user
clicks on “Edit” next to an item of the outputs list.

[[/media/wiki/multi-broadcasting.png|]]

## Ideas

  - Drop-down item in the menu bar to start/stop streaming to one or all
    outputs

## Technical details

  - The EngineBroadcast must be modified to only act as a "broadcast
    manager" : receive audio samples and push them to the output
    instances
  - The broadcasting code must be separated from EngineBroadcast. An
    IBroadcastOutput interface for outputs is to be defined so that
    several types of outputs can be implemented.
  - Interface methods:

<!-- end list -->

``` 
    * (static) Get output properties (used by the UI)
    * Set output settings (based on the properties)  
    * Start output
    * Stop output
    * Push uncompressed audio frame to output
* The current libshout logic implemented in EngineBroadcast will be moved to a class ("ShoutOutput") implementing IBroadcastOutput 
```

*TODO: UML diagram*

## Project deliverables

### Community bonding period (May 4 - May 30) :

  - Getting familiar with Mixxx’s codebase and community
  - Fixing “starter issues” and general issues referenced in the issue
    tracker
  - Providing support to users on the project communication channels

### Phase 1 (May 31 - June 30) :

Implement broadcasting profiles (quickly-loadable presets of streaming
server credentials and connection information) and their accompanying UI
operations (create, delete, rename, select)

### Phase 2 and Final Phase (July 1st - August 21) :

Implement the ability to broadcast to several outputs (streaming
servers) simultaneously, within the range of Mixxx’s currently supported
protocols

### Final week (August 22 - August 29) :

Polishing and bug hunting
