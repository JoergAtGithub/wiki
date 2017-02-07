***If you were directed here from the Sound Hardware preferences in
Mixxx, see [Adjusting Audio Latency](Adjusting%20Audio%20Latency).***

# Troubleshooting

If you've got a question that's not answered here, please post in the
[forums](http://www.mixxx.org/forums). Please be sure you are using the
latest version of Mixxx before you ask for help. The latest version is
available on [the download page](http://mixxx.org/download).

## A deck randomly stops playing

There is currently a known bug with decoding M4A/AAC files on Windows in
Mixxx 2.0 that can cause a deck to seemingly randomly stop playing until
Mixxx is restarted. If you can help resolve this bug by developing or
testing on Windows, please contribute\! See the following bug reports:

https://bugs.launchpad.net/mixxx/+bug/1490580  
<https://bugs.launchpad.net/mixxx/+bug/1519472>

The most reliable workaround would be to convert all your M4A/AAC files
to FLAC. [Fre:AC](https://www.freac.org/) is a free program that can do
this. Unfortunately, this wastes a lot of disk space. Keep your original
M4A/AAC files around so you can delete the FLAC files when this bug is
fixed. Converting lossy M4A/AAC files to another lossy format will sound
worse than the starting M4A/AAC files and is not advised.

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

## My controller does not work

To use a MIDI or HID controller with Mixxx, enable the device and load a
mapping. Go to Options \> Preferences in Mixxx and look for your
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

Some controllers have their own pecularities that are noted on their own
wiki pages. If the information below does not solve your problem, check
the wiki page for your controller, which you can find a link to on the
[DJ Hardware Guide](hardware%20compatibility).

### MIDI controllers on GNU/Linux

Make sure that the snd-seq-midi kernel module has been loaded. Open a
console and run `lsmod | grep snd_seq_midi` to check if the module has
been loaded. If it has not, run `modprobe snd-seq-midi` as root and
restart Mixxx.

This happens on GNU/Linux where devices like the American Audio VMS4.1
only show up as an HID device, not a MIDI device. Also, there is [a
bug](https://bugs.archlinux.org/task/44286) in Arch Linux that requires
loading the snd-seq-midi module manually.

# Native Instruments Traktor Kontrol S4 MK2

[[/media/native_instrument_traktor_s4-mkii-1.jpg|native\_instrument\_traktor\_s4-mkii-1.jpg]]

  - [Manufacturer's product
    page](https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s4/)
  - [DJTechTools
    review](http://djtechtools.com/2013/10/22/review-traktor-kontrol-s4-mk2-and-s2-mk2/)
  - [Digital DJ Tips
    review](http://www.digitaldjtips.com/2013/10/review-video-traktor-kontrol-s4-mk2/)
  - [DJWORX
    review](https://djworx.com/review-ni-traktor-kontrol-s4-mk2-dj-controller/)

The Kontrol S4 MK2 is a 4 deck all-in-one controller with a sturdy build
quality and integrated sound card. The MK2 has substantial improvements
over the S4 MK1, including large multicolor buttons. The MK1 is not
supported and cannot be supported because it uses a proprietary
communication protocol exclusive to Traktor. The MK2 uses the open HID
standard, so it can work with Mixxx. The easiest way to tell the MK1
apart from the MK2 is the appearance of the jog wheel. On the MK1, the
top of the jog wheel is black plastic; on the MK2, the top of the jog
wheel is shiny aluminum.

## Compatibility

### Controller

The Kontrol S4 MK2 is compatible with Mixxx without any proprietary
drivers on GNU/Linux and Mac OS X. On Windows, it is recommended to
install the [driver from Native
Instruments](https://www.native-instruments.com/en/support/downloads/drivers-other-files/)
and select the ASIO sound API in the Sound Hardware section of Mixxx's
Preferences.

With the S4 plugged in, a MIDI device is listed as an available
controller in Mixxx's Preferences. That is the MIDI input/output ports
on the back of the S4 for connecting external MIDI gear; no mapping for
the S4 will appear in the menu for the MIDI device. The controller uses
HID, so the mapping can only be loaded when you select the HID device on
the left side of Mixxx's Preferences.

### Timecode vinyl

The phono inputs on the S4 can be used with turntables for timecode
vinyl control of Mixxx. Unlike Traktor, there is no additional software
to install to use timecode with the S4; the free version of Mixxx is the
full version. However, note that Mixxx is not compatible with Traktor
Scratch Mk2 timecode; refer to the [Mixxx
manual](http://mixxx.org/manual/latest/chapters/vinyl_control.html#supported-timecode-media)
for a list of supported types of timecode.

## Mapping description

Most of the functions are mapped as they appear on the device and most
users coming from Traktor should not have a problem picking up and using
the controller right away. While there is a lot of overlap between Mixxx
and Traktor, some buttons on the S4 do not quite translate to Mixxx.
This guide is not a replacement for the [Mixxx
Manual](http://www.mixxx.org/manual/2.0/) and any questions not answered
here ("What is keylock?") are addressed there.

Note that Mixxx doesn't have the concept of a single "master" deck for
sync. Instead, you should push and hold the sync button to "lock" sync
on for all decks you want to remain in sync. Or you can push Shift +
Sync to lock sync on. See [the Mixxx
manual](http://www.mixxx.org/manual/2.0/chapters/djing_with_mixxx.html#master-sync)
for details.

Mixxx does not have remix decks, so the four remix slot buttons have
been repurposed. By default, they will launch samples in the sampler
decks.

The Loop Size select knob is not fully implemented. Currently, pressing
the "Loop Set" knob always creates an 8 bar loop, and turning the knob
will change the size of existing loops. This will be fixed in a future
update to allow creation of arbitrary-sized loops.

The FX Mode button changes which effect is loaded in the FX bank.
Currently only one effect can be loaded in each bank.

There are some more bonus actions that can be accessed by holding shift
and pressing certain buttons.

\* Shift + Loop Move will adjust the musical pitch of the track without
changing the speed. \* Shift + pressing the Loop Move knob will reset
the musical pitch to natural. \* Shift + Loop Size will seek quickly
through the track for easy previewing. \* Shift + Load will eject the
track. \* Shift + Remix Slot will create a loop of predetermined size.

The Master Volume knob on the S4 controls the built-in hardware volume
directly, so we have chosen not to also bind it to the Mixxx software
master volume control. Peak display is only generated from software,
however. So if you see or hear clipping, it won't help to lower the
master volume knob -- adjust the knob in the Mixxx GUI or lower the gain
of the playing tracks.

### Unused controls

  - Snap button does nothing (in Mixxx, Quantize does both Quantizing
    and Snapping)
  - Master button does nothing, but lights up when sync is enabled
  - Loop recorder knob and buttons do nothing
  - FX knob buttons do nothing
  - While the Flux button works, the Reset button does nothing

### Mapping options

If you choose, you can edit the controller script and change the Remix
Slot buttons to perform loop rolls instead. Also by default, Shift + CUE
rewinds the track to the beginning but you can change this to a Reverse
Roll (or "Censor") effect instead.

Making these changes is still a little awkward and we will be making
controller preferences easier to change in the future. For now you'll
have to make a small change to the mapping script file. Don't worry, the
actual edit only involves replacing a single word in a text file.

1.  Open Mixxx Preferences and select the Kontorl S4 in the side list.
2.  You should see a series of tabs at the top of the preferences
    window, one of which is "Scripts". Select that tab.
3.  Select "Traktor-Kontrol-S4-MK2-hid-scripts.js". 
4.  Click "Open Selected File."
5.  Either the file should open in an editor, or you should see a file
    browser window with that file selected. If you see a file browser,
    right click the file and select an option to edit it.
6.  At the top of the file will be short instructions explaining what to
    do.

### TODO

There are some features we still plan to add to this mapping:

  - New effects interface in Mixxx 2.1
  - Loop size readout / selection
  - On Air indicator for shoutcast or set recording
  - Find uses for other unused buttons
  - Microphone volume knob

## Mixxx says my sound card does not support the sample format

Try opening a console and running `export PA_ALSA_PLUGHW=1` before
running `mixxx` (or `pasuspender mixxx`, see above). To avoid having to
do this every time you run Mixxx, add `export PA_ALSA_PLUGHW=1` to the
end of /etc/profile or \~/.bashrc, log out, and log back in. This will
tell PortAudio, the library Mixxx uses to interact with sound hardware
on multiple operating systems, to use ALSA's plughw devices rather than
hw. plughw automatically converts audio streams to a sample format
supported by the sound card.

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

## I hear crackling

Your audio latency may be set lower than your system can handle. See the
[Adjusting Audio Latency](Adjusting%20Audio%20Latency) page for tips on
adjusting your latency.

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

By default, Mixxx combines microphone inputs with the main output,
broadcasting, and recording signals. It takes time for the signal from
your microphone to go through your sound card's analog-to-digital
converter, through Mixxx, and back out through your sound card's
digital-to-analog converter. So, the microphone signal reaches your
speakers and/or headphones a few milliseconds after you make the sound.
If you are only interested in broadcasting or recording with your
microphone input, you can prevent Mixxx from mixing the delayed input
signal with the main output to your sound card. Go to Options \>
Preferences \> Sound Hardware in Mixxx. Change the "Microphone/Talkover
Mix" option from "Master output" to "Recording and Broadcasting Only".

If you do want to mix the signal from your microphone with Mixxx's
output with an unnoticeably small delay, mix the microphone signal with
Mixxx's output without digitizing it. However, you won't be able to
record or broadcast the microphone signal. DJ controllers with
microphone inputs and integrated sound cards often do this. If you are
plugging Mixxx's output into another hardware mixer, this can be done by
plugging your microphone into that mixer instead of running it through
Mixxx.

Alternatively, sound cards marketed for recording typically have a
feature called direct monitoring that mixes the input signal directly
with the output without digitizing it, and also runs the digitized
signal to the computer. These sound cards typically have a knob on them
that controls the mix between the computer output and the direct monitor
signal. See your sound card's manual for more information.

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
  - OGG
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
5.  Go on `Execute SQL` and enter: `update track_locations set directory
    = replace (directory, '/old/path/DJ/Music/', '/new/path/DJ/Music/');
    
    update track_locations set location = replace (location,
    '/old/path/DJ/Music/', '/new/path/DJ/Music/');` where the old and
    new paths point to your corresponding music folders. 
6.  Then hit `Run SQL`. The above statements will replace all instances
    of `/old/path/DJ/Music/` to `/new/path/DJ/Music/` in the field of
    *location* and *directory* of *track\_locations* table.
7.  Start `mixxx` and under settings change your music folder to the new
    one. If you want you can do a rescan to check that the music files
    do not turn up twice suddenly (if you are on linux, do especially
    check music files which where in symbolically linked directory).
    Check if bpm and other meta infomation like cue points are still
    stored with the files.

## Troubleshooting other issues (Finding the mixxx.log file)

Mixxx logs debugging information, [MIDI/HID/etc.
messages](command_line_options) it receives and script functions it
loads in the `mixxx.log` plain text file. When you [report a
bug](reporting%20bugs) or ask for help on the Mixxx forum or IRC
channel, please attach your `mixxx.log` file to help us help you.

  - **Linux:** \~/.mixxx/mixxx.log
  - **Windows:** `%LOCALAPPDATA%\Mixxx\mixxx.log` on Vista and up,
    `%USERPROFILE%\Local Settings\Application Data\Mixxx\mixxx.log` on
    XP and below. (You can just type either of those into the Location
    bar of a Computer or Folder window, or even under Start -\> Run...
    and press Enter.)
  - Note: The file may not show up as `mixxx.log` unless you've
    unchecked `Hide extensions for known file types` in the Windows
    Explorer folder options. Until then it is just `mixxx`, the only
    text file in that location (with a notepad icon.) By default in
    Windows 7 and up, extensions for known file types are set to hidden.
    See [How to show or hide file name extensions in Windows
    Explorer](http://support.microsoft.com/kb/865219).
  - **Mac OS X:** `/Users/<username>/Library/Application Support/Mixxx`
  - Note: The user library folder is hidden by default, so use one of
    the following methods to open the Mixxx folder.

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
