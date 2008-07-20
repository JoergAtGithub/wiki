# Table of Contents

1.  [Beginner's Guide](Beginner's%20Guide)
2.  [Introduction](manual#introduction)
3.  [Installation](manual#installation)
    1.  [Windows](manual#windows)
    2.  [Linux](manual#linux)
    3.  [OS X](manual#os_x)
4.  [User Interface Overview](manual#userinterface)
5.  [Configuration](manual#configuration)
    1.  [Master and Headphone
        Outputs](manual#master_and_headphone_outputs)
    2.  [Latency](manual#latency)
    3.  [Samplerates](manual#samplerates)
    4.  [Sound APIs](manual#sound_apis)
    5.  [Vinyl Control](manual#vinyl_control)
6.  [DJing with Mixxx](manual#djing_with_mixxx)
    1.  [Loading Tracks](manual#loading_tracks)
    2.  [Waveform Displays](manual#waveform_displays)
    3.  [Beatmatching and Mixing](manual#beatmatching_and_mixing)
    4.  [Headphone Cueing](manual#headphone_cueing)
7.  [Keys and Hardware
    Controllers](manual#keys_and_hardware_controllers).
    1.  [Keyboard Shortcuts](manual#keyboard_shortcuts).
    2.  [MIDI Controllers](manual#midi_controllers).
8.  [Getting Involved](manual#getting_involved).

# Introduction

Mixxx is software for DJs that allows you to mix songs live. Mixxx
supports MP3, OGG, FLAC, and WAVE playback, and can be controlled by
numerous DJ MIDI controllers.

# Installation

## Windows

Windows users can install Mixxx by double-clicking on the Mixxx
installer executable. Mixxx is supported on Windows XP and Vista.

## Linux

Linux users can often find Mixxx included with their favourite
distribution. For example, **Ubuntu** users can install Mixxx through
the *Applications-\>Add/Remove...* menu item. If Mixxx is not packaged
for your distribution, you can compile Mixxx from scratch. For details
on compiling Mixxx, see: [Compiling on Linux](Compiling%20on%20Linux)

## OS X

OS X (Intel) users can install Mixxx by double-clicking the Mixxx zip
archive, and then dragging-and-dropping the Mixxx bundle into their
*Applications* folder. Mixxx requires an Intel Mac running OS 10.4+.

# Configuration

The first time Mixxx is started, you are asked to select a directory
containing your music library. This directory will be scanned and any
music found will be indexed in Mixxx's internal library. The music
library path can be changed at any time in the preferences, via the
*Library and Playlists* pane.

Mixxx's preferences can be accessed by selecting
*Options-\>Preferences*.

When Mixxx is launched, it tries to select a reasonable sound device for
output. You can check which device Mixxx has selected in the *Sound
Hardware* pane in the preferences.

## Master and Headphone Outputs

Mixxx has two audio paths: The **Master** output and the **Headphones**
output. The Master output is what a DJ should have connected to their
main speakers, while the Headphones output should be connected to their
personal headphones. The headphone output is optional, and can be used
for [Headphone Cueing](#headphone-cueing).

To configure the Master and Headphones outputs, enter Mixxx's
preferences and select the *Sound Hardware* pane. In order to select a
headphone device, either a soundcard with at least 4 channels of output
(two stereo outputs, as featured on 5.1 soundcards) *or* two separate
stereo soundcards is required. The output channel mapping, which
determines the physical jack on the soundcard that the audio comes out
of, can be selected under "Channel".

<span class="underline">**Example Soundcard Configurations**</span>

**Single audio device (4 Channel Soundcard)**

    Master device:    Echo Digital AudioFire4   Channels: 1/2
    Headphone device: Echo Digital AudioFire4   Channels: 3/4

**Dual audio devices (Two Stereo Soundcards)**

    Master device:    ElCheapo USB Audio        Channels: 1/2
    Headphone device: SoundBlaster Live!        Channels: 1/2

## Latency

The latency in Mixxx indicates the amount of time it will take for the
audio to respond to any change in a control. For example, a latency of
36 ms indicates that it will take approximately 36 ms for Mixxx to stop
the audio after you toggle the play button. Generally speaking, the
lower the latency, the more responsive Mixxx will be. A latency between
36-64 ms is acceptable if you are using Mixxx with a keyboard/mouse or a
MIDI controller. A latency below 16 ms is recommended when vinyl control
is used because Mixxx will feel unresponsive otherwise.

In order to tweak your latency, reduce the latency slider in the *Sound
Hardware* preferences pane and experiment until you can reliably run
Mixxx **without hearing any crackles, pops, or dropouts in the audio**.
Changing your [Sound API](#sound-apis) to ASIO on Windows or JACK on
Linux may allow you to reduce your latency setting, but this depends on
your hardware configuration.

Keep in mind that **lower latencies require better soundcards and faster
CPUs** and that **zero latency DJ software is a myth** (although Mixxx
is capable of \< 10 ms operation).

## Samplerates

The soundcard samplerate describes the temporal resolution of its audio.
Because most audio tracks are encoded at a samplerate of 44100 Hz,
increasing the samplerate inside Mixxx beyond this may not lead to
increased audio quality. However, users that still prefer upsampled
audio can select a higher sampling rate in the *Sound Hardware*
preferences pane. Keep in mind that increasing the samplerate will
increase CPU usage and likely raise the minimum latency you can achieve.

## Sound APIs

Mixxx supports several different Sound APIs across Windows, OS X, and
Linux. A Sound API is a tool Mixxx uses to interact with soundcards.
Some soundcards come with drivers that are provide lower latency with
certain Sound APIs, so different APIs can be selected from *Sound
Hardware* preferences pane.

On Windows, **ASIO** is generally the lowest latency API. On OS X,
**CoreAudio** is the best choice, and on Linux, **JACK** or **ALSA**
provide the best compatibility and performance. Linux users wishing to
use JACK should **ensure they run the *jackd* daemon before launching
Mixxx**, otherwise JACK will not appear as a Sound API in the
preferences.

## Vinyl Control

Vinyl control allows a user to manipulate the playback of a song in
Mixxx using a real turntable as a controller. In effect, it simulates
the sound and feel of having your digital music collection on vinyl.
Many DJs prefer the tactile feel of vinyl, and vinyl control allows that
feel to be preserved while retaining the benefits of using digital
audio.

You can configure vinyl control through the *Vinyl Control* pane in the
preferences.

More information about Mixxx's vinyl control and supported hardware
configurations is available on the [vinyl control wiki
page](vinyl_control).

# User Interface Overview

# DJing with Mixxx

Mixxx was designed to be easy to learn for both novice and experienced
DJs. The user interface mimics a hardware DJ mixer, but also includes
several extra elements to gives DJs a better user experience, such as
the parallel waveform displays.

## Loading tracks

Songs can be loaded into a player in several ways:

  - Right-click the library track table: Right-clicking on a track in
    the table will present the options "Load in Player 1" and "Load in
    Player 2", among others. Making either selection will load a track
    into a player.
  - Drag-and-drop from library track table: Dragging-and-dropping a song
    from the track table onto a wavefoprm display will load a track into
    a player.
  - Drag-and-drop from external file browser: Dragging-and-dropping a
    song from an external file browser directly onto a waveform display
    in Mixxx will load that song. This function is also known to work on
    some platforms with other applications. For example, on OS X,
    dragging-and-dropping a track from iTunes onto one of Mixxx's
    waveform displays will load that song into a player.

## Waveform displays

There are two main **waveform displays** in Mixxx that are used to
display the waveform of the songs you are mixing. These are useful
because they allow you to see features in a song (like a breakdown)
before you hear them. The waveform displays are aligned parallel to each
other in order to make beat matching easier, as it is possible to
beatmatch visually by aligning the beats that appear in each waveform.

Clicking and dragging on a waveform allows you to seek through a song in
both directions. The waveform display is updated in realtime upon
seeking. There are two smaller **waveform summary** displays located
adjacent to the main waveform displays. These smaller displays show the
waveform envelope of the entire song, and are useful because they allow
DJs to see breakdowns far in advance. Vinyl DJs will find this familiar
because quiet sections of songs can be visually distinguished when
looking at a vinyl record, and this is a useful tool when planning your
mixes on-the-fly.

## Beatmatching and Mixing

**Beatmatching** is the process of adjusting the playback rate of a song
so that it matches the tempo of another song. Beatmatching also involves
adjusting the *phase* of the beats in a song so that they are *aligned*
with the beats in the other song. Matching the tempo and aligning the
beats are the two things a DJ must do to beatmatch.

In Mixxx, you can match the **tempo** of two songs by adjusting the
playback rate sliders on left and right side of the user interface. You
can adjust the **phase** of the beats by clicking-and-dragging on either
waveform display to temporarily slow down one of the songs until the
beats are aligned. The temporary pitch bend buttons can also be used to
momentarily adjust the playback rate, allowing you to "shuffle" the
beats in a song forwards or backwards, so they can be aligned with
another song.

Once the tempos are matched and the beats aligned between two songs,
they are said to be beatmatched. A "perfect" beatmatch is near
impossible - there will always be some tiny difference in the playback
rates. A keen DJ will keep his or her ears open and listen for the beats
drifting out of alignment. This has a distinct "double bass kick" sound
which is often preceded by the kick weakening in intensity (as the two
kicks drift out of phase). When this happens, the beats can be realigned
by simply tapping one of the temporary pitch bend buttons a few times in
the appropriate direction. Now get out there and make Tiesto jealous\!

## Headphone Cueing

Headphone cueing is a technique DJs use to listen to the next track they
want to play in their headphones before playing it out the main
speakers. Mixxx allows a DJ to route audio from either player to their
headphones by toggling either of the "HEADPHONE" buttons located on the
far left/right sides of Mixxx's interface. Headphone cueing is useful
because it allows a DJ to beatmatch the next song in their headphones
before bringing it into their mix by sliding the crossfader.

# Keys and Hardware Controllers

[[/media/mixxx.gif|]]

The shortcuts are defined in a text file, and can be changed by the user
-

Linux: /usr/share/mixxx/keyboard/Standard.kbd.cfg

MacOS X: \<Mixxx bundle\>/keyboard/Standard.kbd.cfg

Windows: \<Mixxx directory\>\\keyboard\\Standard.kbd.cfg

## MIDI Controllers

# Getting Involved

Mixxx is a community-driven project involving many DJs worldwide.
Without the contributions from these DJs, Mixxx would not exist, and
we're constantly looking for more contributors.

FIXME - Ideas for stuff to talk about:

  - Get on IRC\!
  - If you know C++...
  - Take a look at our specs/projects page and see if anything catches
    your eye. If you want to start coding one of these, go right ahead\!
  - We're always willing to mentor and help out new coders
  - Take a look at our bug tracker, try to fix a bug\!
  - Send patches to Adam, Albert, or mixxx-devel\!
  - Help answer questions in the forum
  - Help promote Mixxx - Blog about us, etc.
  - Send us some photos of you using Mixxx at a gig\!
