# M-Audio Torq Xponent

![http://ecx.images-amazon.com/images/I/41Fm-FrL5gL.jpg](http://ecx.images-amazon.com/images/I/41Fm-FrL5gL.jpg)

This device has been discontinued. M-Audio discontinued its DJ products
after the company was bought by inMusic in 2012.

## Getting the leds to work with Mixxx

How to start up Xponent in Listening Mode for LED support:

1.  Hold down the keys "2" (cues, not loops) and "key-lock" on the left
    deck of the xPponent
2.  Switch on the Xponent (while holding both keys)
3.  Wait until the Xponent is completely started up (red progress LEDS
    on both decks are fully lit) then release the keys
4.  Now LEDs work\!

Xponent setup for LEDs
<http://www.native-instruments.com/forum/showthread.php?t=71882>

You can verify that the Xponent is in "listening" mode by observing the
button behavior. If the buttons no longer pulse brightly and fade down
when you press them, then the Xponent is in the correct mode for use
with Mixxx.

**Note for Windows users:** It seems that the current version of the
Windows Xponent ASIO driver interferes with the ability to send MIDI
control messages to the Xponent. As a result, if you are running the
M-Audio Xponent drivers, the lights will not work. If you uninstall the
drivers, the lights will work, but you can no longer use the Xponent's
audio in ASIO mode. The Xponent will still show up using "Windows
WDM-KS" as the Sound API. It will appear as "Analog Connector 1 (Xponent
Audio)" and "Analog Connector 2 (Xponent Audio)". Connector 2 is the
main out, and Connector 1 is the headphones. The latency meter seems to
run a bit higher than it did under ASIO though, so keep this in mind,
and test both setups with your own system to see how they compare. If
you require low latency as well as a lot of effects or time stretching,
you may want to run with the ASIO driver at the expense of the lights.

## Button behaviour in Mixxx

[[/media/hardware/xponent-mapping-3.png|]]

  - **10:** Unordered List Item
  - **11:** Unordered List Item
