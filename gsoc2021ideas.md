## Student Project Ideas for Google Summer of Code 2021

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of Code 2021](https://summerofcode.withgoogle.com/). 

If you are interested in applying to GSoC, read [GSoC Advice](gsocadvice)
before applying or getting involved. Only students that are active members
of the Mixxx community are accepted. If this is not the case yet, just
say hello at <https://mixxx.zulipchat.com> and discuss your Ideas and
use cases with us.

# OSC Interface

Open Sound Control (OSC) is a descriptive network protocol that suits to remote control Mixxx via a standard interface. 

There where various promising attempts to integrate that into Mixxx, but nothing has landed into the code base yet. 

  - https://github.com/mixxxdj/mixxx/wiki/OSC%20Backend
  - https://github.com/mixxxdj/mixxx/wiki/OSC-Client
  - https://github.com/mixxxdj/mixxx/pull/2078
  - https://github.com/mixxxdj/mixxx/pull/2064
  - https://github.com/mixxxdj/mixxx/pull/2062

In this project you should evaluate the exiting OSC Mixxx code for building a custom touch controller using Open Stage Control https://openstagecontrol.ammd.net/

The discovered issues and short comings shall be ironed out and you should finally deliver a stream lined experience for integrating Mixxx and Open Stage Control.

# New controller system

The current controller mapping system has a lot of inconveniences and limitations. The community has been brainstorming [plans](https://github.com/mixxxdj/mixxx/wiki/New-controller-system) for a new controller mapping system. This project would start implementing the new system.

# Spin-Up/Spin-Down effect 

Some Controller mappings have implemented a Spin-Up/Spin-Down to mimic the inertia of a turn table. 
This should be moved into the engine, so that it is accessible without a controller.

# Fader-Start Feature

Some Controller mappings have implemented a Fader-Start feature. This allows to start a track by pulling the line fader-up.
This should be accessible without a controller.  
 
# Scratch smoothing.

Our scratching algorithm suffers from jitter noise created by the latency of the midi messages. 
This can be improved by considering the time stamps of the midi messages.

# Sharp Scratching

Currently crossfader changes are stretched on audio buffer time to avoid pop sounds. 
This is too long for some scratching styles. 

# Resample options

Mixxx uses a linear resample when scratching. This is blazing fast, but the sound can be improved. 
Here Mixxx should provide more resample options. 

# graceful recovery of controllers

If a controller is accidentally unplugged it has to be manually reconfigured, which is a party stopper. 
Mixxx should do it automatically . 

# Dual screen Skin 

Allow to create a Windows widget form skins. 

# *Custom Tags* UI

[PR #2656](https://github.com/mixxxdj/mixxx/pull/2656) allows to assign *custom tags* to tracks. The feature is almost finished (database and file import/export) but lacking a decent UI for managing and searching custom tags.

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
