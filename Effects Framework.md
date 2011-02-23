## Summary

**Status**: This specification is **in drafting**. Please feel free to
edit this page.

DJs often augment their mixes with effects. Mixxx is severely lacking in
this department, as released versions of Mixxx only offer EQs and a
flanger.

This project aims to bring effects to Mixxx, both via native effects and
effects plugins via LADSPA, LV2, or VST.

## Requirements

  - Backend
  - Support for multiple backends
  - A general plugin interface which allows each plugin to express:

<!-- end list -->

``` 
    * The plugin name
    * A description of the plugin
    * The parameters each plugin has, including:
      * An internal identifier
      * A human-readable name
      * A prose description, with support for internationalization, suitable for display in a tooltip
      * Units and ranges of the parameter
    * A preferred ordering of parameters in order of importance
* A reference implementation of a backend implementing LADSPA support
* A reference implementation of a Mixxx-internal effects backend
    * Support for at least a flanger
* Effects / Engine Interface
* Effects Slots per-EngineChannel
* A Plugin provided by an EffectsBackend can be allocated to a slot
```

## Design

The effects system will implement a backend architecture similar to
Mixxx's MIDI backend. Multiple backends will provide plugins that are
discovered by a central EffectsManager class by invoking the plugin
Enumerator for each backend.

## Work Breakdown

## Current Progress

This feature has been attempted twice by two GSoC students. There is a
lot of old code lying around, and we will try to reuse whenever
possible. The current branch for work on this feature is the
[lp:\~mixxxdevelopers/mixxx/features\_effects](https://code.launchpad.net/~mixxxdevelopers/mixxx/features_effects)
branch.

## Team

  - RJ Ryan
