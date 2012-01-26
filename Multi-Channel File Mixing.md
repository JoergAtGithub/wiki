# Multiple-channel file mixing

FLAC files support up to eight channels and OGG Vorbis supports up to
255. It would be interesting to extend Mixxx to allow DJs to work with
these channels individually within a virtual deck so as to be able to
create live remixes from stems. Doing this from a single multi-channel
file greatly simplifies the workflow and eliminates synchronization
problems.

## Overview of required changes

*(Awaiting review from the Mixxx lead developer.)*

  - FLAC and OGG SoundSources need to:
  - Be extended to work with up to 8 channels, correctly reporting the
    overall track length.
  - Get meta-data for each (whether any are stereo pairs/other groups.)
    Limit Vorbis to 8 channels as well for now.
  - TrackInfoObject needs to add a property for channel groups and
    get/set functions for it.
  - Decks need to:
  - Offer additional controls for each mono channel or channel group:
    Mute, Solo and Volume controls 
  - Tell the Analyzer which channel(s) to use for BPM detection
  - Analyzers need to:
  - Remove their assumptions of stereo, treating all channels as
    individual mono entities
  - Handle channel groups from 1-8 channels and process each group as a
    single combined mono signal
  - Report the number of rendered streams to the waveform renderer (Due
    to channel grouping, this may be less than the number of channels in
    the file.)
  - CachingReader needs to be extended to support up to eight channels
  - The GUI needs to:
  - Include additional parallel summary waveforms for each mono channel
    or stereo pair
  - Display Mute, Solo, Volume, and Pan controls as the Deck reports
  - Overlap all (active) channels' waveforms in the detailed waveform
    display
  - The waveform needs to change the way it renders to either 0 at
    bottom, |max| at top; or 0 at center, -max at bottom, +max at top.
    (Current is left channel from 0 at center to |max| at top, right
    channel from 0 at center to |max| at bottom.)
