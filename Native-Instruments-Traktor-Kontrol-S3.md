# Native Instruments Traktor Kontrol S3

**This page is a draft, and support for the S3 has not been added to Mixxx yet**

[[/media/native-instruments-traktor-kontrol-s3.jpg|native-instruments-traktor-kontrol-s3.jpg]]

  - [Manufacturer's product
    page](https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s3/)
  - [DJTechTools
    review](https://djtechtools.com/2019/10/16/traktor-kontrol-s3-the-middle-child-for-the-mk3-traktor-generation/)
  - [DJWORX
    overview](https://djworx.com/the-traktor-kontrol-s3-we-have-it-but-not-the-software/)

The Kontrol S3 is an introductory 4 deck controller with good buil
quality and integrated sound card. This is the first controller released
with the "S3" name.

The Kontrol S3 can run from USB bus power. Using the separate power
supply increases the brightness of the LEDs, which is helpful for using
it in daylight, and increases the volume of the headphone output.

## Compatibility

### Controller

The Kontrol S3 is a USB class compliant audio, HID, and MIDI device,
so it is compatible with Mixxx without any proprietary drivers on
GNU/Linux and Mac OS X. On Windows, it is recommended to install the
[driver from Native
Instruments](https://www.native-instruments.com/en/support/downloads/drivers-other-files/)
and select the ASIO sound API in the Sound Hardware section of Mixxx's
Preferences.

With the S3 plugged in, a MIDI device is listed as an available
controller in Mixxx's Preferences. The controller uses
HID for the knobs, buttons, and other components on the device, so the
mapping can only be loaded when you select the HID device on the left
side of Mixxx's Preferences.

## Mapping description

Note that Mixxx doesn't have the concept of a single "master" deck for
sync. Instead, push and hold the sync button to "lock" sync on for all
decks you want to remain in sync. Or you can push Shift + Sync to lock
sync on. Refer to [the Mixxx
manual](http://www.mixxx.org/manual/2.0/chapters/djing_with_mixxx.html#master-sync)
for details.

### Mixer

  - Gain, equalizer high/mid/low, and cue (headphones)
    behave as labelled.
  - The FX setup is unusual on this controller.  Each deck has a single on-off button for effects, and on the right-hand side there are five buttons that determine which effects are applied to every channel that has effects on.  This means it is not possible to use the controller to select one effect for one deck, and another effect for another.  You can still make these choices in the Mixxx UI, however.
  - Filter: controls QuickEffect superknob. This controls the Filter
    effect by default, but a different effect can be chosen in the
    Equalizer section of Mixxs's Preferences.

The Master Volume knob on the S3 controls the volume of the S3's master
output in hardware, so it does not affect the software master gain knob
in Mixxx. Peak display is only generated from software, however. So if
you see or hear clipping, lower the gain of the playing decks; adjusting
the master volume knob on the S3 will not help.

### Decks

  - Pressing the library knob: load track selected in library to the deck.
  - Shift + pressing knob: eject track
  - View button: move focus of library control between left-hand tree and main list.
  - Small buttons with play icons: play a sampler from its cue point.
  - Small buttons with play icons + shift: If sampler is playing, stop
    it. If sampler is not playing, the loaded eject track from the
    sampler.

#### Looping

  - right encoder turn: double/halve loop size.
  - right encoder press: activate loop of set size from current position

<!-- end list -->

  - left encoder turn: beatjump forward/backward by beatjump size (shown
    on screen but not on controller), or move the loop by beatjump size
    if there is a loop enabled
  - left encoder press: re-enable a loop that has been set previously.
    Pressing this before a loop will keep playing until the loop is
    entered.
  - left encoder turn + shift: adjust beatjump size
  - left encoder press + shift: jump to loop in point, activate loop,
    and stop playback. This is helpful for preparing to mix a track in
    with a loop.

<!-- end list -->

  - In button: set loop in point manually. Hold pressed while moving the
    jog wheel to finely adjust the loop in point.
  - Out button: set loop out point manually. Hold pressed while moving
    the jog wheel to finely adjust the loop out point.

### Effects

The knob on the left of each effect unit controls the mix (dry/wet) knob
for all 3 effects in the unit. The other knobs control the metaknobs of
the effects. The buttons below the metaknobs control the effect enable
buttons. When pressed with shift, they cycle through the available
effects. The button below the mix knob toggles whether the effect
parameters are showing on screen. This will be expanded in a future
update to implement the [Standard Effects
Mapping](Standard%20Effects%20Mapping).

The buttons at the top of each mixer column control which decks are
routed to which effects units.

### Mapping options

Making these changes is still a little awkward and we will be making
controller preferences easier to change in the future. For now you'll
have to make a small change to the mapping script file. Don't worry, the
actual edit only involves replacing a single word in a text file.

1.  Open Mixxx Preferences and select the Kontrol S3 in the side list.
2.  You should see a series of tabs at the top of the preferences
    window, one of which is "Scripts". Select that tab.
3.  Select "Traktor-Kontrol-S3-hid-scripts.js". 
4.  Click "Open Selected File."
5.  Either the file should open in an editor, or you should see a file
    browser window with that file selected. If you see a file browser,
    right click the file and select an option to edit it.
6.  At the top of the file will be short instructions explaining what to
    do.
