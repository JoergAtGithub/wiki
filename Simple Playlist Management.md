# Simple playlist management

HEY LOOK\! This is in no way advice to others; these are basically notes
to myself. I am a bottom rank sh\*t novice with no public performance
experience. I'm taking notes now for the future. You were warned. The
only thing I'll say in defense of these ideas at this point is that I'm
copying from people better than me, and I'm organized, and I test, test,
test. If you use anything here and your laptop catches fire, it's your
own stupid fault.

# Software

I intended to write about technique not tools, but there's few enough
worth a damn... so it goes. This is all open source software.

  - I'm using [mixxx](www.mixxx.org) for DJing. Two players, beat
    detection, pitch-independent matching, support for inexpensive
    control surfaces, great support culture. I'm having problems with
    various functions within it (probably my fault), but I'm able to
    work around and work with to fix them. Who could ask for more?

<!-- end list -->

  - Good old [grip](http://nostatic.org/grip) for ripping audio CDs.
    It's un-fancy, been around forever, somewhat nerdly to configure,
    but it's fast, reliable, utterly trustworthy, and has worked on
    every hardware and software platform I've ever used in the last
    decade (freeBSD, linux, openBSD, ...). And, a huge positive feature,
    if you're ripping a disc not in the [freeDB CD
    database](http://www.freedb.org), your work typing in artist, disc,
    tracknames can be shared with the rest of the world literally with a
    click. If you don't like the named grip found in freeDB, you can
    edit them before ripping. (iTunes uses the craptacular Gracenote DB;
    if a disc isn't there it doesn't ask, it just uses "UNKNOWN"; if it
    comes up with a crazy name for the disc and/or tracks, good luck
    figuring out where iTunes stored them).

<!-- end list -->

  - Last, for previewing music and making playlists,
    [rhythmbox](rhythmbox). At first, I thought I would "put up with"
    rhythmbox since my preferred programs didn't work well for this, but
    it's turned out to be all around the best (meaning well-behaved)
    player program so far. It's fairly easy to make playlists, and
    barely acceptable for [changing
    "collections"](rhythmbox%20annoyance). 

# Music collection organization

I have a dedicated, modest, music computer; it does nothing else. Ubuntu
linux, Intel dual core, 4GM ram, two disks in RAID1, M-Audio 2496 sound
card for the main outs, and the onboard soundcard for headphones. I keep
a simple file hierarchy for storing music; a directory ingeniously named
**Music/** that contains directories with tracks in various states of
existence:

| Directory   | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Incoming/   | CDs ripped by Grip store here (Artist/Album). This where the CD ripper, grip, stores its results. Things don't live there long. If CDDB uses crazy filenames I can at least find the resulting files, and not have to search for the scattered throughout the Collection. I rip at the highest-possible sound quality; disk space is cheap and getting cheaper, and bad sound sucks. |
| Collection/ | This is the complete collection of all of my music, entire ripped CDs, etc, for archiving, error recovery and casual listening.                                                                                                                                                                                                                                                      |
| Psy/        | Ready to DJ (psytrance) tracks, only. This is a subset of the **Collection**, with all non-mix-able tracks removed. All tracks in here are within the desired BPM range, culled of dud tracks, and are all marked with my own ID3 "genre" tags.                                                                                                                                      |
| Trance/     | Ready to DJ trance tracks, as above.                                                                                                                                                                                                                                                                                                                                                 |

The DJ software, mixxx, uses **Music/Psy** has it's music collection.

# Collection management and tagging

It's been tough to find a program to manage my collection. The trick is
to be able to listen to track(s), edit ID3 tags and delete .mp3 files.
Many promise to do it (amarok, juk, ...) but all have some problem. So
far, rhythmbox is the best; to change "collections" I have to Edit -\>
Preferences, quit and restart, and sometimes
[more](rhythmbox%20annoyance); but at least it works. (With juk I was
utterly unable to find a way to change the collection itself after
initial setup. Amarok... drowning in it's own feature list.)

When I get new CD(s), I deal with them like so:

  - Rip the new discs with grip, first thing. The ripped discs go in
    **Music/Incoming**, a bunch of MP3 files stored in directories, like
    **Music/Incoming/Artist/Album/**.
  - Run easytag to mass-edit tags and rename files. I often don't like
    (or find baffling) the names in the CDDB and immediately fix
    problems here.
  - Copy \~Music/Ripped/\* untouched to \~/Music/Collection. If I screw
    up or change my mind here's a copy. 
  - Start up rhythmbox, with the collection set to \~/Music/Ripped.
  - Select-all, right-click, change (repair\!) GENRE ID3 tag to "psy" if
    I didn't do it in easytag. All my music right now is psy\!
  - Give all new tracks at least a quick listen. If it sucks for mixing,
    right-click and delete. (There's a spare copy in the Collection).
  - Right-click edit ID3 tags and add additional GENRE tags as necessary
    to describe the track. A list of my made up tags is below. They all
    contain 'psy' but the rest are descriptive; fast, dark, etc.
  - When a disc is done, it's moved from Ripped to Psy.

I don't always do all steps all in one sitting. Almost always I'll
immediately rip newly purchased discs, and do the rest of the steps as I
get to them, moving completed discs into Psy, and leaving un-processed
dics in Ripped. This way I know where I left off -- anything left in
Ripped is incomplete.

A copy goes into my music player (Creative Zen V) for listening, and the
Ripped directory left empty for the next round.

# ID3 'genre' tag values

These are the tags I use in the ID3 GENRE field to label and organize my
music. Most of the music players I've looked at handle searching and
sorting based upon genre tag. Your mileage may vary. The important thing
here (if there is one) is consistency. I keep this in a little text file
in my home dir and update as necessary (with comments, eg. a canonical
track/performer that defines that category).

| GENRE | DESCRIPTION                 |
| ----- | --------------------------- |
| psy   | (top level)                 |
| best  | hot track                   |
| deep  | Dimension 5                 |
| prog  | radio compatible            |
| full  | a bit full-on for me        |
| crazy | Frozen Ghost                |
| fast  | 150bpm+                     |
| dark  | Ka-Sol                      |
| light | as in not dark, not l-i-t-e |
| slow  | \-140bpm                    |

# Making playlists

Oh yeah, that. Basically I launch rhythmbox, point it to the **Psy/**
directory, and start picking songs. Often when I'm casually listening to
music, on my Zen, in the car, etc, I'll think "that would make a good
opener". So I start with one of those. As far as the actual process of
making a *good* playlist, well ask an expert, but basically I queue up
songs for playing, if I like it, I right-click and copy to a playlist.
(With rhythmbox, in the right-click menu there's an option to make a new
playlist; I do that for the first song (usually named something
ingenious like today's date)).

  - Right-click track to add to (new) playlist.
  - When done, right-click playlist, in left column, save-to-file.

Playlists remain internal to rhythmbox until you export them, which is
simply right-click the playlist name in the left column, save-as a
filename in your home directory.

It's easier to find playlists in mixxx if you copy them into it's music
collection root directory (in my case **\~/Music/**).

# Credits

Much of this arrangement was copied from this person:

<http://paradineshift.wordpress.com/2007/09/30/how-to-best-tag-and-manage-your-music-collection-for-digital-dj-mixing-mp3-flac-ogg-etc>

Who I thank thoroughly for hir concise notes\!
