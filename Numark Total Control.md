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
    face card, then documenting them for end-users on this page.
  - Jog wheels are too low precision / too touchy. (Mixxx should be
    moving fewer samples per unit of rotation.) (\<sensitivity\> doesn't
    work?)
  - In a possibly related note, scratching is impossible with current
    configuration. Would a lower sensitivity fix this?
  - Mixxx thinks jog wheels are spinning forward fast when spinning
    backward fast. (Mixxx is misinterpreting 0x40 as a positive number,
    when it's actually a negative number.)
  - cue\_set only works every other time the button is pressed. (?\!)
  - Track selection knob needs to be able to send +1 for SelectNextTrack
    and -1 for SelectPrevTrack.
  - Press track selection knob should load track into first stopped
    player.
  - Map flanger buttons for both decks.
  - Add support for LEDs. (No LED codes have been added to the MIDI map
    yet.)
  - Most LEDs are only supposed to light up at (or near) the center of
    the related control. I'm informed that this will require a patch to
    the Mixxx codebase.

*Please* send any comments and/or suggestions to [Alex
Markley](http://malexmedia.net/contact/malex).
