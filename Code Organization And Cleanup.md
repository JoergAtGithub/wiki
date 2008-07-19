# Code Organization and Cleanup Project

## Summary

**Status**: This specification is **in progress**.

Mixxx has over 400 source files, all of which are stored alone in the
'src' directory. As Mixxx is gaining contributors, it is important for
the source tree to be well organized and furthermore that it reflects
the organization of Mixxx itself. This will allow new contributors to
more easily be able to pick a specific module of Mixxx to contribute to
without having to understand the whole system, as well as making it
easier on the core developers when adding new features. It will also
encourage more thought when adding new code. For example, if you are
about to add a class to the widget folder that does a fair amount of
'music logic', it shouldn't feel 'right'.

Another potential idea is to standardize the headers of files across the
project. Currently many of the file headers are the same as when they
were originally written. They vary in their mention of the GPL, and most
all lack a summary of the logic/code contained in the file. We should
standardize on a top header that mentions the project, the project
website, and a brief summary of what goes on in the file. The original
author, start date, and email can stay because it's useful information,
but it can contribute to people feeling like they are touching "someone
else's code." [How Open Source Projects Survive Poisonous
People](http://www.youtube.com/watch?v=ZSFDm3UYkeE).

## Use Cases

  - DJ Bill got a degree in CS and knows some C++. He loves Mixxx and
    would like to contribute. After discussing with the folks in
    \#mixxx, he decides to take on a 'weekend project' sized feature of
    adding a new widget to the UI. He is easily able to find the widget
    code in the 'widget' folder to see an example of a current Mixxx
    widget. He can easily ignore the engine, soundsource, MIDI, and
    visual code because they are stored in their appropriate
    directories. 
  - Developer Dan is a longtime Mixxx contributor, but hasn't been
    keeping up to date with the changes in the most recent release. He
    takes a look at the svn changelist from since he last contributed,
    and can see many additions to the 'input', 'widget', and 'engine'
    folders. He can easily tell where active development has been taking
    place by which folders have been changed the most. 

## Timetable

**This change is planned for post 1.6.0 release**

## Planning

The following are overall groups that the code can be grouped into:

  - Input 
  - Engine
  - SoundSource
  - Widget
  - Waveform
  - Util
  - LADSPA 
  - Skin
  - Dialog
  - Config

## Deprecated Classes

  - Player, PlayerProxy, PlayerAsio, PlayerPortAudio, PlayerJack,
    PlayerAlsa, PlayerRTAudio, need to be removed (or moved to 'old').
  - the old visual stuff can be deleted (it lived in 'old')

## Process

  - All files will be moved with the 'svn move' command so that their
    histories will be preserved within the SCM.
