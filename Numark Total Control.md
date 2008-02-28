# Numark Total Control

![http://www.numark.com/stuff/contentmgr/files/b9586647d14912401d318473b480ae91/medium/totalcontrol\_angle\_med.jpg](http://www.numark.com/stuff/contentmgr/files/b9586647d14912401d318473b480ae91/medium/totalcontrol_angle_med.jpg)

Link to the website: <http://www.numark.com/totalcontrol>

## Numark Total Control Support

I (Alex Markley) am actively working on putting together a MIDI map for
Mixxx which will add support for the Numark Total Control.
Reverse-engineering of the Numark Total Control should be complete.
Please see [Numark Total Control MIDI
Codes](Numark%20Total%20Control%20MIDI%20Codes) for details.

### WIP MIDI Mapping

The current (very unstable) version of the MIDI map is available [on my
site](http://www.alexmarkley.com/numark_totalcontrol_mixxxmap.xml).
(This is for reference *only*, as it isn't working properly yet.)

### TODO List

Here is a list of things which still need addressed before the Numark
Total Control will work properly with Mixxx. Many (but not all) of these
TODO list items will require a patch against Mixxx or (at least) some
input from the developers.

  - Numark Total Control comes with swappable face cards. One for
    Traktor and one for Cue. My goal is to create one MIDI map for each
    face card, then document them for end-users on this page.
  - cue\_set only works every other time the button is pressed. (?\!)
  - Pitch sliders are currently reversed from their labeled meaning.
  - Map flanger buttons for both decks.
  - Patch mixxx to allow comments in midi map files. (MIDI map files are
    too complex not to have comments.)
  - Add support for LEDs. (No LED codes have been added to the MIDI map
    yet.)
  - Most LEDs are only supposed to light up at (or near) the center of
    the related control. I'm informed that this will require a patch to
    the Mixxx codebase.

*Please* send any comments and/or suggestions to [Alex
Markley](http://malexmedia.net/contact/malex).
