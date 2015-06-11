# Hardware Compatibility

Because Mixxx is [free
software](http://www.gnu.org/philosophy/free-sw.html) — free as in
freedom, not just price — we strive to make it work with as much
hardware as we can. If hardware does not work with Mixxx, that does not
mean it is impossible, it only means that no one has made it work with
Mixxx yet. Anyone, including you, who has the hardware is welcome to
make Mixxx work with it.

Mixxx works with any sound card that your operating system has a driver
to use.

Standards compliant MIDI controllers do not need any special drivers on
Linux, Mac OS X, or Windows. Standards compliant HID controllers do not
need any special drivers on Linux and Mac OS X, but do require drivers
on Windows. Controllers that have integrated sound cards require a
driver on every OS for the sound card.

## Controller mappings

Mixxx can be made to work with any standards compliant USB MIDI or USB
HID controller by mapping the controller's signals to manipulate
controls in Mixxx. The Mixxx developers and community have made a number
of mappings for MIDI and HID controllers. There are two different levels
of controller support in Mixxx:

  - Mixxx Certified Support: mappings verified by the Mixxx Development
    Team
  - Community Support: mappings provided by the Mixxx Community, but the
    Mixxx Team is unable to verify their quality because we don't have
    the devices ourselves.

If your controller does not have a mapping, or the mapping for your
controller does not work how you would like it to, please consider
contributing to Mixxx by making one and sharing it [on the
forums](http://mixxx.org/forums/viewforum.php?f=7). Within Mixxx, you
can easily map any MIDI controller with the MIDI Learning Wizard
available in Preferences \> Controllers (this does not (yet) work for
HID devices). For jog wheels and other advanced functions, you will need
to program a JavaScript mapping. See [these wiki
pages](start#controller%20midi%20mapping%20documentation) for
documentation on making and editing controller mappings.

If you notice any bugs in the mappings, or wish the mapping would work
differently, please [report it on our bug tracker](reporting%20bugs).

### Mixxx Certified Mappings

|                                                                  |                       |                 |                               |
| ---------------------------------------------------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                                           | Integrated Sound Card | Signal protocol | Supported since Mixxx version |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)           | yes                   | MIDI            | 1.11                          |
| [American Audio VMS4](American%20Audio%20VMS4)                   | yes                   | MIDI            | 1.9                           |
| [DJ TechTools MIDIFighter](http://midifighter.com)               | no                    | MIDI            | 1.8                           |
| [eks Otus](eks%20Otus)                                           | no                    | HID             | 1.11 \[1\]                    |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)          | yes                   | HID             | 1.11                          |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)         | yes                   | HID             | 1.11                          |
| [Hercules DJ Control MP3 e2](Hercules%20DJ%20Control%20MP3%20e2) | yes                   | HID             | 1.11                          |
| [Keith McMillen Instruments QuNeo](keith_mcmillen_quneo)         | no                    | MIDI            | 1.11                          |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)               | no                    | MIDI            | 1.6 \[2\]                     |
| [Reloop Terminal Mix4](Reloop%20Terminal%20Mix4)                 | yes                   | MIDI            | 1.11                          |
| [Stanton SCS.3d](Stanton%20SCS.3d)                               | no                    | MIDI            | 1.7                           |
| [Stanton SCS.3m](Stanton%20SCS.3m)                               | no                    | MIDI            | 1.7                           |
| [Stanton SCS.1m](Stanton%20SCS.1m)                               | yes                   | MIDI            | 1.9 \[3\]                     |
| [Stanton SCS.1d](Stanton%20SCS.1d)                               | no                    | MIDI            | 1.9.1 \[4\]                   |
| [Vestax VCI-400](Vestax%20VCI-400)                               | yes                   | MIDI            | 1.10.1 \[5\]                  |

### Community Supported Mappings

All controllers listed on GNU/Linux, Mac OS X, and Windows unless
otherwise indicated. If your controller is listed here but does not work
with your OS, please [report the bug](reporting%20bugs).

|                                                                                                    |                       |                 |                               |
| -------------------------------------------------------------------------------------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                                                                             | Integrated sound card | Signal protocol | Supported since Mixxx version |
| [Akai MPD24](Akai%20MPD24)                                                                         | no                    | MIDI            | 1.8                           |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | no                    | MIDI            | 1.10                          |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | yes                   | MIDI            | 1.6                           |
| [Denon SC2000](http://esync.de/denon-sc2000-mixxx-bindings)                                        | no                    | MIDI            | 1.8                           |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                                               | yes                   | MIDI            | 1.12                          |
| [Evolution X-Session](Evolution%20X-Session)                                                       | no                    | MIDI            | 1.6 \[6\]                     |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | no                    | MIDI            | 1.6                           |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | no                    | HID             | 1.11                          |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | yes                   | HID             | 1.11 \[7\]                    |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | yes                   | HID?            | 1.7 \[8\]                     |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | yes                   | HID             | 1.8 \[9\]                     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | no                    | HID             | 1.11                          |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | no                    | MIDI            | 1.8                           |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | yes                   | MIDI            | 1.6                           |
| [Mixman DM2](Mixman%20DM2)                                                                         | yes                   | ?               | 1.7 \[10\]\[11\]              |
| [Novation Dicer](Novation%20Dicer)                                                                 | no                    | MIDI            | 1.10                          |
| [Numark Total Control](Numark%20Total%20Control)                                                   | no                    | MIDI            | 1.6                           |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | yes                   | MIDI            | 1.8                           |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | yes                   | ?               | 1.8 \[12\]                    |
| [Numark Mixtrack](Numark%20Mixtrack)                                                               | no                    | MIDI            | 1.8.2                         |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | yes                   | MIDI            | 1.10                          |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | yes                   | MIDI            | 1.11                          |
| [Numark NS7](Numark%20NS7)                                                                         | yes                   | MIDI            | 1.9 \[13\]                    |
| [Numark DJ2GO](Numark%20DJ2GO)                                                                     | no                    | MIDI            | 1.10                          |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | no                    | MIDI or HID     | 1.8.2 (MIDI)                  |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | no                    | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | no                    | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Vestax VCI-100](Vestax%20VCI-100)                                                                 | yes                   | MIDI            | 1.6 \[14\]                    |
| [Vestax VCI-300](Vestax%20VCI-300)                                                                 | yes                   | MIDI            | 1.11 \[15\]                   |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | yes                   | MIDI            | 1.9 \[16\]                    |
| [Vestax Spin](Vestax%20Spin)                                                                       | yes                   | MIDI            | 1.9 \[17\]                    |

Please keep the list in alphabetical order and do not modify this list
unless a MIDI mapping preset for a new controller has been added to
Mixxx and it has been tested by at least one user and developer.

### Devices We Don't Have Mappings For

#### Do you own one of these? Consider contributing back to Mixxx by making a mapping

|                                           |                       |                 |
| ----------------------------------------- | --------------------- | --------------- |
| Device                                    | Integrated sound card | Signal protocol |
| Akai Pro AMX                              | yes                   | MIDI            |
| Gemini Slate                              | yes                   | MIDI            |
| Gemini Slate 4                            | yes                   | MIDI            |
| Hercules DJ Control Jogvision             | yes                   | MIDI            |
| Korg KAOSS DJ                             | yes                   | MIDI            |
| Native Instruments Traktor Kontrol D2     | no                    | ?               |
| Native Instruments Traktor Kontrol F1     | no                    | HID             |
| Native Instruments Traktor Kontrol X1 Mk1 | no                    | NHL             |
| Native Instruments Traktor Kontrol X1 Mk2 | no                    | HID             |
| Native Instruments Traktor Kontrol S2 Mk1 | yes                   | NHL             |
| Native Instruments Traktor Kontrol S2 Mk2 | yes                   | HID             |
| Native Instruments Traktor Kontrol S4 Mk1 | yes                   | NHL             |
| Native Instruments Traktor Kontrol S4 Mk2 | yes                   | HID             |
| Native Instruments Traktor Kontrol S8     | yes                   | NHL             |
| Native Instruments Traktor Kontrol Z1     | yes                   | HID             |
| Native Instruments Traktor Kontrol Z2     | yes                   | HID             |
| Numark Mixdeck                            | yes                   | MIDI            |
| Numark Mixdeck Expresss                   | yes                   | MIDI            |
| Numark Mixdeck Quad                       | yes                   | MIDI            |
| Numark Mixtrack Edge                      | no                    | MIDI            |
| Numark Mixtrack 3                         | no                    | MIDI            |
| Numark Mixtrack Pro 3                     | yes                   | MIDI            |
| Numark Mixtrack Quad                      | yes                   | MIDI            |
| Numark N4                                 | yes                   | MIDI            |
| Numark NS6                                | yes                   | MIDI            |
| Numark NS7II                              | yes                   | MIDI            |
| Numark NS7III                             | yes                   | MIDI            |
| Numark NV                                 | yes                   | MIDI            |
| Numark NSFX                               | no                    | ?               |
| Numark Orbit                              | no                    | MIDI            |
| Numark V7                                 | yes                   | MIDI            |
| Pioneer DDJ Ergo                          | yes                   | MIDI            |
| Pioneer DDJ-S1                            | yes                   | MIDI            |
| Pioneer DDJ-SB                            | yes                   | MIDI            |
| Pioneer DDJ-SR                            | yes                   | MIDI            |
| Pioneer DDJ-SX                            | yes                   | MIDI            |
| Pioneer DDJ-SX2                           | yes                   | MIDI            |
| Pioneer DDJ-SZ                            | yes                   | MIDI            |
| Pioneer DDJ WeGO                          | yes                   | MIDI            |
| Pioneer DDJ WeGO 2                        | yes                   | MIDI            |
| Pioneer DDJ WeGO 3                        | yes                   | MIDI            |
| Rane MP2015                               | yes                   | MIDI            |
| Rane MP25                                 | yes                   | MIDI            |
| Rane MP26                                 | yes                   | MIDI            |
| Rane Sixty-Two                            | yes                   | MIDI            |
| Rane Sixty-Fou                            | yes                   | MIDI            |
| Rane Sixty-Eight                          | yes                   | MIDI            |
| Reloop Beatmix 2                          | yes                   | MIDI            |
| Reloop Beatmix 4                          | yes                   | MIDI            |
| Reloop Terminal Mix 2                     | yes                   | MIDI            |
| Reloop Terminal Mix 8                     | yes                   | MIDI            |

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
registers the signals some of the controllers as generic Linux input
events. To get these devices to work with Mixxx on GNU/Linux, either the
driver would need to be modified to translate these signals to HID or
MIDI, Mixxx would need to be able to read Linux input events, or a
program would need to translate the Linux input events to HID or MIDI.

## Sound cards

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

1.  Discontinued product

2.  Discontinued product

3.  On Linux, requires kernel 3.8 or later

4.  On Linux, requires kernel 3.8 or later

5.  Discontinued product

6.  Discontinued product

7.  Discontinued product

8.  Mac OS X and Windows only with MIDI driver

9.  with MIDI driver. For Linux support, see [this forum
    thread](http://mixxx.org/forums/viewtopic.php?f=3&t=5064)

10. Discontinued product

11. [Mac OS X driver](http://www.joemattiello.com/dm2/); [Linux MIDI
    Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz), [Alternate
    Linux MIDI driver
    (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2),
    [dm2linux on
    sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453)

12. Mac OS X and Windows only with MIDI driver

13. Does this work with Linux?

14. Discontinued product

15. Discontinued product

16. Discontinued product

17. Discontinued product
