\-- DRAFT --

# The Midi\_for\_light controller

Midi\_for\_light is a controller for mixxx. It sends midi "light
intresting" signals. The lightshow can follow in different ways the
music.

## Overview MIDI Notes

| action                  | note            | value                        |                  |
| ----------------------- | --------------- | ---------------------------- | ---------------- |
| deck change             | C ( 48 / 0x30 ) | 100 / 0x64 (+new decknumber) |                  |
| beat                    | D ( 50 / 0x32 ) | 100 / 0x64                   |                  |
| BPM                     | E ( 52 / 0x34 ) | BPM - 50                     |                  |
| VU mono current         | E               | ( 64 / 0x40 )                | 0-127 / 0x0-0x7f |
| VU mono average min     | F               | ( 65 / 0x41 )                | 0-127 / 0x0-0x7f |
| VU mono average mid     | F\#             | ( 66 / 0x42 )                | 0-127 / 0x0-0x7f |
| VU mono average max     | G               | ( 67 / 0x43 )                | 0-127 / 0x0-0x7f |
| VU mono average fit     | G\#             | ( 68 / 0x44 )                | 0-127 / 0x0-0x7f |
| VU mono current meter 1 | A               | ( 69 / 0x45 )                | 0-127 / 0x0-0x7f |
| VU mono current meter 2 | A\#             | ( 70 / 0x46 )                | 0-127 / 0x0-0x7f |
| VU mono current meter 3 | B               | ( 71 / 0x47 )                | 0-127 / 0x0-0x7f |
| VU mono current meter 4 | C               | ( 72 / 0x48 )                | 0-127 / 0x0-0x7f |
| VU mono average meter 1 | A               | ( 73 / 0x49 )                | 0-127 / 0x0-0x7f |
| VU mono average meter 2 | A\#             | ( 74 / 0x4a )                | 0-127 / 0x0-0x7f |
| VU mono average meter 3 | B               | ( 75 / 0x4b )                | 0-127 / 0x0-0x7f |
| VU mono average meter 4 | C               | ( 76 / 0x4c )                | 0-127 / 0x0-0x7f |
