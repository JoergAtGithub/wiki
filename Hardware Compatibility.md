# Mixxx DJ Hardware Guide

## What kind of hardware should I get to DJ with Mixxx?

Bare minimum equipment for DJing:

  - computer (preferably a laptop)
  - [splitter cable](#splitter-cables) or [sound card](#sound-cards)
  - [headphones](DJ%20headphones)
  - speakers
  - audio cables and adapters

Helpful but not strictly necessary:

  - [sound card](#sound-cards) with 4 mono outputs (2 stereo pairs)
  - [controller](#controllers) and/or [turntables with timecode
    vinyl](http://mixxx.org/manual/latest/chapters/vinyl_control.html)
  - [laptop stand](laptop%20stands)
  - surge protector
  - cases for laptop, controller, and headphones
  - backpack or other carrying case
  - mouse
  - portable hard drive
  - powered USB hub
  - [custom fader and knob caps](custom%20caps) to customize your gear

See [the manual](http://mixxx.org/manual/latest/chapters/setup.html) for
diagrams and descriptions of setups with different kinds of hardware.

See the [Beginner DJ Links](Beginner%20DJ%20Links) page for more helpful
resources.

## Hardware compatibility

Because Mixxx is [free
software](http://www.gnu.org/philosophy/free-sw.html) — free as in
artistic freedom, not just price — we strive to make it work with as
much hardware as we can. Mixxx is collaboratively developed by a
community of volunteers and we can only make mappings for controllers
that we have. If hardware does not work with Mixxx, that does not mean
it is impossible, it only means that no one has made it work with Mixxx
yet. Anyone, including you, who has the hardware is welcome to make
Mixxx work with it.

Mixxx can work with any controller that sends MIDI or HID signals to
your computer; it just needs a controller mapping to tell Mixxx what to
do with the signals. Standards compliant MIDI controllers do not need
any special drivers on Linux, Mac OS X, or Windows. Standards compliant
HID controllers do not need any special drivers. Most DJ controllers are
standards compliant MIDI controllers, with exceptions noted in the
tables below.

Controllers that have integrated sound cards often have a USB Audio
Class compliant sound card. Sound cards that aren't USB Audio Class
compliant need a driver for each OS. USB Audio Class compliant sound
cards, both stand-alone and integrated into controllers, do not need any
special drivers for Linux or Mac OS X. On Windows, they can be used
without any special drivers, but a driver is needed from the
manufacturer to use the recommended [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api).
Sound cards that are advertised for use with iOS devices are class
compliant.

Unlike some proprietary DJ programs, Mixxx works with any sound card
that your operating system has a driver to use—including for timecode
vinyl (DVS) use.

## Controllers

Controllers are devices with knobs, buttons, and other components that
provide hands-on control of computer software such as Mixxx. They do not
actually mix audio themselves; they send signals to a computer that tell
Mixxx how to manipulate the music. While it is possible to use Mixxx
with just a keyboard & mouse, controllers make it much easier to access
Mixxx's features and perform typical DJing techniques. Many DJ
controllers also have a built-in [sound card](#sound-cards) providing 4
channels of audio (2 stereo pairs) for separate main and headphone
outputs.

Mixxx can be made to work with any standards compliant USB MIDI or USB
HID controller by mapping the controller's signals to manipulate
controls in Mixxx. The Mixxx developers and community have made a number
of mappings for MIDI and HID controllers. There are two different levels
of controller support in Mixxx:

  - Mixxx Certified Support: mappings verified by the Mixxx Development
    Team
  - Community Support: mappings provided by the Mixxx Community, but the
    Mixxx Team is unable to verify their quality because we don't have
    the devices ourselves. Check the wiki page and forum thread for
    information about the completeness of the mapping.

If your controller does not have a mapping, refer to the
[start\#controller mapping
documentation](start#controller%20mapping%20documentation) for how to
make a mapping. Feel free to ask for help mapping your controller on the
forums. If you ask for help, please consider that most people reading
your post will not have your controller, so be specific about what kind
of controller you have and what you want to map it to do.

Please update these tables as mappings are added to Mixxx. Keep the
tables sorted by price and move devices to the bottom of the table when
they are discontinued (keep the discontinued sections sorted
alphabetically). Be sure to add specifications for the sound cards of
controllers with integrated sound cards to the table towards the bottom.

### Mixxx Certified Mappings

Click the name of the controller for more information.

\<sortable 2=numeric\>

| Device                                                                           | Price (USD) \[1\] | Description                                   | Integrated Sound Card | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------------------------------------------------- | ----------------- | --------------------------------------------- | --------------------- | --------------- | ----------------------------- | -------- |
| [Hercules DJ Control MP3 e2 / MP3 LE / Glow](Hercules%20DJ%20Control%20MP3%20e2) | $90               | basic 4 deck all-in-one \[2\]                 | no                    | USB Bulk        | 1.11                          | 2009     |
| [Keith McMillen QuNeo](Keith%20McMillen%20QuNeo)                                 | $250              | miscellaneous                                 | no                    | MIDI            | 1.11                          | 2012     |
| [Hercules DJ Console RMX 2](Hercules%20DJ%20Console%20RMX%202)                   | $300              | 2 deck all-in-one                             | yes                   | MIDI            | 1.11                          | 2012     |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)                           | $300              | 4 deck mixer + pads                           | yes                   | MIDI            | 1.11                          | 2012     |
| [American Audio VMS4/4.1](American%20Audio%20VMS4)                               | $400              | 4 deck all-in-one                             | yes                   | MIDI            | 1.9                           | 2012     |
| [DJ TechTools MIDIFighter Classic](DJ%20TechTools%20MIDIFighter%20Classic)       | discontinued      | 4x4 spring-loaded arcade button grid \[3\]    | no                    | MIDI            | 1.8                           | 2011     |
| [Denon HS5500](Denon%20HS5500)                                                   | discontinued      | 2-decks-in-1 CD player with motorized platter | yes                   | MIDI            | 2.0                           | 2008     |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)                          | discontinued      | 2 deck all-in-one                             | yes                   | HID             | 1.11                          | 2008     |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)                         | discontinued      | basic 2 deck all-in-one                       | yes                   | HID             | 1.11                          | 2008     |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)                               | discontinued      | 2 deck mixer                                  | no                    | MIDI            | 1.6                           | 2007     |
| [Stanton SCS.3d](Stanton%20SCS.3d)                                               | discontinued      | 1 deck control \[4\]                          | no                    | MIDI            | 1.7                           | 2009     |
| [Stanton SCS.3m](Stanton%20SCS.3m)                                               | discontinued      | 2 deck mixer \[5\]                            | no                    | MIDI            | 1.7                           | 2009     |
| [Stanton SCS.1m](Stanton%20SCS.1m)                                               | discontinued      | 4 deck mixer                                  | yes                   | HSS1394 (MIDI)  | 1.7                           | 2009     |
| [Stanton SCS.1d](Stanton%20SCS.1d)                                               | discontinued      | 1 turntable \[6\]                             | no                    | HSS1394 (MIDI)  | 1.9.1                         | 2009     |
| [Vestax VCI-400](Vestax%20VCI-400)                                               | discontinued      | 4 deck all-in-one                             | yes                   | MIDI            | 1.10.1                        | 2012     |

\</sortable\>

### Community Supported Mappings

All of these devices have mappings included in Mixxx. There may be other
mappings more suited to your workflow on [the
forum](http://www.mixxx.org/forums/viewforum.php?f=7).

Do not add mappings to this list until they have been included in Mixxx.
If you make a mapping for a controller, please add it to the [\#Mappings
In Development](#Mappings%20In%20Development) table and refer to the
[Contributing Mappings](Contributing%20Mappings) page for instructions
on how to get it included in Mixxx. When the pull request is merged,
move your controller to this table.

\<sortable 2=numeric\>

| Device                                                                                             | Price (USD) \[7\] | Description                             | Integrated sound card | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------- | --------------------- | --------------- | ----------------------------- | -------- |
| [Numark DJ2GO](Numark%20DJ2GO)                                                                     | $60               | basic 2 deck                            | no                    | MIDI            | 1.10                          | 2011     |
| [Korg nanoKONTROL 2](Korg%20nanoKONTROL%202)                                                       | $60               | miscellaneous                           | no                    | MIDI            | 1.11                          | 2011     |
| [Akai LPD8](Akai%20LPD8)                                                                           | $70               | miscellaneous                           | no                    | MIDI            | 1.10.1                        | 2010     |
| [Novation Dicer](Novation%20Dicer)                                                                 | $70 \[8\]         | pads for use with turntables            | no                    | MIDI            | 1.10                          | 2010     |
| [Novation Launchpad Mini](Novation%20Launchpad%20Mini)                                             | $75               | pad grid                                | no                    | MIDI            | 2.0                           | 2013     |
| [Hercules DJ Control Instinct S](Hercules%20DJ%20Control%20Instinct)                               | $100              | basic 2 deck                            | yes                   | MIDI            | 1.10.1                        | 2015     |
| [Numark Mixtrack 3](Numark%20Mixtrack%20Pro%203)                                                   | $150              | 2 deck all-in-one                       | no                    | MIDI            | 2.1\[9\]                      | 2015     |
| [Numark Mixtrack Pro 3](Numark%20Mixtrack%20Pro%203)                                               | $250              | 2 deck all-in-one                       | yes                   | MIDI            | 2.1\[10\]                     | 2015     |
| [Pioneer DDJ-SB2](Pioneer%20DDJ-SB2)                                                               | $250              | 4 deck\[11\] all-in-one                 | yes                   | MIDI            | 2.0                           | 2015     |
| [American Audio VMS2](American%20Audio%20VMS2)                                                     | $250              | 2 deck all-in-one                       | yes                   | MIDI            | 1.11                          | 2011     |
| [Hercules DJ Console 4-Mx](Hercules%20DJ%20Console%204-Mx)                                         | $300              | 4 deck\[12\] all-in-one                 | yes                   | MIDI            | 1.11                          | 2010     |
| [Reloop Terminal Mix 4](Reloop%20Terminal%20Mix)                                                   | $400              | 4 deck all-in-one                       | yes                   | MIDI            | 1.11                          | 2012     |
| [Numark N4](Numark%20N4)                                                                           | $500              | 4 deck all-in-one                       | yes                   | MIDI            | 1.10                          | 2012     |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                                               | $700              | 4 deck all-in-one                       | yes                   | MIDI            | 2.0                           | 2015     |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | $900              | CD player                               | yes                   | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       | 2010     |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | $2000             | CD player                               | yes                   | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       | 2009     |
| [Akai MPD24](Akai%20MPD24)                                                                         | discontinued      | miscellaneous                           | no                    | MIDI            | 1.8                           | 2007     |
| [Behringer BCD2000](Behringer%20BCD2000)                                                           | discontinued      | basic 2 deck                            | yes                   | MIDI            | 1.11                          | 2006     |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | discontinued      | CD player                               | no                    | MIDI            | 1.10                          | 2010     |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | discontinued      | basic 2 deck                            | yes                   | MIDI            | 1.6                           | 2007     |
| [Denon SC2000](Denon%20SC2000)                                                                     | discontinued      | 1 deck                                  | no                    | MIDI            | 1.8                           | 2010     |
| [DJ Tech CDJ-101](DJ%20Tech%20CDJ-101)                                                             | discontinued      | 2 deck jog wheel                        | no                    | MIDI            | 1.11                          | 2011     |
| [DJ Tech DJM-101](DJ%20Tech%20DJM-101)                                                             | discontinued      | 2 deck mixer                            | no                    | MIDI            | 1.11                          | 2011     |
| [DJ Tech iMix Reload](DJ%20Tech%20iMix%20Reload)                                                   | discontinued      | 2 deck all-in-one                       | no                    | MIDI            | 1.10                          | 2009     |
| [DJ Tech Kontrol One](DJ%20Tech%20Kontrol%20One)                                                   | discontinued      | 4 decks                                 | no                    | MIDI            | 1.11                          | 2009     |
| [DJ Tech Mixer One](DJ%20Tech%20Mixer%20One)                                                       | discontinued      | 2 deck mixer                            | no                    | MIDI            | 1.10.1                        | 2009     |
| [eks Otus](eks%20Otus)                                                                             | discontinued      | 1 turntable + 2 deck mixer              | yes                   | HID             | 1.11                          | 2008     |
| [Electrix Tweaker](Electrix%20Tweaker)                                                             | discontinued      | 4 deck\[13\] without jog wheels         | no                    | MIDI            | 2.0                           | 2012     |
| [Evolution X-Session](Evolution%20X-Session)                                                       | discontinued      | knobs + crossfader                      | no                    | MIDI            | 1.6                           | 2006     |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | discontinued      | 2 deck mixer                            | no                    | MIDI            | 1.6                           | 2006     |
| [Gemini FirstMix](Gemini%20FirstMix)                                                               | discontinued      | basic 2 deck                            | no                    | MIDI            | 1.11                          | 2011     |
| [Kontrol DJ KDJ500](Kontrol%20DJ%20KDJ500)                                                         | discontinued      | basic 2 deck                            | no                    | MIDI            | 1.10                          | 2003     |
| [Korg nanoKONTROL](Korg%20nanoKONTROL)                                                             | discontinued      | 2 deck mixer                            | no                    | MIDI            | 1.8.2                         | 2009     |
| [Hercules DJ Control Air](hercules_dj_control_air)                                                 | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.11                          | 2012     |
| [Hercules DJ Control Instinct](Hercules%20DJ%20Control%20Instinct)                                 | discontinued      | basic 2 deck                            | yes                   | MIDI            | 1.10.1                        | 2012     |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | discontinued      | 2 deck all-in-one                       | yes                   | MIDI \[14\]     | 1.7                           | 2004     |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | discontinued      | 2 deck all-in-one                       | yes                   | HID             | 1.11                          | 2003     |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | discontinued      | 2 deck all-in-one                       | yes                   | HID \[15\]      | 1.8                           | 2010     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | discontinued      | 2 deck all-in-one                       | no                    | HID             | 1.11                          | 2006     |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | discontinued      | 2 deck all-in-one                       | no                    | HID             | 1.11                          | 2009     |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | discontinued      | basic 2 deck                            | no                    | MIDI            | 1.8                           | 2009     |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.6                           | 2007     |
| [Mixman DM2](Mixman%20DM2)                                                                         | discontinued      | 2 decks                                 | yes                   | MIDI \[16\]     | 1.7                           | 2001     |
| [Mixvibes U-Mix Control 2](Mixvibes%20U-Mix%20Control%202%20Pro)                                   | discontinued      | 2 deck all-in-one                       | no                    | MIDI            | 1.10.1                        | 2011     |
| [Mixvibes U-Mix Control 2 Pro](Mixvibes%20U-Mix%20Control%202%20Pro)                               | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.11                          | 2011     |
| [Novation Launchpad Mk1](Novation%20Launchpad%20Mk1)                                               | discontinued      | pad grid                                | no                    | MIDI \[17\]     | 1.11                          | 2009     |
| [Novation Twitch](Novation%20Twitch)                                                               | discontinued      | 2 deck all-in-one                       | no                    | MIDI            | 2.1\[18\]                     | 2011     |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.11                          | 2013     |
| [Numark Omni Control](Numark%20Omni%20Control)                                                     | discontinued      | 2 deck all-in-one                       | yes                   | MIDI \[19\]     | 1.10                          | 2008     |
| [Numark Total Control](Numark%20Total%20Control)                                                   | discontinued      | 2 deck all-in-one                       | no                    | MIDI            | 1.6                           | 2007     |
| [Numark Mixtrack](Numark%20Mixtrack)                                                               | discontinued      | 2 deck all-in-one                       | no                    | MIDI            | 1.8.2                         | 2010     |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.10                          | 2010     |
| [Numark NS7](Numark%20NS7)                                                                         | discontinued      | 2 deck all-in-one with motorized wheels | yes                   | MIDI            | 1.9                           | 2009     |
| [Numark V7](Numark%20V7)                                                                           | discontinued      | 2 deck motorized wheel                  | yes                   | MIDI            | 1.10                          | 2010     |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | discontinued      | CD player                               | no                    | MIDI or HID     | 1.8.2 (MIDI)                  | 2010     |
| [Pioneer DDJ-SB](Pioneer%20DDJ-SB)                                                                 | discontinued      | 4 deck\[20\] all-in-one                 | yes                   | MIDI            | 2.0                           | 2014     |
| [Reloop Beatmix 2](Reloop%20Beatmix%202)                                                           | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 2.1\[21\]                     | 2014     |
| [Reloop Beatmix 4](Reloop%20Beatmix%204)                                                           | discontinued      | 4 deck all-in-one                       | yes                   | MIDI            | 2.1\[22\]                     | 2014     |
| [Reloop Beatpad](Reloop%20Beatpad)                                                                 | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 2.0                           | 2014     |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.8                           | 2009     |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | discontinued      | 2 deck all-in-one                       | yes                   | MIDI \[23\]     | 1.8                           | 2009     |
| [Reloop Terminal Mix 2](Reloop%20Terminal%20Mix)                                                   | discontinued      | 4 deck\[24\] all-in-one                 | yes                   | MIDI            | 1.11                          | 2012     |
| [Tascam US-428](Tascam%20US-428)                                                                   | discontinued      | mixing console                          | yes                   | MIDI            | 1.6.2                         | 2001     |
| [Vestax VCI-100MKI](Vestax%20VCI-100)                                                              | discontinued      | 2 deck all-in-one                       | no                    | MIDI            | 1.6                           | 2007     |
| [Vestax VCI-100MKII](Vestax%20VCI-100MKII)                                                         | discontinued      | 4 deck all-in-one                       | yes                   | MIDI            | 2.0                           | 2011     |
| [Vestax VCI-300](Vestax%20VCI-300)                                                                 | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.11                          | 2008     |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.9                           | 2010     |
| [Vestax Spin](Vestax%20Spin)                                                                       | discontinued      | 2 deck all-in-one                       | yes                   | MIDI            | 1.9                           | 2009     |

\</sortable\>

#### Esoteric controllers

These are devices that were not designed for controlling music software
but have been mapped to Mixxx anyway.

\<sortable 2=numeric\>

| Device                                 | Price (USD) | Description             | Integrated sound card | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------- | ----------- | ----------------------- | --------------------- | --------------- | ----------------------------- | -------- |
| [Nintendo Wiimote](Nintendo%20Wiimote) | $25         | game console controller | no                    | HID             | 1.11                          | 2006     |
| [Sony SixxAxis](Sony%20SixxAxis)       | $25         | game console controller | no                    | HID             | 1.11                          | 2006     |

\</sortable\>

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

\<sortable 2=numeric\>

| Device                                                       | Price (USD) \[25\] | Description                     | Integrated Sound Card | Signal protocol | Released |
| ------------------------------------------------------------ | ------------------ | ------------------------------- | --------------------- | --------------- | -------- |
| [Akai AMX](Akai%20AMX)                                       | $250               | 2 deck mixer                    | yes                   | MIDI            | 2014     |
| [Behringer CMD Studio 4a](Behringer%20CMD%20Studio%204a)     | $200               | 4 deck \[26\] all-in-one        | yes                   | MIDI            | 2013     |
| [Hercules DJControl Compact](Hercules%20DJControl%20Compact) | $80                | basic 2 deck                    | no                    | MIDI            | 2015     |
| [Reloop Jockey 3 ME](Reloop%20Jockey%203%20ME)               | discontinued       | 4 deck \[27\] all-in-one        | yes                   | MIDI            | 2011     |
| [Hercules P32 DJ](Hercules%20P32%20DJ)                       | $300               | 4 deck \[28\] mixer + pad grids | yes                   | MIDI            | 2016     |
| [Denon MC4000](Denon%20MC4000)                               | $399               | 2 deck controller and mixer     | yes                   | MIDI            | 2015     |
| [Gemini G4V](Gemini%20G4V)                                   | $\~282             | 4 deck \[29\] all-in-one        | yes                   | MIDI            | 2013     |
| [Pioneer DDJ-WeGO3](Pioneer%20DDJ-WeGO3)                     | $300               | 2 deck controller and mixer     | yes                   | MIDI            | 2014     |

\</sortable\>

### Not mapped controllers

There are too many DJ controllers out there to list. Some of these
controllers may have mappings (of unverified quality and may be
incomplete) posted on [the
forums](http://www.mixxx.org/forums/viewforum.php?f=7) that have not
(yet) been included with Mixxx. If a controller you own or are
interested in getting is not listed here, [search the
forum](http://mixxx.org/forums/search.php?fid[]=7) to see if anyone has
posted a mapping. If you are willing to put in the effort to map one of
these controllers, please get the controller, map it, and [contribute
the mapping to Mixxx](contributing%20mappings).

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

## Splitter cables

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

Available DJ splitter cables:

  - [Native Instruments Traktor DJ
    Cable](http://www.native-instruments.com/en/products/traktor/traktor-for-ios/traktor-dj-cable/):
    $10
  - [Griffin DJ
    Cable](https://griffintechnology.com/us/products/audio/dj-accessories/dj-cable):
    $20

## Sound cards

To be able to hear the next track you want to mix in before your
audience hears it, you need two separate sound outputs. Most computers
come with a sound card built into the motherboard with only 1 stereo
1/8“ headphone output (2 mono channels). Onboard sound cards built
into computers generally have bad sound quality and may pick up
interference from other devices in the computer, especially the charger
or power supply. **It is recommended to use one sound card with at least
4 mono output channels (2 stereo channels).** For vinyl control, it is
recommended to use a sound card with phono preamplifiers.

### Compatibility

As stated above, Mixxx can use any sound card that your OS has a driver
to use. All sound cards listed in the table below work with Mac OS X.
All except the Griffin DJ Connect and Apogee Duet have drivers for the
recommended [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api)
on Windows. Most work with Linux, but not all; check the table for
details.

If you have a Firewire/IEEE 1394 interface, the only way to use it with
Linux is with JACK (not ALSA). The FFADO project has [a list of Firewire
interfaces compatible with
Linux](http://ffado.org/?q=devicesupport/list).

Thunderbolt sound cards can operate at lower latencies than USB or
Firewire sound cards, but are generally only compatible with Mac OS X.

### Sound card considerations

#### Stand-alone sound cards versus sound cards integrated with controllers or mixers

Most DJ
[\#controllers](#controllers)-that-cost-more-than-$200-have-a-4-output-sound-card-built-into-them.-This-is-more-convenient-to-transport-and-set-up-than-a-stand-alone-[sound
card](#USB-sound-cards) plus a controller because it only requires one
device with one USB cable. Most of these produce better quality sound
than a sound card built into a computer. However, the highest quality
sound cards like the Apogee Duet and RME Babyface Pro are stand alone
devices not integrated into controllers.

If a controller with a built in sound card is only powered by a USB
cable, the sound card may not be able to reach very high output levels
because the electricity available from a USB port has to power the sound
card as well as the lights and other components of the controller.
Controllers for which this is a known issue have that information on
their wiki page. Insufficient power for a high output level is rarely an
issue for standalone USB sound cards that are not built into
controllers. Some controllers with built in sound cards have an
additional power adapter to ensure the sound card output has enough
power. A low sound card output can be worked around by running it
through a mixer and applying gain or a stand-alone headphone amplifier
if the headphone output is too quiet.

[Some DJ mixers](#Mixers-with-sound-cards) also include built-in USB
sound cards. These can be used to send Mixxx's unmixed Deck 1-4 outputs
to the external mixer. This is more convenient than having a separate
device plugged into a mixer. Most DJ mixers have phono preamplifiers,
allowing turntables to be plugged into them for timecode vinyl control
(DVS). If the mixer is a digital mixer, the sound quality would be
better using a sound card built into the mixer than plugging in a
separate sound card because it would skip converting the signal from
digital to analog and back again.

#### Vinyl control, microphones, and preamplifiers

If you want to use [vinyl
control](http://mixxx.org/manual/latest/chapters/vinyl_control.html),
sometimes referred to as a Digital Vinyl System (DVS), it is best to
have phono preamplifiers (one for each deck) somewhere between your
turntable and sound card to boost the turntable's phono level signal to
line level. Mixxx can amplify phono level signals in software, but it is
better to do it in hardware. The phono preamp can be in the turntable,
in the sound card, or a stand alone device. Most sound cards do not have
phono preamps; these are generally found on sound cards specifically
made for controlling DJ software with timecode vinyl. [\#Mixers with
sound cards](#Mixers%20with%20sound%20cards) have phono preamps on their
deck inputs, but not necessarily on every deck input. Many higher-end
all-in-one controllers also include sound cards with phono preamps.
Refer to the tables below for some devices with phono preamps.

Turntables, microphones, and contact microphones (like those used on
electric guitars) all output very low voltage signals that need to be
amplified to line level by a preamplifier before a sound card (or most
audio equipment) can effectively work with them. Additionally, vinyl
records have the [RIAA equalization
curve](https://en.wikipedia.org/wiki/RIAA_equalization) applied to the
recording, which needs to be undone by a phono preamplifier. If a device
has a switch between phono, mic, or instrument (contact microphone)
level and line level, it has a preamplifier in it. If you want to plug a
microphone into your sound card, it will need a microphone preamplifier.
If you want to plug an electric guitar or bass into your sound card, it
will need an instrument preamplifier.

Note that phono preamplifiers work on a stereo pair (2 input channels)
whereas microphone and instrument preamplifiers work on a single input
channel.

#### Connector and cable types

If you are unfamiliar with professional audio equipment, read Digital DJ
Tips' [Essential Guide to Audio Cables for
DJs](http://www.digitaldjtips.com/2011/07/the-essential-guide-to-audio-cables-for-djs/)
to understand the different kinds of connectors on sound cards. It is
better to use a sound card with balanced outputs, especially if you will
run long cables directly into an amplifier or active speakers without
going through a hardware mixer. Balanced signals reject interference and
are less susceptible to ground loop hum issues (which can be a problem
when plugging unbalanced gear into separate power sources). However,
most venues have DJs plug into hardware DJ mixers, which typically only
have RCA inputs (RCA cables cannot be balanced). Most home/computer
speakers and amplifiers have RCA and/or 1/8" TRS stereo inputs. Most
live sound mixers have balanced 1/4" TRS mono inputs. If you need to
interconnect balanced and unbalanced gear, see [this
guide](http://www.presonus.com/news/articles/balanced-unbalanced) from
Presonus and [this guide](http://www.rane.com/note110.html) from Rane.

#### Number of channels

Sound cards often have multiple connectors for a single channel,
resulting in more connectors than channels. So, not every connector can
send or receive an independent signal. For example, some sound cards
made for DJing have 4 output channels with 4 mono output connectors and
1 stereo headphone connector. This does not mean that the sound card can
send out 6 different signals at the same time; rather, the signal on 2
of the mono outputs and the stereo headphone output would be the same.

#### Bit depth and sample rate

Most music is published with a bit depth of 16 bits at a sample rate of
44.1 kHz because this is all that is needed to store all the detail of
music in digital form.

Bit depth determines the possible dynamic range of the signal. 16 bits
is more than enough for playing back music. While 24 bits is helpful for
recording, [it is useless for
playback](http://www.sonicscoop.com/2013/08/29/why-almost-everything-you-thought-you-knew-about-bit-depth-is-probably-wrong/).

Half the sample rate determines the maximum frequency that can be
represented by the signal. Humans generally can't hear frequencies above
20 kHz, so a sampling rate of 44.1 kHz, representing a maximum frequency
of 22.05 kHz, is fine for playback. Higher sample rates like 88.2 kHz
and 96 kHz can be helpful to reduce aliasing distortion when recording,
but have no benefit for playback and make your computer work harder.

For a more thorough and technical explanation of why 16 bits at 44.1 kHz
is all that is needed for playback, read [24/192 Music Downloads Are
Very Silly Indeed](http://xiph.org/~xiphmont/demo/neil-young.html).

#### Specifications

When considering specifications, higher dynamic range, higher
signal-to-noise ratio (SNR), higher maximum output level, lower THD+N
(Total Harmonic Distortion + Noise; look for a more negative dB value or
smaller percentage), and lower crosstalk (more negative dB value) are
better. Cheap sound cards tend to not have these specifications
published.

### USB sound cards

These devices allow a computer to output and input sound. It is possible
to use just a sound card plus a keyboard & mouse to use Mixxx, but a
separate [controller](#controllers) makes using Mixxx easier and more
intuitive.

Many extremely cheap ($1-$10) 2 channel output USB sound cards that look
like USB flash drives are available, but these tend to be very poor
quality, sometimes even worse than onboard sound cards. [\#Splitter
cables](#Splitter%20cables) are a good option in that price range. Mixxx
2.0 can use multiple sound cards at the same time, so it is possible to
use a 2 output sound card for the main stereo output and the onboard
sound card on a computer for headphones. However, a higher quality, 4
output sound card is recommended. You generally get the sound quality
you pay for with sound cards.

\<sortable 2=numeric\>

| Device                                                                                                                                                                                                                                         | Price (USD) \[30\] | Channels out         | Output connectors                                                       | Channels in          | Input connectors                                                                        | Preamps             | Linux         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | -------------------- | ----------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------- | ------------------- | ------------- |
| [Behringer U-Control UCA202](http://www.music-group.com/Categories/Behringer/Computer-Audio/Audio-Interfaces/UCA202/p/P0484) & [UCA222](http://www.music-group.com/Categories/Behringer/Computer-Audio/Audio-Interfaces/UCA222/p/P0A31) \[31\] | $30                | 2                    | 2 RCA, 1 1/8" headphone, 1 SPDIF Toslink                                | 2                    | 2 RCA                                                                                   | none                | yes           |
| [Behringer U-Phono UFO202](http://www.music-group.com/Categories/Behringer/Computer-Audio/Audio-Interfaces/UFO202/p/P0A12)\[32\]                                                                                                               | $30                | 2                    | 2 RCA, 1 1/8" headphone                                                 | 2                    | 2 RCA                                                                                   | 1 phono             | yes           |
| [Native Instruments Traktor Audio 2 DJ (Mk2)](http://www.native-instruments.com/en/products/traktor/dj-audio-interfaces/traktor-audio-2/)                                                                                                      | $100               | 4                    | 2 1/8" stereo                                                           | 0                    | none                                                                                    | none                | yes           |
| [Numark DJ iO 2](http://www.numark.com/product/djio-2)                                                                                                                                                                                         | $100               | 4                    | 2 RCA, 1 1/4" headphone                                                 | 0                    | 1 1/4" mic \[33\]                                                                       | 1 mic               | yes           |
| [ESI UDJ6](http://www.esi-audio.com/products/udj6/)                                                                                                                                                                                            | $140               | 6                    | 4 RCA, 1 1/4" headphone                                                 | 0                    | none                                                                                    | none                | likely \[34\] |
| [ESI Maya 44 USB+](http://www.esi-audio.com/products/maya44usb+/)                                                                                                                                                                              | $140               | 4                    | 4 RCA, 1 1/4" headphone/SPDIF optical combo                             | 4                    | 4 RCA                                                                                   | none                | yes           |
| [Novation Audiohub 2x4](https://us.novationmusic.com/accessories/audiohub-2x4)                                                                                                                                                                 | $170               | 4                    | 4 RCA, 2 1/4" balanced, 1 1/4" headphone                                | 2                    | 2 RCA (+3 USB ports for connecting other devices)                                       | none                | likely \[35\] |
| [Focusrite Scarlett 2i4](http://us.focusrite.com/usb-audio-interfaces/scarlett-2i4)                                                                                                                                                            | $200               | 4                    | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 5-pin MIDI                  | 2                    | 2 XLR+1/4" balanced combo, 1 5-pin MIDI                                                 | 2 mic, 2 instrument | yes           |
| [Native Instruments Komplete Audio 6](http://www.native-instruments.com/en/products/komplete/audio-interfaces/komplete-audio-6-migrated/included-software/)                                                                                    | $230               | 4 analog, 2 digital  | 4 1/4" balanced, 1 1/4" headphone, 1 5-pin MIDI, 1 optical SPDIF        | 4 analog, 2 digital  | 2 XLR+1/4" balanced, 2 1/4" balanced, 1 5-pin MIDI, 1 optical SPDIF                     | 2 mic, 2 instrument | yes           |
| [Native Instruments Traktor Scratch A6](http://www.native-instruments.com/en/products/traktor/digital-vinyl/traktor-scratch-a6/)                                                                                                               | $300               | 6                    | 6 RCA, 1 1/4" headphone                                                 | 6                    | 6 RCA                                                                                   | 2 phono             | yes           |
| [Denon DS1](http://denondj.com/products/view/ds1)                                                                                                                                                                                              | $300               | 4                    | 4 RCA                                                                   | 4                    | 4 RCA                                                                                   | 2 phono             | yes           |
| [Audient iD14](http://audient.com/products/id14)                                                                                                                                                                                               | $300               | 4                    | 2 1/4" balanced, 1 1/4" headphone                                       | 2                    | 2 1/4" balanced/XLR combo, 1 1/4" TS instrument                                         | 2 mic, 1 instrument | yes           |
| [Native Instruments Traktor Scratch A10](http://www.native-instruments.com/en/products/traktor/digital-vinyl/traktor-scratch-a10/)                                                                                                             | $500               | 10                   | 10 RCA, 1 1/4" headphone                                                | 10                   | 10 RCA, 1 1/4" mic                                                                      | 4 phono, 1 mic      | yes           |
| [Rane SL2](http://dj.rane.com/products/sl2-for-serato-scratch-live)                                                                                                                                                                            | $500               | 4                    | 4 RCA                                                                   | 4                    | 4 RCA                                                                                   | 2 phono             | no            |
| [Apogee Duet 2](http://www.apogeedigital.com/products/duet) \[36\]                                                                                                                                                                             | $600               | 4                    | 2 1/4" balanced (on breakout cable), 1 1/4" headphone                   | 2                    | 2 1/4" balanced/XLR combo (on breakout cable)                                           | 2 mic, 2 instrument | likely \[37\] |
| [MOTU Ultralite AVB](http://motu.com/products/avb/ultralite-avb/)                                                                                                                                                                              | $650               | 10 analog, 8 digital | 8 1/4" balanced, 1 1/4" headphone, 1 Toslink SPDIF/ADAT, 1 AVB Ethernet | 10 analog, 8 digital | 2 XLR, 2 1/4" Hi-Z, 6 1/4" balanced or unbalanced, 1 Toslink SPDIF/ADAT, 1 AVB Ethernet | 2 mic, 2 instrument | yes           |
| [Rane SL3](http://dj.rane.com/products/sl3-for-serato-scratch-live)                                                                                                                                                                            | $700               | 6                    | 6 RCA                                                                   | 6                    | 6 RCA                                                                                   | 3 phono             | no            |
| [RME Babyface Pro](http://babyface.rme-audio.de/)                                                                                                                                                                                              | $750               | 4 analog, 8 digital  | 2 XLR, 1 1/8" headphone, 1 1/4" headphone, 1 Toslink SPDIF/ADAT         | 4 analog, 8 digital  | 2 XLR, 2 1/4" balanced or unbalanced, 1 Toslink SPDIF/ADAT SPDIF/ADAT                   | 2 mic, 2 instrument | yes \[38\]    |
| [Rane SL4](http://dj.rane.com/products/sl4-for-serato-scratch-live)                                                                                                                                                                            | $900               | 8                    | 8 RCA                                                                   | 8                    | 8 RCA                                                                                   | 4 phono             | no            |

\</sortable\>

### Mixers with sound cards

These are devices that can mix audio from different sources without
needing a computer. They also have a built-in USB sound card to connect
directly to a computer without needing a separate sound card. They tend
to be much more expensive than comparable [\#controllers](#controllers)
and [\#USB sound cards](#USB%20sound%20cards). They are often found
installed in venues for multiple DJs to use.

Each conversion of a signal between digital and analog forms adds noise
and distortion. So, if the mixer's processing is done digitally, it is
best to use the sound card built into a mixer (or a digital input if the
mixer has one). When analog outputs of a separate sound card are plugged
into a digital mixer, the sound card converts the digital signals to
analog, then the mixer converts the analog signals back to digital for
its processing. If the input to the mixer is digital, those two
conversions do not occur.

However, some of these mixers are analog mixers and the built in sound
card converts the digital signals from the computer to analog for the
mixer's analog processing. In that case, using the mixer's built in
sound card may or may not sound better than a separate sound card,
depending on the quality of each of the sound cards.

Many of these mixers also send MIDI signals to the computer over USB,
which could be mapped to control Mixxx.

Most of these have a single USB port, but some have two. Two USB ports
allows two different DJs to use the mixer's sound card at the same time
with their own computer for collaborative DJ sets and easy, seamless
transitions between DJs. \<sortable 2=numeric\>

| Device                                                                                                                      | Price (USD) \[39\] | Decks | Phono preamps | USB ports | Analog or digital mixing | Linux         |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----- | ------------- | --------- | ------------------------ | ------------- |
| [Numark M101USB](http://www.numark.com/product/m101usb)                                                                     | $100               | 2     | 2             | 1         | ?                        | likely \[40\] |
| [Allen & Heath Xone 23C](http://www.allen-heath.com/ahproducts/xone-23c/)                                                   | $400               | 2     | 2             | 1         | analog                   | likely \[41\] |
| [Native Instruments Traktor Kontrol Z2](http://www.native-instruments.com/en/products/traktor/dj-mixer/traktor-kontrol-z2/) | $600               | 2     | 2             | 1         | ?                        | likely \[42\] |
| [Allen & Heath Xone 43C](http://www.allen-heath.com/ahproducts/xone43C/)                                                    | $1000              | 4     | 4             | 1         | analog                   | likely \[43\] |
| [Pioneer DJM-750](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-750)                                                 | $1000              | 4     | 2             | 1         | digital                  | ?             |
| [Pioneer DJM-5000](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-5000)                                               | $1000              | 4     | 0             | 1         | digital                  | ?             |
| [Allen & Heath Xone DB2](http://www.allen-heath.com/ahproducts/xonedb2/)                                                    | $1500              | 4     | 4             | 1         | digital                  | no            |
| [Pioneer DJM-850](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-850)                                                 | $1500              | 4     | 2             | 1         | digital                  | ?             |
| [Rane TTM57MkII](http://dj.rane.com/products/ttm57mkii)                                                                     | $1750              | 2     | 2             | 2         | digital                  | likely \[44\] |
| [Rane MP2014](http://dj.rane.com/products/mp2014-mixer)                                                                     | $2000              | 4     | 2             | 2         | digital                  | likely \[45\] |
| [Allen & Heath Xone DB4](http://www.allen-heath.com/ahproducts/xonedb4/)                                                    | $2000              | 4     | 4             | 1         | digital                  | no            |
| [Pioneer DJM-900NXS](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-900NXS)                                           | $2000              | 4     | 2             | 1         | digital                  | ?             |
| [Rane Sixty-Two](http://dj.rane.com/products/sixty-two)                                                                     | $2000              | 2     | 2             | 2         | digital                  | no            |
| [Pioneer DJM-900NXS2](https://www.pioneerdj.com/en-us/product/mixer/djm-900nxs2/black/overview/)                            | $2200              | 4     | 4             | 2         | digital                  | ?             |
| [Rane Sixty-Four](http://dj.rane.com/products/sixty-four)                                                                   | $2200              | 4     | 4             | 2         | digital                  | no            |
| [Pioneer DJM-900SRT](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-900SRT)                                           | $2300              | 4     | 2             | 1         | digital                  | ?             |
| [Pioneer DJM-2000NXS](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-2000NXS)                                         | $2500              | 4     | 2             | 1         | digital                  | likely \[46\] |
| [Rane MP2015](http://dj.rane.com/products/mp2015-mixer)                                                                     | $2900              | 4     | 4             | 2         | digital                  | likely \[47\] |

\</sortable\>

### Controllers with sound cards

These are USB devices that send MIDI or HID signals to [control
Mixxx](#controllers) and also have a built-in sound card. \<sortable
2=numeric\>

| Device                                                               | Price (USD) \[48\] | Channels out | Output connectors                                                 | Channels in | Input connectors                                                         | Preamps        | Linux |
| -------------------------------------------------------------------- | ------------------ | ------------ | ----------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------ | -------------- | ----- |
| [Behringer BCD3000](Behringer%20BCD3000)                             | $100               | 4            | 2 RCA, 1 1/4" headphone                                           | 4           | 4 RCA, 1 XLR mic                                                         | 2 phono, 1 mic | yes   |
| [Hercules DJ Control Instinct](Hercules%20DJ%20Control%20Instinct)   | $125               | 4            | 2 RCA, 2 1/8" stereo                                              | 0           | none                                                                     | none           | yes   |
| [Hercules DJ Console RMX 2](Hercules%20DJ%20Console%20RMX%202)       | $200               | 4            | 2 XLR, 2 RCA, 2 1/4" headphone                                    | 4           | 4 RCA, 1 XLR \[49\]                                                      | 2 phono, 1 mic | yes   |
| [American Audio VMS2](American%20Audio%20VMS2)                       | $250               | 4            | 2 XLR, 4 RCA, 1 1/4" headphone                                    | 4           | 4 RCA, 1 XLR mic, 1 1/4" mic                                             | 2 phono, 1 mic | yes   |
| [Pioneer DDJ-SB](Pioneer%20DDJ-SB)                                   | $250               | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 0           | 1 1/4" mic \[50\]                                                        | 1 mic          | yes   |
| [Pioneer DDJ-SB2](Pioneer%20DDJ-SB2)                                 | $250               | 4            | 2 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 0           | 1 1/4" mic \[51\]                                                        | 1 mic          | yes   |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)               | $300               | 4            | 2 RCA, 1 1/8" headphone                                           | 0           | none                                                                     | none           | yes   |
| [Denon MC4000](Denon%20MC4000)                                       | $399               | 4            | 2 RCA, 2 XLR, 2 1/4" balanced, 1 1/8" headphone, 1 1/4" headphone | 0           | 2 RCA, 1 1/4“ XLR combo mic, 1 1/4“ mic \[52\]                           | 2 mic          | yes   |
| [Reloop Terminal Mix 4](Reloop%20Terminal%20Mix)                     | $400               | 4            | 4 RCA, 2 1/4" balanced, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1/4" mic                                                          | 1 phono, 1 mic | ?     |
| [Numark N4](Numark%20N4)                                             | $500               | 4            | 4 RCA, 2 XLR, 1 1/4" headphone, 1 1/8" headphone                  | 4           | 4 RCA                                                                    | 2 phono        | ?     |
| [Denon MC6000Mk2](Denon%20MC6000Mk2)                                 | $700               | 4            | 2 1/4" balanced, 2 XLR, 2 RCA, 1 1/4" headphone                   | 9           | 8 RCA, 1 1/4" mic, 1 XLR mic                                             | 4 phono, 1 mic | yes   |
| [Behringer BCD2000](Behringer%20BCD2000)                             | discontinued       | 4            | 2 RCA, 1 1/4" headphone                                           | 4           | 4 RCA, 1 XLR                                                             | 2 phono, 1 mic | yes   |
| [Denon HS5500](Denon%20HS5500)                                       | discontinued       | ?            | ?                                                                 | ?           | ?                                                                        | ?              | ?     |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)             | discontinued       | 4            | 4 1/4" balanced, 4 RCA, 2 1/4" headphone                          | 5           | 4 RCA, 1 1/4" mic                                                        | 2 phono, 1 mic | yes   |
| [Mixvibes U-Mix Control 2 Pro](Mixvibes%20U-Mix%20Control%202%20Pro) | discontinued       | 4            | 4 RCA, 1 1/4" headphone, 1 1/8" headphone                         | 5           | 4 RCA, 1 1/4" mic                                                        | 2 phono, 1 mic | ?     |
| [Numark Omni Control](Numark%20Omni%20Control)                       | discontinued       | 4            | 4 RCA, 1 1/4" headphone                                           | 1           | 1/14" mic                                                                | 1 mic          | no    |
| [Reloop Terminal Mix 2](Reloop%20Terminal%20Mix)                     | discontinued       | 4            | 2 1/4" balanced, 4 RCA, 1 1/4" headphone, 1 1/8" headphone        | 3           | 2 RCA, 1 1/4" mic                                                        | 1 phono, 1 mic | ?     |
| [Tascam US-428](Tascam%20US-428)                                     | discontinued       | 2            | 2 RCA, 1 optical SPDIF, 2 5-pin MIDI                              | 4           | 2 1/4" balanced, 2 1/4" unbalanced, 2 XLR, 1 optical SPDIF, 2 5-pin MIDI | ?              | yes   |

\</sortable\>

1.  Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop) in the United States.
    Prices may vary in other parts of the world, but the relative prices
    of different devices in USD should still provide a rough guide. You
    may be able to find hardware available for sale cheaper. Devices are
    marked as discontinued if the manufacturer has declared them as
    discontinued, the manufacturer has gone out of business, or new
    units are not widely available online. They may or may not still be
    available used online. If the price of a device has dropped or it
    has been discontinued, please update this page.

2.  Mapping has buttons to toggle between decks 1/3 and decks 2/4.

3.  The default Mixxx mapping has this mapped to hotcues.

4.  Mapping supports 4-deck switching

5.  Mapping supports 4-deck switching

6.  Mapping supports n-deck switching

7.  Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop) in the United States.
    Prices may vary in other parts of the world, but the relative prices
    of different devices in USD should still provide a rough guide. You
    may be able to find hardware available for sale cheaper. Devices are
    marked as discontinued if the manufacturer has declared them as
    discontinued, the manufacturer has gone out of business, or new
    units are not widely available online. They may or may not still be
    available used online. If the price of a device has dropped or it
    has been discontinued, please update this page.

8.  The Novation Dicer is priced per pair.

9.  This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

10. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

11. switching between decks 1/3 and decks 2/4

12. switching between decks 1/3 and decks 2/4

13. switching between decks 1/3 and decks 2/4

14. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Mac OS X. There is no
    driver available for Linux or Windows.

15. with MIDI driver. For Linux support, see [this forum
    thread](http://mixxx.org/forums/viewtopic.php?f=3&t=5064)

16. [Mac OS X driver](http://www.joemattiello.com/dm2/); [Linux MIDI
    Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz), [Alternate
    Linux MIDI driver
    (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2),
    [dm2linux on
    sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453)

17. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

18. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

19. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

20. switching between decks 1/3 and decks 2/4

21. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

22. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

23. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

24. switching between decks 1/3 and decks 2/4

25. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop) in the United States.
    Prices may vary in other parts of the world, but the relative prices
    of different devices in USD should still provide a rough guide. You
    may be able to find hardware available for sale cheaper. Devices are
    marked as discontinued if the manufacturer has declared them as
    discontinued, the manufacturer has gone out of business, or new
    units are not widely available online. They may or may not still be
    available used online. If the price of a device has dropped or it
    has been discontinued, please update this page.

26. switching between decks 1/3 and decks 2/4

27. switching between decks 1/3 and decks 2/4

28. switching between decks 1/3 and decks 2/4

29. switching between decks 1/3 and decks 2/4

30. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop) in the United States.
    Prices may vary in other parts of the world, but the relative prices
    of different devices in USD should still provide a rough guide. You
    may be able to find hardware available for sale cheaper. Devices are
    marked as discontinued if the manufacturer has declared them as
    discontinued, the manufacturer has gone out of business, or new
    units are not widely available online. They may or may not still be
    available used online. If the price of a device has dropped or it
    has been discontinued, please update this page.

31. The only difference between the Behringer U-Control UCA202 & UCA222
    are the color and the software they are bundled with.

32. See [this forum
    thread](http://mixxx.org/forums/viewtopic.php?f=6&t=2438) for how to
    modify the hardware to work with Mixxx.

33. Microphone input is mixed with the master output in hardware. It is
    not available to the computer.

34. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

35. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

36. No ASIO driver for Windows.

37. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

38. In class compliant mode. Hold Select and Dim buttons when plugging
    in USB cable to enable class compliant mode.

39. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop) in the United States.
    Prices may vary in other parts of the world, but the relative prices
    of different devices in USD should still provide a rough guide. You
    may be able to find hardware available for sale cheaper. Devices are
    marked as discontinued if the manufacturer has declared them as
    discontinued, the manufacturer has gone out of business, or new
    units are not widely available online. They may or may not still be
    available used online. If the price of a device has dropped or it
    has been discontinued, please update this page.

40. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

41. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

42. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

43. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

44. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

45. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

46. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

47. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

48. Prices listed on this page are the prevailing prices for unused
    devices found from [searching Google
    Shopping](https://www.google.com/?tbm=shop) in the United States.
    Prices may vary in other parts of the world, but the relative prices
    of different devices in USD should still provide a rough guide. You
    may be able to find hardware available for sale cheaper. Devices are
    marked as discontinued if the manufacturer has declared them as
    discontinued, the manufacturer has gone out of business, or new
    units are not widely available online. They may or may not still be
    available used online. If the price of a device has dropped or it
    has been discontinued, please update this page.

49. Microphone input is mixed with the master output in hardware. It is
    not available to the computer.

50. Microphone input is mixed with the master output in hardware. It is
    not available to the computer.

51. Microphone input is mixed with the master output in hardware. It is
    not available to the computer.

52. Microphone and auxiliary inputs are mixed with the master output in
    hardware. They are not available to the computer.
