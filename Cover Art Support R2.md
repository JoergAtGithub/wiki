# Cover Art Support

[Cover Art Support](cover_art_support)

# Report \#2: June 29 - July 05

Last week: [June 22 - June 28](cover_art_support_r1)

## Updating cover\_art columns in tableview

As the library.cover\_art column is updated in
TrackDAO::updateCoverArt(), we could just emit the signal "trackChanged"
and it would be enough to let the BaseTrackCache knows that it needs
update the tableview. However, currently BTC is using TIOs to get the
values of each column and as the cover\_art column is not a member of
TIO, it would not be enough.

First implementations of this project was based on the use of TIO, but
we realized that it was bringing many performance issues and that
everything would work much better without it. In this way, we needed
another solution to update the BTC and basically the best idea that we
found was implement a new SIGNAL/SLOT to access
BTC::updateTrackInIndex(int trackId).

<https://github.com/cardinot/mixxx/commit/7b5be7774cbb3d780796a02edd164d4f2ce4ee2b>

## Duplicated covers in cache (MD5 Hash)

As I said last week, the main idea to sort it out would be using md5
hash. The problem is that MD5 calculation can take a long time and it
could bring many performance issues, so we need to avoid doing it as
much as possible.

In this way, the best choice would be doing it just during the
\*search\* and storing it in database. So, now we have a new column in
cover\_cache table (md5) and we also added it in the tableview, avoiding
doing extra queries (as we were doing for cover location).

As all covers have a md5hash, now we are using the md5hash as key for
our covercache (QPixmapCache) instead of doing it using coverLocation,
because just the covers loaded from track directory have coverLocation.
So, we did not need a QHash to maintain the md5 hashes.

## Using a delay when the selection changes very fast

Firstly I thought that it could happens just when the user is holding
down an arrow key. So, the simplest and more efficient solution that I
found was to use the \*keyevent\* and \*keyeventrelease\* to check if
the user is holding the arrow key and it would be enough to handle the
loadCoverArt signal.

However, \*daschuer\* showed me that it would not work for Midi mapping.
<https://github.com/mixxxdj/mixxx/blob/831a1450a70ea5d19b6a44fed6b6eb71d8ba9d0b/res/controllers/Hercules-DJ-Console-Mk4-scripts.js#L59>

Thus, a better approach would be using some kind of timer to know if the
user is "stopped" in the same row for a definite time (I chose 0.1s).
And it's also more efficient because it ensures that we'll only call
loadCoverArt() after finish quick selections.
<https://github.com/cardinot/mixxx/commit/ab39f640619116c7ac07b21168e991aa9b121470>

## Remove pixmap from pixmapFound() signal

In order to avoid loading heavy pixmaps in the QT signal queue, the
pixmap is being passed as reference in CoverCache::requestPixmap().

## Unit test

After the changes in the "loading and searching" steps due to the
implementation of the md5hash, all tests were reviewed to make that
everything was working properly. I also add some tests for the md5hash.

As now we are using the “album” and “base track” names to try finding a
cover, I also added a test to check if everything works with UTF8 chars.

## Redesign dlgtrackinfo to show covers

As all other info about a track, the editions of covers will also be
done in dlgtrackinfo. The problem is that the current layout is not
ideal, because usually small screens (netbooks) have a very low height
(600px) and now it has 635px, which is already too long and awful for
these users. In this way, I think that the best thing to do is redesign
the layout and try using more "width" instead of "height" (as other
softwares do).

It's also the first issue for the second pull request.
<https://github.com/cardinot/mixxx/commits/coverArtSupport_2>

# Issues for the next week

Next week: [July 06 - July 12](cover_art_support_r3)

## Second pull request

  - redesign dlgtrackinfo to show covers
  - load cover in dlgtrackinfo
  - edit cover in dlgtrackinfo
  - warning box for “reload metadata” action

### Warning box for “reload metadata” action

if user reload id3tags from file, and it has a different cover from the
current cover, we could use a simple warning box to ask if the user
really want to reload the cover art from id3tag. We could also show both
covers in this box.
