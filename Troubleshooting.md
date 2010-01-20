# Troubleshooting FAQ

## Latency reduction tips

*Being able to lower the Latency slider in Mixxx's Sound Hardware
Preferences as much as possible makes a huge difference in its
responsiveness. Here are some tips to help you do that.*

### Linux

  - **Disable CPU Frequency Scaling or use the 'Performance' mode.** CPU
    Frequency Scaling is a main cause of Mixxx skipping on laptops. (Do
    `ps aux | grep cpufreq` and kill any processes you find.) --
    Actually it is better to remove the kernel modules, do \`lsmod |
    grep freq\` and then remove each of the modules using rmmod, note
    that if you are using a notebook it will burn through battery
    **much** quicker when doing this. 
  - **Disable chipcard2.** This utility polls for smart cards every few
    seconds, and when it does, it can cause Mixxx's audio to skip, even
    with the latency set really high.
  - If you're using ALSA, **try setting your Master output hardware to
    just "default"** instead of specific hardware. (This made a huge
    difference on a test system with integrated Intel soundcard.) The
    drawback to this is that system sounds (KDE beeps and such) will now
    be mixed in and will come out the main output.
  - As a last resort, you can try using a [real-time
    kernel](http://pkg-freebob.alioth.debian.org/lowlat.html) or a
    distribution that includes one, like
    [64Studio](http://www.64studio.com/) or [Ubuntu
    Studio](http://ubuntustudio.org/).

### Windows

  - **Use the ASIO sound API in Preferences** This requires that you
    have ASIO drivers installed for your sound hardware. If not, search
    for them at the web sites of your sound card manufacturer and/or the
    chipset manufacturer (for integrated cards.) If they don't offer
    ASIO drivers, try using [ASIO4ALL](http://www.asio4all.com/).
  - **Disable any anti-spyware "realtime" scanning.** It's been
    discovered doing this for Ad-Aware makes a huge difference in
    latency.
  - **Disable anti-virus on-access scanning.** This hasn't been
    confirmed but is worth a try since these programs are known to slow
    systems down in general. ***This is only recommended if your system
    is not connected to a network or the internet*** otherwise you put
    your system at risk of infection.
  - **Disable nVidia's "PowerMizer."** nVidia's laptop drivers have a
    feature called "PowerMizer" that has been reported to cause all
    kinds of problems for audio and overall latency. It can be disabled
    with a registry tweak:
    <http://forum.notebookreview.com/showthread.php?t=261929>
  - **Deactivate the "Microsoft ACPI-Compliant Control Method Battery"**
    in the Device Manager (under Control Panel-\>System-\>Hardware.)

### All operating systems

Run Mixxx as the root user or a user with administrative privileges.
This allows Mixxx to increase the priority of its critical threads to
real-time. This should greatly reduce latency on a busy system.

  - Linux/OSX: edit limits.conf to allow Mixxx to increase its thread
    priority, or just run it with `sudo mixxx`

## The BPM detection is wrong

We've updated the library Mixxx uses for BPM detection in 1.7.0 so you
may need to explicitly tell it to recheck your files or just delete your
library file [(see below)](#how-do-i-delete-my-library-file) and it will
try to do auto-detection the next time you load each song. If you see
values half what they should be, go into Preferences-\>BPM Detection,
and check Allow BPM above the range. Click OK, then have Mixxx try to
detect it again.

## The library doesn't see new songs

First try clicking Library-\>Rescan library. Then re-sort it (by artist
name or whatever) by clicking on the column heading. If that doesn't
help, [delete your library file](#how-do-i-delete-my-library-file) and
restart Mixxx.

## How do I delete my library file?

Make sure Mixxx is closed, then look for "mixxxtrack.xml" in:

  - Windows: `$USERPROFILE$\Local Settings\Application Data\Mixxx`
  - Linux/Mac OS X/BSD/Unix: `~/.mixxx`

If you can't find it, search your computer for "mixxxtrack.xml"

  - If on Windows, Click Start-\>Run, type `$USERPROFILE$\Local
    Settings\Application Data\Mixxx` and click OK. (If you want to use
    "Find files/folders," make sure to open "Advanced Options" and mark
    "Search Hidden Files/Folders".)
  - If on Mac OSX, press Shift-Command-G or "Go to folder..." command in
    the Finder's Go menu. Then enter `~/.mixxx/`

## No or too few sound cards appear in the preferences dialog

When no sound cards/devices appear in the sound preferences dialog, it
usually means that another application is using your sound card(s). This
problem only appears on Linux. To fix it, make sure no other
applications are using your sound card. The usual culprits are Firefox
and the esound daemon. Closing Firefox normally will take care of the
former, and running "killall esd" in a terminal will take care of the
latter. If it's still not working, running "sudo fuser -v /dev/dsp\*"
and "sudo fuser -v /dev/snd/\*" will show you the list of applications
currently using your soundcards. If you're using ALSA, you can also
choose the "default" sound card option which will mix Mixxx's output
with everything else.

You can also go into your sound manager preferences and change the
auto-suspend feature to do so after just a second or so. (In KDE Control
Center, go to Sound & Multimedia, Sound System, then at the bottom of
the pane, change "Auto-suspend if idle".) This will cause the desktop to
drop exclusive control of the card sooner so Mixxx can see it on
startup.

## Mixxx behaves weird with Beryl/Compiz/Compiz Fusion

Mixxx 1.5 doesn't play nicely with Beryl/Compiz, as reported by several
users. This is due to some funky OpenGL code inside QT3. Fortunately,
Mixxx 1.6.0 no longer uses QT3 and reportedly works very well with
Beryl/Compiz.

## I'm using Compiz and Mixxx, and sometimes the waveform view gets corrupted and slows my CPU to a halt

This is a known bug with Qt and Compiz -- the only solution at this time
is to disable Compiz when using Mixxx. In many cases, however, the two
are able to work fine together. It seems this might be specific to
certain graphics hardware.

## Mixxx's waveforms eat my screen in Ubuntu

See "Mixxx behaves weird with Beryl/Compiz/Compiz Fusion" above. Thought
there is some (unknown to us) extra problem with how Ubuntu uses compiz,
appearently. The workaround is to go
System-\>Preferences-\>Appearence-\>Visual Effects and set them to
"none". After you do this Mixxx should behave properly (tell us if it
doesn't\!).

## I have a decently fast system & video card. Why does Mixxx seem to crawl or pin the CPU?

We've seen this a few times and it has always been a video driver
problem. Make sure you have the latest drivers for your card. (You may
need to get them from the chipset maker (nVidia, AMD/ATI) rather than
the system board or computer manufacturer, since the manufacturer
drivers aren't always the latest.) Also, if you're on Windows, make sure
you have the latest [DirectX](http://www.microsoft.com/directx)
installed.

## Mixxx freezes, crashes, or otherwise misbehaves and I have an nVidia graphics card

Before you try anything else, please update or reinstall your nVidia
graphics driver. (This applies to all OSes.) I don't care if it's the
same exact version, apparently it is fickle and needs to be
rebuilt/reinstalled any time things change in the OS. Try this first
before going any further. 90% of the time it will fix your problem. You
might also try getting the latest driver from nVidia's web site instead
of your PC/card manufacturer since they may be newer.

## Mixxxcelaneous Known Issues

  - Mobile Intel 4 Series chipset with I945/965 graphics driver
    sometimes causes segmentation fault on exit in Windows and Linux.
    This is fixed by upgrading your version of the Qt libraries on Linux
    or getting the latest Mixxx 1.7 package for Windows.
