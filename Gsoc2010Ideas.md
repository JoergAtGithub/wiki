### Google Summer of Code 2010 Project Ideas Page

#### Skinning Engine Prototype

#### Sampler Decks

##### Overview

Mixxx currently has 2 main decks for playing audio tracks. Many DJs like
to incorporate sample tracks into their sets so that they can enhance
their sets by playing extra samples on command. The goal of this project
is to support this workflow by adding multiple samplers into Mixxx.

##### Project Deliverables

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

#### DVS Mode / External Mixer Mode

##### Overview

Many Mixxx users would like to use Mixxx with an external mixer instead
of making use of Mixxx's mixing engine to mix the output of each audio
deck. The user may optionally want to disable CPU-intense processing
such as Effects and EQ processing in favor of using their mixer. This
project entails redesigning the master mixing portion of the Mixxx
engine to support enabling or disabling various mixing features.

##### Project Deliverables

  - Implement Mixxx-engine support for granularly enabling or disabling
    features such as the mixing of deck outputs and the EQ or effects
    processing of each deck.
  - Enhance the Mixxx preferences dialog to provide a UI for configuring
    the mixing engine. 
    1.  Must allow for configuring the output soundcard of each Mixxx
        deck
    2.  Must provide options for enabling and disabling engine features
        such as Effects and EQ

#### Plug and Play MIDI Mode / Community MIDI Mappings

##### Overview

Mixxx currently supports a wide-range of hardware MIDI controllers that
DJs can use to perform with. Each supported MIDI controller has a
"mapping" file that is bundled with Mixxx, but this mapping must be
manually selected by the user before their controller works. The aim of
this project is to increase the usability for new users by automatically
selecting the correct MIDI mapping and to provide an intelligent
workflow for when an unsupported MIDI device is connected.

##### Project Deliverables

  - Implement auto-selection of MIDI mappings based on connected MIDI
    devices.
  - For unsupported devices, provide a UI that helps make that
    controller functional.
    1.  Must check mixxx.org for additional community-provided mappings.
    2.  Must allow ratings and comments to be made on community-provided
        mappings.
    3.  Must allow the creation of mappings using our existing MIDI
        Learning Wizard.
    4.  Must allow user-created mappings to be uploaded to mixxx.org.

#### Finish LADSPA Effects Work

#### Ableton Live Integration
