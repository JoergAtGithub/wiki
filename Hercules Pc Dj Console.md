# Drivers / Supportability / Recommendation FAQ

Preface - As a vendor, Hercules has been good about supporting the Mixxx
project through donations of their hardware. We'd like to thank them for
that support and encourage you to consider their goodwill towards Mixxx
when you are weighing your options. ;-)

Now onto the meat... **On 2/16/2009, Hercules released Linux MIDI
drivers for all of their DJ product. Download them here [Hercules
Technical Support](http://ts.hercules.com)**

## Drivers / Supportability

### What is the state of Hercules device support for the different Hercules DJ Consoles?

  - On Windows/OSX you can use any of Mk1, MP3 Control, Mk2, RMX, DJ
    Steel Control via MIDI. These devices are remappable via the XML
    config files that correspond to their names. LED support doesn't
    work all that reliably though (this is a Mixxx problem not a driver
    or hardware problem).
  - On Linux, all devices should work with the Mk1 provided you have
    Mixxx 1.6.1+Herc and the [Hercules Linux
    Drivers](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1).
    The Mk1 needs the kernel maintainer to remove the USBQuirks put in
    for the Mk1 which interfere with the Herc MIDI driver.

### Are Hercules devices USB-MIDI class compliant?

  - Nope, none of the Hercules devices from Mk1 to RMX are USB-MIDI
    class compliant. They all require OS MIDI drivers to do MIDI.
    Fortunately MIDI drivers are available for Windows, Linux and OSX.

### My Hercules RMX doesn't work with Mixxx on Linux

  - If you are using Mixxx 1.6.1, you need to get the +Herc pack from
    the [downloads](http://mixxx.org/downloads/) page. If you have Linux
    you need 1.6.1+Herc and the Hercules Linux driver installed.

### Does the Joystick on the Mk1/Control MP3/Mk2 work in Mixxx?

  - No and it never will. The hercules joysticks are very imprecise mice
    that overshoot all the time, they are in no way helpful because of
    that and have been superseded by direction buttons on the RMX and DJ
    Steel controllers, these work much better and are used to navigate
    library and playlists.
  - If you load the joystick driver you may get an error message that
    libDJConsole can not communicate with your DJ Console, because the
    kernel sees it as one device you can only use either the joystick OR
    the rest of the console via libDJConsole, to fix it ditch the
    joystick driver.

## Recommendation

### Which one should I buy?

  - Cost and function should drive your decision. They all work pretty
    well, the RMX has a better sound output at low volume but is heavier
    then the others by quite bit (it's solid metal vs. the others which
    are plastic).
  - The Mk1 is quite old and though it can be made to work with previous
    builds of Mixxx on Linux, we would not recommend it until the
    problem with the MIDI Drivers and USBQuirks gets sorted out and it
    can supported.

# General Info

The Hercules PC DJ Consoles are a series of USB DJ controllers for use
with software such as Mixxx.

Link to website: <http://www.hercules.com/us/>

## Hardware Models

Currently, there are 5 different models:

  - Hercules DJ Console MK2 - Very popular controller with a built in
    4x4 soundcard. (Two inputs, two outputs.) 
  - Hercules DJ Console MK1 - Same as the MK2, but much older. Linux
    MIDI driver does not work because of USB Quirks kernel conflict.
  - Hercules DJ Control MP3 - Very similar to the MK2, but without the
    built-in soundcard. It's also significantly cheaper.
  - Hercules DJ Console Mac Edition - Same as the MK2, slightly
    different MIDI mapping file in Mixxx.
  - Hercules DJ Console RMX - supported in Mixxx - Thanks Francois @
    Hercules\!

Mixxx's support for the Hercules controllers is described on our
[hardware compatibility](hardware_compatibility) page.

## Pictures

[[/media/hardware/hercules_dj_console_mk2.jpg|]] The Hercules DJ Console MK2.
The Mac Edition and Control MP3 versions are very similar.

[[/media/hardware/hercules_dj_console_rmx.jpg|]] The Hercules DJ Console RMX.
Release date is April 2008.
