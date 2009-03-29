# Hardware Compatibility

We're currently trying to compile a list of support hardware for Mixxx.
If you've tested a hardware controller on a particular operating system,
please update the table below to reflect the state of Mixxx's hardware
support:

|                                                                  |                              |                                                         |                                                                                                                                                                                                                                                         |                    |
| ---------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Device                                                           | Windows                      | Mac OS X                                                | Linux                                                                                                                                                                                                                                                   | Presets Available? |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)        | Yes (1.6.2)                  | Yes (1.6.2)                                             | Yes (1.6.1+Herc) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                                 | Yes - untested     |
| [Hercules DJ Console RMX](Hercules%20PC%20DJ%20Console)          | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.1+Herc) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                                 | Yes                |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)          | Yes (1.6.0)                  | Yes (1.6.0)                                             | No - driver conflict between Linux kernel usbquirks and Herc MIDI driver                                                                                                                                                                                | Yes                |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)          | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.1+Herc) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                                 | Yes                |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)  | Yes (1.6.0)                  | Yes (1.6.0)                                             | ???                                                                                                                                                                                                                                                     | Yes                |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                | Yes (1.6.0, untested)        | Yes (untested)                                          | Yes (1.6.1+Herc) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                                 | Yes                |
| [Stanton SCS.1m](Stanton%20SCS.1m)                               | Yes (1.6.1) \[1\]            | Yes (1.6.1) untested                                    | Waiting on [FFADO](http://www.ffado.org/) support                                                                                                                                                                                                       | Yes                |
| [Stanton SCS.1d](Stanton%20SCS.1d)                               | In Progress                  | In Progress                                             | Waiting on [FFADO](http://www.ffado.org/) support                                                                                                                                                                                                       | No                 |
| [Stanton SCS.3d](Stanton%20SCS.3d)                               | Yes (1.6.1)\[2\] (1.6.2)     | Yes (1.6.1)\[3\] (1.6.2)                                | Yes (1.6.2)                                                                                                                                                                                                                                             | Yes                |
| [Stanton SCS.3m](Stanton%20SCS.3m)                               | Waiting for programming info | Ditto                                                   | Ditto                                                                                                                                                                                                                                                   | No                 |
| [Mixman DM2](Mixman%20DM2)                                       | ?                            | Yes [via MIDI Driver](http://www.joemattiello.com/dm2/) | Yes [ALSA MIDI Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz) [Alternate ALSA MIDI driver (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2) [dm2linux on sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453) | Yes                |
| [Tascam US-428](Tascam%20US-428)                                 | MIDI (1.6.0, untested)       | ?                                                       | Yes, you need the latest us428control (launch us428control -m mixxx) and the select the US428 mapping in Mixxx's options                                                                                                                                | No                 |
| [Griffin PowerMate](Griffin%20PowerMate) **No longer supported** | No                           | No                                                      | Supported in \<1.6.0                                                                                                                                                                                                                                    | No                 |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)               | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             | Yes                |
| [Evolution X-Session](Evolution%20X-Session)                     | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             | Yes                |
| [M-Audio Xponent](M-Audio%20Xponent)                             | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             | Yes                |
| [Ecler NUO4](Ecler%20NUO4)                                       | Yes (1.6.0)                  | Yes (1.6.0, untested)                                   | Yes (1.6.0, untested)                                                                                                                                                                                                                                   | No                 |
| [FaderFox DJ2](FaderFox%20DJ2)                                   | Yes (1.6.0)                  | Yes (1.6.0, untested)                                   | Yes (1.6.0)                                                                                                                                                                                                                                             | Yes                |
| [Vestax VCI-100](Vestax%20VCI-100)                               | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             | Yes                |
| [Numark Total Control](Numark%20Total%20Control)                 | Yes (1.6.0)                  | Yes (1.6.0)                                             | Yes (1.6.0)                                                                                                                                                                                                                                             | Yes                |
| [Behringer BCD3000](Behringer%20BCD3000)\[4\]                    | Yes (1.6.0, untested)        | Yes (1.6.0, untested)                                   | Yes (1.6.0)                                                                                                                                                                                                                                             | Yes                |
| [M-Audio Trigger Finger](M-Audio%20Trigger%20Finger)             | Yes (1.6.0)                  | untested                                                | untested                                                                                                                                                                                                                                                | N/A                |
| [Eks XP5](Eks%20XP5)/[Eks XP10](Eks%20XP10)                      | ?                            | ?                                                       | ?                                                                                                                                                                                                                                                       | No                 |
| [Eks Otus](Eks%20Otus)                                           | Yes\[5\] (untested)          | Yes\[6\] (untested)                                     | Yes\[7\] (untested)                                                                                                                                                                                                                                     | No                 |

# Mixxx Soundcard Compatibility Notes

Mixxx is generally compatible with all sound cards, but here are some
tips our users have given us:

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

2.  with DaRouter

3.  with DaRouter

4.  no jogwheels

5.  Compatible with any software that supports MIDI learn, in Linux/Mac
    OS X/Windows: <http://eks.fi/product.php?p=products&id=35>

6.  Compatible with any software that supports MIDI learn, in Linux/Mac
    OS X/Windows: <http://eks.fi/product.php?p=products&id=35>

7.  Compatible with any software that supports MIDI learn, in Linux/Mac
    OS X/Windows: <http://eks.fi/product.php?p=products&id=35>
