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

  - Make LADSPA pane use QGridLayout (?)
  - Pick the default LADSPA plugins:
  - Make sure we have preset XML files for all of these.
  - Build them on OS X, recommend them on Linux, repack Audacity plugin
    build on Windows or have installer fetch them from Audacity's site.
  - Use pre-built plugins for Win32 ([Audacity win32 LADSPA
    Plugins](http://audacity.sourceforge.net/download/beta_windows#optional))
    and Linux ([cmt](http://packages.ubuntu.com/intrepid/cmt),
    [caps](http://packages.ubuntu.com/intrepid/caps),
    [swh-plugins](http://packages.ubuntu.com/intrepid/swh-plugins)).
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

  - the pane with the slots should have a scrollbar (ie. put it in a
    QScrollArea or whatever it's called). The 3 slots don't currently
    show up right on all OSes, so putting it in a scoll area will fix
    this plus maybe let us make more slots or something later.
  - the little "x" to remove an effect from a slot needs to be
    right-aligned, instead of just pasted where-ever.
  - someone should re-evaluate how the effects are layed out inside each
    slot, because all of that code was done before Qt 4 (and before
    QLayouts existed). We don't have to change it, but I think the "x"
    button is probably just hardcoded to be in some position. Would be
    good to know what work will be need to be done later.
  - Fix the text getting cut off. Some of the QLabels in the slots get
    cut off. Needs to word wrap or something smart.
  - Fix the duplicate wet/dry knobs for some plugins.
  - and/or either remove our non-working wet/dry knob or make it work.
    :)
  - The delay time knob in the delay plugin is hard to use because it's
    not tempo synced. There is a reasonable solution to this, which is
    to add some sort of "tempo synced control" declaration in the LADSPA
    xml format, and gives a conversion ratio from BPM to whatever the
    knob is in (millisec probably). Then our LADSPA code would see this,
    and make the knob increment/decrements dependent on the detected BPM
    of whatever's playing.

At the very least, all the GUI problems and knobs-not-working need to be
resolved before LADSPA is ready.
