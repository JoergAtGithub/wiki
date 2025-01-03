# Lambda scheme

This is article on new scheme of database access.

## Todays approach to database access in Mixxx

There are lots of objects which need to use database access. Most of
that type of access is provided by respective `*DAO` (`DAO` means data
access object) objects. Instances of each `*DAO` object consist in
`TrackCollection` class. `TrackCollection` holds also database
connection and populates it on all `DAO`s.

In Mixxx 1.11 if you want to conduct database access you must:

1.  Get pointer to respective DAO
2.  Prepare query and data
3.  Apply query (synchronously in main thread)
4.  Populate table models from query results (if it's necessary)

The main problem of such scheme is conducting the db access mostly from
the Main thread. That's why while query's pending we face UI freezing.

The main requirement is avoid hanging of UI (or minimize hanging up to
16 ms given by the display refresh rate, but not more).

There are lots of inherited complexity in the db usage:

1.  Threads are evil =)
2.  The db connections can be used only in that thread where it was
    created
3.  We must have just one access point to db in perfect case

We propose new scheme of the db accessing. This scheme requires usage of
[lambdas which was presented in new
C++11](http://www.cprogramming.com/c++11/c++11-lambda-closures.html).

Thanks to the introduction of Lambdas into C++11 it is much easier to
write RPC, so we can avoid callbacks or using signal-slots (as it need
us to write lots of overhead). Lambdas (in our case) is alternative to
callbacks. But, as for me (and you can see at small example here
<https://github.com/troyane/lambdaConcurrent>) lambdas syntax is little
bit unusual, but very clear and much shorter then other ones.

Lambda also can behaves as closure (closure unlike a plain function
pointer allows a function to access those non-local variables even when
invoked outside of its immediate lexical scope).

We move execution of lambda to separate thread.

Without chaining the Mixxx 1.11 business logic too much we got ability
to provide database access in separate thread. As it was required.

## Scheme in few words

We are going to keep all `DAO` class hierarchy and keep behaviour mostly
the same, except one important moment -- conduct all database access in
dedicated database thread.

Object `TrackCollection` becomes our separate thread. It is creating in
`Library`, also connects to database, holds this connection, initializes
all `DAO` objects and begins its own "event loop" (`while` cycle in
`run()` method where thread waits for incoming lambdas containing db
queries).

We got into cycle body every time someone places lambda to queue by
calling `callAsync()/callSync`. Here we dequeue lambda and execute it
(in `TrackCollection`s thread).

**What do I need to do with some code to apply new scheme?**

1.  Get pointer to `TrackCollection`s thread
2.  Surround your code by respective call of `callAsync/callSync` where
    the first parameter will be lambda with its catched values (most
    common -- this).
3.  Be sure all used `this` member variables are used in a thread save
    way. We must rely on fact that object will be still alive when
    lambda'll execute in separate thread. 

It guarantees your code will be placed into queue and executed as soon
as possible in `TrackCollection`s thread. Must admit that `callAsync` is
**asynchronous** function. It means that all operations on placing
lambda into queue happen in less than 16 ms and execution from your
context goes on. We can't say exactly when lambda will be executed (as
soon as it is placed to queue and becomes at the top of queue).

## Locking UI

Here is sarcastic comics on theme of locking --
<http://dottech.org/93827/how-many-people-madly-click-their-mouse-when-a-program-freezes-comic/>

There is no sense to queue lot of identical queries, so we must not lock
all UI, but just lock ability to do some other queries (so, lock just
left sidebar and library for example).

For this purposes we created new binary control \[Playlist\] “isBusy”
with range (0.0f — off, else on). And it makes library widget grey
(enabled==false).

So, we can use this CO this way: `m_pCOTPlaylistIsBusy = new
ControlObjectThread(ConfigKey("[Playlist]", "isBusy"));`. And we are
locking/unlocking UI through this CO from `TrackCollection`s thread.

## Some moments of lambda usage

### If you need to access UI from lambda

See [Rules and arrangements using lambdas scheme for database
access](lambda_rules)

### Not Asynchronous, but synchronous

*This can be uses safely during construction time of Mixxx but should be
avoided in run time.*

If you can't move on until code in lambda executes. For example, when
you need results of some query in initialization of your class. Do it
with `callSync`.

Completing this instruction, we do as it was previously, but with pause
of further execution until respective lambda will be executed and
respective mutex will be unlocked. Beware your lambda must wait whole
lambda queue.

### Lambdas queue upper bound

There is the upper bound for lambda queue (`MAX_LAMBDA_COUNT`). Someone
someday could wait in `callAsync` if there is no empty positions in
lambdas queue.

In this case this debug message: "..." will be printed to the mixxx.log
file.

## Dia

All of written above can be described by next sequence diagram

[[/media/wiki/callasync.png|]]

**NOTE:** Here is mistake -- we use `Qt::QueuedConnection` (or
`MainExecuter`) instead of `Qt::BlockingQueuedConnection`.

## Long transactions

Example of "long" transaction is `LibraryScanner`.

We already have working scheme on pausing library scanner (here we can
make pause by clicking "pause" button in respective
`LibraryScannerDlg`).

Main idea is to use same interface for accessing database -- `callSync`.

Here uses cashing system -- we collect 50 tracks and wrap into one
transaction. While that transaction is pending, user can be able to
interact with Mixxx UI, for example, create playlists (even without need
to click "pause" button).

# Idea of usage scheme based on chunks

`LibraryScanner` runs in separate thred.

We already have `callSync` function, which calls synchronously. Also
there is mechanism that controls weather we are in `Main` thread or in
other thread. In case of other thread we just sleep (sleep thread in
background).

So, new API for long transaction expects possibility to divide all
database access into several **chunks** and send it one by one and wait
until it executes.

This synchronous scheme gives us great programming experience -- we
avoid need of thread synchronization (and lot of inherited overhead
codding). Every thread just do `callSync` with adequate *(I mean, not so
big, and not so small)* transaction. Our scheme will be workable on lots
of *parallel* working threads, and user input will be smooth as well.

All bad moments of this scheme is in that fact that `LibraryScanner` (or
other "long" transactions) will cost more time and that in general case
-- since we need to open lot of transactions. *(But we are talking about
operations in separate thread, so it can take its time).*

If it would be very important - we can rewrite scheme further. But as I
feel, now this is best solution -- chopped transactions.
