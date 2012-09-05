# General Info

The [Hercules](http://www.hercules.com/us/) PC DJ Consoles are a series
of USB DJ controllers for use with software such as Mixxx.

Hercules is supporting the Mixxx project through donations of their
hardware, we'd like to thank them for that\!

**On 2/16/2009, Hercules released Linux MIDI drivers for their DJ
products. Download: [Hercules Linux Driver
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)**

## Drivers / Supportability

### What is the state of Hercules device support for the different Hercules DJ Consoles?

  - On Windows/OSX/Linux you can use any of Mk1, MP3 Control, Mk2, RMX,
    DJ Steel Control via MIDI or as a HID with Mixxx 1.11+. 
  - These devices are remappable via the XML config files that
    correspond to their names. 
  - LED support works with scripts.

### Are Hercules devices USB-MIDI class compliant?

  - None of the Hercules devices from Mk1 to RMX are USB-MIDI class
    compliant, they require OS MIDI drivers, which are available for
    Windows, Linux and OSX.

### My Hercules Mk1/RMX doesn't work with Mixxx on Linux

  - If you have Linux you need the Hercules Linux driver installed. 
  - The Mk1 needs a modified dynamic kernel module for the Herc MIDI
    driver.

### Does the Joystick on the Mk1/Control MP3/Mk2 work in Mixxx?

  - The hercules joysticks are HID mice used to navigate library and
    playlists, they have been superseded by direction buttons on the RMX
    and DJ Steel controllers.
  - The joystick driver may mess with the MIDI driver.

## Hardware Models

Currently, there are 5 different models:

  - Hercules DJ Console MK1 - controller with a built in 4-channel
    soundcard. (1 input, 3 outputs.) 
  - Hercules DJ Console MK2 - controller with a built in 4-channel
    soundcard. (2 inputs, 2 outputs.) 
  - Hercules DJ Console RMX - supported in Mixxx with a built in
    4-channel soundcard. (2 inputs, 2 outputs.)

The MK2 and RMX have headphone ports for monitoring (configure
headphones for channels 3-4)

  - Hercules DJ Control MP3 - Very similar to the MK2, but without the
    built-in soundcard. It's also significantly cheaper.
  - Hercules DJ Console Mac Edition - Same as the MK1, slightly
    different MIDI mapping file in Mixxx.

Mixxx's support for the Hercules controllers is described on our
[hardware compatibility](hardware_compatibility) page.

## Pictures

[[/media/hardware/hercules_dj_console_mk2.jpg|]] The 1st Hercules DJ Console
(Mk1, but Mac/MK2/Control MP3 versions are all similar looking).

[[/media/hardware/hercules_dj_console_rmx.jpg|]] The Hercules DJ Console RMX
(April 2008).
