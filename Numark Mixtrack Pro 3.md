# Numark Mixtrack Pro 3

![http://www.numark.com/images/sized/images/product\_large/MixtrackProIII\_ortho\_web\_1200x750-624x390.jpg](http://www.numark.com/images/sized/images/product_large/MixtrackProIII_ortho_web_1200x750-624x390.jpg)

  - [Manufacturer's product
    page](http://www.numark.com/product/mixtrack-pro-3)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=7286)

The Numark Mixtrack 3 and Numark Mixtrack Pro 3 are the same controller
except that the Pro version has an integrated sound card and costs $100
more.

## Controller Mapping for script by Stéphane Morin - Version 1, beta 8

found in the following forum post:
<http://mixxx.org/forums/viewtopic.php?f=7&p=27997&sid=0ea9ad1cdef4e0a452f0c17aa113145c#p27991>

[[/media/numarkmixtrackpro3mapping.gif|]]

### Configuration options

Configuration options can be set in the mapping. You will need to edit
the values below at the very top of the JavaScript file
“Numark-Mixtrack-3-scripts.js” and save changes. Allowed values are
“**true**” or “**false**”

**TrackEndWarning**: Default value: true When you reach the end of the
track, the jog wheel Button will flash. If value is "false": there will
be no flash of Jog Wheel Button at the end of the track.

**iCutEnabled**: Default value: true iCut mode simulates a scratch
routine with the jog wheel. When the jog wheel is turned back, the
crossfader closes; when the jog wheel is turned forward the crossfader
will open. Shift needs to be enabled and Wheel button is activated and
you are scratching. As a visual reference, TAP LED and Wheel button LED
will be ON.

**fastSeekEnabled**: Default value: true Enables fast seek with Jog
Wheel platter. This is available only when Wheel is Off and Shift is
enabled.

**smartPFL**: Default value: true When set to true, when the Load button
is used, the Cue channel of the track being loaded is activated and the
other Cue channel is deactivated. Cue channel can be activated directly
with Cue/PFL button.

**printComments**: Default value: true Used for debugging, print
comments on prompt screen

**beatlooprollActivate**: Default value: false Use beatlooproll instead
of beatloop command when using AutoLoop buttons (Performance Pads)

**PADLoopButtonPressed**: Default value: false When "false" is set, loop
will start on press and stop on 2nd press. When "True" is set: Loop
stops when finger release.

**PADSamplerButtonPressed**: Default value: false When "false" is set,
Sampler will start on press and stop on 2nd press. When "True" is set:
Sampler stops when finger release.

**OnBeatActiveFlash**: Default value: true When “true” is set: TAP LED
will flash to the beat if Shift Lock is not enabled

### Mapping

#### 1.Browser Knob:

Rotate this knob to cycle through tracks in main library window. Press
the Knob to load selected track into first stopped deck. **Shift +
Turn:** allows selecting Play Lists and side navigation bar items. //
**Shift + Push:** opens / closes selected side navigation bar item.
