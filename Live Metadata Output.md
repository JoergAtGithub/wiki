# Live metadata output

In this project I will write the code foundation that will broadcast the
tracks currently being played in the Mixxx app to various services
(online or not) dedicated to compile this information and display it for
everyone. First I will implement a proof-of-concept text file displaying
the current track. Then I will work on a [Last.fm
scrobbler](https://www.last.fm/home). Afterwards, I will write a
[Listenbrainz listener](https://listenbrainz.org/). And lastly, if I
have time, I will make a [MPRIS
broadcaster](https://specifications.freedesktop.org/mpris-spec/latest/)
with [QtDbus](http://doc.qt.io/qt-5/qtdbus-index.html) so that other
apps can receive this info.

## Proposed schedule

Modified as of 29/05/2018.

### First week: May 14th to May 20th

~~ During this week I will think about the operations that need to be
added to the base abstract class of every service by checking the
various services that I want to implement. Then I will add a listener
class that will receive the proper signal that a track has been changed
and broadcast it via another signal to all service implementing
interfaces. This will be a very busy week since I have a Bachelor's
thesis deadline and also German finals. Specifically, in **Tuesday
15th** I won't be able to work at all because I have Bachelor's thesis
work during the morning and German exam in the afternoon. Also, in
**Thursday 17th** I won't be able to work as much because I have another
German final in the afternoon.~~

During this week I added the necessary signals to track when a track is
paused, resumed, loaded and unloaded. I also created some timers to
count the played time, necessary to know when a track is scrobbable. I
wrote some tests for the Track object, which was intended to hold this
information.

### Second week: May 21st to May 27th

~~Here I will add a basic service interface implementation that will
simply display the current track being played in a file. I will also add
any necessary unit tests and will start looking at the Last.fm scrobbler
API.~~

During this week I moved all the metadata management to a separate
class, instead of the Player Manager, moved the timers away from the
Track object to this class, introduced the total volume as a factor to
take into account besides whether if a track is being played or not and
redid the implementation of the timer to use GuiTick50ms as I was told
the waveforms conflict with the use of QTimer's timeout signal.

### Third week: May 28th to June 3rd

During this week I will finish and make sure that the Listener class,
which listens for paused and resumed events and polls the volume of the
tracks, works.

### Fourth week: June 4th to June 10th

During this week I will hopefully have finished with the Listener class,
which will give me some time to write a proof of concept of the service
interface with the writing of a file. This will leave the project ready
for the evaluation.

## Proposed deadline goals

### First deadline: 11th June

For this deadline I should have a solid code base and a proof of concept
of a scrobbler in the form of a txt file.

## Project outline

Here's a rough outline of the intention of the project. This is far from
complete.

[[/media/gsoc_2018/livemetadataoutline.jpg|livemetadataoutline.jpg]]

A track counts as a new listen when:

  - The track has a duration greater than 30 seconds and has been
    listened to (through master, see definition of audible below) for
    half of its duration or 4 minutes, whichever is shorter. This played
    time is paused while the song is not audible. And it gets reset if
    the track is unloaded.
  - The time between the last unload and the current load of the track
    is greater than 5 minutes. Not counting application resets (it is
    assumed that the user will not keep restarting the app and playing
    the same track over and over again).

A track is audible if its final volume is above 20% (including pregain
and faders).

For the "now listening" signal (i.e much less restrictive than the full
listen), every second the track with the most overall volume is the one
selected.

## Weekly blog

[1st
week](http://lkese3ker.blogspot.com.es/2018/05/week-1-14th-may-20th-may.html)
