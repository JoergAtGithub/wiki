# Frequently Asked Questions

If you've got a question that's not answered here, please post in the
[forums](http://www.mixxx.org/forums)\! Also see the
[Troubleshooting](Troubleshooting) page.

## How can I hear one track in the headphones with the other playing out the main output?

This requires either a sound card with 4 (mono) output channels or
multiple sound cards. Nearly all sound cards built into computers have
only one output pair, so you will need to add a second sound card with
one or more additional output pairs. See the [DJ Hardware
Guide](hardware%20compatibility) for more information.

To make the track playing in your headphones not play on the main
output, turn the volume down on the deck you do not want your audience
to hear yet (or push the crossfader all the way to the opposite side)
then press the headphone ('PFL') button for that deck. This will not
turn down the volume in your headphones; it will only turn down the
volume on the main output.

## How do I record my Mixxx session?

Click "Options" and select "Record Mix". When you're done recording, go
back to "Options "and toggle "Record Mix" again, or just exit Mixxx. To
choose the recording format, click "Options", then "Preferences", then
"Recording" and set the options as you like.

## Is it possible to use Mixxx with an external mixer?

Yes. There are two ways to do it depending on what you want to achieve:

  - **Direct deck outputs**: Direct deck outputs is a feature of Mixxx
    1.9.0 onwards. [Set the outputs](manual#external_mixer_mode) in
    Options-\>Preferences-\>Sound Hardware and you're done. If you are
    on 1.8.x or below, the trick is to force Mixxx's master output to
    play back the left/top track, and the headphone output to playback
    the right/bottom track. (Each track will come out a separate output,
    suitable for plugging right into an external DJ mixer.) The way one
    does this is by sliding Mixxx's crossfader all the way to the left,
    and turning on the headphone cue for the right channel. This forces
    the first track to play out the master out, and the second track to
    play out the headphone out. (Since both outputs are now going
    straight into an external mixer, you'd use the headphone cue on the
    mixer as well as it's crossfader.) Using an external mixer is also
    described briefly in the [Threadbox
    tutorial](http://mixxx.sourceforge.net/wiki/index.php/Threadbox_Tutorial#Using_an_External_Mixer_or_MIDI_Device).
  - **Software mixing as an additional sound source**: If you want to
    mix on-screen but need to integrate with an external mixer (such as
    when playing CDs and/or records as well, or in a radio studio) you
    can plug the headphone output into one channel of the mixer, and the
    main output into another. Then bring the channel fader of the
    headphone one all the way down on the mixer and set it to play in
    your headphones all the time (thereby adding Mixxx's headphone bus
    to the mixer's.) Then use the other fader (with Mixxx's main output)
    when you want to bring Mixxx's output into/out of the main mix.

## What's vinyl control all about? How do I use it?

See the [manual
chapter](http://mixxx.org/manual/latest/chapters/vinyl_control.html).

## Does Mixxx modify the files or structure of my library?

No, Mixxx does not write to or move any files in your library. It's safe
to use Mixxx with your iTunes library - Mixxx will not change anything
in your library.

There is an option to write metadata changes back to the file tags (e.g.
ID3, Xiph/Ogg, APE) but this is disabled by default. You can enable it
from the Mixxx Library Preferences.

## Yeah, but does it run on Linux?

Yes. Yes it does.

## What platforms are officially supported by Mixxx?

  - Windows XP and newer. Windows 10 Beta support is spotty.
  - GNU/Linux, with official binary packages for Ubuntu 10.04 (Lucid)
    and newer
  - Mac OS X 10.4+

Many GNU/Linux distributions (e.g. Debian) bundle their own copy of
Mixxx rather than relying on our official releases, check with your
distribution for more details.

Of course as an open source project, source is always available to build
for whatever platform you work on, either a Linux distribution which
doesn't provide Mixxx packages or something more exotic. Historically
Mixxx has been known to compile on FreeBSD.

We are always happy to hear from people building Mixxx on other
platforms, whether you are doing a one-time build for yourself or
maintaining a Mixxx package for a distribution please get in touch.

## What music file formats can Mixxx play?

  - MP3
  - OGG
  - FLAC
  - WAV, AIFF
  - AAC/M4A/MP4 (with plugin)
  - WavPack (WV) (with plugin)

If your music isn't currently in one of these formats (or you don't have
a suitable plugin installed) it won't show up in the Mixxx library.
You'll need to use a program like Sox or Audacity to convert it.

## What happens if a file's sample rate is different from the sound card rate?

Mixxx performs sample rate conversion on the fly.

Note that the quality of the re-sampling depends on the setting of the
*pitch behaviour*. Having key lock disabled ("vinyl emulation" in 1.8.x
and below) will use linear interpolation, which doesn't sound very good
(you will notice graininess and increased noise, especially obvious on
high, long notes). When you enable key lock ("pitch-independent
time-stretch" in 1.8.x and below) Mixxx will use a vocoder-based
algorithm from the SoundTouch library, which sounds a lot better (but is
not recommended when scratching).

## How can I move my music to another folder or hard drive without losing information like bpm or cue points?

Unfortunately, this does not yet work automagically but needs some
manual fiddling with the music configuration files. Here is one way of
doing it:

1.  **Backup your mixxx configuration files** (under Linux, this is
    `.mixxx/` in the home folder)
2.  Move your music folder to the new folder or new hard drive
3.  Install *SQLite Manager*, which is a Firefox extension that lets you
    manipulate the mixxx database:
    <https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager-webext>
4.  Open the SQLite Manager from within firefox. Within SQLite Manager
    open the file `mixxxdb.sqlite` that can be found in your mixxx
    configuration folder
5.  Go on `Execute SQL` and enter:  
    ```
        update track_locations set directory = replace (directory, '/old/path/DJ/Music/', '/new/path/DJ/Music/');  
        update track_locations set location = replace (location, '/old/path/DJ/Music/', '/new/path/DJ/Music/');  
    ```
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
