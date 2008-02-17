## Numark Total Control Support

I (Alex Markley) am actively working on putting together a MIDI map for
Mixxx which will add support for the Numark Total Control.
Reverse-engineering of the Numark Total Control should be complete.
Please see [Numark Total Control MIDI
Codes](Numark%20Total%20Control%20MIDI%20Codes) for details.

### WIP MIDI Mapping

The current (very unstable) version of the MIDI map is available [on my
site](http://www.alexmarkley.com/numark_totalcontrol_mixxxmap.xml).
(This is for reference *only*, as it isn't working yet.)

### TODO List

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
