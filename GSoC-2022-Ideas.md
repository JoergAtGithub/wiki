## Student Project Ideas for Google Summer of Code 2022

This page lists the suggested tasks to build a GSoC medium or large project for [Google Summer of Code 2022](https://summerofcode.withgoogle.com/). Please pick one or two of these task and define your own project from it by putting it into a time frame and extend it with our own ideas for improving Mixxx. 

If you are interested in applying to GSoC, read [GSoC Advice](gsocadvice)
before applying or getting involved. Only students that are active members
of the Mixxx community are accepted. If this is not the case yet, just
say hello at <https://mixxx.zulipchat.com> and discuss your Ideas and
use cases with us.

# Spin-Up/Spin-Down effect 

Some Controller mappings have implemented a Spin-Up/Spin-Down to mimic the inertia of a turn table. 
This should be moved into the engine, so that it is accessible without a controller. https://bugs.launchpad.net/mixxx/+bug/1692261

# Fader-Start Feature

Some Controller mappings have implemented a Fader-Start feature. This allows to start a track by pulling the line fader-up.
This should be accessible without a controller.  https://bugs.launchpad.net/mixxx/+bug/661917
 
# Scratch smoothing.

Our scratching algorithm suffers from jitter noise created by the latency of the midi messages. 
This can be improved by considering the time stamps of the midi messages. https://bugs.launchpad.net/mixxx/+bug/1157573

# Sharp Scratching

Currently crossfader changes are stretched on audio buffer time to avoid pop sounds. 
This is too long for some scratching styles. https://bugs.launchpad.net/mixxx/+bug/1703475

# Resample options

Mixxx uses a linear resample when scratching. This is blazing fast, but the sound can be improved. 
Here Mixxx should provide more resample options. https://bugs.launchpad.net/mixxx/+bug/1775164

# Graceful recovery of controllers

If a controller is accidentally unplugged it has to be manually reconfigured, which is a party stopper. 
Mixxx should do it automatically.

# Graceful suspend/resume support: 

Mixxx should be able to continue playing after cumming back from the suspend state of the PC. 
https://bugs.launchpad.net/mixxx/+bug/1744641

# Auto Updater for Windows and MacOs

Mixxx should look up our download page and automatically update itself in case an update is available.

# Track suggestion feature

Mixxx shall suggest compatible tracks matching the current playing one. The feature may use existing meta data like bpm genre and key or tab online resources like LastFM and similar. https://bugs.launchpad.net/mixxx/+bug/889898

# Transpose / Pitch shift effect

There should be an independent effect for pitch shifting. In addition to our main pitch shift feature this should be implemented as an independent effect with a wider range of parameter values. https://bugs.launchpad.net/mixxx/+bug/1299035  


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
