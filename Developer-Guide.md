# Mixxx Developer Guide

The purpose of this guide is to give you, our intrepid contributor, an
overview of the Mixxx codebase. Mixxx is a big project with millions of
lines of code so it can be daunting at first. If you know how to get
around then it really isn't that big and scary.

*This guide is a work in progress. If you have any questions, join the
[Mixxx Zulip chat](https://mixxx.zulipchat.com) to get live help from
developers*

## Prerequisites

First, get the code of Mixxx [using Git](using%20Git).

To understand this guide, you should have a working experience with a
systems language like C, C++, or Java. You should be able to get by with
trial and error even if you don't know these. It will help significantly
if you have some experience with the [Qt Framework](http://doc.qt.io/)
which Mixxx uses extensively.

We also highly recommend that you use a C++ IDE rather than a text
editor. Mixxx is a huge project spread across hundreds of source code
files. IDEs index the entire code tree and allow you to jump from where
a function is used to its definition, even if that is in another file
(which it often is). Without this powerful tool, you will spend a lot of
time simply finding the code you're looking for instead of understanding
what it is doing. We have [guides](developer%20tools#using%20IDEs) for
setting up several IDEs to work on Mixxx, but feel free to use whatever
IDE you prefer.

Please check out the [Learning resources](Learning%20resources) page to
learn about the basics and underlying concepts

## Core Infrastructure

These are the fundamental building blocks used almost everywhere in
Mixxx. You should skim these first so that you aren't confused when you
see them in other sections.

  - [Control System (ControlObjects)](developer_guide_control)
  - [Config System (ConfigObject, ConfigKey)](developer_guide_config)

## Major Subsystems

  - [Startup](developer_guide_startup)
  - [Library](developer_guide_library)
  - Shoutcast
  - [Mixing Engine](developer_guide_engine)
  - [Deck/Sampler Processing](developer_guide_engine_player)
  - [Effects Framework](developer_guide_effects)
  - SoundManager (OS audio interface)
  - SoundSource (per-format audio
    decoding)
  - [Analysers (beat detection, key detection, waveform analysis,
    replaygain, etc.)](developer_guide_analysers)
  - Vinyl Control
  - Controllers (MIDI, HID,
    etc.)
  - Keyboard Control
  - Preferences Dialogs
  - Waveforms
  - [Skins](start#skin_documentation)
  - [GUI Widgets (non-skin)](developer_guide_widgets)
