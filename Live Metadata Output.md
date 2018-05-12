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
and also German finals.

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
