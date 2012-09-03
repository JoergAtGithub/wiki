# Troubleshooting FAQ

## Latency reduction tips

*Being able to lower the Latency in Mixxx's Sound Hardware Preferences
as much as possible makes a huge difference in its responsiveness. Here
are some tips to help you do that.*

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
  - Set [IRQ Priorities](http://subversion.ffado.org/wiki/IrqPriorities)
  - You can also try using a [real-time
    kernel](http://pkg-freebob.alioth.debian.org/lowlat.html) or a
    distribution that includes one, like
    [64Studio](http://www.64studio.com/) or [Ubuntu
    Studio](http://ubuntustudio.org/). Note that you will need to [set
    up real-time support (scroll down to "Real-time
    support")](https://help.ubuntu.com/community/UbuntuStudioPreparation)
    for audio applications in order to gain any benefit from a real-time
    kernel.
  - Wireless networking is known to cause xruns with Mixxx. If you're
    experiencing dropouts every few seconds during regular playback, try
    right-clicking the network widget in your GNOME tray, and unchecking
    the Enable Networking" box. (Yeah, we know this is lame, but we're
    not sure what we can do if the OS is fighting us. Keep your eyes
    peeled for other peripherals that might be causing xruns too.) You
    can also try disabling PCI bus mastering and/or changing the IRQ for
    the device in your BIOS and the Device Manager (Windows) or in
    /etc/modules (Linux.)

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
  - **Ensure that your hardware's ASIO Sample Rate setting is equal to
    the "Sample Rate (Hz)"** in MIXXX's Audio Output settings (under
    Preferences-\>Sound Hardware.)

### All operating systems

  - **IRQ sharing** - Make sure your sound card(s) are not sharing
    <span class="underline">I</span>nterrupt
    <span class="underline">R</span>e<span class="underline">q</span>uest
    ports with any other system devices (like network cards.) If they
    are, try to change them in your OS or BIOS or disable the other
    devices while you're DJing.
  - *Linux:* at a console, issue `cat /proc/interrupts` If the line that
    contains the kernel module for your sound card has something else
    next to it, this affects you, and you may be able to change the IRQ
    at module load time (type `man modprobe` for more information on
    this.)
  - *Windows:* Open Device Manager (Start-\>Control Panel-\>System,
    Hardware tab, Device Manager button) find your sound card,
    right-click it, choose Properties, then the Resources tab. Drop down
    to IRQs and see if anything else is sharing it. If so, this affects
    you, and you can try changing the IRQ assignment for your sound card
    in this window.
  - **Increase process priority**
  - As a last resort, run Mixxx as the root user or a user with
    administrative privileges. This allows Mixxx to increase the
    priority of its critical threads to real-time. This should greatly
    reduce latency on a busy system. **Be aware that running as
    root/admin puts your system at greater risk from malicious code.**
  - Alternately and more safely, on Linux, edit
    `/etc/security/limits.conf` and add `<your user name> soft
    rtprio 99` to allow Mixxx (and other processes you run) to increase
    their thread priority to maximum, or just run Mixxx from a console
    with `sudo mixxx`.
  - In OS X, you have three choices:

<!-- end list -->

``` 
    - ''sudo nice -n -20 /Applications/Mixxx.app/Contents/MacOS/Mixxx.app'' in console, assuming you have appropriate privileges in ''/etc/sudoers''.
    - run Mixxx like normal but then find the PID with ''ps -l'' in console, and then run ''sudo renice -20 //<PID>//'' (again, must be in ''/etc/sudoers'').
    - try [[http://homepage.mac.com/northernSW/renicer.html|Renicer]] which automatically ''renice''s the topmost application. I can't personally vouch for this. It is ~$10. -[[|wxl]]
```

## Mixxx won't load any tracks

This happens when Mixxx can't open any output sound devices. Click
Options-\>Preferences-\>Sound Hardware and ensure that you have a sound
device selected for at least one output and that the selected sample
rate is supported by the device (Mixxx will complain when you click
Apply if it isn't.)

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

## How do I delete my library file?

Make sure Mixxx is closed, then look for "mixxxdb.sqlite" (or
"mixxxtrack.xml" if using Mixxx 1.8.x or below) in:

  - Windows: `%USERPROFILE%\Local Settings\Application Data\Mixxx`
  - Linux/BSD/Unix: `~/.mixxx` 
  - Mac OS X: `~/Library/Application Support/Mixxx/`
  - If using Mixxx 1.8.x or below it is just like on Linux in `~/.mixxx`
    

If you can't find it, search your computer for "mixxxdb.sqlite" (or
"mixxxtrack.xml" if using Mixxx 1.8.x or below)

  - If on Windows, Click Start-\>Run, type `%USERPROFILE%\Local
    Settings\Application Data\Mixxx` and click OK. 
  - If you want to use "Find files/folders", make sure to open "Advanced
    Options" and mark "Search Hidden Files/Folders".
  - If on Mac OSX, press Shift-Command-G or "Go to folder..." command in
    the Finder's Go menu. Then enter `~/Library/Application
    Support/Mixxx/`.

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

## Where is the mixxx.log file?

  - Linux: \~/.mixxx/mixxx.log
  - Windows: (enter the following into the Location bar of an
    Explorer/My Computer window, or at the command prompt)
  - v1.9.0 and up: `%LOCALAPPDATA%\Mixxx` on Vista and up,
    `%USERPROFILE%\Local Settings\Application Data\Mixxx` on XP and
    below.
  - v1.8.x and below: `%PROGRAMFILES%\Mixxx` (or wherever Mixxx.exe is)
  - OSX:
  - v1.9.0 and up: in your home folder under `Library/Application
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

## Mixxxcelaneous Known Issues

  - Mobile Intel 4 Series chipset with I945/965 graphics driver
    sometimes causes segmentation fault on exit in Windows and Linux.
    This is fixed by upgrading your version of the Qt libraries on Linux
    or getting the latest Mixxx 1.7 package for Windows.

## Mixxx says I have no HID controllers attached even though I do

This happens on Linux and results from not having write permissions to
USB devices. (Mixxx will say something to this effect in the log when it
scans for HID devices.) To fix this, do the following:

1.  Open a console
2.  As root, create `/etc/udev/rules.d/15-mixxx-usb.rules` (you can
    change the number and name as appropriate): `sudo nano
    /etc/udev/rules.d/15-mixxx-usb.rules`
3.  Edit that file and add the following: `# Allow scannining USB
    devices
    SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", GROUP="users"
    
    # Allow communicating with HID devices
    ATTRS{bInterfaceClass}=="03", GROUP="users", MODE="0660"` (use
    whatever group name you prefer)

for avlinux 6.0 you should try this:

    # Allow scannining USB devices
    SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", GROUP="users"
    
    # Allow communicating with HID devices
    ATTRS{bInterfaceClass}=="03", GROUP="users", MODE="0660"
    
    # Allow scannining USB devices
    #SUBSYSTEM=="usb", ATTR{idVendor}=="1157", ATTR{idProduct}=="0310", GROUP="users"
    #
    # Allow communicating with HID devices
    #SUBSYSTEM=="usb", ATTR{idVendor}=="1157", ATTR{idProduct}=="0310", ATTRS{bInterfaceClass}=="03", GROUP="users", MODE="0660"
    #
    KERNEL=="hiddev*", NAME="usb/%k", GROUP="users"
    #

1.  Save and exit.
2.  Enter `sudo /etc/init.d/udev restart`
3.  If your user account is not already a member of `users`, enter `sudo
    usermod -a -G users $USER`
4.  Log off and back on so your user account gets the new group and
    associated permissions.
5.  Start Mixxx and you should be good to go.
