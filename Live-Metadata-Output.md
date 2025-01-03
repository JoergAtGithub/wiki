# Live metadata output

Author: David Hernández (davidhm)

Email: <david.hm.1994@gmail.com>

## GSoC 2018 recap

Working in this community has been a lot of fun. It has given me
valuable experience in coding on collaborative projects. Previously,
almost all my work has been individual or with a group of 4/5 students,
but it has never been of this scale. I've learned about the way open
source projects work, with pull requests, code review, bug tracking,
etc. and I've deepened my knowledge of C++ and the Qt framework. I've
also learned that IDEs are invaluable when it comes to handling this
scale of code otherwise it becomes cumbersome to navigate and read the
necessary code.

I thank my mentor @daschuer for his help, especially for his comments on
the code and the patience to deal with my schedule issues. Overall, it's
been an intense project, but a rewarding one. Coding is always fun, but
it is yet more fun when you see the (hopefully correct) results of your
code.

### Work done

Further below the original proposal with the full details of the project
is found. The whole code is in the following github pull request:

<https://github.com/mixxxdj/mixxx/pull/1675>

In hindsight, perhaps the pull request should have been split in several
PRs to keep comments and reviews of the code focused on only one topic.

### Future work

Clearly, one of the things that remains to be done is the Last.fm API,
which I will finish when I find the time. Beyond that, perhaps what
needs to be done is further testing with more broadcasting products
suggested in <https://bugs.launchpad.net/mixxx/+bug/1775095> and mantain
the code generated.

## Original proposal

In this project I will write the code foundation that will broadcast the
tracks currently being played in the Mixxx app to various services
(online or not) dedicated to compile this information and display it for
everyone. First I will implement a proof-of-concept text file displaying
the current track. Then I will work on a [Listenbrainz
listener](https://listenbrainz.org/). Afterwards, I will make a [MPRIS
broadcaster](https://specifications.freedesktop.org/mpris-spec/latest/)
with [QtDbus](http://doc.qt.io/qt-5/qtdbus-index.html) so that other
apps can receive this info. I originally intended to include a Last.fm
API scrobbler but I didn't have the time.

### Proposed schedule

Modified as of 16/07/2018.

#### First week: May 14th to May 20th

During this week I added the necessary signals to track when a track is
paused, resumed, loaded and unloaded. I also created some timers to
count the played time, necessary to know when a track is scrobbable. I
wrote some tests for the Track object, which was intended to hold this
information.

#### Second week: May 21st to May 27th

During this week I moved all the metadata management to a separate
class, instead of the Player Manager, moved the timers away from the
Track object to this class, introduced the total volume as a factor to
take into account besides whether if a track is being played or not and
redid the implementation of the timer to use GuiTick50ms as I was told
the waveforms conflict with the use of QTimer's timeout signal.

#### Third week: May 28th to June 3rd

This week I finished the scrobbling manager and wrote some automatic
tests for it. I also started working on the file listener.

#### Fourth week: June 4th to June 10th

This week I refactored the file listener into a factory and template to
accommodate for the various file formats admitted by the broadcasting
APPS. I also refactored the scrobbling manager to allow for dependency
injection and changed the isTrackAudible function into a strategy
pattern.

#### Fifth week: June 11th to June 17th

I've decided to start with the user settings before programming the API
client that will interact with Last.fm. I wrote a new tab in the user
settings and refactored the file listener so it uses those settings (a
previous version).

#### Sixth week: June 18th to June 24th

This week I refactored the metadata settings dialog, deleting the table
view and moved the file settings to a new class. I added a work in
progress concurrency for the file listener and I removed the factory and
template method.

#### Seventh week: June 25th to July 1st

This week I refactored the file listener class to use a dedicated thread
and started implementing the ListenBrainz API interaction.

#### Eighth week: July 2nd to July 8th

This week I finished the ListenBrainz interaction and fixed the metadata
preferences tab.

#### Ninth week: July 9th to July 15th

This week I started implementing the MPRIS interface. It took a while
because Qt's DBus implementation is incomplete and I didn't realize.

#### Tenth week: July 16th to July 22nd

This week I wrote a dedicated class to implement the MPRIS
MediaPlayer2Player logic.

#### Eleventh week: July 23rd to July 29th

This week I finished the MPRIS implementation.

#### Twelfth week: July 30th to August 5th

This week I refactored the code to meet some propositions on github as
well as simplifying implementations and changing UIs.

## Proposed deadline goals

### First deadline: 11th June

For this deadline, I will have a solid code base and a proof of concept
of a scrobbler in the form of a txt file.

### Second deadline: 9th July

For this deadline, I will have the full interaction with the
ListenBrainz API. Including the option added to the preferences, the
authentication process and the uploading of the scrobbles. As well as
solving any bugs that come up.

### Third deadline: 6th August

For this date, I will have finished the interaction with the MPRIS
interface, and if I have time I will implement a Last.fm interaction.

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
[2nd
week](http://lkese3ker.blogspot.com/2018/05/week-2-21st-may-27th-may.html)  
[3rd
week](http://lkese3ker.blogspot.com/2018/06/week-3-28th-may-3rd-june.html)  
[4th
week](http://lkese3ker.blogspot.com/2018/06/week-4-4th-june-10th-june.html)  
[5th
week](https://lkese3ker.blogspot.com/2018/06/week-5-11th-june-17th-june.html)  
[6th
week](http://lkese3ker.blogspot.com/2018/06/week-6-june-18th-to-june-24th.html)  
[7th
week](http://lkese3ker.blogspot.com/2018/07/week-7-25th-june-1st-july.html)  
[8th
week](http://lkese3ker.blogspot.com/2018/07/week-8-2nd-july-8th-july.html)  
[9th
week](http://lkese3ker.blogspot.com/2018/07/week-9-9th-july-15th-july.html)  
[10th
week](http://lkese3ker.blogspot.com/2018/07/week-10-23th-july-29th-july.html)  
[11th
week](http://lkese3ker.blogspot.com/2018/07/week-11th-23th-july-29th-july.html)  
[12th
week](http://lkese3ker.blogspot.com/2018/08/week-12th-30th-july-5th-august.html)
