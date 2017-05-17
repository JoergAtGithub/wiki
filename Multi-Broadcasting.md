# Multi-broadcasting

by Stéphane Lepin

**Current State**: project technical planning

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

  - Engine changes for Broadcasting Profiles
  - Fixed fields:

<!-- end list -->

``` 
    * Server type
    * Server hostname
    * Server port
    * Username (used only for types Icecast and Shoutcast V2)
    * Password
    * Mountpoint (used only for types Icecast and Shoutcast V2)
* Implement a new class BroadcastProfile
* The BroadcastProfile class can be passed to an ShoutOutput instance
* The settings code must be updated to accomodate broadcasting profiles
```

  - Engine changes for Multiple Outputs
  - The EngineBroadcast sidechain filter must be modified to only act as
    a "broadcast manager" : receive audio samples and push them to the
    output instances
  - The current libshout logic implemented in EngineBroadcast must be
    moved to a new class ShoutOutput

<!-- end list -->

``` 
    * Class methods:
      * Set broadcasting profiles  
      * Start output
      * Stop output
      * Push uncompressed audio frame to output
* The settings code must be updated to handle several outputs
```

  - UI
  - *TODO* 

*TODO: UML diagram*

<span class="underline">Possible evolution</span>: make the broadcasting
code more generic and not specific to libshout.

## Weekly schedule

*Will be written once the technical specifications are complete*

## Useful info about the student's schedule

  - School project from May 18th to 26th
  - Another school project from June 22th to June 30th
  - School Year end: July 12th 2017
