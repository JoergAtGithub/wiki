## How to compile Mixxx for Mac OS X

Compiling Mixxx for Mac OS X is pretty straight forward once you have
all the dependancies and Qt set up properly. This guide assumes you have
basic knowledge about compiling (untar/ungzip, ./configure, make). If
you don't, there is a basic guide available at
<http://www.ee.surrey.ac.uk/Teaching/Unix/unix7.html>.

This guide is written for Leopard (10.5.x) but should work on Tiger. You
will need the XCode development tools installed for gcc and all the
other sundry Unix headers. If you don't have XCode already then look on
OS X Install Disc 2 or sign up at [Apple Developer
Connection](http://connect.apple.com) and download them (warning: almost
1G). A guide to getting xcode is available at [this
page](http://www.techsww.com/tutorials/operating_systems/macosx/tools/configuring_macosx_compile_install_software_xcode_tools.php).

### 1\. Install build dependencies (Method 1 - MacPorts)

Mixxx relies on several external libraries for various features.
Fortunately, you can automatically download and install most of these
dependencies through MacPorts.

Start by downloading and installing one of the .dmg disk image for
MacPorts: <http://www.macports.org/install.php>

Then, open the Terminal application and type in the following:

``` 
 sudo port install scons libid3tag libmad portaudio libsndfile libogg libvorbis libmp4v2 portmidi faad2 bzr taglib libshout2
```

Lastly, after that has completed, download and install the [Qt SDK
package](http://qt.nokia.com/downloads/qt-for-open-source-cpp-development-on-mac-os-x)
for your platform.

Optionally, also install HSS1394; see the entry for this under the "1.
Install build dependencies (Method 2 - Compile by hand)" for details
about installation or exclusion.

#### If this is your First Time

FIXME --- Clarify Macports usage, - Work in progress *\[\[|jus\]\]
2011/02/12 15:06*

First, download all of the libraries and utilities in the above list,
starting with scons. During this process, your main command is "sudo
port install XXX", where XXX is the name of each library you'll need. If
the library already happens to be installed on your computer, that's a
time-saver, and you'll get this message:

`~/Music/mixxx>sudo port install libmad`

`Skipping org.macports.activate (libmad ) since this port is already
active`

`---> Cleaning libmad`

Otherwise, it will automatically install it, like this:

`~/Music/mixxx>sudo port install libid3tag`

`Password:`

`---> Fetching libid3tag`

`---> Attempting to fetch libid3tag-0.15.1b.tar.gz from
ftp://ftp.mars.org/pub/mpeg/`

`---> Verifying checksum(s) for libid3tag`

`---> Extracting libid3tag`

`---> Configuring libid3tag`

`---> Building libid3tag with target all`

`---> Staging libid3tag into destroot`

`---> Installing libid3tag 0.15.1b_0`

`---> Activating libid3tag 0.15.1b_0`

`---> Cleaning libid3tag`

Note that the password it asks for is just your local machine, not an
online password. It is necessary because you are going into super-user
mode in order to write the libraries to your hard drive. It's a
basically safe operation, but they put it behind a password so the area
where the libraries are stored doesn't get touched very often.

If you get a message like this:

`Error: Target org.macports.fetch returned: fetch failed`

It probably means that the config file for port hasn't been updated.
Perhaps there has been a newer version of the library released. You may
be hosed at this point, but if you have an older version of the library
already installed on your system, it may still compile and run properly.

### 1\. Install build dependencies (Method 2 - Compile by hand)

You will need to install the following by hand for the compile process:

  - scons ([Download](http://www.scons.org/download.php), [Install
    guide](http://www.scons.org/doc/0.97/HTML/scons-user/x166.html)) --
    if you have Macports and have already installed its version of
    python then "sudo port install scons" is also a reasonable way to
    get this installed.
  - libid3tag
    ([Download](http://sourceforge.net/project/showfiles.php?group_id=12349))
    -- \`./configure && sudo make install\` or "sudo port install
    libid3tag"
  - libmad
    ([Download](http://sourceforge.net/project/showfiles.php?group_id=12349))
    -- \`./configure && sudo make install\` or "sudo port install
    libmad" . If you run into the following error with libmad in 10.6:
    *version.c:1: error: CPU you selected does not support x86-64
    instructions* run the following *export CFLAGS="-arch i686"* then,
    configure, make, sudo make install as normal.
  - Portaudio [Download](http://www.portaudio.com) -- Use the latest
    "v19" trunk snapshot -- \`./configure && sudo make install\` or
    "sudo port install portaudio"
  - libsndfile
    ([Download](http://www.mega-nerd.com/libsndfile/#Download)) --
    \`./configure && sudo make install\` or "sudo port install
    libsndfile"
  - libogg, libvorbis ([Download](http://xiph.org/downloads/)) --
    \`./configure && sudo make install\` or if you have been using port,
    :?: this will have already been covered by previous ports.:?:
  - libmp4v2 ([Download](http://code.google.com/p/mp4v2/downloads/list))
    or "sudo port install mp4v2"
  - portmidi
    ([Download](http://sourceforge.net/apps/trac/portmedia/wiki/portmidi),
    or "sudo port install portmidi"
  - faad2 ([Download](http://sourceforge.net/projects/faac/)) or "sudo
    port install faad2"
  - QT 4.6.0+
    ([Download](http://www.qtsoftware.com/downloads/sdk-mac-os-cpp)) --
    get the .dmg and install to the default location, for snow leopard
    make sure to grab the [64bit cocoa
    version](http://get.qt.nokia.com/qt/source/qt-mac-cocoa-opensource-4.6.1.dmg)
    -- DO NOT use qt4-mac delivered through macports. It will give you
    an error messages that some header files are missing e.g. libmad and
    others. This is due to a missing QTCore framework.
  - Bazaar ([Download](http://bazaar-vcs.org/Download)) -- Get the
    installer for your version of OS X. The installer contains the
    [Bazaar Explorer
    GUI](http://mixxx.org/wiki/doku.php/using_bazaar?s[]=explorer#gui_clients).
    -- or "sudo port install bzr" and "sudo port install bzr-explorer"
    for the GUI
  - HSS1394 -- only applicable to 1.9+ -- "bzr checkout lp:hss1394" then
    "scons" then "sudo scons install" but you probably don't need it
    unless you got a HSS1394 MIDI device like the Stanton SCS 1 series.
    Get around this by including "hss1394=0" when running scons on mixxx
    (see below).
  - taglib --
    ([Download](http://developer.kde.org/~wheeler/taglib.html)) -- or
    "sudo port install taglib"
  - libshout -- ([Download](http://www.icecast.org/download.php)) -- or
    "sudo port install libshout2"

### 2\. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release off our [downloads
page](http://www.mixxx.org/download.php), or checkout the latest Mixxx
code:

    bzr checkout lp:mixxx/1.8 (for current stable v1.7)
    bzr checkout lp:mixxx/1.9 (for current beta v1.9)
    bzr checkout lp:mixxx (for latest trunk)

### 3\. Compile and install

If you got the source code from BZR, change to the newly created "mixxx"
directory, and use scons to compile and install:

    cd mixxx
    scons
    scons bundle

If it you get a message like:

    Error: QT path does not exist or QT4 is not installed.

Then try the "scons" command above like this:

    scons qtdir=/Developer

If it you get a message like:

    d: warning: in /opt/local/lib/libGLU.dylib, file was built for unsupported file format which is not the architecture being linked (i386)

Then try the "scons" command above like this:

    scons machine=x86_64

This should generate Mixxx.app. Generating the .app has some expensive
scanning and relinking steps so if you want to avoid this you can skip
'scons bundle' and instead on the first run of mixxx run it as:

    ./mixxx --resourcePath res/

So that it records res/ in mixxx.cfg as where to find skins etc instead
of dying at startup.

If you wanted to update later to a newer BZR snapshot, you would go back
to the mixxx directory and run:

    bzr update

### 4\. Create an XCode project (optional)

If you want to work on Mixxx with XCode for an IDE:

This is taken from the Scons site, who have a pretty good description of
how to get a scons project up and running in XCode:

``` 
  - File->New Project->Mac OSX ->Others, choose "External Build System" \\ {{:compiling:xcode_scons_step_1.png|}}
  - Save the project into the same directory as your SConstruct file.
  - In Groups and Files -> Targets, double click the target that was automatically created.
  - Fill in the blanks, i.e. the full path to scons - like "/System/Library/Frameworks/Python.framework/Versions/2.3/bin/scons" or "/usr/local/bin/scons" \\ {{:compiling:xcode_scons_step_4.png|}}
  - You should now be able to build using the Build command from Xcode
  - Right click "Executables" and choose "Add new custom executable" and point it to the executable you are building and then you can debug using Xcode.
  - Use Debug -> Breakpoints menu to add a symbolic breakpoint at main() - just type main where it says 'Double click for Symbol' - if you don't add this break point none of the breakpoints set in the editors will work, because gdb doesn't have the symbol information until you start debugging ([[http://www.cocoabuilder.com/archive/message/xcode/2006/8/15/8869|Jim Ingham suggests]] turning off "Lazy Symbol Loading" in Debug Preferences.)
```
