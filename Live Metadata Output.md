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

Modified as of 3/07/2018.

### First week: May 14th to May 20th

During this week I added the necessary signals to track when a track is
paused, resumed, loaded and unloaded. I also created some timers to
count the played time, necessary to know when a track is scrobbable. I
wrote some tests for the Track object, which was intended to hold this
information.

### Second week: May 21st to May 27th

During this week I moved all the metadata management to a separate
class, instead of the Player Manager, moved the timers away from the
Track object to this class, introduced the total volume as a factor to
take into account besides whether if a track is being played or not and
redid the implementation of the timer to use GuiTick50ms as I was told
the waveforms conflict with the use of QTimer's timeout signal.

### Third week: May 28th to June 3rd

This week I finished the scrobbling manager and wrote some automatic
tests for it. I also started working on the file listener.

### Fourth week: June 4th to June 10th

This week I refactored the file listener into a factory and template to
accommodate for the various file formats admitted by the broadcasting
APPS. I also refactored the scrobbling manager to allow for dependency
injection and changed the isTrackAudible function into a strategy
pattern.

### Fifth week: June 11th to June 17th

I've decided to start with the user settings before programming the API
client that will interact with Last.fm. I wrote a new tab in the user
settings and refactored the file listener so it uses those settings (a
previous version).

### Sixth week: June 18th to June 24th

This week I refactored the metadata settings dialog, deleting the table
view and moved the file settings to a new class. I added a work in
progress concurrency for the file listener and I removed the factory and
template method.

### Seventh week: June 25th to July 1st

This week I refactored the file listener class to use a dedicated thread
and started implementing the ListenBrainz API interaction.

### Eighth week: July 2nd to July 8th

During this week I will wrap up the interaction, solving any bugs,
errors or obstacles that will come up. If I have finished early I will
start the MPRIS interaction by looking at [this github
branch](https://github.com/daschuer/mixxx/tree/mpris) for ideas.

### Ninth week: July 9th to July 15th

During this week I will start implementing the MPRIS interface. If I
haven't looked at the github branch for ideas I will in this week. I
will also talk to the devs to see what ideas they have since I'm told
this is a somewhat popular request. I will use QDBus for this.

### Tenth week: July 16th to July 22nd

During this week I will continue implementing the MPRIS interface.

### Eleventh week: July 23rd to July 29th

During this week I expect to have finished with the MPRIS interface as
well as test how it interacts with other programs.

### Twelfth week: July 30th to August 5th

This week will be dedicated to wrap up the MPRIS interface as well as
solve any bugs or problems that come up.

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
