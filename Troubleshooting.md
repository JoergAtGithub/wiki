# Troubleshooting FAQ

## Latency reduction tips

*Being able to lower the Latency in Mixxx's Sound Hardware Preferences
as much as possible makes a huge difference in its responsiveness.
However, lowering it beyond what your system can handle will cause
audible glitches (pops). Here are some tips to configure your system to
handle lower latency audio:*

### Linux

#### Enable realtime scheduling

In Preferences \> Sound hardware, if there is a link to this page, Mixxx
is not running with real time priority. To enable Mixxx to run with real
time priority, you will need to set up your kernel and scheduling
permissions.

##### Kernel setup

To use real time scheduling, you will either need to boot Linux with the
"threadirqs" parameter or use a kernel with the [realtime patch
set](https://rt.wiki.kernel.org/index.php/Main_Page). To always boot
with the "threadirqs" kernel argument, add it to your grub.cfg by
editing /etc/default/grub as root, adding "threadirqs" to the line for
GRUB\_CMDLINE\_LINUX, then running `grub2-mkconfig -o
/boot/grub2/grub.cfg`. Reboot. Check that you have booted with the
"threadirqs" kernel parameter by running `grep threadirqs
/proc/cmdline`. If you booted with the "threadirqs" kernel parameter,
all the parameters you booted with will be printed. If there is no
output, you did not boot with the "threadirqs" kernel parameter.

To use a kernel with the realtime patch set, Fedora users can install
the kernel-rt package from the [Planet
CCRMA](http://ccrma.stanford.edu/planetccrma/software/) repository.
Ubuntu users can install the [kernel-rt or
kernel-lowlatency](https://help.ubuntu.com/community/UbuntuStudio/RealTimeKernel)
packages. [Crossfade](http://nongnu.org/crossfade) and [Ubuntu
Studio](http://ubuntustudio.org/) are distributions that come with a
realtime patched kernel. Note that kernels with the realtime patch set
may have some stability issues.

##### User permissions

Enabling real time scheduling in your kernel will only have an effect if
your user has permission to run Mixxx with realtime priority. Set the
maximum rtprio for your user by editing `/etc/security/limits.conf` as
root and add `<your user name> - rtprio 99` to allow Mixxx (and other
processes you run) to increase their thread priority to maximum. Reboot
for this to take effect.

#### Raise the IRQ priority of your sound card

This will not have any effect unless you have enabled realtime
scheduling in your kernel as described above. The easiest way to raise
the IRQ priority of your sound card is by installing
[rtirq](http://www.rncbc.org/archive/#rtirq) and setting it to run on
boot. To set rtirq to run on boot on distributions using systemd (which
is most nowadays), run 'systemctl enable rtirq' as root. To set IRQ
priorities manually, see [this
guide](http://subversion.ffado.org/wiki/IrqPriorities).

#### Disable CPU frequency scaling or use the 'performance' mode

CPU Frequency Scaling is a main cause of Mixxx skipping on laptops. (Do
`ps aux | grep cpufreq` and kill any processes you find.) -- Actually it
is better to remove the kernel modules, do \`lsmod | grep freq\` and
then remove each of the modules using rmmod, note that if you are using
a notebook it will burn through battery **much** quicker when doing
this.

#### Disable chipcard2

This utility polls for smart cards every few seconds, and when it does,
it can cause Mixxx's audio to skip, even with the latency set really
high.

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
    confirmed but is worth testing since these programs are known to
    slow systems down in general. ***Do not attempt this if your system
    is connected to a network or the internet or will be using media
    from unknown/untrusted sources*** otherwise you put your system at
    risk of infection.
  - **Raise the IRQ (interrupt request) priority of your sound card.**
    Open Device Manager (Start-\>Control Panel-\>System, Hardware tab,
    Device Manager button) find your sound card, right-click it, choose
    Properties, then the Resources tab. Drop down to IRQs and see if
    anything else is sharing it. If so, this affects you, and you can
    try changing the IRQ assignment for your sound card in this window.
  - **Disable nVidia's "PowerMizer."** nVidia's laptop drivers have a
    feature called "PowerMizer" that has been reported to cause all
    kinds of problems for audio and overall latency. It can be disabled
    with a registry tweak:
    <http://forum.notebookreview.com/showthread.php?t=261929>
  - **Deactivate the "Microsoft ACPI-Compliant Control Method Battery"**
    in the Device Manager (under Control Panel-\>System-\>Hardware.)
  - **Ensure that your hardware's ASIO Sample Rate setting is equal to
    the "Sample Rate (Hz)"** in MIXXX's Audio Output settings (under
    Preferences-\>Sound Hardware.)

### Mac OS X

Raise the priority of Mixxx. While Mixxx is running, open Terminal and
run `` sudo renice -20 `pidof mixxx` `` (your user must be in
`/etc/sudoers`).

## Controller troubleshooting

To use a MIDI or HID controllers with Mixxx, enable the device and load
a mapping. Go to Options \> Preferences in Mixxx and look for your
controller under the "Controllers" label on the left. Check the
"Enabled" box, select a mapping from the drop down menu and press "Ok".
If Mixxx did not come with a mapping for your controller, [search the
forum](http://mixxx.org/forums/search.php?fid[]=7) to see if anyone has
made one. If not, you can [map it
yourself](start#controller%20mapping%20documentation).

If your controller does not show up under "Controllers" on the left side
of Mixxx's preferences window, Mixxx did not detect your controller.
Check that your controller is plugged into your computer. If your
controller has its own power supply, check that the power supply is
plugged in. If your controller has a power switch, make sure it is on.
Note that Mixxx will only detect controllers on start up, so if you
plugged in your controller after starting Mixxx, restart Mixxx and go
back to the Preferences window.

If you are sure your controller is connected but it still does not show
up in Mixxx, read the appropriate section below. If you do not know
whether your controller is a MIDI controller or HID controller, search
for it on the [DJ Hardware Guide](hardware%20compatibility). If it is
not listed there, it is most likely a MIDI device.

### MIDI controllers on GNU/Linux

Make sure that the snd-seq-midi kernel module has been loaded. Open a
console and run `lsmod | grep snd_seq_midi` to check if the module has
been loaded. If it has not, run `modprobe snd-seq-midi` as root and
restart Mixxx.

This happens on GNU/Linux where devices like the American Audio VMS4.1
only show up as an HID device, not a MIDI device. Also, there is [a
bug](https://bugs.archlinux.org/task/44286) in Arch Linux that requires
loading the snd-seq-midi module manually.

### HID controllers on GNU/Linux

Mixxx may not have permission to use your HID device. (Mixxx will say
something to this effect in the log when it scans for HID devices.) To
fix this, do the following:

1.  Open a console
2.  As root, create `/etc/udev/rules.d/15-mixxx-usb.rules` \[1\] (you
    can change the number and name as appropriate): `sudo nano
    /etc/udev/rules.d/15-mixxx-usb.rules`
3.  Edit that file and add the following: `# Allow scanning of USB
    devices
    SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", GROUP="users"
    
    # Allow communicating with HID devices
    ATTRS{bInterfaceClass}=="03", GROUP="users", MODE="0660"` (use
    whatever group name you prefer.) Some distributions (like AV Linux
    6.0) may also require adding this line as well: `KERNEL=="hiddev*",
    NAME="usb/%k", GROUP="users"
    `
4.  Save and exit.
5.  Enter `sudo /etc/init.d/udev restart`
6.  If your user account is not already a member of `users` (or whatever
    group name you used in the `rules` file above,) enter `sudo usermod
    -a -G users $USER`
7.  Log off and back on so your user account gets the new group and
    associated permissions.
8.  Start Mixxx and your HID devices should now be listed under
    Controllers in the Preferences window.

## Errors on starting Mixxx

**`Could not open xml file: "/usr/local/share/mixxx/schema.xml"`**
happens to people that have built Mixxx from source but didn't do the
install step. You can either do that (with `sudo scons install`) or
explicitly tell Mixxx where to look for resources with the
`-``-resourcePath` command line parameter, like so: `./mixxx
-``-resourcePath res/`

## What do I enter for the user name in Live Broadcasting?

  - For an Icecast2 server, the user name is **source** by default.
  - For a Shoutcast server, the user name is **admin** by default.

## The BPM detection is wrong

Mixxx 1.11.0 has a brand new BPM detection engine and has proven to be
quite accurate in testing. If you're on a version older than that, read
on.

We've updated the library Mixxx uses for BPM detection in 1.7 which
helps. There's also a bug with BPM schemes that's difficult to fix in
the short term, so here is a workaround in the meantime:

``` 
 - Open Options->Preferences->BPM Detection
 - Create or edit a BPM scheme with the range you want & click OK.
 - Highlight that scheme in the list.
 - Click the "Default" button. (It's only by doing this that the selected BPM scheme is activated.)
```

After doing that, you may need to explicitly tell Mixxx to re-analyze
your files, or you can just delete your library file [(see
below)](#how-do-i-delete-my-library-file) and it will do auto-detection
the next time you load each song. If you see values half what they
should be, go into Preferences-\>BPM Detection, and check Allow BPM
above the range. Click OK, then have Mixxx try to detect it again.
(Though you shouldn't need to use that checkbox if you set the scheme
correctly.)

## The library doesn't see new songs

First try clicking Library-\>Rescan library. Then re-sort it (by artist
name or whatever) by clicking on the column heading. If that doesn't
help, [delete your library file](#how-do-i-delete-my-library-file) and
restart Mixxx.

## No or too few sound cards appear in the preferences dialog

*This also applies for the **"Audio device could not be opened"**
error.*

When no sound cards/devices appear in the sound preferences dialog or
you get the "Audio device could not be opened" error, it usually means
that another application is using your sound card(s). This problem only
appears on Linux. To fix it, make sure no other applications are using
your sound card. If your system has PulseAudio installed (Ubuntu,) you
will want to run Mixxx from a console with the following command:
`pasuspender mixxx` This suspends the PulseAudio daemon and lets it
release the sound card so Mixxx can take exclusive control. Once Mixxx
ends, PulseAudio takes the card over again.

If that doesn't help, the usual culprits are Firefox and the esound
daemon. Closing Firefox normally will take care of the former, and
running "killall esd" in a terminal will take care of the latter. If
it's still not working, running "sudo fuser -v /dev/dsp\*" and "sudo
fuser -v /dev/snd/\*" will show you the list of applications currently
using your soundcards. If you're using ALSA, you can also choose the
"default" sound card option which will mix Mixxx's output with
everything else.

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
you have the latest [DirectX](http://support.microsoft.com/kb/179113)
installed.

## Mixxx freezes, crashes, or otherwise misbehaves and I have an nVidia graphics card

Before you try anything else, please update or reinstall your nVidia
graphics driver. (This applies to all OSes.) I don't care if it's the
same exact version, apparently it is fickle and needs to be
rebuilt/reinstalled any time things change in the OS. Try this first
before going any further. 90% of the time it will fix your problem. You
might also try getting the latest driver from nVidia's web site instead
of your PC/card manufacturer since they may be newer.

## Where is the mixxx.log file?

Mixxx logs debugging information, [MIDI/HID/etc.
messages](command_line_options) it receives and script functions it
loads in the `mixxx.log` plain text file.

  - **Linux:** \~/.mixxx/mixxx.log
  - **Windows:** (enter the following into the Location bar of an
    Explorer/My Computer window, or at the command prompt)
  - Mixxx v1.9.0 and up: `%LOCALAPPDATA%\Mixxx` on Vista and up,
    `%USERPROFILE%\Local Settings\Application Data\Mixxx` on XP and
    below.
  - Mixxx v1.8.x and below: `%PROGRAMFILES%\Mixxx` (or wherever
    Mixxx.exe is)
  - Note: The file may not show up as `mixxx.log` unless you've
    unchecked `Hide extensions for known file types` in the Windows
    Explorer folder options. Until then it is just `mixxx`, the only
    text file in that location. By default in Windows 7 and up, known
    file types are set to hide. See [How to show or hide file name
    extensions in Windows
    Explorer](http://support.microsoft.com/kb/865219)
  - **Mac OS X:**
  - Mixxx v1.9.0 and up: in your home folder under `Library/Application
    Support/Mixxx` (so e.g. Users/\<username\>/Library/Application
    Support/Mixxx)
  - Note: Apple made the user library folder hidden by default with OSX
    10.7 ff., use one of the following methods to open the Mixxx folder.

<!-- end list -->

``` 
    * __Method A__:
    * In the Finder, choose Go > Go To Folder.
    * In the Go To Folder dialog, type ''~Library/Application Support/Mixxx''
    * Click Go.
    * __Method B__:
    * Hold down the Alt (Option) key when using the Go menu
    * The user library folder is listed below the current users home directory
    * Navigate to ''Application Support/Mixxx''
```

## I'm using two or more separate sound cards and one/some of them (usually assigned to headphones) are crackling

This is a known artifact of using multiple separate audio interfaces.
Each one has its own clock crystal and no two are precisely the same
frequency even if the devices are the same model and from the same
production run. Mixxx before 1.12 synchronized its audio generation to
the clock crystal of whichever device is selected as the master output
(deck 1 output if no master is selected) so that the crowd won't hear
the artifacts. As a result, secondary devices either fall behind or run
ahead of the primary one, causing them to play silence until Mixxx
generates the next audio buffer exactly in time for the primary device.
Playing bits of audio interspersed with bits of silence sounds like
crackling.

Mixxx 1.12 can compensate for this issue. If you are using two sound
cards, [try Mixxx 1.12
beta](http://mixxx.org/forums/viewtopic.php?f=1&t=7131).

If you use one sound card with at least 4 channels (2 stereo pairs), you
will not have this issue.

1.  or /lib/udev/rules.d/15-mixxx-usb.rules in Ubuntu 12.04
