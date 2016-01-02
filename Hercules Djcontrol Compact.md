# Hercules DJControl Compact

[[/media/hercules-djcontrol-compact_angle.jpg|]]

[[/media/hercules-djcontrol-compact_top.jpg|]]

  - [Product on manufacturer
    website](https://www.hercules.com/us/DJ-Music/bdd/p/253/djcontrol-compact/)
  - [forked github repository](https://github.com/mwillerich/mixxx)
  - [Forum entry](http://www.mixxx.org/forums/viewtopic.php?f=7&t=7773).
    This is a good place to contact me and let me know whether you've
    found a bug or have a suggestion for improvement.

## Mapping notes

These notes are currently work-in-progress; I felt I should share my
thoughts about the mapping.

  - The controller mapping supports 2 decks. Any magic to map 4 decks
    onto this seems over the top to me.
  - Sync, cue, play, bass and medium filters and volume control work as
    you would expect for each deck.
  - As does the crossfader
  - The wheels do basic, reasonable scratching. After 1 second timeout
    the decks revert to playing. Shift-wheel could control pitch, but
    it's not mapped yet.
  - The mode button switches the modes of the pads. Example:
    Mode+Deck1/Pad1 = Switch to Loop mode on the Deck1 pads.
  - The shift button currently only unsets hot cues. It could support
    pitch bend through the wheels.
  - The 4 pads per deck can be used to control 
  - hot cues on the relevant deck. Pressing the pad (both while stopped
    or during play) sets the hot cue, shift-pad resets it
  - 1,2,4,8 beat loops on the relevant deck. Pressing the relevant pad
    sets the start position and length. Then pressing another pad
    changes the length while preserving the starting point. Shift-pad
    does nothing.
  - FX (controlling the effect rack) is not supported yet. I will likely
    map, per deck, each pad to one effect, so that each deck's output
    can be selectively mapped through the effects 1 to 4. 
  - Sample (controlling samplers) is not supported yet. I will likely
    control a single sampler with 2 pads, making it 4 in total. This is
    the only pad setup that ignores the decks. Not sure there's a
    connection anyway, though.
