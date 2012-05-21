# HID Device API

An API to allow mapping/scripting of HID devices in a similar manner to
MIDI devices, hiding ugly details of HID protocol as much as possible.

Development of this API for Mixxx 1.11 is done by Hile in
[hidscripts](https://code.launchpad.net/~hile/mixxx/hidscripts) branch.
This branch will modify files only in the res/controllers/ directory and
the files mostly are new scripts, not conflicting with existing files.

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

Current proposed API contains three javascript prototype classes:

  - **HIDController** implements an abstract HID controller javascript
    class, which is expected to take care of all HID packet creation and
    parsing, including updating the field values in these packets.
  - **HIDPacket** is a container used to both receive and parse HID
    packets from devices and to specify the format for packets sent to
    the device.
  - **HIDBitVector** is initialized from HIDPacket automatically and
    should not be directly handled by user scripts. It's purpose is to
    combine bits in same HID packet field to group of independently
    parsed and updated bits. A new HIDBitVector is automatically created
    when a control or output is added to same HID packet offset. 

Each controller script using the API must at least:

  - Include hid-common-packet-parser.js in the XML file before the
    actual script
  - Implement exactly one HIDController instance (instead of new
    Controller() in MIDI scripts)
  - Create and register one HIDPacket *Input Packet* entry named
    'control' to the HIDController instance

Optionally, each HID controller script often needs to:

  - Define other input packets to receive other than controller status
    from the device
  - Define output packets to control LEDs or other items on the device,
    according to device specific details
  - Define output packets to change HID device state, for example
    disable mouse, initialize HID mode or request details from device
  - Add *Scaling Functions* to the HID controller values, which can be
    anything from single bit to 32bit integer numbers
  - Add *Filtering Functions* to the HID data. The HID controllers are
    often too high resolution and may send meaningless minor changes
    which we want to filter out
  - Register a *Callback Function* to the control registered in a HID
    packet

All these details have been implemented by the HID common packet parser
classes.

### Defining Controls

Signature for the function to add controls:

    HIDPacket.prototype.addControl = function(group,name,offset,pack,bitmask,isEncoder) {};

A *control* identifies the bits/bytes that relate to a specific element
on the controller, whether incoming changes from controller or outgoing
data to be sent to the controller.

If a *control* were to be defined from within a
[hid\_mapping\_format](hid_mapping_format) xml file it should be
possible to bind this *control* to a custom script function via
something like a `scriptfunction="myprefix.myfunction"` attribute or use
the midi xml format method of *key* optionally representing the function
name. This is not yet supported in Mixxx 1.11, all controls must be
mapped in javascript for now.

There are four types of controls supported by HIDPacket:

#### Type

  - **button:** a binary on/off toggle from device. While some buttons
    may have multiple states (bitmask not bit), this is not yet
    supported and the fiedl must be manually processed from a byte.
  - **fader:** a numeric value, size 1-4 bytes, from the device. Usually
    these control mixxx internal values like knobs, jogs or faders.
    Unlike MIDI, HID does not specify range of such controls and the
    values are often far off from mixxx ranges. A scaling function can
    be automatically applied to move the value to expected range (for
    example, fader from unsigned short value to -1..1 range of mixxx).
  - **encoder:** the physical control is an encoder that sends out
    continous data like a fader, but resets to zero once reaching it's
    maximum value (and conversely when moved in reverse). An encoder is
    processed and added exactly like a fader, only difference is setting
    of isEncoder variable to true. This will change the field parsing
    code to set the field 'delta' attribute to -1 or +1 offsets, and
    wrapping over minimum and maximum values automatically. The minimum
    and maximum values are deduced from the field size, for example a
    'byte' encoder wraps from 255 to 0 and from 0 to 255, giving delta
    -1 and 1 respectively.
  - **LED/Output** a bit or byte to be sent back to the controller, most
    commonly to control status LEDs. Current implementation does not
    support sending short or integer size values, and sending of bitmask
    of bits is possible but not yet supported by the API. HIDController
    takes care of updating only modified parts of the outgoing packet.
    Right now API is missing a function to set other types of data
    except LED, but this can be trivially added when we know what is
    exactly needed.

#### Packet Header

On many devices, each HID packet has a prefix in the packet to recognize
which packet this is: for example, EKS Otus 'control' packet first two
bytes are 0x0 and 0x35 (id and length). The packet header is given as an
array when creating new packet. If there is no header, pass empty array
to the variable.

#### Offset

The byte offset of the field within the packet, starting from 0.

#### Packing

Instead of telling the packet field length, HIDPacket parses the fields
based on *pack* attribute. The packing tells the size and numeric range
for each field, and allows us to convert the input number to and from
exactly correct value. Valid 'pack' values are b (signed byte), B
(unsigned byte), h (signed short), H (unsigned short), i (unsigned int)
and I (signed int). A field containing bits still needs to be given
valid 'pack' value, to calculate bit vector masks and check boundaries.

#### Bitmask

Bitmask defines the bit to flip for bit controls in the packet:
internally, a HIDBitVector packet field is created when bitmasks are
seen. If multiple controls with same offset and packing are defined,
they are mapped transparently as fields of same HIDBitVector field,
which can be updated or read in one go.

Bitmask can be used when defining both button bit inputs and LED output
bits.

In current implementation, fader and encoder controls must have bitmask
attribute set to 0: we don't support controls like 'high four bits of
this byte'. It is not possible to have both fader/encoder numeric fields
and bits in same input packet field.

#### Group

Used in the same way as for a midi mapping - the default *group* that
this control will be bound to.

For automatic deck assignment to dynamic controllers, special names
'deck', 'deck1' and 'deck2' can be used to assign to even/odd decks, or
to currently selected deck. All internal controls and connections are
updated automatically, when deck status is changed and such group names
are used. You can also register some controls with virtual deck mappings
and some fields hard coded to specific deck.

For input and output controls not to mapped anywhere automatically, we
suggest using using group name 'hid'. All data from and to these fields
must be manually scripted or assigned in custom script functions. One
example of such variable could be 'deck chooser' control in EKS Otus, or
'modifier fields.

#### Name

A name for the control. If the control is mapped without a script
function directly to mixxx, this name must be valid control name in
mixxx for the group where the control is attacked to.

\<del\>=== Min Value ===

Lowest value of these bytes when the control is at its minimum setting.
0 is the default.

#### Max Value

The highest value of these bits/bytes when the control is at its maximum
setting. 0xFFFF is the default for two bytes \</del\>

**NOTE** Minimum and maximum values are calculated automatically for a
field from the 'pack' attribute.

Current control defination format is following:

    packet.addControl('[Master]','crossfader',34,'H');
    packet.addControl('[Playlist]','SelectTrackKnob',15,'B',undefined,true);

### Parsing Incoming Controls

HIDController implements parsing of incoming packet named 'control'
automatically. Unfortunately due to namespace issues in current qtscript
implementation we use, you still need to implement an incomingData
function in your script. The standard wrapper to your script is
following:

    MyDevice.incomingData = function(data,length) {
      MyDevice.parsePacket(data,length);
    }

The default parsePacket function has following side effects:

  - Only modified input field values are processed by any callbacks or
    automated calls to engine
  - If a field has registered callback function, this function is called
    **without running** scaling functions or resolving correct decks.
    All other processing for fields with a custom callback is ignored.
  - If field has no callback, it's scaling function is called (if
    defined), virtual deck mapping to actual deck is performed and the
    assigned control group and name are attempted to be update directly
    in mix with scaled value. If the field's group name does not match a
    known mixxx control group or virtual deck, this is not done and the
    field input is ignored.
  - Finally, if a function called processDelta is defined, it is called
    with all modified fields in the packet. This is done after automated
    fields and callbacks already have been called, so don't handle same
    field twice\!

### Binding Actions to Incoming Controls

After packets have been added to HIDController, the registered fields
can be mapped to controls. It's not recommended to bind controls in the
addControl call, while possible: we should keep the packet declaration
separate from functional declarations.

The callback function is called, whenever we receive a modified value
for the given field from HID device.

Example call to register a callback function (exactly same group and
name must be defined in packets):

``` 
 MyDevice.registerInputCallback('control','[Master]','headphones_knob',MyDevice.headphones);
```

Note we need to specify the 'control' packet name, even if it's the
default packet to receive. We must support multiple different input
packets here\!

## Loading of packets, scalers and callbacks in one call

It is recommended to group all input, output, scaling and callback
declarations to following four functions and call these in this order in
init():

``` 
  MyDevice.registerInputPackets();
  MyDevice.registerOutputPackets();
  MyDevice.registerScalers();
  MyDevice.registerCallbacks();
  
```

### Sending Data to the HID Device

Currently only LED output control is implemented for the output packets
in the HIDController APIs. Outgoing LED controls are defined with
similar syntax to addControl: only big difference is outgoing packets
are registered with 'MyDevice.registerOutputPacket()' and LED control
adding function is called 'addLEDControl', the packet itself is
initialized in exactly same way.

LED controls packet declaration example (declaring two LEDs controller
by whole byte not by bits):

``` 
  packet = new HIDPacket('test_leds',[0x17,0x16],4);
  packet.addLED('hid',"test_led_1",2,'B');
  packet.addLED('hid',"test_led_1",3,'B');
  MyDevice.registerOutputPacket(packet);
  
```

LED in this packet can be set explicitly with call like:

``` 
  setLED('hid','test_led_1',MyDevice.LEDColors['blue']);
```

LEDs matching virtual decks can be automatically assigned to current
deck. TODO document this.

Packets can also have packet level callbacks, so custom functions can be
used to send arbitrary packets. In the custom function, you need to fill
in the correct values to the packet fields before sending to construct
the packet: see EKS Otus mapping for examples.

Minimal example of output packet with just one field from Otus mapping:

``` 
  packet = new HIDPacket('set_ledcontrol_mode',[0x1d,0x3],32);
  packet.addControl('hid','mode',2,'B');
  EksOtus.registerOutputPacket(packet);
  
```

Example part of custom function to send this packet:

``` 
  var packet = EksOtus.OutputPackets['set_ledcontrol_mode'];
  var field = packet.lookupField('hid','mode');
  if (field==undefined) {
      script.HIDDebug("EksOtus.setLEDControlMode error fetching field mode");
      return;
  }
  field.value = mode;
  packet.send();
```

## References

  - **Development branch by Hile for HID scripts**
    <https://code.launchpad.net/~hile/mixxx/hidscripts>
  - **Hercules Console Mk2 HID Mapping**
    <http://mixxx.org/forums/viewtopic.php?f=7&t=3712>
