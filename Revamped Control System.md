## Summary and Rationale

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

Mixxx's ControlObject system is lacking a few desirable features. This
project will build a new Control system for thread-safe value
communication across the Mixxx codebase. The new control system will run
alongside the old system as is it slowly phased out.

## Use Cases

  - Thread safe communication of basic value types (string, boolean,
    double, integer, etc)
  - Unified method for changing and retrieving system parameters across
    different Mixxx subsystems (MIDI, GUI, Script, OSC, etc)
  - Unified namespace for referring to control values across Mixxx 
  - Triggering on changes to control values

## Motivation and Design Issues

When designing pieces of Mixxx, every value that needs to be shared
across threads must be guarded by locks in order to prevent race
conditions that can lead to invalid data, nasty race conditions, and
mysterious segfaults. Mixxx receives contributions from developers
around the world, many of which do not have the time to invest in fully
understanding the Mixxx codebase, including which thread runs in which
context. For any given piece of code, a new developer may not be able to
easily determine the threading model, and which threads run in which
sections of code. Furthermore, if a given value in the Mixxx code needs
to be shared across threads, the most common pattern for making it
thread-safe is to make a per-variable lock, and guarding every use of
the variable with the lock.

A Control system resolves these two issues by automatically protecting
every use of a variable with a lock, and providing a 'worry-free'
approach to thread safety where the contributor does not have to worry
about the thread safety of their code as long as their values are in the
Control system.

There are two competing interests while designing a thread safe value
communication system: thread safety and performance. The problem with
the above approach is that if every reference to a value is guarded by a
lock, then there can be a significant performance impact if every
variable in the code is protected in this manner.

## The Existing Control System

The original Mixxx control system, the ControlObject system, balances
the above concerns with a hybrid approach. This amounts to a two-tier
system. There are ControlObjects, and ControlObjectThreads.
ControlObjects, which guard a double variable, supports two main
methods: set() and get(). The double value in the ControlObject is not
guarded by a lock at all.

#### Internal Changes

#### Architectural Issues

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

## Team
