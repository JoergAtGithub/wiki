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

Presets are now in Trunk \<del\> You'll also need some presets. Just
download
[ladspa\_presets.tar.bz2](http://fatcat.ftj.agh.edu.pl/~i7bartki/files/mixxx/ladspa_presets.tar.bz2)
and extract the directory ladspa\_presets to your Mixxx share directory
(as root):

    tar -C /usr/local/share/mixxx/ -xjf ladspa_presets.tar.bz2

\</del\>

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
LADSPA \> Show LADSPA window from the menu.

Currently the following skins are supported: outlineSmall, outline,
outlineClose, traditional, hercules, nCut, Collusion (1280), Collusion
(1280-WS).

## Integration into Trunk TODO

All the LADSPA code is already in trunk, it just needs to be enabled by
default. In order for us to do this "right", here's the stuff that needs
to be done:

  - Integrate LADSPA window into main window (in progress by Albert)
  - Make LADSPA pane use QGridLayout
  - Remove LADSPA menu
  - Pick the default LADSPA plugins:
  - Make sure we have preset XML files for all of these.
  - Build them on Windows, OS X, and Linux
  - Put the precompiled plugins in mixxx-winlib/linlib/maclib
  - Add LADSPA presets and plugins to trunk
  - Modify SConscript to install them on OS X, Linux (and move to dist
    dir on Win32)
  - Modify mixxx.nsi to install/uninstall them on Windows
  - Update src/debian/rules file (might not need editing, but
    doublecheck)

<!-- end list -->

``` 
    * Figure out deployment strategy for Linux:
       * On Windows/OS X, we'll just bundle them
       * ... but on Linux, we may only want to ship the presets files and require users to install their distro's LADSPA plugins package (Anyone have ideas here?)
```
