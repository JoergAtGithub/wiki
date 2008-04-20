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

## People

As with any project, there are some names which you will see. Here's a
list of some:

### Mentor Team in Alphabetical Order

  - Garth Dahlstrom - Long-time Mixxx contributor \[how long... I don't
    know?\]. Experience with MIDI control, \[feel free to add more...\]
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
  - John Sully - 
  - Paweł Bartkiewicz - SoC student from last year, implemented LADSPA
    support in Mixxx
  - Micah Lee - SoC student from last year, worked on BPM detection in
    Mixxx
  - Nathan Prado - The final 2007 SoC student, worked on the library
    interface
  - Mark Hills/radiomark - Author of xwax, an open source vinyl control
    project which Mixxx relies on

## Community Resources

Mailing list, wiki, forum, blog, irc channel ...
