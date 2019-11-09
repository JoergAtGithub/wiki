# Serato System Exclusive Midi Messages

According to the [list of MIDI manufacturer
IDs](https://www.midi.org/specifications/item/manufacturer-id-numbers),
Serato has a MIDI manufacturer ID of `[0x00, 0x20, 0x7F]`.

Controller manufacturers and Serato use this manufacturer ID to exchange
sysex messages from the computer to the controller to trigger some
functions of the controller.

Currently, the only identified System Exclusive MIDI message using this
ID is described below.

#### Controller status dump

It appears that Serato sends the `F0 00 20 7F 03 01 F7` sysex message to
the Serato certified controllers to ask them to send back the status of
each item on the control surface (the value of all knobs and sliders)
which means:

  - F0 ⇒ Begin SysEx Message
  - 00 20 7F ⇒ it's the Serato Manufacturer according to
    <https://www.midi.org/specifications/item/manufacturer-id-numbers>
  - 03 01 ⇒ The Serato's proprietary message (controller dump)
  - F7 ⇒ End of SysEx Message

After receiving this message, the controller sends back a MIDI message
for each item (knob, slider, ...) sending its current value.

So if you are mapping a Serato-certified controller, you can try to send
this sysex message by adding this declaration at the top of your
javascript file:

``` javascript
// The SysEx message to send to the controller to force the midi controller
// to send the status of every item on the control surface.
var ControllerStatusSysex = [0xF0, 0x00, 0x20, 0x7F, 0x03, 0x01, 0xF7];
```

and send it at the end of your `init()` function, after connections have
been made:

``` javascript
// After midi controller receive this Outbound Message request SysEx Message,
// midi controller will send the status of every item on the
// control surface. (Mixxx will be initialized with current values)
midi.sendSysexMsg(ControllerStatusSysex, ControllerStatusSysex.length);
```

This should make Mixxx match the state of your controller when Mixxx
starts up and the mapping is loaded.

#### Special SysEx'

  - [DDJ-SX2](DDJ-SX2)
