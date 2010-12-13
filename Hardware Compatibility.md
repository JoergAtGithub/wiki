# Hardware Compatibility

## Controllers

Mixxx can work with any MIDI controller that has drivers for your OS:
you simply need a mapping file to tell Mixxx how to understand it. Mixxx
comes bundled with a number of MIDI mapping presets for the devices
listed below.

There are two different levels of device support in Mixxx:

  - **Mixxx Certified Support** - These mappings are verified by the
    Mixxx Development Team
  - **Community Support** - These mappings are provided by the Mixxx
    Community, but the Mixxx Team is unable to verify their quality
    because we don't have the devices ourselves.

### Mixxx Certified Mappings

|                                                                  |                                         |                            |                                                                                                                                      |
| ---------------------------------------------------------------- | --------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Device                                                           | Windows                                 | Mac OS X                   | Linux                                                                                                                                |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)          | Yes (1.7.0+)                            | Yes (1.7.0+)               | Yes (1.7.0+) [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)    |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)         | Yes (1.7.0+)                            | Yes (1.7.0+)               | Yes (1.7.0+) [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?%20pg=view_files&gid=2&fid=28&pid=215&cid=1#section1) |
| [Hercules DJ Control MP3 e2](Hercules%20DJ%20Control%20MP3%20e2) | Yes (1.8.0+)                            | Yes (1.8.0+)               | Yes (1.8.0+) [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)    |
| [Stanton SCS.3d](Stanton%20SCS.3d)                               | Yes (1.6.1)\[1\] (1.7.0+)               | Yes (1.6.1)\[2\] (1.7.0+)  | Yes (1.7.0+)                                                                                                                         |
| [Stanton SCS.3m](Stanton%20SCS.3m)                               | Yes (1.7.0+)                            | Yes (1.7.0+)               | Yes (1.7.0+)                                                                                                                         |
| [Stanton SCS.1m](Stanton%20SCS.1m)                               | Yes (1.6.1)\[3\] (1.7.0+)\[4\] (1.9.0+) | Yes (1.7.0+)\[5\] (1.9.0+) | Yes (1.6.0+)\[6\]                                                                                                                    |
| [Stanton SCS.1d](Stanton%20SCS.1d)                               | In Progress (1.9.0)                     | In Progress (1.9.0)        | In Progress (1.11.0)                                                                                                                 |
| [DJ TechTools MIDIFighter](http://midifighter.com)               | Yes (1.8.0+)                            | Yes (1.8.0+)               | Yes (1.8.0+)                                                                                                                         |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)               | Yes (1.6.0+)                            | Yes (1.6.0+)               | Yes (1.6.0+)                                                                                                                         |
| [eks Otus](eks%20Otus)                                           | In Progress                             | In Progress                | In Progress                                                                                                                          |

### Community Supported Mappings

These mappings have been verified as working by the Mixxx community.
They might have bugs or rough edges. If you run into issues with these
mappings, please file a bug on our [bug
tracker](http://bugs.launchpad.net/mixxx) or tell us about it on our
mailing list, forums, or IRC channel.

|                                                                                                    |                         |                                                         |                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device                                                                                             | Windows                 | Mac OS X                                                | Linux                                                                                                                                                                                                                                                   |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | Yes (1.8.0+)            | Yes (1.8.0+)                                            | Yes (1.8.0+)                                                                                                                                                                                                                                            |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | Yes (1.7.0+)            | Yes (1.7.0+)                                            | Yes (1.7.0+ ) + [Hercules Linux kernel module](hercules_linux_kernel_module)                                                                                                                                                                            |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | No                      | No                                                      | No\[7\]                                                                                                                                                                                                                                                 |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | Yes (1.7.0+)            | Yes (1.7.0+)                                            | ???                                                                                                                                                                                                                                                     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | Yes (1.7.0+)            | Yes (1.7.0+)                                            | Yes (1.7.0+) + [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?% Apg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                                  |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | Yes (1.8.2+)            | Yes (1.8.2+)                                            | No way to test it \[8\] For any news see [here](http://www.mixxx.org/forums/viewtopic.php?f=1&t=1560)                                                                                                                                                   |
| [Numark MIXTRACK](Numark%20MIXTRACK)                                                               | Yes (1.8.2+)            | Yes (1.8.2+)                                            | Yes (1.8.2+)                                                                                                                                                                                                                                            |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | Yes (1.8.0+)            | Yes (1.8.0+)                                            | Yes (1.8.0+)                                                                                                                                                                                                                                            |
| [Akai MPD24](Akai%20MPD24)                                                                         | Yes (1.8.0+)            | Yes (1.8.0+)                                            | Yes (1.8.0+)                                                                                                                                                                                                                                            |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | Yes (1.8.2+)            | Yes (1.8.2+)                                            | Yes (1.8.2+)                                                                                                                                                                                                                                            |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | Yes (1.6.0+)            | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Numark Total Control](Numark%20Total%20Control)                                                   | Yes (1.6.0+)            | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | Yes (1.6.0+)            | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Mixman DM2](Mixman%20DM2)                                                                         | ?                       | Yes [via MIDI Driver](http://www.joemattiello.com/dm2/) | Yes [ALSA MIDI Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz) [Alternate ALSA MIDI driver (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2) [dm2linux on sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453) |
| [Evolution X-Session](Evolution%20X-Session)                                                       | Yes (1.6.0+)            | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | Yes (1.6.0+)            | Yes (1.6.0+, untested)                                  | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Vestax VCI-100](Vestax%20VCI-100)                                                                 | Yes (1.6.0+)            | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Tascam US-428](Tascam%20US-428)                                                                   | MIDI (1.6.0+, untested) | ?                                                       | Yes\[9\]                                                                                                                                                                                                                                                |
| [Griffin PowerMate](Griffin%20PowerMate)                                                           | No                      | No                                                      | Supported in \<1.6.0                                                                                                                                                                                                                                    |

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

### Devices We Don't Have Mappings For

#### Do you own one of these? Consider contributing back to Mixxx by making a mapping

|                               |
| ----------------------------- |
| Device                        |
| Allen and Heath Xone:1D       |
| Allen and Heath Xone:2D       |
| Allen and Heath Xone:3D       |
| Allen and Heath Xone:4D       |
| Allen and Heath Xone:DX       |
| American Audio VMS4           |
| Ecler Evo4                    |
| Ecler Evo5                    |
| Korg NanoPad                  |
| Korg NanoKontrol              |
| Korg NanoKey                  |
| Korg PadKontrol               |
| Native Instruments Kontrol X1 |
| Native Instruments Kontrol S4 |
| Numark Stealth Control        |
| Numark Omni Control           |
| Numark MixDeck                |
| Numark Mixmeister Control     |
| Numark iDJ2                   |
| Numark NS7                    |
| Numark NSFX                   |
| Numark V7                     |
| Vestax VCI-300                |
| Vestax Spin                   |
| Vestax Typhoon                |
| Vestax TR-1                   |
| Vestax VCM-100                |
| Vestax VCM-600                |

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

### Behringer U-Control UCA202

[Product page](http://www.behringer.com/EN/Products/UCA202.aspx)

This is one of the least expensive yet quality audio interfaces we've
come across and it works fine in Linux, too. It's good for a non-vinyl
control setup (or single-deck if your turntable outputs line level)
since it is very compact and has just enough additional channels. (One
pair for main output and one input pair.) You would then use the
built-in jack on your laptop for the headphone output. (This is how one
of our developers uses it. Below are some screen shots from his Windows
setup showing how to configure ASIO4ALL and Mixxx.)
[[/media/hardware/uca202/asio4all.png|]] [[/media/hardware/uca202/prefs.png|]]

Note that the SoundMAX integrated card only supports 48kHz sampling rate
natively, so the "always resample" box is checked for that card.

### Behringer U-Phono UFO202

[Product page](http://www.behringer.com/EN/Products/UFO202.aspx)

For those wishing to use vinyl control on a budget, you can pick up two
of these devices. Same idea as the UCA202 but these allow you to switch
the input to phono for use with standard turntables. Also good for
archiving your vinyl.

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

1.  DaRouter Required

2.  DaRouter Required

3.  basic support

4.  DaRouter Required

5.  DaRouter Required

6.  with FFADO 2.1

7.  Driver conflict between Linux kernel usbquirks and Herc MIDI driver

8.  hercules mk4 linux MIDI driver missing

9.  Need the latest us428control (launch us428control -m mixxx) and the
    select the US428 mapping in Mixxx's options
