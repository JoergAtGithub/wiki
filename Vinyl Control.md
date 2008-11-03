# Vinyl Control

## What is it?

Vinyl control allows a user to manipulate the playback of a song in
Mixxx using a turntable as an interface. In effect, it simulates the
sound and feel of having your MP3 collection on vinyl.

## How does it work?

Vinyl control uses special timecoded records which are placed on real
turntables. The audio output of the turntables is plugged into a
computer, on which Mixxx is running. When a record is played on one of
the attached turntables, Mixxx decodes the timecode off the record, and
uses information from that to manipulate whatever song is loaded.

For those more technically inclined, Mixxx uses
[Scratchlib](http://www.9elements.com/scratchlib/) to decode the
FinalScratch timecode and [xwax](http://www.xwax.co.uk/) to decode the
Serato/Traktor timecodes.

## What do I need to use it?

It's possible to use Mixxx's vinyl control with several hardware setups,
but the basic ones are:

**Setup 1: Vinyl DJ** Two timecoded records, two turntables with phono
preamps (or line-out), and two "sound inputs". You can skip the phono
amplifiers if you use the snazzy new software preamp in Mixxx, though
this will not provide as clean a signal and may not work for everyone -
line-level signals are preferred.

**Setup 2: CDJ** Two timecoded CDs, two CD decks, and two "sound
inputs".

Now, for the "sound inputs", you have two options: You can either use a
fancy DJ soundcard that has multiple stereo line-inputs on it, or can
use two soundcards (each with a single stereo line-in). Currently,
Mixxx's vinyl control has only been tested with the latter
configuration. Currently (2008-03-03) running both inputs through the
one soundcard does not work, it will cause the song to drift randomly.
(tested on Linux/SVN-2008-02-29/M-Audio Delta 1010LT\[envy24\])

**For best scratch performance** with vinyl control, your system must be
able to handle setting the latency to **10ms or less** otherwise the
scratch sound will start to become distorted as latencies (and lag time)
increase.

For timecoded records or CDs, you can use any of the records supported
by Mixxx:

**Timecode Support**

|                         |                |
| ----------------------- | -------------- |
| Vinyl                   | Responsiveness |
| Serato CV02             | Very high      |
| Serato CD               | Very high      |
| Traktor Scratch         | Very high      |
| FinalScratch (Standard) | Moderate       |
| FinalScratch (Scratch)  | High           |
| MixVibes DVS CD         | Untested       |
| MixVibes DVS Vinyl      | Does not work  |

At the present time, **Serato records are the ones you should purchase**
if you're looking to buy vinyl. If you want to use CDs, you can
**download a free copy** from Rane
[here](http://rane.com/scratchlivecontrol.zip). (Information is on
[this](http://rane.com/scratch.html) page.)

Support for Final Scratch records needs work, and at the moment isn't
nearly as good as the Serato/Traktor support.

## How responsive is it? Does it have absolute mode?

The responsiveness of Serato/Traktor records is limited only by the
latency of your soundcard. This latency can be adjusted in Mixxx's
preferences under the "Sound Hardware" pane. With a good soundcard which
is properly configured and a fast CPU, **latencies below 10 ms are
possible**.

Mixxx supports **absolute** and **relative** mode with all of the vinyl
listed in the table above.

## What does it look like in action?

Check out these videos (YouTube):

  - [Mixxx Vinyl Control
    Demo 1](http://www.youtube.com/watch?v=U2ZPSSXlK60)
  - [Mixxx Vinyl Control Demo 2](http://youtube.com/watch?v=9dRLNT2yspg)
  - [Mixxx Vinyl Control Demo 3 -
    Scratching](http://www.youtube.com/watch?v=nAqI4HAcQi4)

(Need more YouTube videos here, and a screenshot of the prefs dialog)

## Troubleshooting

The downside to vinyl control is that it adds an extra layer of
complexity to troubleshooting - Now there's a pair of turntables to
worry about in addition to software problems.

To begin troubleshooting any problems you have, please do the following:

  - Make sure your needles are clean and your records are relatively
    dust-free. (Dirty needs will cause Mixxx to playback irregularly.)
  - Make sure your left and right RCA cables are plugged into the
    correct plugs. A swapped pair of RCA cables will cause Mixxx to also
    behave strangely, such as play songs in reverse.
  - Make sure your tonearm is balanced. 
  - Make sure your soundcards have stereo line-in. Many on-board
    soundcards only have mono line-in and won't function correctly with
    vinyl control. Before you buy any soundcard, verify that it has
    stereo line-in on it.
  - Make sure the recording volume is turned up in your soundcard's
    volume mixer. Too quiet of a signal can result in pitch control
    being inverted.
  - Make sure you don't have 50/60 Hz ground-loop hum. Ground your
    turntables to your amp/mixer. Ground-loop hum can cause choppy
    playback and otherwise unpredictable behaviour.

Next, verify that the signal is being received by your computer
properly.

  - **Windows:** Fire up "Sound Recorder" from
    Start-\>Programs-\>Accessories-\>Entertainment, then follow the
    instructions below. 

Click record and hit play on your turntable. After a few seconds, stop
Sound Recorder and your turntable. Playback the sound that was just
recorded. If you hear a relatively stable tone, your soundcard is
probably capturing the timecode signal correctly. If you don't hear a
tone, check your recording volume mixer and capture settings. Also,
check that your turntable is plugged into the correct plug on your
soundcard.

  - **Linux:** Grab a copy of [xwax](http://www.xwax.co.uk/), then
    follow the instructions below. (If you want to use a sound editor
    like [Audacity](http://audacity.sourceforge.net/), follow the
    Windows instructions above.)

Start xwax with the -t option set for the type of timecode vinyl/cd
you're using, -l for the path to your music files, and -d for the sound
device your deck is hooked to. (E.g. xwax -t serato\_cd -l
\~/MusicFiles/ -d /dev/dsp ) [More
info](http://www.xwax.co.uk/guide.html). Now just start your record/CD
and watch the timecode scope (crosshairs) in the upper right corner. You
should see a healthy double-circle display. Adjust the input levels
using a mixer control for the device (eg. alsamixer). When settled, the
circle should approximately fill the timecode scope display but not be
cut off. (If you don't see anything, check the mixer program to be sure
the Line input is selected/enabled and turned up.)

**For both:** The last step to try is to launch Mixxx, and go into the
"Vinyl Control" pane in the preferences dialog. Select the soundcard
with the turntable attached to it under "Deck 1", and select the
timecode you're using. Click OK, then in the menu bar at the top, select
"Options-\>Enable vinyl control". Load a track into Mixxx's top player
(Player 1) and hit play on your turntable. Mixxx should begin playing
the track in Player 1.

## How can I help?

If you're interested in adding support for more timecode records, your
effort is best spent contributing to [xwax](http://www.xwax.co.uk/). Any
additional timecode support added to xwax will be included in Mixxx. If
you're interested in fixing some of the quirks that happen or adding
extra features to the vinyl control support in Mixxx, email
[Albert](/mailto/gamegod@users.sf.net) and he can help you get started
working Mixxx's vinyl control code.

## Links

  - [xwax](http://www.xwax.co.uk/)
  - [Scratchlib](http://www.9elements.com/scratchlib/)
  - [Digital-Scratch](http://home.gna.org/dscratch/en_index.html)
  - **[Mixxx Download Page](http://mixxx.org/download.php)**
