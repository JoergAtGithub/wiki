# Cover Art Support

## Abstract

Currently Mixxx does not give any cover art support and this may be
considered a disadvantage for some users due to the fact that it greatly
facilitates the searches of albums and tracks, moreover most of the
other softwares already offer this feature.

I realize that generally people tend to associate this project to
something purely decorative, where the focus is on just think about a
good place to put the cover on the interface, but this is wrong because
have a good interface where covers can not be loaded correctly and
quickly is worse than does not support covers. So the main idea is to
focus on this part, doing tests to be sure that it is working as
expected.

## Requirements

  - Supporting loading cover art (from metadata tags, from cover images
    in album directories, etc.)
  - Deciding where and how to display the cover art in the GUI. 
  - Downloading cover art from metadata sources on the Internet if it is
    not available locally.

Links to Launchpad bugs:

  - <https://bugs.launchpad.net/mixxx/+bug/661459>
  - <https://bugs.launchpad.net/mixxx/+bug/890421>
  - <https://bugs.launchpad.net/mixxx/+bug/1015894>

## General Design Overview

### Cover Scan

Doing cover art scan during the library scan would be a good solution
for new users, however, it could be a pain for existing users, mainly if
the user has a big library, because it would be a very slow process and
most of these users would not be able to see the covers.

Thus, the idea is doing it "on-demand". It means that we would be
searching for covers that the user want to see and it will make our
project works for any kind of user in a way where they would not need to
do new inputs (setting something or doing a new library scan) to start
to see the covers. Everything would start to appear automatically.

### User Interface

The most important point is that the users must be able to choose easily
if they want (or not) to see the covers (on/off), just because if an
user does not have covers or does not care about it, they would likely
turn it off.

The best ways to show covers are:

#### Cover Flow

Advantages

\- It is fashionable - many users like it - it has a modern visual

Disadvantages

\- It could take up much space

Where and how

\- Horizontal or vertical position - LibQxt and pictureflow

Examples

\- VirtualDJ \[<http://i.imgur.com/wXOXQii.png?1>\]

#### Grid View

Advantages

\- It's clean - It's easier to find a cover, because the user can see
everything in a good size.

Disadvantage

\- It may be awful depending on monitor size and amount of tracks.

How and where

\- We need change the current layout of our table view - User could
change the cover size

Examples

\- Serato \[<http://i.imgur.com/aJNCeCz.jpg>\]

\- Banshee \[<http://i.imgur.com/Opo1ZVG.png>\]

#### List View + Cover below directories list

Advantages

\- It's clean - It's good because it doesn't bring any sudden change in
the current layout of our table view.

Disadvantage

\- It may be awful when you want mainly look at covers, because the list
will show just about 30% of the image. - Use the tree view space to show
covers would be a pain for smaller screens (as in netbooks), but it's
not a big problem because we could have a simple enable/disable button.

Where and how

\- Show about 30% always (as Traktor) - Show about 30% and increase to
45% when hover - Show about 30% and open a pop-up when hover (as
MixViber)

Examples

\-Tracktor \[<http://i.imgur.com/qB8eo0o.png?1>\]

\-MixViber \[<http://i.imgur.com/Fi912Ne.png?2>\]

## Work Breakdown

### General Overview

1.  Implement cover scan - storing/loading covers;
2.  Minimal/basic UI - displaying full cover art below directories list;
3.  Improvements in dlgtrackInfo to add/edit a new cover art;
4.  Implementation of search engine (using some API to download covers);
5.  Improving GUI - more options of layout.

This year the idea is have a fast integration of GSOC contribuitions. It
means that we will split the project in smaller tasks, grouping them to
be able to do fast pull requests on Github.

#### First Pull Request

  - implement database scheme
  - search for embedded cover
  - search for cover in track directory
  - minimal ui (display covers in lower left corner)
  - handle existing users
  - LRU cache
  - unit tests

<!-- end list -->

  - <https://github.com/cardinot/mixxx/tree/coverArtSupport>

## Reports

### June 22 - June 28

According to the plan of splitting the project into smaller parts, to be
able to perform quick interactions and consequently better integration
of the source code, this week many code reviews were done, which
provided significant improvements to the project.

The main changes that we have done during this week:

#### Removing the disk-cache logic

In the past week, we were storing all the covers in a folder into the
Mixxx settings path. It was working fine and it also allowed us to
handling images without doing changes in the track directory (add or
modifying files).

However, we noticed that in most cases we would not need to handle the
covers and in this way we would be doing just copies and it does not
make sense, mainly in cases when the source cover is already in a
accessible directory. In addition, we noticed that getting the Qimage
from the SoundSource (embedded cover) is much faster than loading it
from a location.

Thus , the question is “why do not access it directly (for both
cases)?”. We realized that did not make sense maintain the disk-cache
for it. Maybe it could be useful in a near future, when we start to
download covers, but we know that even in this cases, the user could
expect to see the downloaded cover into the track directories to make
them able to reuse the cover in other software.

#### Improvements in the working thread

Currently we are doing all loading and searching via QtConcurrent,
because both processes are very slow and they could easily block the
main thread, affecting the performance and freezing Mixxx. So, we also
did several improvements in the logic for setting up and starting a new
thread, having one QFuture for searching and other for loading the
covers from tracks that already have a valid cover location to be
loaded.

#### Rescaling big covers

The cost of the pixmaps inserted into the QPixmapCache is calculated
from the image size. It means that if we try loading big images, it
could be deleted from QPixmapCache immediately.

In order to sort it out, we are rescaling the big covers before saving
it on covercache. As the current widget and even the other ones that we
are going to implement from the next PR will display the images in a
small place, rescaling covers is always a good strategy to make things
work better.

Currently we avoid using covers with more than 400px of width (or
height). However, it seems that we could use a smaller number to make
them lighter. The rescaling process can be very slow in some cases, but
it's not a problem for us, because we are running it in our working
thread.

#### Loading and searching

After changing the way in which we load covers, in order to always
prefer loading metadata, now we are following this strategy:

1.  try loading the stored path in DB
2.  look for embedded cover in file metadata
3.  look for cover stored in the track directory

#### Searching in track directory

Before that, we were just sorting all files by size and getting the
lighter image. It's a very inefficient strategy, because a directory
could have many images which do not represent a cover art. Actually
other softwares which providing cover art support already follow a logic
strategy to store and load covers by the name of these files. So, to
make it more efficient, we work on a list of favorite cover names,
ordering decreasingly by importance.

Current strategy:

1.  if the trackDir has just one image, we get it
2.  %track-file-base%.jpg in the track directory for
    %track-file-base%.mp3
3.  %album%.jpg
4.  cover.jpg 
5.  front.jpg
6.  folder.jpg
7.  anything else found in the folder (getting the lighter one)

#### Unit tests

Currently the main classes which provide the cover art support are
"CoverArtDAO" and "CoverArtCache".

##### CoverArtDAO\_test

For this class was performed a test for each one of the current methods
that we have implemented.

  - CoverArtDAO::getCoverArtId
  - CoverArtDAO::saveCoverArt
  - CoverArtDAO::deleteUnusedCovers
  - CoverArtDAO::getCoverInfo

##### CoverArtCache\_test

The main objective of the class "CoverArtCache" is of loading and
searching covers, in this way, this week the following tests were made:

  - loading cover from path stored in DB (loadImage)
  - Cover Scan (check preference list)
  - searching in empty directory;
  - searching in directory with just one image;
  - %track-file-base%.jpg in the track directory for
    %track-file-base%.mp3
  - %album%.jpg
  - cover.jpg
  - front.jpg
  - folder.jpg
  - anything else found in the folder (getting the lighter one)
  - what is chosen when cover.jpg and cover.JPG exists? (we must get the
    lighter one)

Actually I did not added a test for embedded covers because SoundSource
is the class responsible for doing it.

#### Issues for the next week

##### Updating cover\_art column of tablemodels

Currently we are getting the cover location of a track directly from the
tablemodel. It is a nice strategy because we avoid doing extra queries.
The problem is that we just get this value once (during the table
construction) and even if we update the DB with a new cover location,
the table model will keep sending the value that it loaded in the first
time.

##### Duplicated cover in cache

After removing the disk-cache, we noticed that the current strategy for
tracks where the image is saved in the id3tag does not look good. Using
this approach we would be loading the same pixmap in our qpixmapcache
most of time (because in general tracks of the same album will have the
same picture).

In order to sort it out, we could:

  - calculate a md5 hash \[1\] in our working thread after finish the
    searching step;
  - add a new column in cover\_art table (database) to store the md5
    hash;
  - maintain a qhash \[2\] with the covers that we have on cache.

\[1\] <http://qt-project.org/doc/qt-5/QCryptographicHash.html>

\[2\] <http://qt-project.org/doc/qt-4.8/qhash.html>

##### Using a delay when scrolling very fast

Last week, @daschuer said that he was getting a bad performance when he
was scrolling very fast. It is a issue still? Should we use a delay?

##### First PR

After finishing all issues that I mentioned above, we could close this
branch and start working in a new one. The initial plan was have it
merged, but as the 1.12 version will have a later release it will not be
possible. So, we could just keep working on the same strategy, freezing
the first branch. It would be good because the first PR already is very
big.

##### Next PR

In the next week, we are going to start a new branch, which will have
the implementation of "cover add/edit" as the main goal.

Initial tasks:

  - displaying the cover in dlgtrackinfo
  - making the user able to choose a cover
