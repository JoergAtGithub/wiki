This page collects some introductory information which we hope will be
of use to our students.

## Mixxx

As you all already know, Mixxx is a cross-platform DJing application
which recreates in software many of the features of a traditional
hardware DJing setup.

### History

Mixxx was originally written by Tue Haste Andersen and Ken Haste
Andersen in 2002 partly as a research project into user interface design
for Tue's PhD. The project continued to develop until some time around
2004 when Tue moved on to full-time employment and no longer had time to
manage the project. Although development continued, there were no new
releases and Mixxx drifted somewhat in this period until early 2006 when
Adam Davison became the lead developer and released Mixxx 1.5.0. For the
last 2 years, the project has been steadily growing leading up to our
inclusion in Summer of Code for the first time last year.

### Technical Info

**Mixxx** was designed with a strong focus on cross-platform
portability. **Qt** gives us a very strong cross-platform graphics
toolkit, and has additional benefits like a thorough set of data
structure implementations (eg. QMap, QList, etc.). Mixxx was originally
written using Qt 3, but during the summer of 2007, Mixxx was ported to
Qt 4. At the same time, we moved away from a custom qmake-based build
system, instead opting for SCONS. **SCONS** is a python-based build
system that has easy syntax, and is still very powerful. Our single
`SConscript` file (in the "src" directory) checks all of our
dependencies and builds Mixxx on Windows, OS X, and Linux.

New experimental (and potentially unstable) features are coded such that
they are only enabled when they are turned on at compile-time. For
example, during its development, recording was turned on by compiling
with `scons recording=1`. Now that recording is stable and reasonably
well tested, the compile flag has disappeared and it is always built
into Mixxx. For a full list of build flags, run `scons --help`

One of our goals is to minimize the amount of platform-specific code we
have. Before we moved our audio core to **PortAudio**, we had separate
backend for ALSA, CoreAudio, ASIO, WMME, etc. This is a losing strategy
for several reasons:

1.  Our code base was inflated by a factor of X.
2.  If we wanted to add new features (eg. multiple soundcard support),
    it was going to require modifying 5 different audio backends.
    Furthermore, nobody has the time/energy/computers to test Windows,
    OS X, and Linux implementations of stuff.

By switching to PortAudio, the platform-specific audio code was removed,
and our audio core is now much more flexible. Currently, our MIDI code
still has three different backends (Windows, CoreMidi, and ALSA-seq),
although creating a single PortMidi-based backend is something we will
consider in the future.

### Managing Expectations

When you enter the work world, you'll hear managers drone-on about how
with better communication all the bad things that happened could have
been avoided.

Its only partially true... Problems are almost assured to crop up from
time to time. To be really successful in handling them, you must also
include how you deal with the people you report to and the clients you
provide service to in your approach to solving them. \[In this case
mentors and the community of Mixxx users\]

This is calling *managing expectations*.

Our expectations of the GSoCers are:

  - Take the initiative. Don't sit around waiting for someone to ask you
    if you need help. If you are stuck, make an effort to understand the
    problem so you can ask good questions, then ask... ask the Google,
    ask the wiki, ask on IRC, ask a mentor, ask the mixxx-devel mailing
    list. 
  - We expect you to encounter problems, all of the mentors are here to
    help all the students, so please bug us.
  - Try to set realistic goals and timelines for yourself. This comes
    with experince, knowing code base and the problem domain. (Mentors
    should try to help with this.)
  - Over-communicate rather then under-communicate.
  - Help each other out. We are all on the same team. Everyone will
    pass/fail on their own, but we want everyone to pass big time (we
    hope to get some amazing contributions from all of you).
  - Feel free to dabble in other parts of Mixxx that interest you. Don't
    feel confined to just your project scope. Remember though, that you
    will be evaluated on your project's progress.

You've been selected because you presented great proposals, you've got
the skills to pull them off and because we sense in each of you a
passion for Music/DJing.

Mentors expectations of ourselves:

  - Ping the students at least once a week to get a progress updates -
    any problems, what happened last week, what's planned for the week
    coming up. 
  - Offer feedback on patches. 
  - Help students find solutions to problems, brainstorming, offer
    suggestions: approaches, better coding style, optimizations, etc.
  - ???
  - Profit\!

### Some Suggested First Activities

  - Sign up to the mixxx-devel mailing list and briefly introduce
    yourself to the broader community; who you are, where you are based
    out of, and what you are working on for GSoC... 
  - Sign up to the wiki and read the [wiki home
    page](http://www.mixxx.org/wiki/) to get and idea of some of the
    stuff that's on here.
  - Check out the code base from
    [SVN](https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk/mixxx)
  - Try build Mixxx - if you are building on a Debian/Ubuntu flavour of
    Linux check out these [Wiki](compiling_on_linux)
    [pages](compiling_on_an_asus_eeepc), if you are on Windows [check
    here](http://mixxx.sourceforge.net/wiki/index.php/HowtoBuildWin32),
    or on OSX [check here](compiling_on_os_x)
  - Check out the [developer tools](developer_tools) page

## People

As with any project, there are some names which you will see. Here's a
list of some:

### Mentor Team in Alphabetical Order

  - Garth Dahlstrom - Long-time Mixxx contributor (since Mixxx
    1.4.something). Most active on Hercules device support on Linux
    (libDJConsole)/Windows(MIDI), various interface tweaks, and
    occasional build script tweaks. Has a Hercules Mk2 and a Hercules
    RMX console, both do MIDI on Windows.
  - Adam Davison - Lead developer and organisation admin for GSoC. Knows
    about Windows development, MIDI control, skins and probably some
    other stuff
  - Albert Santoni - Has written loads of code for Mixxx. Knows about
    Mac/Linux development, wrote the scons build system, vinyl control
    and more.

Albert and Garth are based in Canada (EST -5), while Adam can be found
in either London or Geneva (GMT +0 or CET +1 respectively).

On IRC, Garth is jumpkick, Albert is asantoni, Adam is adam\_d.

### Other Notables in No Good Order

  - Tue and Ken Haste Andersen - As mentioned above, the original
    authors of Mixxx, no longer with the project.
  - Adam Bellinson/DJ Thread - Long time Mixxx user, does a weekly live
    show with Mixxx over on dnbradio.com
  - John Sully - Contributor since Spring 2007, wrote recording, new EQ
    code, improved VU meters, and more.
  - Paweł Bartkiewicz - SoC student from last year, implemented LADSPA
    support in Mixxx
  - Micah Lee - SoC student from last year, worked on BPM detection in
    Mixxx
  - Nathan Prado - The final 2007 SoC student, worked on the library
    interface
  - Mark Hills/radiomark - Author of xwax, an open source vinyl control
    project which Mixxx relies on

## Community Resources

There are a bunch of places where you can interact with the Mixxx
community, here's a list of the main ones:

  - [mixxx-devel](http://lists.sourceforge.net/lists/listinfo/mixxx-devel)
    - This mailing list is the centre of all development related
    discussion. You should all subscribe here:
    <http://lists.sourceforge.net/lists/listinfo/mixxx-devel>, right
    away if you haven't already.
  - [IRC](irc://irc.freenode.net/#mixxx) - More immediate than
    mixxx-devel if the right person is available, \#mixxx on freenode
    although I think you've all been there already
  - [Wiki](http://mixxx.org/wiki/) - A small but growing collection of
    useful documentation, you're already here so I won't put a link :)
  - [Forum](http://www.mixxx.org/forums/) - We now have a brand new
    forum which will hopefully grow and bring the user community closer
    to the development team over the next few months, have a browse
    here: <http://www.mixxx.org/forums/>
  - [Blog](http://mixxxblog.blogspot.com) - Irregular articles about
    Mixxx development progress: <http://mixxxblog.blogspot.com>

### More Developer Resources

  - Check out the [dev tools page](developer_tools) for stuff that makes
    developing under Linux easier
