**WIP**

The Nintendo wii remote (wiimote) undoubtedly the second coolest
invention since the bathtub. The only difference is bathtubs can't be
used to control Mixxx (atleast not yet\!), but the wiimote can be\!

Requirements

  - A **WINDOWS** computer with a bluetooth device
  - Mixxx, pretty obvious
  - Glovepie, THE wiimote interpreter
  - Loopbe1 or midi yoke, both are virtual midi devices to connect
    glovepie to mixxx (more on this later)

How this works is glovepie interprets signals from your wiimote that is
paired with your computer over bluetooth. These signals in glovepie are
converted to midi events that are THEN sent through the virtual midi
device to mixxx\! Mixxx then uses these events to control whatever you
can imagine (such as turning the wiimote to trigger the crossfader based
on the position the wiimote is at). Wow\!

Okay, so thats a pretty straightforward (I hope :S). It does require a
fair amount of configuration and scripting to make it work. Its not as
easy as downloading the above software, installing, and going nuts with
your wiimote to play music. Glovepie must be scripted to capture
specific events, such as hitting the 'B' button or using the built in
accelerometers with movement. Glovepie comes with several script files
that have various examples of different usages that can be examined to
add to your own script.
