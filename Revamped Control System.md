## Summary

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

Mixxx's ControlObject system is lacking a few desirable features and is
not as fast as it could be. This project will build a new Control system
for thread-safe value communication across the Mixxx codebase.

## Use Cases

  - Thread safe communication of basic value types (string, boolean,
    double, integer, etc)
  - Unified method for changing and retrieving system parameters across
    different Mixxx subsystems (MIDI, GUI, Script, OSC, etc)
  - Unified namespace for referring to control values across Mixxx 
  - Triggering on changes to control values
  - Enumeration and logging of Control values for, e.g. crash recovery,
    debugging, 

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
system. There are ControlObjects, and ControlObject proxies.
ControlObjects, which guard a double variable, supports two main
methods: set() and get(). The double value in the ControlObject is not
guarded by a lock at all. The intent is that each value that is in the
control system has an 'owner'. The owner is the section of code that
initially created the ControlObject. The owner of the ControlObject is
the only code which is allowed to use the raw ControlObject itself. This
allows raw (i.e. high-speed) access to the control variable. A
ControlObject proxy, (e.g. ControlObjectThread and
ControlObjectThreadMain) represents a non-owner section of the code
which wishes to be retrieve the control value, change the control value,
and be updated of changes to the control value. The ControlObject and
its proxies operate asynchronously. Periodically, there is a
synchronization step which occurs. All updates to the control object and
all updates to the proxy are queued and during the synchronization step,
all the latest value of the control object is broadcasted to each proxy,
and the changes from the proxy are set on the ControlObject. This
synchronization step is currently run at the beginning of the audio
callback. The idea is that this is a time when no engine code can
possibly be running. However, there is nothing preventing ControlObjects
in other sections of Mixxx from being vulnerable to race conditions. The
reason this is not a problem in practice is that ControlObject's are
primarily created within the engine. In the future, this may not remain
true as more and more features are added to Mixxx.

### Implementation Performance

There are bottlenecks with the implementation of this system. The
synchronization step is facilitated by three static queues, each with
its own corresponding lock. The ControlObject set/get methods and the
ControlObject proxy set/get methods all must use these static queues.
This means that this system is actually far less performant then it
claims to be. What it does achieve is that errant ControlObject proxies
cannot cause lock contention on an engine ControlObject until the
synchronization phase. Errant ControlObject code can cause Mixxx-wide
contention for set/get operations on every ControlObject since the lock
is static.

### Overview of ControlObject Proxies

ControlObjectThread, ControlObjectThreadMain, ControlObjectThreadWidget
are three different types of ControlObject proxies which can be used.
ControlObjectThread uses locks for mutual exclusion when receiving
updates from its corresponding ControlObject. ControlObjectThreadMain
assumes that the only code which will be calling its methods is running
in the Qt GUI thread. In order to ensure mutual exclusion,
ControlObjectThreadMain uses the Qt event loop to deliver updates from
the ControlObject. This allows it to forego the use of locks.
Unfortunately, the implementation does not include a set/get that
doesn't use locks, so there is no real performance increase.
ControlObjectThreadWidget is a ControlObjectThreadMain that is used to
bind Mixxx widgets to ControlObject proxies. ControlObjectThread can be
used in any context, while ControlObjectThreadMain can only be used when
it will only be used by code running from the GUI thread.

## Design Questions

### Two-Tier System or Unified System?

The two-tier system that is currently in Mixxx causes developer
confusion. What kind of proxy should be used? When should a
ControlObject be used versus a proxy? The benefit of the system is that
it can reduce lock contention on the true ControlObject. If some
QtScript was written that continuously set the rate of a player, then it
is possible that the engine thread would have to stall to wait for the
lock when calculating the rate in the engine thread.

A unified system uses locks for every operation, and has no concept of a
proxy. The cost of every operation is the cost of a single, non-static
lock. A unified system would actually cost less in terms of performance
than the existing control system, because every operation results in an
object lock instead of a static lock. Switching to a unified system
would actually result in a performance boost. The choice of whether to
implement a two-tier system is simply to reduce lock contention on the
Control from potentially buggy proxy users.

### Supported control types

The current ControlObject system only supports doubles. There has been
recent demand for a wider range of types. The ability to store a string
in a Control is the most useful of the type additions. If the new
Control system will support a variety of types, then those that would be
most useful to Mixxx would be boolean, integer, double, and string. In
an ideal system, these types would be supported via C++ template
metaprogramming. Unfortunately, QObjects are incompatible with
templates, so this is not an option.

### Support type constraints

The current ControlObject class has a number of subclasses,
ControlPotmeter, ControlLogPotmeter, etc., which determine the semantic
behavior of the control and the range of values that are acceptable for
the control. This is a desirable feature for a control system. A new
system must support the validation of set()'s against a series of
constraints which are determined by the type of the control.

### Keep or Replace ConfigKey?

All ControlObjects are currently referred to by their key, a ConfigKey.
This system allows each Control to be named by two strings: group and
item. The group is effectively the control's namespace. In the engine,
for example, all controls related to the first player have the group
\[Channel1\]. Each control for the second player has the group
\[Channel2\]. This does not allow more granular grouping in a natural
way. If the ConfigKey were more like a filesystem path, then grouping
could be arbitrarily deep. This might not be useful at all, but it might
allow something like this: Select all controls with the namespace
\[Channel1\] will return all controls with the namespace Channel1, while
selecting with the namespace \[Channel1,FX\] will return a subset of
those controls which are also in the FX sub-namespace of Channel1. This
would be useful for something like a Control inspector that lets you
look at a table of all control values in Mixxx and select based on
namespace.

If anything, ConfigKey is really crufty and it would be nice if we could
rename it to something nicer and more relevant.

## Proposed Design

### QVariant Based, Unified Control System

This system would be a unified control system. There would be a single
Control class, and derivatives of it (e.g. ControlPushButton,
ControlTTRotary, ControlLogPotmeter, like in the Mixxx codebase today)
but there would be no such thing as a control proxy. All updates to
Controls happen across Mixxx immediately.

QVariant is a Qt built in type for storing a variety of data types. The
main benefit of using QVariant as the data type for the control system
is that we will automatically be able to support a wide variety of data
types in controls, including things like QByteArray, which could be very
useful. It supports all of the desired types listed above and more. A
list can be found in the QVariant Qt documentation. To sidestep the
annoyance of working with 'boxed' values, subclasses of Control could be
provided that implement methods with the actual type. For example --
ControlValue could be a subclass of Control which provides get/set
methods for double, including add/sub methods that are currently
provided on ControlObjects. ControlBoolean ControlInteger, and
ControlString could be similar.

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

## Team
