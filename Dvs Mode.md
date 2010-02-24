# Digital Vinyl System replacement mode

The goal of this mode would allow people to easily use Mixxx with
external mixers and vinyl control, disabling unneeded internal
processing for better responsiveness.

Add a "DVS mode" checkbox to the Options menu that makes the following
changes:

  - Enables vinyl control, obviously
  - Routes deck outputs to separate selectable sound card outputs (in
    prefs-\>DVS mode) and disables internal mixing
  - Disables gain, EQ, channel faders, cross fader, play, cue, pitch,
    master output MixxxControls and all associated processing
  - Grays out/hides applicable GUI controls (or just suggests changing
    the skin)
  - Leaves LADSPA enabled on a per-deck basis
  - Should still allow the user to load a song in a deck and play it
    without using the timecodes, just in case of any problems with
    timecode decks, however in this case verry small gui controls would
    be sufficient.
  - the gui should show relevant information about how the timecode is
    controling the decks, e.g. connected, disconected,
  - integration with single deck vinyl control [Single-Deck Vinyl
    Control](single-deck_vinyl_control) 
  - any skins made for dvs mode should also support single deck vinyl
    control.
