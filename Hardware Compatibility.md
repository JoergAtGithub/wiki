# Mixxx DJ Hardware Guide

## What hardware do you need to DJ with Mixxx?

It is recommended to use one sound card with at least 4 (mono) output
channels. Most computers only come with a sound card built into the
motherboard with 2 outputs. These onboard sound cards tend to not be
very good quality. When mixing in software on your CPU, use 2 channels
for the master output and 2 channels for your headphones. When mixing on
an analog hardware mixer, each deck uses 2 channels. See [the
manual](http://mixxx.org/manual/latest/chapters/setup.html) for diagrams
and descriptions of setups with different kinds of hardware.

Users completely new to DJing should consider getting an all-in-one
controller with an integrated sound card. Users who also want to produce
music should consider saving money and get a controller without a sound
card and invest in a high quality sound card suitable for recording.
Users who want to use [vinyl control](vinyl%20control) will need a sound
card with at least 4 inputs and phono preamps either on their sound card
or turntables. A few small controllers may be of particular interest to
vinyl DJs, such as the Novation Dicer and Akai Pro AMX. These are all
just guidelines; research your options and decide what you think will
work best for the way you want to DJ.

Many discontinued devices are listed on this page. They may or may not
still be available used online.

## Compatibility with Mixxx

Because Mixxx is [free
software](http://www.gnu.org/philosophy/free-sw.html) — free as in
freedom, not just price — we strive to make it work with as much
hardware as we can. Mixxx is collaboratively developed by a community of
volunteers and we can only make mappings for controllers that we have.
If hardware does not work with Mixxx, that does not mean it is
impossible, it only means that no one has made it work with Mixxx yet.
Anyone, including you, who has the hardware is welcome to make Mixxx
work with it.

Mixxx works with any sound card that your operating system has a driver
to use. Standards compliant USB sound cards do not need any special
drivers on Linux or Mac OS X, but they do on Windows. Most USB sound
cards are not standards compliant.

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

|                                                                  |              |                       |                 |                               |
| ---------------------------------------------------------------- | ------------ | --------------------- | --------------- | ----------------------------- |
| Device                                                           | Price (USD)  | Integrated Sound Card | Signal protocol | Supported since Mixxx version |
| [Keith McMillen QuNeo](Keith%20McMillen%20QuNeo)                 | $250         | no                    | MIDI            | 1.11                          |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)           | $300         | yes                   | MIDI            | 1.11                          |
| [American Audio VMS4](American%20Audio%20VMS4)                   | $400         | yes                   | MIDI            | 1.9                           |
| [Reloop Terminal Mix4](Reloop%20Terminal%20Mix4)                 | $400         | yes                   | MIDI            | 1.11                          |
| [DJ TechTools MIDIFighter](http://midifighter.com)               | discontinued | no                    | MIDI            | 1.8                           |
| [eks Otus](eks%20Otus)                                           | discontinued | no                    | HID             | 1.11                          |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)          | discontinued | yes                   | HID             | 1.11                          |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)         | discontinued | yes                   | HID             | 1.11                          |
| [Hercules DJ Control MP3 e2](Hercules%20DJ%20Control%20MP3%20e2) | discontinued | yes                   | HID             | 1.11                          |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)               | discontinued | no                    | MIDI            | 1.6                           |
| [Stanton SCS.3d](Stanton%20SCS.3d)                               | discontinued | no                    | MIDI            | 1.7                           |
| [Stanton SCS.3m](Stanton%20SCS.3m)                               | discontinued | no                    | MIDI            | 1.7                           |
| [Stanton SCS.1m](Stanton%20SCS.1m)                               | discontinued | yes                   | MIDI            | 1.9 \[1\]                     |
| [Stanton SCS.1d](Stanton%20SCS.1d)                               | discontinued | no                    | MIDI            | 1.9.1 \[2\]                   |
| [Vestax VCI-400](Vestax%20VCI-400)                               | discontinued | yes                   | MIDI            | 1.10.1                        |

### Community Supported Mappings

All controllers listed on GNU/Linux, Mac OS X, and Windows unless
otherwise indicated. If your controller is listed here but does not work
with your OS, please [report the bug](reporting%20bugs).

|                                                                                                    |              |                       |                 |                               |
| -------------------------------------------------------------------------------------------------- | ------------ | --------------------- | --------------- | ----------------------------- |
| Device                                                                                             | Price (USD)  | Integrated sound card | Signal protocol | Supported since Mixxx version |
| [Numark DJ2GO](Numark%20DJ2GO)                                                                     | $60          | no                    | MIDI            | 1.10                          |
| [Novation Dicer](Novation%20Dicer)                                                                 | $70          | no                    | MIDI            | 1.10                          |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | $100         | yes                   | MIDI            | 1.6                           |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | $250         | yes                   | MIDI            | 1.11                          |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                                               | $700         | yes                   | MIDI            | 1.12                          |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | $900         | no                    | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | $2000        | no                    | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Akai MPD24](Akai%20MPD24)                                                                         | discontinued | no                    | MIDI            | 1.8                           |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | discontinued | no                    | MIDI            | 1.10                          |
| [Denon SC2000](http://esync.de/denon-sc2000-mixxx-bindings)                                        | discontinued | no                    | MIDI            | 1.8                           |
| [Evolution X-Session](Evolution%20X-Session)                                                       | discontinued | no                    | MIDI            | 1.6                           |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | discontinued | no                    | MIDI            | 1.6                           |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | discontinued | no                    | HID             | 1.11                          |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | discontinued | yes                   | HID             | 1.11                          |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | discontinued | yes                   | HID?            | 1.7 \[3\]                     |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | discontinued | yes                   | HID             | 1.8 \[4\]                     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | discontinued | no                    | HID             | 1.11                          |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | discontinued | no                    | MIDI            | 1.8                           |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | discontinued | yes                   | MIDI            | 1.6                           |
| [Mixman DM2](Mixman%20DM2)                                                                         | discontinued | yes                   | ?               | 1.7\[5\]                      |
| [Numark Total Control](Numark%20Total%20Control)                                                   | discontinued | no                    | MIDI            | 1.6                           |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | discontinued | yes                   | MIDI            | 1.8                           |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | discontinued | yes                   | ?               | 1.8 \[6\]                     |
| [Numark Mixtrack](Numark%20Mixtrack)                                                               | discontinued | no                    | MIDI            | 1.8.2                         |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | discontinued | yes                   | MIDI            | 1.10                          |
| [Numark NS7](Numark%20NS7)                                                                         | discontinued | yes                   | MIDI            | 1.9 \[7\]                     |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | discontinued | no                    | MIDI or HID     | 1.8.2 (MIDI)                  |
| [Vestax VCI-100](Vestax%20VCI-100)                                                                 | discontinued | yes                   | MIDI            | 1.6                           |
| [Vestax VCI-300](Vestax%20VCI-300)                                                                 | discontinued | yes                   | MIDI            | 1.11                          |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | discontinued | yes                   | MIDI            | 1.9                           |
| [Vestax Spin](Vestax%20Spin)                                                                       | discontinued | yes                   | MIDI            | 1.9                           |

### Devices We Don't Have Mappings For

This is by no means an exhaustive list; these are just DJ controllers
from popular brands. There are too many DJ controllers out there to
list. If a controller you own or are interested in getting is not listed
here, [search the forum](http://mixxx.org/forums/search.php?fid[]=7) to
see if anyone has posted a mapping.

#### Do you own one of these? Consider contributing back to Mixxx by making a mapping

|                                              |              |                       |                          |
| -------------------------------------------- | ------------ | --------------------- | ------------------------ |
| Device                                       | Price (USD)  | Integrated sound card | Signal protocol          |
| Akai Pro AMX                                 | $250         | yes                   | MIDI                     |
| Allen & Heath Xone K1 \[8\]                  | $250         | no                    | MIDI                     |
| Gemini Slate                                 | $200         | yes                   | MIDI                     |
| Gemini Slate 4                               | $250         | yes                   | MIDI                     |
| Hercules DJ Control Jogvision                | $300         | yes                   | MIDI/HID (either? both?) |
| Korg KAOSS DJ                                | $300         | yes                   | MIDI                     |
| Native Instruments Traktor Kontrol D2        | $500         | no                    | ?                        |
| Native Instruments Traktor Kontrol F1        | $200         | no                    | HID                      |
| Native Instruments Traktor Kontrol X1 Mk1    | $200         | no                    | NHL                      |
| Native Instruments Traktor Kontrol X1 Mk2    | $200         | no                    | HID                      |
| Native Instruments Traktor Kontrol S2 Mk1    | discontinued | yes                   | NHL                      |
| Native Instruments Traktor Kontrol S2 Mk2    | $400         | yes                   | HID                      |
| Native Instruments Traktor Kontrol S4 Mk1    | discontinued | yes                   | NHL                      |
| Native Instruments Traktor Kontrol S4 Mk2    | $700         | yes                   | HID                      |
| Native Instruments Traktor Kontrol S8 \[9\]  | $1200        | yes                   | NHL                      |
| Native Instruments Traktor Kontrol Z1        | $200         | yes                   | HID                      |
| Native Instruments Traktor Kontrol Z2 \[10\] | $800         | yes                   | HID                      |
| Numark Mixtrack Edge                         | $100         | no                    | MIDI                     |
| Numark Mixtrack 3                            | $200         | no                    | MIDI                     |
| Numark Mixtrack Pro 3                        | $300         | yes                   | MIDI                     |
| Numark NS7II                                 | $1300        | yes                   | MIDI                     |
| Numark NS7III                                | $1500        | yes                   | MIDI                     |
| Numark NV                                    | $700         | yes                   | MIDI                     |
| Numark Orbit                                 | $100         | no                    | MIDI                     |
| Pioneer DDJ-SB                               | $250         | yes                   | MIDI                     |
| Pioneer DDJ-SR                               | $600         | yes                   | MIDI                     |
| Pioneer DDJ-SX2                              | $1000        | yes                   | MIDI                     |
| Pioneer DDJ-SZ                               | $2000        | yes                   | MIDI                     |
| Pioneer DDJ WeGO 3                           | $300         | yes                   | MIDI                     |
| Rane MP2015 \[11\]                           | $2900        | yes                   | MIDI                     |
| Rane MP25 \[12\]                             | $1500        | yes                   | MIDI                     |
| Rane MP26 \[13\]                             | $1750        | yes                   | MIDI                     |
| Rane Sixty-Two \[14\]                        | $2000        | yes                   | MIDI                     |
| Rane Sixty-Four \[15\]                       | $2200        | yes                   | MIDI                     |
| Rane Sixty-Eight \[16\]                      | $2600        | yes                   | MIDI                     |
| Rane TTM57 \[17\]                            | discontinued | yes                   | MIDI                     |
| Reloop Beatmix 2                             | $300         | yes                   | MIDI                     |
| Reloop Beatmix 4                             | $400         | yes                   | MIDI                     |
| Reloop Terminal Mix 2                        | $500         | yes                   | MIDI                     |
| Reloop Terminal Mix 4                        | $600         | yes                   | MIDI                     |
| Reloop Terminal Mix 8                        | $700         | yes                   | MIDI                     |

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

Mixxx can use any sound card that your OS has a driver to use. The table
below lists some recommended USB soundcards for DJing.

It is recommended to use one sound card with at least 4 output channels.
When mixing in software on your CPU, use 2 channels for the master
output and 2 channels for your headphones. When mixing on an analog
hardware mixer, each deck uses 2 channels. See [the
manual](http://mixxx.org/manual/latest/chapters/setup.html) for diagrams
and descriptions of setups with different kinds of hardware.

It is better to use a sound card with balanced outputs, especially if
you might run long cables directly into an amplifier or active speakers
without going through a DJ mixer. However, most venues have DJs plug
into DJ mixers, which typically only have RCA inputs (RCA cables cannot
be balanced). Most live sound mixers have balanced 1/4" inputs. Playing
audio at 16 bit sample depths and 44.1 kHz sample rate is fine for
DJing; almost all music is published in this format (which was the
standard set by audio CDs).

If you are interested in playing instruments over your DJing and/or
recording your own music, get a sound card with instrument preamps (for
electric guitars) and/or microphone preamps. Also consider getting an
interface that supports 24 bit sample depths and a 96 kHz sample rate.

If you want to use [vinyl control](vinyl%20control), it is best to get
turntables or a sound card with phono preamplifiers. Mixxx can amplify
phono level signals in software, but it is better to do it in hardware.

Mixxx can use multiple sound cards at the same time. However, before
Mixxx 1.12, this would result in crackling in the headphones. Every
sound card has its own clock crystal and no two are precisely the same
frequency even if the devices are the same model and from the same
production run. Mixxx before 1.12 synchronized its audio generation to
the clock crystal of whichever device is selected as the master output
(deck 1 output if no master is selected) so that the crowd won't hear
the artifacts. As a result, secondary devices either fall behind or run
ahead of the primary one, causing them to play silence until Mixxx
generates the next audio buffer exactly in time for the primary device.
Playing bits of audio interspersed with bits of silence sounds like
crackling. Mixxx 1.12 can compensate for this, but it is still better to
use one sound card with 4 outputs.

For Linux users, the [ALSA sound card
matrix](http://www.alsa-project.org/main/index.php/Matrix:Main) lists
Linux-compatible soundcards. Also see [Soundcard resources for Linux
DJs](http://www.pogo.org.uk/~mark/linuxdj/), courtesy of Mark Hills, the
author of [xwax](http://www.xwax.co.uk/). If you have a Firewire/IEEE
1394 interface, you'll want to look at [the FFADO
project](http://www.ffado.org).

### Standalone USB sound cards

|                                                           |             |                         |                                                              |                           |                                                                        |                            |            |                    |               |
| --------------------------------------------------------- | ----------- | ----------------------- | ------------------------------------------------------------ | ------------------------- | ---------------------------------------------------------------------- | -------------------------- | ---------- | ------------------ | ------------- |
| Device                                                    | Price (USD) | Channels out            | Output connectors                                            | Channels in               | Input connectors                                                       | Preamps                    | Bit depths | Sample rates (kHz) | Linux         |
| Behringer UCA222                                          | $30         | 2                       | 2 RCA, 1 1/8" headphone                                      | 2                         | 2 RCA                                                                  | 1 phono                    | 16         | 32, 44.1, 48       | yes           |
| Numark DJ iO                                              | $50         | 4                       | 4 RCA, 1 1/4" headphone                                      | 1                         | 1 1/4" mic                                                             | 1 mic                      | 24         | 44.1, 88.2         | no            |
| Griffin DJ Connect                                        | $90         | 4                       | 2 RCA, 1 1/8" headphone                                      | 0                         | none                                                                   | none                       | 16         | 48                 | likely \[18\] |
| Reloop Play                                               | $130        | 4                       | 4 RCA, 1 1/4" headphone                                      | 0                         | none                                                                   | none                       | 24         | 96                 | yes           |
| Native Instruments [Traktor Audio 2](Traktor%20Audio%202) | $100        | 4                       | 2 1/8" stereo                                                | 0                         | none                                                                   | none                       | 24         | 44.1, 48, 88.2, 96 | likely \[19\] |
| Focusrite Scarlett 2i4                                    | $200        | 4                       | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 5-pin MIDI       | 2                         | 2 XLR+1/4" balanced combo, 1 5-pin MIDI                                | 2 mic, 2 instrument        | 24         | 44.1, 48, 88.2, 96 | yes           |
| Native Instruments Komplete Audio 6                       | $230        | 6 (4 analog, 2 digital) | 4 1/4" balanced, 1 1/4" headphone, 1 5-pin MIDI, 1 RCA SPDIF | 6 (4 analog, 2 digital)   | 2 XLR+1/4" balanced, 2 1/4" balanced, 1 5-pin MIDI, 1 SPDIF            | 2 microphone, 2 instrument | 16, 24     | 44.1, 48, 96       | ?             |
| Focusrite Scarlett 6i6                                    | $250        | 6 (4 analog, 2 digital) | 1/4" balanced, 2 1/4" headphone, 1 5-pin MIDI, 1 RCA SPDIF   | 6 (4 analog, 2 digital)   | 2 XLR+1/4" balanced combo, 2 1/4" balanced, 1 5-pin MIDI, 1 RCA SPDIF  | 2 mic, 2 instrument        | 24         | 44.1, 48, 88.2, 96 | yes           |
| Native Instruments Traktor Scratch A6                     | $300        | 6                       | 6 RCA, 1 1/4" headphone                                      | 6                         | 6 RCA                                                                  | 2 phono                    | 16, 24     | 44.1, 48, 88.2, 96 | yes           |
| Focusrite Scarlett 18i8                                   | $350        | 8 (6 analog, 2 digital) | 2 1/4" balanced, 2 1/4" headphone, 1 5-pin MIDI, 1 RCA SPDIF | 18 (8 analog, 10 digital) | 4 XLR+1/4" balanced combo, 4 1/4" blanced, 1 RCA SPDIF, 1 optical ADAT | 4 mic, 2 instrument        | 24         | 44.1, 48, 88.2, 96 | yes           |
| Native Instruments Traktor Scratch A10                    | $500        | 10                      | 10 RCA, 1 1/4" headphone                                     | 10                        | 10 RCA, 1 1/4" mic                                                     | 4 phono, 1 mic             | 16, 24     | 44.1, 48, 88.2, 96 | ?             |
| Rane SL2                                                  | $500        | 4                       | 4 RCA                                                        | 4                         | 4 RCA                                                                  | 2 phono                    | 24         | 44.1, 48           | no            |
| Rane SL3                                                  | $700        | 6                       | 6 RCA                                                        | 6                         | 6 RCA                                                                  | 3 phono                    | 24         | 44.1, 48           | no            |
| Rane SL4                                                  | $900        | 8                       | 8 RCA                                                        | 8                         | 8 RCA                                                                  | 4 phono                    | 24         | 48, 96             | no            |

### Sound cards integrated into controllers

#### Controllers with Mixxx mappings

|                       |             |              |                                                            |             |                              |                |            |                    |       |
| --------------------- | ----------- | ------------ | ---------------------------------------------------------- | ----------- | ---------------------------- | -------------- | ---------- | ------------------ | ----- |
| Device                | Price (USD) | Channels out | Output connectors                                          | Channels in | Input connectors             | Preamps        | Bit depths | Sample rates (kHz) | Linux |
| Behringer BCD3000     | $100        | 4            | 2 RCA, 1 1/4" headphone                                    | 4           | 4 RCA, 1 XLR mic             | 2 phono, 1 mic | 24         | 44.1               | yes   |
| Numark Mixtrack Pro 2 | $250        | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                  | 1           | 1/4" mic                     | 1 mic          | 16         | 44.1, 48           | yes   |
| Allen & Heath Xone K2 | $300        | 4            | 2 RCA, 1 1/8" headphone                                    | 0           | none                         | none           | 16         | 48                 | ?     |
| Reloop Terminal Mix 4 | $400        | 4            | 4 RCA, 2 1/4" balanced, 1 1/4" headphone, 1 1/8" headphone | 2           | 2 RCA, 1/4" mic              | 1 phono, 1 mic | ?          | ?                  | ?     |
| Denon MC6000 Mk2      | $700        | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone            | 8           | 8 RCA, 1 1/4" mic, 1 XLR mic | 4 phono, 1 mic | 24         | 44.1               | ?     |

#### Controllers with no Mixxx mappings yet

|                                              |              |              |                                                                   |             |                                            |                |            |                    |               |
| -------------------------------------------- | ------------ | ------------ | ----------------------------------------------------------------- | ----------- | ------------------------------------------ | -------------- | ---------- | ------------------ | ------------- |
| Device                                       | Price (USD)  | Channels out | Output connectors                                                 | Channels in | Input connectors                           | Preamps        | Bit depths | Sample rates (kHz) | Linux         |
| Akai Pro AMX                                 | $250         | 4            | 2 RCA, 1 1/8" headphone                                           | 4           | 4 RCA                                      | 2 phono        | 24         | 96                 | ?             |
| Gemini Slate                                 | $200         | 4            | 2 RCA, 1 1/8" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ? \[20\]      |
| Gemini Slate 4                               | $250         | 4            | 2 RCA, 1 1/8" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ? \[21\]      |
| Hercules DJ Control Jogvision                | $300         | 4            | 4 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 2           | 1/4" mic, 1/8" stereo                      | 1 mic          | 16, 24     | 44.1, 48, 96       | ?             |
| Korg KAOSS DJ                                | $300         | 4            | 2 RCA, 1 1/4" headphone                                           | 2           | 2 RCA, 1 1/4" mic                          | 1 mic          | 24         | 44.1, 48           | ?             |
| Native Instruments Traktor Kontrol S2 Mk1    | discontinued | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Native Instruments Traktor Kontrol S2 Mk2    | $400         | 4            | 2 RCA, 2 1/4" balanced, 1 1/4" headphone                          | 1           | 1 1/4" mic                                 | 1 microphone   | 16, 24     | 44.1, 48, 88.2, 96 | ?             |
| Native Instruments Traktor Kontrol S4 Mk1    | discontinued | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | yes           |
| Native Instruments Traktor Kontrol S4 Mk2    | $700         | 4            | 2 RCA, 2 1/4" balanced, 1 5-pin MIDI                              | 5           | 4 RCA, 1/4" mic, 1 5-pin MIDI              | 2 phono, 1 mic | 16, 24     | 44.1, 48, 88.2, 96 | ?             |
| Native Instruments Traktor Kontrol S8 \[22\] | $1200        | 4            | 2 RCA, 2 1/4" balanced, 2 XLR, 1 1/4" headphone, 1 5-pin MIDI     | 4           | 4 RCA, 1 1/4" mic, 1 XLR mic, 1 5-pin MIDI | 2 phono, 1 mic | 24         | 48                 | ?             |
| Native Instruments Traktor Kontrol Z1        | $200         | 4            | 2 RCA, 1 1/8" headphone                                           | 0           | none                                       | none           | 24         | 96                 | ?             |
| Native Instruments Traktor Kontrol Z2 \[23\] | $800         | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 6           | 6 RCA, 1 1/4" mic                          | 2 phono, 1 mic | 24         | 48                 | ?             |
| Numark Mixtrack Pro 3                        | $300         | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 1           | 1/4" mic                                   | 1 mic          | 24         | 44.1               | ?             |
| Numark NS7                                   | discontinued | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Numark NS7II                                 | $1300        | 4            | 2 1/4" balanced, 2 XLR, 4 RCA, 1 1/4" headphone, 1 1/8" headphone | 10          | 8 RCA, 2 XLR+1/4" combo                    | 4 phono, 2 mic | 24         | 44.1               | ?             |
| Numark NS7III                                | $1500        | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Numark NV                                    | $700         | 4            | 4 RCA, 2 XLR, 1 1/4" headphone                                    | 3           | 2 RCA, 1 1/4" mic                          | 1 mic          | ?          | ?                  | ?             |
| Pioneer DDJ-SB                               | $250         | 4            | 2 1/4" balanced, 2 RCA, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1 1/4" mic                          | 1 mic          | 24         | 44.1               | ?             |
| Pioneer DDJ-SR                               | $600         | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 9           | 8 RCA, 1 XLR mic, 1 1/4" mic               | 2 phono, 1 mic | 24         | 44.1               | ?             |
| Pioneer DDJ-SX2                              | $1000        | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 8           | 8 RCA, 1 XLR+1/4" combo, 1 1/4" mic        | 2 phono, 2 mic | 24         | 44.1               | ?             |
| Pioneer DDJ-SZ                               | $2000        | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 8           | 8 RCA, 1 XLR+1/4" combo, 1 1/4" mic        | 2 phono, 2 mic | 24         | 44.1               | ?             |
| Pioneer DDJ WeGO 3                           | $300         | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 1           | 1 1/4" mic                                 | 1 mic          | 24         | 48                 | ?             |
| Rane MP2015 \[24\]                           | $2900        | 10           | N/A                                                               | 14          | N/A                                        | 4 phono        | 24         | 44.1, 48, 96       | likely \[25\] |
| Rane MP25 \[26\]                             | $1500        | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | likely \[27\] |
| Rane MP26 \[28\]                             | $1750        | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | likely \[29\] |
| Rane Sixty-Two \[30\]                        | $2000        | 8            | N/A                                                               | 12          | N/A                                        | 2 phono        | 24         | 48                 | ?             |
| Rane Sixty-Four \[31\]                       | $2200        | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | ?             |
| Rane Sixty-Eight \[32\]                      | $2600        | 12           | N/A                                                               | 10          | N/A                                        | 4 phono        | 24         | 48                 | ?             |
| Rane TTM57 \[33\]                            | discontinued | 10           | N/A                                                               | 10          | N/A                                        | 2 phono        | 24         | 44.1, 48, 96       | likely \[34\] |
| Reloop Beatmix 2                             | $300         | 4            | 2 RCA, 1 1/4" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ?             |
| Reloop Beatmix 4                             | $400         | 4            | 2 RCA, 1 1/4" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | 16         | 48                 | ?             |
| Reloop Terminal Mix 2                        | $500         | 4            | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1 1/4" mic                          | 1 phono, 1 mic | ?          | ?                  | ?             |
| Reloop Terminal Mix 8                        | $700         | 4            | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1 1/4" mic                          | 1 phono, 1 mic | ?          | ?                  | ?             |

1.  On Linux, requires kernel 3.8 or later

2.  On Linux, requires kernel 3.8 or later

3.  Mac OS X and Windows only with MIDI driver

4.  with MIDI driver. For Linux support, see [this forum
    thread](http://mixxx.org/forums/viewtopic.php?f=3&t=5064)

5.  [Mac OS X driver](http://www.joemattiello.com/dm2/); [Linux MIDI
    Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz), [Alternate
    Linux MIDI driver
    (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2),
    [dm2linux on
    sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453)

6.  Mac OS X and Windows only with MIDI driver

7.  Does this work with Linux?

8.  Does the Xone K2 mapping work for this?

9.  also a standalone digital mixer

10. also a standalone analog mixer

11. also a standalone analog mixer

12. also a standalone analog mixer

13. also a standalone analog mixer

14. also a standalone analog mixer

15. also a standalone analog mixer

16. also a standalone analog mixer

17. also a standalone analog mixer

18. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

19. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

20. Fun fact: the firmware runs Linux

21. Fun fact: the firmware runs Linux

22. also a standalone digital mixer

23. also a standalone analog mixer

24. also a standalone analog mixer

25. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

26. also a standalone analog mixer

27. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

28. also a standalone analog mixer

29. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

30. also a standalone analog mixer

31. also a standalone analog mixer

32. also a standalone analog mixer

33. also a standalone analog mixer

34. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.
