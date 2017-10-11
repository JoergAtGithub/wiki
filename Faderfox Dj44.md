# Faderfox DJ44

[[/media/hardware/faderfox_dj44_01-2.jpg|]]
[[/media/hardware/faderfox_dj44_02-2.jpg|]]
[[/media/hardware/faderfox_dj44_03-2.jpg|]]

  - [Manufacturer's product page](http://www.faderfox.de/dj44.html)
  - [Forum
    thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=9366&p=33897#p33897)
  - [Manufacturer's user
    guide](http://www.faderfox.de/PDF/Manual%20DJ44%20V01.pdf)
  - [Description for hardware-implemented options in system
    mode](http://www.faderfox.de/PDF/short%20description%20DJ44%20system%20V0100.PDF)
  - [Standard mapping for Traktor ((link will vanish, when graphical
    mapping chart is available
    here](http://www.faderfox.de/PDF/short%20description%20DJ44%20Traktor%20Pro%202%20V01.pdf)

## Description

Fully midi compliant controller, industrial style, built by hand in
Hamburg, Germany by Mathias Fuchß. Compact style for mobile DJ-ing, the
controller comes in its own carrying case. No jog wheels, scratching
(kind of) and strip search can be done via encoders. The crossfader also
is not initially built for scratching, as it runs pretty tight and
slower (but precise). Default values for Deck, FX slots and global
controls can be changed, so one can use two DJ44 devices side by side
for 4 decks.

## Mapping

Every control is sending a midi note, so the basic mapping is easy.
Javascript is needed for Loop section, scratching via encoders and
perhaps for some LED.

### Progress

v0.5: Basic mapping for Mixxx 2.0. is done via xml for essential
functions and LED. Looping display does not work so far, changing loop
size works via Shift+Button at the moment (encoder unused) and effects
sections need more attention. Quick Filter button and LED is unused at
the moment. Javascript mapping is needed for more comfort.
