# Cover Art Support

[Cover Art Support](cover_art_support)

# Report \#3: July 06 - July 12

Last week: [June 29 - July 05](cover_art_support_r2)

## First Pull Request

This week I also pushed some fixes in the first branch.

We realized that using "guiTick50ms" in wtrackis better than
"guiTickTime", because in this way we would get less updates.

I also updated the unit tests to work on Windows.

## Redesign dlgtrackinfo

We found out that the dlgtrackinfo UI is to large to use with displays
that have a height lower then 635px which is most netbooks. In this way,
we would need to do bigger changes because just adding a placeholder
would just increase the dlg height and it must be avoided.

I pushed a sketch and I got some feedback from jus. It helped me a lot
to improve the layout and think about new possibilities.

Ideas and considerations:

1.  ~~Some fields, such as ARTIST, TITLE and ALBUM, need more space to
    show the information, so it has to be alone in a row.~~ (done\!)
2.  ~~The FILENAME field can be dropped. It only contains redundant
    info, since it still available in the LOCATION field.~~(done\!)
3.  It could have a button to open the current track directory in a file
    browser.
4.  \<del\>The main purpose of showing covers in the dlgtrackinfo is to
    have a "brief idea" of which cover is loaded for the track. In this
    way, it should be as small as possible (maybe 70px). So, other
    fields would have more space... \</del\>(done\!)
5.  ~~dlgtrackinfo should have a height lower than 500px.~~ (done\!)
6.  ~~We could move COMMENTS to a new tab.~~ (done\!)
7.  ~~Covers must be drawn in a QWidget or QGroupBox with a fixed size
    to avoid resizing the fields beside.~~ (done\!)

## Load/edit/unset covers in dlgtrackinfo

During the week, basically all main tasks of the second PR were
implemented.

I spent some time to find out what is the best way to show options like
EDIT and UNSET, Initially was thinking about paint a "X" icon when the
mouser is hovering (like we use in wcoverart) and unset the cover if the
user click on it. However, it is a bad idea because we would need to
reimplement mouseEvent() and repaint(), which could bring many issues.
In addition, it was not enough to affect other actions (edit, reload,
...).

Currently, the cover is being loaded as a icon of a QPushButton and it
has a popup menu, which works as a context menu implemented using QMenu.
In this popup menu we have initially actions to EDIT (change location),
UNSET and RELOAD FROM METADATA.

## Reload from Metadata

In order to make it possible, I did some adaptions in the CoverCache,
adding some methods to handle cover changes. Now it works fine and I
also added an action in the popup menu to make users able to reload just
the cover from metadata.

## Warning boxes

There are two cases when a box is showed:

\*\*1 - \*\* a) Some cover is being displayed;

b) User clicks on "reload track from metadata"

c) the displayed\_cover is different from the embedded\_cover (new)

\-\> currently embedded\_cover is our priority, so if the current cover
is different from the embedded\_cover, it is because the user changed it
once... So, if we see that the md5\_hashes are different, we will ask if
he/she want to overwrite the cover...

\*\*2 - \*\* a) Some cover is being displayed;

b) User clicks on "reload track from metadata"

c) the current track does not have an embedded cover

\-\> We are warning that there is no embedded\_cover for the current
track, and we ask if the user want to unset the current one (that was
probably changed manually)...

# Issues for the next week

Next week: [July 13 - July 19](cover_art_support_r4)

## Qt signal queue

In the last week, we stop passing pixmaps in the SIGNAL queue to start
passing it as reference in CoverCache::requestPixmap(...).

When I was working on the "add/edit" stuff, I realized that we can have
some problems with this approach.

For example,

  - user choose a new cover
  - covercache load it and emit pixmapFound(trackId)

expected: all widgets load the same cover (new one)

current: all widgets\&dlgtrackinfo will reload the cover, but just the
dlgtrackinfo show the new cover, because other widgets would continue
pointing to a old pixmap.

As passing pixmaps in the SIGNAL queue is not a big problem, because it
probably will not bring performance issues (since we are using delay), I
think that we should use revert it.

## Redesign dlgtrackinfo

I saw that other softwares follow a different concept in their
"dlgtrackinfo"...

Usually they show just basic info (COVER ART, artist, title and album)
and info that are not editable (duration, bpm, location...) in the
SUMMARY tab. All editable fields are showed in a different tab
(METADATA).

It seems to be a really good strategy to avoid having a big dlg.

I'm waiting for more feedback about this issue, but maybe we should
think about bigger restructuring and do something similar to other
softwares...

## M4A files

Daniel detected that Mixxx crashes when he is trying to load .m4a files.

## Warning boxes

> @Daniel
> 
> I am not sure about the warning when the cover is replaced with the
> embedded cover.
> 
> IMHO this is the same class of information like track name or artist.
> So it should be handled at the same \> way. I have seen some tracks
> riped from CD where the Artist is "Unknown" overwriting the right
> Artist name with \> "Unknown" is the same class of annoyance.
> 
> Please Issue the case if you reload the metadata from many files.

In this way, should we disable all warning/question boxes?

## Third Pull Request

We already have a lot of big and small issues to sort out in the second
PR during the next week. However, it is important think about what comes
after that. In fact we have just more 2 big tasks to complete, which are
implement a new widget to show covers AND make users able to download
covers.
