# Student Project Ideas for Google Summer of Code 2020

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of
Code 2020](https://summerofcode.withgoogle.com/). Each of these projects
represents something that we think would make a really big difference to
our users and that we as a development team are really excited about. If
you are interested in applying to GSoC, read [GSoC Advice](gsocadvice)
before applying or getting involved.

A GSoC application that simply repeats the project description will
*NOT* be accepted. We expect you to think about the feature and how it
aligns with Mixxx's goals, describe potential use cases and propose a
plan for implementing a solution. Only students that are active members
of the Mixxx community are accepted. If this is not the case yet, just
say hello at <https://mixxx.zulipchat.com> and discuss your Ideas and
use cases with us.

# Preferences Redesign

Mixxx's preferences window has grown with the many features added to
Mixxx over the years. Sometimes the design of the preferences has been
an afterthought compared to working on the feature that the preferences
affect. As a result, the preferences window has become quite complex and
can be overwhelming to new users.

The structure of the preferences code has sometimes been an afterthought
too. Writing and editing code for Mixxx's preferences can be a hassle,
as you may experience working on the GUI design. Some parts of the
preferences have code that is over 10 years old which don't follow
Mixxx's current coding conventions. One issue with the code is that
there is no conventional way to specify the default values for
preference options in a single place, so this can lead to subtle bugs
when different default values are used in different places. Part of this
project would involve cleaning up the code for every page of the
preferences to use the same coding conventions that are easy to maintain
and make it easy to add new preference options.

A strong applicant for working on this project would have links to GUI
designs they have done before. Experience doing UX testing by observing
people using software would be an advantage.

# AutoDJ Improvements

Users have proposed many ideas for improving AutoDJ. Many users have
suggested features to make it easier to plan the timing when tracks will
play in AutoDJ:

  - <https://bugs.launchpad.net/mixxx/+bug/1293980>
  - <https://bugs.launchpad.net/mixxx/+bug/1467156>
  - <https://bugs.launchpad.net/mixxx/+bug/1568928>
  - <https://bugs.launchpad.net/mixxx/+bug/1523252>

Users have suggested ways to make AutoDJ more intuitive to use:

  - <https://bugs.launchpad.net/mixxx/+bug/1727747>
  - <https://bugs.launchpad.net/mixxx/+bug/1095287>
  - <https://bugs.launchpad.net/mixxx/+bug/1334279>

There have also been suggestions for alternate ways to have AutoDJ mix
the tracks:

  - <https://bugs.launchpad.net/mixxx/+bug/1766164>
  - <https://bugs.launchpad.net/mixxx/+bug/1807647>
  - <https://bugs.launchpad.net/mixxx/+bug/1384873>

# Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. We recommend
spending more than a few days using Mixxx and participating in the
community to develop a better understanding of areas where Mixxx could
use improvement. Our bug tracker is full of wishlist bugs and other
ideas scattered throughout, so if you browse through it, you may find
many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!** We
very rarely approve ideas students propose. If you're not already
experienced with DJ equipment, we recommend sticking with one of the
ideas above.
