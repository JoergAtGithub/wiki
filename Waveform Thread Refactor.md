# Waveform Thread Refactor

## Summary and Rationale

**Status**: This specification is **in progress**. Any extra features
people think of should be sent to the mailing list.

The current WaveSummary thread does not work for our purposes. There are
specifically two problems:

  - The thread works as a queue, and can only process requests serially.
    
  - The thread is not capable of aborting the processing of a specific
    song.

## Problem Cases

Examples of usage that leads to problems:

### Example 1

  - User loads a song to deck 1
  - User loads a song to deck 2
  - User loads a song to deck 1

What happens: The waveform thread has 3 items queued. It will take a
while to process the first one, and the two others will not be processed
until the first is done. This results in no waveform view displaying for
either deck until the processing of the first song is done.

What should happen: A song should have its waveform displayed the second
it is loaded to a deck. If a song leaves the deck, CPU time should not
be wasted on it anymore.
