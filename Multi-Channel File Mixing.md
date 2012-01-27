# Multiple-channel file mixing

FLAC files support up to eight channels and OGG Vorbis supports up to
255. It would be interesting to extend Mixxx to allow DJs to work with
these channels individually within a virtual deck so as to be able to
create live remixes from stems. Doing this from a single multi-channel
file greatly simplifies the workflow and eliminates synchronization
problems.

## Overview of required changes

*Note from RJ -- I have filled in time estimates as estimates of how
long it would take me personally to accomplish. Keep in mind I have very
intimate knowledge of Mixxx and have authored half of the code to be
replaced myself*

  - ~~FLAC and OGG SoundSources need to:~~ **Author new `ContentSource`
    API** **(40 hours)**
  - Be extended to work with ~~up to 8~~ **an arbitrary number of audio
    and video** channels
  - Report track length in frames of content rather than samples as
    SoundSource does.
  - Support querying of metadata for semantic information about channels
    (e.g. vocals, bass, down-mixed version, drums, etc.)
  - ~~TrackInfoObject needs to add a property for channel groups and
    get/set functions for it.~~ No changes should be necessary to TIO
    except for deprecation of channels property. No part of Mixxx should
    use TIO for audio data -- ideally it is for metadata of the artistic
    work only. **(20 minutes)**
  - Really need to pick terminology and stick to it :). It's easy to get
    mixed up. 
  - Track: A piece of content e.g. a song or video
  - Channel: A stream of mono audio in a track
  - Sample: A single amplitude of an audio channel
  - Frame: A single time step of the sampling rate of a piece of content
    (E.g. a 4-channel track would have frames of 4 samples, one sample
    from each channel.)
  - Stem: A (set of) channel(s) within a track that represent a
    particular component. E.g. stereo vocals, 3-stereo strings, mono
    drums.
  - Significant Engine work necessary **(120 hours)**
  - In short, remove all assumptions of 2-channel audio and replace with
    n-channel frames
  - At a minimum, major updates to

<!-- end list -->

``` 
    * EngineBuffer
    * All EngineControl classes
    * CachingReader
* EngineObject API needs to be changed to support the passing of frames of arbitrary size between EngineObjects (currently hard-coded to stereo buffers of audio) 
* Extend CachingReader to cache frames of arbitrary size. (Right now it is hard-coded to stereo.)
* Modify EngineBuffer and EngineBufferScale* classes to read and scale N frames (instead of N stereo samples as currently.)
* Build a new EngineObject, let's call it EngineMixdown for now, that sits in the audio rendering path for EngineDeck. This will take the available scaled channels provided by EngineBuffer, group them by stem (needs to ask ContentSource for the stem info,) and mix them according to ControlObjects exposed to the rest of Mixxx (e.g. keyboard, GUI, MIDI). EngineFilterBlock is an example of this kind of merging of 3 paths of audio.
    * EngineMixdown should expose Mute, Solo and Volume controls for each stem of the track.
    * In process(), EngineMixdown will mix together all of the stems given the values of the control parameters and pass the resulting down-mixed stereo audio on to EngineMaster.
```

  - Rewrite Analyzer API **(40 hours, assuming waveform 2.0 lands in
    1.11)**
  - Remove assumption of stereo audio, use ContentSource API to
    understand the available stems in a track.
  - If semantic information about the stems is available, it should
    BPM-detect only the drum track. Use the bass track if there's no
    drum track.
  - Waveform calculation should produce waveforms for each stem. (Easier
    with Waveform 2.0 since this is already done for low/mid/high
    versions of the track)
  - The GUI needs to: **(dirty hack: 15 hours, the right way: 40
    hours)**
  - Include additional parallel summary waveforms for each mono channel
    or stereo pair
  - Display Mute, Solo and Volume controls as the Deck reports
  - Overlap all (active) channels' waveforms in the detailed waveform
    display

**Total time estimate: 5-6 weeks of full-time development** (So maybe
1.5x that if you're new to the code base.)

## Sample multichannel files

Here are sample files that could be used for testing...

<http://people.64studio.com/~daniel/DJ_Vadim-Saturday.ogg> (lossy,
24.5MB)

<http://people.64studio.com/~daniel/DJ_Vadim-Saturday.flac> (lossless,
71.3MB)

These are made using the stem files from
<http://ccmixter.org/imaginashun> dropped into Audacity, mixed down to
four stereo tracks, then using the multichannel export option (in Edit
-\> Preferences -\> Import/Export -\> Use Custom Mix) to get 8 channel
output files.

They are both 44.1KHz sample rate, 16 bit depth, quality setting 5. The
Ogg file will play in VLC. The FLAC file does not, but it can be mixed
down to stereo in Ecasound with:

`ecasound -a:1,2,3,4,5,6,7,8 -i DJ_Vadim-Saturday.flac
-a:1,2,3,4,5,6,7,8 -o alsa -a:3 -chmix:1 -a:4 -chmix:2 -a:5 -chmix:1
-a:6 -chmix:2 -a:7 -chmix:1 -a:8 -chmix:2`
