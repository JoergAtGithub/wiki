# Microphone effects chain

by Aris Stathakis

### Project Overview

My proposal for GSOC 2017 is Microphone effects chain for Mixxx. Mixxx
is the defacto standard in open source world for real time mixing music
tracks. What it currently lacks is a way to seamlessly integrate
microphone input processing, allowing for the dj/presenter to tune the
voice track over mixed music. This would be an ideal solution for
internet radio live broadcasting. In professional setups, a chain of
effects is used in order to tune the speech signal with the rest of the
mix, with a typical chain of a noise gate, noise suppressor, echo
cancellation, ducker. What this project aims to fulfill is the
development and integration of this effects chain into Mixxx. Mixxx has
already an effects chain for the music mix, with selectable input
source. In the same manner, the mic input effect signal path would be
developed and placed underneath the music effects, as a UI element that
will be toggled from a toggle button on bottom left of the screen, in
the same way that the music effects views are toggled. This means that
as an add on this feature will be unobtrusive and can easily integrate
with the rest of the existing UI elements. A mockup of the proposed
speech processing chain is illustrated in the following figure.

[[/media/mockup.svg|]]

The whole development will be done in C++ as Qt framework is used for
Mixxx development and there are also many existing audio processing
libraries in C++. Existing open source projects that can be used for
reference are the speexdsp library which implements speech processing
components for speex codec, and WebRTC AEC library.

### Timeline

What follows is the proposed timeline of the project spanning all 11
weeks of Google Summer of Code.

##### Bonding period

Brainstorm with the mentors features of the project and implementation
details, review and familiarize with all the modules to be utilized for
the project, setup test and verify all the necessary tool-chain
components. This is the ideal period also to start communicating with
the user community the developemnt of the new features and search for
feedback and design some user stories as well as some UI mockups of the
new features.

##### week 1-2

A simple audio processing effect will be coded such as a noise gate,
starting from existing audio effects codebase, exploring the best way to
integrate the new features into Mixxx. In parallel to development, a
general guide for Mixxx signal processing development will be started in
the wiki, so as future contributors can have an easier way to start
developing audio effects.

##### week 3 - 4

The new UI element with the mic effects chain will be developed,
integrated and tested together with the existing UI elements. This is a
nice chance to think upon improvements on other elements and consider
solving as many relevant existing bugs as possible. Also a UI element
design guide for a new togglable element can be authored and added to
the Mixxx wiki.

##### week 5

Prepare for mid-term evaluation, and campaign the up to date results of
the project to the community. At this point it would be very nice to
have some feedback from users, and consider this feedback in the
following brainstorming.

##### week 6 - 7

Up to this point the project will have manage to demonstrate and
document a clean way to add new dsp effects elements to Mixxx, such as
an audio gate. At this point the actual development/porting of the
speech processing blocks will be started, decided upon brainstorming
with the mentors and user feedback. Main intention is to start with
porting speexdsp noise suppression algorithm as it would be a great tool
for controlling the dj/producer environment noise, resulting in a
professional result.

##### week 8

Porting of speexdsp acoustic echo cancellation.

##### week 9

Development testing and integration of other speech processing blocks
such as a tunable audio ducker for auto lowering the music mix volume
when input at microphone source is over a tunable threshold with a
certain envelope.

##### week 10-11

Prepare for final project submission, documenting the new features in
the Mixxx manual, updating the wiki guides for the rest of the
developers, and a small time buffer to keep project in control. If the
project delivers in time, a live radio show using the implemented
features on Mixxx will be presented demonstrating new Mixxx capabilities
and celebrate with a fine music mix.

### Weekly reports

##### week 1-3

A dataset for evaluating the work on microphone signal processing chain
was collected and can be found here:
[dataset](https://drive.google.com/open?id=0B1dik9fZbclrNHBsTVZFVUFRNFk).
This dataset is a set of recordings for two speakers for two different
types of microphones for different usecases. More detailed info can be
found in the readme file inside the dataset folder.

In order to better understand mixxx engine and mixxx native effects, a
[utility effect](https://github.com/mixxxdj/mixxx/pull/1284) was
developed and an accompanying article in the wiki was started
demonstrating a practical way on how an native effect can be developed.
[Mixxx Effect Development
Example](https://mixxx.org/wiki/doku.php/effect_development_example)

Also a minimal framework have been developed in python for prototyping
and tuning audio dsp algorithms in python with numpy and other existing
python packages such as adaptfilt and speexdsp-python. The pull request
can be found [here](https://github.com/mixxxdj/mixxx/pull/1290)

The framework supports both file input/output and realtime audio
processing. For the realtime audio capabilities it requires sounddevice
which requires portaudio.

Currently I am porting CAPS [noise
gate](http://quitte.de/dsp/caps.html#Noisegate) algorithm as a native
mixxx effect in order to gain more experience with mixxx engine.

##### week 4-5

Plan for the next two weeks is to have the noise gate implemented, and
have decided on and implemented a microphone effect rack (help needed
here) that will later be the place in the skin for setting up microphone
effects, and other microphone related settings and possibly be
selectively routed to the main effects rack.
