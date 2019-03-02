# Mixxx Add-ons

This page will contain user-contributed add-ons for Mixxx.

For **extra skins**, check out the [skins subforum on the Mixxx
forums](http://mixxx.org/forums/viewforum.php?f=8).

# Audio Playback Plugins

If you write an audio playback plugin, here's a good place to link to
it. sPOTIFY

## Technical Details

#### Install Locations

Below is where Mixxx will look for plugins on each OS:

Linux:

  - /usr/local/lib/mixxx/plugins/soundsource/
  - /usr/lib/mixxx/plugins/soundsource/
  - \~/.mixxx/plugins/soundsource/

Windows:

  - %ProgramFiles%\\Mixxx\\plugins\\soundsource\\mp4

OSX:

  - /Library/Application Support/Mixxx/Plugins/soundsource/

#### Additional Locations

Tell Mixxx to look for plugins in additional locations by calling it
with the `--pluginPath` argument (for instance, if one wants to be able
to play m4a files from a trunk build without installing, call `./mixxx
--pluginPath ./linux_build/plugins/linux_build`, changing linux\_build
to the appropriate directory name as necessary). As many --pluginPath
arguments may be specified as necessary.

# Auto DJ with Beatmatching and Harmonic Mixing

A script, which extends Auto DJ with BPM- and key-based track selection,
beatmatching, and basic EQ fade mixing, is [available through
forums](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8318&p=34531#p34531).
It works reasonably well, but is technically quirky and unclean;
therefore, Mixxx developers are working on ways to offer similar
functionality cleanly and directly in Mixxx. If you're impatient, the
script might satisfy your needs today.
