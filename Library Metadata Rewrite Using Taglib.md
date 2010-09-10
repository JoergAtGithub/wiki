## Summary

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

Mixxx's metadata parsing is error prone, does not always handle
encodings properly, and doesn't support all tag formats for a given
container. This design document describes an effort to replace all of
Mixxx's current format-specific metadata parsing code with the use of
[TagLib](http://developer.kde.org/~wheeler/taglib.html), a
cross-platform library that provides an all-encompassing API for parsing
many different metadata formats. Currently it supports both ID3v1 and
ID3v2 for MP3 files, Ogg Vorbis comments and ID3 tags and Vorbis
comments in FLAC, MPC, Speex, WavPack and TrueAudio files.

## Metadata to Extract

The new metadata extraction system will extract the following metadata
from every file regardless of file format:

  - Artist (string) 
  - Title (string) 
  - Album (string)
  - Comment (string)
  - Genre (string)
  - Year (integer)
  - Track Number (integer)

Additionally, the system must extract the following properties of each
audio file for use in the GUI to present to the user and for use by the
Mixxx engine to calculate

  - Bitrate (int, best estimate) Only used for GUI purposes.
  - Length in Seconds (int, best estimate) Only used for GUI purposes.
  - Samplerate (int, must be correct) Used for various calculations
    within Mixxx
  - Channels (int) Not used. All SoundSource's upsample mono to stereo
    in SoundSource::read()

## Extra / Non-Standard Metadata

Some metadata formats have standard (or non-standard) ways that people
have gone about storing extra metadata such as the harmonic key of a
song or its average beats per minute.

When possible, Mixxx SoundSource's must extract the following additional
metadata from available tag structures:

  - Average BPM
  - Overall Harmonic Key of a song

### BPM

  - In ID3v1 tags, there is no possible way to store the BPM.
  - In ID3v2 tags, the BPM is stored in the 'TBPM' frame. This is part
    of the [ID3v2.3
    standard](http://www.id3.org/id3v2.3.0#head-42b02d20fb8bf48e38ec5415e34909945dd849dc).
  - In Xiph comment tags, the BPM is conventionally stored in a field
    with the key 'BPM'. It is also potentially stored under the key
    'TEMPO'. 
  - In APE metadata tags, we do not currently know the standard for
    storing BPMs.
  - In MP4 tags, the tempo is stored in a 'tmpo' frame. This is part of
    the MP4 standard.

### Harmonic Key

  - In ID3v1 tags, there is no possible way to store the key.
  - In ID3v2 tags, the initial key of the song is stored in a 'TKEY'
    frame. This is part of the [ID3v2.3
    standard](http://www.id3.org/id3v2.3.0#head-42b02d20fb8bf48e38ec5415e34909945dd849dc).
  - **In Xiph comment tags, the conventional way to store the key is
    currently unknown.** Is it 'KEY'?
  - **In APE metadata tags, the conventional way to store the key is
    currently unknown.**
  - **In MP4 tags, the conventional way to store the key is currently
    unknown.**

### Cover Art

TagLib makes it much easier to load cover art from the formats so this
is a good avenue for a sideproject. It is not a requirement of this
specification.

## Integration with Other Software

  - Serato Scratch Live 
  - Stores and reads BPM and key tags from the 'TBPM' and 'TKEY' frames
    in ID3v2. 
  - Handling of Xiph, APE, and MP4 is unknown.
  - Traktor Pro
  - Reads BPM and key tags from the 'TBPM' and 'TKEY' frames in ID3v2. 
  - It is unknown if it writes to these tags. 
  - Handling of Xiph, APE, and MP4 is unknown.
  - Mixed In Key 
  - Configurable to write key tags to the 'TKEY' frame in ID3v2. 
  - Handling of Xiph, APE, and MP4 is unknown.
  - Rapid Evolution 
  - Writes to 'TKEY' and 'TBPM' frames in ID3v2 by default. 
  - Handling of Xiph, APE, and MP4 is unknown.
  - iTunes
  - Reads 'TBPM' frames from ID3v2 by default. 
  - Does not support FLAC or OGG. 
  - Does not support the 'TKEY' frame.
  - beaTunes 
  - Supports 'TKEY' and 'TBPM' frames in ID3v2. 
  - Handling of Xiph, APE, and MP4 is unknown.
  - MixMeister BPM Analyzer
  - Supports 'TBPM' frames in ID3v2. 
  - Handling of Xiph, APE, and MP4 is unknown.

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
will become more detailed as the design above becomes more thorough and
complete.

    1 Use TagLib to process the metadata of every file format we support
      1.1 Implement parsing for TagLib's generic Tag interface.
      1.2 Implement custom parsing for ID3v2 tags
      1.3 "" APE tags
      1.4 "" Xiph comment tags
      1.5 "" MP4 tags
    2 Verify that nothing broke
      2.1 Verify new duration handling works
        2.1.1 In particular check MP3 VBR files
      2.2 Get a copy of every file format we support with a BPM tag attached. Verify BPM loads on library scan.
      2.3 Test the library on Albert's Library From Hell.

## Team

  - RJ Ryan
