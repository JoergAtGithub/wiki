### Controller

Abstract class representing a controller. For each controller type
there's a subclass: **HidController**, **MidiController**... Jordi will
need to create a *KeyboardController* subclass.

### ControllerDebug

This class is used to provide the *controllerDebug(String s)* macro.
This macro prints controller debug messages. It is only needed to
include the header file in each file where you want to use this macro.
There's nothing that needs to be instantiated.

### ControllerPreset

Abstract class representing a controller preset. For each controller
type there's a subclass: **HidControllerPreset**,
**MidiControllerPreset**... Jordi will need to create a
*KeyboardControllerPreset* subclass.

### ControllerPresetFileHandler

Handles loading and saving of Controller presets.

### ControllerPresetVisitor

*Controller::setPreset(const Controller& preset)* needs to know the
[dynamic
type](http://stackoverflow.com/questions/7649649/what-is-dynamic-type-of-object)
of *preset*, because a controller should only handle its corresponding
preset types (e.g. a *MidiController* should only handle instances of
*MidiControllerPreset*).

To achieve this, the [Visitor
pattern](https://en.wikipedia.org/wiki/Visitor_pattern) is used.

Suppose *preset* is a *MidiControllerPreset*. First
*Controller::setPreset(const Controller& preset)* calls the
*preset.accept(ControllerVisitor\* visitor)*, which calls
*visitor.visit(this)*. But since *preset* is of type
*MidiControllerPreset*, the method that is called is
*Controller::visit(MidiControllerPreset\* preset)*, thus controller now
knows the type of *preset*.

Providing a fallback *Controller::visit(ControllerPreset\* preset)*
saves us from implementing a *visit* method for each subclass of
*ControllerPreset*.

### ControllerEngine

It manages the loading and execution of a script. *Controller* class
holds a *ControllerEngine* instance.

### ControllerEnumerator

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

### ControllerManager

Manages creation/enumeration/deletion of hardware controllers. When a
class wants to access a controller or query the available ones, it asks
*ControllerManager*. There's only one instance of *ControllerManager*
that is created in *MixxxMainWindow* (mixxx.cpp) and gets its
*slotSetUpDevices* method called, at Mixxx start.

### ControllerVisitor

Similar to *ControllerPresetVisitor*. In this case
*ControllerMappingTableModel* wants to know the dynamic type of a
*Controller* instance.
