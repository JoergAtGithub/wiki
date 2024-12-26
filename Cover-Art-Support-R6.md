# Cover Art Support

[Cover Art Support](cover_art_support)

# Report \#6: July 27 - August 02

Last week: [July 20 - July 26](cover_art_support_r5)

## Performance Improvements

This week I spent a lot of time doing some performance tests. Although
everything was already working, it was easy to notice that we still had
some lags especially with the "tracktor view", which is implemented in
the third branch \[1\].

Most problems were happening during the first time that a cover was
being loaded (full loading and searching process), but in fact lags
could happen anytime...

I found out that was possible use the GProf and Valgrind outputs with
some softwares such as KCachegrind to profile data visualization and it
helped me a lot to identify some bottlenecks and improve the code.

So, many big and small changes were done and I'll summarize just the
ones that caused more effect...

**CoverArtDelegate::paint()**

Obviously, this method is called very often and for this reason even a
small calculation done into this method would affect directly the UI
performance. So, I removed as much code as possible from this method in
order to make it lighter to avoid blocking the main UI. I noticed that
it was doing many unnecessary recalculations/calls (such as get
trackmodel, column numbers etc) and after remove it I could see a great
improvement...

**Batch database updates**

As you know, Sqlite can not do a huge number of updates in a very short
time, so the solution was to collect all new covers and write them at
once every half second.

**Removing "indexOf()" calls**

The problem of using "indexOf" is that it just do a dumb loop... it
means that in many functions we are doing many extra loops (5, 10...) to
find things that we could have found using one loop... Now, imagine
doing it hundred/thousand times...

A good example is "CoverDAO::getCoverInfo()". This method can be called
very often mainly in cases when the user is scrolling fast in a new
library. It was doing one new "indexOf" call for each queried column,
just to find the column number, when the same thing could be done using
just a single loop...

So, we must avoid using "indexOf" mainly in places which are called very
often.

**Md5 calculation**

Although it is being done in a working thread (via qtconcurrent), when
it takes a long too long, it slows down the loading of other covers and
it can lead to significant performance losses. I noticed that
CoverArtCache was doing md5 calculation right after the QImage loading
and it could be bad in cases when the original cover has big
resolutions... so, a simple solution was to rescale covers before the
md5 calculation...

## DlgCoverArtFetcher

This week I also worked on several improvements for the fourth branch
(downloading covers), fixing some issues with the Last.fm connections
and also adding some features to the CoverArtFetcher dialog.

# Issues for the next week

Next week: [August 03 - August 09](cover_art_support_r7)

This is the last week before the suggested "pencils down" date. So, my
plan is keep work on the fourth branch, especially in the tableview
issues of the dlgcoverartfetcher. In parallel I plan sort out some
issues which can be raised by my mentor, other developers and users...

# Links

\[1\] - <https://github.com/cardinot/mixxx/pull/2>
