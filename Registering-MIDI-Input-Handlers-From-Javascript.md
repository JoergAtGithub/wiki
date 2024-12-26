# Registering MIDI Input Handlers From JavaScript

This feature is in planning. It is currently not included in Mixxx.

## Background

Working with the hybrid JavaScript & XML system is an unpleasant
developer experience. Most controllers require (almost) all of the
mapping to be written in JavaScript for a fully functional mapping. XML
files quickly become very unwieldy and practically impossible to
organize. Every time a JavaScript input handler is renamed or a mapping
is rearranged, the XML file must be edited and manually reloaded, which
is an error prone process. It would be easier and more fun to write
mappings if development could be done entirely in JavaScript. The
JavaScript system can already handle output to controllers; the only
missing piece is registering functions to handle input from controllers.

## Overview

Registering controller input handlers would be done similar to how
output handlers are registered. A special Q\_INVOKABLE C++ function
would be called by the script that would return an object to the script
representing the input connection. This connection object would have a
UUID and a `disconnect` method, but not do anything else (maybe add a
`connect` method to disconnect and reconnect without creating a new
object?). There would not be a limit to the number of connections that
could be registered to each MIDI input signal.

Each controller mapping would still require an XML file, but the role of
this would be reduced to providing metadata to the preferences so Mixxx
does not have to evaluate every JavaScript file in the mapping
directories to find available mappings. The `<controls>` element would
no longer be needed in the XML file.

# JavaScript API

Instead of mimicking the old hybrid XML/JS system, use this opportunity
to provide a cleaner API that is easy to remember. I still have to copy
and paste because I can't remember the function signature for MIDI input
callbacks registered with XML.

The input handlers will not do much by themselves. Instead of
associating information needed by the input callback (such as a
ControlObject to work with) with the input handler object, leave this
responsibility with scripts. Components will make that easy.

## Basic form

The first argument to the function creating the connection would be an
array containing the first MIDI bytes of the incoming signal. The second
argument would be the callback function. The callback function would
receive a single argument that is an array with each member being a byte
of the incoming MIDI message.

    var connection = midi.makeInputHandler([0x91, 0x40], function (input) {
        engine.setValue('group', 'item', input[2] / 127);
    });
    connection.disconnect();

## Fitting in with object oriented JavaScript

Like registering output connections, the callbacks registered via
`midi.makeInputHandler` would be executed with JavaScript's `this`
keyword set to the object in which `midi.makeInputHandler` was called.

Here is a little demonstration that would handle deck 1's play button:

    var ConstructorFunction = function (group) {
        this.group = group;
        this.inputConnection = midi.makeInputHandler([0x91, 0x40], function (input) {
            engine.setValue(this.group, 'play', input[2] / 127);
        });
    };
    
    var someObject = new ConstructorFunction('[Channel1]');
    
    // ... stuff happens ...
    
    someObject.group = '[Channel3]';
    // someObject now handles the play button for deck 3
    // using the same MIDI input callback connected to the same MIDI signal

A `bind` method on the connection objects could be provided to change
the `this` object. That might open the door to innovative ways of
structuring code better, but it might lead to unnecessarily complex
code. Thoughts?

## Integrating with Components

The [Components JS](Components-JS.md) library would continue to work in
largely the same way. The input callback would be registered by the
generic `Component` constructor using the Component's `midi` and `input`
properties as arguments to `midi.makeInputHandler`. Like the output
connections, the input connection objects would be stored in an array
property of the Component and the library would provide prototype
methods for connecting/disconnecting the input handlers. As before,
input callbacks would use `this.group` and `this.inKey` to refer to a
ControlObject specified by the Component.

## Working with layers

When controllers send different MIDI signals with a shift button
pressed, a second input callback would have to be registered for every
shifted input signal. Like it is currently handled with Components, this
could be the same function as the unshifted callback. Shifted
functionality could be provided by referring to properties of the
Component (such as `inKey`) that are changed by the Component's `shift`
& `unshift` functions (which are called by ComponentContainer's `shift`
and `unshift` methods). Alternatively, separate functions could be
provided for the shifted and unshifted callbacks.

For managing layers when the controller does not send different MIDI
signals for each layer, the input callback could be disconnected by
calling the connection object's `disconnect` method, then a new callback
could be registered. Component and ComponentContainer will provide ways
to manage this.

# C++ side

Input callback connections would be stored with a struct similar to a
ScriptConnection created for an output callback. These structs would
hold a QUuid, the callback QScriptValue, and the `this` object
QScriptValue as members. A Q\_OBJECT wrapper would be created around
those objects to return the connection objects to scripts with
Q\_INVOKABLE methods (disconnect, bind, and any other methods we think
may be useful).

Add the Q\_INVOKABLE makeInputHandler function as a protected method of
MidiController. This function would create a MidiInputMapping and insert
it into the m\_preset.inputMappings QMultiHash. MidiInputMapping would
be modified to hold the connection object described above.
MidiController::processInputMapping would check if the MidiInputMapping
contained a script connected callback, and if so, execute it.
