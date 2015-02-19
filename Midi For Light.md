\-- DRAFT --

# The Midi\_for\_light controller

Midi\_for\_light is a controller for mixxx. It sends midi "light
intresting" signals. The lightshow can follow in different ways the
music.

## Overview MIDI Notes

| action      | note        | value                      |
| ----------- | ----------- | -------------------------- |
| deck change | C (48/0x30) | 100/0x64 (+new decknumber) |
| beat        | D (50/0x32) | 100/0x64                   |
| BPM         | E (52/0x34) | BPM - 50                   |
