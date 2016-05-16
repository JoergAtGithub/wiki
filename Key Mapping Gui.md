# Key Mapping GUI

## Controller classes overview

#### Controller

Abstract class representing a controller. For each controller type
there's a subclass: **HidController**, **MidiController**... Jordi will
need to create a *KeyboardController* subclass.

#### ControllerDebug

This class is used to provide the *controllerDebug(String s)* macro.
This macro prints controller debug messages. It is only needed to
include the header file in each file where you want to use this macro.
There's nothing that needs to be instantiated.

#### ControllerPreset

Abstract class representing a controller preset. For each controller
type there's a subclass: **HidControllerPreset**,
**MidiControllerPreset**... Jordi will need to create a
*KeyboardControllerPreset* subclass.

#### ControllerPresetFileHandler

Handles loading and saving of Controller presets.

#### ControllerPresetVisitor

*Controller* inherits from it. This class defines a series of pure
virtual methods called *visit*. *Controller* subclasses must implement
these *visit* methods according to their ability to handle each preset
type. Like this:

<https://github.com/mixxxdj/mixxx/blob/master/src/controllers/midi/midicontroller.cpp#L34>

<https://github.com/mixxxdj/mixxx/blob/master/src/controllers/midi/midicontroller.cpp#L44>

Here's the explanation of why this is needed:

<https://github.com/mixxxdj/mixxx/blob/master/src/controllers/controller.h#L34>

#### ControllerEngine

It manages the loading and execution of a script. *Controller* class
holds a *ControllerEngine* instance.

#### ControllerEnumerator

Abstract class that looks for available controllers. For each controller
type there's a subclass: **HidEnumerator**, **MidiEnumerator**... Jordi
will need to create a *KeyboardEnumerator* subclass.

For example if a user has two MIDI controllers connected to the
computer, *MidiEnumerator::queryDevices()* returns a list with two
instances of *MidiController*.

Here is were Jordi will have to figure out if two keyboards connected to
the same computer can be used as two controllers or the OS presents them
as a single one.

*ControllerManager* class holds a list of *ControllerEnumerator*
instances.

#### ControllerManager

Manages creation/enumeration/deletion of hardware controllers. When a
class wants to access a controller or query the available ones, it asks
*ControllerManager*. There's only one instance of *ControllerManager*
that is created in *MixxxMainWindow* (mixxx.cpp) and gets its
*slotSetUpDevices* method called, at Mixxx start.
