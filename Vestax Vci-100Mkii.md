# Vestax VCI-100MKII

  - [Product page in
    archive.org](http://web.archive.org/web/20140809134938/http://www.vestax.com/v/products/detail.php?cate_id=118&parent_id=8)
  - [Forum thread](http://www.mixxx.org/forums/viewtopic.php?f=7&t=6038)

## Mapping for Mixxx 2.0 (1.12+)

![http://www.mixxx.org/wiki/lib/exe/fetch.php/vci100mkii.png](http://www.mixxx.org/wiki/lib/exe/fetch.php/vci100mkii.png)

*Functions in square brackets are executed instead if a shift button is
pressed.*

1.  Previous effect \[Select FX1/2\]
2.  Next effect \[Select FX3/4\]
3.  FX parameter1
4.  FX parameter2
5.  FX parameter3
6.  FX mix
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
27. Loop in the default length (4 beats at the beginning) \[Reloop\], or
    *in loop* Exit the loop \[Loop out\]
28. Halve the default length,\[2\] or *in loop* Halve the loop \[Move
    the loop backward by 1/2 beat\]
29. Double the default length, or *in loop* Double the loop \[Move the
    loop forward by 1/2 beat\]
30. Activate \[Clear\] hotcue1
31. Activate \[Clear\] hotcue2
32. Activate \[Clear\] hotcue3
33. Activate \[Clear\] hotcue4
34. Slip mode (affect scratch, loop and hotcue)
35. PFL \[PFL solo\] (if headphone mix is cue or master only then switch
    it)
36. FX1 \[FX3\]
37. FX2 \[FX4\]
38. Up: previous track and scroll, Down: next track and scroll, Left:
    load to left, Right: load to right, Push: load to first stopped
39. Channel select

[Vestax
VCI-100MKII.midi.xml](https://github.com/mixxxdj/mixxx/blob/1.12/res/controllers/Vestax%20VCI-100MKII.midi.xml)
[Vestax-VCI-100MKII-scripts.js](https://github.com/mixxxdj/mixxx/blob/1.12/res/controllers/Vestax-VCI-100MKII-scripts.js)

1.  see [the
    article](http://www.mixxx.org/forums/viewtopic.php?f=7&t=6038&start=20#p25804)
    or use [Controller
    Wizard](http://www.mixxx.org/manual/2.0/chapters/advanced_topics.html)
    (choose "Quick Effect Super Knob") for low-high pass

2.  no LED: default length = 4, LED29: default length \> 4, LED28: 1/4 ≤
    default length \< 4, LED28 + LED29: default length \< 1/4
