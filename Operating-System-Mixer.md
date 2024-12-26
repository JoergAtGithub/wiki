# Operating System Mixer

To adjust the level of Mixxx's outputs and inputs, the main and
headphone gain knobs in Mixxx should be used only as a last resort.
Ideally, for the best sound quality, Mixxx and your sound card would
always be at their maximum level without clipping and a control on the
amplifier or speakers would be used to adjust loudness (see [the
manual](http://mixxx.org/manual/latest/chapters/djing_with_mixxx.html#setting-your-levels-properly-gain-staging)
for a technical explanation). Sometimes this is not accessible though.
In that case, the sound card may be the best place to adjust the
loudness.

Many sound cards have physical knobs on them that control the gains of
the outputs and inputs. Sound cards built into computer motherboards
don't have these and sometimes sound cards built into DJ controllers
don't either. However, they may still have controls accessible through
the operating system's mixer program. How to access this is different on
every operating system:

  - **Linux**: Run the command 'alsamixer' in a terminal, press F6 to
    select the sound card, and press the up & down arrow on your
    keyboard to adjust the slider labeled "Master" (or sometimes "PCM
    Front"). Do not use a GUI program such one launched by clicking a
    speaker icon in the system tray. These typically control
    PulseAudio's software gain, not the sound card's controls.
  - **Windows**: Click the speaker icon in the system tray. Click
    "Mixer" in the popup. In the mixer window that comes up, in the
    Device column, in the drop down menu between the top of the volume
    slider and the bottom of the icon at the top of the column, select
    the sound card. Click and drag the volume slider to adjust the sound
    card's output. FIXME: Is this also the case with ASIO drivers?
  - **Mac OS X**: Adjust the volume by clicking the speaker icon in the
    system tray. FIXME: Add more details

FIXME: Add screenshots for each OS
