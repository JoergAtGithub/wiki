# Introduction to Mixxx's Deck/Sampler Processing

Perhaps the most complicated part of Mixxx lies in its player (decks,
samplers, etc.) processing code. As the result of years worth of work by
multiple, unconnected people there has been significant rot and just
plain buggyness introduced over the years here. In recent years we have
been steadily rewriting it to try and improve the situation but it is
still quite complicated. This section of the developer guide aims to
demystify this monolith a bit.

# EngineBuffer

The lion's share of complexity lies in `EngineBuffer`. This class has
the following responsibilities:

  - Read decoded audio from a file loaded in the player.
  - Keep track of the state of the player (whether it's playing, how
    fast it's playing, what direction it's playing)
  - Respond to requests from elsewhere in Mixxx 
  - For example: seek to location, start/stop playing, seek to hotcue,
    start a beatloop, change the loop start/end position, eject track,
    etc.
  - Re-sample audio from the native file sample-rate to the engine
    sample-rate.
