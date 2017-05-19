# Multi-broadcasting

by Stéphane Lepin

**Current State**: phase 1 planning

### Project description

This project for Mixxx aims to add several features potentially useful
for users willing to broadcast live with Mixxx. Two new features will be
implemented : broadcasting profiles and multiple broadcasting outputs.
These features will be implemented in two parts, matching the GSoC
phases schedule.

### Broadcasting profiles (phase 1)

Broadcasting profiles allow management of several sets of server
settings/credentials and encoder settings. These can be managed through
a dedicated dialog in Mixxx's settings or a new settings panel. Profiles
have the standard Icecast/Shoutcast and encoder settings currently
available in the Live Broadcasting panel.

[[/media/wiki/broadcasting_profiles.png|]]

#### Technical details

  - Changes will be made in majority in the settings engine and UI.
  - Design and write a new BroadcastProfile class
  - Fixed fields/attributes: server info/credentials and encoding
    settings
  - The Settings UI must be updated to add control over and use of
    broadcasting profiles
  - Add a combo list of profiles
  - Selecting a profile loads its settings in the fields of the Live
    Broadcasting panel
  - Saving settings applies the current values to the currently selected
    profile
  - Add buttons to create, delete and rename profiles
  - The current profile can't be changed or edited while streaming is
    running
  - The settings code must be updated to accomodate broadcasting
    profiles

### Multiple broadcasting outputs (phase 2)

The new “Live Broadcasting” settings panel will consist of a list of
broadcasting outputs. The existing GUI for Live Broadcasting settings is
to be moved to a dedicated dialog, which will be spawned when the user
clicks on “Edit” next to an item of the outputs list.

[[/media/wiki/multi-broadcasting.png|]]

#### Technical details

  - The EngineBroadcast sidechain filter must be modified to only act as
    a "broadcast manager" : receive audio samples and push them to the
    output instances
  - The current libshout logic must be separated from EngineBroadcast
    and moved to a new class ShoutOutput (with QThread inheritance)
  - Class methods:

<!-- end list -->

``` 
    * Set broadcasting profile (instance of BroadcastProfile)
    * Start output (overrides QThread::run)
    * Stop output
    * Slot: Push uncompressed audio samples to output
* Each instance should have its own thread(s)
* The settings code must be updated to handle several outputs
* A new Live Broadcasting settings UI must be implemented (see UI mockup above)
* The existing Live Broadcasting settings UI must be moved to an instanciable dialog spawned by an item's "Edit" button in the new Outputs list UI.
```

<span class="underline">Possible evolution</span>: make the broadcasting
code more generic and not specific to libshout.

### Ideas

  - Drop-down item in the menu bar to start/stop streaming of one or all
    outputs

### Weekly schedule

*Work in progress*

#### Phase 1: Broadcasting profiles

##### May 30 - June 2nd

  - Implement the BroadcastProfile class
  - Adapt the settings code to be able to load/save profiles

##### June 5 - June 9

  - Edit the Live Broadcasting UI panel to add the profile widgets
    (combo list + buttons)
  - Write the logic of these widgets and link them with the engine

##### June 12 - June 16

  - Testing and bug hunting

##### June 19 - June 23

  - **First milestone: have this feature mergeable**
  - Project planning for Phase 2

#### Phase 2: Multi-broadcasting

To be defined.

### Useful info about the student's schedule

  - School project from May 18th to 26th
  - Another school project from June 22th to June 30th
  - School Year end: July 12th 2017
