# Vinyl Control

**NOTE:** This article is about a feature in the **upcoming 1.6.0
release**.

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
preamps (or line-out), and two "sound inputs".

**Setup 2: CDJ** Two timecoded CDs, two CD decks, and two "sound
inputs".

Now, for the "sound inputs", you have two options: You can either use a
fancy DJ soundcard that has multiple stereo line-inputs on it, or can
use two soundcards (each with a single stereo line-in). Currently,
Mixxx's vinyl control has only been tested with the latter
configuration.

For timecoded records or CDs, you can use any of the records supported
by Mixxx:

{| style="width:400px;" border="1" |+ **Timecode Support** \! Vinyl \!\!
Responsiveness |- | Serato CV02 || Very high |- | Serato CD || Very high
|- | Traktor Scratch || High |- | FinalScratch (Standard) || Low |- |
FinalScratch (Scratch) || Medium |- | MixVibes DVS CD || Untested |}

At the present time, **Serato records are the ones you should purchase**
if you're looking to buy vinyl.

Support for Final Scratch records needs work, and at the moment isn't
nearly as good as the Serato/Traktor support.

## How responsive is it?

The responsiveness of Serato/Traktor records is limited only by the
latency of your soundcard. This latency can be adjusted in Mixxx's
preferences under the "Sound Hardware" pane. With a good soundcard which
is properly configured, **latencies below 10 ms are possible**.

## What does it look like in action?

Check out these videos (YouTube):

  - [Mixxx Vinyl Control
    Demo 1](http://www.youtube.com/watch?v=U2ZPSSXlK60)
  - [Mixxx Vinyl Control Demo 2](http://youtube.com/watch?v=9dRLNT2yspg)

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
  - **Linux:** Fire up "Audacity", then follow the instructions below.

Click record and hit play on your turntable. After a few seconds, stop
Sound Recorder and your turntable. Playback the sound that was just
recorded. If you hear a relatively stable tone, your soundcard is
probably capturing the timecode signal correctly. If you don't hear a
tone, check your recording volume mixer and capture settings. Also,
check that your turntable is plugged into the correct plug on your
soundcard.

The last step to try is to launch Mixxx, and go into the "Vinyl Control"
pane in the preferences dialog. Select the soundcard with the turntable
attached to it under "Deck 1", and select the timecode you're using.
Click OK, then in the menu bar at the top, select "Options-\>Enable
vinyl control". Load a track into Mixxx's top player (Player 1) and hit
play on your turntable. Mixxx should begin playing the track in Player
1.

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
