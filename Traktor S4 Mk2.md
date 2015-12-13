# Traktor Kontrol S4 MK2

[[/media/native_instrument_traktor_s4-mkii-1.jpg|native\_instrument\_traktor\_s4-mkii-1.jpg]]

The Kontrol S4 MK2 is one of the most popular DJ controllers. The MK2
has substantial improvements over the previous S4 MK1, including large
all-light buttons for easier visibility. We support the S4 MK2 from
version Mixxx 2.0 onwards. The MK1 is not supported and can not be
supported due to a proprietary communication protocol that Native
Instruments invented. The MK2 uses an open standard so the Mixxx mapping
is completely functional.

Most of the functions are exactly as they appear on the device and most
Traktor users shouldn't have a problem picking up and using the
controller right away. While there's a lot of overlap between Mixxx and
Traktor, some buttons on the S4 don't quite translate to Mixxx.

### Loading the Mapping

To load the S4 mapping:

1.  Open the Mixxx Preferences and click on the Controller category in
    the left-hand list. 
2.  You should see multiple items listed for the Kontrol S4. Find the
    Kontrol S4 HID device, not the MIDI device. 
3.  Click the drop-down list labelled "Load Preset." 
4.  Look for Traktor Kontrol S4 MK2 and select it. 
5.  Hit "Apply" at the bottom of the preferences window. 

The controller should light up satisfyingly and should be immediately
usable.

### Mapping Notes

Mixxx does not have remix decks, so the four remix slot buttons have
been repurposed. By default, they will launch samples in the sampler
decks.

The Loop Size select knob is not fully implemented. Currently, pressing
the "Loop Set" knob always creates an 8 bar loop, and turning the knob
will change the size of existing loops. This will be fixed in a future
update to allow creation of arbitrary-sized loops.

There are some more bonus actions that can be accessed by holding shift
and pressing certain buttons.

  - Shift + Loop Move will adjust the musical pitch of the track without
    changing the speed.
  - Shift + pressing the Loop Move knob will reset the musical pitch to
    natural.
  - Shift + Loop Size will seek quickly through the track for easy
    previewing.
  - Shift + Load will eject the track.
  - Shift + Remix Slot will create a loop of predetermined size.

Note that Mixxx doesn't have the concept of a single "master" deck for
sync. Instead, you should push and hold the sync button to "lock" sync
on for all decks you want to remain in sync. Or you can push Shift +
Sync to lock sync on. See the manual: [Master
Sync](http://www.mixxx.org/manual/2.0/chapters/djing_with_mixxx.html#master-sync)

The Master Volume knob on the S4 controls the built-in hardware volume
directly, so we have chosen not to also bind it to the Mixxx software
master volume control. Peak display is only generated from software,
however. So if you see peaking, it won't help to lower the master volume
knob -- adjust the knob in the Mixxx GUI or lower the gain of the
playing tracks.

### Unused Buttons

  - Snap button does nothing (in Mixxx, Quantize does both Quantizing
    and Snapping)
  - Master button does nothing, but lights up when sync is enabled
  - Loop recorder knob and buttons do nothing
  - FX knob buttons do nothing
  - While the Flux button works, the Reset button does nothing

### User Configurable Mapping Changes

If you choose, you can edit the controller script and change the Remix
Slot buttons to perform loop rolls instead. Also by default, Shift + CUE
rewinds the track to the beginning. You can change this to a Reverse
Roll, or "Censor" effect instead.

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

  - Loop size readout / selection
  - On Air indicator for shoutcast or set recording
  - Find uses for other unused buttons
  - Microphone volume knob
