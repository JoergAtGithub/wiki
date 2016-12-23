# Behringer CMD Micro

[[/media/cmd-micro.jpg|]]

[[/media/hardware/behringer-cmd-micro-dj-midi-controller.svg|]]

  - ~~[Manufacturer's product
    page](https://www.music-group.com/Categories/Behringer/Computer-Audio/DJ-Controllers/CMD-MICRO/p/P0AJR/)~~

The *Behringer CMD Micro* is a simple controller for basic two-channel
mixing. This device does not have a built in sound card, so it would
require a [splitter cable](hardware%20compatibility#splitter%20cables)
or [separate sound card](hardware%20compatibility#usb%20sound%20cards)
to be able to preview tracks in headphones.

## Mapping description

  - **Cue**, **Play/Pause**, **Sync**, **Load A**, **Load B**, the
    **Level** / **Browse** knobs, and the crossfader all behave as
    labeled.
  - **Cue A** and **Cue B** send the respective track to the headphones.
  - The outer most sliders control the playback speed.
  - The inner most vertical sliders control the track's volume.
  - The **1**, and **2** buttons begin a four and eight beat loop,
    respectively.
  - The **Pitch Bend** buttons are configurable with an option in the
    JavaScript file:
  - By default they temporarily adjust the playback rate.
  - If the option `PitchBendsKey` is true, they instead shift the key of
    the track. If both are pressed simultaneously, the key is reset to
    default.

### Jog Wheels

The jog wheels are touch enabled. When the top is pressed, they emulate
turntable scratching. When the side is touched, they affect the playback
speed (jog).
