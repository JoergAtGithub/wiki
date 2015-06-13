# Mixxx DJ Hardware Guide

## What hardware is needed to DJ with Mixxx?

It is recommended to use one sound card with at least 4 mono output
channels (2 stereo channels). Most computers come with a sound card
built into the motherboard with only 1 stereo 1/8" headphone output (2
mono channels). While it is possible to get a cheap sound card with only
2 more outputs and use it together with your onboard sound card, it is
not recommended (see [explanation below](#Using-multiple-sound-cards)).
These onboard sound cards are generally not high quality and may pick up
interference from other devices in the computer such as the power supply
or hard drive. When mixing digitally in software on your CPU, use 2
channels for the main output and 2 channels for your headphones. This
allows you to hear and prepare the track you want to play next without
your audience hearing it until you are ready to mix it into the main
output. When mixing on an analog hardware mixer, which is traditional
(but not necessary) with [vinyl control](vinyl%20control), each deck
uses 2 channels and the headphones are plugged into the analog hardware
mixer.

Most digital DJs prefer to use a DJ controller rather than just their
keyboard and mouse for more intuitive control of their software. Most DJ
controllers that cost $200 or more bundle a sound card with the
controller. Cheaper controllers are available without integrated sound
cards.

**The simplest setup for new DJs is an all-in-one controller that can
control mixing, seeking, looping, cues, and effects and has an
integrated sound card.** Users who also want to produce music should
consider saving money and get a controller without a sound card and
getting a separate, high quality sound card suitable for recording.
Users who want to use [vinyl control](vinyl%20control) will need a sound
card with 2 inputs per deck (so 4 inputs for a traditional 2 deck setup)
and a phono preamp for each deck, either in the turntable, in the sound
card, or as a stand alone device. A few small controllers may be of
particular interest to vinyl DJs, such as the Novation Dicer and Akai
Pro AMX. These are all just guidelines; research your options and decide
what you think will work best for the way you want to DJ.

See [the manual](http://mixxx.org/manual/latest/chapters/setup.html) for
diagrams and descriptions of setups with different kinds of hardware.

Many discontinued devices are listed on this page. They may or may not
still be available used online.

## Hardware compatibility with Mixxx

Because Mixxx is [free
software](http://www.gnu.org/philosophy/free-sw.html) — free as in
artistic freedom, not just price — we strive to make it work with as
much hardware as we can. Mixxx is collaboratively developed by a
community of volunteers and we can only make mappings for controllers
that we have. If hardware does not work with Mixxx, that does not mean
it is impossible, it only means that no one has made it work with Mixxx
yet. Anyone, including you, who has the hardware is welcome to make
Mixxx work with it.

Mixxx works with any sound card that your operating system has a driver
to use. Standards compliant USB sound cards do not need any special
drivers on Linux or Mac OS X, but they do on Windows. Most USB sound
cards are not standards compliant. Sound cards that are advertised for
use with iOS devices are standards compliant.

Mixxx can work with any controller that sends MIDI or HID signals to
your computer; it just needs a controller mapping to tell Mixxx what to
do with the signals. Standards compliant MIDI controllers do not need
any special drivers on Linux, Mac OS X, or Windows. Standards compliant
HID controllers do not need any special drivers on Linux and Mac OS X,
but do require drivers on Windows. Controllers that have integrated
sound cards require a driver on every OS for the sound card, unless it
is USB audio class compliant.

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
documentation on making and editing controller mappings. Feel free to
ask for help mapping your controller on the forums. If you ask for help,
please consider that most people reading your post will not have your
controller, so be specific about what kind of controller you have and
what you want to map it to do.

If you notice any bugs in the mappings, or wish the mapping would work
differently, please [report it on our bug tracker](reporting%20bugs).

### Mixxx Certified Mappings

|                                                                  |              |                            |                       |                 |                               |
| ---------------------------------------------------------------- | ------------ | -------------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                                           | Price (USD)  | Description                | Integrated Sound Card | Signal protocol | Supported since Mixxx version |
| [Keith McMillen QuNeo](Keith%20McMillen%20QuNeo)                 | $250         | 2 deck all-in-one          | no                    | MIDI            | 1.11                          |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)           | $300         | 4 deck mixer + pads        | yes                   | MIDI            | 1.11                          |
| [American Audio VMS4](American%20Audio%20VMS4)                   | $400         | 4 deck all-in-one          | yes                   | MIDI            | 1.9                           |
| [Reloop Terminal Mix4](Reloop%20Terminal%20Mix4)                 | $400         | 4 deck all-in-one          | yes                   | MIDI            | 1.11                          |
| [DJ TechTools MIDIFighter](http://midifighter.com)               | discontinued | button grid                | no                    | MIDI            | 1.8                           |
| [eks Otus](eks%20Otus)                                           | discontinued | 1 turntable + 2 deck mixer | no                    | HID             | 1.11                          |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)          | discontinued | basic 2 deck all-in-one    | yes                   | HID             | 1.11                          |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)         | discontinued | basic 2 deck all-in-one    | yes                   | HID             | 1.11                          |
| [Hercules DJ Control MP3 e2](Hercules%20DJ%20Control%20MP3%20e2) | discontinued | basic 2 deck all-in-one    | no                    | MIDI + HID      | 1.11                          |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)               | discontinued | 2 deck mixer               | no                    | MIDI            | 1.6                           |
| [Stanton SCS.3d](Stanton%20SCS.3d)                               | discontinued | 1 deck control             | no                    | MIDI            | 1.7                           |
| [Stanton SCS.3m](Stanton%20SCS.3m)                               | discontinued | 2 deck mixer               | no                    | MIDI            | 1.7                           |
| [Stanton SCS.1m](Stanton%20SCS.1m)                               | discontinued | 4 deck mixer               | yes                   | MIDI            | 1.9 \[1\]                     |
| [Stanton SCS.1d](Stanton%20SCS.1d)                               | discontinued | 1 turntable                | no                    | MIDI            | 1.9.1 \[2\]                   |
| [Vestax VCI-400](Vestax%20VCI-400)                               | discontinued | 4 deck all-in-one          | yes                   | MIDI            | 1.10.1                        |

### Community Supported Mappings

All controllers listed on GNU/Linux, Mac OS X, and Windows unless
otherwise indicated. If your controller is listed here but does not work
with your OS, please [report the bug](reporting%20bugs).

|                                                                                                    |              |                                           |                       |                 |                               |
| -------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                                                                             | Price (USD)  | Description                               | Integrated sound card | Signal protocol | Supported since Mixxx version |
| [Numark DJ2GO](Numark%20DJ2GO)                                                                     | $60          | basic 2 deck all-in-one                   | no                    | MIDI            | 1.10                          |
| [Novation Dicer](Novation%20Dicer)                                                                 | $70          | hotcues and loops for use with turntables | no                    | MIDI            | 1.10                          |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | $100         | basic all-in-one                          | yes                   | MIDI            | 1.6                           |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | $250         | 2 deck all-in-one                         | yes                   | MIDI            | 1.11                          |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                                               | $700         | 4 deck all-in-one                         | yes                   | MIDI            | 1.12                          |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | $900         | CD player                                 | no                    | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | $2000        | CD player                                 | no                    | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Akai MPD24](Akai%20MPD24)                                                                         | discontinued | ?                                         | no                    | MIDI            | 1.8                           |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | discontinued | CD player                                 | no                    | MIDI            | 1.10                          |
| [Denon SC2000](http://esync.de/denon-sc2000-mixxx-bindings)                                        | discontinued | 1 deck                                    | no                    | MIDI            | 1.8                           |
| [Evolution X-Session](Evolution%20X-Session)                                                       | discontinued | knobs + crossfader                        | no                    | MIDI            | 1.6                           |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | discontinued | 2 deck mixer                              | no                    | MIDI            | 1.6                           |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | discontinued | 2 deck all-in-one                         | no                    | HID             | 1.11                          |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | discontinued | 2 deck all-in-one                         | yes                   | HID             | 1.11                          |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | discontinued | 2 deck all-in-one                         | yes                   | HID?            | 1.7 \[3\]                     |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | discontinued | 2 deck all-in-one                         | yes                   | HID             | 1.8 \[4\]                     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | discontinued | 2 deck all-in-one                         | no                    | HID             | 1.11                          |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | discontinued | 2 deck all-in-one                         | no                    | MIDI            | 1.8                           |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | discontinued | 2 deck all-in-one                         | yes                   | MIDI            | 1.6                           |
| [Mixman DM2](Mixman%20DM2)                                                                         | discontinued | 2 decks                                   | yes                   | ?               | 1.7\[5\]                      |
| [Numark Total Control](Numark%20Total%20Control)                                                   | discontinued | 2 deck all-in-one                         | no                    | MIDI            | 1.6                           |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | discontinued | 2 deck all-in-one                         | yes                   | MIDI            | 1.8                           |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | discontinued | 2 deck all-in-one                         | yes                   | ?               | 1.8 \[6\]                     |
| [Numark Mixtrack](Numark%20Mixtrack)                                                               | discontinued | 2 deck all-in-one                         | no                    | MIDI            | 1.8.2                         |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | discontinued | 2 deck all-in-one                         | yes                   | MIDI            | 1.10                          |
| [Numark NS7](Numark%20NS7)                                                                         | discontinued | 2 deck all-in-one with motorized wheels   | yes                   | MIDI            | 1.9 \[7\]                     |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | discontinued | CD player                                 | no                    | MIDI or HID     | 1.8.2 (MIDI)                  |
| [Vestax VCI-100](Vestax%20VCI-100)                                                                 | discontinued | 2 deck all-in-one                         | yes                   | MIDI            | 1.6                           |
| [Vestax VCI-300](Vestax%20VCI-300)                                                                 | discontinued | 2 deck all-in-one                         | yes                   | MIDI            | 1.11                          |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | discontinued | 2 deck all-in-one                         | yes                   | MIDI            | 1.9                           |
| [Vestax Spin](Vestax%20Spin)                                                                       | discontinued | 2 deck all-in-one                         | yes                   | MIDI            | 1.9                           |

### Controllers that do not yet have Mixxx mappings

This is by no means an exhaustive list; these are just DJ controllers
from popular brands. There are too many DJ controllers out there to
list. If a controller you own or are interested in getting is not listed
here, [search the forum](http://mixxx.org/forums/search.php?fid[]=7) to
see if anyone has posted a mapping. If you are willing to put in the
effort to map one of these controllers, please get the controller, map
it, and publish the mapping so we can include it in Mixxx.

|                                           |              |                                                         |                       |                          |
| ----------------------------------------- | ------------ | ------------------------------------------------------- | --------------------- | ------------------------ |
| Device                                    | Price (USD)  | Description                                             | Integrated sound card | Signal protocol          |
| Behringer CMD MM-1                        | $100         | 4 deck mixer                                            | no                    | MIDI                     |
| Numark Mixtrack Edge                      | $100         | basic 2 deck all-in-one                                 | no                    | MIDI                     |
| Numark Mixtrack 2 \[8\]                   | $150         | 2 deck all-in-one                                       | no                    | MIDI                     |
| Native Instruments Traktor Kontrol Z1     | $200         | basic 2 deck mixer                                      | yes                   | HID                      |
| Native Instruments Traktor Kontrol F1     | $200         | remixing pads + faders                                  | no                    | HID                      |
| Native Instruments Traktor Kontrol X1 Mk1 | $200         | effects                                                 | no                    | NHL                      |
| Native Instruments Traktor Kontrol X1 Mk2 | $200         | effects + touch strip                                   | no                    | HID                      |
| Gemini Slate                              | $200         | 2 deck all-in-one                                       | yes                   | MIDI                     |
| Allen & Heath Xone K1 \[9\]               | $250         | 4 deck mixer + pads                                     | no                    | MIDI                     |
| Numark Mixtrack 3 \[10\]                  | $200         | 2 deck all-in-one                                       | no                    | MIDI                     |
| Akai Pro AFX                              | $200         | 2 deck effects + pads + touch strip                     | no                    | MIDI                     |
| Akai Pro AMX                              | $250         | 2 deck mixer + vinyl hookup                             | yes                   | MIDI                     |
| Gemini Slate 4                            | $250         | 4 deck all-in-one                                       | yes                   | MIDI                     |
| Pioneer DDJ-SB                            | $250         | 2 deck all-in-one                                       | yes                   | MIDI                     |
| Hercules DJ Control Jogvision             | $300         | 2 deck all-in-one                                       | yes                   | MIDI/HID (either? both?) |
| Korg KAOSS DJ                             | $300         | 2 deck all-in-one                                       | yes                   | MIDI                     |
| Numark Mixtrack Pro 3 \[11\]              | $300         | 2 deck all-in-one                                       | yes                   | MIDI                     |
| Reloop Beatmix 2                          | $300         | 2 deck all-in-one                                       | yes                   | MIDI                     |
| Pioneer DDJ WeGO 3                        | $300         | 2 deck all-in-one                                       | yes                   | MIDI                     |
| Reloop Beatmix 4                          | $400         | 4 deck all-in-one                                       | yes                   | MIDI                     |
| Native Instruments Traktor Kontrol S2 Mk1 | discontinued | 2 deck all-in-one                                       | yes                   | NHL                      |
| Native Instruments Traktor Kontrol S2 Mk2 | $400         | 2 deck all-in-one                                       | yes                   | HID                      |
| Native Instruments Traktor Kontrol D2     | $500         | remixing pads, faders, and touch strip                  | no                    | ?                        |
| Reloop Terminal Mix 2                     | $500         | 2 deck all-in-one                                       | yes                   | MIDI                     |
| Pioneer DDJ-SR                            | $600         | 2 deck all-in-one                                       | yes                   | MIDI                     |
| Reloop Terminal Mix 4                     | $600         | 4 deck all-in-one                                       | yes                   | MIDI                     |
| Native Instruments Traktor Kontrol S4 Mk1 | discontinued | 4 deck all-in-one                                       | yes                   | NHL                      |
| Native Instruments Traktor Kontrol S4 Mk2 | $700         | 4 deck all-in-one                                       | yes                   | HID                      |
| Numark NV                                 | $700         | 4 deck all-in-one                                       | yes                   | MIDI                     |
| Reloop Terminal Mix 8                     | $700         | 4 deck all-in-one                                       | yes                   | MIDI                     |
| Native Instruments Traktor Kontrol Z2     | $800         | 2 decks + effects + standalone digital mixer            | yes                   | HID                      |
| Native Instruments Traktor Kontrol S8     | $1200        | 4 deck all-in-one + remixing + standalone digital mixer | yes                   | NHL                      |
| Pioneer DDJ-SX2                           | $1000        | 4 deck all-in-one                                       | yes                   | MIDI                     |
| Numark NS7II                              | $1300        | 4 deck all-in-one with motorized wheels                 | yes                   | MIDI                     |
| Numark NS7III                             | $1500        | 4 deck all-in-one with motorized wheels                 | yes                   | MIDI                     |
| Rane MP25                                 | $1500        | 4 deck analog mixer                                     | yes                   | MIDI                     |
| Rane MP26                                 | $1750        | 4 deck analog mixer                                     | yes                   | MIDI                     |
| Rane Sixty-Two                            | $2000        | 2 deck analog mixer + loops, cues, and effects          | yes                   | MIDI                     |
| Pioneer DDJ-SZ                            | $2000        | 4 deck all-in-one                                       | yes                   | MIDI                     |
| Rane Sixty-Four                           | $2200        | 4 deck analog mixer + loops, cues, and effects          | yes                   | MIDI                     |
| Rane Sixty-Eight                          | $2600        | 4 deck analog mixer + loops, cues, and effects          | yes                   | MIDI                     |
| Rane MP2015                               | $2900        | 4 deck analog rotary mixer                              | yes                   | MIDI                     |
| Rane TTM57                                | discontinued | 2 deck analog mixer + loops, cues, and effects          | yes                   | MIDI                     |

## Sound cards

### Compatibility

Mixxx can use any sound card that your OS has a driver to use. The
tables below list some recommended USB soundcards for DJing. All listed
sound cards work with Mac OS X and Windows. Most work with Linux, but
not all; check the table for details.

The [ALSA sound card
matrix](http://www.alsa-project.org/main/index.php/Matrix:Main) lists
Linux-compatible soundcards. Linux users may also benefit from [these
soundcard resources for Linux
DJs](http://www.pogo.org.uk/~mark/linuxdj/), courtesy of Mark Hills, the
author of [xwax](http://www.xwax.co.uk/). If you have a Firewire/IEEE
1394 interface, the only way to use it with Linux is with JACK (not
ALSA). The FFADO project has [a list of Firewire interfaces compatible
with Linux](http://ffado.org/?q=devicesupport/list).

### Sound card types for different uses

As explained [at the top of the
page](#What-hardware-is-needed-to-DJ-with-Mixxx?), it is recommended to
use a sound card with at least 4 mono output channels with Mixxx.

If you are unfamiliar with professional audio equipment, read Digital DJ
Tips' [Essential Guide to Audio Cables for
DJs](http://www.digitaldjtips.com/2011/07/the-essential-guide-to-audio-cables-for-djs/).

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

If you want to use [vinyl control](vinyl%20control), it is best to have
phono preamplifiers (one for each deck) somewhere between your turntable
and sound card to boost the turntable signal to line level. Mixxx can
amplify phono level signals in software, but it is better to do it in
hardware. The phono preamp can be in the turntable, in the sound card,
or a stand alone device. For a traditional 2 deck setup, the Akai Pro
AMX and Native Instruments Traktor Scratch A6 are good options. Some
cheaper sound cards, namely the Electrix Ebox44 and Mixvibes U-Mix44,
would also work but have been discontinued and may be difficult to find.
The Native Instruments Traktor Scratch A10 is a good option for using 4
vinyl decks. Many higher-end all-in-one controllers include phono
preamps too.

Sound cards often have multiple connectors for a single channel,
resulting in more connectors than channels. So, not every connector can
send or receive an independent signal. Many sound cards made for DJing
have 4 output channels with 4 mono output connectors and 1 stereo
headphone connector. This does not mean that the sound card can send out
6 different signals at the same time; rather, the signal on 2 of the
mono outputs and the stereo headphone output would be the same.

### Using multiple sound cards

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

### Standalone USB sound cards

|                                                           |                         |                         |                                                              |                           |                                                                        |                                      |            |                    |               |
| --------------------------------------------------------- | ----------------------- | ----------------------- | ------------------------------------------------------------ | ------------------------- | ---------------------------------------------------------------------- | ------------------------------------ | ---------- | ------------------ | ------------- |
| Device                                                    | Price (USD)             | Channels out            | Output connectors                                            | Channels in               | Input connectors                                                       | Preamps                              | Bit depths | Sample rates (kHz) | Linux         |
| Behringer UCA222                                          | $30                     | 2                       | 2 RCA, 1 1/8" headphone                                      | 2                         | 2 RCA                                                                  | 1 phono                              | 16         | 32, 44.1, 48       | yes           |
| Numark DJ iO                                              | $50                     | 4                       | 4 RCA, 1 1/4" headphone                                      | 1                         | 1 1/4" mic                                                             | 1 mic                                | 24         | 44.1, 88.2         | no            |
| Griffin DJ Connect                                        | $90                     | 4                       | 2 RCA, 1 1/8" headphone                                      | 0                         | none                                                                   | none                                 | 16         | 48                 | likely \[12\] |
| Native Instruments [Traktor Audio 2](Traktor%20Audio%202) | $100                    | 4                       | 2 1/8" stereo                                                | 0                         | none                                                                   | none                                 | 24         | 44.1, 48, 88.2, 96 | likely \[13\] |
| Electrix Ebox-44                                          | discontinued (was $100) | 4                       | 4 RCA, 1 1/4" headphone                                      | 5                         | 4 RCA, 1 1/4" mic                                                      | 2 phono (one switch for both), 1 mic | 16         | 44.1, 48           | yes           |
| Mixvibes U-Mix44                                          | discontinued (was $100) | 4                       | 4 RCA, 1 1/8" headphone                                      | 5                         | 4 RCA, 1 1/4" mic                                                      | 2 phono, 1 mic                       | 16         | 48                 | yes           |
| Reloop Play                                               | $130                    | 4                       | 4 RCA, 1 1/4" headphone                                      | 0                         | none                                                                   | none                                 | 24         | 96                 | yes           |
| Focusrite Scarlett 2i4                                    | $200                    | 4                       | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 5-pin MIDI       | 2                         | 2 XLR+1/4" balanced combo, 1 5-pin MIDI                                | 2 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | yes           |
| Native Instruments Komplete Audio 6                       | $230                    | 6 (4 analog, 2 digital) | 4 1/4" balanced, 1 1/4" headphone, 1 5-pin MIDI, 1 RCA SPDIF | 6 (4 analog, 2 digital)   | 2 XLR+1/4" balanced, 2 1/4" balanced, 1 5-pin MIDI, 1 SPDIF            | 2 mic, 2 instrument                  | 16, 24     | 44.1, 48, 96       | yes           |
| Focusrite Scarlett 6i6                                    | $250                    | 6 (4 analog, 2 digital) | 1/4" balanced, 2 1/4" headphone, 1 5-pin MIDI, 1 RCA SPDIF   | 6 (4 analog, 2 digital)   | 2 XLR+1/4" balanced combo, 2 1/4" balanced, 1 5-pin MIDI, 1 RCA SPDIF  | 2 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | yes           |
| Native Instruments Traktor Scratch A6                     | $300                    | 6                       | 6 RCA, 1 1/4" headphone                                      | 6                         | 6 RCA                                                                  | 2 phono                              | 16, 24     | 44.1, 48, 88.2, 96 | yes           |
| Focusrite Scarlett 18i8                                   | $350                    | 8 (6 analog, 2 digital) | 2 1/4" balanced, 2 1/4" headphone, 1 5-pin MIDI, 1 RCA SPDIF | 18 (8 analog, 10 digital) | 4 XLR+1/4" balanced combo, 4 1/4" blanced, 1 RCA SPDIF, 1 optical ADAT | 4 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | yes           |
| Native Instruments Traktor Scratch A10                    | $500                    | 10                      | 10 RCA, 1 1/4" headphone                                     | 10                        | 10 RCA, 1 1/4" mic                                                     | 4 phono, 1 mic                       | 16, 24     | 44.1, 48, 88.2, 96 | ?             |
| Rane SL2                                                  | $500                    | 4                       | 4 RCA                                                        | 4                         | 4 RCA                                                                  | 2 phono                              | 24         | 44.1, 48           | no            |
| Rane SL3                                                  | $700                    | 6                       | 6 RCA                                                        | 6                         | 6 RCA                                                                  | 3 phono                              | 24         | 44.1, 48           | no            |
| Rane SL4                                                  | $900                    | 8                       | 8 RCA                                                        | 8                         | 8 RCA                                                                  | 4 phono                              | 24         | 48, 96             | no            |

### Sound cards integrated into controllers

#### Controllers with Mixxx mappings

|                       |             |              |                                                            |             |                              |                |            |                    |       |
| --------------------- | ----------- | ------------ | ---------------------------------------------------------- | ----------- | ---------------------------- | -------------- | ---------- | ------------------ | ----- |
| Device                | Price (USD) | Channels out | Output connectors                                          | Channels in | Input connectors             | Preamps        | Bit depths | Sample rates (kHz) | Linux |
| Behringer BCD3000     | $100        | 4            | 2 RCA, 1 1/4" headphone                                    | 5           | 4 RCA, 1 XLR mic             | 2 phono, 1 mic | 24         | 44.1               | yes   |
| Numark Mixtrack Pro 2 | $250        | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                  | 1           | 1/4" mic                     | 1 mic          | 16         | 44.1, 48           | yes   |
| Allen & Heath Xone K2 | $300        | 4            | 2 RCA, 1 1/8" headphone                                    | 0           | none                         | none           | 16         | 48                 | ?     |
| Reloop Terminal Mix 4 | $400        | 4            | 4 RCA, 2 1/4" balanced, 1 1/4" headphone, 1 1/8" headphone | 3           | 2 RCA, 1/4" mic              | 1 phono, 1 mic | ?          | ?                  | ?     |
| Denon MC6000 Mk2      | $700        | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone            | 9           | 8 RCA, 1 1/4" mic, 1 XLR mic | 4 phono, 1 mic | 24         | 44.1               | ?     |

#### Controllers with no Mixxx mappings yet

|                                              |              |              |                                                                   |             |                                            |                |            |                    |               |
| -------------------------------------------- | ------------ | ------------ | ----------------------------------------------------------------- | ----------- | ------------------------------------------ | -------------- | ---------- | ------------------ | ------------- |
| Device                                       | Price (USD)  | Channels out | Output connectors                                                 | Channels in | Input connectors                           | Preamps        | Bit depths | Sample rates (kHz) | Linux         |
| Native Instruments Traktor Kontrol Z1        | $200         | 4            | 2 RCA, 1 1/8" headphone                                           | 0           | none                                       | none           | 24         | 96                 | yes           |
| Gemini Slate                                 | $200         | 4            | 2 RCA, 1 1/8" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ? \[14\]      |
| Gemini Slate 4                               | $250         | 4            | 2 RCA, 1 1/8" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ? \[15\]      |
| Akai Pro AMX                                 | $250         | 4            | 2 RCA, 1 1/8" headphone                                           | 4           | 4 RCA                                      | 2 phono        | 24         | 96                 | likely \[16\] |
| Pioneer DDJ-SB                               | $250         | 4            | 2 1/4" balanced, 2 RCA, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1 1/4" mic                          | 1 mic          | 24         | 44.1               | ?             |
| Hercules DJ Control Jogvision                | $300         | 4            | 4 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 3           | 1/4" mic, 1/8" stereo                      | 1 mic          | 16, 24     | 44.1, 48, 96       | ?             |
| Numark Mixtrack Pro 3                        | $300         | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 1           | 1/4" mic                                   | 1 mic          | 24         | 44.1               | likely \[17\] |
| Korg KAOSS DJ                                | $300         | 4            | 2 RCA, 1 1/4" headphone                                           | 3           | 2 RCA, 1 1/4" mic                          | 1 mic          | 24         | 44.1, 48           | ?             |
| Pioneer DDJ WeGO 3                           | $300         | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 1           | 1 1/4" mic                                 | 1 mic          | 24         | 48                 | ?             |
| Reloop Beatmix 2                             | $300         | 4            | 2 RCA, 1 1/4" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ?             |
| Reloop Beatmix 4                             | $400         | 4            | 2 RCA, 1 1/4" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | 16         | 48                 | ?             |
| Native Instruments Traktor Kontrol S2 Mk1    | discontinued | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Native Instruments Traktor Kontrol S2 Mk2    | $400         | 4            | 2 RCA, 2 1/4" balanced, 1 1/4" headphone                          | 1           | 1 1/4" mic                                 | 1 mic          | 16, 24     | 44.1, 48, 88.2, 96 | ?             |
| Reloop Terminal Mix 2                        | $500         | 4            | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1 1/4" mic                          | 1 phono, 1 mic | ?          | ?                  | ?             |
| Pioneer DDJ-SR                               | $600         | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 9           | 8 RCA, 1 XLR mic, 1 1/4" mic               | 2 phono, 1 mic | 24         | 44.1               | ?             |
| Native Instruments Traktor Kontrol S4 Mk1    | discontinued | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | yes           |
| Native Instruments Traktor Kontrol S4 Mk2    | $700         | 4            | 2 RCA, 2 1/4" balanced, 1 5-pin MIDI                              | 5           | 4 RCA, 1/4" mic, 1 5-pin MIDI              | 2 phono, 1 mic | 16, 24     | 44.1, 48, 88.2, 96 | ?             |
| Reloop Terminal Mix 8                        | $700         | 4            | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1 1/4" mic                          | 1 phono, 1 mic | ?          | ?                  | ?             |
| Native Instruments Traktor Kontrol Z2 \[18\] | $800         | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 7           | 6 RCA, 1 1/4" mic                          | 2 phono, 1 mic | 24         | 48                 | likely \[19\] |
| Pioneer DDJ-SX2                              | $1000        | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 8           | 8 RCA, 1 XLR+1/4" combo, 1 1/4" mic        | 2 phono, 2 mic | 24         | 44.1               | ?             |
| Native Instruments Traktor Kontrol S8 \[20\] | $1200        | 4            | 2 RCA, 2 1/4" balanced, 2 XLR, 1 1/4" headphone, 1 5-pin MIDI     | 5           | 4 RCA, 1 1/4" mic, 1 XLR mic, 1 5-pin MIDI | 2 phono, 1 mic | 24         | 48                 | ?             |
| Numark NS7                                   | discontinued | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Numark NS7II                                 | $1300        | 4            | 2 1/4" balanced, 2 XLR, 4 RCA, 1 1/4" headphone, 1 1/8" headphone | 10          | 8 RCA, 2 XLR+1/4" combo                    | 4 phono, 2 mic | 24         | 44.1               | ?             |
| Numark NS7III                                | $1500        | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Numark NV                                    | $700         | 4            | 4 RCA, 2 XLR, 1 1/4" headphone                                    | 3           | 2 RCA, 1 1/4" mic                          | 1 mic          | ?          | ?                  | ?             |
| Rane MP25 \[21\]                             | $1500        | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | likely \[22\] |
| Rane MP26 \[23\]                             | $1750        | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | likely \[24\] |
| Pioneer DDJ-SZ                               | $2000        | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 8           | 8 RCA, 1 XLR+1/4" combo, 1 1/4" mic        | 2 phono, 2 mic | 24         | 44.1               | ?             |
| Rane Sixty-Two \[25\]                        | $2000        | 8            | N/A                                                               | 12          | N/A                                        | 2 phono        | 24         | 48                 | ?             |
| Rane Sixty-Four \[26\]                       | $2200        | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | ?             |
| Rane Sixty-Eight \[27\]                      | $2600        | 12           | N/A                                                               | 10          | N/A                                        | 4 phono        | 24         | 48                 | ?             |
| Rane MP2015 \[28\]                           | $2900        | 10           | N/A                                                               | 14          | N/A                                        | 4 phono        | 24         | 44.1, 48, 96       | likely \[29\] |
| Rane TTM57 \[30\]                            | discontinued | 10           | N/A                                                               | 10          | N/A                                        | 2 phono        | 24         | 44.1, 48, 96       | likely \[31\] |

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

8.  This controller is similar to the Mixtrack Pro 2, which has a
    mapping. Using the Mixtrack Pro 2 mapping would probably work (for
    the most part).

9.  This is very similar to the A\&H Xone K2, which does have a mapping.
    The Xone K2 mapping may work for the Xone K1 (for the most part).

10. This controller is similar to the Mixtrack Pro 2, which has a
    mapping. Using the Mixtrack Pro 2 mapping would probably work (for
    the most part).

11. This controller is similar to the Mixtrack Pro 2, which has a
    mapping. Using the Mixtrack Pro 2 mapping would probably work (for
    the most part).

12. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

13. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

14. Fun fact: the firmware runs Linux

15. Fun fact: the firmware runs Linux

16. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

17. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

18. also a standalone analog mixer

19. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

20. also a standalone digital mixer

21. also a standalone analog mixer

22. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

23. also a standalone analog mixer

24. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

25. also a standalone analog mixer

26. also a standalone analog mixer

27. also a standalone analog mixer

28. also a standalone analog mixer

29. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

30. also a standalone analog mixer

31. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.
