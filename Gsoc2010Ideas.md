# Google Summer of Code 2010 Project Ideas

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of Code 2010](http://socghop.appspot.com/). Each
of these projects represents something that we think would make a really
big difference to our users and that we as a development team are really
excited about. For advice on how to get in touch and how to apply, you
should read [gsoc2010advice](gsoc2010advice).

## Skinning Engine Prototype

### Overview

Over the last 5 years, Mixxx has grown to provide useful functionality
for an increasingly diverse group of DJs. Some of our commercial
competitors have adapted to meet the needs of these same types of DJs,
but at a cost of increasing their user interface complexity. As we like
to put it, the number of knobs per square inch of UI in audio
applications tends to infinity. As a result, the learning curve for
audio applications is often quite steep, and in order to keep Mixxx
accessible to new DJs, Mixxx's UI must not suffer the same fate.

We recognise that changing the whole UI is a huge task, so the goal of
this project is to explore and develop a prototype of a more scalable
user interface that allows different types of DJs to always have the
simplest, easiest possible UI. This project will also aim to solve
technical shortcomings present in Mixxx's existing skinning engine.
Regular feedback from Mixxx's skin artists during development will help
ensure the project direction is aligned with the vision of our artists.

This project will involve working heavily with Qt. It is a very open
ended project ideal for an ambitious student who is interested in user
interface design.

### Project Deliverables

  - Analysis of existing user interface, commercial competitors' UIs,
    and existing proposed solutions
    [1](http://mixxx.org/forums/viewtopic.php?f=1&t=729)
    [2](http://mixxx.org/wiki/doku.php/skinning_engine)
    [3](http://www.mail-archive.com/mixxx-devel@lists.sourceforge.net/msg02654.html)
    [4](http://article.gmane.org/gmane.comp.multimedia.mixxx.devel/2804).
  - Implement a working prototype user interface for Mixxx
    1.  Must provide widget grouping for like controls
    2.  Widget groups' visibility must be toggleable (eg. so that
        looping controls can be hidden)
    3.  Widget groups must be re-arrangeable.
    4.  Must provide resizable main window

## Sampler Decks

### Overview

Mixxx currently has 2 main decks for playing audio tracks. Many DJs like
to incorporate sample tracks into their sets so that they can enhance
their sets by playing extra samples on command. The goal of this project
is to support this workflow by adding multiple samplers into Mixxx.

This project will require the student to work on both the audio core and
user interface of Mixxx. It will give the student an opportunity to take
their design all the way through implementation to real-world use and to
hear user feedback on their work.

### Project Deliverables

  - Implement Mixxx-engine support for multiple samplers
    1.  Model a new Sampler class off of the Player class
    2.  Provide code for other parts of Mixxx (e.g. the GUI widget) to
        control the Sampler 
  - Implement a Sampler GUI widget that displays: 
    1.  The overview waveform of the sample audio (using our
        pre-existing waveform widgets)
    2.  Buttons to play/pause the sample, and a button to enable looping
        of the sample 
    3.  Button to eject the current track from the sampler

## DVS Mode / External Mixer Mode

### Overview

Many Mixxx users would like to use Mixxx with an external mixer instead
of making use of Mixxx's mixing engine to mix the output of each audio
deck. The user may optionally want to disable CPU-intense processing
such as Effects and EQ processing in favor of using their mixer. This
project entails redesigning the master mixing portion of the Mixxx
engine to support enabling or disabling various mixing features.

This project is focussed on the audio processing parts of Mixxx. Ideal
for a student interested in the technical aspects of low-latency audio
software development.

### Project Deliverables

  - Implement Mixxx-engine support for granularly enabling or disabling
    features such as the mixing of deck outputs and the EQ or effects
    processing of each deck.
  - Enhance the Mixxx preferences dialog to provide a UI for configuring
    the mixing engine. 
    1.  Must allow for configuring the output soundcard of each Mixxx
        deck
    2.  Must provide options for enabling and disabling engine features
        such as Effects and EQ

## Plug and Play MIDI Mode / Community MIDI Mappings

### Overview

Mixxx currently supports a wide-range of hardware MIDI controllers that
DJs can use to perform with. Each supported MIDI controller has a
"mapping" file that is bundled with Mixxx, but this mapping must be
manually selected by the user before their controller works. The aim of
this project is to increase the usability for new users by automatically
selecting the correct MIDI mapping and to provide an intelligent
workflow for when an unsupported MIDI device is connected.

This project will involve a lot of time thinking about use cases,
dealing with users and understanding their requirements. It would be a
great opportunity for a student to get involved with the Mixxx
community. The student will also have the opportunity to borrow a MIDI
controller from the development team for the duration of the project.

### Project Deliverables

  - Implement auto-selection of MIDI mappings based on connected MIDI
    devices.
  - For unsupported devices, implement a UI and simple server-side
    functionality to:
    1.  Check mixxx.org for additional community-provided mappings.
    2.  Allow ratings and comments to be made on community-provided
        mappings.
    3.  Allow user-created mappings to be uploaded to mixxx.org.

## LADSPA Effects

### Overview

A previous GSoC student wrote a LADSPA plugin interface for Mixxx, but
did not have time to write a user interface. Effects are one of our top
requested features so this project is very high impact and will allow
Mixxx users to be much more creative with their DJ sets.

This project will involve working heavily with Qt in a highly visible
role and would be ideal for a student interested in user interface
design and dealing with users.

### Project Deliverables

  - Complete plugin integration into the GUI
    1.  Must allow selection and mapping of available LADSPA plugins
        into GUI effects slots
    2.  Must connect GUI controls to the mixing engine to change
        parameters of loaded plugins
  - Design user-friendly way to load new LADSPA plugins downloaded from
    the Internet into Mixxx
    1.  Must allow a user to select a LADSPA plugin to load from their
        hard drive

## Something Else\!

### Overview

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it.

### Project Deliverables

  - Something awesome
