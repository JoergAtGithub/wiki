# Mixxx DJ Hardware Guide

## What kind of hardware should I get to DJ with Mixxx?

Bare minimum equipment for DJing:

  - computer (preferably a laptop)
  - sound card or splitter cable
  - headphones or in-ear monitors
  - speakers
  - audio cables and adapters

Helpful but not strictly necessary:

  - controller and/or turntables with timecode vinyl
  - laptop stand
  - surge protector
  - cases for laptop, controller, and headphones
  - backpack or some other carrying case
  - portable hard drive
  - powered USB hub

To be able to hear the next track you want to mix in before your
audience hears it, you need two separate sound outputs. It is
recommended to use one sound card with at least 4 mono output channels
(2 stereo channels). Most computers come with a sound card built into
the motherboard with only 1 stereo 1/8" headphone output (2 mono
channels). While it is possible to get a splitter cable or cheap sound
card with only 2 more outputs and use it together with your onboard
sound card, it is not recommended (see [explanation
below](#Using-multiple-sound-cards)). Onboard sound cards built into
computers are generally not high quality and may pick up interference
from other devices in the computer such as the power supply or hard
drive. When mixing digitally in software on your CPU, use 2 channels for
the main output and 2 channels for your headphones (or 1 for each if
using a splitter cable). When mixing on an analog hardware mixer, which
is traditional (but not necessary) with [vinyl
control](http://mixxx.org/manual/latest/chapters/vinyl_control.html),
each deck uses 2 channels and the headphones are plugged into the analog
hardware mixer.

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
Users who want to use [vinyl
control](http://mixxx.org/manual/latest/chapters/vinyl_control.html)
will need a sound card with 2 inputs per deck (so 4 inputs for a
traditional 2 deck setup) and a phono preamp for each deck. The phono
preamps can either be in the turntable, in the sound card, or stand
alone devices. A few small controllers may be of particular interest to
vinyl DJs, particularly the Novation Dicer and Akai AMX. Some higher-end
all-in-one controllers include sound cards with phono preamps.

DJ headphones are generally better quality than typical consumer
headphones. Importantly, they are designed to have good isolation,
meaning they block outside sound. This allows the DJ to focus on the
sound in the headphones better without having to turn up the volume to
drown out sound from the monitors, PA system, and chatter. Also, DJ
headphones have hinges or flexible headbands that allow the DJ to take
off one headphone cup to hear the monitor or PA output better in one ear
and compare it to the headphone output in the other ear. When shopping
for headphones, consider how well they isolate sound and their
durability. The most frequent places that headphones break are the cable
attachment point and the headband. Look for headphones with detachable
cables, metal headbands, and other individually replaceable parts.

In-ear monitors isolate sound better than headphones but are more
expensive. Good DJ headphones can be purchased new for $150-250; IEMs
with comparable sound quality cost $350-$1000. They may be a sound
investment for musicians who play often in very loud environments to
preserve their hearing.

These are all just guidelines; research your options and decide what you
think will work best for the way you want to DJ.

See [the manual](http://mixxx.org/manual/latest/chapters/setup.html) for
diagrams and descriptions of setups with different kinds of hardware.

See the [Beginner DJ Links](Beginner%20DJ%20Links) page for more helpful
resources.

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

Unlike some proprietary DJ programs, Mixxx works with any sound card
that your operating system has a driver to use. USB sound cards
compliant with the USB audio class standard do not need any special
drivers on Linux or Mac OS X, but they do on Windows. Most USB sound
cards are not class compliant. Sound cards that are advertised for use
with iOS devices are class compliant.

Mixxx can work with any controller that sends MIDI or HID signals to
your computer; it just needs a controller mapping to tell Mixxx what to
do with the signals. Standards compliant MIDI controllers do not need
any special drivers on Linux, Mac OS X, or Windows. Standards compliant
HID controllers do not need any special drivers on Linux and Mac OS X,
but do require drivers on Windows. Most DJ controllers are standards
compliant MIDI controllers, with exceptions noted in the tables below.
Controllers that have integrated sound cards require a driver on every
OS for the sound card, unless it is USB audio class compliant.

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
    the devices ourselves. Check the wiki page and forum thread for that
    controller for an idea of the quality of the mapping.

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

Please update these tables as mappings are added to Mixxx. Keep the
tables sorted by price and move devices to the bottom of the table when
they are discontinued (keep the discontinued sections sorted
alphabetically). Be sure to add specifications for the sound cards of
controllers with integrated sound cards to the table towards the bottom.

### Mixxx Certified Mappings

Click the name of the controller for more information.

|                                                                            |                   |                                               |                       |                 |                               |
| -------------------------------------------------------------------------- | ----------------- | --------------------------------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                                                     | Price (USD) \[1\] | Description                                   | Integrated Sound Card | Signal protocol | Supported since Mixxx version |
| [Keith McMillen QuNeo](Keith%20McMillen%20QuNeo)                           | $250              | 2 deck all-in-one                             | no                    | MIDI            | 1.11                          |
| [Hercules DJ Console RMX 2](Hercules%20DJ%20Console%20RMX%202)             | $300              | 2 deck all-in-one                             | yes                   | MIDI            | 1.11                          |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)                     | $300              | 4 deck mixer + pads                           | yes                   | MIDI            | 1.11                          |
| [American Audio VMS4/4.1](American%20Audio%20VMS4)                         | $400              | 4 deck all-in-one                             | yes                   | MIDI            | 1.9                           |
| [Reloop Terminal Mix 4](Reloop%20Terminal%20Mix)                           | $400              | 4 deck all-in-one                             | yes                   | MIDI            | 1.11                          |
| [DJ TechTools MIDIFighter Classic](DJ%20TechTools%20MIDIFighter%20Classic) | discontinued      | 4x4 spring-loaded arcade button grid \[2\]    | no                    | MIDI            | 1.8                           |
| [Denon HS5500](Denon%20HS5500)                                             | discontinued      | 2-decks-in-1 CD player with motorized platter | yes                   | MIDI            | 1.12                          |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)                    | discontinued      | 2 deck all-in-one                             | yes                   | HID             | 1.11                          |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)                   | discontinued      | basic 2 deck all-in-one                       | yes                   | HID             | 1.11                          |
| [Hercules DJ Control MP3 e2](Hercules%20DJ%20Control%20MP3%20e2)           | discontinued      | basic 4 deck all-in-one                       | no                    | MIDI + HID      | 1.11                          |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)                         | discontinued      | 2 deck mixer                                  | no                    | MIDI            | 1.6                           |
| [Reloop Terminal Mix 2](Reloop%20Terminal%20Mix)                           | discontinued      | 4 deck all-in-one \[3\]                       | yes                   | MIDI            | 1.11                          |
| [Stanton SCS.3d](Stanton%20SCS.3d)                                         | discontinued      | 1 deck control \[4\]                          | no                    | MIDI            | 1.7                           |
| [Stanton SCS.3m](Stanton%20SCS.3m)                                         | discontinued      | 2 deck mixer \[5\]                            | no                    | MIDI            | 1.7                           |
| [Stanton SCS.1m](Stanton%20SCS.1m)                                         | discontinued      | 4 deck mixer                                  | yes                   | HSS1394 (MIDI)  | 1.9                           |
| [Stanton SCS.1d](Stanton%20SCS.1d)                                         | discontinued      | 1 turntable \[6\]                             | no                    | HSS1394 (MIDI)  | 1.9.1                         |
| [Vestax VCI-400](Vestax%20VCI-400)                                         | discontinued      | 4 deck all-in-one                             | yes                   | MIDI            | 1.10.1                        |

### Community Supported Mappings

All controllers listed are supported on GNU/Linux, Mac OS X, and Windows
unless otherwise indicated by a footnote in the signal protocol column.
If your controller is listed here but does not work with your OS, please
[report the bug](reporting%20bugs). All of these devices have mappings
included in Mixxx. There may be other mappings more suited to your
workflow on [the forum](http://www.mixxx.org/forums/viewforum.php?f=7).

Do not add mappings to this list until they have been included in Mixxx.
If you make a mapping for a controller, please add it to the
[\#Mappings-In-Development](#Mappings-In-Development)-table-and-[make a
pull request](midi-scripting#setting-up-git) on GitHub to include it in
Mixxx when it is ready. When the pull request is merged, move your
controller to this table.

|                                                                                                    |                   |                                                            |                                 |                 |                               |
| -------------------------------------------------------------------------------------------------- | ----------------- | ---------------------------------------------------------- | ------------------------------- | --------------- | ----------------------------- |
| Device                                                                                             | Price (USD) \[7\] | Description                                                | Integrated sound card           | Signal protocol | Supported since Mixxx version |
| [Numark DJ2GO](Numark%20DJ2GO)                                                                     | $60               | basic 2 deck all-in-one                                    | no                              | MIDI            | 1.10                          |
| [Korg nanoKONTROL 2](Korg%20nanoKONTROL%202)                                                       | $60               | hotcues + samples                                          | no                              | MIDI            | 1.11                          |
| [Akai LPD8](Akai%20LPD8)                                                                           | $70               | basic 2 deck all-in-one                                    | no                              | MIDI            | 1.10.1                        |
| [Novation Dicer](Novation%20Dicer)                                                                 | $70               | hotcues and loops for use with turntables                  | no                              | MIDI            | 1.10                          |
| [Novation Launchpad Mini](Novation%20Launchpad%20Mini)                                             | $75               | hotcues, loops, transport                                  | no                              | MIDI            | 1.12                          |
| [Electrix Tweaker](Electrix%20Tweaker)                                                             | $100              | 4 deck mixer\[8\] + transport + loops + hotcues + samplers | no, but 5-pin MIDI I/O included | MIDI            | 1.12                          |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | $100              | basic 2 deck all-in-one                                    | yes                             | MIDI            | 1.6                           |
| [Hercules DJ Control Instinct](Hercules%20DJ%20Control%20Instinct)                                 | $125              | basic 2 deck all-in-one                                    | yes                             | MIDI            | 1.10.1                        |
| [Pioneer DDJ-SB](Pioneer%20DDJ-SB)                                                                 | $250              | 4 deck all-in-one\[9\]                                     | yes                             | MIDI\[10\]      | 1.12                          |
| [American Audio VMS2](American%20Audio%20VMS2)                                                     | $250              | 2 deck all-in-one                                          | yes                             | MIDI            | ?                             |
| [Numark N4](Numark%20N4)                                                                           | $500              | 4 deck all-in-one                                          | yes                             | MIDI            | 1.10                          |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                                               | $700              | 4 deck all-in-one                                          | yes                             | MIDI            | 1.12                          |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | $900              | CD player                                                  | no                              | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | $2000             | CD player                                                  | no                              | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Akai MPD24](Akai%20MPD24)                                                                         | discontinued      | 2 deck mixer                                               | no                              | MIDI            | 1.8                           |
| [Behringer BCD2000](Behringer%20BCD2000)                                                           | discontinued      | basic 2 deck all-in-one                                    | yes                             | MIDI            | 1.11                          |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | discontinued      | CD player                                                  | no                              | MIDI            | 1.10                          |
| [Denon SC2000](Denon%20SC2000)                                                                     | discontinued      | 1 deck                                                     | no                              | MIDI            | 1.8                           |
| [DJ Tech CDJ-101](DJ%20Tech%20CDJ-101)                                                             | discontinued      | 2 deck jog wheel                                           | no                              | MIDI            | 1.11                          |
| [DJ Tech DJM-101](DJ%20Tech%20DJM-101)                                                             | discontinued      | 2 deck mixer                                               | no                              | MIDI            | 1.11                          |
| [DJ Tech iMix Reload](DJ%20Tech%20iMix%20Reload)                                                   | discontinued      | 2 deck all-in-one                                          | no                              | MIDI            | 1.10                          |
| [DJ Tech Kontrol One](DJ%20Tech%20Kontrol%20One)                                                   | discontinued      | 4 decks                                                    | no                              | MIDI            | 1.11                          |
| [DJ Tech Mixer One](DJ%20Tech%20Mixer%20One)                                                       | discontinued      | 2 deck mixer                                               | no                              | MIDI            | 1.10.1                        |
| [eks Otus](eks%20Otus)                                                                             | discontinued      | 1 turntable + 2 deck mixer                                 | yes                             | HID             | 1.11                          |
| [Evolution X-Session](Evolution%20X-Session)                                                       | discontinued      | knobs + crossfader                                         | no                              | MIDI            | 1.6                           |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | discontinued      | 2 deck mixer                                               | no                              | MIDI            | 1.6                           |
| [Gemini FirstMix](Gemini%20FirstMix)                                                               | discontinued      | basic 2 deck all-in-one                                    | no                              | MIDI            | 1.11                          |
| [Kontrol DJ KDJ500](Kontrol%20DJ%20KDJ500)                                                         | discontinued      | basic 2 deck all-in-one                                    | no                              | MIDI            | 1.10                          |
| [Korg nanoKONTROL](Korg%20nanoKONTROL)                                                             | discontinued      | 2 deck mixer                                               | no                              | MIDI            | 1.8.2                         |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | discontinued      | 2 deck all-in-one                                          | no                              | HID             | 1.11                          |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | discontinued      | 2 deck all-in-one                                          | yes                             | HID             | 1.11                          |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI \[11\]     | 1.7                           |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | discontinued      | 2 deck all-in-one                                          | yes                             | HID \[12\]      | 1.8                           |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | discontinued      | 2 deck all-in-one                                          | no                              | HID             | 1.11                          |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | discontinued      | 2 deck all-in-one                                          | no                              | MIDI            | 1.8                           |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.6                           |
| [Mixman DM2](Mixman%20DM2)                                                                         | discontinued      | 2 decks                                                    | yes                             | MIDI \[13\]     | 1.7                           |
| [Mixvibes U-Mix Control 2](Mixvibes%20U-Mix%20Control%202%20Pro)                                   | discontinued      | 2 deck all-in-one                                          | no                              | MIDI            | 1.10.1                        |
| [Mixvibes U-Mix Control 2 Pro](Mixvibes%20U-Mix%20Control%202%20Pro)                               | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.11                          |
| [Novation Launchpad Mk1](Novation%20Launchpad%20Mk1)                                               | discontinued      | 2 deck mixer, hotcues, loops                               | no                              | MIDI \[14\]     | 1.11                          |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.11                          |
| [Numark Omni Control](Numark%20Omni%20Control)                                                     | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI \[15\]     | 1.10                          |
| [Numark Total Control](Numark%20Total%20Control)                                                   | discontinued      | 2 deck all-in-one                                          | no                              | MIDI            | 1.6                           |
| [Numark Mixtrack](Numark%20Mixtrack)                                                               | discontinued      | 2 deck all-in-one                                          | no                              | MIDI            | 1.8.2                         |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.10                          |
| [Numark NS7](Numark%20NS7)                                                                         | discontinued      | 2 deck all-in-one with motorized wheels                    | yes                             | MIDI            | 1.9                           |
| [Numark V7](Numark%20V7)                                                                           | discontinued      | 2 deck motorized wheel                                     | yes                             | MIDI            | 1.10                          |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | discontinued      | CD player                                                  | no                              | MIDI or HID     | 1.8.2 (MIDI)                  |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.8                           |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI \[16\]     | 1.8                           |
| [Tascam US-428](Tascam%20US-428)                                                                   | discontinued      | mixing console                                             | yes                             | MIDI            | 1.6.2                         |
| [Vestax VCI-100](Vestax%20VCI-100)                                                                 | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.6                           |
| [Vestax VCI-300](Vestax%20VCI-300)                                                                 | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.11                          |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.9                           |
| [Vestax Spin](Vestax%20Spin)                                                                       | discontinued      | 2 deck all-in-one                                          | yes                             | MIDI            | 1.9                           |

#### Esoteric controllers

These are devices that were not designed for DJing but have been mapped
to Mixxx anyway.

|                                        |             |                         |                       |                 |                               |
| -------------------------------------- | ----------- | ----------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                 | Price (USD) | Description             | Integrated sound card | Signal protocol | Supported since Mixxx version |
| [Nintendo Wiimote](Nintendo%20Wiimote) | $25         | game console controller | no                    | HID             | 1.11                          |
| [Sony SixxAxis](Sony%20SixxAxis)       | $25         | game console controller | no                    | HID             | 1.11                          |

### Mappings In Development

These controllers have Mixxx mappings under active development. If you
are considering getting one of these controllers, you are encouraged to
do so. You can help the development of the mapping by testing it and
providing feedback to the developer. You can also [edit the mapping
yourself](start#controller%20mapping%20documentation). Click the name of
the controller for more information.

When a mapping is included in Mixxx, please move it to the [\#Mixxx
Certified Mappings](#Mixxx%20Certified%20Mappings) or [\#Community
Supported Mappings](#Community%20Supported%20Mappings) table above.

|                                                      |                    |                   |                       |                       |
| ---------------------------------------------------- | ------------------ | ----------------- | --------------------- | --------------------- |
| Device                                               | Price (USD) \[17\] | Description       | Integrated sound card | Signal protocol       |
| [Numark Mixtrack Pro 3](Numark%20Mixtrack%20Pro%203) | $250               | 2 deck all-in-one | yes                   | MIDI\[18\] (and HID?) |

### Controllers that do not yet have Mixxx mappings

This is by no means an exhaustive list; these are just DJ controllers
from popular brands. There are too many DJ controllers out there to
list. Some of these controllers may have mappings (of unverified quality
and may be incomplete) posted on [the
forums](http://www.mixxx.org/forums/viewforum.php?f=7) that have not
(yet) been included with Mixxx. If a controller you own or are
interested in getting is not listed here, [search the
forum](http://mixxx.org/forums/search.php?fid[]=7) to see if anyone has
posted a mapping. If you are willing to put in the effort to map one of
these controllers, please get the controller, map it, and publish the
mapping so we can include it in Mixxx. MIDI controllers are easier to
map than HID controllers.

|                                              |                    |                                                                         |                       |                          |
| -------------------------------------------- | ------------------ | ----------------------------------------------------------------------- | --------------------- | ------------------------ |
| Device                                       | Price (USD) \[19\] | Description                                                             | Integrated sound card | Signal protocol          |
| Behringer CMD MM-1                           | $100               | 4 deck mixer                                                            | no                    | MIDI                     |
| Numark Mixtrack Edge                         | $100               | 2 deck all-in-one                                                       | no                    | MIDI                     |
| Novation Launchpad Mk2                       | $100               | 8x8 RGB button grid                                                     | no                    | MIDI                     |
| Novation Launchpad S                         | $125               | 8x8 3-color button grid                                                 | no                    | MIDI                     |
| Numark Mixtrack 3                            | $150               | 2 deck all-in-one                                                       | no                    | MIDI\[20\] (and HID?)    |
| Native Instruments Traktor Kontrol Z1        | $200               | basic 2 deck mixer                                                      | yes                   | HID                      |
| Native Instruments Traktor Kontrol F1 \[21\] | $200               | remixing pads + faders                                                  | no                    | HID                      |
| Native Instruments Traktor Kontrol X1 Mk1    | $200               | effects                                                                 | no                    | NHL                      |
| Native Instruments Traktor Kontrol X1 Mk2    | $200               | effects + touch strip                                                   | no                    | HID                      |
| Gemini Slate                                 | $200               | 2 deck all-in-one                                                       | yes                   | MIDI                     |
| American Audio MXR 10                        | $200               | 2 deck analog mixer + MIDI library browsing and transport               | yes                   | MIDI                     |
| Akai AFX                                     | $200               | 2 deck effects + pads + touch strip                                     | no                    | MIDI                     |
| DJ Tech Tools MIDI Fighter Spectra           | discontinued       | 4x4 spring-loaded arcade button grid with LED rings                     | no                    | MIDI                     |
| DJ Tech Tools MIDI Fighter 3D                | $220               | 4x4 spring-loaded arcade button grid with LED rings + 3D motion sensing | no                    | MIDI                     |
| DJ Tech Tools MIDI Fighter Twister           | $220               | 4x4 encoder grid with LED rings and push buttons and multicolor LEDs    | no                    | MIDI                     |
| Akai AMX                                     | $250               | 2 deck mixer + vinyl hookup                                             | yes                   | MIDI                     |
| Allen & Heath Xone K1 \[22\]                 | $250               | 4 deck mixer + pads                                                     | no                    | MIDI                     |
| Gemini Slate 4                               | $250               | 4 deck all-in-one                                                       | yes                   | MIDI                     |
| Pioneer DDJ-SB2                              | $250               | 4 deck all-in-one                                                       | yes                   | MIDI                     |
| American Audio MXR 14                        | $300               | 2 deck analog mixer + MIDI library browsing and transport               | yes                   | MIDI                     |
| Hercules DJ Control Jogvision                | $300               | 2 deck all-in-one                                                       | yes                   | MIDI/HID (either? both?) |
| Korg KAOSS DJ                                | $300               | 2 deck all-in-one                                                       | yes                   | MIDI                     |
| Novation Launchpad Pro                       | $300               | 8x8 RGB velocity-sensitive button grid                                  | no                    | MIDI                     |
| Reloop Beatmix 2                             | $300               | 2 deck all-in-one                                                       | yes                   | MIDI                     |
| Pioneer DDJ WeGO 3                           | $300               | 2 deck all-in-one                                                       | yes                   | MIDI                     |
| Reloop Beatmix 4                             | $400               | 4 deck all-in-one                                                       | yes                   | MIDI                     |
| Native Instruments Traktor Kontrol S2 Mk1    | discontinued       | 2 deck all-in-one                                                       | yes                   | NHL                      |
| Native Instruments Traktor Kontrol S2 Mk2    | $400               | 2 deck all-in-one                                                       | yes                   | HID                      |
| Native Instruments Traktor Kontrol D2        | $500               | remixing pads, faders, and touch strip                                  | no                    | ?                        |
| Pioneer DDJ-SR                               | $600               | 2 deck all-in-one                                                       | yes                   | MIDI                     |
| Reloop Terminal Mix 4                        | $600               | 4 deck all-in-one                                                       | yes                   | MIDI                     |
| Livid OhmRGB                                 | $640               | 2 decks + 8x8 multicolor button grid + many encoders                    | no                    | MIDI                     |
| Livid CNTRL:R                                | $700               | 2 decks + 4x4 and 2x16 multicolor button grids + many encoders          | no                    | MIDI                     |
| Native Instruments Traktor Kontrol S4 Mk1    | discontinued       | 4 deck all-in-one                                                       | yes                   | NHL                      |
| Native Instruments Traktor Kontrol S4 Mk2    | $700               | 4 deck all-in-one                                                       | yes                   | HID                      |
| Numark NV                                    | $700               | 4 deck all-in-one                                                       | yes                   | MIDI                     |
| Reloop Terminal Mix 8                        | $700               | 4 deck all-in-one                                                       | yes                   | MIDI                     |
| Native Instruments Traktor Kontrol Z2        | $800               | 2 decks + effects + standalone digital mixer                            | yes                   | HID                      |
| Native Instruments Traktor Kontrol S8        | $1200              | 4 deck all-in-one + remixing + standalone digital mixer                 | yes                   | NHL                      |
| Pioneer DDJ-SX2                              | $1000              | 4 deck all-in-one                                                       | yes                   | MIDI                     |
| Numark NS7II                                 | $1300              | 4 deck all-in-one with motorized wheels                                 | yes                   | MIDI                     |
| Numark NS7III                                | $1500              | 4 deck all-in-one with motorized wheels                                 | yes                   | MIDI                     |
| Rane MP25                                    | $1500              | 4 deck analog mixer                                                     | yes                   | MIDI                     |
| Rane MP26                                    | $1750              | 4 deck analog mixer                                                     | yes                   | MIDI                     |
| Rane Sixty-Two                               | $2000              | 2 deck analog mixer + loops, cues, and effects                          | yes                   | MIDI                     |
| Pioneer DDJ-SZ                               | $2000              | 4 deck all-in-one                                                       | yes                   | MIDI                     |
| Rane Sixty-Four                              | $2200              | 4 deck analog mixer + loops, cues, and effects                          | yes                   | MIDI                     |
| Rane Sixty-Eight                             | $2600              | 4 deck analog mixer + loops, cues, and effects                          | yes                   | MIDI                     |
| Rane MP2015                                  | $2900              | 4 deck analog rotary mixer                                              | yes                   | MIDI                     |
| Rane TTM57                                   | discontinued       | 2 deck analog mixer + loops, cues, and effects                          | yes                   | HID                      |
| [Vestax VCI-380](Vestax%20VCI-380)           | discontinued       | 2 deck all-in-one                                                       | yes                   | MIDI                     |

#### Note regarding Native Instruments controllers

Native Instruments' newer DJ controllers are USB HID class compliant
devices
([source](http://www.native-instruments.com/en/support/knowledge-base/show/1925/i-cannot-find-the-driver-for-my-ni-device-on-the-website-mac-os-x/)).
The Windows and Mac OS X drivers can translate the HID signals to MIDI,
but this is not available on GNU/Linux. So, if you make a mapping for
these controllers, please make an HID mapping so it is compatible with
every OS that Mixxx runs on.

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
registers the signals from some of the controllers as generic Linux
input events. To get these devices to work with Mixxx on GNU/Linux,
either the driver would need to be modified to translate these signals
to HID or MIDI, Mixxx would need to be able to read Linux input events,
or a program would need to translate the Linux input events to HID or
MIDI.

### Custom caps

Most DJ gear comes with black or grey knobs and fader caps. Several
companies sell brightly colored knobs and fader caps that can replace
the standard black or grey that your gear came with. In addition to
looking cool, brighter caps can be easier to see in dark environments.
Some caps have a hard plastic slippery surface whereas others have a
rubberized surface that fingers don't slide off as much. Some DJs prefer
plastic; some prefer rubberized surfaces. Be sure to check that the caps
you order fit your controller before purchasing them.

Custom caps available:

  - [CoolorCaps](http://coolorcaps.com/)
  - [DJ Tech Tools Chroma
    Caps](https://store.djtechtools.com/products/chroma-caps-knobs-and-faders)
  - [Reloop Fader and Knob Cap
    Sets](http://www.reloop.com/fader-and-knob-cap-sets)

[Here](https://www.youtube.com/watch?v=hFyTtiLDqVA) is a video comparing
different brands.

## Sound cards

### Compatibility with Mixxx

Mixxx can use any sound card that your OS has a driver to use. The
tables below list some recommended USB soundcards for DJing. All listed
sound cards work with Mac OS X and Windows unless otherwise noted. Most
work with Linux, but not all; check the table for details.

The [ALSA sound card
matrix](http://www.alsa-project.org/main/index.php/Matrix:Main) lists
Linux-compatible soundcards. Linux users may also benefit from [these
soundcard resources for Linux
DJs](http://www.pogo.org.uk/~mark/linuxdj/), courtesy of Mark Hills, the
author of [xwax](http://www.xwax.co.uk/). If you have a Firewire/IEEE
1394 interface, the only way to use it with Linux is with JACK (not
ALSA). The FFADO project has [a list of Firewire interfaces compatible
with Linux](http://ffado.org/?q=devicesupport/list).

### Splitter cables

Splitter cables are **the cheapest way** to get two separate sound
outputs from your computer. These plug into the onboard sound card built
into computer motherboards and split the stereo signal into two separate
mono signals. However, onboard sound cards are not good quality.

Do not buy splitter cables or adapters that are not marketed as DJ
splitters. Devices marketed as "headphone splitter" cables or adapters
duplicate one stereo signal in two jacks. These cannot be used for
headphone cueing. Also, generic stereo-to-mono splitter cables or
adapters typically have two mono jack outputs. Plugging headphones or
stereo speakers into a generic stereo-to-mono splitter will only play
sound on one side of the headphones or speakers.

Mono output is a new feature in Mixxx 1.12. Older versions of Mixxx will
not work with splitter cables.

Available DJ splitter cables:

  - [Native Instruments Traktor DJ
    Cable](http://www.native-instruments.com/en/products/traktor/traktor-for-ios/traktor-dj-cable/):
    $10
  - [Griffin DJ
    Cable](https://griffintechnology.com/us/products/audio/dj-accessories/dj-cable):
    $20

### What to look for in a sound card

As explained [at the top of the
page](#What-hardware-is-needed-to-DJ-with-Mixxx?), it is recommended to
use a sound card with at least 4 mono output channels with Mixxx.
Playing audio at 16 bit sample depths and 44.1 kHz sample rate is fine
for DJing; almost all music is published in this format (which was the
standard set by audio CDs). If you are interested in recording music,
consider getting a higher quality sound card that supports 24 bit sample
depths and a 96 kHz sample rate (there is [no
advantage](http://xiph.org/~xiphmont/demo/neil-young.html) of 192 kHz
sample rates).

Laptops do not always have the most reliable power output to their USB
ports, so the ability to use a separate power adapter for your sound
card can be an advantage. Also, sound cards with power adapters can
generally output stronger signals. A lack of an external power supply
can especially be an issue for sound cards built into controllers
because one USB port has to power both the lights on the controller and
the sound card. However, sound cards that are USB bus powered can be
used with a laptop and battery powered speakers for a completely battery
powered setup.

If you are unfamiliar with professional audio equipment, read Digital DJ
Tips' [Essential Guide to Audio Cables for
DJs](http://www.digitaldjtips.com/2011/07/the-essential-guide-to-audio-cables-for-djs/)
to understand the different kinds of connectors on sound cards. It is
better to use a sound card with balanced outputs, especially if you will
run long cables directly into an amplifier or active speakers without
going through an analog mixer. Balanced signals reject interference and
are less susceptible to ground loop hum issues (which can be a problem
when plugging unbalanced gear into separate power sources). However,
most venues have DJs plug into analog DJ mixers, which typically only
have RCA inputs (RCA cables cannot be balanced). Most home/computer
speakers have RCA and/or 1/8" TRS stereo inputs. Most live sound mixers
have balanced 1/4" TRS mono inputs. If you need to interconnect balanced
and unbalanced gear, see [this
guide](http://www.presonus.com/news/articles/balanced-unbalanced) from
Presonus and [this guide](http://www.rane.com/note110.html) from Rane.

If you want to plug a microphone into your sound card, it will need a
microphone preamplifier. If you want to plug an electric guitar or bass
into your sound card, it will need an instrument preamplifier.

If you want to use [vinyl
control](http://mixxx.org/manual/latest/chapters/vinyl_control.html), it
is best to have phono preamplifiers (one for each deck) somewhere
between your turntable and sound card to boost the turntable's phono
level signal to line level. Mixxx can amplify phono level signals in
software, but it is better to do it in hardware. The phono preamp can be
in the turntable, in the sound card, or a stand alone device. Many
higher-end all-in-one controllers include sound cards with phono
preamps.

Sound cards often have multiple connectors for a single channel,
resulting in more connectors than channels. So, not every connector can
send or receive an independent signal. Some sound cards made for DJing
have 4 output channels with 4 mono output connectors and 1 stereo
headphone connector. This does not mean that the sound card can send out
6 different signals at the same time; rather, the signal on 2 of the
mono outputs and the stereo headphone output would be the same.

When considering specifications, higher dynamic range, higher
signal-to-noise ratio (SNR), higher maximum output level, lower THD+N
(more negative dB value or smaller percentage), and lower crosstalk
(more negative dB value) are better.

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

Many extremely cheap ($1-$10) 2 channel output USB sound cards that look
like USB flash drives are available, but these tend to be very poor
quality, even worse than onboard sound cards.

See [this video](https://www.youtube.com/watch?v=bBi6ecfm-Oo) for a
comparison of cheap DJ sound cards. Note that it does not include the
Numark DJ iO 1 or 2 though.

|                                                                                                                                                                                                                                                |                         |                         |                                                                  |                           |                                                                            |                                      |            |                    |                                   |               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------------- | ---------------------------------------------------------------- | ------------------------- | -------------------------------------------------------------------------- | ------------------------------------ | ---------- | ------------------ | --------------------------------- | ------------- |
| Device                                                                                                                                                                                                                                         | Price (USD) \[23\]      | Channels out            | Output connectors                                                | Channels in               | Input connectors                                                           | Preamps                              | Bit depths | Sample rates (kHz) | power adapter                     | Linux         |
| [Behringer U-Control UCA202](http://www.music-group.com/Categories/Behringer/Computer-Audio/Audio-Interfaces/UCA202/p/P0484) & [UCA222](http://www.music-group.com/Categories/Behringer/Computer-Audio/Audio-Interfaces/UCA222/p/P0A31) \[24\] | $30                     | 2                       | 2 RCA, 1 1/8" headphone, 1 SPDIF Toslink                         | 2                         | 2 RCA                                                                      | none                                 | 16         | 32, 44.1, 48       | no                                | yes           |
| [Behringer U-Phono UFO202](http://mixxx.org/forums/viewtopic.php?f=6&t=2438)                                                                                                                                                                   | $30                     | 2                       | 2 RCA, 1 1/8" headphone                                          | 2                         | 2 RCA                                                                      | 1 phono                              | 16         | 32, 44.1, 48       | no                                | yes           |
| [Numark Stereo iO](http://www.numark.com/product/stereoio)                                                                                                                                                                                     | $50                     | 2                       | 2 RCA                                                            | 2                         | 4 RCA                                                                      | 1 phono                              | 16         | 44.1               | no                                | likely \[25\] |
| [Numark DJ iO](http://www.numark.com/product/djio)                                                                                                                                                                                             | $50                     | 4                       | 4 RCA, 1 1/4" headphone                                          | 1                         | 1 1/4" mic                                                                 | 1 mic                                | 24         | 44.1, 88.2         | optional                          | no            |
| [Griffin DJ Connect](https://griffintechnology.com/us/products/audio/dj-accessories/dj-connect) \[26\]                                                                                                                                         | $90                     | 4                       | 2 RCA, 1 1/8" headphone                                          | 0                         | none                                                                       | none                                 | 16         | 48                 | no                                | likely \[27\] |
| [Numark DJ iO 2](http://www.numark.com/product/djio-2)                                                                                                                                                                                         | $100                    | 4                       | 2 RCA, 1 1/4" headphone                                          | 1                         | 1 1/4" mic                                                                 | 1 mic                                | 24         | 44.1               | no                                | likely \[28\] |
| [Native Instruments Traktor Audio 2 DJ (Mk2)](http://www.native-instruments.com/en/products/traktor/dj-audio-interfaces/traktor-audio-2/)                                                                                                      | $100                    | 4                       | 2 1/8" stereo                                                    | 0                         | none                                                                       | none                                 | 24         | 44.1, 48, 88.2, 96 | optional, sold separately for $25 | likely \[29\] |
| Native Instruments [Traktor Audio 2](Traktor%20Audio%202) (Mk1)                                                                                                                                                                                | discontinued (was $120) | 4                       | 2 1/4" stereo                                                    | 0                         | none                                                                       | none                                 | 24         | 44.1, 48, 88.2, 96 | no                                | yes           |
| Electrix Ebox-44                                                                                                                                                                                                                               | discontinued (was $100) | 4                       | 4 RCA, 1 1/4" headphone                                          | 5                         | 4 RCA, 1 1/4" mic                                                          | 2 phono (one switch for both), 1 mic | 16         | 44.1, 48           | no                                | yes           |
| [Mixvibes U-Mix44](http://www.mixvibes.com/products/u-mix-44)                                                                                                                                                                                  | discontinued (was $100) | 4                       | 4 RCA, 1 1/8" headphone                                          | 5                         | 4 RCA, 1 1/4" mic                                                          | 2 phono, 1 mic                       | 16         | 48                 | no                                | yes           |
| [Reloop Play](http://www.reloop.com/reloop-play)                                                                                                                                                                                               | $130                    | 4                       | 4 RCA, 1 1/4" headphone                                          | 0                         | none                                                                       | none                                 | 24         | 96                 | no                                | yes           |
| [Focusrite Scarlett 2i4](http://us.focusrite.com/usb-audio-interfaces/scarlett-2i4)                                                                                                                                                            | $200                    | 4                       | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 5-pin MIDI           | 2                         | 2 XLR+1/4" balanced combo, 1 5-pin MIDI                                    | 2 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | no                                | yes           |
| [Native Instruments Komplete Audio 6](http://www.native-instruments.com/en/products/komplete/audio-interfaces/komplete-audio-6-migrated/included-software/)                                                                                    | $230                    | 6 (4 analog, 2 digital) | 4 1/4" balanced, 1 1/4" headphone, 1 5-pin MIDI, 1 optical SPDIF | 6 (4 analog, 2 digital)   | 2 XLR+1/4" balanced, 2 1/4" balanced, 1 5-pin MIDI, 1 optical SPDIF        | 2 mic, 2 instrument                  | 16, 24     | 44.1, 48, 96       | no                                | yes           |
| [Focusrite Scarlett 6i6](http://us.focusrite.com/usb-audio-interfaces/scarlett-6i6/)                                                                                                                                                           | $250                    | 6 (4 analog, 2 digital) | 4 1/4" balanced, 2 1/4" headphone, 1 5-pin MIDI, 1 optical SPDIF | 6 (4 analog, 2 digital)   | 2 XLR+1/4" balanced combo, 2 1/4" balanced, 1 5-pin MIDI, 1 optical SPDIF  | 2 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | yes                               | yes           |
| [Native Instruments Traktor Scratch A6](http://www.native-instruments.com/en/products/traktor/digital-vinyl/traktor-scratch-a6/)                                                                                                               | $300                    | 6                       | 6 RCA, 1 1/4" headphone                                          | 6                         | 6 RCA                                                                      | 2 phono                              | 16, 24     | 44.1, 48, 88.2, 96 | optional                          | yes           |
| [Audient iD14](http://audient.com/products/id14)                                                                                                                                                                                               | $300                    | 4                       | 2 1/4" balanced, 1 1/4" headphone                                | 2                         | 2 1/4" balanced/XLR combo, 1 1/4" TS instrument                            | 2 mic, 1 instrument                  | 24         | 44.1, 48, 88.2, 96 | optional                          | ?             |
| [Focusrite Scarlett 18i8](http://us.focusrite.com/usb-audio-interfaces/scarlett-18i8)                                                                                                                                                          | $350                    | 8 (6 analog, 2 digital) | 2 1/4" balanced, 2 1/4" headphone, 1 5-pin MIDI, 1 optical SPDIF | 18 (8 analog, 10 digital) | 4 XLR+1/4" balanced combo, 4 1/4" blanced, 1 optical SPDIF, 1 optical ADAT | 4 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | yes                               | yes           |
| [Native Instruments Traktor Scratch A10](http://www.native-instruments.com/en/products/traktor/digital-vinyl/traktor-scratch-a10/)                                                                                                             | $500                    | 10                      | 10 RCA, 1 1/4" headphone                                         | 10                        | 10 RCA, 1 1/4" mic                                                         | 4 phono, 1 mic                       | 16, 24     | 44.1, 48, 88.2, 96 | optional                          | ?             |
| [Rane SL2](http://dj.rane.com/products/sl2-for-serato-scratch-live)                                                                                                                                                                            | $500                    | 4                       | 4 RCA                                                            | 4                         | 4 RCA                                                                      | 2 phono                              | 24         | 44.1, 48           | optional                          | no            |
| [Rane SL3](http://dj.rane.com/products/sl3-for-serato-scratch-live)                                                                                                                                                                            | $700                    | 6                       | 6 RCA                                                            | 6                         | 6 RCA                                                                      | 3 phono                              | 24         | 44.1, 48           | optional                          | no            |
| [Rane SL4](http://dj.rane.com/products/sl4-for-serato-scratch-live)                                                                                                                                                                            | $900                    | 8                       | 8 RCA                                                            | 8                         | 8 RCA                                                                      | 4 phono                              | 24         | 48, 96             | optional                          | no            |
| [ESI MAYA 44 USB](http://www.esi-audio.de/produkte/maya44usb/)                                                                                                                                                                                 | discontinued            | 4                       | 4 RCA, 1 1/8" headphone, 1 optical SPDIF                         | 4                         | 4 RCA                                                                      | none                                 | 16         | 44.1 48            | no                                | no            |

### Sound cards integrated into controllers

#### Controllers with Mixxx mappings

|                                                                      |                    |              |                                                            |             |                                                                          |                |            |                    |       |
| -------------------------------------------------------------------- | ------------------ | ------------ | ---------------------------------------------------------- | ----------- | ------------------------------------------------------------------------ | -------------- | ---------- | ------------------ | ----- |
| Device                                                               | Price (USD) \[30\] | Channels out | Output connectors                                          | Channels in | Input connectors                                                         | Preamps        | Bit depths | Sample rates (kHz) | Linux |
| [Behringer BCD3000](Behringer%20BCD3000)                             | $100               | 4            | 2 RCA, 1 1/4" headphone                                    | 5           | 4 RCA, 1 XLR mic                                                         | 2 phono, 1 mic | 24         | 44.1               | yes   |
| [Hercules DJ Control Instinct](Hercules%20DJ%20Control%20Instinct)   | $125               | 4            | 2 RCA, 2 1/8" stereo                                       | 0           | none                                                                     | none           | 16         | 44.1               | yes   |
| [Hercules DJ Console RMX 2](Hercules%20DJ%20Console%20RMX%202)       | $200               | 4            | 2 XLR, 2 RCA, 2 1/4" headphone                             | 5           | 4 RCA, 1 XLR                                                             | 2 phono, 1 mic | 24         | 44.1, 48, 88.2, 96 | yes   |
| [American Audio VMS2](American%20Audio%20VMS2)                       | $250               | 4            | 2 XLR, 4 RCA, 1 1/4" headphone                             | 4           | 4 RCA, 1 XLR mic, 1 1/4" mic                                             | 2 phono, 1 mic | 16         | 44.1               | yes   |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)               | $300               | 4            | 2 RCA, 1 1/8" headphone                                    | 0           | none                                                                     | none           | 16         | 48                 | yes   |
| [Reloop Terminal Mix 4](Reloop%20Terminal%20Mix)                     | $400               | 4            | 4 RCA, 2 1/4" balanced, 1 1/4" headphone, 1 1/8" headphone | 3           | 2 RCA, 1/4" mic                                                          | 1 phono, 1 mic | ?          | ?                  | ?     |
| [Numark N4](Numark%20N4)                                             | $500               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone, 1 1/8" headphone           | 4           | 4 RCA                                                                    | 2 phono        | 16         | 44.1               | ?     |
| [Denon MC6000Mk2](Denon%20MC6000Mk2)                                 | $700               | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone            | 9           | 8 RCA, 1 1/4" mic, 1 XLR mic                                             | 4 phono, 1 mic | 24         | 44.1               | ?     |
| [Behringer BCD2000](Behringer%20BCD2000)                             | discontinued       | 4            | 2 RCA, 1 1/4" headphone                                    | 5           | 4 RCA, 1 XLR                                                             | 2 phono, 1 mic | 24         | 44.1               | yes   |
| [Denon HS5500](Denon%20HS5500)                                       | discontinued       | ?            | ?                                                          | ?           | ?                                                                        | ?              | 16         | 44.1               | ?     |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)             | discontinued       | 4            | 4 1/4" balanced, 4 RCA, 2 1/4" headphone                   | 5           | 4 RCA, 1 1/4" mic                                                        | 2 phono, 1 mic | 16, 24     | 44.1, 96           | yes   |
| [Mixvibes U-Mix Control 2 Pro](Mixvibes%20U-Mix%20Control%202%20Pro) | discontinued       | 4            | 4 RCA, 1 1/4" headphone, 1 1/8" headphone                  | 5           | 4 RCA, 1 1/4" mic                                                        | 2 phono, 1 mic | ?          | ?                  | ?     |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)               | discontinued       | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                  | 1           | 1/4" mic                                                                 | 1 mic          | 16         | 44.1, 48           | yes   |
| [Numark Omni Control](Numark%20Omni%20Control)                       | discontinued       | 4            | 4 RCA, 1 1/4" headphone                                    | 1           | 1/14" mic                                                                | 1 mic          | 24         | 44.1, 88.2         | no    |
| [Reloop Terminal Mix 2](Reloop%20Terminal%20Mix)                     | discontinued       | 4            | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 1/8" headphone | 3           | 2 RCA, 1 1/4" mic                                                        | 1 phono, 1 mic | ?          | ?                  | ?     |
| [Tascam US-428](Tascam%20US-428)                                     | discontinued       | 2            | 2 RCA, 1 optical SPDIF, 2 5-pin MIDI                       | 4           | 2 1/4" balanced, 2 1/4" unbalanced, 2 XLR, 1 optical SPDIF, 2 5-pin MIDI | ?              | 24         | 48                 | yes   |

#### Controllers with no Mixxx mappings yet

|                                              |                    |              |                                                                   |             |                                            |                |            |                    |               |
| -------------------------------------------- | ------------------ | ------------ | ----------------------------------------------------------------- | ----------- | ------------------------------------------ | -------------- | ---------- | ------------------ | ------------- |
| Device                                       | Price (USD) \[31\] | Channels out | Output connectors                                                 | Channels in | Input connectors                           | Preamps        | Bit depths | Sample rates (kHz) | Linux         |
| Native Instruments Traktor Kontrol Z1        | $200               | 4            | 2 RCA, 1 1/8" headphone                                           | 0           | none                                       | none           | 24         | 96                 | yes           |
| American Audio MXR 10 \[32\]                 | $200               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone                                    | 5           | 4 RCA, 1 1/4" mic                          | 2 phono, 1 mic | 24         | 48                 | ?             |
| Gemini Slate                                 | $200               | 4            | 2 RCA, 1 1/8" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ? \[33\]      |
| Gemini Slate 4                               | $250               | 4            | 2 RCA, 1 1/8" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ? \[34\]      |
| Akai AMX                                     | $250               | 4            | 2 RCA, 1 1/8" headphone                                           | 4           | 4 RCA                                      | 2 phono        | 24         | 96                 | likely \[35\] |
| Numark Mixtrack Pro 3                        | $250               | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 1           | 1/4" mic                                   | 1 mic          | 24         | 44.1               | yes           |
| Pioneer DDJ-SB                               | $250               | 4            | 2 1/4" balanced, 2 RCA, 1 1/4" headphone, 1 1/8" headphone        | 1           | 1 1/4" mic                                 | 1 mic          | 24         | 44.1               | yes           |
| American Audio MXR 14 \[36\]                 | $300               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone                                    | 6           | 4 RCA, 2 XLR mic                           | 2 phono, 2 mic | 24         | 48                 | ?             |
| Hercules DJ Control Jogvision                | $300               | 4            | 4 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 3           | 1/4" mic, 1/8" stereo                      | 1 mic          | 16, 24     | 44.1, 48, 96       | ?             |
| Korg KAOSS DJ                                | $300               | 4            | 2 RCA, 1 1/4" headphone                                           | 3           | 2 RCA, 1 1/4" mic                          | 1 mic          | 24         | 44.1, 48           | ?             |
| Pioneer DDJ WeGO 3                           | $300               | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 1           | 1 1/4" mic                                 | 1 mic          | 24         | 48                 | ?             |
| Reloop Beatmix 2                             | $300               | 4            | 2 RCA, 1 1/4" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ?             |
| Reloop Beatmix 4                             | $400               | 4            | 2 RCA, 1 1/4" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | 16         | 48                 | ?             |
| Native Instruments Traktor Kontrol S2 Mk1    | discontinued       | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Native Instruments Traktor Kontrol S2 Mk2    | $400               | 4            | 2 RCA, 2 1/4" balanced, 1 1/4" headphone                          | 1           | 1 1/4" mic                                 | 1 mic          | 16, 24     | 44.1, 48, 88.2, 96 | ?             |
| Pioneer DDJ-SR                               | $600               | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 9           | 8 RCA, 1 XLR mic, 1 1/4" mic               | 2 phono, 1 mic | 24         | 44.1               | ?             |
| Native Instruments Traktor Kontrol S4 Mk1    | discontinued       | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | yes           |
| Native Instruments Traktor Kontrol S4 Mk2    | $700               | 4            | 2 RCA, 2 1/4" balanced, 1 5-pin MIDI                              | 5           | 4 RCA, 1/4" mic, 1 5-pin MIDI              | 2 phono, 1 mic | 16, 24     | 44.1, 48, 88.2, 96 | ?             |
| Reloop Terminal Mix 8                        | $700               | 4            | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1 1/4" mic                          | 1 phono, 1 mic | ?          | ?                  | ?             |
| Native Instruments Traktor Kontrol Z2 \[37\] | $800               | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 7           | 6 RCA, 1 1/4" mic                          | 2 phono, 1 mic | 24         | 48                 | likely \[38\] |
| Pioneer DDJ-SX2                              | $1000              | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 8           | 8 RCA, 1 XLR+1/4" combo, 1 1/4" mic        | 2 phono, 2 mic | 24         | 44.1               | ?             |
| Native Instruments Traktor Kontrol S8 \[39\] | $31200             | 4            | 2 RCA, 2 1/4" balanced, 2 XLR, 1 1/4" headphone, 1 5-pin MIDI     | 5           | 4 RCA, 1 1/4" mic, 1 XLR mic, 1 5-pin MIDI | 2 phono, 1 mic | 24         | 48                 | ?             |
| Numark NS7                                   | discontinued       | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Numark NS7II                                 | $1300              | 4            | 2 1/4" balanced, 2 XLR, 4 RCA, 1 1/4" headphone, 1 1/8" headphone | 10          | 8 RCA, 2 XLR+1/4" combo                    | 4 phono, 2 mic | 24         | 44.1               | ?             |
| Numark NS7III                                | $1500              | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Numark NV                                    | $700               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone                                    | 3           | 2 RCA, 1 1/4" mic                          | 1 mic          | ?          | ?                  | ?             |
| Rane MP25 \[40\]                             | $1500              | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | likely \[41\] |
| Rane MP26 \[42\]                             | $1750              | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | likely \[43\] |
| Pioneer DDJ-SZ                               | $2000              | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 8           | 8 RCA, 1 XLR+1/4" combo, 1 1/4" mic        | 2 phono, 2 mic | 24         | 44.1               | ?             |
| Rane Sixty-Two \[44\]                        | $2000              | 8            | N/A                                                               | 12          | N/A                                        | 2 phono        | 24         | 48                 | ?             |
| Rane Sixty-Four \[45\]                       | $2200              | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | ?             |
| Rane Sixty-Eight \[46\]                      | $2600              | 12           | N/A                                                               | 10          | N/A                                        | 4 phono        | 24         | 48                 | ?             |
| Rane MP2015 \[47\]                           | $2900              | 10           | N/A                                                               | 14          | N/A                                        | 4 phono        | 24         | 44.1, 48, 96       | likely \[48\] |
| Rane TTM57 \[49\]                            | discontinued       | 10           | N/A                                                               | 10          | N/A                                        | 2 phono        | 24         | 44.1, 48, 96       | likely \[50\] |

1.  Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

2.  The default Mixxx mapping has this mapped to hotcues.

3.  Mapping has buttons to toggle between decks 1/3 and decks 2/4.

4.  Mapping supports 2-deck switching

5.  Mapping supports 4-deck switching

6.  Mapping supports n-deck switching

7.  Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

8.  This controller has physical controls for 2 decks, but deck toggle
    buttons in the Mixxx mapping allow it to control 4 decks.

9.  This controller is designed for 2 decks, but the Mixxx mapping has
    buttons to toggle between decks 1/3 and 2/4.

10. High resolution MIDI

11. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Mac OS X. There is no
    driver available for Linux or Windows.

12. with MIDI driver. For Linux support, see [this forum
    thread](http://mixxx.org/forums/viewtopic.php?f=3&t=5064)

13. [Mac OS X driver](http://www.joemattiello.com/dm2/); [Linux MIDI
    Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz), [Alternate
    Linux MIDI driver
    (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2),
    [dm2linux on
    sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453)

14. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

15. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

16. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

17. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

18. High resolution MIDI

19. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

20. High resolution MIDI

21. This device has a Mixxx mapping started, but it does not do much
    yet.

22. This is very similar to the A\&H Xone K2, which does have a mapping.
    The Xone K2 mapping may work for the Xone K1 (for the most part).

23. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

24. The only difference between the Behringer U-Control UCA202 & UCA222
    are the color and the software they are bundled with.

25. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

26. Not compatible with Windows.

27. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

28. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

29. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

30. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

31. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

32. also a standalone analog mixer

33. Fun fact: the firmware runs Linux

34. Fun fact: the firmware runs Linux

35. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

36. also a standalone analog mixer

37. also a standalone analog mixer

38. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

39. also a standalone digital mixer

40. also a standalone analog mixer

41. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

42. also a standalone analog mixer

43. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

44. also a standalone analog mixer

45. also a standalone analog mixer

46. also a standalone analog mixer

47. also a standalone analog mixer

48. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

49. also a standalone analog mixer

50. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.
