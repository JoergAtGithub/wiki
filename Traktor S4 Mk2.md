# Traktor Kontrol S4 MK2

[[/media/native_instrument_traktor_s4-mkii-1.jpg|native\_instrument\_traktor\_s4-mkii-1.jpg]]

The Kontrol S4 MK2 is one of the most popular controllers for DJs. The
MK2 has substantial improvements over the previous S4 MK1, including
large all-light buttons for easier visibility.

Mixxx supports the S4 MK2 from version 2.0 onwards. The MK1 is not
supported and can not be supported due to a proprietary communication
protocol that Native Instruments invented. The MK2 uses an open
standard, so the Mixxx mapping is completely functional.

The S4 MK2 has been designed to work with Traktor, and while there's a
lot of overlap between Mixxx and Traktor, some buttons on the S4 don't
quite translate to Mixxx.

Most of the functions are exactly as they appear on the device, and most
Traktor users shouldn't have a problem picking up and using the
controller right away.

### Loading the Mapping

To load the S4 mapping, open the preferences and click on the Controller
item in the side list. You should see multiple items listed for the
Kontrol S4. Find the Kontrol S4 HID device, not the MIDI device. In the
main window, click the drop-down list labeled "Load Preset." Look for
Traktor Kontrol S4 MK2 and select it. Then hit "Apply" at the bottom of
the preferences window. The controller should light up satisfyingly,

### Mapping Notes

Mixxx does not have remix decks, so the four remix slot buttons have
been repurposed. By default, they will launch samples in the sampler
decks. If you choose, you can edit the controller script and change
these buttons to perform loop rolls instead. Also by default, Shift +
CUE rewinds the track to the beginning. You can change this to a Reverse
Roll, or "Censor" effect instead.

Making these changes is still a little awkward and we will be making
controller preferences easier to change in the future. For now you'll
have to make a one-word change to the mapping script. Don't worry, the
actual edit only involves replacing a single word in a text file.

1.  In the preferences for the controller you should see a series of
    tabs at the top of the preferences window, one of which is
    "Scripts". Select this.
2.  Select "Traktor-Kontrol-S4-MK2-hid-scripts.js". 
3.  Click "Open Selected File."
4.  Either the file should open in an editor, or you should see a file
    browser window with that file selected. If you see a file browser,
    right click the file and select an option to edit it.
5.  The script file will explain what word to change.

The Looping controls are not fully implemented. Currently, pressing the
"Loop Set" knob always creates an 8 bar loop. This will be fixed in a
future update to allow creation of arbitrary-sized loops.

There are some more bonus actions that can be accessed by holding shift
and pressing certain buttons.

  - Shift + Loop Move will adjust the musical pitch of the track without
    changing the speed.
  - Shift + Loop Size will seek quickly through the track for easy
    previewing.
  - Shift + Load will eject the track.
  - Shift + Remix Slot will create a loop of predetermined size.

The Master Volume knob on the S4 controls the built-in hardware volume
directly, so we have chosen not to also bind it to the Mixxx software
master volume control. Peak display is only generated from software,
however. So if you see peaking, it won't help to lower the master volume
knob -- adjust the knob in the Mixxx GUI or lower the gain of the
playing tracks.

### TODO

There are some features we still plan to add to this mapping:

  - Loop size readout / selection
  - On Air indicator for shoutcast or set recording
  - Find uses for other unused buttons
  - Microphone volume knob
