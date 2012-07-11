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

# CachingReader

# ReadAheadManager

# EngineBufferScale

`EngineBufferScale` is an interface for representing modules that are
capable of re-sampling audio. Re-sampling is one of the key tasks that
`EngineBuffer` must accomplish since if a track is recorded at a sample
rate of 44.1kHz and the engine is outputting at a sample rate of 48kHz
then without re-sampling, the track will sound 'chipmunky' since the
track's samples will be played much faster than they would normally be
played.

To prevent this effect, the track must be resampled to Mixxx's output
sample rate. This is accomplished with an `EngineBufferScale`
derivative.

## EngineBufferScaleLinear

## EngineBufferScaleST
