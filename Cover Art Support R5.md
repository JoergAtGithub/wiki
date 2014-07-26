# Cover Art Support

[Cover Art Support](cover_art_support)

# Report \#5: July 20 - July 26

Last week: [July 13 - July 19](cover_art_support_r4)

## Handling unsupported features

As I explained last week, the cover art project must be disabled for
some features. After some research and discussions with other
developers, I notice that the best solution so far would be having a
signal "enableCoverArtDisplay(bool)" in the active() method of all
features. As this method is called always when the user switch the views
(loading a new view) it is working fine now.

**Supported features**  
\* analysis  
\* auto dj  
\* crates  
\* library  
\* history  
\* playlist  
**Non-supported features:**  
\* banshee  
\* browse  
\* itunes  
\* recording  
\* rhythmbox  
\* traktor  

## Bug with database schema

Currently we are identifying covers by looking for md5hash and it must
be unique (obvious reasons).

In cases when the user overwrite the cover file in the trackdir, it will
have the same location but an different md5hash. In this way, COVERDAO
would try to store the new cover (new md5hash) but it would not be
possible since it would have the same location as the old image... so,
as the md5hash already is unique, we do not need to maintain unique
locations as well...

New revision:

``` xml
  <revision version="24" min_compatible="3">
    <description>
      Add cover art support
    </description>
    <sql>
      CREATE TABLE IF NOT EXISTS cover_art (
    id INTEGER primary key AUTOINCREMENT,
    location TEXT,
    md5 TEXT UNIQUE
      );
      ALTER TABLE library ADD COLUMN cover_art INTEGER;
    </sql>
  </revision>
```

## Second PR

Some improvements done during the week:

**Copying covers**  
As I pointed out last week, it was important keep all new covers (chosen
by the user) in the track directory. So, now Mixxx will check if the new
cover comes from an external directory and decide if it have to be
copied to the track directory.

**Redesign dlgtrackinfo**  
It is very important that all fields have the same vertical spacing. I
noticed that the only way to ensure it is drawing all fields in the same
box\_layout and it had an excessive number of them which could cause
some bugs on Windows. Now it is also loading the covers on the right
side.

**Bug when showing smaller covers**  
The QPushButton will rescale just covers which are bigger than the icon
bounds, so it is important rescale all of then to ensure that it will
always use as much space as possible...

## Third PR

This week I also spent a lot of time studying the best ways to load the
covers in the table view. Actually it was working since the last week
(coverdelegate), however it had many issues yet. So, I did several
improvements in the CoverArtDelegate and I do not see any performance
issue any more...

### Adjust cover art size

Now it is cropping the covers in a working thread and storing them into
the PixmapCache. It is being done in the CoverArtCache class and a new
parameter (croppedPixmap) was added to the requestPixmap method.

Basically, if the request comes from CoverDelegate (table view), it'll
want to get a cropped cover which is ready to be drawn in the table view
(cover art column).

It's very important to keep the cropped covers in cache because it
avoids having to rescale+crop it ALWAYS (which brings a lot of
performance issues).

### Delaying cover loading

I extended the same logic that was used to delay covers for the cover
widget to also delay the coverdelegate loading... Basically, now we have
a member to lock/unlock coverdelegate calls.

Obviously, as the CoverDelegate calls are done when a new row is painted
(always) it is be very dangerous when the user scroll very fast, because
many requests would be done at the same time... So, now it is also
delaying covers (search and loading) when the user is scrolling (it
means that while the user is scrolling, the table view will show just
covers which are already in the pixmapcache)...

If the CoverDelegate is locked, it must not try to load and search
covers. It means that in this cases it will just draw covers which are
already in the PixmapCache.

## Fourth PR: Downloading Covers

This week I also spent a lot of time studying some APIs to download
covers. The good point is that the best available APIs use a very
similar logic to request and reply the queries. In this way, we could
put more effort in just one API and spend more time working on the new
dialog (dlgcoverfetcher). After that we could analyse if we would need
to integrate other API, but it would be much easier...

Initially my plan is download covers from **Last.fm**. I found a nice
library which could make this integration a bit easier (liblastfm),
however I noticed that is possible do the queries (that we need for this
purpose) just using some Qt functions and it is very nice because it
avoids having to add new dependencies to Mixxx.

Now the **Last.fm** search is already working and I also implemented a
initial layout to show the results.

<https://github.com/cardinot/mixxx/tree/coverArtSupport_4>

# Issues for the next week

Next week: [July 27 - August 02](cover_art_support_r6)

## Downloading from Last.fm

Although it is already working, it needs more work around the download
management. It is using a QMap to store the search results, but it makes
necessary doing many iterations to handle the results. A better approach
would be having a simple list to store just the urls (download queue)...

## DlgCoverArtFetcher

The current layout is very basic and it has already many issues with the
table view. It should also display the search status
(error/no\_results/searching/...).

## Other issues

**Saving downloaded covers**  
After a search, all covers are downloaded and stored as a pixmap in a
list. If the user choose any of them, we just need to store it as a file
into the track directory. So, it could use the same logic that we are
using when the user change the cover with the file browser...

**Fetching missing covers**  
Should we have an option in the context-menu to auto fetch covers? (as
we have for tags)

**Automatic downloads**  
Should we have an option to enable/disable automatic download for
missing covers?
