# Mixxx DJ Hardware Guide

## What kind of hardware should I get to DJ with Mixxx?

Bare minimum equipment for DJing:

  - computer (preferably a laptop)
  - [splitter cable](#splitter-cables) or [sound card](#sound-cards)
  - [headphones](DJ%20headphones)
  - speakers
  - audio cables and adapters

Helpful but not strictly necessary:

  - [sound card](#sound-cards) with 4 mono output channels (2 stereo
    pairs)
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

### Mixxx Certified Mappings

Click the name of the controller for more information.

\<sortable 2=numeric\>

| Device                                                                           | Price (USD) \[1\] | Description                                   | Integrated Sound Card | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------------------------------------------------- | ----------------- | --------------------------------------------- | --------------------- | ---------------- | --------------- | ----------------------------- | -------- |
| [Hercules DJControl Compact](Hercules%20DJControl%20Compact)                     | $80               | basic 2 deck                                  | no                    | N/A              | MIDI            | 2.1\[2\]                      | 2015     |
| [Hercules DJ Control MP3 e2 / MP3 LE / Glow](Hercules%20DJ%20Control%20MP3%20e2) | $90               | basic 2 deck\[3\]                             | no                    | N/A              | USB Bulk        | 1.11\[4\]                     | 2009     |
| [Hercules P32 DJ](Hercules%20P32%20DJ)                                           | $250              | 2 deck\[5\] without jog wheels                | yes                   | no               | MIDI            | 2.1\[6\]                      | 2016     |
| [Allen & Heath Xone K2](Allen%20&%20Heath%20Xone%20K2)                           | $270              | 4 deck mixer + pads                           | yes                   | no               | MIDI            | 1.11                          | 2012     |
| [American Audio VMS4/4.1](American%20Audio%20VMS4)                               | discontinued      | 4 deck all-in-one                             | yes                   | yes              | MIDI            | 1.9                           | 2012     |
| [DJ TechTools MIDIFighter Classic](DJ%20TechTools%20MIDIFighter%20Classic)       | discontinued      | 4x4 spring-loaded arcade button grid \[7\]    | no                    | N/A              | MIDI            | 1.8                           | 2011     |
| [Denon HS5500](Denon%20HS5500)                                                   | discontinued      | 2-decks-in-1 CD player with motorized platter | yes                   | no               | MIDI            | 2.0                           | 2008     |
| [Hercules DJ Console Mk2](Hercules%20PC%20DJ%20Console)                          | discontinued      | 2 deck all-in-one                             | yes                   | no               | USB Bulk        | 1.11                          | 2008     |
| [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)                         | discontinued      | basic 2 deck all-in-one                       | yes                   | yes              | HID             | 1.11                          | 2008     |
| [Hercules DJ Console RMX 2](Hercules%20DJ%20Console%20RMX%202)                   | discontinued      | 2 deck all-in-one                             | yes                   | yes              | MIDI            | 1.11                          | 2012     |
| [M-Audio X-Session Pro](M-Audio%20X-Session%20Pro)                               | discontinued      | 2 deck mixer                                  | no                    | N/A              | MIDI            | 1.6                           | 2007     |
| [Stanton SCS.3d](Stanton%20SCS.3d)                                               | discontinued      | 1 deck control \[8\]                          | no                    | N/A              | MIDI            | 1.7                           | 2009     |
| [Stanton SCS.3m](Stanton%20SCS.3m)                                               | discontinued      | 2 deck mixer \[9\]                            | no                    | N/A              | MIDI            | 1.7                           | 2009     |
| [Stanton SCS.1m](Stanton%20SCS.1m)                                               | discontinued      | 4 deck mixer                                  | yes                   | yes              | HSS1394 (MIDI)  | 1.7                           | 2009     |
| [Stanton SCS.1d](Stanton%20SCS.1d)                                               | discontinued      | 1 turntable \[10\]                            | no                    | N/A              | HSS1394 (MIDI)  | 1.9.1                         | 2009     |
| [Vestax VCI-400](Vestax%20VCI-400)                                               | discontinued      | 4 deck all-in-one                             | yes                   | yes              | MIDI            | 1.10.1                        | 2012     |

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

| Device                                                                                             | Price (USD) \[11\] | Description                             | Integrated sound card | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------------------------------------------------------------------- | ------------------ | --------------------------------------- | --------------------- | ---------------- | --------------- | ----------------------------- | -------- |
| [Numark DJ2GO](Numark%20DJ2GO)                                                                     | $60                | basic 2 deck                            | no                    | N/A              | MIDI            | 1.10                          | 2011     |
| [Korg nanoKONTROL 2](Korg%20nanoKONTROL%202)                                                       | $60                | miscellaneous                           | no                    | N/A              | MIDI            | 1.11                          | 2011     |
| [Akai LPD8](Akai%20LPD8)                                                                           | $70                | miscellaneous                           | no                    | N/A              | MIDI            | 1.10.1                        | 2010     |
| [Novation Launchpad Mini](Novation%20Launchpad%20Mini)                                             | $75                | pad grid                                | no                    | N/A              | MIDI            | 2.0                           | 2013     |
| [Novation Dicer](Novation%20Dicer)                                                                 | $100 \[12\]        | pads for use with turntables            | no                    | N/A              | MIDI            | 1.10                          | 2010     |
| [Hercules DJ Control Instinct S](Hercules%20DJ%20Control%20Instinct)                               | $100               | basic 2 deck                            | yes                   | no               | MIDI            | 1.10.1                        | 2015     |
| [Novation Launchpad Mk2](Novation%20Launchpad%20Mk2)                                               | $150               | pad grid                                | no                    | N/A              | MIDI            | 2.1\[13\]                     | 2015     |
| [Numark Mixtrack 3](Numark%20Mixtrack%20Pro%203)                                                   | $150               | 2 deck all-in-one                       | no                    | N/A              | MIDI            | 2.1\[14\]                     | 2015     |
| [Behringer CMD Studio 4a](Behringer%20CMD%20Studio%204a)                                           | $200               | 2 deck \[15\] all-in-one                | yes                   | no               | MIDI            | 2.1\[16\]                     | 2013     |
| [Numark Mixtrack Pro 3](Numark%20Mixtrack%20Pro%203)                                               | $200               | 2 deck all-in-one                       | yes                   | no               | MIDI            | 2.1\[17\]                     | 2015     |
| [Keith McMillen QuNeo](Keith%20McMillen%20QuNeo)                                                   | $250               | miscellaneous                           | no                    | N/A              | MIDI            | 1.11                          | 2012     |
| [Pioneer DDJ-SB2](Pioneer%20DDJ-SB2)                                                               | $250               | 2 deck\[18\] all-in-one                 | yes                   | no               | MIDI            | 2.0                           | 2015     |
| [American Audio VMS2](American%20Audio%20VMS2)                                                     | $250               | 2 deck all-in-one                       | yes                   | yes              | MIDI            | 1.11                          | 2011     |
| [Denon MC4000](Denon%20MC4000)                                                                     | $400               | 2 deck controller and mixer             | yes                   | yes              | MIDI            | 2.1\[19\]                     | 2015     |
| [Denon MC6000MK2](Denon%20MC6000MK2)                                                               | $700               | 4 deck all-in-one                       | yes                   | yes              | MIDI            | 2.0                           | 2015     |
| [Akai MPD24](Akai%20MPD24)                                                                         | discontinued       | miscellaneous                           | no                    | N/A              | MIDI            | 1.8                           | 2007     |
| [Behringer BCD2000](Behringer%20BCD2000)                                                           | discontinued       | basic 2 deck                            | yes                   | no               | MIDI            | 1.11                          | 2006     |
| [American Audio Radius 1000 / 2000 / 3000](American%20Audio%20Radius%201000%20/%202000%20/%203000) | discontinued       | CD player                               | no                    | N/A              | MIDI            | 1.10                          | 2010     |
| [Behringer BCD3000](Behringer%20BCD3000)                                                           | discontinued       | basic 2 deck                            | yes                   | no               | MIDI            | 1.6                           | 2007     |
| [Behringer CMD Micro](Behringer%20CMD%20Micro)                                                     | discontinued       | basic 2 deck                            | no                    | N/A              | MIDI            | 2.1\[20\]                     | 2013     |
| [Denon SC2000](Denon%20SC2000)                                                                     | discontinued       | 1 deck                                  | no                    | N/A              | MIDI            | 1.8                           | 2010     |
| [DJ Tech CDJ-101](DJ%20Tech%20CDJ-101)                                                             | discontinued       | 2 deck jog wheel                        | no                    | N/A              | MIDI            | 1.11                          | 2011     |
| [DJ Tech DJM-101](DJ%20Tech%20DJM-101)                                                             | discontinued       | 2 deck mixer                            | no                    | N/A              | MIDI            | 1.11                          | 2011     |
| [DJ Tech iMix Reload](DJ%20Tech%20iMix%20Reload)                                                   | discontinued       | 2 deck all-in-one                       | no                    | N/A              | MIDI            | 1.10                          | 2009     |
| [DJ Tech Kontrol One](DJ%20Tech%20Kontrol%20One)                                                   | discontinued       | 4 decks                                 | no                    | N/A              | MIDI            | 1.11                          | 2009     |
| [DJ Tech Mixer One](DJ%20Tech%20Mixer%20One)                                                       | discontinued       | 2 deck mixer                            | no                    | N/A              | MIDI            | 1.10.1                        | 2009     |
| [eks Otus](eks%20Otus)                                                                             | discontinued       | 1 turntable + 2 deck mixer              | yes                   | no               | HID             | 1.11                          | 2008     |
| [Electrix Tweaker](Electrix%20Tweaker)                                                             | discontinued       | 2 deck\[21\] without jog wheels         | no                    | N/A              | MIDI            | 2.0                           | 2012     |
| [Evolution X-Session](Evolution%20X-Session)                                                       | discontinued       | knobs + crossfader                      | no                    | N/A              | MIDI            | 1.6                           | 2006     |
| [FaderFox DJ2](FaderFox%20DJ2)                                                                     | discontinued       | 2 deck mixer                            | no                    | N/A              | MIDI            | 1.6                           | 2006     |
| [Gemini FirstMix](Gemini%20FirstMix)                                                               | discontinued       | basic 2 deck                            | no                    | N/A              | MIDI            | 1.11                          | 2011     |
| [Kontrol DJ KDJ500](Kontrol%20DJ%20KDJ500)                                                         | discontinued       | basic 2 deck                            | no                    | N/A              | MIDI            | 1.10                          | 2003     |
| [Korg nanoKONTROL](Korg%20nanoKONTROL)                                                             | discontinued       | 2 deck mixer                            | no                    | N/A              | MIDI            | 1.8.2                         | 2009     |
| [Hercules DJ Control Air](hercules_dj_control_air)                                                 | discontinued       | 2 deck all-in-one                       | yes                   | no               | MIDI            | 1.11                          | 2012     |
| [Hercules DJ Control Instinct](Hercules%20DJ%20Control%20Instinct)                                 | discontinued       | basic 2 deck                            | yes                   | no               | MIDI            | 1.10.1                        | 2012     |
| [Hercules DJ Console Mac Edition](Hercules%20PC%20DJ%20Console)                                    | discontinued       | 2 deck all-in-one                       | yes                   | no               | MIDI \[22\]     | 1.7                           | 2004     |
| [Hercules DJ Console 4-Mx](Hercules%20DJ%20Console%204-Mx)                                         | discontinued       | 2 deck\[23\] all-in-one                 | yes                   | yes              | MIDI \[24\]     | 1.11                          | 2010     |
| [Hercules DJ Console Mk1](Hercules%20PC%20DJ%20Console)                                            | discontinued       | 2 deck all-in-one                       | yes                   | no               | HID             | 1.11                          | 2003     |
| [Hercules DJ Console Mk4](Hercules%20PC%20DJ%20Console)                                            | discontinued       | 2 deck all-in-one                       | yes                   | no               | USB Bulk        | 1.8                           | 2010     |
| [Hercules DJ Control MP3](Hercules_PC_DJ_Console)                                                  | discontinued       | 2 deck all-in-one                       | no                    | N/A              | HID             | 1.11                          | 2006     |
| [Hercules DJ Control Steel](Hercules%20PC%20DJ%20Console)                                          | discontinued       | 2 deck all-in-one                       | no                    | N/A              | HID             | 1.11                          | 2009     |
| [Ion Discover DJ](Ion%20Discover%20DJ)                                                             | discontinued       | basic 2 deck                            | no                    | N/A              | MIDI            | 1.8                           | 2009     |
| [M-Audio Xponent](M-Audio%20Xponent)                                                               | discontinued       | 2 deck all-in-one                       | yes                   | N/A              | MIDI            | 1.6                           | 2007     |
| [Mixman DM2](Mixman%20DM2)                                                                         | discontinued       | 2 decks                                 | no                    | N/A              | MIDI \[25\]     | 1.7                           | 2001     |
| [Mixvibes U-Mix Control 2](Mixvibes%20U-Mix%20Control%202%20Pro)                                   | discontinued       | 2 deck all-in-one                       | no                    | N/A              | MIDI            | 1.10.1                        | 2011     |
| [Mixvibes U-Mix Control 2 Pro](Mixvibes%20U-Mix%20Control%202%20Pro)                               | discontinued       | 2 deck all-in-one                       | yes                   | no               | MIDI            | 1.11                          | 2011     |
| [Novation Launchpad Mk1](Novation%20Launchpad%20Mk1)                                               | discontinued       | pad grid                                | no                    | N/A              | MIDI \[26\]     | 1.11, 2.1\[27\]               | 2009     |
| [Novation Twitch](Novation%20Twitch)                                                               | discontinued       | 2 deck all-in-one                       | no                    | N/A              | MIDI            | 2.1\[28\]                     | 2011     |
| [Numark Mixtrack Pro II](Numark%20Mixtrack%20Pro%20II)                                             | discontinued       | 2 deck all-in-one                       | yes                   | N/A              | MIDI            | 1.11                          | 2013     |
| [Numark Omni Control](Numark%20Omni%20Control)                                                     | discontinued       | 2 deck all-in-one                       | yes                   | no               | MIDI \[29\]     | 1.10                          | 2008     |
| [Numark Total Control](Numark%20Total%20Control)                                                   | discontinued       | 2 deck all-in-one                       | no                    | N/A              | MIDI            | 1.6                           | 2007     |
| [Numark Mixtrack](Numark%20Mixtrack)                                                               | discontinued       | 2 deck all-in-one                       | no                    | N/A              | MIDI            | 1.8.2                         | 2010     |
| [Numark Mixtrack Pro](Numark%20Mixtrack%20Pro)                                                     | discontinued       | 2 deck all-in-one                       | yes                   | no               | MIDI            | 1.10                          | 2010     |
| [Numark N4](Numark%20N4)                                                                           | discontinued       | 4 deck all-in-one                       | yes                   | yes              | MIDI            | 1.10                          | 2012     |
| [Numark NS7](Numark%20NS7)                                                                         | discontinued       | 2 deck all-in-one with motorized wheels | yes                   | yes              | MIDI            | 1.9                           | 2009     |
| [Numark V7](Numark%20V7)                                                                           | discontinued       | 2 deck motorized wheel                  | yes                   | no               | MIDI            | 1.10                          | 2010     |
| [Pioneer CDJ-350](Pioneer%20CDJ-350)                                                               | discontinued       | CD player                               | no                    | N/A              | MIDI or HID     | 1.8.2 (MIDI)                  | 2010     |
| [Pioneer CDJ-850](Pioneer%20CDJ-850)                                                               | discontinued       | CD player                               | yes                   | no               | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       | 2010     |
| [Pioneer CDJ-2000](Pioneer%20CDJ-2000)                                                             | discontinued       | CD player                               | yes                   | no               | MIDI or HID     | 1.10 (MIDI), 1.11 (HID)       | 2009     |
| [Pioneer DDJ-SB](Pioneer%20DDJ-SB)                                                                 | discontinued       | 2 deck\[30\] all-in-one                 | yes                   | no               | MIDI            | 2.0                           | 2014     |
| [Pioneer DDJ-SX](Pioneer%20DDJ-SX)                                                                 | discontinued       | 4 deck all-in-one controller/mixer      | yes                   | yes              | MIDI            | 2.1                           | 2012     |
| [Reloop Beatmix 2](Reloop%20Beatmix%202)                                                           | discontinued       | 2 deck all-in-one                       | yes                   | no               | MIDI            | 2.1\[31\]                     | 2014     |
| [Reloop Beatmix 4](Reloop%20Beatmix%204)                                                           | discontinued       | 4 deck all-in-one                       | yes                   | no               | MIDI            | 2.1\[32\]                     | 2014     |
| [Reloop Beatpad](Reloop%20Beatpad)                                                                 | discontinued       | 2 deck all-in-one                       | yes                   | yes              | MIDI            | 2.0                           | 2014     |
| [Reloop Digital Jockey 2 Controller Edition](Reloop%20Digital%20Jockey%202%20Controller%20Edition) | discontinued       | 2 deck all-in-one                       | no                    | N/A              | MIDI            | 1.8                           | 2009     |
| [Reloop Digital Jockey 2 Master Edition](Reloop%20Digital%20Jockey%202%20Master%20Edition)         | discontinued       | 2 deck all-in-one                       | yes                   | yes              | MIDI \[33\]     | 1.8                           | 2009     |
| [Reloop Jockey 3 ME](Reloop%20Jockey%203%20ME)                                                     | discontinued       | 2 deck\[34\] all-in-one                 | yes                   | yes              | MIDI            | 2.1\[35\]                     | 2011     |
| [Reloop Terminal Mix 2](Reloop%20Terminal%20Mix)                                                   | discontinued       | 2 deck\[36\] all-in-one                 | yes                   | yes              | MIDI            | 1.11                          | 2012     |
| [Reloop Terminal Mix 4](Reloop%20Terminal%20Mix)                                                   | discontinued       | 4 deck all-in-one                       | yes                   | yes              | MIDI            | 1.11                          | 2012     |
| [Tascam US-428](Tascam%20US-428)                                                                   | discontinued       | mixing console                          | yes                   | no               | MIDI            | 1.6.2                         | 2001     |
| [Vestax VCI-100MKI](Vestax%20VCI-100)                                                              | discontinued       | 2 deck all-in-one                       | no                    | N/A              | MIDI            | 1.6                           | 2007     |
| [Vestax VCI-100MKII](Vestax%20VCI-100MKII)                                                         | discontinued       | 2 deck\[37\] all-in-one                 | yes                   | no               | MIDI            | 2.0                           | 2011     |
| [Vestax VCI-300](Vestax%20VCI-300)                                                                 | discontinued       | 2 deck all-in-one                       | yes                   | yes              | MIDI            | 1.11                          | 2008     |
| [Vestax Typhoon](Vestax%20Typhoon)                                                                 | discontinued       | 2 deck all-in-one                       | yes                   | no               | MIDI            | 1.9                           | 2010     |
| [Vestax Spin](Vestax%20Spin)                                                                       | discontinued       | 2 deck all-in-one                       | yes                   | no               | MIDI            | 1.9                           | 2009     |

\</sortable\>

#### Esoteric controllers

These are devices that were not designed for controlling music software
but have been mapped to Mixxx anyway.

\<sortable 2=numeric\>

| Device                                 | Price (USD) | Description             | Integrated sound card | Balanced outputs | Signal protocol | Supported since Mixxx version | Released |
| -------------------------------------- | ----------- | ----------------------- | --------------------- | ---------------- | --------------- | ----------------------------- | -------- |
| [Nintendo Wiimote](Nintendo%20Wiimote) | $25         | game console controller | no                    | N/A              | HID             | 1.11                          | 2006     |
| [Sony SixxAxis](Sony%20SixxAxis)       | $25         | game console controller | no                    | N/A              | HID             | 1.11                          | 2006     |

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
<th>Price (USD) [38]</th>
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
<td><a href="Gemini G4V">Gemini G4V</a></td>
<td>$350</td>
<td>2 deck[39] all-in-one</td>
<td>yes</td>
<td>yes</td>
<td>MIDI</td>
<td>2013</td>
</tr>
<tr class="odd">
<td><a href="Pioneer DDJ-WeGO3">Pioneer DDJ-WeGO3</a></td>
<td>$300</td>
<td>2 deck controller and mixer</td>
<td>yes</td>
<td>no</td>
<td>MIDI</td>
<td>2014</td>
</tr>
<tr class="even">
<td><a href="Native Instruments Traktor Kontrol S4 Mk2">Native Instruments Traktor Kontrol S4 Mk2</a></td>
<td>$600</td>
<td>4 deck all-in-one</td>
<td>yes</td>
<td>yes</td>
<td>HID</td>
<td>2013</td>
</tr>
<tr class="odd">
<td><a href="Behringer CMD PL-1">Behringer CMD PL-1</a></td>
<td>$100</td>
<td>1 deck controller</td>
<td>no</td>
<td>no</td>
<td>MIDI</td>
<td>2013</td>
</tr>
<tr class="even">
<td><a href="Behringer CMD MM-1">Behringer CMD MM-1</a><br />
<a href="behringer_cmd_mm-1_advanced_mapping">(Alternative advanced mapping)</a></td>
<td>$100</td>
<td>MIDI mixer</td>
<td>no</td>
<td>no</td>
<td>MIDI</td>
<td>2013</td>
</tr>
<tr class="odd">
<td><a href="JBSystems DJ-kontrol 3">JBSystems DJ-kontrol 3</a><br />
<a href="Resident DJ-kontrol 3">(Resident DJ-kontrol 3 identically?)</a></td>
<td>$200</td>
<td>2 deck controller</td>
<td>yes</td>
<td>yes</td>
<td>MIDI</td>
<td>2012</td>
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
mono signals. However, onboard sound cards are not good quality, and you
cannot hear the arrangement of different sounds in space.

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
to use. All USB sound cards listed in the table below work with Windows,
macOS, and Linux.

Thunderbolt sound cards can operate at lower latencies than USB or
Firewire sound cards, but are generally only compatible with Mac OS X.

### Sound card considerations

#### Stand-alone sound cards versus sound cards integrated with controllers or mixers

Many DJ
[\#controllers](#controllers)-have-a-4-output-sound-card-built-into-them.-This-is-more-convenient-to-transport-and-set-up-than-a-stand-alone-[sound
card](#USB-sound-cards) plus a controller because it only requires one
device with one USB cable. However, stand-alone sound cards are
generally higher quality than those built into controllers (except for
the cheapest stand-alone sound cards).

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

Turntables, microphones, and instrument pickups all output very low
voltage signals that need to be amplified to line level by a
preamplifier before a sound card (or most audio equipment) can
effectively work with them. Additionally, vinyl records have the [RIAA
equalization curve](https://en.wikipedia.org/wiki/RIAA_equalization)
applied to the recording, which needs to be undone by a phono
preamplifier. If a device has a switch between phono, mic, or instrument
(contact microphone) level and line level, it has a preamplifier in it.
If you want to plug a microphone into your sound card, it will need a
microphone preamplifier. If you want to plug an electric guitar or bass
into your sound card, it will need an instrument preamplifier.

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

Sound cards sometimes have multiple connectors for a single channel,
resulting in more connectors than channels. So, not every connector can
send or receive an independent signal. For example, some sound cards
made for DJing have 4 output channels with 4 mono output connectors and
1 stereo headphone connector. This does not mean that the sound card can
send out 6 different signals at the same time; rather, the signal on 2
of the mono outputs and the stereo headphone output would be the same.
Also, many controllers have separate master and booth outputs with
independent volume controls, but they both play the same signal.

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

These devices allow a computer to output and input sound. Any sound card
that your operating system has a driver to use can be used with Mixxx.
All the USB sound cards in the table below are compatible with Windows,
macOS, and Linux. It is possible to use just a sound card plus a
keyboard & mouse to use Mixxx, but a separate [controller](#controllers)
makes using Mixxx easier, more intuitive, and more fun.

A sound card with at least 4 mono output channels (2 stereo pairs) is
recommended for most uses. Refer to the [Mixxx
manual](https://mixxx.org/manual/latest/chapters/setup.html) for
details. If your sound card does not have 4 output channels, it is
possible to use multiple sound cards. However, this increases latency
and there may be crackling on one sound card.

Surround sound (5.1 or 7.1) cards are not recommended. They sometimes do
signal processing in hardware or in the driver to split a stereo signal
into multiple components. It may be possible to configure them to output
a separate master and headphone stereo signals, but it is often tricky
to do so.

This table only lists a handful of available USB sound cards that are
currently in production and suitable for use with Mixxx. There are many
more options available that may be better for you depending on your
input and output needs and the sound quality you can afford. You
generally get the sound quality you pay for with sound cards.

\<sortable 2=numeric\>

| Device                                                                                                                                    | Price (USD) \[40\] | Channels out | Balanced outputs | Channels in | Microphone input with direct monitoring | Phono preamp | Notes                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------ | ---------------- | ----------- | --------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Generic USB sound cards                                                                                                                   | \< $10             | 2            | no               | 0-2         | no                                      | no           | These look similar to USB flash drives. They tend to be poor quality, sometimes even worse than onboard sound cards. [\#Splitter cables](#Splitter%20cables) are another option in this price range.                                                                                                         |
| [Behringer U-Phono UFO202](http://www.music-group.com/Categories/Behringer/Computer-Audio/Audio-Interfaces/UFO202/p/P0A12)                | $30                | 2            | no               | 2           | no                                      | yes          | Cheapest option for vinyl control, but requires using 2 of them and making [a small hardware modification](http://mixxx.org/forums/viewtopic.php?f=6&t=2438). Not to be confused with the Behringer U-Control **UCA**202 & **UCA**222, which do not have phono preamps and cannot be used for vinyl control. |
| [Behringer UMC22](https://www.music-group.com/Categories/Behringer/Computer-Audio/Audio-Interfaces/UMC22/p/P0AUX)                         | $40                | 2            | yes              | 2           | yes                                     | no           | Cheap option suitable for broadcasting with a microphone. The headphone jack cannot play a separate signal from the main output, so the onboard sound card on a computer would be required for a separate headphone output.                                                                                  |
| [Focusrite Scarlett Solo](https://us.focusrite.com/usb-audio-interfaces/scarlett-solo)                                                    | $100               | 2            | no               | 2           | yes                                     | no           | Similar inputs and outputs as the Behringer UMC22 but with better sound quality. Also available bundled with a microphone and headphones for $200.                                                                                                                                                           |
| [Native Instruments Traktor Audio 2 DJ (Mk2)](http://www.native-instruments.com/en/products/traktor/dj-audio-interfaces/traktor-audio-2/) | $100               | 4            | no               | 0           | no                                      | no           | Has the minimum recommended number of output channels, but no input channels, so it cannot be used for vinyl control or broadcasting with a microphone input.                                                                                                                                                |
| [ESI Maya 44 USB+](http://www.esi-audio.com/products/maya44usb+/)                                                                         | $140               | 4            | no               | 4           | no                                      | no           | Does not have phono preamps on the inputs, but has been reported to work for vinyl control.                                                                                                                                                                                                                  |
| [Roland Rubix24](https://www.roland.com/us/products/rubix24/)                                                                             | $200               | 4            | yes              | 2           | yes                                     | no           | Good balance of sound quality and price with independent main and headphone outputs. Has microphone inputs with an analog compressor that can be used with direct monitoring.                                                                                                                                |
| [Denon DS1](http://denondj.com/products/view/ds1)                                                                                         | $300               | 4            | no               | 4           | no                                      | yes          | Higher quality option for vinyl control. Comes with a pair of Serato timecode vinyl that are compatible with Mixxx.                                                                                                                                                                                          |
| [MOTU Ultralite AVB](http://motu.com/products/avb/ultralite-avb/)                                                                         | $650               | 10           | yes              | 10          | yes                                     | no           | High quality outputs can plug directly into main speakers, booth monitors, and headphones with independent volume controls without needing an external mixer. Also works as a WiFi controllable mixer without needing a computer.                                                                            |

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

| Device                                                                                                                      | Price (USD) \[41\] | Decks | Phono preamps | USB ports | Analog or digital mixing | Linux         |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----- | ------------- | --------- | ------------------------ | ------------- |
| [Numark M101USB](http://www.numark.com/product/m101usb)                                                                     | $100               | 2     | 2             | 1         | ?                        | likely \[42\] |
| [Allen & Heath Xone 23C](http://www.allen-heath.com/ahproducts/xone-23c/)                                                   | $400               | 2     | 2             | 1         | analog                   | likely \[43\] |
| [Native Instruments Traktor Kontrol Z2](http://www.native-instruments.com/en/products/traktor/dj-mixer/traktor-kontrol-z2/) | $600               | 2     | 2             | 1         | ?                        | likely \[44\] |
| [Allen & Heath Xone 43C](http://www.allen-heath.com/ahproducts/xone43C/)                                                    | $1000              | 4     | 4             | 1         | analog                   | likely \[45\] |
| [Pioneer DJM-750](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-750)                                                 | $1000              | 4     | 2             | 1         | digital                  | ?             |
| [Pioneer DJM-5000](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-5000)                                               | $1000              | 4     | 0             | 1         | digital                  | ?             |
| [Allen & Heath Xone DB2](http://www.allen-heath.com/ahproducts/xonedb2/)                                                    | $1500              | 4     | 4             | 1         | digital                  | no            |
| [Pioneer DJM-850](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-850)                                                 | $1500              | 4     | 2             | 1         | digital                  | ?             |
| [Rane TTM57MkII](http://dj.rane.com/products/ttm57mkii)                                                                     | $1750              | 2     | 2             | 2         | digital                  | likely \[46\] |
| [Rane MP2014](http://dj.rane.com/products/mp2014-mixer)                                                                     | $2000              | 4     | 2             | 2         | digital                  | likely \[47\] |
| [Allen & Heath Xone DB4](http://www.allen-heath.com/ahproducts/xonedb4/)                                                    | $2000              | 4     | 4             | 1         | digital                  | no            |
| [Pioneer DJM-900NXS](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-900NXS)                                           | $2000              | 4     | 2             | 1         | digital                  | ?             |
| [Rane Sixty-Two](http://dj.rane.com/products/sixty-two)                                                                     | $2000              | 2     | 2             | 2         | digital                  | no            |
| [Pioneer DJM-900NXS2](https://www.pioneerdj.com/en-us/product/mixer/djm-900nxs2/black/overview/)                            | $2200              | 4     | 4             | 2         | digital                  | ?             |
| [Rane Sixty-Four](http://dj.rane.com/products/sixty-four)                                                                   | $2200              | 4     | 4             | 2         | digital                  | no            |
| [Pioneer DJM-900SRT](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-900SRT)                                           | $2300              | 4     | 2             | 1         | digital                  | ?             |
| [Pioneer DJM-2000NXS](http://www.pioneerelectronics.com/PUSA/DJ/Mixers/DJM-2000NXS)                                         | $2500              | 4     | 2             | 1         | digital                  | likely \[48\] |
| [Rane MP2015](http://dj.rane.com/products/mp2015-mixer)                                                                     | $2900              | 4     | 4             | 2         | digital                  | likely \[49\] |

\</sortable\>

## Microphones and broadcasting

Mixxx can work with any microphone that you can plug into a sound card
that your operating system supports. To hear yourself on the microphone
without noticeable latency, a sound card that supports direct monitoring
is recommended. To preview the music you will play next in headphones
and have microphone input, a single sound card with 4 output channels is
recommended. The sound cards built into computers meet neither of these
criteria, so a dedicated sound card is recommended. Some options are
listed in the [\#USB sound cards](#USB%20sound%20cards) table above. You
do not need an external mixer, and using one is generally discouraged
because it adds unnecessary noise and distortion to your signal chain.

USB microphones are not recommended. These are devices that combine a
microphone with a USB sound card with one microphone input channel. Many
USB microphones have a headphone jack for direct monitoring the input,
but the computer cannot output to this jack, so you would only hear your
voice, but not the music from Mixxx. Again, a dedicated sound card that
supports direct monitoring is recommended.

The microphone inputs on DJ controllers, particularly cheaper DJ
controllers, is often mixed directly with the master output of the DJ
controllers' sound card in hardware, but not digitized and sent to the
computer. If this is the case, it is not possible to get the microphone
signal into Mixxx for broadcasting or recording. Some controllers do
make the microphone input available to the computer though. Check the
controllers' wiki page linked in the tables above for information about
this and search online for information about any particular controller.

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

2.  This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

3.  4 deck control available by toggling between decks 1/3 and decks 2/4

4.  DJ Control Glow and MP3 LE will be supported starting with Mixxx 2.1

5.  4 deck control available by toggling between decks 1/3 and decks 2/4

6.  This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

7.  The default Mixxx mapping has this mapped to hotcues.

8.  Mapping supports 4-deck switching

9.  Mapping supports 4-deck switching

10. Mapping supports n-deck switching

11. Prices listed on this page are the prevailing prices for unused
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

12. The Novation Dicer is priced per pair.

13. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

14. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

15. 4 deck control available by toggling between decks 1/3 and decks 2/4

16. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

17. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

18. 4 deck control available by toggling between decks 1/3 and decks 2/4

19. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

20. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

21. 4 deck control available by toggling between decks 1/3 and decks 2/4

22. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Mac OS X. There is no
    driver available for Linux or Windows.

23. 4 deck control available by toggling between decks 1/3 and decks 2/4

24. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

25. [Mac OS X driver](http://www.joemattiello.com/dm2/); [Linux MIDI
    Driver](http://www.jockusch.de/dm2/dm2-pre20080225.tgz), [Alternate
    Linux MIDI driver
    (unfinished)](http://prophet.homelinux.org/usbdm2/usbdm2.tar.bz2),
    [dm2linux on
    sf.net](http://sourceforge.net/project/showfiles.php?group_id=198453)

26. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

27. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

28. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

29. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

30. 4 deck control available by toggling between decks 1/3 and decks 2/4

31. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

32. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

33. This device is not USB MIDI class compliant. Its signals are
    translated to MIDI by special drivers on Windows and Mac OS X. There
    is no driver available for Linux.

34. 4 deck control available by toggling between decks 1/3 and decks 2/4

35. This mapping is compatible with Mixxx 2.0 and will be included with
    Mixxx when Mixxx 2.1 is released.

36. 4 deck control available by toggling between decks 1/3 and decks 2/4

37. 4 deck control available by toggling between decks 1/3 and decks 2/4

38. Prices listed on this page are the prevailing prices for unused
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

39. 4 deck control available by toggling between decks 1/3 and decks 2/4

40. Prices listed on this page are the prevailing prices for unused
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

41. Prices listed on this page are the prevailing prices for unused
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

48. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.

49. This device is USB class compliant, so it should work without any
    special driver. However, there is no information about anyone using
    it with Linux online.
