# Mixxx DJ Hardware Guide

## What kind of hardware should I get to DJ with Mixxx?

It is recommended to use one sound card with at least 4 mono output
channels (2 stereo channels). Most computers come with a sound card
built into the motherboard with only 1 stereo 1/8" headphone output (2
mono channels). While it is possible to get a cheap sound card with only
2 more outputs and use it together with your onboard sound card, it is
not recommended (see [explanation below](#Using-multiple-sound-cards)).
Onboard sound cards built into computers are generally not high quality
and may pick up interference from other devices in the computer such as
the power supply or hard drive. When mixing digitally in software on
your CPU, use 2 channels for the main output and 2 channels for your
headphones. This allows you to hear and prepare the track you want to
play next without your audience hearing it until you are ready to mix it
into the main output. When mixing on an analog hardware mixer, which is
traditional (but not necessary) with [vinyl
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
vinyl DJs, such as the Novation Dicer and Akai AMX. Some higher-end
all-in-one controllers include sound cards with phono preamps. These are
all just guidelines; research your options and decide what you think
will work best for the way you want to DJ.

See [the manual](http://mixxx.org/manual/latest/chapters/setup.html) for
diagrams and descriptions of setups with different kinds of hardware.

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
to use. USB sound cards compliant with the USB audio class standard do
not need any special drivers on Linux or Mac OS X, but they do on
Windows. Most USB sound cards are not standards compliant. Sound cards
that are advertised for use with iOS devices are standards compliant.

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

Please update these tables as mappings are added to Mixxx. Keep the
tables sorted by price. Be sure to add specifications for the sound
cards of controllers with integrated sound cards to the table towards
the bottom.

### Mixxx Certified Mappings

|                                                                                            |                   |                                               |                       |                 |                               |
| ------------------------------------------------------------------------------------------ | ----------------- | --------------------------------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                                                                     | Price (USD) \[1\] | Description                                   | Integrated Sound Card | Signal protocol | Supported since Mixxx version |
| [Keith McMillen QuNeo](Keith%20McMillen%20QuNeo)                                           | $250              | 2 deck all-in-one                             | no                    | MIDI            | 1.11                          |
| [Hercules DJ Console RMX 2](http://www.hercules.com/us/DJ-Music/bdd/p/193/djconsole-rmx-2) | $300              | 2 deck all-in-one                             | yes                   | MIDI            | 1.11                          |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)                                     | $300              | 4 deck mixer + pads                           | yes                   | MIDI            | 1.11                          |
| [American Audio VMS4](American%20Audio%20VMS4)                                             | $400              | 4 deck all-in-one                             | yes                   | MIDI            | 1.9                           |
| [Reloop Terminal Mix](Reloop%20Terminal%20Mix) 4                                           | $400              | 4 deck all-in-one                             | yes                   | MIDI            | 1.11                          |
| [DJ TechTools MIDIFighter](http://midifighter.com)                                         | discontinued      | 4x4 spring-loaded arcade button grid \[2\]    | no                    | MIDI            | 1.8                           |
| [Denon HS5500](Denon%20HS5500)                                                             | discontinued      | 2-decks-in-1 CD player with motorized platter | yes                   | MIDI            | 1.12                          |
| [eks Otus](eks%20Otus)                                                                     | discontinued      | 1 turntable + 2 deck mixer                    | no                    | HID             | 1.11                          |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)                                    | discontinued      | 2 deck all-in-one                             | yes                   | HID             | 1.11                          |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)                                   | discontinued      | basic 2 deck all-in-one                       | yes                   | HID             | 1.11                          |
| [Hercules DJ Control MP3 e2](Hercules%20DJ%20Control%20MP3%20e2)                           | discontinued      | basic 4 deck all-in-one                       | no                    | MIDI + HID      | 1.11                          |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)                                         | discontinued      | 2 deck mixer                                  | no                    | MIDI            | 1.6                           |
| [Reloop Terminal Mix](Reloop%20Terminal%20Mix) 2                                           | discontinued      | 4 deck all-in-one \[3\]                       | yes                   | MIDI            | 1.11                          |
| [Stanton SCS.3d](Stanton%20SCS.3d)                                                         | discontinued      | 1 deck control                                | no                    | MIDI            | 1.7                           |
| [Stanton SCS.3m](Stanton%20SCS.3m)                                                         | discontinued      | 2 deck mixer                                  | no                    | MIDI            | 1.7                           |
| [Stanton SCS.1m](Stanton%20SCS.1m)                                                         | discontinued      | 4 deck mixer                                  | yes                   | MIDI            | 1.9                           |
| [Stanton SCS.1d](Stanton%20SCS.1d)                                                         | discontinued      | 1 turntable                                   | no                    | MIDI            | 1.9.1                         |
| [Vestax VCI-400](Vestax%20VCI-400)                                                         | discontinued      | 4 deck all-in-one                             | yes                   | MIDI            | 1.10.1                        |

### Community Supported Mappings

All controllers listed are supported on GNU/Linux, Mac OS X, and Windows
unless otherwise indicated by a footnote in the signal protocol column.
If your controller is listed here but does not work with your OS, please
[report the bug](reporting%20bugs).

|                                                                                                    |                   |                                           |                       |                 |                               |
| -------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                                                                             | Price (USD) \[4\] | Description                               | Integrated sound card | Signal protocol | Supported since Mixxx version |
| [Numark DJ2GO](Numark%20DJ2GO)                                                                     | $60               | basic 2 deck all-in-one                   | no                    | MIDI            | 1.10                          |
| [Korg nanoKONTROL 2](Korg%20nanoKONTROL%202)                                                       | $60               | hotcues + samples                         | no                    | MIDI            | 1.11                          |
| [Akai LPD8](Akai%20LPD8)                                                                           | $70               | basic 2 deck all-in-one                   | no                    | MIDI            | 1.10.1                        |
| [Novation Dicer](Novation%20Dicer)                                                                 | $70               | hotcues and loops for use with turntables | no                    | MIDI            | 1.10                          |
| [Novation Launchpad Mini](Novation%20Launchpad%20Mini)                                             | $75               | hotcues, loops, transport                 | no                    | MIDI            | 1.12                          |
| [DJ Tech CDJ-101](DJ%20Tech%20CDJ-101)                                                             | $90               | 2 deck jog wheel                          | no                    | MIDI            | 1.11                          |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | $100              | basic 2 deck all-in-one                   | yes                   | MIDI            | 1.6                           |
| [Hercules DJ Control Instinct](Hercules%20DJ%20Control%20Instinct)                                 | $125              | basic 2 deck all-in-one                   | yes                   | MIDI            | 1.10.1                        |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | $250              | 2 deck all-in-one                         | yes                   | MIDI            | 1.11                          |
| [Numark N4](Numark%20N4)                                                                           | $500              | 4 deck all-in-one                         | yes                   | MIDI            | 1.10                          |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                                               | $700              | 4 deck all-in-one                         | yes                   | MIDI            | 1.12                          |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | $900              | CD player                                 | no                    | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | $2000             | CD player                                 | no                    | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       |
| [Akai MPD24](Akai%20MPD24)                                                                         | discontinued      | 2 deck mixer                              | no                    | MIDI            | 1.8                           |
| [Behringer BCD2000](Behringer%20BCD2000)                                                           | discontinued      | basic 2 deck all-in-one                   | yes                   | MIDI            | 1.11                          |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | discontinued      | CD player                                 | no                    | MIDI            | 1.10                          |
| [Denon SC2000](http://esync.de/denon-sc2000-mixxx-bindings)                                        | discontinued      | 1 deck                                    | no                    | MIDI            | 1.8                           |
| [DJ Tech DJM-101](DJ%20Tech%20DJM-101)                                                             | discontinued      | 2 deck mixer                              | no                    | MIDI            | 1.11                          |
| [DJ Tech iMix Reload](DJ%20Tech%20iMix%20Reload)                                                   | discontinued      | 2 deck all-in-one                         | no                    | MIDI            | 1.10                          |
| [DJ Tech Kontrol One](DJ%20Tech%20Kontrol%20One)                                                   | discontinued      | 4 decks                                   | no                    | MIDI            | 1.11                          |
| [DJ Tech Mixer One](DJ%20Tech%20Mixer%20One)                                                       | discontinued      | 2 deck mixer                              | no                    | MIDI            | 1.10.1                        |
| [Evolution X-Session](Evolution%20X-Session)                                                       | discontinued      | knobs + crossfader                        | no                    | MIDI            | 1.6                           |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | discontinued      | 2 deck mixer                              | no                    | MIDI            | 1.6                           |
| [Gemini FirstMix](Gemini%20FirstMix)                                                               | discontinued      | basic 2 deck all-in-one                   | no                    | MIDI            | 1.11                          |
| [Kontrol DJ KDJ500](Kontrol%20DJ%20KDJ500)                                                         | discontinued      | basic 2 deck all-in-one                   | no                    | MIDI            | 1.10                          |
| [Korg nanoKONTROL](Korg%20nanoKONTROL)                                                             | discontinued      | 2 deck mixer                              | no                    | MIDI            | 1.8.2                         |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | discontinued      | 2 deck all-in-one                         | no                    | HID             | 1.11                          |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | discontinued      | 2 deck all-in-one                         | yes                   | HID             | 1.11                          |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | discontinued      | 2 deck all-in-one                         | yes                   | MIDI \[5\]      | 1.7                           |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | discontinued      | 2 deck all-in-one                         | yes                   | HID \[6\]       | 1.8                           |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | discontinued      | 2 deck all-in-one                         | no                    | HID             | 1.11                          |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | discontinued      | 2 deck all-in-one                         | no                    | MIDI            | 1.8                           |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | discontinued      | 2 deck all-in-one                         | yes                   | MIDI            | 1.6                           |
| [Mixman DM2](Mixman%20DM2)                                                                         | discontinued      | 2 decks                                   | yes                   | MIDI \[7\]      | 1.7                           |
| [Mixvibes U-Mix Control 2](Mixvibes%20U-Mix%20Control%202)                                         | discontinued      | 2 deck all-in-one                         | no                    | MIDI            | 1.10.1                        |
| [Novation Launchpad Mk1](Novation%20Launchpad%20Mk1)                                               | discontinued      | 2 deck mixer, hotcues, loops              | no                    | MIDI \[8\]      | 1.11                          |
| [Numark Omni Control](Numark%20Omni%20Control)                                                     | discontinued      | 2 deck all-in-one                         | yes                   | MIDI \[9\]      | 1.10                          |
| [Mixvibes U-Mix Control 2 Pro](Mixvibes%20U-Mix%20Control%202%20Pro)                               | discontinued      | 2 deck all-in-one                         | yes                   | MIDI            | 1.11                          |
| [Numark Total Control](Numark%20Total%20Control)                                                   | discontinued      | 2 deck all-in-one                         | no                    | MIDI            | 1.6                           |
| [Numark Mixtrack](Numark%20Mixtrack)                                                               | discontinued      | 2 deck all-in-one                         | no                    | MIDI            | 1.8.2                         |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | discontinued      | 2 deck all-in-one                         | yes                   | MIDI            | 1.10                          |
| [Numark NS7](Numark%20NS7)                                                                         | discontinued      | 2 deck all-in-one with motorized wheels   | yes                   | MIDI            | 1.9                           |
| [Numark V7](Numark%20V7)                                                                           | discontinued      | 2 deck motorized wheel                    | yes                   | MIDI            | 1.10                          |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | discontinued      | CD player                                 | no                    | MIDI or HID     | 1.8.2 (MIDI)                  |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | discontinued      | 2 deck all-in-one                         | yes                   | MIDI            | 1.8                           |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | discontinued      | 2 deck all-in-one                         | yes                   | MIDI \[10\]     | 1.8                           |
| [Tascam US-428](Tascam%20US-428)                                                                   | discontinued      | mixing console                            | yes                   | MIDI            | 1.6.2                         |
| [Vestax VCI-100](Vestax%20VCI-100)                                                                 | discontinued      | 2 deck all-in-one                         | yes                   | MIDI            | 1.6                           |
| [Vestax VCI-300](Vestax%20VCI-300)                                                                 | discontinued      | 2 deck all-in-one                         | yes                   | MIDI            | 1.11                          |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | discontinued      | 2 deck all-in-one                         | yes                   | MIDI            | 1.9                           |
| [Vestax Spin](Vestax%20Spin)                                                                       | discontinued      | 2 deck all-in-one                         | yes                   | MIDI            | 1.9                           |

#### Esoteric controllers

These are devices that were not designed for DJing but have been mapped
to Mixxx anyway.

|                                        |             |                         |                       |                 |                               |
| -------------------------------------- | ----------- | ----------------------- | --------------------- | --------------- | ----------------------------- |
| Device                                 | Price (USD) | Description             | Integrated sound card | Signal protocol | Supported since Mixxx version |
| [Nintendo Wiimote](Nintendo%20Wiimote) | $25         | game console controller | no                    | HID             | 1.11                          |
| [Sony SixxAxis](Sony%20SixxAxis)       | $25         | game console controller | no                    | HID             | 1.11                          |

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

|                                              |                    |                                                                                |                                 |                          |
| -------------------------------------------- | ------------------ | ------------------------------------------------------------------------------ | ------------------------------- | ------------------------ |
| Device                                       | Price (USD) \[11\] | Description                                                                    | Integrated sound card           | Signal protocol          |
| Electrix Tweaker                             | $100               | 2 deck mixer + 8x4 multicolor button grid + 4x2 velocity sensitive button grid | no, but 5-pin MIDI I/O included | MIDI                     |
| Behringer CMD MM-1                           | $100               | 4 deck mixer                                                                   | no                              | MIDI                     |
| Numark Mixtrack Edge                         | $100               | 2 deck all-in-one                                                              | no                              | MIDI                     |
| Novation Launchpad S                         | $125               | 8x8 3-color button grid                                                        | no                              | MIDI                     |
| Numark Mixtrack 2 \[12\]                     | $150               | 2 deck all-in-one                                                              | no                              | MIDI                     |
| Native Instruments Traktor Kontrol Z1        | $200               | basic 2 deck mixer                                                             | yes                             | HID                      |
| Native Instruments Traktor Kontrol F1 \[13\] | $200               | remixing pads + faders                                                         | no                              | HID                      |
| Native Instruments Traktor Kontrol X1 Mk1    | $200               | effects                                                                        | no                              | NHL                      |
| Native Instruments Traktor Kontrol X1 Mk2    | $200               | effects + touch strip                                                          | no                              | HID                      |
| Gemini Slate                                 | $200               | 2 deck all-in-one                                                              | yes                             | MIDI                     |
| Allen & Heath Xone K1 \[14\]                 | $250               | 4 deck mixer + pads                                                            | no                              | MIDI                     |
| Numark Mixtrack 3 \[15\]                     | $200               | 2 deck all-in-one                                                              | no                              | MIDI                     |
| American Audio MXR 10                        | $200               | 2 deck analog mixer + MIDI library browsing and transport                      | yes                             | MIDI                     |
| Akai AFX                                     | $200               | 2 deck effects + pads + touch strip                                            | no                              | MIDI                     |
| DJ Tech Tools MIDI Fighter Spectra           | discontinued       | 4x4 spring-loaded arcade button grid with LED rings                            | no                              | MIDI                     |
| DJ Tech Tools MIDI Fighter 3D                | $220               | 4x4 spring-loaded arcade button grid with LED rings + 3D motion sensing        | no                              | MIDI                     |
| DJ Tech Tools MIDI Fighter Twister           | $220               | 4x4 encoder grid with LED rings and push buttons and multicolor LEDs           | no                              | MIDI                     |
| Akai AMX                                     | $250               | 2 deck mixer + vinyl hookup                                                    | yes                             | MIDI                     |
| Gemini Slate 4                               | $250               | 4 deck all-in-one                                                              | yes                             | MIDI                     |
| Pioneer DDJ-SB                               | $250               | 2 deck all-in-one                                                              | yes                             | MIDI                     |
| American Audio MXR 14                        | $300               | 2 deck analog mixer + MIDI library browsing and transport                      | yes                             | MIDI                     |
| Hercules DJ Control Jogvision                | $300               | 2 deck all-in-one                                                              | yes                             | MIDI/HID (either? both?) |
| Korg KAOSS DJ                                | $300               | 2 deck all-in-one                                                              | yes                             | MIDI                     |
| Novation Launchpad Pro                       | $300               | 8x8 RGB velocity-sensitive button grid                                         | no                              | MIDI                     |
| Numark Mixtrack Pro 3 \[16\]                 | $300               | 2 deck all-in-one                                                              | yes                             | MIDI                     |
| Reloop Beatmix 2                             | $300               | 2 deck all-in-one                                                              | yes                             | MIDI                     |
| Pioneer DDJ WeGO 3                           | $300               | 2 deck all-in-one                                                              | yes                             | MIDI                     |
| Reloop Beatmix 4                             | $400               | 4 deck all-in-one                                                              | yes                             | MIDI                     |
| Native Instruments Traktor Kontrol S2 Mk1    | discontinued       | 2 deck all-in-one                                                              | yes                             | NHL                      |
| Native Instruments Traktor Kontrol S2 Mk2    | $400               | 2 deck all-in-one                                                              | yes                             | HID                      |
| Native Instruments Traktor Kontrol D2        | $500               | remixing pads, faders, and touch strip                                         | no                              | ?                        |
| Pioneer DDJ-SR                               | $600               | 2 deck all-in-one                                                              | yes                             | MIDI                     |
| Reloop Terminal Mix 4                        | $600               | 4 deck all-in-one                                                              | yes                             | MIDI                     |
| Livid OhmRGB                                 | $640               | 2 decks + 8x8 multicolor button grid + many encoders                           | no                              | MIDI                     |
| Livid CNTRL:R                                | $700               | 2 decks + 4x4 and 2x16 multicolor button grids + many encoders                 | no                              | MIDI                     |
| Native Instruments Traktor Kontrol S4 Mk1    | discontinued       | 4 deck all-in-one                                                              | yes                             | NHL                      |
| Native Instruments Traktor Kontrol S4 Mk2    | $700               | 4 deck all-in-one                                                              | yes                             | HID                      |
| Numark NV                                    | $700               | 4 deck all-in-one                                                              | yes                             | MIDI                     |
| Reloop Terminal Mix 8                        | $700               | 4 deck all-in-one                                                              | yes                             | MIDI                     |
| Native Instruments Traktor Kontrol Z2        | $800               | 2 decks + effects + standalone digital mixer                                   | yes                             | HID                      |
| Native Instruments Traktor Kontrol S8        | $1200              | 4 deck all-in-one + remixing + standalone digital mixer                        | yes                             | NHL                      |
| Pioneer DDJ-SX2                              | $1000              | 4 deck all-in-one                                                              | yes                             | MIDI                     |
| Numark NS7II                                 | $1300              | 4 deck all-in-one with motorized wheels                                        | yes                             | MIDI                     |
| Numark NS7III                                | $1500              | 4 deck all-in-one with motorized wheels                                        | yes                             | MIDI                     |
| Rane MP25                                    | $1500              | 4 deck analog mixer                                                            | yes                             | MIDI                     |
| Rane MP26                                    | $1750              | 4 deck analog mixer                                                            | yes                             | MIDI                     |
| Rane Sixty-Two                               | $2000              | 2 deck analog mixer + loops, cues, and effects                                 | yes                             | MIDI                     |
| Pioneer DDJ-SZ                               | $2000              | 4 deck all-in-one                                                              | yes                             | MIDI                     |
| Rane Sixty-Four                              | $2200              | 4 deck analog mixer + loops, cues, and effects                                 | yes                             | MIDI                     |
| Rane Sixty-Eight                             | $2600              | 4 deck analog mixer + loops, cues, and effects                                 | yes                             | MIDI                     |
| Rane MP2015                                  | $2900              | 4 deck analog rotary mixer                                                     | yes                             | MIDI                     |
| Rane TTM57                                   | discontinued       | 2 deck analog mixer + loops, cues, and effects                                 | yes                             | MIDI                     |

#### Note regarding Native Instruments controllers

Native Instruments' newer DJ controllers are USB HID class compliant
devices. The Windows and Mac OS X drivers can translate the HID signals
to MIDI, but this is not available on GNU/Linux. So, if you make a
mapping for these controllers, please make an HID mapping so it is
compatible with every OS that Mixxx runs on.

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

## Sound cards

### Compatibility with Mixxx

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
output louder signals. A lack of an external power supply can especially
be an issue for sound cards built into controllers because one USB port
has to power both the lights on the controller and the sound card.
However, sound cards that are USB bus powered can be used with a laptop
and battery powered speakers for a completely battery powered setup.

If you are unfamiliar with professional audio equipment, read Digital DJ
Tips' [Essential Guide to Audio Cables for
DJs](http://www.digitaldjtips.com/2011/07/the-essential-guide-to-audio-cables-for-djs/)
to understand the different kinds of connectors on sound cards. It is
better to use a sound card with balanced outputs, especially if you will
run long cables directly into an amplifier or active speakers without
going through an analog DJ mixer. Balanced signals reject interference
and are less susceptible to ground loop hum issues (which can be a
problem when plugging unbalanced gear into separate power sources).
However, most venues have DJs plug into analog DJ mixers, which
typically only have RCA inputs (RCA cables cannot be balanced). Most
home/computer speakers have RCA and/or 1/8" TRS stereo inputs. Most live
sound mixers have balanced 1/4" TRS mono inputs. If you need to
interconnect balanced and unbalanced gear, see [this
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

When considering specifications, higher dynamic range, higher
signal-to-noise ratio (SNR), and lower THD+N (more negative dB value),
and lower crosstalk (more negative dB value) are better.

Sound cards often have multiple connectors for a single channel,
resulting in more connectors than channels. So, not every connector can
send or receive an independent signal. Some sound cards made for DJing
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

Many extremely cheap ($1-$10) 2 channel output USB sound cards that look
like USB flash drives are available, but these tend to be very poor
quality, even worse than onboard sound cards.

|                                                                              |                         |                         |                                                                  |                           |                                                                            |                                      |            |                    |                                   |               |
| ---------------------------------------------------------------------------- | ----------------------- | ----------------------- | ---------------------------------------------------------------- | ------------------------- | -------------------------------------------------------------------------- | ------------------------------------ | ---------- | ------------------ | --------------------------------- | ------------- |
| Device                                                                       | Price (USD) \[17\]      | Channels out            | Output connectors                                                | Channels in               | Input connectors                                                           | Preamps                              | Bit depths | Sample rates (kHz) | power adapter                     | Linux         |
| Behringer U-Control UCA202 & UCA222 \[18\]                                   | $30                     | 2                       | 2 RCA, 1 1/8" headphone, 1 SPDIF Toslink                         | 2                         | 2 RCA                                                                      | none                                 | 16         | 32, 44.1, 48       | no                                | yes           |
| [Behringer U-Phono UFO202](http://mixxx.org/forums/viewtopic.php?f=6&t=2438) | $30                     | 2                       | 2 RCA, 1 1/8" headphone                                          | 2                         | 2 RCA                                                                      | 1 phono                              | 16         | 32, 44.1, 48       | no                                | yes           |
| Numark Stereo iO                                                             | $50                     | 2                       | 2 RCA                                                            | 2                         | 4 RCA                                                                      | 1 phono                              | 16         | 44.1               | no                                | likely \[19\] |
| Numark DJ iO                                                                 | $50                     | 4                       | 4 RCA, 1 1/4" headphone                                          | 1                         | 1 1/4" mic                                                                 | 1 mic                                | 24         | 44.1, 88.2         | optional                          | no            |
| Griffin DJ Connect \[20\]                                                    | $90                     | 4                       | 2 RCA, 1 1/8" headphone                                          | 0                         | none                                                                       | none                                 | 16         | 48                 | no                                | likely \[21\] |
| Numark DJ iO 2                                                               | $100                    | 4                       | 2 RCA, 1 1/4" headphone                                          | 1                         | 1 1/4" mic                                                                 | 1 mic                                | 24         | 44.1               | no                                | likely \[22\] |
| Native Instruments Traktor Audio 2 DJ (Mk2)                                  | $100                    | 4                       | 2 1/8" stereo                                                    | 0                         | none                                                                       | none                                 | 24         | 44.1, 48, 88.2, 96 | optional, sold separately for $25 | likely \[23\] |
| Native Instruments [Traktor Audio 2](Traktor%20Audio%202) (Mk1)              | discontinued (was $120) | 4                       | 2 1/4" stereo                                                    | 0                         | none                                                                       | none                                 | 24         | 44.1, 48, 88.2, 96 | no                                | yes           |
| Electrix Ebox-44                                                             | discontinued (was $100) | 4                       | 4 RCA, 1 1/4" headphone                                          | 5                         | 4 RCA, 1 1/4" mic                                                          | 2 phono (one switch for both), 1 mic | 16         | 44.1, 48           | no                                | yes           |
| Mixvibes U-Mix44                                                             | discontinued (was $100) | 4                       | 4 RCA, 1 1/8" headphone                                          | 5                         | 4 RCA, 1 1/4" mic                                                          | 2 phono, 1 mic                       | 16         | 48                 | no                                | yes           |
| Reloop Play                                                                  | $130                    | 4                       | 4 RCA, 1 1/4" headphone                                          | 0                         | none                                                                       | none                                 | 24         | 96                 | no                                | yes           |
| Focusrite Scarlett 2i4                                                       | $200                    | 4                       | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 5-pin MIDI           | 2                         | 2 XLR+1/4" balanced combo, 1 5-pin MIDI                                    | 2 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | no                                | yes           |
| Native Instruments Komplete Audio 6                                          | $230                    | 6 (4 analog, 2 digital) | 4 1/4" balanced, 1 1/4" headphone, 1 5-pin MIDI, 1 optical SPDIF | 6 (4 analog, 2 digital)   | 2 XLR+1/4" balanced, 2 1/4" balanced, 1 5-pin MIDI, 1 optical SPDIF        | 2 mic, 2 instrument                  | 16, 24     | 44.1, 48, 96       | no                                | yes           |
| Focusrite Scarlett 6i6                                                       | $250                    | 6 (4 analog, 2 digital) | 4 1/4" balanced, 2 1/4" headphone, 1 5-pin MIDI, 1 optical SPDIF | 6 (4 analog, 2 digital)   | 2 XLR+1/4" balanced combo, 2 1/4" balanced, 1 5-pin MIDI, 1 optical SPDIF  | 2 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | yes                               | yes           |
| Native Instruments Traktor Scratch A6                                        | $300                    | 6                       | 6 RCA, 1 1/4" headphone                                          | 6                         | 6 RCA                                                                      | 2 phono                              | 16, 24     | 44.1, 48, 88.2, 96 | optional                          | yes           |
| Focusrite Scarlett 18i8                                                      | $350                    | 8 (6 analog, 2 digital) | 2 1/4" balanced, 2 1/4" headphone, 1 5-pin MIDI, 1 optical SPDIF | 18 (8 analog, 10 digital) | 4 XLR+1/4" balanced combo, 4 1/4" blanced, 1 optical SPDIF, 1 optical ADAT | 4 mic, 2 instrument                  | 24         | 44.1, 48, 88.2, 96 | yes                               | yes           |
| Native Instruments Traktor Scratch A10                                       | $500                    | 10                      | 10 RCA, 1 1/4" headphone                                         | 10                        | 10 RCA, 1 1/4" mic                                                         | 4 phono, 1 mic                       | 16, 24     | 44.1, 48, 88.2, 96 | optional                          | ?             |
| Rane SL2                                                                     | $500                    | 4                       | 4 RCA                                                            | 4                         | 4 RCA                                                                      | 2 phono                              | 24         | 44.1, 48           | optional                          | no            |
| Rane SL3                                                                     | $700                    | 6                       | 6 RCA                                                            | 6                         | 6 RCA                                                                      | 3 phono                              | 24         | 44.1, 48           | optional                          | no            |
| Rane SL4                                                                     | $900                    | 8                       | 8 RCA                                                            | 8                         | 8 RCA                                                                      | 4 phono                              | 24         | 48, 96             | optional                          | no            |
| [ESI MAYA 44 USB](http://www.esi-audio.de/produkte/maya44usb/)               | discontinued            | 4                       | 4 RCA, 1 1/8" headphone, 1 optical SPDIF                         | 4                         | 4 RCA                                                                      | none                                 | 16         | 44.1 48            | no                                | no            |

### Sound cards integrated into controllers

#### Controllers with Mixxx mappings

|                              |                    |              |                                                            |             |                                                                          |                |            |                    |       |
| ---------------------------- | ------------------ | ------------ | ---------------------------------------------------------- | ----------- | ------------------------------------------------------------------------ | -------------- | ---------- | ------------------ | ----- |
| Device                       | Price (USD) \[24\] | Channels out | Output connectors                                          | Channels in | Input connectors                                                         | Preamps        | Bit depths | Sample rates (kHz) | Linux |
| Behringer BCD3000            | $100               | 4            | 2 RCA, 1 1/4" headphone                                    | 5           | 4 RCA, 1 XLR mic                                                         | 2 phono, 1 mic | 24         | 44.1               | yes   |
| Numark Mixtrack Pro 2        | $250               | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                  | 1           | 1/4" mic                                                                 | 1 mic          | 16         | 44.1, 48           | yes   |
| Hercules DJ Console RMX 2    | $300               | 4            | 2 XLR, 2 RCA, 2 1/4" headphone                             | 5           | 4 RCA, 1 XLR                                                             | 2 phono, 1 mic | 24         | 44.1, 48, 88.2, 96 | yes   |
| Allen & Heath Xone K2        | $300               | 4            | 2 RCA, 1 1/8" headphone                                    | 0           | none                                                                     | none           | 16         | 48                 | yes   |
| Reloop Terminal Mix 4        | $400               | 4            | 4 RCA, 2 1/4" balanced, 1 1/4" headphone, 1 1/8" headphone | 3           | 2 RCA, 1/4" mic                                                          | 1 phono, 1 mic | ?          | ?                  | ?     |
| Numark N4                    | $500               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone, 1 1/8" headphone           | 4           | 4 RCA                                                                    | 2 phono        | 16         | 44.1               | ?     |
| Denon MC6000 Mk2             | $700               | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone            | 9           | 8 RCA, 1 1/4" mic, 1 XLR mic                                             | 4 phono, 1 mic | 24         | 44.1               | ?     |
| Behringer BCD2000            | discontinued       | 4            | 2 RCA, 1 1/4" headphone                                    | 5           | 4 RCA, 1 XLR                                                             | 2 phono, 1 mic | 24         | 44.1               | yes   |
| Denon DN-HS550               | discontinued       | ?            | ?                                                          | ?           | ?                                                                        | ?              | 16         | 44.1               | ?     |
| Hercules DJ Console RMX      | discontinued       | 4            | 4 1/4" balanced, 4 RCA, 2 1/4" headphone                   | 5           | 4 RCA, 1 1/4" mic                                                        | 2 phono, 1 mic | 16, 24     | 44.1, 96           | yes   |
| Mixvibes U-Mix Control Pro 2 | discontinued       | 4            | 4 RCA, 1 1/4" headphone, 1 1/8" headphone                  | 5           | 4 RCA, 1 1/4" mic                                                        | 2 phono, 1 mic | ?          | ?                  | ?     |
| Numark Omni Control          | discontinued       | 4            | 4 RCA, 1 1/4" headphone                                    | 1           | 1/14" mic                                                                | 1 mic          | 24         | 44.1, 88.2         | no    |
| Reloop Terminal Mix 2        | discontinued       | 4            | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 1/8" headphone | 3           | 2 RCA, 1 1/4" mic                                                        | 1 phono, 1 mic | ?          | ?                  | ?     |
| Tascam US-428                | discontinued       | 2            | 2 RCA, 1 optical SPDIF, 2 5-pin MIDI                       | 4           | 2 1/4" balanced, 2 1/4" unbalanced, 2 XLR, 1 optical SPDIF, 2 5-pin MIDI | ?              | 24         | 48                 | yes   |

#### Controllers with no Mixxx mappings yet

|                                              |                    |              |                                                                   |             |                                            |                |            |                    |               |
| -------------------------------------------- | ------------------ | ------------ | ----------------------------------------------------------------- | ----------- | ------------------------------------------ | -------------- | ---------- | ------------------ | ------------- |
| Device                                       | Price (USD) \[25\] | Channels out | Output connectors                                                 | Channels in | Input connectors                           | Preamps        | Bit depths | Sample rates (kHz) | Linux         |
| Hercules DJ Control Instinct                 | $125               | 4            | 2 RCA, 2 1/8" stereo                                              | 0           | none                                       | none           | 16         | 44.1               | yes           |
| Native Instruments Traktor Kontrol Z1        | $200               | 4            | 2 RCA, 1 1/8" headphone                                           | 0           | none                                       | none           | 24         | 96                 | yes           |
| American Audio MXR 10 \[26\]                 | $200               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone                                    | 5           | 4 RCA, 1 1/4" mic                          | 2 phono, 1 mic | 24         | 48                 | ?             |
| Gemini Slate                                 | $200               | 4            | 2 RCA, 1 1/8" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ? \[27\]      |
| Gemini Slate 4                               | $250               | 4            | 2 RCA, 1 1/8" headphone                                           | 1           | 1/4" mic                                   | 1 mic          | ?          | ?                  | ? \[28\]      |
| Akai AMX                                     | $250               | 4            | 2 RCA, 1 1/8" headphone                                           | 4           | 4 RCA                                      | 2 phono        | 24         | 96                 | likely \[29\] |
| Pioneer DDJ-SB                               | $250               | 4            | 2 1/4" balanced, 2 RCA, 1 1/4" headphone, 1 1/8" headphone        | 1           | 1 1/4" mic                                 | 1 mic          | 24         | 44.1               | yes           |
| American Audio MXR 14 \[30\]                 | $300               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone                                    | 6           | 4 RCA, 2 XLR mic                           | 2 phono, 2 mic | 24         | 48                 | ?             |
| Hercules DJ Control Jogvision                | $300               | 4            | 4 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 3           | 1/4" mic, 1/8" stereo                      | 1 mic          | 16, 24     | 44.1, 48, 96       | ?             |
| Numark Mixtrack Pro 3                        | $300               | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 1           | 1/4" mic                                   | 1 mic          | 24         | 44.1               | likely \[31\] |
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
| Native Instruments Traktor Kontrol Z2 \[32\] | $800               | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 7           | 6 RCA, 1 1/4" mic                          | 2 phono, 1 mic | 24         | 48                 | likely \[33\] |
| Pioneer DDJ-SX2                              | $1000              | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 8           | 8 RCA, 1 XLR+1/4" combo, 1 1/4" mic        | 2 phono, 2 mic | 24         | 44.1               | ?             |
| Native Instruments Traktor Kontrol S8 \[34\] | $1200              | 4            | 2 RCA, 2 1/4" balanced, 2 XLR, 1 1/4" headphone, 1 5-pin MIDI     | 5           | 4 RCA, 1 1/4" mic, 1 XLR mic, 1 5-pin MIDI | 2 phono, 1 mic | 24         | 48                 | ?             |
| Numark NS7                                   | discontinued       | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Numark NS7II                                 | $1300              | 4            | 2 1/4" balanced, 2 XLR, 4 RCA, 1 1/4" headphone, 1 1/8" headphone | 10          | 8 RCA, 2 XLR+1/4" combo                    | 4 phono, 2 mic | 24         | 44.1               | ?             |
| Numark NS7III                                | $1500              | ?            | ?                                                                 | ?           | ?                                          | ?              | ?          | ?                  | ?             |
| Numark NV                                    | $700               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone                                    | 3           | 2 RCA, 1 1/4" mic                          | 1 mic          | ?          | ?                  | ?             |
| Rane MP25 \[35\]                             | $1500              | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | likely \[36\] |
| Rane MP26 \[37\]                             | $1750              | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | likely \[38\] |
| Pioneer DDJ-SZ                               | $2000              | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone, 1 1/8" headphone | 8           | 8 RCA, 1 XLR+1/4" combo, 1 1/4" mic        | 2 phono, 2 mic | 24         | 44.1               | ?             |
| Rane Sixty-Two \[39\]                        | $2000              | 8            | N/A                                                               | 12          | N/A                                        | 2 phono        | 24         | 48                 | ?             |
| Rane Sixty-Four \[40\]                       | $2200              | 10           | N/A                                                               | 12          | N/A                                        | 4 phono        | 24         | 48                 | ?             |
| Rane Sixty-Eight \[41\]                      | $2600              | 12           | N/A                                                               | 10          | N/A                                        | 4 phono        | 24         | 48                 | ?             |
| Rane MP2015 \[42\]                           | $2900              | 10           | N/A                                                               | 14          | N/A                                        | 4 phono        | 24         | 44.1, 48, 96       | likely \[43\] |
| Rane TTM57 \[44\]                            | discontinued       | 10           | N/A                                                               | 10          | N/A                                        | 2 phono        | 24         | 44.1, 48, 96       | likely \[45\] |

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

3.  This controller is designed for 2 decks, but the Mixxx mapping has
    buttons to toggle between decks 1/3 and decks 2/4.

4.  Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

5.  This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Mac OS X. There is no
    driver available for Linux or Windows.

6.  with MIDI driver. For Linux support, see [this forum
    thread](http://mixxx.org/forums/viewtopic.php?f=3&t=5064)

7.  [Mac OS X driver](http://www.joemattiello.com/dm2/); [Linux MIDI
    Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz), [Alternate
    Linux MIDI driver
    (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2),
    [dm2linux on
    sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453)

8.  This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

9.  This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

10. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

11. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

12. This controller is similar to the Mixtrack Pro 2, which has a
    mapping. Using the Mixtrack Pro 2 mapping would probably work (for
    the most part).

13. This device has a Mixxx mapping started, but it does not do much
    yet.

14. This is very similar to the A\&H Xone K2, which does have a mapping.
    The Xone K2 mapping may work for the Xone K1 (for the most part).

15. This controller is similar to the Mixtrack Pro 2, which has a
    mapping. Using the Mixtrack Pro 2 mapping would probably work (for
    the most part).

16. This controller is similar to the Mixtrack Pro 2, which has a
    mapping. Using the Mixtrack Pro 2 mapping would probably work (for
    the most part).

17. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

18. The only difference between the Behringer U-Control UCA202 & UCA222
    are the color and the software they are bundled with.

19. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

20. Not compatible with Windows.

21. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

22. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

23. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

24. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

25. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop). You may be able to find
    hardware available for sale cheaper. Devices are marked as
    discontinued if the manufacturer has declared them as discontinued,
    the manufacturer has gone out of business, or new units are not
    widely available online. They may or may not still be available used
    online. If the price of a device has dropped or it has been
    discontinued, please update this page.

26. also a standalone analog mixer

27. Fun fact: the firmware runs Linux

28. Fun fact: the firmware runs Linux

29. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

30. also a standalone analog mixer

31. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

32. also a standalone analog mixer

33. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

34. also a standalone digital mixer

35. also a standalone analog mixer

36. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

37. also a standalone analog mixer

38. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

39. also a standalone analog mixer

40. also a standalone analog mixer

41. also a standalone analog mixer

42. also a standalone analog mixer

43. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

44. also a standalone analog mixer

45. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.
