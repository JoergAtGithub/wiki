# Hardware Compatibility

## Controllers

The following is a list of hardware controllers that are known to work
with Mixxx. Mixxx comes bundled with MIDI mapping presets for the
devices that are listed as working below.

|                                                                 |                              |                                                         |                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device                                                          | Windows                      | Mac OS X                                                | Linux                                                                                                                                                                                                                                                   |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)       | Yes (1.6.1 +Herc Untested)   | Yes (1.6.1 +Herc Untested)                              | Yes (1.6.1+Herc Untested) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                        |
| [Hercules DJ Console RMX](Hercules%20PC%20DJ%20Console)         | Yes (1.6.1 +Herc)            | Yes (1.6.1 +Herc Untested)                              | Yes (1.6.1+Herc) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                                 |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)         | Yes (1.6.0)                  | Yes (1.6.0)                                             | No - driver conflict between Linux kernel usbquirks and Herc MIDI driver                                                                                                                                                                                |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)         | Yes (1.6.1 +Herc Untested)   | Yes (1.6.1 +Herc Untested)                              | Yes (1.6.1+Herc Untested) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                        |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console) | Yes (1.6.0)                  | Yes (1.6.0)                                             | ???                                                                                                                                                                                                                                                     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)               | Yes (1.6.1 +Herc Untested)   | Yes (1.6.1 +Herc Untested)                              | Yes (1.6.1+Herc) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                                 |
| [Stanton SCS.1m](Stanton%20SCS.1m)                              | Yes (1.6.1) \[1\] (1.7.0)    | Yes (1.7.0 Beta2, untested) \[2\] (1.7.0, untested)     | 1.6.0 \[3\]                                                                                                                                                                                                                                             |
| [Stanton SCS.1d](Stanton%20SCS.1d)                              | In Progress                  | In Progress                                             | Waiting on [FFADO](http://www.ffado.org/) support                                                                                                                                                                                                       |
| [Stanton SCS.3d](Stanton%20SCS.3d)                              | Yes (1.6.1)\[4\] (1.7.0)     | Yes (1.6.1)\[5\] (1.7.0)                                | Yes (1.7.0)                                                                                                                                                                                                                                             |
| [Stanton SCS.3m](Stanton%20SCS.3m)                              | Waiting for programming info | Ditto                                                   | Ditto                                                                                                                                                                                                                                                   |
| [Mixman DM2](Mixman%20DM2)                                      | ?                            | Yes [via MIDI Driver](http://www.joemattiello.com/dm2/) | Yes [ALSA MIDI Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz) [Alternate ALSA MIDI driver (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2) [dm2linux on sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453) |
| [Tascam US-428](Tascam%20US-428)                                | MIDI (1.6.0, untested)       | ?                                                       | Yes, you need the latest us428control (launch us428control -m mixxx) and the select the US428 mapping in Mixxx's options                                                                                                                                |
| [Griffin PowerMate](Griffin%20PowerMate)                        | No                           | No                                                      | Supported in \<1.6.0                                                                                                                                                                                                                                    |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)              | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             |
| [Evolution X-Session](Evolution%20X-Session)                    | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             |
| [M-Audio Xponent](M-Audio%20Xponent)                            | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             |
| [FaderFox DJ2](FaderFox%20DJ2)                                  | Yes (1.6.0)                  | Yes (1.6.0, untested)                                   | Yes (1.6.0)                                                                                                                                                                                                                                             |
| [Vestax VCI-100](Vestax%20VCI-100)                              | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             |
| [Numark Total Control](Numark%20Total%20Control)                | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             |
| [Behringer BCD3000](Behringer%20BCD3000)\[6\]                   | Yes (1.6.0, untested)        | Yes (1.6.0, untested)                                   | Yes (1.6.0)                                                                                                                                                                                                                                             |

Please do not modify this list unless a MIDI mapping preset for a new
controller has been added to Mixxx and it has been tested by at least
one user and developer.

Please note that any DJ controller which is a standard MIDI device can
be made to work with Mixxx via our mapping system. Simple controllers
can be mapped from inside Mixxx using our MIDI learning feature, though
more complicated devices may require additional editing by hand of a
mapping XML file or script file. For more information, please see our
[MIDI Controller Mapping File
Format](MIDI%20Controller%20Mapping%20File%20Format) and our [MIDI
Scripting](MIDI%20Scripting) pages.

## Sound cards

Mixxx is generally compatible with all sound cards that are supported by
the host operating system.

### On Linux

Linux generally has very good support for sound cards, but if you'd like
to see if there's any known issues with any sound card, take a look at
the [ALSA sound card
matrix](http://www.alsa-project.org/main/index.php/Matrix:Main). Also
see [Soundcard resources for Linux
DJs](http://www.pogo.org.uk/~mark/linuxdj/), courtesy of Mark Hills, the
author of [xwax](http://www.xwax.co.uk/). If you have a Firewire/IEEE
1394 interface, you'll want to look at [the FFADO
project](http://www.ffado.org).

### Creative Soundblaster Audigy NX, SE/Value and Creative X-Fi

For both sound cards, ASIO is the best "Sound API" setting to use in
Mixxx's preferences, as it enables you to use all the channels on the
sound card for output. For more information, see [this
thread](https://sourceforge.net/forum/forum.php?thread_id=1649679&forum_id=156157).

While the Audigy NX works well on Linux, **the Creative X-Fi is
currently incompatible with Linux**. Creative says they're releasing a
[closed-source driver](http://opensource.creative.com/soundcard.html) in
the ~~second~~ third or fourth quarter of 2007, but closed-source
drivers often lead to headaches, so Mixxx users might be best to steer
clear of these cards.

The cheaper Creative Audigy cards on the market currently (usually
billed as the Audigy SE or Value) do not correctly support input under
Linux, and while they have the required number of inputs for vinyl
control, are not a good budget choice. Several users have had problems
with these cards generally under Linux, and with Mixxx in particular.
The driver/chipset of note is CA0106 in the [ALSA sound card
matrix](http://www.alsa-project.org/main/index.php/Matrix:Main).

Note: An Audigy LS user reported having to select "surround70" or
"surround50" as the audio devices in Mixxx's preferences in order to be
able to use both Master and Headphone outputs.

## Multiple sound cards

Mixxx 1.6.0+ supports multiple sound cards.

Mixxx 1.5.0 doesn't support multiple output devices that span different
sound cards. For example, if you have two sound cards, you cannot
currently use one sound card for headphone cueing and the other for
master output. However, you **can** use multiple outputs on a single
sound card. For example, if you purchase a cheap 5.1 USB sound card, you
can use the "front" output as your master output, and plug your
headphones into the "rear" output for cueing. This is what the majority
of Mixxx users do.

1.  basic support

2.  basic support

3.  with FFADO 2.1

4.  with DaRouter

5.  with DaRouter

6.  no jogwheels
