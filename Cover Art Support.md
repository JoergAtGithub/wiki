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
  - md5 hash (avoids duplication)
  - avoids showing cover widget for not supported features:
  - banshee
  - browse
  - itunes
  - recordings
  - rhythmbox
  - traktor

<!-- end list -->

  - <https://github.com/cardinot/mixxx/tree/coverArtSupport>
  - <https://github.com/mixxxdj/mixxx/pull/278>

#### Second Pull Request

  - redesign dlgtrackinfo to show covers
  - load cover in dlgtrackinfo
  - change cover location in dlgtrackinfo
  - unset cover (load default)
  - reload cover art
  - warning box issue
  - icon for each cover\_art action
  - copy cover from external dir to track dir (if the user changes the
    cover)

<!-- end list -->

  - <https://github.com/cardinot/mixxx/tree/coverArtSupport_2>
  - <https://github.com/cardinot/mixxx/pull/1>

#### Third Pull Request

  - add cover\_art column in Library feature
  - add cover\_art column in AutoDJ feature
  - add cover\_art column in Analyze feature
  - add cover\_art column in Playlists feature
  - add cover\_art column in Crates feature
  - adjust cover art size
  - delay cover loading when the user is scrolling fast
  - batch updates (avoiding doing many writes in a short time)

<!-- end list -->

  - <https://github.com/cardinot/mixxx/tree/coverArtSupport_3>
  - <https://github.com/cardinot/mixxx/pull/2>

#### Fourth Pull Request

  - basic UI to download and show covers (dlgcoverartfetcher)
  - download covers from Last.fm

<!-- end list -->

  - <https://github.com/cardinot/mixxx/tree/coverArtSupport_4>
  - <https://github.com/cardinot/mixxx/pull/3>

## Reports

  - [June 22 - June 28](cover_art_support_r1)
  - [June 29 - July 05](cover_art_support_r2)
  - [July 06 - July 12](cover_art_support_r3)
  - [July 13 - July 19](cover_art_support_r4)
  - [July 20 - July 26](cover_art_support_r5)
  - [July 27 - August 02](cover_art_support_r6)
  - [August 03 - August 09](cover_art_support_r7)
