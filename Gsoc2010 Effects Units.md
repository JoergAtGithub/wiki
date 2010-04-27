# Effects Units based on existing LADSPA integration (GSoC 2010 project)

  - Student: **Bruno Buccolo**
  - Mentor: **Russell Ryan**

### Abstract

Sometimes playing the right tracks at the right time in a perfect mix is
not enough. Users like to use effects/filters in their mix to squeeze
every bit of energy of a track, make creative mixes using filters, delay
beats to get funky, use reverb on vocals to fill the room and so on.
Mixxx can already host LADSPA plugins, however it lacks a user interface
for proper configuration since there must be a mapping between Mixxx
controls and LADSPA plugins.

I'm proposing not only designing a user interface for configuration of
LADSPA plugins, but also taking the effects on Mixxx to a whole new
level. I'll create Effects Units, that will have standard controls, so
we only have to map MIDI once, and then plug-in the desired effect in
the effect unit to use them. The user will also have the flexibility to
choose how he's going to use these 2 effects units, being able to use
both on a channel, a unit per channel or even both on master.
