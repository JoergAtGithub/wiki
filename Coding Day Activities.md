# Coding Day

On Tuesday July 29th, we'll be having a day of code to get release 1.6.0
ready to go. If you want to help, hop on our IRC channel (**\#mixxx** on
Freenode) and we'll get you involved.

There's tons of stuff to do, here's a list:

  - Coding/Bug fixing obviously needs doing, visit the [launchpad
    tracker](https://launchpad.net/mixxx/) and talk to the developers
  - Testing will be needed at various points on various platforms
    throughout the day
  - Documentation needs plenty of work
  - Especially the [manual](manual) could use a lot of work
  - New website design is in progress, anyone with useful
    php/javascript/jquery skills should talk to **asantoni** (IRC)
  - Could use some new high quality skins if there are any designers out
    there

## Available Non-Coding Tasks:

  - **Help us finish the new manual**. The PDF manual currently bundled
    with Mixxx is ancient, and the original source document for it is
    lost to the sands of time. For 1.6.0, we've decided to rewrite the
    manual. We need your help writing sections for it though - some of
    you know Mixxx very well and doubtlessly have better writing skills
    than us. Take a crack at filling in one of the empty sections of
    [the Mixxx 1.6.0 manual](manual). In particular:
  - Many of the interface elements in the [UI
    Overview](manual#user_interface_overview) are incomplete - a few
    sentences will suffice for each.
  - Figure out what we're missing. Take a peek at what we have, and try
    to think of any big points that we've missed in the manual. Comb
    over [the old manual](http://mixxx.sourceforge.net/Mixxx-Manual.pdf)
    as well for ideas.
  - **Test Serato CD support**. Got a CDJ? Have a CD discman or anything
    that plays CDs? Download the Serato CD wave, burn it to a CD, and
    test to see if you can control Mixxx via your CDJ or discman. 
  - The wave can be downloaded
    here:<http://rane.com/scratchlivecontrol.zip>
  - Report your findings on IRC and here:
    <https://bugs.launchpad.net/mixxx/+bug/186341>
  - ~~**Create the massive 1.6.0 changelog**~~. Go through the [Mixxx
    Blog](http://mixxxblog.blogspot.com/) archives, and find the release
    announcements for 1.6.0 beta 1, 2, 3, and 4. A changelog was
    included with each release - copy and paste the changelog bullets
    from each announcement into one gigantic document. Email that to
    someone on IRC. 
  - **Help us reproduce crazy Windows bugs**. We don't have very many
    Windows developers (or developers with Windows installed even), so
    it's hard for us to track down certain Windows-only bugs. In
    particular, the following three bugs have been driving us crazy:
  - [Program fails to
    open](https://bugs.launchpad.net/mixxx/1.6/+bug/223464) - We think
    we've fixed this in Beta4, but we can't get in touch with the person
    who reported the bug initially, so we don't know for sure. If anyone
    can reproduce this on Windows, or confirmed that the problem was
    fixed for them when upgrading from Beta3 to Beta4, please let us
    know.
  - [Mixxx doesn't exit
    cleanly](https://bugs.launchpad.net/mixxx/1.6/+bug/235479) - Same
    deal, we may have fixed this already, but we don't know. Do **you**
    have this problem on Windows? Get in touch with us and we'll try to
    track it down with you.
  - [Runtime error on
    exit](https://bugs.launchpad.net/mixxx/+bug/251128) - A user
    reported this problem with Vista Home Premium + SP1. Are you using
    Vista? Does Mixxx work for you? Yes or no, please let us know. If
    you're encountering this problem too, please get in touch on IRC or
    by email and we'll track it down with you.

## Available Coding Tasks:

  - **Crush bugs with an iron fist**. [Baby, we've got
    bugs](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=status&search=Search&field.status%3Alist=NEW&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.assignee=&field.bug_reporter=&field.omit_dupes=on&field.has_patch=&field.has_no_package=).
    Take a crack at any bug marked "new" or "confirmed". While most of
    those bugs are not 1.6.0 release blockers, we'll still accept
    patches for most of them. Bugs that are probably fixable without a
    huge time investment:
  - [Library rescan doesn't work
    sometimes](https://bugs.launchpad.net/mixxx/+bug/239883)
  - [Scanning library does not exit
    cleanly](https://bugs.launchpad.net/mixxx/+bug/194415) (might be
    related to above)
  - [New playlist doesnt show up
    initially](https://bugs.launchpad.net/mixxx/+bug/248918)
  - ~~**Cleanup Input Controllers Prefs**~~. The "Input Controllers"
    preferences pane contains unsupported (broken) mouse control stuff.
    Remove this from dlgprefmidi.cpp and dlgprefmididlg.ui and send us a
    patch.
  - **QSpinBox-\>QDoubleSpinBox in Interface Prefs**. The temporary and
    permanent pitch/rate buttons options in the interface preferences
    pane uses QSpinBox controls, which only support integer numbers. The
    value in the spinbox controls is actually divided by 1000 before
    being applied to Mixxx's engine (a value of 400 turns into a pitch
    bend of 0.4%). Your task is to change the QSpinBox controls to
    [QDoubleSpinBox](http://doc.trolltech.com/4.1/qdoublespinbox.html)
    and remove the division by 1000, so it's WYSIWYG. Make your changes
    to dlgprefcontrols.cpp and dlgprefcontrolsdlg.ui and send us a
    patch. Please test the hell out of this before sending us a patch
    because we'd rather not break this before 1.6.0.

## Tasks In-Progess:

  - Fixing the cue button for the Hercules on Windows
  - assigned to adam\_d, might be finished already.
  - **PHP: Generate news...better** - The news on our front page is
    generated by this magpierss php script, which downloads and parses
    our RSS feed from our Launchpad announcements. What we'd like to
    have is it to use our blog's RSS feed, but to ignore entries that
    aren't tagged with "news". This way, when we want to post news
    that'll show up on the front page, we'll just post on the blog and
    make sure we include the "news" tag. Existing code:
    <http://senduit.com/654416>
  - assigned to mattorsky

## What We Got Done

Let's keep track of how productive we were:

  - make ov\_fopen ifdef'd for Windows
  - remove crufty unsupported mouse controls from the preferences
  - added clear button to the search box
  - many SConscript changes / fixes
  - added support for a new MIDI controller : NuMark TotalControl
  - found and filed a lot of Windows bugs (hooray\!)
  - fixed an XML parsing bug
  - new artwork for 1.6.0 website
