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

### First week: May 14th to May 20th

During this week I will think about the operations that need to be added
to the base abstract class of every service by checking the various
services that I want to implement. Then I will add a listener class that
will receive the proper signal that a track has been changed and
broadcast it via another signal to all service implementing interfaces.
This will be a very busy week since I have a Bachelor's thesis deadline
and also German finals. Specifically, in **Tuesday 15th** I won't be
able to work at all because I have Bachelor's thesis work during the
morning and German exam in the afternoon. Also, in **Thursday 17th** I
won't be able to work as much because I have another German final in the
afternoon.

### Second week: May 21st to May 27th

Here I will add a basic service interface implementation that will
simply display the current track being played in a file. I will also add
any necessary unit tests and will start looking at the Last.fm scrobbler
API.

### Third week: May 28th to June 3rd

In this week I will start implementing the classes that will have basic
interaction with Last.fm API with Qt's own networking classes perhaps
using Postman or Google test as needed.

### Fourth week: June 4th to June 10th

During this week I will continue implementing and testing the classes
and testing and also think about how to integrate Last.fm into the UI
seeing as the user will probably need to OAuth with Mixxx.

## Proposed deadline goals

### First deadline: 11th June

Since Last.fm API integration will take a while I probably won't have it
ready by the 11th of June. So for this deadline I should have a solid
code base and a proof of concept of a scrobbler in the form of a txt
file.

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
