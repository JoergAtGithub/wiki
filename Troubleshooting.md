***If you were directed here from the Sound Hardware preferences in
Mixxx, see [Adjusting Audio Latency](Adjusting%20Audio%20Latency).***

# Troubleshooting

If you've got a question that's not answered here, please post in the
[forums](http://www.mixxx.org/forums). Please be sure you are using the
latest version of Mixxx before you ask for help. The latest version is
available on [the download page](http://mixxx.org/download).

## Audio is crackling

Your audio latency may be set lower than your system can handle. See the [Adjusting Audio Latency](Adjusting%20Audio%20Latency) page for tips on adjusting your latency.

Updating to Windows 10 20H2 has made this worse for some users. Raising the audio buffer size or downgrading to an earlier version of Windows may work around the issue.

## Broadcasting or recording signal is silent

Check if you have anything configured for the Record/Broadcast input in
the Sound Hardware section of the Preferences. When this input is
configured, Mixxx will broadcast and record the signal from it instead
of the output of Mixxx. This is for recording and broadcasting from an
external hardware mixer or an audio interface with a loopback input. If
you are not using either of those, do not configure the Record/Broadcast
input. You probably want to use a Microphone input instead. Refer to the
[Using
Microphones](https://mixxx.org/manual/latest/en/chapters/microphones.html)
section of the manual for more information.

## Graphical user interface (GUI) is too big or too small

As of Mixxx 2.2, Mixxx uses Qt's automatic scaling for high pixel
density screens. Unfortunately, this does not always work well.
Sometimes it uses scaling to make the GUI too big on screens that do not
need scaling, or if your screen does require scaling you may prefer a
different size than the automatically determined default.  
You can disable automatic scaling with `QT_AUTO_SCREEN_SCALE_FACTOR=0`.  
You can also apply a specific scale factor (for example 1.5 = 150%):  
`QT_SCALE_FACTOR=1.5` or `QT_SCREEN_SCALE_FACTORS=1.5` while the latter overwrites `QT_SCALE_FACTOR`.  
For supported operating systems the commands to apply scaling options vary:

### Linux

Open a shell console and type:

    export QT_AUTO_SCREEN_SCALE_FACTOR=0

before running Mixxx from that shell. Alternatively, you can manually
set a scale factor by running

    export QT_SCREEN_SCALE_FACTORS=your-scale-factor

To avoid needing to run these commands every time you run Mixxx, you can
add them to `/etc/profile` or `~/.bashrc` (assuming you are using Bash as
your shell), log out, and log back in.

### Windows

Open a command prompt ( cmd ) and type:

    set QT_AUTO_SCREEN_SCALE_FACTOR=0

You can also manually set a scale factor by running

    set QT_SCREEN_SCALE_FACTORS=your-scale-factor

Then type the full path to your Mixxx.exe file, or cd to the directory
where it is and run it. Usually `C:\\Program Files\\Mixxx\\Mixxx.exe`

To avoid needing to run these commands every time you run Mixxx, you can
create a batch file (which is a text file with the extensions .bat or
.cmd). It should contain the commands you need, each on a separate line.
Then doubleclick this file instead of Mixxx shortcut
to launch it.

Refer to [Qt's
documentation](http://doc.qt.io/qt-5/highdpi.html#high-dpi-support-in-qt)
for details.

### macOS

Mixxx 2.2 on macOS 11 may need to be run in Low Resolution Mode. This is not an issue with Mixxx 2.3 beta. To run Mixxx in Low Resolution Mode, right click on the Mixxx application in Finder, select Get Info, and check "Open in Low Resolution".

## Other programs do not make sound while Mixxx is running

On GNU/Linux, running Mixxx from a GUI menu or from the launcher icon
automatically suspends PulseAudio while Mixxx is running so Mixxx can
use your sound card with ALSA directly. To keep other programs playing
sound, either they all need to use JACK, or you can try using the
"pulse" virtual ALSA device with Mixxx when running Mixxx on the command
line without pasuspender. Refer to the Mixxx manual for more information
about [sound
APIs](https://mixxx.org/manual/latest/en/chapters/preferences.html#sound-api).
If you use JACK and do not want Mixxx to pause PulseAudio, you can edit
/usr/share/applications/mixxx.desktop to change the line:

`Exec=sh -c "pasuspender -- mixxx || mixxx"`

to

`Exec=mixxx`

On Windows, the recommended ASIO sound API typically requires that only
one program uses a sound card at a time. Refer to the Mixxx manual for
more information about [sound
APIs](https://mixxx.org/manual/latest/en/chapters/preferences.html#sound-api).

## I can't select my sound card in the Sound Hardware preferences

Check that your sound card is plugged in. If it has its own power
supply, make sure that is plugged in too. If it has a power switch,
check that it is switched on.

Mixxx only detects sound cards on startup. If you plugged your sound
card in after starting Mixxx, restart Mixxx and look again under Sound
Hardware in Options \> Preferences.

### Windows

On Windows, you need to have a driver for each sound sound card you are
trying to use with the sound API you have configured. Generally,
consumer grade sound cards like those built into computer motherboards
and external monitors do not have ASIO drivers. Check the sound card
manufacturer's website for an ASIO driver to download and install. If
there is no ASIO driver for your sound card, it might be possible to use
[ASIO4ALL](http://asio4all.com/), but ASIO4ALL is a wrapper around
WDM-KS, so it may be better to use WDM-KS directly. ASIO4ALL can be
helpful for using a sound card that has an ASIO driver together with
another sound card that does not have an ASIO driver. Refer to the
[manual](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api)
for more information about different sound APIs.

If you are running Mixxx on Windows 10, try following [these
suggestions](http://wiki.audacityteam.org/wiki/Windows_10_OS#Sound_Device_driver_requirements_and_problems)
from Audacity. Mixxx and Audacity both use the PortAudio library to
access sound cards on multiple OSs, so those suggestions apply to both
programs.

If you are considering what sound card to get for use with Mixxx, read
the [DJ Hardware Guide](Hardware%20Compatibility).

### GNU/Linux

If you are starting Mixxx from a command line on GNU/Linux, you probably
need to suspend or disable PulseAudio. On most GNU/Linux distributions
today, the PulseAudio sound server is automatically started upon logging
in. PulseAudio is convenient for most desktop audio use, but it is not
good for audio use that requires low latency like Mixxx. The PulseAudio
daemon occupies the ALSA device while it is running. To temporarily
disable PulseAudio while Mixxx is running, start it with `pasuspender
mixxx`. The .desktop launcher icon for Mixxx does this automatically. To
run Mixxx with [command line options](command%20line%20options), such as
`--mididebug`, put `--` between `pasuspender` and the rest of the
command. For example, run `pasuspender -- mixxx --mididebug`

## Bluetooth audio is delayed

Bluetooth audio always has a high latency and is not recommended for
DJing. Bluetooth audio also uses lossy compression which reduces the
audio quality. Use wired connections instead.

## What should I do to get Mixxx to run the best it can on my computer?

First, try each option for waveform renderer in Preferences \> Waveforms
\> Summary type and Overview type. Different options will work better on
different combinations of video card, video driver, and operating
system. Lower the framerate to the lowest it needs to be before you
notice the waveforms flicker. Also see [Adjusting Audio
Latency](Adjusting%20Audio%20Latency).

## How can I get Mixxx to run well on an old or slow computer?

In Preferences \> Sound Hardware, select "Soundtouch (faster)" for
Keylock/Pitch-Bending Engine. Be careful not to make big changes in
tempo to a track with keylock on because it will not sound good with
Soundtouch. See also [\#What should I do to get Mixxx to run the best it
can on my
computer?](#What%20should%20I%20do%20to%20get%20Mixxx%20to%20run%20the%20best%20it%20can%20on%20my%20computer?)

## Master signal is silent or too low

In Preferences \> Equalizers, check if the master EQ is enabled. Disable
or reset to defaults to test whether this is the cause.

In Preferences \> Normalization, check if both target Loudness and
Initial Boost are at reasonable values. If in doubt, reset the page to
default values.

In the skin, check if microphone talkover ducking is enabled (set to
Auto or Manual). Even with no microphone configured this setting could
affect Master volume to the extent that Master is silent if the Ducking
knob is turned all the way to the left. In case you have such a knob on
your controller, check that as well, as its position might be read the
next time you start Mixxx.

## My controller does not work

To use a MIDI or HID controller with Mixxx, enable the device and load a
mapping. Go to Options \> Preferences in Mixxx and look for your
controller under the "Controllers" label on the left. Check the
"Enabled" box, select a mapping from the drop down menu and press "Ok".
If Mixxx did not come with a mapping for your controller, [search the
forum](http://mixxx.org/forums/search.php?fid[]=7) to see if anyone has
made one. If not, you can [map it
yourself](home#controller%20mapping%20documentation).

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

Some controllers have their own pecularities that are noted on their own
wiki pages. If the information below does not solve your problem, check
the wiki page for your controller, which you can find a link to on the
[DJ Hardware Guide](hardware%20compatibility).

### MIDI controllers on GNU/Linux

Make sure that the snd-seq-midi kernel module has been loaded. Open a
console and run `lsmod | grep snd_seq_midi` to check if the module has
been loaded. If it has not, run `modprobe snd-seq-midi` as root and
restart Mixxx.

### HID and USB Bulk controllers on GNU/Linux

If your controller does not appear in the list of controllers on the
left pane of Mixxx's Preferences (under the "Controllers" section),
Mixxx may not have permission to use your HID or USB Bulk device. (Mixxx
will say something to this effect in the
[log](#Troubleshooting-other-issues-\(Finding-the-mixxx.log-file\)) when
it scans for controllers.) Mixxx should automatically install a udev
rule to give users in the group called "users" permission to use HID and
USB Bulk devices. It is installed with the Ubuntu PPA and RPMFusion
package as well as when installing Mixxx from source (if you have write
access to /etc/udev/rules.d when running `scons install`), however
packages for other distributions might not install it correctly.

**Up to version 2.2.x**

If you still do not see your controller on the left side of Mixxx's
Preferences, check that your user account is in the group "users". Open
a console and run the command `groups` to find out what groups your user
is in. If `users` is not listed, run `usermod -aG users YOUR-USER-NAME`
as root to add YOUR-USER-NAME to the "users" group, log out, and log
back in.

If you did not install Mixxx from the Ubuntu PPA or RPMFusion, you may
need to save save [this
file](https://raw.githubusercontent.com/mixxxdj/mixxx/master/res/linux/mixxx-usb-uaccess.rules)
to `/etc/udev/rules.d/mixxx-usb-uaccess.rules`. You will need root
privileges (use `sudo` or `su`) to copy the file to that location. Then,
restart your computer.

**Version 2.3 and later**

Please refer to the instructions in the [udev .rules
file](https://raw.githubusercontent.com/mixxxdj/mixxx/master/res/linux/mixxx-usb-uaccess.rules).
Both install location and target file name depend on your Linux
distribution.

## Mixxx says my sound card does not support the sample format

First try using each of the Sample Rate options on the Audio Hardware
page in Mixxx's preferences. (You have to press OK or Apply after
changing the setting for it to take effect.) Nearly all sound interfaces
support at least one of 48000 Hz or 44100 Hz so try both of those first.

If that doesn't help and you're on Linux, try opening a console and
running `export PA_ALSA_PLUGHW=1` before running `mixxx` (or
`pasuspender mixxx`, see above). To avoid having to do this every time
you run Mixxx, add `export PA_ALSA_PLUGHW=1` to the end of /etc/profile
or \~/.bashrc, log out, and log back in. This will tell PortAudio, the
library Mixxx uses to interact with sound hardware on multiple operating
systems, to use ALSA's plughw devices rather than hw. plughw
automatically converts audio streams to a sample format supported by the
sound card.

## I can't preview tracks in headphones

This requires either a sound card with 4 (mono) output channels,
multiple sound cards, or a DJ splitter cable. See the [DJ Hardware
Guide](hardware%20compatibility) for more information. Both the Master
and Headphones outputs must be configured in the Sound Hardware section
of Options \> Preferences.

To make the track playing in your headphones not play on the main
output, turn the volume down on the deck you do not want your audience
to hear yet (or push the crossfader all the way to the opposite side)
then press the headphone ('PFL') button for that deck. This will not
turn down the volume in your headphones; it will only turn down the
volume on the main output.

## There is a delay before I hear a change in the audio

Your audio latency may be set too high. See the [Adjusting Audio
Latency](Adjusting%20Audio%20Latency) page for tips on adjusting your
latency.

## My sound card randomly stops working

This can happen when poor quality USB cables pick up electromagnetic
interference. Some sound cards are bundled with poor quality USB cables.
Sending digital audio over USB requires a clear, uninterrupted signal
transmitted at regular time intervals (isochronus transfer). This is
more sensitive to interference than most USB signals. Try using a
different USB cable if you have one. If that does not work, consider
getting a [Chroma
Cable](https://store.djtechtools.com/products/chroma-cables-usb) from DJ
Tech Tools. These are high quality USB cables made specifically for DJs
with a ferrite bead on each end to dissipate high frequency interference
as heat. Additionally, try to avoid having your USB cables near sources
of interference like other devices' power cables.

Also see [this
guide](https://www.native-instruments.com/en/support/knowledge-base/show/2085/choosing-the-correct-usb-cable-for-your-ni-hardware-device/)
from Native Instruments for identifying USB cables that are better for
DJ gear.

## I have some other issue with sound on Windows

Try different options for the sound API. If the manufacturer of your
sound card provides an ASIO driver, it is recommended to install that
and use ASIO. Select which sound API to use in Options \> Preferences \>
Sound Hardware. See [the
manual](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api)
for an explanation of the different sound APIs.

## I hear the microphone input echoed back with a delay

Refer to the [Using Microphones chapter of the
manual](https://mixxx.org/manual/latest/en/chapters/microphones.html).

## BPM of tracks is not shown in my library

Scanning and analyzing the library are separate steps because analyzing
tracks takes a lot of CPU resources and time. When a track that has not
been analyzed is loaded, Mixxx will analyze its BPM and Replay Gain as
well as generate the waveform. You can analyze your whole library in
advance so you can see the BPM of every track in your library before
loading it. When you have time to let your computer run for a long time
(for example, before you go to sleep), go to "Analyze" on the left panel
of the library display in Mixxx's main window. Select the "All" button
on the top left, click the "Select All" button on the top right, then
click the "Analyze" button in the top right.

## New songs are not shown in my library

Click Library-\>Rescan library, wait for the scan to finish, and search
for your new music.

## My music was not detected by the library scanner

Mixxx supports the following audio file formats:

  - FLAC
  - OGG/Vorbis (as OGG files, **not** OGA)
  - Opus
  - MP3
  - WAV
  - AIFF
  - AAC/M4A/MP4 (with plugin)
  - WavPack (WV) (with plugin)

If your music isn't currently in one of these formats (or you don't have
a suitable plugin installed) it won't show up in the Mixxx library.
You'll need to use a program like Sox, Audacity, or ffmpeg to convert
it.

## What do I enter for the user name in Live Broadcasting?

  - For an Icecast2 server, the user name is **source** by default.
  - For a Shoutcast server, the user name is **admin** by default.

## Beatgrid is not aligned with the beats

If the detected BPM of a track is correct but the beat markers are not
in the correct place, seek the track to where a beat starts. Click the
"Adjust beatgrid" icon in the grid of icons to the right of the overview
waveform. This is the bottom left icon in the grid.

## BPM detection is wrong

Try adjusting the BPM analyzer's range. Go to Options \> Preferences \>
Beat Detection, adjust the numbers, and press okay. Reanalyze your
tracks.

## I have a decently fast system & video card. Why does Mixxx seem to crawl or pin the CPU?

We've seen this a few times and it has always been a video driver
problem. Make sure you have the latest drivers for your card. (You may
need to get them from the chipset maker (nVidia, AMD/ATI) rather than
the system board or computer manufacturer, since the manufacturer
drivers aren't always the latest.) Also, if you're on Windows, make sure
you have the latest [DirectX](http://support.microsoft.com/kb/179113)
installed. See also [\#What should I do to get Mixxx to run the best it
can on my
computer?](#What%20should%20I%20do%20to%20get%20Mixxx%20to%20run%20the%20best%20it%20can%20on%20my%20computer?)

## Mixxx freezes, crashes, or otherwise misbehaves and I have an nVidia graphics card

Before you try anything else, please update or reinstall your nVidia
graphics driver. (This applies to all OSes.) Even if it is the same
exact version, apparently it is fickle and needs to be
rebuilt/reinstalled any time things change in the OS. Try this first
before going any further. You might also try getting the latest driver
from nVidia's web site instead of your PC/card manufacturer since they
may be newer.

If you are using GNU/Linux, try uninstalling the proprietary nVidia
driver and using the free nouveau driver.

## Errors on starting Mixxx

**`Could not open xml file: "/usr/local/share/mixxx/schema.xml"`**
happens to people that have built Mixxx from source but didn't do the
install step. You can either do that (with `sudo scons install`) or
explicitly tell Mixxx where to look for resources with the
`-``-resourcePath` command line parameter, like so: `./mixxx
-``-resourcePath res/`

## How can I move my music to another folder or hard drive without losing information like BPM or cue points?

Unfortunately, this does not yet work automagically but needs some
manual fiddling with the music configuration files. Here is one way of
doing it:

1.  **Backup your mixxx configuration files** (under Linux, this is
    `.mixxx/` in the home folder)
2.  Move your music folder to the new folder or new hard drive
3.  Install *SQLite Manager*, which is a Firefox extension that lets you
    manipulate the mixxx database:
    <https://addons.mozilla.org/de/firefox/addon/sqlite-manager/>
4.  Open the SQLite Manager from within firefox. Within SQLite Manager
    open the file `mixxxdb.sqlite` that can be found in your mixxx
    configuration folder
5.  Go on `Execute SQL` and enter:

        update track_locations set directory = replace (directory, '/old/path/DJ/Music/', '/new/path/DJ/Music/');
        update track_locations set location = replace (location, '/old/path/DJ/Music/', '/new/path/DJ/Music/');

    where the old and new paths point to your corresponding music folders. 
6.  Then hit `Run SQL`. The above statements will replace all instances
    of `/old/path/DJ/Music/` to `/new/path/DJ/Music/` in the field of
    *location* and *directory* of *track\_locations* table.
7.  Start `mixxx` and under settings change your music folder to the new
    one. If you want you can do a rescan to check that the music files
    do not turn up twice suddenly (if you are on linux, do especially
    check music files which where in symbolically linked directory).
    Check if bpm and other meta infomation like cue points are still
    stored with the files.

## Starting with a new configuration

Sometimes an old or invalid configuration setting can cause Mixxx to do
strange or unexpected things. It's always a good idea to try with a
fresh, clean default configuration to see if your problem disappears.

First, close Mixxx completely. Then rename your Mixxx configuration
directory:

  - **Linux**: The configuration is stored in a hidden directory called
    `.mixxx` off of your home directory. Rename it using the console
    command `mv ~/.mixxx ~/.mixxx-backup`
  - **Windows**: 
    1.  Open a File Explorer window and browse to `%LOCALAPPDATA%`.
    2.  Rename the `Mixxx` folder there to something else like
        `Mixxx-Backup`. 

<!-- end list -->

  - **macOS**: Rename your Mixxx configuration directory by opening a
    Terminal (under Applications -\> Utilities) and entering `mv
    ~/Library/Application Support/Mixxx ~/Library/Application
    Support/Mixxx-backup`

Then start Mixxx again and test to see if your problem still exists.
(You can rename or copy the directory back to restore your settings when
you're done testing.)

## Mixxx on Wayland

Some Linux distributions like
[Fedora 31](https://fedoraproject.org/wiki/Changes/Qt_Wayland_By_Default_On_Gnome)
switched to using [QtWayland](https://wiki.qt.io/QtWayland) as the
default *platform plugin* for Qt applications in a *Wayland* desktop
environment. This [does not work as
expected](https://bugs.launchpad.net/mixxx/+bug/1850729) for Mixxx.
There are two options to enforce using the X11 platform plugin `xcb`
instead of `wayland`:

  - Set the environment variable `QT_QPA_PLATFORM=xcb`
  - Start Mixxx with the command-line argument `-platform xcb`

The desktop launchers in the source repository already include this fix.

## Troubleshooting other issues (Finding the mixxx.log file)

Refer to [Finding the mixxx.log file](Finding%20the%20mixxx.log%20file)
