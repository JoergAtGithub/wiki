## Student Project Ideas for Google Summer of Code 2023

This page lists the suggested tasks to build a 175 hour (medium sized) or 350 hour (large project) for [Google Summer of Code 2023](https://summerofcode.withgoogle.com/). The ideas are already assigned to example projects, but you are encouraged to use them for building your own project adding your own ideas and make it suit perfectly to you, your skills and your time line.

If you are interested in applying to GSoC, read [GSoC Advice](gsocadvice)
before applying or getting involved. Only beginner contributors that are active members
of the Mixxx community are accepted. If this is not the case yet, just
say hello at <https://mixxx.zulipchat.com> and discuss your Ideas and
discus cases with us.

# Spin-Up/Spin-Down effect

Some Controller mappings have implemented a Spin-Up/Spin-Down to mimic the inertia of a turn table. 
This should be moved into the engine, so that it is accessible without a controller.

Part of the project is to record the spin up of a real turn table to get to know of the real acceleration curve and model this via software. You may also deal with the BPM sync feature, in a way that the spin up and down integrates faultlessly into a mix. 
 
https://github.com/mixxxdj/mixxx/issues/8867

* **Expected Outcome:** A flawlessly working spin up and down effect accessible without controller
* **Skills:** Good understanding of sound processing, C++
* **Possible Mentor:** 
* **Difficulty:** Medium 
* **Size:** 350 h

 
# Scratch smoothing

Our scratching algorithm suffers from jitter noise created by the latency of the midi messages. It also suffers from a so called sticker drift, an incrementing offset shifting away form the original scratch sample. 
Part of this project is to filter the discrete messages from the controller in a way that you can either "play" the track without much wobbling by turning the jog wheel, and keep the position during scratching. 

We may also make use of the time stamps of the midi messages. https://github.com/mixxxdj/mixxx/issues/6951

The required controller can be provided as a loan.

* **Expected Outcome:** Wobble fee scratching using a joggwheel
* **Skills:** Good understanding of real time processing, C++
* **Possible Mentor:**
* **Difficulty:** Hard
* **Size:** 350 h

# Sharp Scratching

Currently crossfader changes are stretched on audio buffer time to avoid pop sounds. 
This is too long for some scratching styles. During this project you need to dive into the audio engine code find the code that is responsible for crossfading and make it independent from the audio buffer size. 

 https://github.com/mixxxdj/mixxx/issues/8899

* **Expected Outcome:** Cut type crossfader curve, suitable for scratching.
* **Skills:** Good understanding of sound processing, C++
* **Possible Mentor:**
* **Difficulty:** Medium 
* **Size:** 175 h

# Resample options

Mixxx uses a linear resample when scratching. This is blazing fast, but the sound can be improved. 
Here Mixxx should provide more resample options. This project involves to review the already used resample libraries RubberBand and Soundtouch and compare them with other candidates. The one with the best Sound/CPU load trade of shall be selected. Make sure that it supports on the fly changing of the sample rate without artefacts. This project may also involve to contribute a missing feature to such library.  

https://github.com/mixxxdj/mixxx/issues/9328


* **Expected Outcome:** Optional replacement of the linear resampler.
* **Skills:** Good understanding of sound processing, C++
* **Possible Mentor:**
* **Difficulty:** Easy
* **Size:** 175 h

# Graceful recovery of controllers

If a controller is accidentally unplugged it has to be manually reconfigured, which is a party stopper. 
Mixxx should do it automatically. This project has two stages, fist behave like a real DJ: fix the issue but faster. So the the time of silence on the dance floor is kept short. The advance stage of this project is to implement real Hot Plug And Play. In order to that you likely need to touch the low level inside third party libraries. 

The required controller can be provided on loan.

 
* **Expected Outcome:** Re-power the controller and continue to use it, on your target platform. 
* **Skills:** Good understanding of the USB stack, C++
* **Possible Mentor:** Daniel Schürmann
* **Difficulty:** Easy / (Hot Plug And Play = Difficult)  
* **Size:** 175 h  / (Hot Plug And Play = 350 h)

# Graceful suspend/resume support: 

Mixxx should be able to continue playing after cumming back from the suspend state of the PC. This requires to detect the faulty state after resume and reinitialize the required parts of Mixxx.   
https://github.com/mixxxdj/mixxx/issues/9099

* **Expected Outcome:** The sound output shall continue after sleep. 
* **Skills:** Good understanding of the USB stack, C++
* **Possible Mentor:** 
* **Difficulty:** Difficult
* **Size:** 175 h

# Auto Updater for Windows and MacOs

Mixxx should look up our download page and automatically update itself in case an update is available. This shall be implement using Sparkle on MacOS and WinSparkle on windows like Wireshark.  

* **Expected Outcome:** A working update notifier, frontend and server part. 
* **Skills:** Experience with MacOs and Windows, C++
* **Possible Mentor:**
* **Difficulty:** Easy 
* **Size:** 175 h

# Track suggestion feature

Mixxx shall suggest compatible tracks matching the current playing one. The feature may use existing meta data like bpm genre and key or tab online resources like LastFM and similar. https://github.com/mixxxdj/mixxx/issues/9328

* **Expected Outcome:** A dynamically changing list of suggested tracks.
* **Skills:** Experience with web services, C++
* **Possible Mentor:**
* **Difficulty:** Medium
* **Size:** 350 h

# First class Pipewire support

Currently Mixxx supports Pipewire via Portaudio and Jack. These two gue layers leads to a limited feature support with a weak user experience. 
In this project you need to consider solutions to improve the situation. Desired features are
* Better audio routing using external tools
* Route sound to/from other applications from inside Mixxx
* Access to DAC timing info of the soundcards 
* Acesss to analog volume settings of the soundcards.   

* **Expected Outcome:** A rock solid interface to Pipewire.
* **Skills:** Experience with Audio processing and  C++
* **Possible Mentor:**
* **Difficulty:** Difficult
* **Size:** 350 h

# Support of RTMP and SRT as additional streaming protocols

Mixxx supports the Shoutcast and Icecast protocols for radio DJs, but not the
streaming protocols used by platforms like Twitch, Youtube or Mixcloud.

* They use the RTMP protocol, which is also the most common input format for OBS.
* While RTMP is still the defacto standard, OBS reccomends to use SRT in future.
* Both protocols are implemented in FFMPEG, which is also used inside Mixxx for other purposes.

* **Expected Outcome:** A rock solid RTMP and SRT audio streaming output.
* **Skills:** Experience with FFMPEG and C++
* **Possible Mentor:**
* **Difficulty:** Medium
* **Size:** 175 h

# Track encoding offset correction

Different codecs used to encode sound files introduce slight shift in the audio samples comparing the input with the output stream. 
This is no issue when you use always the same file and the same decoder. It becomes however an issue when the decoder is updated or replaced because than all stored metadata like waveform, beat-grids and cue points are no longer at the correct position. To protect against surprises Mixxx has unit-tests to verify that seeks inside that track do not introduce an offset and checks if the fist sound sample can be found at the expected time.  

We have currently the issue that the Microsoft has introduced such a breaking change in Windows 11. https://github.com/mixxxdj/mixxx/issues/11094 In this project we need to investigate the issue and implement a fix so that the stored metadata of a user are still valid after an upgrade to Windows 11. As a project extension, this may also fix an issues that prevents us from moving to ffmpeg as an encoder wrapper where the underlying encoder library is no longer in control of us. 

* **Expected Outcome:** No Beat-Grid offset after Windows 11 update
* **Skills:** Experience and C++
* **Possible Mentor:**
* **Difficulty:** Medium
* **Size:** 175 h (350 h for a general solution) 

# Address sanitizer facilities

Sometimes we have reports of hard to find crashes that my have to do with dangling pointer or other memory addressing issues. When hunting such a general environment that helps to find it would be great. However it is often not worth the effort for that particular issue and that's why we don't have it. 
This project is for contributors who have real experience with such memory sanitizer facility. We like to learn from you, what is reasonable to use and how we can integrate checks in out continuous integration. This may also something integrated in Mixxx itself to have more info users can provide in case of a crash.

* **Expected Outcome:** A new workflow how to deal with crasher bugs along with an improved set of tools. 
* **Skills:** Experience with address sanitizer tools and CMake
* **Possible Mentor:**
* **Difficulty:** Medium
* **Size:** 175 h

# Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it. We recommend
spending more than a few days using Mixxx and participating in the
community to develop a better understanding of areas where Mixxx could
use improvement. Our issue tracker is full of [feature requests](https://github.com/mixxxdj/mixxx/issues?q=is%3Aopen+is%3Aissue+label%3Afeature) and other
ideas scattered throughout, so if you browse through it, you may find
many more ideas for GSoC projects.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!** We
very rarely approve ideas students propose. If you're not already
experienced with DJ equipment, we recommend sticking with one of the
ideas above.
