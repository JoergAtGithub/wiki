# M-Audio Torq Xponent

![http://ecx.images-amazon.com/images/I/41Fm-FrL5gL.jpg](http://ecx.images-amazon.com/images/I/41Fm-FrL5gL.jpg)

This device has been discontinued. M-Audio discontinued its DJ products
after the company was bought by inMusic in 2012. This device is a class
compliant USB audio and MIDI device, so it does not require a special
driver on any OS that Mixxx runs on.

## Note for Windows users

Typically, the ASIO sound API is the best option on Windows and it
requries an ASIO driver from the sound card manufacturer. However, it
seems that the current version of the Windows Xponent ASIO driver
interferes with the ability to send MIDI control messages to the
Xponent. As a result, if you are running the M-Audio Xponent drivers,
the lights will not work. If you uninstall the drivers, the lights will
work, but you can no longer use the Xponent's sound card with the ASIO
sound API.

It is recommended to **use the WDM-KS sound API** instead. The sound
card will appear as "Analog Connector 1 (Xponent Audio)" and "Analog
Connector 2 (Xponent Audio)". Connector 2 is the main out, and Connector
1 is the headphones. The latency meter seems to run a bit higher than it
did under ASIO, so keep this in mind, and test both setups with your own
system to see how they compare. If you require low latency as well as a
lot of effects or time stretching, you may want to run with the ASIO
driver at the expense of the lights.

## Mixxx version 2.0 or later

A new mapping has been merged with Mixxx and will be included in Mixxx
in the 2.1 release. You can use it now with Mixxx 2.0 by downloading the
following files and putting them in your [controller mapping file
locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder):

  - [JS
    file](https://raw.githubusercontent.com/mixxxdj/mixxx/master/res/controllers/maudio_xponent.mixco.output.js)
  - [XML
    file](https://raw.githubusercontent.com/mixxxdj/mixxx/master/res/controllers/maudio_xponent.mixco.output.midi.xml)

The script was written with the [Mixco mapping
framework](https://sinusoid.es/mixco/). [Documentation for the
mapping](https://sinusoid.es/mixco/script/maudio_xponent.mixco.html) is
available on the Mixco website.

## Getting LEDs to work with old mappings (pre-2.0)

The Mixco mapping included with Mixxx 2.1 and usable with Mixxx 2.0 does
not require these steps.

How to start up Xponent in Listening Mode for LED support:

1.  Hold down the keys "2" (cues, not loops) and "key-lock" on the left
    deck of the Xponent
2.  Switch on the Xponent (while holding both keys)
3.  Wait until the Xponent is completely started up (red progress LEDS
    on both decks are fully lit) then release the keys
4.  Now LEDs work\!

You can verify that the Xponent is in "listening" mode by observing the
button behavior. If the buttons no longer pulse brightly and fade down
when you press them, then the Xponent is in the correct mode for use
with Mixxx.
