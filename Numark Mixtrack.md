[[/media/numark_mixtrack_angle_large.jpg|]]

Manufacturer link: <http://www.numark.com/mixtrack>

# Controller description

## Technically

The Numark Mixtrack is a fully compliant MIDI controller. It is
interfaced with a computer through a single USB port and it does not
include a sound card.

## Who should buy ?

Anyone who wants an affordable mixing midi controller to start with the
hobby and who already has a sound card with two **independent** outputs
(one for the headphones and one for the main output).

## Who should not buy ?

Anyone who wants a professional grade mixing controller, or a piece of
equipment combining both the mixing gear and the soundcard.

# Numark Mixtrack Support in Mixxx

## What is the state of the support in Mixxx ?

As of Mixxx 1.8.2, the Numark Mixtrack is fully supported. The
controller mapping and backing script is maintained by the community and
is regularly updated to take the remarks and improvements into account.
As an example, the "stutter" functionality was implemented in the 1.0b
mapping, which can be found in the [corresponding forum
thread](http://www.mixxx.org/forums/viewtopic.php?f=7&t=1808&start=30#p10182).

## Current mapping

## Known problems

  - The pitch on the controller have a very short run. Thus, having it
    configured as a +10/-10 (or more) is tricky because you will get a
    very low pitch precision. Configuring it as +8/-8 (Mk2 style) is
    higly recommended
  - The autolooping functions, altough implemented are quite flawed. The
    "loop one bar", which is present since the 1.0b version, is making a
    loop between two bars, which are rarely fitted on real "measures".
    As of mixxx 1.9, there is no possibility to adjust the bars to make
    them fit perfectly to the tempo
  - Pressing play while "cue previewing" should start the track for
    real, CDJ style. This is not implemented yet, and is marked as a
    TODO in Mixxx code, so it is unlikely to get implemented on the
    controller mapping side.
  - Final remark on the hardware design: be very, very careful not to
    press the "Load A" or "Load B" button, instead of the corresponding
    track's "cue" button. They are very near, the error is easy and
    produces the most dire effect in a party: an awful blank \!
