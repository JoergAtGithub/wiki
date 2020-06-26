# Mixxx DJ Hardware Guide

## What kind of hardware should I get to DJ with Mixxx?

Bare minimum equipment for DJing:

  - computer (preferably a laptop)
  - [splitter cable](#splitter-cables) or [audio
    interface](#audio-interfaces)
  - [headphones](DJ%20headphones)
  - speakers
  - audio cables and adapters

Helpful but not strictly necessary:

  - [audio interface](#audio-interfaces) with 4 mono output channels (2
    stereo pairs)
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

#### Controllers

Mixxx can work with any controller that sends MIDI or HID signals to
your computer; it just needs a controller mapping to tell Mixxx what to
do with the signals. Standards compliant MIDI controllers do not need
any special drivers on Linux, macOS, or Windows. Standards compliant HID
controllers do not need any special drivers. Most DJ controllers are
standards compliant MIDI controllers and so are these in the tables
below. Exceptions from the standard are noted in the tables below.

#### Audio interfaces

Controllers that have integrated audio interfaces often have a USB Audio
Class compliant audio interface. Sound cards that aren't USB Audio Class
compliant need a driver for each OS. USB Audio Class compliant audio
interfaces, both stand-alone and integrated into controllers, do not
need any special drivers for Linux or macOS. On Windows, they can be
used without any special drivers, but a driver is needed from the
manufacturer to use the recommended [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api).
Sound cards that are advertised for use with iOS devices are class
compliant.

Unlike some proprietary DJ programs, Mixxx works with any audio
interface that your operating system has a driver to use—including for
timecode vinyl (DVS) use.

#### Determining USB class compliance

If you are considering buying a controller or audio interface, the
easiest way to tell if it is USB class compliant before you buy it is to
search for macOS drivers for the device on the manufacturer's website,
even if you do not use macOS. If it is advertised as compatible with
macOS but there are no drivers to download for macOS, it does not
require drivers from the manufacturer on macOS because it is class
compliant. If it is advertised as compatible with iOS, it is class
compliant because Apple does not let manufacturers provide proprietary
drivers on iOS. USB class compliant audio, MIDI, and HID devices can be
used with Mixxx on Linux, macOS, and Windows.

### Mixxx Certified Mappings

Click the name of the controller for more information.

\<sortable 2=numeric\>

| Device                                                                           | Price (USD) \[1\] | Description                                             | Integrated Sound Card | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------- | --------------------- | ---------------- | --------------- | ----------------------------- | -------- |
| [Hercules DJControl Compact](Hercules%20DJControl%20Compact)                     | $80               | basic 2 deck                                            | no                    | \-               | MIDI            | 2.1                           | 2015     |
| [Hercules DJ Control MP3 e2 / MP3 LE / Glow](Hercules%20DJ%20Control%20MP3%20e2) | $90               | basic 2 deck\[2\]                                       | no                    | \-               | USB Bulk        | 1.11                          | 2009     |
| [Hercules P32 DJ](Hercules%20P32%20DJ)                                           | $250              | 2 deck\[3\] without jog wheels                          | yes                   | no               | MIDI            | 2.1                           | 2016     |
| [Allen & Heath Xone K1](Allen%20Heath%20Xone%20K2)                           | $250              | 2 decks + 2 effect units, or 4 decks, or 4 effect units | no                    | \-               | MIDI            | 2.1                           | 2014     |
| [Allen & Heath Xone K2](Allen%20Heath%20Xone%20K2)                           | $270              | 2 decks + 2 effect units, or 4 decks, or 4 effect units | yes                   | no               | MIDI            | 1.11                          | 2012     |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                             | $700              | 4 deck all-in-one                                       | yes                   | yes              | MIDI            | 2.0                           | 2015     |
| [American Audio VMS4/4.1](American%20Audio%20VMS4)                               | discontinued      | 4 deck all-in-one                                       | yes                   | yes              | MIDI            | 1.9                           | 2012     |
| [DJ TechTools MIDIFighter Classic](DJ%20TechTools%20MIDIFighter%20Classic)       | discontinued      | 4x4 spring-loaded arcade button grid \[4\]              | no                    | \-               | MIDI            | 1.8                           | 2011     |
| [Denon HS5500](Denon%20HS5500)                                                   | discontinued      | 2-decks-in-1 CD player with motorized platter           | yes                   | no               | MIDI            | 2.0                           | 2008     |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)                          | discontinued      | 2 deck all-in-one                                       | yes                   | no               | USB Bulk        | 1.11                          | 2008     |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)                         | discontinued      | basic 2 deck all-in-one                                 | yes                   | yes              | HID             | 1.11                          | 2008     |
| [Hercules DJ Console RMX 2](Hercules%20DJ%20Console%20RMX%202)                   | discontinued      | 2 deck all-in-one                                       | yes                   | yes              | MIDI            | 1.11                          | 2012     |
| [Korg Kaoss DJ](Korg%20Kaoss%20DJ)                                               | discontinued      | 2 deck controller and standalone mixer (switchable)     | yes                   | no               | MIDI            | 2.1                           | 2015     |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)                               | discontinued      | 2 deck mixer                                            | no                    | \-               | MIDI            | 1.6                           | 2007     |
| [Stanton SCS.3d](Stanton%20SCS.3d)                                               | discontinued      | 1 deck control \[5\]                                    | no                    | \-               | MIDI            | 1.7                           | 2009     |
| [Stanton SCS.3m](Stanton%20SCS.3m)                                               | discontinued      | 2 deck mixer \[6\]                                      | no                    | \-               | MIDI            | 1.7                           | 2009     |
| [Stanton SCS.1m](Stanton%20SCS.1m)                                               | discontinued      | 4 deck mixer                                            | yes                   | yes              | HSS1394 (MIDI)  | 1.7                           | 2009     |
| [Stanton SCS.1d](Stanton%20SCS.1d)                                               | discontinued      | 1 turntable \[7\]                                       | no                    | \-               | HSS1394 (MIDI)  | 1.9.1                         | 2009     |
| [Vestax VCI-400](Vestax%20VCI-400)                                               | discontinued      | 4 deck all-in-one                                       | yes                   | yes              | MIDI            | 1.10.1                        | 2012     |

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

| Device                                                                                             | Price (USD) \[8\] | Description                                                  | Integrated audio interface | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------ | -------------------------- | ---------------- | --------------- | ----------------------------- | -------- |
| [Korg nanoKONTROL 2](Korg%20nanoKONTROL%202)                                                       | $60               | miscellaneous                                                | no                         | \-               | MIDI            | 1.11                          | 2011     |
| [Akai LPD8](Akai%20LPD8)                                                                           | $70               | miscellaneous                                                | no                         | \-               | MIDI            | 1.10.1                        | 2010     |
| [Novation Launchpad Mini](Novation%20Launchpad%20Mini)                                             | $75               | pad grid                                                     | no                         | \-               | MIDI            | 2.0                           | 2013     |
| [Novation Dicer](Novation%20Dicer)                                                                 | $100 \[9\]        | pads for use with turntables                                 | no                         | \-               | MIDI            | 1.10                          | 2010     |
| [Hercules DJ Control Instinct S](Hercules%20DJ%20Control%20Instinct)                               | $100              | basic 2 deck                                                 | yes                        | no               | MIDI            | 1.10.1                        | 2015     |
| [Novation Launchpad Mk2](Novation%20Launchpad%20Mk2)                                               | $150              | pad grid                                                     | no                         | \-               | MIDI            | 2.1                           | 2015     |
| [Numark Mixtrack 3](Numark%20Mixtrack%20Pro%203)                                                   | $150              | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 2.1                           | 2015     |
| [Behringer CMD Studio 4a](Behringer%20CMD%20Studio%204a)                                           | $200              | 2 deck \[10\] all-in-one                                     | yes                        | no               | MIDI            | 2.1                           | 2013     |
| [Native Instruments Traktor Kontrol F1](Native%20Instruments%20Traktor%20Kontrol%20F1)             | $200              | originally branded as "Remix controller", but very versatile | no                         | \-               | HID             | 1.11                          | 2012     |
| [Numark Mixtrack Pro 3](Numark%20Mixtrack%20Pro%203)                                               | $200              | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 2.1                           | 2015     |
| [DJ Tech Tools MIDI Fighter Twister](DJ%20Tech%20Tools%20MIDI%20Fighter%20Twister)                 | $220              | 2 deck controller \[11\]                                     | no                         | \-               | MIDI            | 2.1.5                         | 2015     |
| [Keith McMillen QuNeo](Keith%20McMillen%20QuNeo)                                                   | $250              | miscellaneous                                                | no                         | \-               | MIDI            | 1.11                          | 2012     |
| [Numark Mixtrack Platinum](Numark%20Mixtrack%20Platinum)                                           | $250              | 2 deck\[12\] all-in-one                                      | yes                        | no               | MIDI            | 2.2.0                         | 2016     |
| [American Audio VMS2](American%20Audio%20VMS2)                                                     | $250              | 2 deck all-in-one                                            | yes                        | yes              | MIDI            | 1.11                          | 2011     |
| [Native Instruments Traktor Kontrol S2 MK3](Native%20Instruments%20Traktor%20Kontrol%20S2%20MK3)   | $300              | 2 deck controller all-in-one                                 | yes                        | no               | HID             | 2.2.4                         | 2018     |
| [Denon MC4000](Denon%20MC4000)                                                                     | $400              | 2 deck controller and mixer                                  | yes                        | yes              | MIDI            | 2.1                           | 2015     |
| [Roland DJ-505](Roland%20DJ-505)                                                                   | $550              | 2 deck\[13\] all-in-one with integrated drum machine         | yes                        | no               | MIDI            | 2.3.0                         | 2017     |
| [Denon MC7000](Denon%20MC7000)                                                                     | $750              | 4 channel controller with Dual USB                           | yes                        | yes              | MIDI            | 2.2.4                         | 2017     |
| [Akai MPD24](Akai%20MPD24)                                                                         | discontinued      | miscellaneous                                                | no                         | \-               | MIDI            | 1.8                           | 2007     |
| [Behringer BCD2000](Behringer%20BCD2000)                                                           | discontinued      | basic 2 deck                                                 | yes                        | no               | MIDI            | 1.11                          | 2006     |
| [Behringer CMD MM-1](Behringer%20CMD%20MM-1)                                                       | discontinued      | 4 deck mixer                                                 | no                         | \-               | MIDI            | 2.1                           | 2013     |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | discontinued      | CD player                                                    | no                         | \-               | MIDI            | 1.10                          | 2010     |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | discontinued      | basic 2 deck                                                 | yes                        | no               | MIDI            | 1.6                           | 2007     |
| [Behringer CMD Micro](Behringer%20CMD%20Micro)                                                     | discontinued      | basic 2 deck                                                 | no                         | \-               | MIDI            | 2.1                           | 2013     |
| [Denon SC2000](Denon%20SC2000)                                                                     | discontinued      | 1 deck                                                       | no                         | \-               | MIDI            | 1.8                           | 2010     |
| [DJ Tech CDJ-101](DJ%20Tech%20CDJ-101)                                                             | discontinued      | 2 deck jog wheel                                             | no                         | \-               | MIDI            | 1.11                          | 2011     |
| [DJ Tech DJM-101](DJ%20Tech%20DJM-101)                                                             | discontinued      | 2 deck mixer                                                 | no                         | \-               | MIDI            | 1.11                          | 2011     |
| [DJ Tech iMix Reload](DJ%20Tech%20iMix%20Reload)                                                   | discontinued      | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.10                          | 2009     |
| [DJ Tech Kontrol One](DJ%20Tech%20Kontrol%20One)                                                   | discontinued      | 4 decks                                                      | no                         | \-               | MIDI            | 1.11                          | 2009     |
| [DJ Tech Mixer One](DJ%20Tech%20Mixer%20One)                                                       | discontinued      | 2 deck mixer                                                 | no                         | \-               | MIDI            | 1.10.1                        | 2009     |
| [eks Otus](eks%20Otus)                                                                             | discontinued      | 1 turntable + 2 deck mixer                                   | yes                        | no               | HID             | 1.11                          | 2008     |
| [Electrix Tweaker](Electrix%20Tweaker)                                                             | discontinued      | 2 deck\[14\] without jog wheels                              | no                         | \-               | MIDI            | 2.0                           | 2012     |
| [Evolution X-Session](Evolution%20X-Session)                                                       | discontinued      | knobs + crossfader                                           | no                         | \-               | MIDI            | 1.6                           | 2006     |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | discontinued      | 2 deck mixer                                                 | no                         | \-               | MIDI            | 1.6                           | 2006     |
| [Gemini FirstMix](Gemini%20FirstMix)                                                               | discontinued      | basic 2 deck                                                 | no                         | \-               | MIDI            | 1.11                          | 2011     |
| [Kontrol DJ KDJ500](Kontrol%20DJ%20KDJ500)                                                         | discontinued      | basic 2 deck                                                 | no                         | \-               | MIDI            | 1.10                          | 2003     |
| [Korg nanoKONTROL](Korg%20nanoKONTROL)                                                             | discontinued      | 2 deck mixer                                                 | no                         | \-               | MIDI            | 1.8.2                         | 2009     |
| [Hercules DJ Control Air](hercules_dj_control_air)                                                 | discontinued      | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.11                          | 2012     |
| [Hercules DJ Control Instinct](Hercules%20DJ%20Control%20Instinct)                                 | discontinued      | basic 2 deck                                                 | yes                        | no               | MIDI            | 1.10.1                        | 2012     |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | discontinued      | 2 deck all-in-one                                            | yes                        | no               | MIDI \[15\]     | 1.7                           | 2004     |
| [Hercules DJ Console 4-Mx](Hercules%20DJ%20Console%204-Mx)                                         | discontinued      | 2 deck\[16\] all-in-one                                      | yes                        | yes              | MIDI \[17\]     | 1.11                          | 2010     |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | discontinued      | 2 deck all-in-one                                            | yes                        | no               | HID             | 1.11                          | 2003     |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | discontinued      | 2 deck all-in-one                                            | yes                        | no               | USB Bulk        | 1.8                           | 2010     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | discontinued      | 2 deck all-in-one                                            | no                         | \-               | HID             | 1.11                          | 2006     |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | discontinued      | 2 deck all-in-one                                            | no                         | \-               | HID             | 1.11                          | 2009     |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | discontinued      | basic 2 deck                                                 | no                         | \-               | MIDI            | 1.8                           | 2009     |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | discontinued      | 2 deck all-in-one                                            | yes                        | N/A              | MIDI            | 1.6                           | 2007     |
| [Mixman DM2](Mixman%20DM2)                                                                         | discontinued      | 2 decks                                                      | no                         | \-               | MIDI \[18\]     | 1.7                           | 2001     |
| [Mixvibes U-Mix Control 2](Mixvibes%20U-Mix%20Control%202%20Pro)                                   | discontinued      | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.10.1                        | 2011     |
| [Mixvibes U-Mix Control 2 Pro](Mixvibes%20U-Mix%20Control%202%20Pro)                               | discontinued      | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.11                          | 2011     |
| [Native Instruments Traktor Kontrol S4 Mk2](Native%20Instruments%20Traktor%20Kontrol%20S4%20Mk2)   | discontinued      | 4 deck all-in-one                                            | yes                        | yes              | HID             | 2.1                           | 2013     |
| [Novation Launchpad Mk1](Novation%20Launchpad%20Mk1)                                               | discontinued      | pad grid                                                     | no                         | \-               | MIDI \[19\]     | 1.11, 2.1                     | 2009     |
| [Novation Twitch](Novation%20Twitch)                                                               | discontinued      | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 2.1                           | 2011     |
| [Numark DJ2GO](Numark%20DJ2GO)                                                                     | discontinued      | basic 2 deck                                                 | no                         | \-               | MIDI            | 1.10                          | 2011     |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | discontinued      | 2 deck all-in-one                                            | yes                        | N/A              | MIDI            | 1.11                          | 2013     |
| [Numark Omni Control](Numark%20Omni%20Control)                                                     | discontinued      | 2 deck all-in-one                                            | yes                        | no               | MIDI \[20\]     | 1.10                          | 2008     |
| [Numark Total Control](Numark%20Total%20Control)                                                   | discontinued      | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.6                           | 2007     |
| [Numark Mixtrack](Numark%20Mixtrack)                                                               | discontinued      | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.8.2                         | 2010     |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | discontinued      | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.10                          | 2010     |
| [Numark N4](Numark%20N4)                                                                           | discontinued      | 4 deck all-in-one                                            | yes                        | yes              | MIDI            | 1.10                          | 2012     |
| [Numark NS7](Numark%20NS7)                                                                         | discontinued      | 2 deck all-in-one with motorized wheels                      | yes                        | yes              | MIDI            | 1.9                           | 2009     |
| [Numark V7](Numark%20V7)                                                                           | discontinued      | 2 deck motorized wheel                                       | yes                        | no               | MIDI            | 1.10                          | 2010     |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | discontinued      | CD player                                                    | no                         | \-               | MIDI or HID     | 1.8.2 (MIDI)                  | 2010     |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | discontinued      | CD player                                                    | yes                        | no               | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       | 2010     |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | discontinued      | CD player                                                    | yes                        | no               | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       | 2009     |
| [Pioneer DDJ-SB](Pioneer%20DDJ-SB)                                                                 | discontinued      | 2 deck\[21\] all-in-one                                      | yes                        | no               | MIDI            | 2.0                           | 2014     |
| [Pioneer DDJ-SB2](Pioneer%20DDJ-SB2)                                                               | discontinued      | 2 deck\[22\] all-in-one                                      | yes                        | no               | MIDI            | 2.0                           | 2015     |
| [Pioneer DDJ-SX](Pioneer%20DDJ-SX)                                                                 | discontinued      | 4 deck all-in-one controller/mixer                           | yes                        | yes              | MIDI            | 2.1                           | 2012     |
| [Pioneer DDJ-SX2](Pioneer%20DDJ-SX)                                                                | discontinued      | 4 deck all-in-one controller/mixer                           | yes                        | yes              | MIDI            | 2.1                           | 2014     |
| [Reloop Beatmix 2](Reloop%20Beatmix%202)                                                           | discontinued      | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 2.1                           | 2014     |
| [Reloop Beatmix 4](Reloop%20Beatmix%204)                                                           | discontinued      | 4 deck all-in-one                                            | yes                        | no               | MIDI            | 2.1                           | 2014     |
| [Reloop Beatpad](Reloop%20Beatpad)                                                                 | discontinued      | 2 deck all-in-one                                            | yes                        | yes              | MIDI            | 2.0                           | 2014     |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | discontinued      | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.8                           | 2009     |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | discontinued      | 2 deck all-in-one                                            | yes                        | yes              | MIDI \[23\]     | 1.8                           | 2009     |
| [Reloop Jockey 3 ME](Reloop%20Jockey%203%20ME)                                                     | discontinued      | 2 deck\[24\] all-in-one                                      | yes                        | yes              | MIDI \[25\]     | 2.1                           | 2011     |
| [Reloop Terminal Mix 2](Reloop%20Terminal%20Mix)                                                   | discontinued      | 2 deck\[26\] all-in-one                                      | yes                        | yes              | MIDI            | 1.11                          | 2012     |
| [Reloop Terminal Mix 4](Reloop%20Terminal%20Mix)                                                   | discontinued      | 4 deck all-in-one                                            | yes                        | yes              | MIDI            | 1.11                          | 2012     |
| [Tascam US-428](Tascam%20US-428)                                                                   | discontinued      | mixing console                                               | yes                        | no               | MIDI            | 1.6.2                         | 2001     |
| [Vestax VCI-100MKI](Vestax%20VCI-100)                                                              | discontinued      | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.6                           | 2007     |
| [Vestax VCI-100MKII](Vestax%20VCI-100MKII)                                                         | discontinued      | 2 deck\[27\] all-in-one                                      | yes                        | no               | MIDI            | 2.0                           | 2011     |
| [Vestax VCI-300](Vestax%20VCI-300)                                                                 | discontinued      | 2 deck all-in-one                                            | yes                        | yes              | MIDI            | 1.11                          | 2008     |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | discontinued      | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.9                           | 2010     |
| [Vestax Spin](Vestax%20Spin)                                                                       | discontinued      | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.9                           | 2009     |

\</sortable\>

#### Esoteric controllers

These are devices that were not designed for controlling music software
but have been mapped to Mixxx anyway.

\<sortable 2=numeric\>

| Device                                 | Price (USD) | Description             | Integrated audio interface | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------- | ----------- | ----------------------- | -------------------------- | ---------------- | --------------- | ----------------------------- | -------- |
| [Nintendo Wiimote](Nintendo%20Wiimote) | $25         | game console controller | no                         | \-               | HID             | 1.11                          | 2006     |
| [Sony SixxAxis](Sony%20SixxAxis)       | $25         | game console controller | no                         | \-               | HID             | 1.11                          | 2006     |

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

<table>
<thead>
<tr class="header">
<th>Device</th>
<th>Price (USD) [28]</th>
<th>Description</th>
<th>Integrated Sound Card</th>
<th>Balanced outputs</th>
<th>Signal protocol</th>
<th>Released</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="Akai AMX">Akai AMX</a></td>
<td>$250</td>
<td>2 deck mixer</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2014</td>
</tr>
<tr class="even">
<td><a href="Faderfox DJ44">Faderfox DJ44</a></td>
<td>€499</td>
<td>2/4 deck[29] mobile controller</td>
<td>no</td>
<td>-</td>
<td>MIDI</td>
<td>2013</td>
</tr>
<tr class="odd">
<td><a href="Gemini G4V">Gemini G4V</a></td>
<td>$350</td>
<td>2 deck[30] all-in-one</td>
<td>yes</td>
<td>yes</td>
<td>MIDI</td>
<td>2013</td>
</tr>
<tr class="even">
<td><a href="Pioneer DDJ-400">Pioneer DDJ-400</a></td>
<td>$279</td>
<td>2 deck controller all-in-one</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2018</td>
</tr>
<tr class="odd">
<td><a href="DDJ-1000">Pioneer DDJ-1000</a></td>
<td>1199</td>
<td>4 deck controller all-in-one</td>
<td>yes</td>
<td>yes</td>
<td>MIDI and HID</td>
<td>2018</td>
</tr>
<tr class="even">
<td><a href="Pioneer DDJ-SB3">Pioneer DDJ-SB3</a></td>
<td>$249</td>
<td>2 deck controller [31] all-in-one</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2018</td>
</tr>
<tr class="odd">
<td><a href="Pioneer DDJ-WeGO">Pioneer DDJ-WeGO</a></td>
<td>discontinued</td>
<td>2 deck controller</td>
<td>yes</td>
<td>n/a</td>
<td>MIDI</td>
<td>2012</td>
</tr>
<tr class="even">
<td><a href="Pioneer DDJ-WeGO3">Pioneer DDJ-WeGO3</a></td>
<td>$300</td>
<td>2 deck controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2014</td>
</tr>
<tr class="odd">
<td><a href="Behringer CMD PL-1">Behringer CMD PL-1</a></td>
<td>$100</td>
<td>1 deck controller</td>
<td>no</td>
<td>-</td>
<td>MIDI</td>
<td>2013</td>
</tr>
<tr class="even">
<td><a href="JBSystems DJ-kontrol 3">JBSystems DJ-kontrol 3</a><br />
<a href="Resident DJ-kontrol 3">(Resident DJ-kontrol 3 identically?)</a></td>
<td>$200</td>
<td>2 deck controller</td>
<td>yes</td>
<td>yes</td>
<td>MIDI</td>
<td>2012</td>
</tr>
<tr class="odd">
<td><a href="Behringer CMD Studio 2a">Behringer CMD Studio 2a</a></td>
<td>$100</td>
<td>2 deck controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2014</td>
</tr>
<tr class="even">
<td><a href="Roland DJ-202">Roland DJ-202</a></td>
<td>$300</td>
<td>2 deck[32] all-in-one</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2017</td>
</tr>
<tr class="odd">
<td><a href="Hercules DJ Control Instinct P8">Hercules DJ Control Instinct P8</a></td>
<td>€90</td>
<td>2 deck[33] all-in-one</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2016</td>
</tr>
<tr class="even">
<td><a href="Hercules DJ Control Jogvision">Hercules DJ Control Jogvision</a></td>
<td>$250</td>
<td>2 deck all-in-one controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2015</td>
</tr>
<tr class="odd">
<td><a href="Hercules Universal DJ">Hercules Universal DJ</a></td>
<td>$250</td>
<td>2 deck all-in-one controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2014</td>
</tr>
<tr class="even">
<td><a href="Hercules DJ Control Starlight">Hercules DJ Control Starlight</a></td>
<td>$99</td>
<td>2 deck all-in-one compact controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2018</td>
</tr>
<tr class="odd">
<td><a href="Hercules DJControl Inpulse 200">Hercules DJControl Inpulse 200</a></td>
<td>$129</td>
<td>2 deck all-in-one controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2018</td>
</tr>
<tr class="even">
<td><a href="Hercules DJControl Inpulse 300">Hercules DJControl Inpulse 300</a></td>
<td>$250</td>
<td>2 deck all-in-one controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2018</td>
</tr>
<tr class="odd">
<td><a href="Hercules DJControl AIR Plus">Hercules DJControl AIR Plus</a></td>
<td>Discontinued</td>
<td>2 deck all-in-one controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2013</td>
</tr>
<tr class="even">
<td><a href="Hercules DJ 4set">Hercules DJ 4set</a></td>
<td>Discontinued</td>
<td>2 deck[34] all-in-one controller</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2011</td>
</tr>
<tr class="odd">
<td><a href="Native Instruments Traktor Kontrol Z1">Native Instruments Traktor Kontrol Z1</a></td>
<td>$200</td>
<td>2 deck compact</td>
<td>yes</td>
<td>no</td>
<td>HID</td>
<td>2013</td>
</tr>
<tr class="even">
<td><a href="Native Instruments Traktor Kontrol F1">Native Instruments Traktor Kontrol F1</a></td>
<td>$200</td>
<td>originally branded as "Remix controller", but very versatile</td>
<td>no</td>
<td>-</td>
<td>HID</td>
<td>2012</td>
</tr>
<tr class="odd">
<td><a href="Soundless Studio joyMIDI">Soundless Studio joyMIDI</a></td>
<td>$85</td>
<td>2 deck controller</td>
<td>no</td>
<td>no</td>
<td>MIDI</td>
<td>2019</td>
</tr>
<tr class="even">
<td><a href="Stanton DJC.4">Stanton DJC.4</a></td>
<td>Discontinued</td>
<td>2 deck controller [35] all-in-one</td>
<td>yes</td>
<td>yes</td>
<td>MIDI</td>
<td>2012</td>
</tr>
<tr class="odd">
<td><a href="Numark DJ2GO2 Touch">Numark DJ2GO2 Touch</a></td>
<td>$79</td>
<td>2 deck pocket dj controller with capacitive touch jog wheels</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2019</td>
</tr>
<tr class="even">
<td><a href="Numark iDJ Live II">Numark iDJ Live II</a></td>
<td>discontinued</td>
<td>basic 2 deck</td>
<td>no</td>
<td>-</td>
<td>MIDI</td>
<td>2014</td>
</tr>
</tbody>
</table>

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
The Windows and macOS drivers can translate the HID signals to MIDI, but
this is not available on GNU/Linux. So, if you make a mapping for these
controllers, please make an HID mapping so it is compatible with every
OS that Mixxx runs on.

Native Instruments' older DJ controllers use a proprietary protocol
called NHL that Mixxx does not support. The Windows and macOS drivers
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

## Microphones

Mixxx can work with any microphone that can be plugged into your audio
interface. Refer to the [Mixxx
Manual](https://mixxx.org/manual/latest/en/chapters/microphones.html)
for a detailed explanation of different options for setting up Mixxx
with microphones. As explained in the manual, **USB microphones are not
recommended** because they cannot be used with direct monitoring with
Mixxx.

The table of
[\#USB-audio-interfaces](#USB-audio-interfaces)-below-has-notes-regarding-use-of-some-audio-interfaces-with-microphones.-As-[explained
in the
manual](https://mixxx.org/manual/latest/en/chapters/microphones.html#hardware-mixers),
**Behringer Xenyx and Yamaha AG03/AG06 mixers are not recommended**
because their audio interfaces only have 2 channels for output.

## Splitter cables

Splitter cables are **the cheapest way** to get two separate sound
outputs from your computer. These plug into the onboard audio interface
built into computer motherboards and split the stereo signal into two
separate mono signals. However, onboard audio interfaces are not good
quality, and you lose the stereo effect of hearing different sounds
arranged in space.

Devices marketed as "headphone splitter" instead of DJ splitters
duplicate one stereo signal in two jacks. These cannot be used for
headphone cueing. Also, generic stereo-to-mono splitter cables or
adapters typically have two mono jack outputs. Plugging headphones or
stereo speakers into a generic stereo-to-mono splitter will only play
sound on one side of the headphones or speakers.

Available DJ splitter cables:

  - [Native Instruments Traktor DJ
    Cable](http://www.native-instruments.com/en/products/traktor/traktor-for-ios/traktor-dj-cable/):
    $10

## Audio interfaces

To be able to hear the next track you want to mix in before your
audience hears it, you need two separate sound outputs. Most computers
come with an audio interface built into the motherboard with only 1
stereo 1/8“ headphone output (2 mono channels). Onboard audio interfaces
built into computers generally have bad sound quality and may pick up
interference from other devices in the computer, especially the charger
or power supply. **It is recommended to use one audio interface with at
least 4 mono output channels (2 stereo channels).** For vinyl control,
it is recommended to use an audio interface with phono preamplifiers.

### Compatibility

As stated above, Mixxx can use any audio interface that your OS has a
driver to use. All USB audio interfaces listed in the table below work
with Windows, macOS, and Linux.

Thunderbolt audio interfaces can operate at lower latencies than USB or
Firewire audio interfaces, but are generally only compatible with macOS.

### USB audio interfaces

These devices allow a computer to output and input sound. Any audio
interface that your operating system has a driver to use can be used
with Mixxx. All the USB audio interfaces in the table below are
compatible with Windows, macOS, and Linux. It is possible to use just an
audio interface plus a keyboard & mouse to use Mixxx, but a separate
[controller](#controllers) makes using Mixxx easier, more intuitive, and
more fun.

An audio interface with at least 4 mono output channels (2 stereo pairs)
is recommended for most uses. Refer to the [Mixxx
manual](https://mixxx.org/manual/latest/chapters/setup.html) for
details. If your audio interface does not have 4 output channels, it is
possible to use multiple audio interfaces. However, this increases
latency. On Windows, it can be tricky to configure Mixxx to use both of
them at the same time depending on the sound APIs supported by each
audio interface's driver.

Surround sound (5.1 or 7.1) cards are not recommended. They sometimes do
signal processing in hardware or in the driver to split a stereo signal
into multiple components. It may be possible to configure them to output
separate master and headphone stereo signals, but it is often tricky to
do so.

This table only lists a handful of available USB audio interfaces that
are currently in production and suitable for use with Mixxx. There are
many more options available that may be better for you depending on your
input and output needs and the sound quality you can afford. You
generally get the sound quality you pay for with audio interfaces. The
[Mixxx
manual](http://mixxx.org/manual/latest/en/chapters/hardware.html#audio-interface-considerations)
has more information to help decide on an audio interface to use.

\<sortable 2=numeric\>

| Device                                                                                                                                 | Price (USD) \[36\] | Channels out | Balanced outputs | Channels in | Microphone input with direct monitoring | Phono preamp | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------ | ---------------- | ----------- | --------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Generic USB audio interfaces                                                                                                           | \< $10             | 2            | no               | 0-2         | no                                      | no           | These look similar to USB flash drives. They tend to be poor quality, sometimes even worse than onboard audio interfaces. [\#Splitter cables](#Splitter%20cables) are another option in this price range.                                                                                                                                                                                                                                    |
| [Behringer U-Phono UFO202](http://www.music-group.com/Categories/Behringer/Computer-Audio/Audio-Interfaces/UFO202/p/P0A12)             | $30                | 2            | no               | 2           | no                                      | yes          | Cheapest option for vinyl control, but requires using 2 of them and making [a small hardware modification](http://mixxx.org/forums/viewtopic.php?f=6&t=2438). Not to be confused with the Behringer U-Control **UCA**202 & **UCA**222, which do not have phono preamps and cannot be used for vinyl control.                                                                                                                                 |
| [Behringer U-Phoria UMC204HD](http://www.musictri.be/Categories/Behringer/Computer-Audio/Interfaces/UMC204HD/p/P0BK0)                  | $80                | 4            | yes              | 2           | yes                                     | no           | Cheapest option for broadcasting with a microphone input and independent main & headphone outputs. However, it has no loopback input, so it is more complicated to [configure the microphone input](https://mixxx.org/manual/latest/en/chapters/microphones.html#direct-monitoring). Sound quality is [adequate but not great](https://www.audiosciencereview.com/forum/index.php?threads/behringer-umc204-hd-audio-interface-review.9856/). |
| [ESI Maya 44 USB+](http://www.esi-audio.com/products/maya44usb+/)                                                                      | $140               | 4            | no               | 4           | no                                      | no           | Does not have phono preamps on the inputs, but has been reported to work for vinyl control.                                                                                                                                                                                                                                                                                                                                                  |
| [Roland Rubix24](https://www.roland.com/us/products/rubix24/)                                                                          | $200               | 4            | yes              | 2           | yes                                     | no           | Good balance of sound quality and price with independent main and headphone outputs. Has microphone inputs with direct monitoring and loopback for [easy setup](https://mixxx.org/manual/latest/en/chapters/microphones.html#direct-monitoring). Also, the microphone inputs have compressors that can be used with direct monitoring.                                                                                                       |
| [Focusrite Scarlett 2i4](http://us.focusrite.com/usb-audio-interfaces/scarlett-2i4)                                                    | $200               | 4            | yes              | 2           | yes                                     | no           | Good balance of sound quality and price with independent main and headphone outputs. Has microphone inputs with direct monitoring but no loopback input.                                                                                                                                                                                                                                                                                     |
| [Denon DS1](https://www.denondj.com/dvs-audio-interface-for-serato-ds1)                                                                | $300               | 4            | no               | 4           | no                                      | yes          | Higher quality option for vinyl control. Comes with a pair of Serato timecode vinyl that are compatible with Mixxx.                                                                                                                                                                                                                                                                                                                          |
| [Native Instruments Traktor Scratch Audio 6](https://www.native-instruments.com/en/products/traktor/digital-vinyl/traktor-scratch-a6/) | $300               | 6            | no               | 6           | no                                      | yes          | Higher quality option for vinyl control. Has an extra stereo pair of inputs for recording or broadcasting with an external hardware mixer. The included Traktor Scratch Mk2 timecode vinyl are not compatible with Mixxx;[compatible control vinyl](https://mixxx.org/manual/latest/en/chapters/vinyl_control.html#supported-timecode-media) can be purchased separately.                                                                    |
| [RME Babyface Pro FS](https://www.rme-audio.com/babyface-pro-fs.html/)                                                                 | $900               | 4            | yes              | 4           | yes                                     | no           | Very high sound quality. Requires a [kernel patch](https://github.com/MrBollie/RME-Babyace-Pro-ALSA-Mixer-Patch) for full control of direct monitor routing on Linux \< 5.8.                                                                                                                                                                                                                                                                 |

\</sortable\>

### Mixers with audio interfaces

These are devices that can mix audio from different sources without
needing a computer. They also have a built-in USB audio interface to
connect directly to a computer without needing a separate audio
interface. They tend to be much more expensive than comparable
[\#controllers](#controllers) and [\#USB audio
interfaces](#USB%20audio%20interfaces). They are often found installed
in venues for multiple DJs to use.

Each conversion of a signal between digital and analog forms adds noise
and distortion. So, if the mixer's processing is done digitally, it is
best to use the audio interface built into a mixer (or a digital input
if the mixer has one). When analog outputs of a separate audio interface
are plugged into a digital mixer, the audio interface converts the
digital signals to analog, then the mixer converts the analog signals
back to digital for its processing. If the input to the mixer is
digital, those two conversions do not occur.

However, some of these mixers are analog mixers and the built in audio
interface converts the digital signals from the computer to analog for
the mixer's analog processing. In that case, using the mixer's built in
audio interface may or may not sound better than a separate audio
interface, depending on the quality of each of the audio interfaces.

Many of these mixers also send MIDI signals to the computer over USB,
which could be mapped to control Mixxx.

Most of these have a single USB port, but some have two. Two USB ports
allows two different DJs to use the mixer's audio interface at the same
time with their own computer for collaborative DJ sets and easy,
seamless transitions between DJs. \<sortable 2=numeric\>

| Device                                                                                                                      | Price (USD) \[37\] | Decks | Phono preamps | USB ports | Analog or digital mixing | Linux         |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----- | ------------- | --------- | ------------------------ | ------------- |
| [Allen & Heath Xone 23C](http://www.allen-heath.com/ahproducts/xone-23c/)                                                   | $400               | 2     | 2             | 1         | analog                   | yes \[38\]    |
| [Native Instruments Traktor Kontrol Z2](http://www.native-instruments.com/en/products/traktor/dj-mixer/traktor-kontrol-z2/) | $600               | 2     | 2             | 1         | ?                        | likely \[39\] |
| [Allen & Heath Xone 43C](http://www.allen-heath.com/ahproducts/xone43C/)                                                    | $1000              | 4     | 4             | 1         | analog                   | likely \[40\] |
| [Pioneer DJM-750](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-750)                                                 | $1000              | 4     | 2             | 1         | digital                  | ?             |
| [Pioneer DJM-5000](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-5000)                                               | $1000              | 4     | 0             | 1         | digital                  | ?             |
| [Allen & Heath Xone DB2](http://www.allen-heath.com/ahproducts/xonedb2/)                                                    | $1500              | 4     | 4             | 1         | digital                  | no            |
| [Pioneer DJM-850](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-850)                                                 | $1500              | 4     | 2             | 1         | digital                  | ?             |
| [Rane TTM57MkII](http://dj.rane.com/products/ttm57mkii)                                                                     | $1750              | 2     | 2             | 2         | digital                  | likely \[41\] |
| [Rane MP2014](http://dj.rane.com/products/mp2014-mixer)                                                                     | $2000              | 4     | 2             | 2         | digital                  | likely \[42\] |
| [Allen & Heath Xone DB4](http://www.allen-heath.com/ahproducts/xonedb4/)                                                    | $2000              | 4     | 4             | 1         | digital                  | no            |
| [Pioneer DJM-900NXS](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-900NXS)                                           | $2000              | 4     | 2             | 1         | digital                  | ?             |
| [Rane Sixty-Two](http://dj.rane.com/products/sixty-two)                                                                     | $2000              | 2     | 2             | 2         | digital                  | no            |
| [Pioneer DJM-900NXS2](https://www.pioneerdj.com/en-us/product/mixer/djm-900nxs2/black/overview/)                            | $2200              | 4     | 4             | 2         | digital                  | ?             |
| [Rane Sixty-Four](http://dj.rane.com/products/sixty-four)                                                                   | $2200              | 4     | 4             | 2         | digital                  | no            |
| [Pioneer DJM-900SRT](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-900SRT)                                           | $2300              | 4     | 2             | 1         | digital                  | ?             |
| [Pioneer DJM-2000NXS](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-2000NXS)                                         | $2500              | 4     | 2             | 1         | digital                  | likely \[43\] |
| [Rane MP2015](http://dj.rane.com/products/mp2015-mixer)                                                                     | $2900              | 4     | 4             | 2         | digital                  | likely \[44\] |

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

2.  4 deck control available by toggling between decks 1/3 and decks 2/4

3.  4 deck control available by toggling between decks 1/3 and decks 2/4

4.  The default Mixxx mapping has this mapped to hotcues.

5.  Mapping supports 4-deck switching

6.  Mapping supports 4-deck switching

7.  Mapping supports n-deck switching

8.  Prices listed on this page are the prevailing prices for unused
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

9.  The Novation Dicer is priced per pair.

10. 4 deck control available by toggling between decks 1/3 and decks 2/4

11. This controller could potentially be mapped many ways. The mapping
    included in Mixxx maps it as a 2 deck mixer.

12. 4 deck control available by toggling between decks 1/3 and decks 2/4

13. 4 deck control available by toggling between decks 1/3 and decks 2/4

14. 4 deck control available by toggling between decks 1/3 and decks 2/4

15. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on macOS. There is no driver
    available for Linux or Windows.

16. 4 deck control available by toggling between decks 1/3 and decks 2/4

17. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and macOS. There is
    no driver available for Linux.

18. [macOS driver](http://www.joemattiello.com/dm2/); [Linux MIDI
    Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz), [Alternate
    Linux MIDI driver
    (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2),
    [dm2linux on
    sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453)

19. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and macOS. There is
    no driver available for Linux.

20. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and macOS. There is
    no driver available for Linux.

21. 4 deck control available by toggling between decks 1/3 and decks 2/4

22. 4 deck control available by toggling between decks 1/3 and decks 2/4

23. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and macOS. There is
    no driver available for Linux.

24. 4 deck control available by toggling between decks 1/3 and decks 2/4

25. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on macOS. There is no driver
    available for Linux or Windows.

26. 4 deck control available by toggling between decks 1/3 and decks 2/4

27. 4 deck control available by toggling between decks 1/3 and decks 2/4

28. Prices listed on this page are the prevailing prices for unused
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

29. 4 deck control available by toggling between decks 1/3 and decks 2/4

30. 4 deck control available by toggling between decks 1/3 and decks 2/4

31. 4 deck control available by toggling between decks 1/3 and decks 2/4

32. 4 deck control available by toggling between decks 1/3 and decks 2/4

33. 4 deck control available by toggling between decks 1/3 and decks 2/4

34. 4 deck control available by toggling between decks 1/3 and decks 2/4

35. 4 deck control available by toggling between decks 1/3 and decks 2/4

36. Prices listed on this page are the prevailing prices for unused
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

37. Prices listed on this page are the prevailing prices for unused
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

38. Needs a udev rule to configure it as a 4 input + 4 output mixer for
    DVS - see this
    [gist](https://gist.github.com/timnugent/ed65a79b2bd6c63788bfada3624756a4)

39. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

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
