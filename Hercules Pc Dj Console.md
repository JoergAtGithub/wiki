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

  - On Windows/OSX you can use any of Mk1, Control MP3, Mk2, or RMX via
    MIDI. These devices are remappable via the XML config files that
    correspond to their names. LED support doesn't work all that
    reliably though (this is a Mixxx problem not a driver or hardware
    problem).
  - On Linux, you can use the MK1/MK2/MP3/RMX/Steel via the official
    MIDI driver for Linux. Download it at [Hercules Technical
    Support](http://ts.hercules.com).

### Are Hercules devices USB-MIDI class compliant?

  - Nope, none of the Hercules devices from Mk1 to RMX are USB-MIDI
    class compliant. They all require OS MIDI drivers to do MIDI.

### My Hercules RMX doesn't work with Mixxx on Linux

  - You need to have libDJConsole 0.1.3 (which as of Aug 2008 is only
    available from the bzr source repo on launchpad)

### My Hercules device only works as root

  - Check that you have the correct udev rules for the DJ Console
    devices (these are part of libDJConsole or libdjconsole-data on
    Ubuntu).

### Does the Joystick on the Mk1/Control MP3/Mk2 work in Mixxx?

  - No and it never will. The hercules joysticks are very imprecise mice
    that overshoot all the time, they are in no way helpful because of
    that and have been superseded by direction buttons (which are
    supported by Mixxx/libDJConsole), these work much better and are
    used to navigate library and playlists.
  - If you load the joystick driver you may get an error message that
    libDJConsole can not communicate with your DJ Console, because the
    kernel sees it as one device you can only use either the joystick OR
    the rest of the console via libDJConsole, to fix it ditch the
    joystick driver.

### Will there ever be MIDI drivers for Hercules devices on Linux?

  - We are in the process of testing drivers supplied by
    Hercules/Guillemot that will be released when they are deemed to be
    stable. This will mean that all Herc devices appear as MIDI on
    Linux. Currently they are working well, and will hopefully be
    released in the very short term. When that happens, this page will
    get a bit of an overhaul.

## Recommendation

### Which one should I buy?

  - On Windows or OSX: cost and function should drive your decision.
    They all work pretty well, the RMX has a better sound output at low
    volume but is heavier then the others by quite bit (it's solid metal
    vs. the others which are plastic).
  - On Linux: Unless Hercules releases a MIDI driver I can not recommend
    the Control MP3 as it can only be used via the legacy hack (you will
    have to build Mixxx from source and turn it on). The Mk1 is quite
    old and though it works via the libDJConsole hack, it seems the
    least likely to have a MIDI driver written for it by Hercules. That
    leaves the Mk2 and the RMX which are both decently supported by
    libDJConsole and seem to have the best chance at this point of their
    product lifetime of seeing a vendor MIDI driver.

# General Info

The Hercules PC DJ Consoles are a series of USB DJ controllers for use
with software such as Mixxx.

Link to website: <http://www.hercules.com/us/>

## Hardware Models

Currently, there are 5 different models:

  - Hercules DJ Console MK2 - Very popular controller with a built in
    4x4 soundcard. (Two inputs, two outputs.) 
  - Hercules DJ Console MK1 - Same as the MK2, but much older.
  - Hercules DJ Control MP3 - Very similar to the MK2, but without the
    built-in soundcard. It's also significantly cheaper.
  - Hercules DJ Console Mac Edition - Same as the MK2, slightly
    different MIDI mapping file in Mixxx.
  - Hercules DJ Console RMX - Next-generation Hercules controller,
    release date is April 2008. ~~Will be supported in Mixxx if we can
    get our hands on one.~~ Supported, Thanks Francois @ Hercules\!

Mixxx's support for the Hercules controllers is described on our
[hardware compatibility](hardware_compatibility) page.

## Pictures

[[/media/hardware/hercules_dj_console_mk2.jpg|]] The Hercules DJ Console MK2.
The Mac Edition and Control MP3 versions are very similar.

[[/media/hardware/hercules_dj_console_rmx.jpg|]] The Hercules DJ Console RMX.
Release date is April 2008.
