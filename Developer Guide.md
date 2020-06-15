# Mixxx Developer Guide

# Overview

The purpose of this guide is to give you, our intrepid contributor, an
overview of the Mixxx codebase. Mixxx is a big project with millions of
lines of code so it can be daunting at first. If you know how to get
around then it really isn't that big and scary.

**This guide is a work in progress. If you have any questions, join the
[Mixxx Zulip chat](https://mixxx.zulipchat.com/) to get live help from
developers.**

# Prerequisites

First, you will need to download the code of Mixxx [using
Git](using%20Git).

To understand this guide, you should have a working experience with a
systems language like C, C++, or Java. You should be able to get by with
trial and error even if you don't know these. It will help significantly
if you have some experience with the [Qt Framework](http://doc.qt.io/)
which Mixxx uses extensively.

We recommend you review these sections of the Qt documentation to get
familiar with aspects of Qt that we use heavily:

  - [Signals &
    Slots](http://qt-project.org/doc/latest/signalsandslots.html)

If you're not familiar with C++, [The Cherno
Project](https://www.youtube.com/watch?v=18c3MTX0PK0&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)
on YouTube has a good series dedicated to the core concepts.

We also highly recommend that you use a C++ IDE rather than a text
editor. Mixxx is a huge project spread across hundreds of source code
files. IDEs index the entire code tree and allow you to jump from where
a function is used to its definition, even if that is in another file
(which it often is). Without this powerful tool, you will spend a lot of
time simply finding the code you're looking for instead of understanding
what it is doing. We have [guides](developer%20tools#using%20IDEs) for
setting up several IDEs to work on Mixxx, but feel free to use whatever
IDE you prefer.

We highly recommend these resources from the Xiph.org Foundation for
background information on digital and analog signal processing:

  - [A Digital Media Primer For
    Geeks](https://wiki.xiph.org/Videos/A_Digital_Media_Primer_For_Geeks)
  - [Digital Show and
    Tell](https://wiki.xiph.org/Videos/Digital_Show_and_Tell)
  - [24/192 Music Downloads are Very Silly
    Indeed](https://xiph.org/~xiphmont/demo/neil-young.html)

# main.cpp

As all C++ programs usually do, Mixxx starts up with a `main` function
located in `src/main.cpp`. It looks roughly like this:

    int main(int argc, char** argv) { 
        // start up Mixxx
    }

You don't need to pay much attention to this section of the code. Most
of what it does is:

  - Initialize logging to file and some other minor things.
  - Initialize some Qt basics and plugin paths.
  - Interpret command line arguments
  - Create a `MixxxApp` class which is what starts up the rest of Mixxx.

# MixxxApp Class

`MixxxApp` is the class that ties everything Mixxx does together. Mixxx
is made up of a variety of subsystems that all accomplish different
purposes. You can find all of the code to `MixxxApp` in `src/mixxx.h`
and `src/mixxx.cpp`.

In earlier years, `MixxxApp` was in charge of way more than it should
have been. Over time we've tried to reduce the number of things it is
responsible for, but as of Summer 2012 it's still a whopping 1600 lines.

Among the things it does (in no particular order) are:

  - Initialize all of the Mixxx subsystems.
  - Shut-down all of the Mixxx subsystems at shutdown time.
  - Handle all of the menu-bar actions.
  - Control the transition into and out of fullscreen mode.
  - Keeps a list of all the contributors to Mixxx that are shown in the
    credits.
  - Install and setup translations. 
  - Load and save the Mixxx config file.
  - Initializes and displays the Mixxx GUI

# Core Infrastructure

These are the fundamental building blocks used almost everywhere in
Mixxx. You should skim these first so that you aren't confused when you
see them in other sections.

  - [Control System (ControlObjects)](developer_guide_control)
  - [Config System (ConfigObject, ConfigKey)](developer_guide_config)

# Major Subsystems

  - [Library](developer_guide_library)
  - [Shoutcast](developer_guide_shoutcast)
  - [Mixing Engine](developer_guide_engine)
  - [Deck/Sampler Processing](developer_guide_engine_player)
  - [Effects Framework](developer_guide_effects)
  - [SoundManager (OS audio interface)](developer_guide_soundmanager)
  - [SoundSource (per-format audio
    decoding)](developer_guide_soundsource)
  - [Analysers (beat detection, key detection, waveform analysis,
    replaygain, etc.)](developer_guide_analysers)
  - [Vinyl Control](developer_guide_vinyl_control)
  - [Controllers (MIDI, HID, etc.)](developer_guide_controllers)
  - [Keyboard Control](developer_guide_keyboard)
  - [Preferences Dialogs](developer_guide_preferences)
  - [Waveform](developer_guide_waveform)
  - [Skins](developer_guide_skins)
  - [GUI Widgets (non-skin)](developer_guide_widgets)
