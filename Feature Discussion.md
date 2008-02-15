# Feature Discussion

This page is to discuss possible future features along with some
implementation details. Lengthy discussions will probably get moved to
their own page.

## Reducing Number of Input Libraries

Possibly migrating to a single file decoding solution such as
libavformat.

### Pros

  - Reduces library dependency count
  - Increases playable formats
  - I specifically want m4a/aac playback in our next version - [Adam
    d](/User/Adam%20d)
  - User can recompile library to add new format support to an old
    version of mixxx

### Cons

  - Lots of work to make the change
  - All our eggs are in one basket

### Possible Libraries

  - libavformat/libavcodec (the library used by ffmpeg and mplayer)
  - support lot's of format
  - support utf8

## New Hardware Controller Engine

### Current problems

  - range precision limited by MIDI 7-bit value specification
  - it's impossible to bind different midi controller to a value
  - it's not possible to add a new channel Focus, this channel would
    send event to the channel you have focused (with two button to
    select channel)
  - midi input value could be computed, for example I added a Rot64
    option, that increase the value if midival \> 64 and decrease if
    midival \< 64 (a patch is already done for this)

### Solution

  - new XML file mapping format, allowing us to specify option easier
    (Controller Inverted, Rot64, Value Range)

example xml file:

    <controller>
      <group>ChannelA</group>
      <value>123</value>
      <port>1</port>
      <range begin=0 end=127>
      <acceleration>42</acceleration>
      <sensitivity>42</sensitivity>
      <option>Rot64</option>
      <option>Invert</option>
    </controller>
    * add one class who does the mapping between event (midi,kbd,osc), and the real value.

### Some Desirable Features

  - Should be easy to map a plugged in device through the user interface
  - Should be easy to write more mappings for more devices (i.e.
    sensible xml format)
  - Shouldn't affect stability for people not using midi devices
