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

## Use Cases

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
