# Multi-broadcasting

by Stéphane Lepin

**Current State**: Community bonding period

## Introduction

This project for Mixxx aims to implement several features potentially
useful for users willing to broadcast live with Mixxx in simple and more
advanced ways.

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

## Implementation details

This project will be implemented in two parts, each leading to a working
result : the broadcasting profiles first, and then the multiple
broadcasting outputs.

### Broadcasting profiles (part one)

The broadcast profile selection will be integrated under the “Live
Broadcasting” section of Mixxx’s preferences as a dropdown list, with
three buttons (or a dropdown menu) at its right to create, delete and
rename the currently selected profile, integrated within the existing
GUI of the panel and reusing its widgets. A newly created profile will
have default values.

[[/media/wiki/broadcasting_profiles.png|]]

### Multiple broadcasting outputs (part two)

The new “Live Broadcasting” settings panel will consist of a list of
broadcasting outputs. The existing GUI for Live Broadcasting settings is
to be moved to a dedicated dialog, which will be spawned when the user
clicks on “Edit” next to an item of the outputs list.

Under the hood, the EngineBroadcast class will be adapted to be an
individually-instanciable class for each broadcasting output. This class
already has comprehensive streaming protocols support. Multithreading of
the outputs (one thread per output) may be implemented.

[[/media/wiki/multi-broadcasting.png|]]
