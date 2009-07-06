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
