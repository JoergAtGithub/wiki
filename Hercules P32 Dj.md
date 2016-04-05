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
  - [Digital DJ Tips
    review](http://www.digitaldjtips.com/2016/03/review-video-hercules-p32-dj-grid-pad-controller/)

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. However, it recommended to install [the
driver](https://support.hercules.com/en/product/p32dj-en/) on Windows to
be able to use the [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api).

Thanks to Hercules for supporting the development of this mapping by
providing a controller.

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
**turn the volume of the main output all the way up in your OS mixer
program:**

  - GNU/Linux: Run the command 'alsamixer' in a terminal, press F6 to
    select the Hercules P32 DJ sound card, and press the up arrow on
    your keyboard to turn the slider labeled "PCM Front" all the way up.
  - Windows: Click the speaker icon in the system tray. Click "Mixer" in
    the popup. In the mixer window that comes up, in the Device column,
    in the drop down menu between the top of the volume slider and the
    bottom of the icon at the top of the column, select "Spekaers
    (Hercules P32 DJ)". Click and drag the volume slider to its top.
  - Mac OS X: Adjust the volume by clicking the speaker icon in the
    system tray.

## Mapping description

This mapping is a work in progress, but is in a usable condition. It
mostly works as labeled on the controller, but some functionality is
different and there is additional functionality not labeled on the
controller.

  - **Browse encoder**: scrolls through library. Pushing toggles big
    library view. Turning with shift controls the cue/main mix going to
    the headphone output. Pushing with shift toggles split cue mode
    (left ear of headphone output plays cue signal, right ear plays main
    signal).
  - **Record button**: toggles recording on and off. With shift, toggles
    between decks 1 & 3 on the left and decks 2 & 4 on the right.
  - **Slip button**: not mapped yet
  - **Loop/Tempo encoder**: turning left halves loop size; turning right
    doubles loop size. Pushing (de)activates a loop. For loops 1 beat or
    less, the loop only stays active while the encoder is pushed down.
    Turning while holding shift moves the loop. If the loop is 1 beat or
    larger, it moves the loop by 1 beat; if the loop is smaller than 1
    beat, it moves the loop by the size of the loop.
  - **Filter/Move encoder**: turning controls the filter. Turning with
    shift adjusts the pitch, or with keylock on, just the tempo. Pushing
    while holding shift resets the pitch to the track's default.
  - **Effects knobs and buttons**: not mapped yet
  - **Pad grid**: Only the Hotcue layer is mapped yet. Press the Hotcue
    button to activate this layer if the Hotcue button is not lit.
    Pressing an unlit pad in the grid sets a hotcue. Pressing a lit pad
    activates that hotcue. Pressing a lit pad with shift deletes that
    hotcue.
  - **Shift + sync**: toggle quantize
  - **Shift + cue**: toggle keylock
  - **Shift + load**: ejects a track from the deck
  - **EQ knobs, volume faders, crossfader, headphone button, play, cue,
    sync, and load** all behave as labeled.
