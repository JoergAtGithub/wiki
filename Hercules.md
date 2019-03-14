# Hercules/Guillemot DJ Console Series Controllers

## Mixxx Community Sites

| General                       | Download                                     | Forums                                       | Bugs                                                     | Wiki                                     | IRC                                              | Developer Mailing List                                                               |
| ----------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------ |
| [mixxx.org](http://mixxx.org) | [Get Mixxx\!](http://mixxx.org/download.php) | [mixxx.org/forums](http://mixxx.org/forums/) | [Mixxx launchpad bugs](https://bugs.launchpad.net/mixxx) | [mixxx.org/wiki](http://mixxx.org/wiki/) | [\#mixxx on freenode](irc://freenode.net/#mixxx) | [Mixxx-devel mailing list](https://lists.sourceforge.net/lists/listinfo/mixxx-devel) |

## Intro

Welcome the [Mixxx](http://mixxx.org) page for
[Hercules](http://www.hercules.com/) devices, Mixxx is the world's best
free open source DJ software and the only one that runs on Windows, Mac
OSX and Linux (**[download Mixxx](http://mixxx.org/download.php)**)...
Hercules does not directly develop or support troubleshooting of Mixxx,
so please direct questions/bugs encountered/comments/praise about Mixxx
to the Mixxx community sites at the top of this page.

Join us if you want to help\!

  - If you can code C++, then [build mixxx](start#build_mixxx), and
    [send us patches](start#mixxx_community_sites)
  - If you can't code, join the [community
    forums](start#mixxx_community_sites), test Mixxx, help [translating
    it](internationalization) or cheer on the Mixxx dev team.

### What this Page Covers

The purpose of this document is to be a front page for information on
how to configure Mixxx to use your Hercules controllers.

On each of the different subpages, you will find how controls have been
mapped to different or non-obvious functions in Mixxx, controls not
listed there should behave as you would expect (i.e. Crossfader cross
fades, Play - plays/pauses, etc). Most of the mappings should work for
Windows and OSX, and most of them should also work in Linux (depending
if you need HID or MIDI support). These are default mappings and can be
changed by editing the [XML mappings (click to see
how)](midi_controller_mapping_file_format).

Bracketed numbers indicate a control's position on the control diagrams.
Controller diagrams are copyright of Hercules/Guillemot corporation.

## Hardware installation / Driver support

Users of Hercules products on Windows and OSX have had functional
drivers available from Hercules Website for a long time, and can use the
mappings already shipped with the current versions of Mixxx.

Under Linux, there are three options, depending on the controller that
you use: Kernel module, user-mode driver or HID mapping.

On Feb 16, 2009 - Hercules released [GPL Linux MIDI
drivers](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1)
for their Hercules series of DJ midi controller devices. In response to
this wonderful development, the Mixxx team released an updated build of
Mixxx for Linux - 1.6.1+Herc. <span class="underline">Thanks go out to
Hercules for supporting their Linux users\!</span>

Later on, the development halted and newer Linux versions broke the
support. From then on, other community member have been keeping it in
working condition. Check out more information in the [Hercules Linux
kernel module](hercules_linux_kernel_module) page.

Aside of the kernel driver, there is an [user-mode
driver](hercules_linux_usermode_driver) which supports a different set
of controllers

Since of Mixxx 1.11 some of the Hercules devices including the Dj
Console Mk2 and Mk1 can be used as HID devices under Linux without the
need for the special Hercules driver.

In order to use a HID device in Linux you must have read and write
permission to the hid devices see details at this page:
<http://www.mixxx.org/wiki/doku.php/troubleshooting>

If you want more information, you can read on these threads in the
forum:

<http://www.mixxx.org/forums/viewtopic.php?f=7&t=3712&sid=d6b392ca77e54fd7b21c468d0e77b3e7>

<http://www.mixxx.org/forums/viewtopic.php?f=7&t=4081>

## Configuring Mixxx to use a Hercules controller

[[/media/hercules_midi_mapping_setup.png|hercules\_midi\_mapping\_setup.png]]

\*\* Steps \*\*

1.  Start Mixxx, open preferences panel (Ctrl+P).
2.  Select ***Input Controllers***.
3.  Under ***Device*** find the MIDI entry for Hercules controller and
    select it, if it is not already selected -\> If you do not see a
    Hercules MIDI device then the driver is not properly loaded or the
    devices is not plugged in.
4.  Choose the ***Controller Mapping*** matching your Hercules device.

## Hercules DJ Console MK2 and Hercules MP3 Control

> > **Note:** Both the MP3 and MK2 controllers are mapped the same way,
> > but have different configuration files, picking the wrong config
> > file will result in some buttons failing to perform as indicated.

[[/media/hercules_mk2_top_face.png|]]

| Hercules MP3/MK2 Controls |                       |                             |  |
| ------------------------- | --------------------- | --------------------------- |  |
| Control                   | Default Mixxx Mapping |                             |  |
|                           | 3 (3)                 | Kill High                   |  |
|                           | 2 (3)                 | Kill Mid                    |  |
|                           | 1 (3)                 | Kill Low                    |  |
|                           | FX/Cue/Loop (3)       | Reverse                     |  |
|                           | Master Tempo Left     | Select Prev Track in List   |  |
|                           | Master Tempo Right    | Select Next Track in List   |  |
|                           | Left Joy Button (4)   | Load selected to Left Deck  |  |
|                           | Right Joy Button (4)  | Load selected to Right Deck |  |
|                           | Autobeat (11)         | Sync                        |  |
|                           | Joystick (4)          | Unmapped                    |  |
|                           | Mic Functions         | Not Available in Mixxx      |  |

  
  

| Hercules MK2 Controls - Mixxx 1.7 Additions |                               |                                                                                     |  |
| ------------------------------------------- | ----------------------------- | ----------------------------------------------------------------------------------- |  |
| Control                                     | Default Mixxx Mapping         |                                                                                     |  |
|                                             | FX/Cue/Loop (3)               | MIDI Script: Select mode - EQ Kill/FX/Cue/Loop                                      |  |
|                                             | FX/Cue/Loop LEDs (5)          | MIDI Script: Indicates current mode - None lit (the default) indicates EQ Kill mode |  |
|                                             | \[EQ Kill mode\] 3/2/1 (3)    | MIDI Script: Kill high/mid/low                                                      |  |
|                                             | \[FX mode\] 3/2/1 (3)         | MIDI Script: Toggle flanger on/off                                                  |  |
|                                             | \[FX mode\] 1 (3) + Pitch (2) | MIDI Script: Adjust flanger Depth                                                   |  |
|                                             | \[FX mode\] 2 (3) + Pitch (2) | MIDI Script: Adjust flanger Delay                                                   |  |
|                                             | \[FX mode\] 3 (3) + Pitch (2) | MIDI Script: Adjust flanger LFO                                                     |  |

> > **Note for the MK2:** Although selectable, cue and loop modes are
> > currently unsupported pending the functionality being available in
> > Mixxx

## Hercules Dj Console Mk1

The Hercules Dj Console Mk1 does not work with the Hercules driver, but
can be used as a hid device in mixxx 1.11 and up. remember that you need
permission to the HID devices:
<http://www.mixxx.org/wiki/doku.php/troubleshooting>

The Dj Console Mk1 apears in the mixxx preferences as 3 separate
devices, the first one is the controler, the second one is the joystick
mouse(which is unuasble) and the third apears to do nothing.

enable the seccond device (the unusable joystick mouse) but do not load
a mapping, this will stop it from interfering with your mouse pointer.

the pads on the Hercules Dj Console Mk1 lose responsiveness over time
but can trivialy be cleaned to restore your controler to like new
condition:
<http://djconsole.blogspot.it/2007/11/1-how-can-i-repair-my-dj-console-mk1-to.html>

## Hercules Dj Console MK4

There isn't currently a specific page for the MK4.

In order to use it under Linux, you will need the Linux [user-mode
driver](hercules_linux_usermode_driver).

## Hercules DJ Console RMX

Moved -\> [Hercules DJ Console RMX](Hercules%20DJ%20Console%20RMX)

## Hercules DJ Console RMX 2

Find it here -\> [Hercules DJ Console RMX 2](hercules_dj_console_rmx_2)

## Hercules DJ Console 4-Mx

Find it here -\>[Hercules DJ Console 4-Mx](hercules_dj_console_4-mx)

## Hercules DJ Control Steel

Moved -\> [Hercules DJ Control Steel](Hercules%20DJ%20Control%20Steel)

## Hercules DJ Control MP3 e2 / MP3 LE / Glow

Moved -\> [Hercules DJ Control MP3 e2](hercules_dj_control_mp3_e2)

## Hercules DJ Control Air

Find it here -\> [Hercules DJ Control Air](hercules_dj_control_air)

## Hercules DJ Control Instinct

Find it here -\> [Hercules DJ Control
Instinct](hercules_dj_control_instinct)

## Hercules DJ Control Compact

Find it here -\> [Hercules DJ Control
Compact](hercules_djcontrol_compact)

## Hercules P32 DJ

Find it here -\> [Hercules P32 DJ](hercules_p32_dj)

## Hercules DJControl Starlight

Find it here -\> [DJControl Starlight](hercules_dj_control_starlight)

## Additional information

[More information about the DJ console series](hercules_pc_dj_console)
