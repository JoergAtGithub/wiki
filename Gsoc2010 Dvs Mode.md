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

  - [dvs\_mode](dvs_mode) has some good ideas, as does [GSOC2010
    page](gsoc2010ideas).
  - I'm bkgood on launchpad and freenode
  - To contact me by email, use my irc name @gmail.com

### Current status

Digging through the mixxx code base to try to further figure out
implementation details, plus learning a bit about how sampling (digital
represenation of analog signals) works and skimming a book on Qt.

### Specification

#### Use cases

  - DJ Joe doesn't like lugging around crates of vinyl or CDs, but
    enjoys using his vinyl turntables (or DJ CD players) and mixer. DVS
    mode will allow him to control Mixxx's playback with vinyl control,
    and then mix the outputs with his own mixer, his his own effect
    modules, etc.

#### Design

Currently, the sample buffers are only accessible to EngineMaster. These
will be exposed via accessor methods so that SoundManager can choose
between the master and headphone mixes or the individual samples.
Changes made will be conscious of eventual merge of n-decks branch, i.e.
will want to look at exposing the various decks using a `CSAMPLE*
EngineMaster::getDeckByIndex(uint index);` method in place of

``` cpp-qt
CSAMPLE* EngineMaster::getDeck1();
CSAMPLE* EngineMaster::getDeck2(); // etc
```

There is, of course, an upper-bound given the finite nature of PCI
slots, USB ports, and sound cards, but a DJ could easily use four decks
(8 channels) of output (of course, there's currently only 2 inputs of
vinyl control... not sure if n-decks extends that). The other major
aspect of the mode is UI, preferences will have to be extended to
support routing audio to an external instead of using an internal mixer.
This will likely include a bit of refactoring.

#### Work breakdown structure

  - To be completed :) See
    [Work\_breakdown\_structure](https://en.wikipedia.org/wiki/Work_breakdown_structure)

### Links

  - Branch at (fill me in)
