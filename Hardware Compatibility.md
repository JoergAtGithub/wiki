# Hardware Compatibility

We're currently trying to compile a list of support hardware for Mixxx.
If you've tested a hardware controller on a particular operating system,
please update the table below to reflect the state of Mixxx's hardware
support:

|                                                                 |                                                                       |                                                     |                                                                                                                                                                  |
| --------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device                                                          | Windows                                                               | OS X                                                | Linux                                                                                                                                                            |
| [Hercules DJ Console RMX](Hercules%20PC%20DJ%20Console)         | MIDI (untested)                                                       | MIDI (untested)                                     | libDJConsole [BZR](https://code.launchpad.net/~libdjconsole/libdjconsole/trunk) (1.6.0) \[1\]                                                                    |
| [Hercules DJ Console Mk1/Mk2](Hercules%20PC%20DJ%20Console)     | MIDI (1.6.0)                                                          | MIDI (untested)                                     | libDJConsole 0.1.0+ (1.6.0) \[2\]                                                                                                                                |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console) | MIDI (1.6.0)                                                          | MIDI (untested)                                     | libDJConsole 0.1.0+ (1.6.0) \[3\]                                                                                                                                |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)               | MIDI (1.6.0, untested)                                                | MIDI (untested)                                     | HerculesLegacy (1.5.0) \[4\] via /dev/inputX device files                                                                                                        |
| [Mixman DM2](Mixman%20DM2)                                      | ?                                                                     | [via MIDI Driver](http://www.joemattiello.com/dm2/) | [ALSA MIDI Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz) [Alternate ALSA MIDI driver (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2) |
| [Tascam US-428](Tascam%20US-428)                                | MIDI (1.6.0, untested)                                                | ?                                                   | Yes, you need the latest us428control (launch us428control -m mixxx) and the select the US428 mapping in Mixxx's options                                         |
| [Griffin PowerMate](Griffin%20PowerMate)                        | Possibly (code exists for it)                                         | ?                                                   | Full support (jog wheel and light visualization)                                                                                                                 |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)              | Yes (1.6.0)                                                           | Yes (1.6.0)                                         | Yes (1.6.0)                                                                                                                                                      |
| [Evolution X-Session](Evolution%20X-Session)                    | Yes (1.6.0)                                                           | Yes (1.6.0)                                         | Yes (1.6.0)                                                                                                                                                      |
| [M-Audio Xponent](M-Audio%20Xponent)                            | Yes (1.6.0)                                                           | Yes (1.6.0)                                         | Yes (1.6.0)                                                                                                                                                      |
| [Ecler NUO4](Ecler%20NUO4)                                      | Yes (1.6.0)                                                           | Yes (1.6.0, untested)                               | Yes (1.6.0, untested)                                                                                                                                            |
| [FaderFox DJ2](FaderFox%20DJ2)                                  | Yes (1.6.0)                                                           | Yes (1.6.0, untested)                               | Yes (1.6.0)                                                                                                                                                      |
| [Vestax VCI-100](Vestax%20VCI-100)                              | ?                                                                     | ?                                                   | ?                                                                                                                                                                |
| [Numark Total Control](Numark%20Total%20Control)                | Soon                                                                  | Soon                                                | Soon                                                                                                                                                             |
| [Behringer BCD3000](Behringer%20BCD3000)\[5\]                   | Yes (1.6.0, untested)                                                 | Yes (1.6.0, untested)                               | Yes (1.6.0)                                                                                                                                                      |
| [Stanton SC System](http://www.enterthesystem.com/)             | Hopefully soon (waiting on Stanton for programming info & test units) | Hopefully soon                                      | Hopefully soon                                                                                                                                                   |
| [M-Audio Trigger Finger](M-Audio%20Trigger%20Finger)            | Yes (1.6.0)                                                           | untested                                            | untested                                                                                                                                                         |

# Mixxx Soundcard Compatibility Notes

Mixxx is generally compatible with all sound cards, but here's some tips
our users have given us:

## Creative Soundblaster Audigy NX, SE/Value and Creative X-Fi

For both sound cards, ASIO is the best "Sound API" setting to use in
Mixxx's preferences, as it enables you to use all the channels on the
sound card for output. For more information, see [this
thread](https://sourceforge.net/forum/forum.php?thread_id=1649679&forum_id=156157).

While the Audigy NX works well on Linux, **the Creative X-Fi is
currently incompatible with Linux**. Creative says they're releasing a
[closed-source driver](http://opensource.creative.com/soundcard.html) in
the \<strike\>second\</strike\> third or fourth quarter of 2007, but
closed-source drivers often lead to headaches, so Mixxx users might be
best to steer clear of these cards.

The cheaper Creative Audigy cards on the market currently (usually
billed as the Audigy SE or Value) do not correctly support input under
Linux, and while they have the required number of inputs for vinyl
control, are not a good budget choice. Several users have had problems
with these cards generally under Linux, and with Mixxx in particular.
The driver/chipset of note is CA0106 in the [ALSA sound card
matrix](http://www.alsa-project.org/main/index.php/Matrix:Main/).

Note: An Audigy LS user reported having to select "surround70" or
"surround50" as the audio devices in Mixxx's preferences in order to be
able to use both Master and Headphone outputs.

## Linux and Sound cards

Linux generally has very good support for sound cards, but if you'd like
to see if there's any known issues with any sound card, take a look at
the [ALSA sound card
matrix](http://www.alsa-project.org/main/index.php/Matrix:Main/).

## Multiple Sound cards

Mixxx 1.6.0 will support multiple sound cards.

Mixxx 1.5.0 doesn't support multiple output devices that span different
sound cards. For example, if you have two sound cards, you cannot
currently use one sound card for headphone cueing and the other for
master output. However, you **can** use multiple outputs on a single
sound card. For example, if you purchase a cheap 5.1 USB sound card, you
can use the "front" output as your master output, and plug your
headphones into the "rear" output for cueing. This is what the majority
of Mixxx users do.

1.  UI led triggers need to be added to core

2.  UI led triggers need to be added to core

3.  UI led triggers need to be added to core

4.  Mixxx must be compiled with the *SCons djconsole\_legacy=1* option,
    and user must have proper */dev/inputX* permissions to access the
    device. Hercules is currently developing a MIDI driver for their
    products for Linux, and with any luck, we'll be able to support the
    Control MP3 via MIDI in the future.

5.  no jogwheels
