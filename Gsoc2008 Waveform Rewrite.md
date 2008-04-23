# Creating a new Waveform View handler for Mixxx (GSoC 2008 project)

  - Student: **Russell Ryan**
  - Mentor: **Albert Santoni**

### Abstract

The current Mixxx waveform view is in need of a refresh. In its current
state it is not flexible enough to support desirable new features, and
it also causes performance issues that can cause skipping in the audio.
Redesigning the waveform view will both provide Mixxx with a more
feature-full waveform view and hopefully alleviate these performance
issues.

The goal of the project is to rewrite the Mixxx waveform view. The new
waveform view will support all the current features of the waveform
view, and more. The new viewer will be designed to be flexible enough to
support improvements and features that could come in the future.

Features of the waveform viewer include:

  - A display of a waveform with time on the horizontal axis and
    amplitude on the vertical axis.
  - A center 'mark' which indicates the current position of the player
    on the waveform.
  - 'beat frames' which coordinate with Mixxx's beat detection
    algorithms to render markers on each detected beat in the waveform
  - Coloring of the waveform based on the 'timbre' or sound feel of the
    waveform.
  - Integration with the GUI (or vinyl control interfaces) to support
    dragging of the waveform back and forth
  - Support for drag-and-dropping a song onto a 'virtual deck' to load
    the song into that deck
  - Support for an arbitrary number of audio streams for which to
    display waveforms
  - Support for markers or other meta-indicators to be set on the
    waveform to serve as visual feedback to the user. This will be
    useful for implementing features such as looping controls.

These features will be implemented over the course of the summer of
2008. Checkpoints and measurable progress indicators will be used to
ensure development is on schedule.
