# Hercules P32 DJ

![http://www.hercules.com/fichier/h\_photo/1492/photo\_file\_p32dj\_top.png](http://www.hercules.com/fichier/h_photo/1492/photo_file_p32dj_top.png)

  - [Manufacturer's product
    page](http://www.hercules.com/uk/advanced-controllers/bdd/p/258/hercules-p32-dj/)
  - [Manufacturer's support and downloads
    page](https://support.hercules.com/en/product/p32dj-en/)
  - Mapping files on GitHub: [Hercules P32
    DJ.midi.xml](https://raw.githubusercontent.com/Be-ing/mixxx/hercules_p32_mapping/res/controllers/Hercules%20P32%20DJ.midi.xml)
    and
    [Hercules-P32-scripts.js](https://raw.githubusercontent.com/Be-ing/mixxx/hercules_p32_mapping/res/controllers/Hercules-P32-scripts.js)
    (save both files to your [controller mapping file locations\#user
    controller mapping
    folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder))
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=8132)
  - [DJTechTools
    review](http://djtechtools.com/2016/06/22/can-pads-replace-jogs-hercules-p32-dj-controller/)
  - [Digital DJ Tips
    review](http://www.digitaldjtips.com/2016/03/review-video-hercules-p32-dj-grid-pad-controller/)

The Hercules P32 DJ is a relatively compact DJ controller with a
built-in sound card. Rather than jog wheels, it has a 4 x 4 multicolor
(red/blue/purple) pad grid for each deck. The pad grids can be switched
between 4 different layers to perform a variety of functions.

Thanks to Hercules for supporting the development of this mapping by
providing a controller.

## Compatibility

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. However, it recommended to install [the
driver](https://support.hercules.com/en/product/p32dj-en/) on Windows to
be able to use the [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api).

## Sound card setup

This device has a built in 4 channel output sound card. There are 2 RCA
outputs for the main output and a 1/4" TRS stereo headphone jack. There
are buttons in the center of the controller that adjust the sound card's
headphone output volume. These do not adjust the headphone gain in
Mixxx.

There is no master output volume control on the device, but the master
output volume of the sound card can be controlled from the OS mixer. The
device comes with the main output set to 45%. So, for the best [gain
staging](http://mixxx.org/manual/latest/chapters/djing_with_mixxx.html#setting-your-levels-properly-gain-staging),
**turn the volume of the main output all the way up in your [operating
system mixer](operating%20system%20mixer) program**.

## Mapping description

This mapping is a work in progress, but is in a usable condition. It
mostly works as labeled on the controller, but some functionality is
different and there is additional functionality not labeled on the
controller.

### User configurable options

There are a few user configurable options available for you to
customize. You can change these by opening the Hercules-P32-scripts.js
file in your [controller mapping file locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder)
with your text editor of choice (such as Notepad, TextEdit, Kate, or
gEdit) and editing the lines at the very top of the file.

  - **defaultLoopSize**: loop size (in beats) when Mixxx starts
  - **defaultBeatJumpSize**: beat jump size when Mixxx starts
  - **loopEnabledDot**: whether to use the dot on the loop size LED
    display to indicate that a loop is active. This restricts loop sizes
    to 2-32 beats and may be helpful if you never use loops less than 2
    beats long. Otherwise the dot indicates a loop size equal to 1/(\#
    on the LED display).
  - **samplerCrossfaderAssign**: whether to assign the samplers to the
    crossfader. If true, the samplers controlled by the left pad grid
    are assigned to the left of the crossfader and the samplers
    controlled by the right pad grid are assigned to the right of the
    crossfader.

### Encoders

The encoders do not behave exactly as labeled.

  - **Browse encoder**: scrolls through library. Pushing toggles big
    library view. Turning with shift controls the cue/main mix going to
    the headphone output. Pushing with shift toggles split cue mode
    (left ear of headphone output plays cue signal, right ear plays main
    signal).
  - **Loop/Tempo encoder**: turning left halves loop size; turning right
    doubles loop size. Pushing (de)activates a loop. For loops 1 beat or
    less, the loop only stays active while the encoder is pushed down.
    Turning while holding shift moves the loop. If the loop is 1 beat or
    larger, it moves the loop by 1 beat; if the loop is smaller than 1
    beat, it moves the loop by the size of the loop.
  - **Filter/Move encoder**: Turning adjusts the pitch, or with keylock
    on, just the tempo. Pushing resets the pitch to the track's default.
    Turning with shift jumps forward/backward by beats (default 4
    beats). Hold shift, push, and turn to select how many beats to jump
    by, shown on the LED display on the controller. When the encoder is
    released, the LED display goes back to showing the loop size. 

### Effects

#### Mixxx 2.0

The effects controls on the left control Effect Unit 1, the controls on
the right control Effect Unit 2. This does not change when decks are
toggled between decks 1/3 or 2/4.

Press ON/MACRO buttons to activate the Effect Unit on Decks 1-4.

Turn the FX AMOUNT knobs to adjust effect parameters. By default, the
knobs control the parameters of the first effect in the effect unit. The
other effects can be selected with the Slicer pad mode (see below).

Turn the Dry/Wet knob to control the mix of the effect sounds with the
source deck(s). Shift + Dry/Wet adjusts the super knob for the Effect
Unit.

Be warned that soft takeover does not work for the effect parameter
knobs when switching between effects due to [a bug in
Mixxx](https://bugs.launchpad.net/mixxx/+bug/1479008). Soft take over
does work for switching between dry/wet and the superknob though.

#### Mixxx 2.1

The effects controls on the left control Effect Unit 1 and the controls
on the right control Effect Unit 2. When the pad grid is in Slicer mode,
the top row has switches to enable the Effect Unit on decks 1-4. The
bottom row has switches to enable the Effect Unit on the headphone,
master, microphone, and auxiliary signals (in that order left to right).
Mixxx remembers which signals an Effect Unit is enabled on across
restarts.

The MACRO button toggles whether the effect unit shows all the
parameters of each effect or just the metaknobs.

When the effect unit shows the metaknobs without the individual
parameters of effects, the P32's knobs control the metaknob of each
effect in the unit. The ON buttons control whether each effect is
enabled. Pressing an ON button with shift switches to the next available
effect.

When the effect unit shows all the parameters of the effects, the ON
buttons control the enable switches for the effect like when the
parameters are hidden. By default, the knobs control the metaknobs of
each effect. They can be switched to control the first 3 parameters of
an effect by focusing that effect. Focus an effect by pressing shift +
ON when the parameters are showing or clicking the focus button on
screen. The focused effect has a box around it on screen. Unfocus an
effect and go back to controlling the metaknobs by pressing shift + ON
for the focused effect.

Turn the Dry/Wet knob to control the mix of the effect sounds with the
source deck(s). Shift + Dry/Wet adjusts the super knob for the Effect
Unit.

### Other controls

  - **Record button**: toggles recording on and off.
  - **Slip button**: toggles slip mode on and off for all decks. With
    shift, toggles between decks 1 & 3 on the left and decks 2 & 4 on
    the right.
  - **Pad grid**: Press the Hotcue/Loop/Slicer/Sampler buttons to
    activate different modes
  - **Hotcue mode**: Press an unlit pad to set a hotcue. Pres a red pad
    to activate a hotcue. Press a red pad with shift to delete a hotcue.
  - **Loop mode**: Control manual loops and other miscellaneous
    functions. On the top row, from left to right, the pads set the loop
    in point, loop out point, and toggle the loop (without changing its
    size). On the bottom row, the two purple buttons temporarily
    decrease/increase the playback speed while they are held down for
    beatmatching. The button to the right of those shifts the beat grid
    to the current position. The button on the right toggles quantize. 
  - **Slicer mode**: various controls for effects. The bottom row
    toggles the effect unit on the headphones, master mix, microphone 1,
    and auxiliary input 1 (from left to right). In Mixxx 2.0 (not 2.1),
    the top three rows each control an individual effect in the effect
    unit, allowing you to set up effect chains. (These are not visible
    in the LateNight skin). The left button toggles whether that effect
    is enabled (the whole effect unit still has to be enabled for a deck
    for it to be audible). With shift, the left button resets the
    effect's parameters to their default values. The two purple buttons
    in the middle scroll through the available effects. The button on
    the right sets the parameter knobs to control that effect's
    parameters. 
  - **Sampler mode**: Press an unlit pad to load the track selected in
    the library to that sampler. Pads are blue when the sampler is
    loaded but not playing and red when playing. Press a blue pad to
    play the sample from its cue point. Press a red pad to jump back to
    the sample's cue point. Press a red pad with shift to stop a playing
    sample. Press a blue pad with shift to eject a sample. Note that
    samplers are independent from decks; the left grid controls samplers
    1-16 and the right grid controls samplers 17-32. 
  - **Shift + sync**: sync beats without enabling sync lock
  - **Shift + play**: go to beginning of track and stop
  - **Shift + load**: ejects a track from the deck
  - **EQ knobs, volume faders, crossfader, headphone button, play, cue,
    sync, and load** all behave as labeled.
