# Frequently Asked Questions

If you've got a question that's not answered here, please post in the
[forums](http://www.mixxx.org/forums)\! Also see the
[Troubleshooting](Troubleshooting) page.

## How do I monitor one track in the headphones with the other playing out the main output?

This requires either a multi-channel sound card or multiple sound cards.
Note that nearly all built-in sound cards have only one output pair, so
you will need to add a second sound card with one or more additional
output pairs. See [below](faq#does_mixxx_support_multiple_soundcards)
and the [sound card information](hardware_compatibility#sound_cards)
page for more information.

## How do I record my Mixxx session?

Mixxx 1.6.0 and up support recording mixes to WAV and AIFF files.
Versions 1.9.0 and up also support recording to MP3 and Ogg Vorbis
formats. To choose the format, click "Options", then "Preferences", then
"Recording" and set the options as you like. To start recording your
mix, click "Options" and select "Record Mix". You will then be prompted
to enter a file name, and after that, Mixxx will start recording about 5
seconds after you start playing a track. (So to get the beginning, play
something, stop the deck, wait 5 seconds, then begin mixing.) When
you're done recording, go back to "Options "and toggle "Record Mix"
again, or just exit Mixxx.

## What's the best hardware DJ controller to use with Mixxx?

"Best" is a matter of preference. It depends on what exactly you want to
do with a controller. Do you want to control everything, or use one as a
bunch of extra buttons in conjunction with turntables? Mixxx 1.7 and up
has the ability to provide comprehensive support for any MIDI controller
due to its scripting engine, and it ships with mappings for a number of
popular controllers, a complete list of which can be found on the
[Hardware Compatibility](Hardware%20Compatibility) page.
Community-contributed mappings for more controllers can be found [on the
forums](http://mixxx.org/forums/viewforum.php?f=7).

## Does Mixxx support multiple soundcards?

Yes, as of v1.6.0. This means you can have the headphone output coming
out of one sound card and have the master output going out another.

But **please note** that due to natural differences in clock crystals
even between two cards of the exact same model, it's not possible to
have multiple cards work synchronously. As a result, you will likely
hear pops or skips when using more than one card. Mixxx v1.9.2 and up
will lock to the clock of the card used for the Master output so at
least these pops aren't heard on the dance floor, but it's always
recommended to instead use a single sound card with multiple stereo
outputs, such as on a true surround (5.1 channel) sound card: you can
use the "front" output as your master output, and plug your headphones
into the "rear" output for cueing.

:\!: Be aware that sound cards are usually marketed with the number of
<span class="underline">monaural</span> channels they have, and you need
two mono channels for one stereo signal, so you would need at least a
four-output card to have Master and Headphones outputs on the same card.
(And if you're using vinyl control with two decks, that means you need a
card with at least four inputs too.)

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

See the [Vinyl Control](Vinyl%20Control) page.

## Does Mixxx modify the files or structure of my library?

No, Mixxx does not write to or move any files in your library. It's safe
to use Mixxx with your iTunes library - Mixxx will not change anything
in your library.

As of Mixxx 1.9.0, there is an option to write metadata changes back to
the file tags (e.g. ID3, Xiph/Ogg, APE) but this is disabled by default.
You can enable it from the Mixxx Library Preferences.

## What platforms are officially supported by Mixxx?

As of release 1.6.0, the official Mixxx **binary** releases attempt to
support the following operating systems equally:

  - Windows - XP (Home/Pro) and Vista (all versions)
  - Linux - Ubuntu (Hardy Heron)
  - Mac - Intel Macs (OSX 10.4+)

We also support the following platforms through binary releases on a
best effort basis, not all beta releases will be built for these
platforms and full releases often lag behind the release cycle by a
month or so:

  - Linux - Generic i386 binary
  - Mac - PPC Macs

Many Linux distributions (e.g. Debian) bundle their own copy of Mixxx
rather than relying on our official releases, check with your
distribution for more details.

Of course as an open source project, source is always available to build
for whatever platform you work on, either a Linux distribution which
doesn't provide Mixxx packages or something more exotic. Historically
Mixxx has been known to compile on FreeBSD.

We are always happy to hear from people building Mixxx on other
platforms, whether you are doing a one-time build for yourself or
maintaining a Mixxx package for a distribution please get in touch.

## What music file formats can Mixxx play?

As of release 1.8.x, Mixxx supports the following file formats:

  - MP3
  - OGG
  - FLAC
  - WAV, AIFF
  - AAC/M4A (with plugin)
  - WavPack (WV) (with plugin)

If your music isn't currently in one of these formats (or you don't have
a suitable plugin installed,) it won't show up in the Mixxx library.
You'll need to use a program like Sox or Audacity to convert it.

## What happens if a file's sample rate is different from the sound card rate?

Mixxx performs sample rate conversion on the fly.

Note that the quality of the re-sampling depends on the setting of the
*pitch behaviour*. Having key lock disabled ("vinyl emulation" in 1.8.x
and below) will use linear interpolation, which doesn't sound very good
(you will notice graininess and increased noise, especially obvious on
high, long notes). When you enable key lock ("pitch-independent
time-stretch" in 1.8.x and below,) Mixxx will use a vocoder-based
algorithm from the SoundTouch library, which sounds a lot better (but is
not recommended when scratching.)

## How can I move my music to another folder or hard drive without loosing information like bpm or cue points?

Unfortunately, as of today (mixxx 1.10) this does not work automagically
but needs some manual fiddling with the music configuration files. Here
is one way of doing it:

1.  **Backup your mixxx configuration files** (under Linux, this is
    `.mixxx/` in the home folder)
2.  Move your music folder to the new folder or new hard drive
3.  Install *SQLite Manager*, which is a firefox extensions that lets
    you manipulate the mixxx database:
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
    do not turn up twice suddenly. Check if bpm and other meta
    infomation like cue points are still stored with the files.
