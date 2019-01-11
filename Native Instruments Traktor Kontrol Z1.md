# Native Instruments Traktor Kontrol Z1

[[/media/native-instruments-traktor-kontrol-z1.jpg|native-instruments-traktor-kontrol-z1.jpg]]

  - [Manufacturer's product
    page](https://www.native-instruments.com/de/products/traktor/traktor-for-ios/traktor-kontrol-z1/)

The Traktor Kontrol Z1 is a small, portable 2-deck controller with an
integrated soundcard.

## Usage

A mapping for the Kontrol Z1 exists that maps all controls to Mixxx just
as they are labelled, except for the "Mode" button, which right now does
nothing.

You can use the Kontrol Z1 as a sound output. Channel 1-2 will go to the
Main Out, two cinch ports at the top of the controller, with volume
being regulated by the "Main" knob. Channel 3-4 will go to the phones, a
single 3.5mm stereo jack at the bottom of the controller, with volume
being regulated by the "Cue Vol" knob.

## HID Specification

### Input

> Note: The "Main" and "Cue Vol" controls operate on the hardware level
> and thus do not send any signals

Report ID: 0x1

#### Knobs & faders

Each control spans 2 Bytes, but only sends up to 12 Bits. These are the
controls in order in which they are sent.

Each of these knobs exists twice, first are all that are one the left
and then all on the right.

  - "Gain" Knob
  - "HI" Knob
  - "MID" Knob
  - "LOW" Knob
  - "FX" Knob
  - "Cue Mix" Knob

Left Vertical Fader

Right Vertical Fader

Crossfader

#### Buttons

The buttons all are at an offset of 29 and and are listed here with
their bitmask:

  - Mode - 0x2
  - Headphone Button (A) - 0x10
  - Headphone Button (B) - 0x1
  - FX Button left - 0x4
  - FX Button right - 0x8

### Output

Report ID: 0x80

All bytes represent Brightness and can be set granularly from 00 to 7F
(Even though Traktor always sends either 0A or 7F).

  - Volume meter left - 7 Bytes (5 Blue + 2 Orange)
  - Volume meter right - 7 Bytes (5 Blue + 2 Orange)
  - Headphone Button (A) - 1 Byte Blue
  - Headphone Button (B) - 1 Byte Blue
  - FX Button left - 1 Byte Red, 1 Byte Blue
  - Mode Button - 1 Byte White
  - FX Button right - 1 Byte Red, 1 Byte Blue
