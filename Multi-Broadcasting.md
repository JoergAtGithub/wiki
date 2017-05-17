# Multi-broadcasting

by Stéphane Lepin

**Current State**: project technical planning

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

#### Technical details

  - Design and write a new BroadcastProfile class
  - Fixed fields/attributes: server info/credentials and encoding
    settings
  - The Settings UI must be updated to add control over and use of
    broadcasting profiles
  - The settings code must be updated to accomodate broadcasting
    profiles

### Multiple broadcasting outputs (phase 2)

The new “Live Broadcasting” settings panel will consist of a list of
broadcasting outputs. The existing GUI for Live Broadcasting settings is
to be moved to a dedicated dialog, which will be spawned when the user
clicks on “Edit” next to an item of the outputs list.

#### Technical details

  - The EngineBroadcast sidechain filter must be modified to only act as
    a "broadcast manager" : receive audio samples and push them to the
    output instances
  - The current libshout logic must be separated from EngineBroadcast
    and moved to a new class ShoutOutput
  - Class methods:

<!-- end list -->

``` 
    * Set broadcasting profile (instance of BroadcastProfile)
    * Start output
    * Stop output
    * Push uncompressed audio frame to output (encode in a separate thread?)
* The settings code must be updated to handle several outputs
* A new Live Broadcasting settings UI must be implemented (see UI draft below)
* The existing Live Broadcasting settings UI must be moved to an instanciable dialog spawned by an item's button in the new Outputs list UI.
```

<span class="underline">Possible evolution</span>: make the broadcasting
code more generic and not specific to libshout.

### UI drafts

[[/media/wiki/multi-broadcasting.png|]]

### Ideas

  - Drop-down item in the menu bar to start/stop streaming of one or all
    outputs

### Weekly schedule

*Will be written once the technical specifications are complete*

### Useful info about the student's schedule

  - School project from May 18th to 26th
  - Another school project from June 22th to June 30th
  - School Year end: July 12th 2017
