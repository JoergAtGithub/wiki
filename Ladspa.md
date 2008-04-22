# LADSPA support

Note that LADSPA support is experimental currently so this page is
intended mainly for developers.

## Compiling with LADSPA support enabled

Required packages: ladspa-sdk

Compiling Mixxx with LADSPA support:

    scons ladspa=1

## Installing

If you're updating from a previous version of Mixxx, you'll need to
reinstall the skins (as root):

    rm -Rf /usr/local/share/mixxx/skins
    scons install

(the directory can be different, e.g. /usr/share/mixxx)

You'll also need some presets. Just download
[ladspa\_presets.tar.bz2](http://fatcat.ftj.agh.edu.pl/~i7bartki/files/mixxx/ladspa_presets.tar.bz2)
and extract the directory ladspa\_presets to your Mixxx share directory
(as root):

    tar -C /usr/local/share/mixxx/ -xjf ladspa_presets.tar.bz2

## Required plugins

I'm not sure if Debian package names are correct.

| Preset      | Plugin(s) | Library              | Debian package | Gentoo package | Homepage                         |
| ----------- | --------- | -------------------- | -------------- | -------------- | -------------------------------- |
| Compressor  | Compress  | caps.so              | caps           | caps-plugins   | <http://quitte.de/dsp/caps.html> |
| PlateReverb | Plate2x2  | caps.so              | caps           | caps-plugins   | <http://quitte.de/dsp/caps.html> |
| Delay5s     | delay\_5s | cmt.so or delay.so   | cmt            | ladspa-cmt     | <http://www.ladspa.org/cmt>      |
| DJFlanger   | djFlanger | dj\_flanger\_1438.so | swh-plugins    | swh-plugins    | <http://plugin.org.uk>           |
| Karaoke     | karaoke   | karaoke\_1409.so     | swh-plugins    | swh-plugins    | <http://plugin.org.uk>           |

## Using

The LADSPA window is hidden by default. You can enable it by activating
LADSPA -\> Show LADSPA window from the menu.

Currently the following skins are supported: outlineSmall, outline,
outlineClose, traditional, hercules, nCut.
