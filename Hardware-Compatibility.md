# Mixxx DJ Hardware Guide

## What kind of hardware should I get to DJ with Mixxx?

Bare minimum equipment for DJing:

  - computer - preferably a laptop
  - Audio output solution for speakers and headphones 
    - [splitter cable](https://manual.mixxx.org/latest/en/chapters/hardware#hardware-splitter-cables) - _e.g. the [Native Instruments Traktor DJ Cable](http://www.native-instruments.com/en/products/traktor/traktor-for-ios/traktor-dj-cable/) for ~10€_
    - [audio interface](#audio-interfaces) - usually a USB device with multiple analog audio channels
  - [headphones](https://manual.mixxx.org/latest/de/chapters/hardware#headphones)
  - speakers
  - audio cables and adapters

Helpful but not strictly necessary:

  - [audio interface](#audio-interfaces) with 4 mono output channels (2 stereo pairs)
  - [controller](#controllers) and/or [turntables with timecode vinyl](http://mixxx.org/manual/latest/chapters/vinyl_control.html)
  - [laptop stand](https://github.com/mixxxdj/mixxx/wiki/Laptop-Stands)
  - [microphone (analog)](https://manual.mixxx.org/latest/en/chapters/microphones) - USB microphones are not recommended
  - surge protector
  - cases for laptop, controller, and headphones
  - backpack or other carrying case
  - mouse
  - portable hard drive
  - powered USB hub
  - [custom fader and knob caps](custom-caps.md) to customize your gear

See [the manual](http://mixxx.org/manual/latest/chapters/example_setups) for
diagrams and descriptions of setups with different kinds of hardware.

See the [Beginner DJ Links](https://github.com/mixxxdj/mixxx/wiki/Beginner-DJ-Links.md) page for more helpful
resources.

## Hardware compatibility

Because Mixxx is [free software](http://www.gnu.org/philosophy/free-sw.html) — 
free as in artistic freedom, not just price — we strive to make it work
with as much hardware as we can. Mixxx is collaboratively developed by a
community of volunteers and we can only make mappings for controllers
that we have. If hardware does not work with Mixxx, that does not mean
it is impossible, it only means that no one has made it work with Mixxx
yet. Anyone, including you, is welcome to contribute to make Mixxx
compatible with more hardware.

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
API](http://mixxx.org/manual/latest/chapters/preferences/sound_hardware#sound-api).
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
_Note: this list is possibly incomplete! See the 
[Hardware section in the Manual](https://manual.mixxx.org/latest/en/hardware/manuals.html) 
for a complete list of mappings included in mixxx_

| Device                                                                           | Price (USD) \[1\] | Description                                             | Integrated Sound Card | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
|----------------------------------------------------------------------------------|------------------|---------------------------------------------------------|-----------------------|------------------|-----------------|-------------------------------|----------|
| [Allen & Heath Xone K1](Allen-&-Heath-Xone-K2-K1)                                | $250             | 2 decks + 2 effect units, or 4 decks, or 4 effect units | no                    | \-               | MIDI            | 2.1                           | 2014     |
| [Allen & Heath Xone K2](Allen-&-Heath-Xone-K2-K1)                                | $270             | 2 decks + 2 effect units, or 4 decks, or 4 effect units | yes                   | no               | MIDI            | 1.11                          | 2012     |
| [Hercules DJControl Compact](Hercules-DJControl-Compact.md)                     | $80              | basic 2 deck                                            | no                    | \-               | MIDI            | 2.1                           | 2015     |
| [Hercules P32 DJ](Hercules-P32-DJ.md)                                           | $250             | 2 deck[^3] without jog wheels                           | yes                   | no               | MIDI            | 2.1                           | 2016     |
| [American Audio VMS4/4.1](American-Audio-VMS4.md)                               | discontinued     | 4 deck all-in-one                                       | yes                   | yes              | MIDI            | 1.9                           | 2012     |
| [Denon HS5500](Denon-HS5500.md)                                                   | discontinued     | 2-decks-in-1 CD player with motorized platter           | yes                   | no               | MIDI            | 2.0                           | 2008     |
| [Denon MC6000MK2](Denon-MC6000MK2.md)                                             | discontinued     | 4 deck all-in-one                                       | yes                   | yes              | MIDI            | 2.0                           | 2015     |
| [DJ TechTools MIDIFighter Classic](DJ-TechTools-MIDIFighter-Classic.md)       | discontinued     | 4x4 spring-loaded arcade button grid [^4]               | no                    | \-               | MIDI            | 1.8                           | 2011     |
| [Hercules DJ Console Mk2](Hercules-PC-DJ-Console.md)                          | discontinued     | 2 deck all-in-one                                       | yes                   | no               | USB Bulk        | 1.11                          | 2008     |
| [Hercules DJ Console RMX](Hercules-DJ-Console-RMX.md)                         | discontinued     | basic 2 deck all-in-one                                 | yes                   | yes              | HID             | 1.11                          | 2008     |
| [Hercules DJ Console RMX 2](Hercules-DJ-Console-RMX-2.md)                   | discontinued     | 2 deck all-in-one                                       | yes                   | yes              | MIDI            | 1.11                          | 2012     |
| [Hercules DJ Control MP3 e2 / MP3 LE / Glow](Hercules-DJ-Control-MP3-e2.md) | discontinued     | basic 2 deck[^2]                                        | no                    | \-               | USB Bulk        | 1.11                          | 2009     |
| [Korg Kaoss DJ](Korg-Kaoss-DJ.md)                                               | discontinued     | 2 deck controller and standalone mixer (switchable)     | yes                   | no               | MIDI            | 2.1                           | 2015     |
| [M-Audio X-Session Pro](M-Audio-X-Session-Pro.md)                               | discontinued     | 2 deck mixer                                            | no                    | \-               | MIDI            | 1.6                           | 2007     |
| [[Native Instruments Traktor Kontrol S2 Mk2]]                                    | discontinued     | 2 deck all-in-one                                       | yes                   | yes              | HID             | 2.3                           | 2013     |
| [Stanton SCS.1d](Stanton-SCS.1d.md)                                               | discontinued     | 1 turntable [^7]                                        | no                    | \-               | HSS1394 (MIDI)  | 1.9.1                         | 2009     |
| [Stanton SCS.1m](Stanton-SCS.1m.md)                                               | discontinued     | 4 deck mixer                                            | yes                   | yes              | HSS1394 (MIDI)  | 1.7                           | 2009     |
| [Stanton SCS.3d](Stanton-SCS.3d.md)                                               | discontinued     | 1 deck control [^5]                                     | no                    | \-               | MIDI            | 1.7                           | 2009     |
| [Stanton SCS.3m](Stanton-SCS.3m.md)                                               | discontinued     | 2 deck mixer [^6]                                       | no                    | \-               | MIDI            | 1.7                           | 2009     |
| [Vestax VCI-400](Vestax-VCI-400.md)                                               | discontinued     | 4 deck all-in-one                                       | yes                   | yes              | MIDI            | 1.10.1                        | 2012     |

### Community Supported Mappings

All of these devices have mappings included in Mixxx. There may be other
mappings more suited to your workflow on [the
forum](http://www.mixxx.org/forums/viewforum.php?f=7).

Do not add mappings to this list until they have been included in Mixxx.
If you make a mapping for a controller, please add it to the [\#Mappings
In Development](#Mappings%20In%20Development) table and refer to the
[Contributing Mappings](Contributing-Mappings.md) page for instructions
on how to get it included in Mixxx. When the pull request is merged,
move your controller to this table.

| Device                                                                                             | Price (USD) \[8\] | Description                                                  | Integrated audio interface | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
|----------------------------------------------------------------------------------------------------|------------------|--------------------------------------------------------------|----------------------------|------------------|-----------------|-------------------------------|----------|
| [Akai LPD8](Akai-LPD8.md)                                                                           | $70              | miscellaneous                                                | no                         | \-               | MIDI            | 1.10.1                        | 2010     |
| [American Audio VMS2](American-Audio-VMS2.md)                                                     | $250             | 2 deck all-in-one                                            | yes                        | yes              | MIDI            | 1.11                          | 2011     |
| [Behringer CMD Studio 4a](Behringer-CMD-Studio-4a.md)                                           | $200             | 2 deck [^10] all-in-one                                      | yes                        | no               | MIDI            | 2.1                           | 2013     |
| [Behringer DDM4000](https://manual.mixxx.org/2.3/en/hardware/controllers/behringer_ddm4000.html)   | $380             | 4 deck mixer                                                 | no                         | -                | MIDI            | 2.3                           | 2007     |
| [Denon MC4000](Denon-MC4000.md)                                                                     | $400             | 2 deck controller and mixer                                  | yes                        | yes              | MIDI            | 2.1                           | 2015     |
| [Denon MC7000](Denon-MC7000.md)                                                                     | $750             | 4 channel controller with Dual USB                           | yes                        | yes              | MIDI            | 2.2.4                         | 2017     |
| [DJ Tech Tools MIDI Fighter Twister](DJ-Tech-Tools-MIDI-Fighter-Twister.md)                 | $220             | 2 deck controller [^11]                                      | no                         | \-               | MIDI            | 2.1.5                         | 2015     |
| [Hercules DJ Control Inpulse 300](Hercules-DJControl-Inpulse-300.md)                            | $250             | basic 2 deck                                                 | yes                        | no               | MIDI            | 2.2.4                         | 2018     |
| [Hercules DJ Control Instinct S](Hercules-DJ-Control-Instinct.md)                               | $100             | basic 2 deck                                                 | yes                        | no               | MIDI            | 1.10.1                        | 2015     |
| [Keith McMillen QuNeo](Keith-McMillen-QuNeo.md)                                                   | $250             | miscellaneous                                                | no                         | \-               | MIDI            | 1.11                          | 2012     |
| [Korg nanoKONTROL 2](Korg-nanoKONTROL-2.md)                                                       | $60              | miscellaneous                                                | no                         | \-               | MIDI            | 1.11                          | 2011     |
| [Native Instruments Traktor Kontrol F1](Native-Instruments-Traktor-Kontrol-F1.md)             | $200             | originally branded as "Remix controller", but very versatile | no                         | \-               | HID             | 1.11                          | 2012     |
| [Native Instruments Traktor Kontrol S2 MK3](Native-Instruments-Traktor-Kontrol-S2-MK3.md)   | $300             | 2 deck controller all-in-one                                 | yes                        | no               | HID             | 2.2.4                         | 2018     |
| [Novation Dicer](Novation-Dicer.md)                                                                 | $100 \[9\]        | pads for use with turntables                                 | no                         | \-               | MIDI            | 1.10                          | 2010     |
| [Novation Launchpad Mini](Novation-Launchpad-Mini.md)                                             | $75              | pad grid                                                     | no                         | \-               | MIDI            | 2.0                           | 2013     |
| [Novation Launchpad Mk2](Novation-Launchpad-Mk2.md)                                               | $150             | pad grid                                                     | no                         | \-               | MIDI            | 2.1                           | 2015     |
| [Numark Mixtrack 3](Numark-Mixtrack-Pro-3.md)                                                   | $150             | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 2.1                           | 2015     |
| [Numark Mixtrack Platinum](Numark-Mixtrack-Platinum.md)                                           | $250             | 2 deck[^12] all-in-one                                       | yes                        | no               | MIDI            | 2.2.0                         | 2016     |
| [Numark Mixtrack Pro 3](Numark-Mixtrack-Pro-3.md)                                               | $200             | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 2.1                           | 2015     |
| [Roland DJ-505](Roland-DJ-505.md)                                                                   | $550             | 2 deck[^13] all-in-one with integrated drum machine          | yes                        | no               | MIDI            | 2.3.0                         | 2017     |
| [Akai MPD24](Akai-MPD24.md)                                                                         | discontinued     | miscellaneous                                                | no                         | \-               | MIDI            | 1.8                           | 2007     |
| [American Audio Radius 1000 / 2000 / 3000](American-Audio-Radius-1000-/-2000-/-3000.md) | discontinued     | CD player                                                    | no                         | \-               | MIDI            | 1.10                          | 2010     |
| [Behringer BCD2000](Behringer-BCD2000.md)                                                           | discontinued     | basic 2 deck                                                 | yes                        | no               | MIDI            | 1.11                          | 2006     |
| [Behringer BCR2000](https://manual.mixxx.org/2.3/en/hardware/controllers/behringer_bcr2000.html)   | discontinued     | miscellaneous                                                | no                         | -                | MIDI            | 2.3                           | 2006     |
| [Behringer CMD MM-1](Behringer-CMD-MM-1.md)                                                       | discontinued     | 4 deck mixer                                                 | no                         | \-               | MIDI            | 2.1                           | 2013     |
| [Behringer BCD3000](Behringer-BCD3000.md)                                                           | discontinued     | basic 2 deck                                                 | yes                        | no               | MIDI            | 1.6                           | 2007     |
| [Behringer CMD Micro](Behringer-CMD-Micro.md)                                                     | discontinued     | basic 2 deck                                                 | no                         | \-               | MIDI            | 2.1                           | 2013     |
| [Denon SC2000](Denon-SC2000.md)                                                                     | discontinued     | 1 deck                                                       | no                         | \-               | MIDI            | 1.8                           | 2010     |
| [DJ Tech CDJ-101](DJ-Tech-CDJ-101.md)                                                             | discontinued     | 2 deck jog wheel                                             | no                         | \-               | MIDI            | 1.11                          | 2011     |
| [DJ Tech DJM-101](DJ-Tech-DJM-101.md)                                                             | discontinued     | 2 deck mixer                                                 | no                         | \-               | MIDI            | 1.11                          | 2011     |
| [DJ Tech iMix Reload](DJ-Tech-iMix-Reload.md)                                                   | discontinued     | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.10                          | 2009     |
| [DJ Tech Kontrol One](DJ-Tech-Kontrol-One.md)                                                   | discontinued     | 4 decks                                                      | no                         | \-               | MIDI            | 1.11                          | 2009     |
| [DJ Tech Mixer One](DJ-Tech-Mixer-One.md)                                                       | discontinued     | 2 deck mixer                                                 | no                         | \-               | MIDI            | 1.10.1                        | 2009     |
| [eks Otus](eks-Otus.md)                                                                             | discontinued     | 1 turntable + 2 deck mixer                                   | yes                        | no               | HID             | 1.11                          | 2008     |
| [Electrix Tweaker](Electrix-Tweaker.md)                                                             | discontinued     | 2 deck[^14] without jog wheels                               | no                         | \-               | MIDI            | 2.0                           | 2012     |
| [Evolution X-Session](Evolution-X-Session.md)                                                       | discontinued     | knobs + crossfader                                           | no                         | \-               | MIDI            | 1.6                           | 2006     |
| [FaderFox DJ2](FaderFox-DJ2.md)                                                                     | discontinued     | 2 deck mixer                                                 | no                         | \-               | MIDI            | 1.6                           | 2006     |
| [Gemini FirstMix](Gemini-FirstMix.md)                                                               | discontinued     | basic 2 deck                                                 | no                         | \-               | MIDI            | 1.11                          | 2011     |
| [Kontrol DJ KDJ500](Kontrol-DJ-KDJ500.md)                                                         | discontinued     | basic 2 deck                                                 | no                         | \-               | MIDI            | 1.10                          | 2003     |
| [Korg nanoKONTROL](Korg-nanoKONTROL.md)                                                             | discontinued     | 2 deck mixer                                                 | no                         | \-               | MIDI            | 1.8.2                         | 2009     |
| [Hercules DJ Console Mac Edition](Hercules-PC-DJ-Console.md)                                    | discontinued     | 2 deck all-in-one                                            | yes                        | no               | MIDI [^15]      | 1.7                           | 2004     |
| [Hercules DJ Console 4-Mx](Hercules-DJ-Console-4-Mx.md)                                         | discontinued     | 4 deck[^16] all-in-one                                       | yes                        | yes              | USB Bulk [^17]  | 1.11                          | 2010     |
| [Hercules DJ Console Mk1](Hercules-PC-DJ-Console.md)                                            | discontinued     | 2 deck all-in-one                                            | yes                        | no               | HID             | 1.11                          | 2003     |
| [Hercules DJ Console Mk4](Hercules-PC-DJ-Console.md)                                            | discontinued     | 2 deck all-in-one                                            | yes                        | no               | USB Bulk        | 1.8                           | 2010     |
| [Hercules DJ Control Air](hercules_dj_control_air)                                                 | discontinued     | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.11                          | 2012     |
| [Hercules DJ Control Instinct](Hercules-DJ-Control-Instinct.md)                                 | discontinued     | basic 2 deck                                                 | yes                        | no               | MIDI            | 1.10.1                        | 2012     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | discontinued     | 2 deck all-in-one                                            | no                         | \-               | HID             | 1.11                          | 2006     |
| [Hercules DJ Control Steel](Hercules-PC-DJ-Console.md)                                          | discontinued     | 2 deck all-in-one                                            | no                         | \-               | HID             | 1.11                          | 2009     |
| [Ion Discover DJ](Ion-Discover-DJ.md)                                                             | discontinued     | basic 2 deck                                                 | no                         | \-               | MIDI            | 1.8                           | 2009     |
| [[Ion Discover DJ Pro]]                                                                            | discontinued     | 2 deck all-in-one                                            | yes                        | \-               | MIDI            | 2.3                           | 2012     |
| [M-Audio Xponent](M-Audio-Xponent.md)                                                               | discontinued     | 4 deck[^16] all-in-one                                       | yes                        | N/A              | MIDI            | 1.6                           | 2007     |
| [Mixman DM2](Mixman-DM2.md)                                                                         | discontinued     | 2 decks                                                      | no                         | \-               | MIDI [^18]      | 1.7                           | 2001     |
| [Mixvibes U-Mix Control 2](Mixvibes-U-Mix-Control-2-Pro.md)                                   | discontinued     | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.10.1                        | 2011     |
| [Mixvibes U-Mix Control 2 Pro](Mixvibes-U-Mix-Control-2-Pro.md)                               | discontinued     | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.11                          | 2011     |
| [Native Instruments Traktor Kontrol S4 Mk2](Native-Instruments-Traktor-Kontrol-S4-Mk2.md)   | discontinued     | 4 deck all-in-one                                            | yes                        | yes              | HID             | 2.1                           | 2013     |
| [Novation Launchpad Mk1](Novation-Launchpad-Mk1.md)                                               | discontinued     | pad grid                                                     | no                         | \-               | MIDI [^19]      | 1.11, 2.1                     | 2009     |
| [Novation Twitch](Novation-Twitch.md)                                                               | discontinued     | 2 deck all-in-one                                            | yes                        | \-               | MIDI            | 2.1                           | 2011     |
| [Numark DJ2GO](Numark-DJ2GO.md)                                                                     | discontinued     | basic 2 deck                                                 | no                         | \-               | MIDI            | 1.10                          | 2011     |
| [Numark Mixtrack Pro II](Numark-Mixtrack-Pro-II.md)                                             | discontinued     | 2 deck all-in-one                                            | yes                        | N/A              | MIDI            | 1.11                          | 2013     |
| [Numark Omni Control](Numark-Omni-Control.md)                                                     | discontinued     | 2 deck all-in-one                                            | yes                        | no               | MIDI [^20]      | 1.10                          | 2008     |
| [Numark Total Control](Numark-Total-Control.md)                                                   | discontinued     | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.6                           | 2007     |
| [Numark Mixtrack](Numark-Mixtrack.md)                                                               | discontinued     | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.8.2                         | 2010     |
| [Numark Mixtrack Pro](Numark-Mixtrack-Pro.md)                                                     | discontinued     | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.10                          | 2010     |
| [Numark N4](Numark-N4.md)                                                                           | discontinued     | 4 deck all-in-one                                            | yes                        | yes              | MIDI            | 1.10                          | 2012     |
| [Numark NS7](Numark-NS7.md)                                                                         | discontinued     | 2 deck all-in-one with motorized wheels                      | yes                        | yes              | MIDI            | 1.9                           | 2009     |
| [Numark V7](Numark-V7.md)                                                                           | discontinued     | 2 deck motorized wheel                                       | yes                        | no               | MIDI            | 1.10                          | 2010     |
| [Pioneer CDJ-350](Pioneer-CDJ-350.md)                                                               | discontinued     | CD player                                                    | no                         | \-               | MIDI or HID     | 1.8.2 (MIDI)                  | 2010     |
| [Pioneer CDJ-850](Pioneer-CDJ-850.md)                                                               | discontinued     | CD player                                                    | yes                        | no               | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       | 2010     |
| [Pioneer CDJ-2000](Pioneer-CDJ-2000.md)                                                             | discontinued     | CD player                                                    | yes                        | no               | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       | 2009     |
| [Pioneer DDJ-SB](Pioneer-DDJ-SB.md)                                                                 | discontinued     | 2 deck[^21] all-in-one                                       | yes                        | no               | MIDI            | 2.0                           | 2014     |
| [Pioneer DDJ-SB2](Pioneer-DDJ-SB2.md)                                                               | discontinued     | 2 deck[^22] all-in-one                                       | yes                        | no               | MIDI            | 2.0                           | 2015     |
| [Pioneer DDJ-SX](Pioneer-DDJ-SX.md)                                                                 | discontinued     | 4 deck all-in-one controller/mixer                           | yes                        | yes              | MIDI            | 2.1                           | 2012     |
| [Pioneer DDJ-SX2](Pioneer-DDJ-SX.md)                                                                | discontinued     | 4 deck all-in-one controller/mixer                           | yes                        | yes              | MIDI            | 2.1                           | 2014     |
| [Reloop Beatmix 2](Reloop-Beatmix-2.md)                                                           | discontinued     | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 2.1                           | 2014     |
| [Reloop Beatmix 4](Reloop-Beatmix-4.md)                                                           | discontinued     | 4 deck all-in-one                                            | yes                        | no               | MIDI            | 2.1                           | 2014     |
| [Reloop Beatpad](Reloop-Beatpad.md)                                                                 | discontinued     | 2 deck all-in-one                                            | yes                        | yes              | MIDI            | 2.0                           | 2014     |
| [Reloop Digital Jockey 2 Controller Edition](Reloop-Digital-Jockey-2-Controller-Edition.md) | discontinued     | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.8                           | 2009     |
| [Reloop Digital Jockey 2 Master Edition](Reloop-Digital-Jockey-2-Master-Edition.md)         | discontinued     | 2 deck all-in-one                                            | yes                        | yes              | MIDI [^23]      | 1.8                           | 2009     |
| [Reloop Jockey 3 ME](Reloop-Jockey-3-ME.md)                                                     | discontinued     | 2 deck[^24] all-in-one                                       | yes                        | yes              | MIDI [^25]      | 2.1                           | 2011     |
| [Reloop Terminal Mix 2](Reloop-Terminal-Mix.md)                                                   | discontinued     | 2 deck[^26] all-in-one                                       | yes                        | yes              | MIDI            | 1.11                          | 2012     |
| [Reloop Terminal Mix 4](Reloop-Terminal-Mix.md)                                                   | discontinued     | 4 deck all-in-one                                            | yes                        | yes              | MIDI            | 1.11                          | 2012     |
| [Stanton DJC.4](Stanton-DJC.4.md)                                                                   | discontinued     | 2 deck[^2] all-in-one                                        | yes                        | yes              | MIDI            | 2.2.4                         | 2012     |
| [Tascam US-428](Tascam-US-428.md)                                                                   | discontinued     | mixing console                                               | yes                        | no               | MIDI            | 1.6.2                         | 2001     |
| [Vestax VCI-100MKI](Vestax-VCI-100.md)                                                              | discontinued     | 2 deck all-in-one                                            | no                         | \-               | MIDI            | 1.6                           | 2007     |
| [Vestax VCI-100MKII](Vestax-VCI-100MKII.md)                                                         | discontinued     | 2 deck[^27] all-in-one                                       | yes                        | no               | MIDI            | 2.0                           | 2011     |
| [Vestax VCI-300](Vestax-VCI-300.md)                                                                 | discontinued     | 2 deck all-in-one                                            | yes                        | yes              | MIDI            | 1.11                          | 2008     |
| [Vestax Typhoon](Vestax-Typhoon.md)                                                                 | discontinued     | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.9                           | 2010     |
| [Vestax Spin](Vestax-Spin.md)                                                                       | discontinued     | 2 deck all-in-one                                            | yes                        | no               | MIDI            | 1.9                           | 2009     |

#### Esoteric controllers

These are devices that were not designed for controlling music software
but have been mapped to Mixxx anyway.

| Device                                 | Price (USD) | Description             | Integrated audio interface | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
|----------------------------------------|-------------|-------------------------|----------------------------|------------------|-----------------|-------------------------------|----------|
| [Nintendo Wiimote](Nintendo-Wiimote.md) | $25         | game console controller | no                         | \-               | HID             | 1.11                          | 2006     |
| [Sony SixxAxis](Sony-SixxAxis.md)       | $25         | game console controller | no                         | \-               | HID             | 1.11                          | 2006     |

### Mappings In Development

These controllers have Mixxx mappings under active development. If you
are considering getting one of these controllers, you are encouraged to
do so. You can help the development of the mapping by testing it and
providing feedback to the developer. You can also [edit the mapping
yourself](home#controller%20mapping%20documentation). Click the name of
the controller for more information.

When a mapping is included in Mixxx, please move it to the [\#Mixxx
Certified Mappings](#Mixxx%20Certified%20Mappings) or [\#Community
Supported Mappings](#Community%20Supported%20Mappings) table above.

| Device                                                                                                            | Price (USD) [^28] | Description                                                        | Integrated Sound Card | Balanced outputs | Signal protocol | Released |
|-------------------------------------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------|-----------------------|------------------|-----------------|----------|
| [Akai AMX](Akai-AMX.md)                                                                                              | $250              | 2 deck mixer                                                       | yes                   | no               | MIDI            | 2014     |
| [Faderfox DJ44](Faderfox-DJ44.md)                                                                                    | €499              | 2/4 deck[^29] mobile controller                                    | no                    | \-               | MIDI            | 2013     |
| [Gemini G4V](Gemini-G4V.md)                                                                                          | $350              | 2 deck[^30] all-in-one                                             | yes                   | yes              | MIDI            | 2013     |
| [Pioneer DDJ-400](Pioneer-DDJ-400.md)                                                                                | $279              | 2 deck controller all-in-one                                       | yes                   | no               | MIDI            | 2018     |
| [Pioneer DDJ-1000](DDJ-1000)                                                                                      | 1199              | 4 deck controller all-in-one                                       | yes                   | yes              | MIDI and HID    | 2018     |
| [Pioneer DDJ-SB3](Pioneer-DDJ-SB3.md)                                                                                | $249              | 2 deck controller [^31] all-in-one                                 | yes                   | no               | MIDI            | 2018     |
| [Pioneer DDJ-WeGO](Pioneer-DDJ-WeGO.md)                                                                              | discontinued      | 2 deck controller                                                  | yes                   | n/a              | MIDI            | 2012     |
| [Pioneer DDJ-WeGO3](Pioneer-DDJ-WeGO3.md)                                                                            | $300              | 2 deck controller                                                  | yes                   | no               | MIDI            | 2014     |
| [Pioneer XDJ-RX](Pioneer-XDJ-RX.md)                                                                                  | discontinued      | all-in-one DJ system(2 deck controller)                            | yes                   | n/a              | MIDI            | 2015     |
| [Behringer CMD PL-1](Behringer-CMD-PL-1.md)                                                                          | $100              | 1 deck controller                                                  | no                    | \-               | MIDI            | 2013     |
| [JBSystems DJ-kontrol 3](JBSystems-DJ-kontrol-3.md)<br>[(Resident DJ-kontrol 3 identically?)](Resident-DJ-kontrol-3.md) | $200              | 2 deck controller                                                  | yes                   | yes              | MIDI            | 2012     |
| [Behringer CMD Studio 2a](Behringer-CMD-Studio-2a.md)                                                                | $100              | 2 deck controller                                                  | yes                   | no               | MIDI            | 2014     |
| [[Denon DJ Prime 4]]                                                                                              | $1,899            | 4 deck standalone unit + controller                                | yes                   | yes              | MIDI            | 2019     |
| [Hercules DJ Control Instinct P8](Hercules-DJ-Control-Instinct-P8.md)                                                | €90               | 2 deck[^33] all-in-one                                             | yes                   | no               | MIDI            | 2016     |
| [Hercules DJ Control Jogvision](Hercules-DJ-Control-Jogvision.md)                                                    | $250              | 2 deck all-in-one controller                                       | yes                   | no               | MIDI            | 2015     |
| [Hercules Universal DJ](Hercules-Universal-DJ.md)                                                                    | $250              | 2 deck all-in-one controller                                       | yes                   | no               | MIDI            | 2014     |
| [Hercules DJ Control Starlight](Hercules-DJ-Control-Starlight.md)                                                    | $99               | 2 deck all-in-one compact controller                               | yes                   | no               | MIDI            | 2018     |
| [Hercules DJControl Inpulse 200](Hercules-DJControl-Inpulse-200.md)                                                  | $129              | 2 deck all-in-one controller                                       | yes                   | no               | MIDI            | 2018     |
| [[Hercules DJControl Inpulse 500]]                                                                                | $300              | 2 deck all-in-one controller                                       | yes                   | yes              | MIDI            | 2020     |
| [Hercules DJControl AIR Plus](Hercules-DJControl-AIR-Plus.md)                                                        | Discontinued      | 2 deck all-in-one controller                                       | yes                   | no               | MIDI            | 2013     |
| [Hercules DJ 4set](Hercules-DJ-4set.md)                                                                              | Discontinued      | 2 deck[^34] all-in-one controller                                  | yes                   | no               | MIDI            | 2011     |
| [Native Instruments Traktor Kontrol Z1](Native-Instruments-Traktor-Kontrol-Z1.md)                                    | $200              | 2 deck compact                                                     | yes                   | no               | HID             | 2013     |
| [Native Instruments Traktor Kontrol F1](Native-Instruments-Traktor-Kontrol-F1.md)                                    | $200              | originally branded as "Remix controller", but very versatile       | no                    | \-               | HID             | 2012     |
| [Numark DJ2GO2 Touch](Numark-DJ2GO2-Touch.md)                                                                        | $79               | 2 deck pocket dj controller with capacitive touch jog wheels       | yes                   | no               | MIDI            | 2019     |
| [Numark iDJ Live II](Numark-iDJ-Live-II.md)                                                                          | discontinued      | basic 2 deck                                                       | no                    | \-               | MIDI            | 2014     |
| [[Numark Party Mix]]                                                                                              | $119              | USB-powered 2-deck portable dj controller with built-in light show | yes                   | no               | MIDI            | 2016     |
| [Roland DJ-202](Roland-DJ-202.md)                                                                                    | $300              | 2 deck[^32] all-in-one                                             | yes                   | no               | MIDI            | 2017     |
| [Soundless Studio joyMIDI](Soundless-Studio-joyMIDI.md)                                                              | $85               | 2 deck controller                                                  | no                    | no               | MIDI            | 2019     |

### Not mapped controllers

There are too many DJ controllers out there to list. Some of these controllers may have mappings (of unverified quality and may be
incomplete) posted on [the forums](https://mixxx.discourse.group/c/controller-mappings/10) that have not
(yet) been included with Mixxx. If a controller you own or are interested in getting is not listed here, search the
forum to see if anyone has posted a mapping. If you are willing to put in the effort to map one of these controllers, please get the controller, map it, and [contribute the mapping to Mixxx](contributing-mappings.md).

#### Note regarding Native Instruments controllers

Native Instruments' newer DJ controllers are USB HID class compliant devices ([source](http://www.native-instruments.com/en/support/knowledge-base/show/1925/i-cannot-find-the-driver-for-my-ni-device-on-the-website-mac-os-x/)). The Windows and macOS drivers can translate the HID signals to MIDI, but this is not available on GNU/Linux. So, if you make a mapping for these controllers, please make an HID mapping so it is compatible with every OS that Mixxx runs on.

Native Instruments' first generation DJ controllers use a proprietary protocol called NHL that Mixxx does not support. The Windows and macOS drivers
can switch these controllers to a MIDI mode by pressing certain buttons (see [the Native Instruments
website](https://www.native-instruments.com/en/support/knowledge-base/show/3659/how-to-use-your-native-instruments-controller-in-midi-mode/)
for the button combination for each controller), which could be mapped to Mixxx. Unfortunately, because this is done by the driver and not the controller firmware, these controllers cannot be used as MIDI controllers on GNU/Linux. However, the snd-usb-caiaq driver in Linux
supports the audio interfaces in at least some of these devices. It also registers the signals from some of the controllers as generic Linux
input events. To get these devices to work with Mixxx on GNU/Linux, either the driver would need to be modified to translate these signals
to HID or MIDI, Mixxx would need to be able to read Linux input events, or a program would need to translate the Linux input events to HID or MIDI.

## Audio interfaces

To be able to hear the next track you want to mix in before your audience hears it, you need two separate sound outputs. Most computers
come with an audio interface built into the motherboard with only 1 stereo 1/8“ headphone output (2 mono channels). Onboard audio interfaces
built into computers generally have bad sound quality and may pick up interference from other devices in the computer, especially the charger or power supply. **It is recommended to use one audio interface with at least 4 mono output channels (2 stereo channels).** For vinyl control, it is recommended to use an audio interface with phono preamplifiers.

### Compatibility

As stated above, Mixxx can use any audio interface that your OS has a driver to use. All USB audio interfaces listed in the table below work
with Windows, macOS, and Linux.

Thunderbolt audio interfaces can operate at lower latencies than USB or Firewire audio interfaces, but are generally only compatible with macOS.

### USB audio interfaces

These devices allow a computer to output and input sound. Any audio interface that your operating system has a driver to use can be used
with Mixxx. All the USB audio interfaces in the table below are compatible with Windows, macOS, and Linux unless otherwise noted. It is possible to use just an audio interface plus a keyboard & mouse to use Mixxx, but a separate [controller](#controllers) makes using Mixxx easier, more intuitive, and more fun.

An audio interface with at least 4 mono output channels (2 stereo pairs) is recommended for most uses. Refer to the [Mixxx
manual](https://mixxx.org/manual/latest/chapters/setup.html) for details. If your audio interface does not have 4 output channels, it is
possible to use multiple audio interfaces. However, this increases latency. On Windows, it can be tricky to configure Mixxx to use both of them at the same time depending on the sound APIs supported by each audio interface's driver.

Surround sound (5.1 or 7.1) cards are not recommended. They sometimes do signal processing in hardware or in the driver to split a stereo signal into multiple components. It may be possible to configure them to output separate master and headphone stereo signals, but it is often tricky to do so.

This table only lists a handful of available USB audio interfaces that are currently in production and suitable for use with Mixxx. There are
many more options available that may be better for you depending on your input and output needs and the sound quality you can afford. You
generally get the sound quality you pay for with audio interfaces. The [Mixxx manual](http://mixxx.org/manual/latest/en/chapters/hardware.html#audio-interface-considerations) has more information to help decide on an audio interface to use.

| Device                                                                                                                                 | Price (USD) [^36]                            | Channels out | Balanced outputs | Channels in | Microphone input with direct monitoring | Phono preamp | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|--------------|------------------|-------------|-----------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Generic USB audio interfaces                                                                                                           | \< $10                                       | 2            | no               | 0-2         | no                                      | no           | These look similar to USB flash drives. They tend to be poor quality, sometimes even worse than onboard audio interfaces. [Splitter cables](#Splitter-cables) are another option in this price range.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Behringer U-Phono UFO202](https://www.behringer.com/product.html?modelCode=P0A12)                                                     | $40                                          | 2            | no               | 2           | no                                      | yes          | Cheapest option for vinyl control, but requires using 2 of them and making [a small hardware modification](https://mixxx.discourse.group/t/modifying-the-behringer-ufo202-for-use-with-mixxx/11352). Not to be confused with the Behringer U-Control **UCA**202 & **UCA**222, which do not have phono preamps and cannot be used for vinyl control.                                                                                                                                                                                                                                                                   |
| [Behringer U-Phoria UMC204HD](https://www.behringer.com/product.html?modelCode=P0BK0)                                                  | $130                                         | 4            | yes              | 2           | yes                                     | no           | Cheapest option for broadcasting with a microphone input and independent main & headphone outputs. However, it has no loopback input, so it is more complicated to [configure the microphone input](https://mixxx.org/manual/latest/en/chapters/microphones.html#direct-monitoring). Sound quality is [adequate but not great](https://www.audiosciencereview.com/forum/index.php?threads/behringer-umc204-hd-audio-interface-review.9856/).                                                                                                                                                                          |
| [ESI Maya 44 USB+](http://www.esi-audio.com/products/maya44usb+/)                                                                      | $140                                         | 4            | no               | 4           | no                                      | no           | Does not have phono preamps on the inputs, but has been reported to work for vinyl control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Roland Rubix24](https://www.roland.com/us/products/rubix24/)                                                                          | $200                                         | 4            | yes              | 2           | yes                                     | no           | Good balance of sound quality and price with independent main and headphone outputs. Has microphone inputs with direct monitoring and loopback for [easy setup](https://mixxx.org/manual/latest/en/chapters/microphones.html#direct-monitoring). Also, the microphone inputs have compressors that can be used with direct monitoring.                                                                                                                                                                                                                                                                                |
| [Focusrite Scarlett 4i4](https://us.focusrite.com/en/usb-audio-interface/scarlett/scarlett-4i4)                                        | $230                                         | 4            | yes              | 4           | yes                                     | no           | Good balance of sound quality and price with independent main and headphone outputs. Has microphone inputs with direct monitoring but no loopback input. Also has an additional stereo pair of line inputs. [Direct monitoring cannot be controlled on Linux](https://linuxmusicians.com/viewtopic.php?f=6&t=20669) without an [out-of-tree kernel patch](https://github.com/geoffreybennett/scarlett-gen2/tree/scarlett-gen3). Linux users may consider getting a used [Scarlett 2i4](https://us.focusrite.com/en/usb-audio-interface/scarlett/scarlett-2i4) instead (the 2i4 was discontinued in favor of the 4i4). |
| [Native Instruments Traktor Scratch Audio 6](https://www.native-instruments.com/en/products/traktor/digital-vinyl/traktor-scratch-a6/) | $320                                         | 6            | no               | 6           | no                                      | yes          | Higher quality option for vinyl control. Has an extra stereo pair of inputs for recording or broadcasting with an external hardware mixer. The included Traktor Scratch Mk2 timecode vinyl are not compatible with Mixxx; [compatible control vinyl](https://mixxx.org/manual/latest/en/chapters/vinyl_control.html#supported-timecode-media) can be purchased separately.                                                                                                                                                                                                                                            |
| [Denon DS1](https://www.denondj.com/dvs-audio-interface-for-serato-ds1)                                                                | $350                                         | 4            | no               | 4           | no                                      | yes          | Higher quality option for vinyl control. Comes with a pair of Serato timecode vinyl that are compatible with Mixxx.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RME Babyface Pro FS](https://www.rme-audio.com/babyface-pro-fs.html)                                                                  | $900                                         | 4            | yes              | 4           | yes                                     | no           | Very high sound quality. Requires an [out-of-tree kernel patch](https://github.com/MrBollie/RME-Babyace-Pro-ALSA-Mixer-Patch) for full control of direct monitor routing on Linux < 5.8 (in particular, direct monitoring mono inputs on both sides of stereo outputs).                                                                                                                                                                                                                                                                                                                                               |
| Rane SL-1                                                                                                                              | Discontinued (\< $70 on second-hand markets) | 2            | no               | 2           | no                                      | yes          | High quality sound card produced initially for vinyl emulation to use with Serato Scratch Live. Can be used as a simple sound card. [Requires Linux 6.0 to correctly work](https://bugzilla.kernel.org/show_bug.cgi?id=216082).                                                                                                                                                                                                                                                                                                                                                                                       |

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
seamless transitions between DJs.

| Device                                                                                                                      | Price (USD) \[37\] | Decks | Phono preamps | USB ports | Analog or digital mixing | Linux         |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----- | ------------- | --------- | ------------------------ | ------------- |
| [Allen & Heath Xone 23C](http://www.allen-heath.com/ahproducts/xone-23c/)                                                   | $400               | 2     | 2             | 1         | analog                   | yes \[38\]    |
| [Native Instruments Traktor Kontrol Z2](http://www.native-instruments.com/en/products/traktor/dj-mixer/traktor-kontrol-z2/) | $600               | 2     | 2             | 1         | ?                        | likely \[39\] |
| [Allen & Heath Xone 43C](http://www.allen-heath.com/ahproducts/xone43C/)                                                    | $1000              | 4     | 4             | 1         | analog                   | no  \[40\]    |
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
    translated to MIDI by special drivers on macOS. On Linux, 
    [hdjd](https://github.com/nealey/hdjd) can be used.

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

38. 
* Needs a udev rule to configure it as a 4 input + 4 output mixer for
    DVS. When installing from your distributions repository, it should 
    already be located at `/usr/lib/udev/rules.d/69-mixxx-usb-uaccess.rules`.
    If not, see this [gist](https://gist.github.com/timnugent/ed65a79b2bd6c63788bfada3624756a4).  
* Between kernel 5.4.0.33 and 5.4.0.37, Linux changed USB 
    initialization scheme causing Xone:23C to not be detected as a 
    4 input + 4 output mixer anymore. You need to switch back to old 
    scheme before plugin the mixer either temporarily using 
    `echo Y >/sys/module/usbcore/parameters/old_scheme_first` or 
    definitely using the `usbcore.old_scheme_first=1` kernel parameter. 
    See [this page](https://wiki.archlinux.org/title/Kernel_parameters) 
    on how to add a parameter to your kernel.

39. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

40. The device shows up as 2 input + 2 output via the USB interface, see
    http://lkml.iu.edu/hypermail/linux/kernel/2106.0/02532.html

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
