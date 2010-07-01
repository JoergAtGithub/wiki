# Mixxx Add-ons

This page will contain user-contributed add-ons for Mixxx.

For **extra skins**, check out the [skins subforum on the Mixxx
forums](http://mixxx.org/forums/viewforum.php?f=8).

# Audio Playback Plugins

If you write an audio playback plugin, here's a good place to link to
it.

## Technical Details

#### Install Locations

This where Mixxx will look for plugins on each OS:

Linux:

  - /usr/local/lib/mixxx/plugins/soundsource/
  - /usr/lib/mixxx/plugins/soundsource/
  - \~/.mixxx/plugins/soundsource/

Windows:

  - %ProgramFiles%\\Mixxx\\plugins\\soundsource\\

OSX:

  - /Library/Application Support/Mixxx/Plugins/soundsource/

#### Additional Locations

Tell mixxx to look for plugins in additional locations by calling it
with the `--pluginPath` argument (for instance, if one wants to be able
to play m4a files from a trunk build without installing, call `./mixxx
--pluginPath ./linux_build/plugins/linux_build`, changing linux\_build
to the appropriate directory name as necessary). As many --pluginPath
arguments may be specified as necessary.
