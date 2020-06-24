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

|                                                                  |              |              |                   |                       |
| ---------------------------------------------------------------- | ------------ | ------------ | ----------------- | --------------------- |
| Device                                                           | Windows      | Mac OS X     | Linux             | Integrated Sound Card |
| [American Audio VMS4](American%20Audio%20VMS4)                   | Yes (1.9.0+) | Yes (1.9.0+) | Yes (1.9.0+)      | yes                   |
| [DJ TechTools MIDIFighter](http://midifighter.com)               | Yes (1.8.0+) | Yes (1.8.0+) | Yes (1.8.0+)      | no                    |
| [eks Otus](eks%20Otus)                                           | Yes (1.11.0) | Yes (1.11.0) | Yes (1.11.0)      | no                    |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)          | Yes (1.7.0+) | Yes (1.7.0+) | Yes (1.11+)       | yes                   |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)         | Yes (1.7.0+) | Yes (1.7.0+) | Yes (1.11+)       | yes                   |
| [Hercules DJ Control MP3 e2](Hercules%20DJ%20Control%20MP3%20e2) | Yes (1.9.0+) | Yes (1.9.0+) | Yes (1.11+)       | yes                   |
| [Keith McMillen Instruments QuNeo](keith_mcmillen_quneo)         | Yes (1.11+)  | Yes (1.11+)  | Yes (1.11+)       | no                    |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)               | Yes (1.6.0+) | Yes (1.6.0+) | Yes (1.6.0+)      | no                    |
| [Reloop Terminal Mix4](Reloop%20Terminal%20Mix4)                 | Yes (1.11.0) | Yes (1.11.0) | Yes (1.11.0)      | yes                   |
| [Stanton SCS.3d](Stanton%20SCS.3d)                               | Yes (1.7.0+) | Yes (1.7.0+) | Yes (1.7.0+)      | no                    |
| [Stanton SCS.3m](Stanton%20SCS.3m)                               | Yes (1.7.0+) | Yes (1.7.0+) | Yes (1.7.0+)      | no                    |
| [Stanton SCS.1m](Stanton%20SCS.1m)                               | Yes (1.9.0+) | Yes (1.9.0+) | Yes (1.6.0+)\[1\] | yes                   |
| [Stanton SCS.1d](Stanton%20SCS.1d)                               | Yes (1.9.1)  | Yes (1.9.1)  | Yes (1.11.0)\[2\] | no                    |
| [Vestax VCI-400](Vestax%20VCI-400)                               | Yes (1.10.1) | Yes (1.10.1) | Yes (1.10.1)\[3\] | yes                   |

### Community Supported Mappings

These mappings have been verified as working by the Mixxx community.
They might have bugs or rough edges. If you run into issues with these
mappings, please file a bug on our [bug
tracker](http://bugs.launchpad.net/mixxx) or tell us about it on our
mailing list, forums, or IRC channel.

////

|                                                                                                    |                |                                                         |                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device                                                                                             | Windows        | Mac OS X                                                | Linux                                                                                                                                                                                                                                                   |
| [Akai MPD24](Akai%20MPD24)                                                                         | Yes (1.8.0+)   | Yes (1.8.0+)                                            | Yes (1.8.0+)                                                                                                                                                                                                                                            |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | Yes (1.10.0 +) |                                                         | Yes (1.10.0 +)                                                                                                                                                                                                                                          |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | Yes (1.6.0+)   | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Denon SC2000](http://esync.de/denon-sc2000-mixxx-bindings)                                        | Yes (1.8.0+)   | Untested (1.8.0+)                                       | Yes (1.8.0+)                                                                                                                                                                                                                                            |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                                               | Yes (1.12.0+)  | Yes (1.12.0+)                                           | Yes (1.12.0+)                                                                                                                                                                                                                                           |
| [Evolution X-Session](Evolution%20X-Session)                                                       | Yes (1.6.0+)   | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | Yes (1.6.0+)   | Yes (1.6.0+, untested)                                  | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | Yes (1.7.0+)   | Yes (1.7.0+)                                            | Yes (1.7.0+ ) + \[4\] [Hercules Linux kernel module](hercules_linux_kernel_module)                                                                                                                                                                      |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | Yes (1.11.0)   | Yes (1.11.0)                                            | Yes (1.11.0)                                                                                                                                                                                                                                            |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | Yes (1.7.0+)   | Yes (1.7.0+)                                            | ???                                                                                                                                                                                                                                                     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | Yes (1.7.0+)   | Yes (1.7.0+)                                            | Yes (1.7.0+) + \[5\] [Hercules Linux MIDI Driver](http://ts.hercules.com/eng/index.php?% Apg=view_files&gid=2&fid=28&pid=215&cid=1#section1)                                                                                                            |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | Yes (1.8.2+)   | Yes (1.8.2+)                                            | Yes (1.12.0+) + \[6\] See [here](http://mixxx.org/forums/viewtopic.php?f=3&t=5064&start=10#p19358)                                                                                                                                                      |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | Yes (1.8.0+)   | Yes (1.8.0+)                                            | Yes (1.8.0+)                                                                                                                                                                                                                                            |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | Yes (1.6.0+)   | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Mixman DM2](Mixman%20DM2)                                                                         | ?              | Yes [via MIDI Driver](http://www.joemattiello.com/dm2/) | Yes [ALSA MIDI Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz) [Alternate ALSA MIDI driver (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2) [dm2linux on sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453) |
| [Novation Dicer](novation_dicer)                                                                   | Yes (1.10.0+)  | Yes (1.10.0+)                                           | Yes (1.10.0+)                                                                                                                                                                                                                                           |
| [Numark Total Control](Numark%20Total%20Control)                                                   | Yes (1.6.0+)   | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | Yes (1.8.0+)   | Yes (1.8.0+)                                            | Yes (1.8.0+)                                                                                                                                                                                                                                            |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | Yes (1.8.0+)   | Yes (1.8.0+)                                            | No \[7\]                                                                                                                                                                                                                                                |
| [Numark MIXTRACK](Numark%20MIXTRACK)                                                               | Yes (1.8.2+)   | Yes (1.8.2+)                                            | Yes (1.8.2+)                                                                                                                                                                                                                                            |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | Yes (1.10.0+)  | ?                                                       | Yes (1.10.0+)                                                                                                                                                                                                                                           |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | ?              | ?                                                       | Yes (1.11.0+)                                                                                                                                                                                                                                           |
| [Numark NS7](Numark%20NS7)                                                                         | Yes (1.9.0+)   | Yes (1.9.0+)                                            | No Driver (1.9.0+)                                                                                                                                                                                                                                      |
| [Numark DJ2GO](Numark%20DJ2GO) \[8\]                                                               | ?              | Yes (1.10.0)                                            | Yes (1.10.1)                                                                                                                                                                                                                                            |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | Yes (1.8.2+)   | Yes (1.8.2+)                                            | Yes (1.8.2+)                                                                                                                                                                                                                                            |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | Yes (1.10.0+)  | Yes (1.10.0+)                                           | Unknown (1.10.0+)                                                                                                                                                                                                                                       |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | Yes (1.10.0+)  | Yes (1.10.0+)                                           | Unknown (1.10.0+)                                                                                                                                                                                                                                       |
| [Vestax VCI-100](Vestax%20VCI-100)                                                                 | Yes (1.6.0+)   | Yes (1.6.0+)                                            | Yes (1.6.0+)                                                                                                                                                                                                                                            |
| [Vestax VCI-300](vestax_vci-300)                                                                   | Yes (1.11.0+)  | Yes (1.11.0+)                                           | Yes (1.11.0+)                                                                                                                                                                                                                                           |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | Yes (1.9.0+)   | Yes (1.9.0+)                                            | Yes (1.9.0+)                                                                                                                                                                                                                                            |
| [Vestax Spin](Vestax%20Spin)                                                                       | Yes (1.9.0+)   | Yes (1.9.0+)                                            | Yes (1.9.0+)                                                                                                                                                                                                                                            |

Please keep the list in alphabetical order and do not modify this list
unless a MIDI mapping preset for a new controller has been added to
Mixxx and it has been tested by at least one user and developer.

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

|                                                  |                         |                         |                                   |
| ------------------------------------------------ | ----------------------- | ----------------------- | --------------------------------- |
| Device                                           | Windows                 | Mac OS X                | Linux                             |
| Allen and Heath Xone:1D                          |                         |                         |                                   |
| Allen and Heath Xone:2D                          |                         |                         |                                   |
| Allen and Heath Xone:3D                          |                         |                         |                                   |
| Allen and Heath Xone:4D                          |                         |                         |                                   |
| Allen and Heath Xone:DX                          |                         |                         |                                   |
| Ecler Evo4                                       |                         |                         |                                   |
| Ecler Evo5                                       |                         |                         |                                   |
| EKS Otus Dualdeck                                |                         |                         |                                   |
| EKS Otus Plus                                    |                         |                         |                                   |
| EKS Otus RAW                                     |                         |                         |                                   |
| [EKS XP5](EKS%20XP5)                             |                         |                         |                                   |
| [EKS XP10](EKS%20XP10)                           |                         |                         |                                   |
| Korg NanoPad                                     |                         |                         |                                   |
| [Korg NanoKontrol](/wiki/dokuwiki)               | Yes (1.10.0+)           |                         |                                   |
| Korg NanoKey                                     |                         |                         |                                   |
| Korg PadKontrol                                  |                         |                         |                                   |
| M-AUDIO Torq Conectiv CD                         |                         |                         |                                   |
| M-AUDIO Torq Conectiv Vinyl                      |                         |                         |                                   |
| Native Instruments Traktor Kontrol D2            |                         |                         |                                   |
| Native Instruments Traktor Kontrol F1 (HID)      |                         |                         |                                   |
| Native Instruments Traktor Kontrol X1 Mk1        | possible with MIDI mode | possible with MIDI mode | see note                          |
| Native Instruments Traktor Kontrol X1 Mk2 (HID)  |                         |                         |                                   |
| Native Instruments Traktor Kontrol S2 Mk1        | possible with MIDI mode | possible with MIDI mode | see note                          |
| Native Instruments Traktor Kontrol S2 Mk2 (HID)  |                         |                         |                                   |
| Native Instruments Traktor Kontrol S4 Mk 1       | possible with MIDI mode | possible with MIDI mode | Sound card should work. See note. |
| Native Instruments Traktor Kontrol S4 Mk 2 (HID) |                         |                         |                                   |
| Native Instruments Traktor Kontrol S8            | possible with MIDI mode | possible with MIDI mode | see note                          |
| Native Instruments Traktor Kontrol Z1 (HID)      |                         |                         |                                   |
| Native Instruments Traktor Kontrol Z2 (HID)      |                         |                         |                                   |
| Numark Stealth Control                           |                         |                         |                                   |
| Numark Omni Control                              |                         |                         |                                   |
| Numark MixDeck                                   |                         |                         |                                   |
| Numark Mixmeister Control                        |                         |                         |                                   |
| Numark iDJ3                                      |                         |                         |                                   |
| Numark NSFX                                      |                         |                         |                                   |
| Numark V7                                        |                         |                         |                                   |
| Rane TTM 57SL                                    |                         |                         |                                   |
| Vestax TR-1                                      |                         |                         |                                   |
| Vestax VCM-100                                   |                         |                         |                                   |
| Vestax VCM-600                                   |                         |                         |                                   |

#### Note about Native Instruments controllers

Native Instruments' newer DJ controllers are standard HID devices. The
Windows and Mac OS X drivers can translate the HID signals to MIDI, but
this is not available on GNU/Linux. So, if you make a mapping for these
controllers, please make an HID mapping so it is compatible with every
OS that Mixxx runs on.

Native Instruments' older DJ controllers use a proprietary protocol
called NHL that Mixxx does not support. The Windows and Mac OS X drivers
can switch these controllers to a MIDI mode by pressing certain buttons
(see [the Native Instruments
website](https://www.native-instruments.com/en/support/knowledge-base/show/3659/how-to-use-your-native-instruments-controller-in-midi-mode/)
for the button combination for each controller), which could be mapped
to Mixxx. Unfortunately, because this is done by the driver and not the
controller firmware, these controllers cannot be used as MIDI
controllers on GNU/Linux. However, the snd-usb-caiaq driver in Linux
supports the audio interfaces in at least some of these devices. It also
registers the signals from the controllers as generic Linux input
events. To get these devices to work with Mixxx on GNU/Linux, either the
driver would need to translate these signals to HID or MIDI, Mixxx would
need to be able to read Linux input events, or a program would need to
translate the Linux input events to HID or MIDI.

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

### Traktor Audio 2

See [this page](traktor_audio_2)

### Native Instruments Audio Kontrol 1

Sound works perfect with additional .asoundrc file. Hardware buttons and
wheel works with additional MIDI mapper program. See [this
page](audio_kontrol_1).

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

### Edirol Firewire FA-101

[Product page](http://www.roland.com/products/en/FA-101/)

Not a budget sound card, but provides plenty of inputs and outputs for
vinyl and external mixers. These are Mono channels though, so you must
select pairs of them in the channel menu. Latency can be reduced to 1ms
with an ocasional hiccup, or kept at 2ms for reliability. A usual setup
would be to set the main outputs (1/2) to headphones, since Monitor
channels are not supported, and to get a stereo output on them. You
could then use the remaining outputs as individual decks. A very
flexible soundcard, that supports many sample rates. Requires a firewire
connection.

### SYBA SD-CM-UAUD

Reported on IRC as working well for using Mixxx in Linux. Available for
about $10 USD.

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

1.  Linux kernel 3.8 and up

2.  Linux kernel 3.8 and up

3.  tested 2015-01-01 with 1.12.0-alpha (build master r5096), but
    previous versions should work as well

4.  official driver must be patched to support kernels \> 2.6.30 see
    <http://mixxx.org/forums/viewtopic.php?f=1&t=851>

5.  official driver must be patched to support kernels \> 2.6.30 see
    <http://mixxx.org/forums/viewtopic.php?f=1&t=851>

6.  no need for special hercules driver.

7.  No Linux MIDI Driver

8.  Mapping included with 1.12
