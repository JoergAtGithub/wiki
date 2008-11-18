# Hercules/Guillemot DJ Console Series Controllers

## Mixxx Community Sites

| General                       | Download                                     | Forums                                       | Bugs                                                     | Wiki                                     | IRC                                              | Developer Mailing List                                                               |
| ----------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------ |
| [mixxx.org](http://mixxx.org) | [Get Mixxx\!](http://mixxx.org/download.php) | [mixxx.org/forums](http://mixxx.org/forums/) | [Mixxx launchpad bugs](https://bugs.launchpad.net/mixxx) | [mixxx.org/wiki](http://mixxx.org/wiki/) | [\#mixxx on freenode](irc://freenode.net/#mixxx) | [Mixxx-devel mailing list](https://lists.sourceforge.net/lists/listinfo/mixxx-devel) |

## Intro

Welcome the [Mixxx](http://mixxx.org) page for
[Hercules](http://www.hercules.com/) devices, Mixxx is the world's best
free open source DJ software and the only one that runs on Windows, Mac
OSX and Linux ([download it](http://mixxx.org/download.php))... Hercules
does not directly develop or support troubleshooting of Mixxx, so please
direct questions/bugs encountered/comments/praise about Mixxx to the
[Mixxx community sites](#mixxx-community-sites) at the top of this page.

The purpose of this page is to document how controls have been mapped to
different or non-obvious functions in Mixxx, controls not listed here
should behave as you would expect (i.e. Crossfader cross fades, Play -
plays/pauses, etc). These mappings work with Hercules MIDI drivers for
Linux, Mac OSX and Windows. *Untested* mappings are based on MIDI code
documentation in the Hercules manuals and have not yet been extensively
validated by the Mixxx community. These are default mappings and can be
changed by editing the [XML mappings (click to see
how)](midi_controller_mapping_file_format), in future versions of Mixxx
(1.7.x+) we will offer a configuration screen to train/retrain/remap
this controls from within Mixxx.

Brackets indicated control position on diagrams to the Left. Controller
diagrams are copyright of Hercules/Guillemot corporation.

> > > **Linux NOTE:** To properly make use of Mixxx **via the Hercules
> > > <span class="underline">Linux</span> MIDI drivers** you will need
> > > a release of Mixxx 1.6.2 (released in Nov 2008) or higher.
> > > Previous versions of Mixxx built for Linux will work with Hercules
> > > devices via libDJConsole but can not be remapped via the [XML
> > > mappings](midi_controller_mapping_file_format).

## The Future

Mixxx is always evolving, changing and getting better... Today our MIDI
support is rough around the edges. Mixxx is powered by a handful of
unpaid part-time developers, so it may take us a while to get where we
want to go, but here are some of the things in the pipeline and in
planning...

Some of the things to look forward to in the future:

  - MIDI training UI to remap controls without [manual editing XML
    files](midi_controller_mapping_file_format) (1.7.x) \[
    [GSoC-MIDI-Tom
    branch](http://mixxx.svn.sourceforge.net/viewvc/mixxx/branches/GSoC-MIDI-Tom/)
    \]
  - Realtime Sound FX processing via the
    [LADSPA](http://en.wikipedia.org/wiki/LADSPA) plug-in architecture
    (1.7.x) \[
    [Trunk](http://mixxx.svn.sourceforge.net/viewvc/mixxx/trunk/) \]
  - Library rewrite (1.8.x) \[ [Features\_sqlite
    branch](http://mixxx.svn.sourceforge.net/viewvc/mixxx/branches/Features_sqlite/)
    \]
  - Looping support (2.x) \[ [planning on wiki](looping)
    [Features\_rryan-looping
    branch](http://mixxx.svn.sourceforge.net/viewvc/mixxx/branches/Features_rryan-looping/)
    \]

Join us if you want to help\!

  - If you can code C++, then [build mixxx](start#build_mixxx), and
    [send us patches](#mixxx-community-sites)
  - If you can't code, join the [community
    forums](#mixxx-community-sites), test Mixxx, cheer on the Mixxx dev
    team or [![Mixxx PayPal Donation
    Button](https://www.paypal.com/en_GB/i/btn/btn_donate_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=donations%40mixxx%2eorg&lc=GB&item_name=Mixxx&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHostedGuest)
    to Mixxx.

## Configuring Mixxx to use a Hercules MIDI driver

> > **Linux NOTE:** Mixxx version \>= 1.6.2 is required (1.6.1 is too
> > old), you must also have compiled and installed the Hercules dkms
> > kernel module into your Linux kernel

[[/media/hercules_midi_mapping_setup.png|]] \*\* Steps \*\*

1.  Start Mixxx, open preferences panel (Ctrl+P).
2.  Select ***Input Controllers***.
3.  Under ***Device*** find the MIDI entry for Hercules controller and
    select it, if it is not already selected -\> If you do not see a
    Hercules MIDI device then the driver is not properly loaded or the
    devices is not plugged in.
4.  Choose the ***Controller Mapping*** matching your Hercules device.

## Hercules DJ Console MK2 and Hercules MP3 Control (Tested)

> > Note: Both the MP3 and MK2 controllers are mapped the same way, but
> > have different configuration files, picking the wrong config file
> > will result in some buttons failing to perform as indicated.

[[/media/hercules_mk2_top_face.png|]]

| Hercules MP3/MK2 Controls |                       |                             |  |
| ------------------------- | --------------------- | --------------------------- |  |
| Control                   | Default Mixxx Mapping |                             |  |
|                           | 3 (3)                 | Kill High                   |  |
|                           | 2 (3)                 | Kill Mid                    |  |
|                           | 1 (3)                 | Kill Base                   |  |
|                           | FX/Cue/Loop (3)       | Reverse                     |  |
|                           | Master Tempo Left     | Select Prev Track in List   |  |
|                           | Master Tempo Right    | Select Next Track in List   |  |
|                           | Left Joy Button (4)   | Load selected to Left Deck  |  |
|                           | Right Joy Button (4)  | Load selected to Right Deck |  |
|                           | Autobeat (11)         | Sync                        |  |
|                           | Joystick (4)          | Unmapped                    |  |
|                           | Mic Functions         | Not Available in Mixxx      |  |

## Hercules RMX (Tested)

[[/media/hercules_rmx_top_face.png|]]

| Hercules RMX Controls |                       |                           |  |
| --------------------- | --------------------- | ------------------------- |  |
| Control               | Default Mixxx Mapping |                           |  |
|                       | Vol Main (25)         | Master Gain               |  |
|                       | 1 (9)                 | Flanger                   |  |
|                       | 4 (9)                 | Reverse                   |  |
|                       | Up (8)                | Select Prev Track in List |  |
|                       | Down (8)              | Select Next Track in List |  |
|                       | 2,3,5,6 (9)           | Unmapped                  |  |
|                       | Right, Left (8)       | Unmapped                  |  |
|                       | Stop (20)             | Unmapped                  |  |
|                       | Pitch Reset (14)      | Unmapped                  |  |
|                       | Beat Lock (13)        | Unmapped                  |  |
|                       | Scratch (7)           | Unmapped                  |  |
|                       | Mic Functions (1)     | Not Available in Mixxx    |  |

## Hercules DJ Control Steel (Untested)

[[/media/hercules_dj_control_steel_top_face.png|]]

| Hercules DJ Control Steel Controls |                       |                           |  |
| ---------------------------------- | --------------------- | ------------------------- |  |
| Control                            | Default Mixxx Mapping |                           |  |
|                                    | FX Wet/Dry Knobs (1)  | Unmapped                  |  |
|                                    | FX Apply Select (1)   | Unmapped                  |  |
|                                    | Bank Shift (2)        | Unmapped                  |  |
|                                    | Pitch Bend + (12)     | Temp Rate Up              |  |
|                                    | Pitch Bend - (13)     | Temp Rate Down            |  |
|                                    | Vol Main (23)         | Master Gain               |  |
|                                    | 1 (9)                 | Flanger                   |  |
|                                    | 4 (9)                 | Reverse                   |  |
|                                    | Up (8)                | Select Prev Track in List |  |
|                                    | Down (8)              | Select Next Track in List |  |
|                                    | 2,3,5,6 (9)           | Unmapped                  |  |
|                                    | 7,8,9,10,11,12 (9)    | Unmapped                  |  |
|                                    | Right, Left (8)       | Unmapped                  |  |
|                                    | Stop (19)             | Unmapped                  |  |
|                                    | Scratch (7)           | Unmapped                  |  |
|                                    | Vol\_HP (11)          | Not Available in Mixxx    |  |
