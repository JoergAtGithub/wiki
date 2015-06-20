***If you were directed here from the Sound Hardware preferences in
Mixxx, see [Adjusting Audio Latency](Adjusting%20Audio%20Latency).***

# Troubleshooting

If you've got a question that's not answered here, please post in the
[forums](http://www.mixxx.org/forums).

## I can't plug in my headphones and speakers at the same time

This requires either a sound card with 4 (mono) output channels or
multiple sound cards. Nearly all sound cards built into computers have
only one output pair, so you will need to add a second sound card with
one or more additional output pairs. See the [DJ Hardware
Guide](hardware%20compatibility) for more information.

## I pressed the headphone button but I still hear that deck on the main output

To make the track playing in your headphones not play on the main
output, turn the volume down on the deck you do not want your audience
to hear yet (or push the crossfader all the way to the opposite side)
then press the headphone ('PFL') button for that deck. This will not
turn down the volume in your headphones; it will only turn down the
volume on the main output.

## I hear crackling

Your audio latency may be set lower than your system can handle. See the
[latency](latency) page for tips on adjusting your latency.

If you are using two separate sound cards and the crackling is only in
your headphones, see below.

## I hear crackling in my headphones

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

## There is a delay before I hear a change in the audio

Your audio latency may be set too high. See the [latency](latency) page
for tips on adjusting your latency.

## My controller does not work

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

## New songs are not shown in my library

Click Library-\>Rescan library, wait for the scan to finish, and search
for your new music.

## My music was not detected by the library scanner

Mixxx supports the following audio file formats:

  - MP3
  - OGG
  - FLAC
  - WAV, AIFF
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
installed.

## Mixxx freezes, crashes, or otherwise misbehaves and I have an nVidia graphics card

Before you try anything else, please update or reinstall your nVidia
graphics driver. (This applies to all OSes.) Even if it is the same
exact version, apparently it is fickle and needs to be
rebuilt/reinstalled any time things change in the OS. Try this first
before going any further. You might also try getting the latest driver
from nVidia's web site instead of your PC/card manufacturer since they
may be newer.

## I can't select my sound card(s) when starting Mixxx from a console on GNU/Linux

On most GNU/Linux distributions today, the PulseAudio sound server is
automatically started upon logging in. PulseAudio is convenient for most
desktop audio use, but it is inappropriate for audio use that requires
low latency like Mixxx. The PulseAudio daemon occupies the ALSA device
while it is running. To temporarily disable PulseAudio while Mixxx is
running, start it with `pasuspender mixxx`. To run Mixxx with command
line options, such as `--mididebug`, run `pasuspender -- mixxx
--mididebug`

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

<!-- end list -->

1.  or /lib/udev/rules.d/15-mixxx-usb.rules in Ubuntu 12.04
