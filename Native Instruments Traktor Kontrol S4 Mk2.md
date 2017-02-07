# Native Instruments Traktor Kontrol S4 MK2

[[/media/native_instrument_traktor_s4-mkii-1.jpg|native\_instrument\_traktor\_s4-mkii-1.jpg]]

  - [Manufacturer's product
    page](https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s4/)
  - [DJTechTools
    review](http://djtechtools.com/2013/10/22/review-traktor-kontrol-s4-mk2-and-s2-mk2/)
  - [Digital DJ Tips
    review](http://www.digitaldjtips.com/2013/10/review-video-traktor-kontrol-s4-mk2/)
  - [DJWORX
    review](https://djworx.com/review-ni-traktor-kontrol-s4-mk2-dj-controller/)

The Kontrol S4 MK2 is a 4 deck all-in-one controller with a sturdy build
quality and integrated sound card. The MK2 has substantial improvements
over the S4 MK1, including large multicolor buttons. The MK1 is not
supported and cannot be supported because it uses a proprietary
communication protocol exclusive to Traktor. The MK2 uses the open HID
standard, so it can work with Mixxx. The easiest way to tell the MK1
apart from the MK2 is the appearance of the jog wheel. On the MK1, the
top of the jog wheel is black plastic; on the MK2, the top of the jog
wheel is shiny aluminum.

## Compatibility

### Controller

The Kontrol S4 MK2 is compatible with Mixxx without any proprietary
drivers on GNU/Linux and Mac OS X. On Windows, it is recommended to
install the [driver from Native
Instruments](https://www.native-instruments.com/en/support/downloads/drivers-other-files/)
and select the ASIO sound API in the Sound Hardware section of Mixxx's
Preferences.

With the S4 plugged in, a MIDI device is listed as an available
controller in Mixxx's Preferences. That is the MIDI input/output ports
on the back of the S4 for connecting external MIDI gear; no mapping for
the S4 will appear in the menu for the MIDI device. The controller uses
HID, so the mapping can only be loaded when you select the HID device on
the left side of Mixxx's Preferences.

### Timecode vinyl

The phono inputs on the S4 can be used with turntables for timecode
vinyl control of Mixxx. Unlike Traktor, there is no additional software
to install to use timecode with the S4; the free version of Mixxx is the
full version. However, note that Mixxx is not compatible with Traktor
Scratch Mk2 timecode; refer to the [Mixxx
manual](http://mixxx.org/manual/latest/chapters/vinyl_control.html#supported-timecode-media)
for a list of supported types of timecode.

## Mapping description

Most of the functions are mapped as they appear on the device and most
users coming from Traktor should not have a problem picking up and using
the controller right away. While there is a lot of overlap between Mixxx
and Traktor, some buttons on the S4 do not quite translate to Mixxx.
This guide is not a replacement for the [Mixxx
Manual](http://www.mixxx.org/manual/2.0/) and any questions not answered
here ("What is keylock?") are addressed there.

Note that Mixxx doesn't have the concept of a single "master" deck for
sync. Instead, you should push and hold the sync button to "lock" sync
on for all decks you want to remain in sync. Or you can push Shift +
Sync to lock sync on. See [the Mixxx
manual](http://www.mixxx.org/manual/2.0/chapters/djing_with_mixxx.html#master-sync)
for details.

Mixxx does not have remix decks, so the four remix slot buttons have
been repurposed. By default, they will launch samples in the sampler
decks.

The Loop Size select knob is not fully implemented. Currently, pressing
the "Loop Set" knob always creates an 8 bar loop, and turning the knob
will change the size of existing loops. This will be fixed in a future
update to allow creation of arbitrary-sized loops.

The FX Mode button changes which effect is loaded in the FX bank.
Currently only one effect can be loaded in each bank.

There are some more bonus actions that can be accessed by holding shift
and pressing certain buttons.

\* Shift + Loop Move will adjust the musical pitch of the track without
changing the speed. \* Shift + pressing the Loop Move knob will reset
the musical pitch to natural. \* Shift + Loop Size will seek quickly
through the track for easy previewing. \* Shift + Load will eject the
track. \* Shift + Remix Slot will create a loop of predetermined size.

The Master Volume knob on the S4 controls the built-in hardware volume
directly, so we have chosen not to also bind it to the Mixxx software
master volume control. Peak display is only generated from software,
however. So if you see or hear clipping, it won't help to lower the
master volume knob -- adjust the knob in the Mixxx GUI or lower the gain
of the playing tracks.

### Unused controls

  - Snap button does nothing (in Mixxx, Quantize does both Quantizing
    and Snapping)
  - Master button does nothing, but lights up when sync is enabled
  - Loop recorder knob and buttons do nothing
  - FX knob buttons do nothing
  - While the Flux button works, the Reset button does nothing

### Mapping options

If you choose, you can edit the controller script and change the Remix
Slot buttons to perform loop rolls instead. Also by default, Shift + CUE
rewinds the track to the beginning but you can change this to a Reverse
Roll (or "Censor") effect instead.

Making these changes is still a little awkward and we will be making
controller preferences easier to change in the future. For now you'll
have to make a small change to the mapping script file. Don't worry, the
actual edit only involves replacing a single word in a text file.

1.  Open Mixxx Preferences and select the Kontorl S4 in the side list.
2.  You should see a series of tabs at the top of the preferences
    window, one of which is "Scripts". Select that tab.
3.  Select "Traktor-Kontrol-S4-MK2-hid-scripts.js". 
4.  Click "Open Selected File."
5.  Either the file should open in an editor, or you should see a file
    browser window with that file selected. If you see a file browser,
    right click the file and select an option to edit it.
6.  At the top of the file will be short instructions explaining what to
    do.

### TODO

There are some features we still plan to add to this mapping:

  - New effects interface in Mixxx 2.1
  - Loop size readout / selection
  - On Air indicator for shoutcast or set recording
  - Find uses for other unused buttons
  - Microphone volume knob
