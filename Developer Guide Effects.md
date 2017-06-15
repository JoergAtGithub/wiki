# Introduction to the Mixxx Effects Framework

Mixxx has a modular effects system to allow the user to creatively
customize the audio produced by Mixxx's engine.

The system aims to accomplish the following:

  - Support the use of audio effects from multiple effect providers /
    backends.
  - Provide an efficient and flexible way for the user to combine
    different effects into new creations and easily share them with
    others.
  - Provide a standard interface for controlling effects that the Mixxx
    GUI and DJ controllers can target.

## Effect Backends

Mixxx aims to support both user-loaded effect plugins (e.g. LV2, VST,
etc.) and "internal" or bundled effects.

An "effect backend" is an abstraction that allows us to support multiple
sources of effects that Mixxx can make use of.

The interface is defined here:
[EffectsBackend](https://github.com/mixxxdj/mixxx/blob/master/src/effects/effectsbackend.h).

It's fairly simple. If you stand back and squint, a backend must support
a method to get a list of available effects, and a method that
instantiates one of those effects.

Today, we only have the "native" backend, which is for built-in effects.
These effects can make strong assumptions about Mixxx since they are
built-in.

We aim to support effect plugins. Work on an LV2 backend is in progress.
Effect plugins cannot make the same assumptions, and therefore may feel
less integrated with Mixxx or less efficient.

## The Native Backend

Mixxx has a suite of core effects implemented in the "native" effects
backend. The code for these effects are a set of nice examples of how to
write an effect.

Check out the code:
[src/effects/native](https://github.com/mixxxdj/mixxx/tree/master/src/effects/native)

## Effect Manifests

Regardless of which backend an effect came from, Mixxx needs to know
various metadata about the effect to make use of it -- for example:

  - a unique ID we an refer to it by internally
  - A name.
  - The effect's author.
  - A description of its functionality.
  - A list of all the parameters the effect supports and their types /
    ranges.

The standard way we represent this information is via a "manifest".

Check out the code:
[EffectManifest](https://github.com/mixxxdj/mixxx/blob/master/src/effects/effectmanifest.h).

## Effect Racks and Effect Chains

### The Main Effect Rack

### The Equalizer Rack

### The Quick Effects Rack

## The Interface with the rest of Mixxx: Effect Units and Effect Slots

### The Control Interface

See also:

  - [Introduction to Mixxx's Control System](developer_guide_control)
  - [Main Effect Rack Controls](mixxxcontrols#effects_framework)
  - [Equalizer Rack / QuickEffect Rack
    Controls](mixxxcontrols#eqs_and_filters)

### GUI Widgets
