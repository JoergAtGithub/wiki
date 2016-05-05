## Summary

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

This project aims to refactor Mixxx's initialization process to decrease
coupling between Mixxx's components, specifically to disentangle the
bootup process with our QtGui based UI (MixxxMainWindow).

## Use Cases

This is an infrastructure project with no user visible impact. The main
use cases are developer oriented.

The benefits to developers are:

  - Easier maintenance of Mixxx's subsystems.
  - Easier support for prototyping of different UIs (e.g. Qt Quick-based
    UIs for iOS or Android)
  - Clearer module boundaries and a more understandable design.

## Design Overview

This design will reinforce the pre-existing Manager pattern within our
codebase. Every major feature within Mixxx has a manager class that is
in charge of keeping track of that feature's state.

For example:

  - ControllerManager
  - EffectsManager
  - RecordingManager
  - BroadcastManager
  - SoundManager
  - etc.

This helps enforce modularity. Services that depend on one-another
should interface via the public API of the manager classes. Not all
existing code follows this rule, but we aim to.

There is a proliferation of "hidden" dependencies between services in
Mixxx today. This happens via a variety of mechanisms:

  - State sharing and message passing via Controls or UserSettings.
  - Singleton classes.
  - Implicit assumptions about ordering of events.

Wherever possible, we should prefer explicit dependencies to implicit
dependencies. This makes it easier to reason about code because you can
see all of its dependencies plainly.

The Mixxx bootup process is an example of hidden dependencies and tight
coupling in action. If you change the ordering of any individual manager
creation or initialization (e.g. move deck creation or effect backend
registration) then problems quickly arise. Even though the code compiles
and everything seems fine, features break and in the worst case Mixxx
crashes at runtime. Not good\!

The lack of organization in the bootup process also leads to long delays
at startup. In Mixxx 2.0, this became so pronounced that we found it
necessary to introduce a splash screen so the user doesn't think the app
is just broken. Since everything in the bootup process is one long
serial list of steps to take, we can't show the UI to the user until
everything has initialized fully.

To disentangle this mess, we propose a significant refactoring based on
these principles:

1.  Mixxx bootup should be restricted to resource allocation only (e.g.
    running constructors). We should be able to show a UI immediately
    after bootup is complete (ideally in less than 1 second).
2.  Opening all resources (controllers, sound devices, library database,
    etc.) must wait until the UI has already been displayed -- and
    should happen in a different thread than the main GUI thread.
3.  Every manager must expose a public API that is the main entry point
    of requests to the service. To the extent possible, hidden
    dependencies will be eliminated and the public API will be used. 
4.  Each manager class will provide a public interface to save and
    restore state. Instead of implementing message passing via
    UserSettings, managers will instead provide public interfaces for
    setting all preference options. 

### Detailed Design

All managers will implement the following interface:

``` c++
// Manager life-cycle:
// - Manager is constructed.
// - Manager::initialize (once).
// - Manager::readPreferences (once).
// - Manager::onInterfaceCreated (one to many times).
// - Manager::onInterfaceDestroyed (one to many times).
// - Manager::savePreferences (one to many times).
// - Manager::finalize (once).
// - Manager is destroyed.
class Manager {
  public:
    // Perform lightweight initialization.
    // For example:
    // - Setting default states.
    // - Allocating resources. 
    // Called after Mixxx has booted but before the UI has been created. 
    // File I/O and other blocking operations should be avoided in this phase.
    virtual Status initialize() = 0;

    // The inverse of initialize. Perform lightweight shutdown.
    // For example:
    // - Free resources allocated in the initialize() step.
    virtual Status finalize() = 0;
    
    // Called when the user interface is created. 
    // Managers should initiate long-running tasks at this time -- for example:
    // - Starting a library scan.
    // - Connecting to audio devices or controllers.
    // These tasks should be started on a thread pool, NOT on the invoking thread.
    virtual void onInterfaceCreated() {}
    
    // Called when the user interface is destroyed and Mixxx is shutting down.
    // Managers should clean up persistent resources held here (file handles, devices, etc.) 
    // and join thread pools.
    virtual void onInterfaceDestroyed() {}
    
    // Save user preferences for this manager to pSettings.
    // Called when about to save user preferences to disk.
    void savePreferences(UserSettingsPointer pSettings) = 0;
    
    // Read user preferences for this manager from pSettings.
    // Called at startup when reading user preferences from disk.
    void readPreferences(UserSettingsPointer pSettings) = 0;
};
```
