# Vestax VCI-100MKII

Vestax went out of business in 2014.

  - [Product page in
    archive.org](http://web.archive.org/web/20140809134938/http://www.vestax.com/v/products/detail.php?cate_id=118&parent_id=8)
  - [ASIO driver for Windows in
    serato.com](https://support.serato.com/hc/en-us/articles/203593924-Vestax-Hardware-Drivers-and-Firmware)
  - [Forum thread](http://www.mixxx.org/forums/viewtopic.php?f=7&t=6038)

![vci100mkii.png](vci100mkii.png)

## Mapping for Mixxx 2.0

\[Functions\] in brackets are executed if a shift button of the deck is
pressed.

1.  Set previous effect chain to the EffectUnit \[Select EffectUnit1/2\]
2.  Set next effect chain to the EffectUnit \[Select EffectUnit3/4\]
3.  Parameter1 of Effect1 of the EffectUnit
4.  Parameter2 of Effect1 of the EffectUnit
5.  Parameter3 of Effect1 of the EffectUnit
6.  Wet/dry mix of the EffectUnit
7.  EQ high
8.  EQ mid
9.  EQ low
10. Gain
11. Filter (high pass only)\[1\]
12. Pitch (semitones only)
13. Rate \[Rate by quantized BPM\]
14. Channel fader
15. Cross fader
16. Headphone volume
17. Headphone mix
18. Master volume
19. Scratch
20. Jog (locked in slip mode)
21. Play \[Adjust beatgrid to the current playposition\]
22. Cue \[Adjust beatgrid to match another playing deck\]
23. Cue and Play \[Move beatgrid earlier\]
24. Sync mode \[Move beatgrid later\]
25. Quantize mode \[Zoom in waveform\]
26. Keylock mode \[Zoom out waveform\]
27. Loop in the default length (4 beats at startup) \[Reloop\], or in
    loop *Exit the loop \[Loop out\]*
28. Halve the default length,\[2\] or in loop *Halve the loop* \[Move
    the loop backward by 1/2 beat\]
29. Double the default length, or in loop *Double the loop* \[Move the
    loop forward by 1/2 beat\]
30. Activate \[Clear\] hotcue1
31. Activate \[Clear\] hotcue2
32. Activate \[Clear\] hotcue3
33. Activate \[Clear\] hotcue4
34. Slip mode (affect scratch, loop and hotcue)
35. PFL \[PFL solo\] (if headphone mix is cue or master only then switch
    it)
36. Enable EffectUnit1 \[EffectUnit3\]
37. Enable EffectUnit2 \[EffectUnit4\]
38. Up: previous track and scroll, Down: next track and scroll, Left:
    load to left, Right: load to right, Push: load to first stopped
39. Channel select

## Mapping for Mixxx Development

\[Functions\] in brackets are executed if a shift button of the deck is
pressed. **{Functions} in braces are executed if a shift button of the
other deck is pressed.** Changes after the previous version are in bold.

1.  Set previous effect chain to the EffectUnit, **or if EffectSlotN is
    focused *Set previous effect to it*** \[Select EffectUnit1/2\]
    **{Clear the EffectUnit/Slot}**
2.  Set next effect chain to the EffectUnit, **or if EffectSlotN is
    focused *Set next effect to it*** \[Select EffectUnit3/4\] **{Change
    the focus}**
3.  **Meta knob of the EffectSlot1 \[with enable/disabling\], or if
    EffectSlotN is focused *Parameter1 of it \[Set the link to meta
    knob\]*\[3\]**
4.  **Meta knob of the EffectSlot2 \[with enable/disabling\], or if
    EffectSlotN is focused *Parameter2 of it \[Set the link to meta
    knob\]***
5.  **Meta knob of the EffectSlot3 \[with enable/disabling\], or if
    EffectSlotN is focused *Parameter3 of it \[Set the link to meta
    knob\]***
6.  **Super knob of the EffectUnit \[with enable/disabling\], or if
    EffectSlotN is focused *Parameter4 of it \[Set the link to meta
    knob\]***
7.  EQ high
8.  EQ mid
9.  EQ low
10. **Pitch (up and down to 3 semitones continuously, or in keylock mode
    *discretely*)**
11. Filter (high pass only)\[4\]
12. **Gain**
13. Rate \[Rate by quantized BPM\]
14. Channel fader
15. Cross fader
16. Headphone volume
17. Headphone mix
18. Master volume
19. Scratch **\[Brake (if released before full stop, playback
    resumes)\]**
20. Jog (locked in slip mode)
21. Play **\[Reverse\]**
22. Cue **\[Adjust beatgrid to the current playposition\]**
23. Cue and Play **\[Adjust beatgrid to match another playing deck\]**
24. Sync mode **\[Sync key harmonically with another deck\]**
25. Quantize mode **\[Zoom out waveform\]**
26. Keylock mode **\[Zoom in waveform\]**
27. Loop in the default length (4 beats at startup) \[Reloop\], or in
    loop *Exit the loop \[Loop out\]*
28. Halve **\[Jump backward by\]** the default length,\[5\] or in loop
    *Halve **\[Move it backward by\]** the loop length*
29. Double **\[Jump forward by\]** the default length, or in loop
    *Double **\[Move it forward by\]** the loop length*
30. Activate \[Clear\] hotcue1
31. Activate \[Clear\] hotcue2
32. Activate \[Clear\] hotcue3
33. Activate \[Clear\] hotcue4
34. Slip mode (affect scratch, brake, pause, reverse, loop and hotcue)
35. PFL \[PFL solo\] (if headphone mix is cue or master only then switch
    it)
36. Enable EffectUnit1 \[EffectUnit3\]
37. Enable EffectUnit2 \[EffectUnit4\]
38. Up: previous **item** and scroll, Down: next **item** and scroll,
    Left: load to left, Right: load to right, **Push: next pane \[choose
    item\]**
39. Channel select

[Vestax
VCI-100MKII.midi.xml](https://raw.githubusercontent.com/sohet/mixxx/master/res/controllers/Vestax%20VCI-100MKII.midi.xml)
[Vestax-VCI-100MKII-scripts.js](https://raw.githubusercontent.com/sohet/mixxx/master/res/controllers/Vestax-VCI-100MKII-scripts.js)
(2017-6-1, not compatible with 2.0)\[6\]

1.  see [the
    article](http://www.mixxx.org/forums/viewtopic.php?f=7&t=6038&start=20#p25804)
    or use [Controller
    Wizard](http://www.mixxx.org/manual/2.0/chapters/advanced_topics.html)
    (choose "Quick Effect Super Knob") for low-high pass

2.  no LED: default length = 4, LED29: default length \> 4, LED28: 1/4 ≤
    default length \< 4, LED28 & LED29: default length \< 1/4

3.  left-right inverse -\> right inverse -\> left inverse -\> full
    inverse -\> none -\> full -\> left -\> right -\> left-right

4.  see [the
    article](http://www.mixxx.org/forums/viewtopic.php?f=7&t=6038&start=20#p25804)
    or use [Controller
    Wizard](http://www.mixxx.org/manual/2.0/chapters/advanced_topics.html)
    (choose "Quick Effect Super Knob") for low-high pass

5.  no LED: default length = 4, LED29: default length \> 4, LED28: 1/4 ≤
    default length \< 4, LED28 & LED29: default length \< 1/4

6.  see [Controller Mapping File
    Locations](controller_mapping_file_locations) for use
