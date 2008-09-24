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

## Proposed Solution

Make the following changes to WaveSummary Thread

  - Eliminate the queue functionality
  - Generate both the waveform summary and visual waveform downsampled
    data, and store them privately
  - Support a 'halt' method which will cause it to stop processing, and
    shut down its thread. 
  - Support being started at any time to generate the visual waveform or
    waveform summary of the TrackInfoObject that it corresponds to.
  - If work on either of the 2 buffers has already completed, it will
    not repeat work.
  - The WaveSummary thread will be in charge of the deletion of the
    wavesummary buffer and visual waveform buffer

Make the following changes to TrackInfoObject

  - Every TrackInfoObject will have its own WaveSummary object
  - TrackInfoObject will no longer hold pointers to the WaveSummary
    object. The getWaveSummary and getVisualWaveform calls will remain,
    but they will be replaced with inline calls to the corresponding get
    method of the WaveSummary Thread.

Make the following changes to Track

  - Where it previously queued a track for WaveSummary processing,
    ensure the TrackInfoObject has a WaveSummary thread, and start it

There will be other minor changes to other places in the codebase, but
these are the most significant.
