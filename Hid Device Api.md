# HID Device API

An API to allow mapping/scripting of HID devices in a similar manor to
MIDI devices.

## Summary and Rationale

When data is *sent* from a hid controller multiple controls are
aggregated into *packets* so a common api is needed to allow the actual
modified *controls* to be processed without every mapping needing to
parse these packets themselves. Similarly when the state of a hid device
needs to be updated (leds or other feedback) one or more updates are
aggregated into a packet which contains the new state for all the
*controls* within that packet regardless of whether each has changed or
not. The common hid api should take care of this
decoding/parsing/encoding.

Ideally the API (and future XML device definition file) should abstract
the hid layer in such a way that a mapping written for a hid controller
could also be used for a midi controller, possibly with no changes at
all for a controller that can be used in both midi and hid modes).

For the HID device mappings for 1.11 each mapping has to implement it's
own parsing/encoding of HID data. We would like to get some common code
into the Javascript library that would later be ported to the C++ core.
The concern is that if we add any functions now that mappers rely on we
won't be able to change it later on, so even if the implementation is
only in Javascript initially it needs to be well considered.

## Components

The API should consist of these functional areas:

### Defining Controls

A *control* identifies the bits/bytes that relate to a specific element
on the controller, whether incoming when physically changed or outgoing
to be sent back to the controller.

A *control* can be defined from a script or from within a hid formatted
xml device definition file.

If a *control* were to be defined from within a
[hid\_mapping\_format](hid_mapping_format) xml file it should be
possible to bind this *control* to a custom script function via
something like a `scriptfunction="myprefix.myfunction"` attribute or use
the midi xml format method of *key* optionally representing the function
name.

A *control* can be defined by:

#### Type

  - **led:** a field to be sent back to the controller (doesn't have to
    be only an led)
  - **fader:** the data is interpreted as though it were a midi
    value/velocity with no masking at the bitlevel
  - **button:** a binary on/off
  - **encoder:** the physical control is an encoder that sends out
    continous data like a pot but resets to zero once reaching it's
    maximum value (and conversely when moved in reverse) so the
    processed value should be the relative difference between this new
    and the previously received message (a jogwheel may also behave like
    this)

#### Packet Id

The id of the packet that this control is a member of

#### Offset

The byte offset within the packet

#### Length

The length in bytes of the data field for multi byte controls

#### Bitmask

An optional bitmask that is applied to the field to extract the actual
value for this control (for when multiple controls are defined within a
single byte)

#### Pack

Whether field is signed or not and it's length like "byte", "unsigned
int", etc.

#### Group

Used in the same way as for a midi mapping - the default *group* that
this control will be bound to

#### Name

A name for the control that ideally should match up with a mixx *engine*
name

#### Key

Specifying a *key* would automatically bind that *control* to the
*engine* function like for a midi mapping.

#### Min Value

Lowest value of these bytes when the control is at its minimum setting.
0 is the default.

#### Max Value

The highest value of these bits/bytes when the control is at its maximum
setting. 0xFFFF is the default for two bytes

Probably only name/group/packetid/type/byteoffset would be mandatory
(and *group* only to conform to the mixxx midi standards, though will be
useful for most controls and make the mapping of the controls to mixxx
actions much simpler) so the it perhaps could be called like:

    addControlField("[Channel1]", "play", 0x1, 2, "button", { bitmask: 0x4 });
    addControlField("[Channel1]", "volume", 0x1, 4, "fader", { max: 255 });

This function should also be called by the future hid device mapping
parser.

### Parsing Incoming Controls

A function should exist in the API to parse an incoming packet of data.
It should perform the following:

  - Decode the first byte to identify the packet type
  - Compare each remaining byte of data with the last received data for
    that packet and identify which bytes have changed
  - Apply needed bitwise logic for each *control* defined to be using
    this byte (and only these *controls*) to identify which have changed
  - Return a list of modified *controls* and their new values or
    automatically dispatch the changes to script functions that have
    been bound to these *control* changes
  - Store a cache of the current packet to identify which bytes of this
    packet change in the future
  - Store a cache of the current value of each control within each
    packet to identify which *controls* change in the future

<!-- end list -->

    controls = parseControlState(raw_hid_packet);
    
    for (i in controls) {
      print(controls[i].name + " has changed and is now " + controls[i].value);
    }

### Binding Actions to Incoming Controls

An API function should exist to bind a *control* to either an internal
function (like binding a midi control to a mixxx *engine* action from a
midi xml mapping file) or to a script function either by name of
reference. Passing by function reference would allow inline small code
snippets to be bound to the changes.

It should be possible to bind multiple functions to a single *control*

It should be possible to define what types of value changes should call
the bound function such as "when non zero" (useful for mapping actions
to button presses instead of presses and releases), "when zero" or "all"

The predefined *group* (if any) and *name* of the changed control should
be passed to the function. This would allow mappings such as:

``` 
// bind directly to an engine action

addEngineBinding("[Channel1]", "play", PRESS, "play");

// bind to a custom function

addScriptBinding("[Channel1]", "play", PRESS, "myprefix.myfunction");

// bind to an anonymous function

addScriptBinding("[Channel1]", "play", ALL, function(group, name, value) {
    if (value > 0) {
      engine.setValue(group, name, !engine.getValue(group, name));
    }
    else {
        // do something different when the button is released
    }
});

```

These functions should also be called by the future hid device mapping
parser.

### Sending Data to the HID Device

Since the API will be keeping a cache of the current values for all
controls within all packets it should be possible to create a function
that can be used like the `engine.sendShortMsg()`

The API function could be called in one of two ways:

#### Control Names

If a named control has been defined via a *addControlField()* call (from
the XML parser or otherwise) for the LED in the same way as an incoming
control then only this name and new value would need to be specified
such as:

``` 
sendNamedMsg("[Channel1]", "play", 1);

```

The API would map the *group* and *name* back to the 'hid packet level'
byte offset+bitmask, apply this to the cache of that packet by applying
a bitwise AND with the inverse of the *controls* bitmask and then
bitwise OR the *controls* new value and then send out the complete
packet.

#### Control Definition

Some of the same parameters used to define a *control* could be passed
in explicitly such as offset, bitmask value or offset, array of values
and length (which again would result in the full packet being sent out
even though the functions are only passed a partial delta):

``` 
sendShortMsg(offset, bitmask, value);
sendShortMsg(2, 0x3, 0x1);

partial_packet = [0x1, 0x0, 0x4, 0x6, 0x7, 0x8];
byte_offset = 10;
sendLongMsg(byte_offset, partial_packet, partial_packet.length);

```

## References

  - **EKS Otus HID Mapping** <http://tuohela.net/otus.js>
  - **Hercules Console Mk2 HID Mapping**
    <http://mixxx.org/forums/viewtopic.php?f=7&t=3712>
