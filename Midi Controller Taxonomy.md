On this page we document and name every different type of MIDI
controller feature we have ever seen.

If you are going to add to this page, please include specific MIDI
message descriptions, not general descriptions of the behavior.

# VCI-100 Jog Wheels

The VCI-100 has various different firmwares so this can vary.

## Pitch-Bend

When the VCI-100 jog wheel touch sensor is not active, ticks of the jog
wheel look like this:

CW 1-tick

    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x6B, val 0x7F"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x6B, val 0x00"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x3A, val 0x7F"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x3A, val 0x00"

CCW 1-tick

    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x6B, val 0x7F"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x6B, val 0x00"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x3B, val 0x7F"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x3B, val 0x00"

The 0x6B control means "button pressed" and is emitted when any button
on the VCI-100 is pressed. CW and CCW is encoded in the control. Pitch
bend is not affected by the "vinyl mode" toggle.

## Vinyl Mode

Vinyl mode is a button on the VCI-100 whose status (including LED) is
controlled by the hardware. Presses only emit the standard "button
pressed" message:

    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x6B, val 0x7F"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x6B, val 0x00"

## Touch Sensor + Platter Move

Touch start

    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x6B, val 0x7F"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x6B, val 0x00"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x30, val 0x7F"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x2E, val 0x7F"

CW turn, Vinyl Mode On

    Debug [Controller]: "MIDI status 0xB0 (ch 1, opcode 0xB), ctrl 0x10, val 0x41"

CW turn

    Debug [Controller]: "MIDI status 0xB0 (ch 1, opcode 0xB), ctrl 0x12, val 0x41"

CCW turn, Vinyl Mode On

    Debug [Controller]: "MIDI status 0xB0 (ch 1, opcode 0xB), ctrl 0x10, val 0x3F"

CCW turn

    Debug [Controller]: "MIDI status 0xB0 (ch 1, opcode 0xB), ctrl 0x12, val 0x3F"

Release

    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x2E, val 0x00"
    Debug [Controller]: "MIDI status 0x90 (ch 1, opcode 0x9), ctrl 0x30, val 0x00"
