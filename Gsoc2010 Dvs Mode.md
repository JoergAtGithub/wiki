# Adding a digital vinyl system (DVS) / external mixer mode to Mixxx (GSoC 2010 project)

  - Student: **Bill Good**
  - Mentor: **Adam Davison**

### Abstract

Adding an external mixer mode to Mixxx will greatly improve Mixxx's
ability to act as a part of a digital vinyl system. Mixxx's current
method of achieving this involves diverting one deck to the main output,
and the other to the headphone output, allowing the two to be mixed
externally. However, no features, such as the equalizer, can be
disabled. Benefits of disabling various features include increased CPU
time for other threads, and UI recognition of unwanted features.

### More info

  - [dvs\_mode](dvs_mode) is probably the closest thing to a project
    spec, aside from the idea from the [GSOC2010 page](gsoc2010ideas).
  - I'm bkgood on launchpad and freenode
  - To contact me by email, use my irc name @gmail.com

### Current status

Digging through the mixxx code base to try to further figure out
implementation details, plus learning a bit about how sampling (digital
represenation of analog signals works and skimming a book on Qt.
