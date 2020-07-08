## 1.7 -- Good Release -- Do it again\!

Present: Sean, Albert, Adam, RJ, Phil, Garth, Sean's grandmother

[Meeting
Slides](http://docs.google.com/a/mixxx.org/present/view?id=dd557nj5_40crds5ztn&invite=1845909554)

1.8 is well on its way. Now that we are more than a month into this
development cycle, a look at the current progress is a good indicator
for what will actually get done.

## Revised 1.8 Targets

Time to narrow in on what will realistically happen:

  - Library : more work, but coming along
  - Looping : needs final spit-n-shine
  - Shoutcast : needs UI feedback for when connection is there or not,
    needs to not crash
  - Pitch-Bend : preferences polish
  - Multi-MIDI : needs to be bug free, support just the basics for
    consideration for 1.8

Features that are in danger of not happening for 1.8:

  - LADSPA: No work has been done this past month. If nobody steps up
    and works on this, it will not be a focus for 1.8
  - BPMDJ: No work on adapting this has happened. 
  - M4A Support 

## Multi-MIDI

How do we support communication between device scripts?

Potentially some script-engine assisted way for scripts to create their
own ControlObjects. This is beyond the scope of 1.8, but we should be
thinking about it.

## M4A Support

Lots of people really want this. It would be a shame if we didn't put in
the extra effort to get it done for this release, especially since it
makes iTunes library work less effective.

  - Adam will contact the Audacity people about legal issues of
    packaging the library on Windows / Mac
  - We can try to get it working reliably in Linux and simply link to
    pre-shipped codecs so we sidestep legal.
  - soundsourcem4a has some lingering memory corruption issues that need
    fixing
  - (Update 10/2009 -- The SSM4A problems are fixed so barring licensing
    issues, M4A is good to go)

## Library

Lots more work to be done, but there are people actively working on it.
In the least the 1.8 library will have feature parity with the old
library, except it will do it faster and less with no bugs.

The revised 1.8 feature targets for the library are:

  - track db
  - searching
  - browse
  - playlists
  - play queue
  - working rescan
  - tagging
  - external sources

Instead of importers we are going to focus on external sources for 1.8.
1.9 may include importers.

## 1.8 Release Schedule

  - Sep 26th Merge features\_looping to trunk
  - Sep 26th or earlier: Mixxx 1.7.1 Bugfix Release
  - Oct TBA Code Sprint
  - Nov 14th Mixxx 1.8 Feature Freeze
  - Dec 14th Mixxx 1.8 Beta 1 (in time for gift season)
  - Jan 14th Mixxx 1.8 Final
  - Feb 14th (Estimated) Lucid Lynx Feature Freeze
