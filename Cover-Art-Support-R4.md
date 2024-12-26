# Cover Art Support

[Cover Art Support](cover_art_support)

# Report \#4: July 13 - July 19

Last week: [July 06 - July 12](cover_art_support_r3)

## First PR: Qt signal queue

As I explained in the last report, in order to sort out the issues
around the pixmap update, we are now passing the pixmap values in the
signal "pixmapFound(..)". I did some tests and I cannot notice any loss
of performance.

Another important change was to make the "pixmapFound" connection as
Qt::DirectConnection. In this way it will process the signal immediately
and not store copies in an event-queue.

## First PR: id3Tag Crashes (SoundSource)

I faced up to some crashes due to metadata extraction. It occurs mainly
when Mixxx is trying to read a lot of embedded\_covers at the same time.
I realized that Mixxx is getting the info directly from the tag and
trying to convert to QString and it was also the cause of the crashes.

Although calling TStringToQString on a String::null should be safe since
null is just a no-args-constructed String and not an actual NULL
pointer\[1\], my solution was just check if the TString is not-null
(before use it) and it seems to work fine now \[2\] (I did tons of tests
and I did not get segfaults any more).

## First PR: Bug when show/hide wcoverart

Test case:

1.  load Mixxx
2.  select a track (which has a cover)
3.  open wcoverwidget (wcoverart displays cover "A")
4.  switch table view (eg. go to autodj)
5.  open wcoverwidget

<!-- end list -->

  - Expected: displays default\_cover
  - Actual: displays cover "A"

The widget must reset all members after a "switchToView()" \[3\]

## Second PR: Fixes in the TrackInfo dialog

This week I also did many small improvements in the dlgtrackinfo layout
and major changes in the actions of the popup menu (accessed clicking on
the cover art).

**UI**  
\- changing window title - using "Artist - Title" instead of "Title" -
drawing all fields with fixed height (25px) - fixing bugs when the user
resize the window - using cover placeholder as a qwidget instead of
qgroupbox (causing weird behavior on Windows7) ...

**UNSET COVER**  
\- changing the cover location to default\_cover instead of use
coverId=-1. It avoids Mixxx to keep searching for a cover (after unset).

**RELOAD COVER**  
\- now it uses the searching algorithm. It will try to reload the cover
as normally we do (firstly looking in the id3tag and then in the
trackdir).

**ICONS**  
I also added an icon for each action of the popup menu \[4\]. The icons
which I pushed are generics, it means that maybe they are not ideal yet
(design). However, for future changes we just would have to overwrite
the current files.

**OPEN IN FILE BROWSER**  
\- added button to open the current track location in the file browser.

## Second PR: Warning/Question Boxes

Considering that when the user choose "reload" the fields, all of them
are overwritten without any kind of warning... So, we should do the same
for cover\_art reloading. It means that we are no longer using warning
boxes \[5\].

Moreover, in cases when the current track has a cover and the reloading
process return NULL, we do not unset the current cover any more.

## Third PR: Corver Art Delegate

During this week I started to implement the coverartdelegate class,
which is responsible for drawing the cover\_art in the tableview.

This part corresponds to the "third pull request" \[6\] and it is
already working for all features which should display cover arts
(library, autodj, analyse, playlists and crates).

The idea is use paint() to request the pixmaps (from covercache). I
changed the method requestPixmap(..) to return a valid pixmap when it is
available in the pixmapcache (instead of just emit signals). So, paint()
will be doing successive callings until it gets the requested pixmap.

# Issues for the next week

Next week: [July 20 - July 26](cover_art_support_r5)

## Adjust cover art size

Currently we are drawing the cover\_art in the whole cell, so when the
user resize the cover\_art column he will see the cover deforming to fit
in the cell.

I did some research and I saw that Traktor fixed the cover\_art width
(something about 70px) and it is not resized even if the column is
smaller than the image. i think that we should use the same strategy for
that.  
However, it is important to think about how we would rescale (and cut)
the covers because doing it in the paint event (for all pixmaps, all the
time) seems to be a very bad idea, because rescale process might be slow
and doing it in many pixmaps at the same time could bring performance
issues...

## Delaying cover loading

I also noticed that we can have some freezes when we scroll the
tableview very fast (just when the covercache is "cold"). The solution
for that would be using a "delay" as we did for the cover widget last
week.

## Copying covers

If the user changes the cover art and the new cover comes from a
directory which is different from the track directory, Mixxx should copy
it to the track dir, trying to use "cover.jpg" or "album.jpg". If the
dir already have any of these files, we must use "mixxx-cover.jpg" (just
to do not overwrite the user files).

This is important because the user could choose an image from a
removable disk or any another place which could not be available in a
"near future". So, it is much more safe let it together with the track.
It is also good because the user could reuse the cover in other software
(automatic)...

## Switching Views

We must avoid showing the cover\_art widget (left corner) for views
which there is no cove\_art support:

  - browse
  - recordings
  - history
  - rhythmbox
  - banshee
  - itunes

# Links

\[1\]
<https://github.com/taglib/taglib/blob/master/taglib/toolkit/tstring.h#L476>  
\[2\]
<https://github.com/cardinot/mixxx/commit/76ebcd41f51da6361dbb96a782e14c07149f4587>  
\[3\]
<https://github.com/cardinot/mixxx/commit/2b858975a584f8beb1234dcca45c7691a462416b>  
\[4\]
<https://github.com/cardinot/mixxx/commit/ba161332d6a3a9e1fddb6840a13921400d025536>  
\[5\]
<https://github.com/cardinot/mixxx/commit/cce6a05c0fae9f9e2987dc7460e5cd0eb94e2469>  
\[6\] <https://github.com/cardinot/mixxx/pull/2/>
