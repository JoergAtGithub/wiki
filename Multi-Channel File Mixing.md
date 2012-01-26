# Multiple-channel file mixing

FLAC files support up to eight channels and OGG Vorbis supports up to
255. It would be interesting to extend Mixxx to allow DJs to work with
these channels individually within a virtual deck so as to be able to
create live remixes from stems. Doing this from a single multi-channel
file greatly simplifies the workflow and eliminates synchronization
problems.

## Overview of required changes

  - FLAC and OGG SoundSources need to find out how many channels the
    loaded file offers, get meta-data for each (whether any are stereo
    pairs/other groups,) and report this information to their parent
    Deck. (Let's limit Vorbis to 8 channels as well for now.)
  - Decks need to:
  - Ask for this information
  - Manage the supplied number of channels
  - Offer additional controls for each mono channel or channel group:
    Mute, Solo, Volume, and Pan controls 
  - CachingReader needs to be extended to support up to eight channels
  - The GUI needs to:
  - Include additional parallel summary waveforms for each mono channel
    or stereo pair
  - Display Mute, Solo, Volume, and Pan controls as the Deck reports
  - Overlap all (active) channels' waveforms in the detailed waveform
    display

## SoundSource API changes

``` 
    int getNumberOfChannels(); // Number of mono channels in the loaded file
    QString[] getChannelNames(); // Name for each channel - from FLAC/OGG tags
    QList(int[]) getLinkedChannels(); // List of channel groups to treat as one unit (Stereo pairs, surround channels)
```
