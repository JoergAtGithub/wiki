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

### 1\. Install build dependencies

Mixxx relies on several external libraries for various features. At the
moment, installing the supporting libraries through fink does not work
properly as the install script expects them in a different place. When
executing make install, you may need to use 'sudo make install' instead.

You will need to install the following before continuing with the
compile process:

  - scons ([Download page](http://www.scons.org/download.php), [Install
    guide](http://www.scons.org/doc/0.97/HTML/scons-user/x166.html)) --
    if you have darwinports and have already installed its version of
    python then \`sudo port install scons\` is also a reasonable way to
    get this installed or port scons or "sudo port install scons"
  - libid3tag, libmad ([Download
    page](http://sourceforge.net/project/showfiles.php?group_id=12349))
    -- \`./configure && sudo make install\` or port libid3tag/libmad or
    "sudo port install libid3tag" , "sudo port install libmad"
  - [PortAudio-v19](http://www.portaudio.com) -- \`./configure && sudo
    make install\` or port portaudio or "sudo port install portaudio"
  - libsndfile ([Download
    page](http://www.mega-nerd.com/libsndfile/#Download)) --
    \`./configure && sudo make install\` or port libsndfile
  - libogg, libvorbis ([Download page](http://xiph.org/downloads/)) --
    \`./configure && sudo make install\` or if you have been using port,
    this will have already been covered by previous ports.
  - libFLAC ([Overchan Download
    page](http://flac.sourceforge.net/download.html), [Download
    Page](http://sourceforge.net/project/showfiles.php?group_id=13478&package_id=32318)
    (don't try to compile the source directly, you'll need to mess with
    the ld(1) options and just don't, there's enough nuisances in this
    process)) -\> still needed or is this covered by libsndfile?  
    \`./configure --disable-asm-optimizations && make && make install\`
    does compile [libflac 1.2.1](http://www.xiph.org/downloads/) from
    source on 10.5 -- *\[\[|jus\]\] 2010/11/28*
  - libmp4v2 ([Download](http://resare.com/libmp4v2)) or port mp4v2
  - portmidi
    ([Download](http://sourceforge.net/apps/trac/portmedia/wiki/portmidi),
    or "sudo port install portmidi"
  - faad2 ([Download](http://sourceforge.net/projects/faac/)) or port
    faad2, e.g. "sudo port install faad2"
  - QT 4.6.0+ ([Download
    page](http://www.qtsoftware.com/downloads/sdk-mac-os-cpp)) -- get
    the .dmg and install to the default location, for snow leopard make
    sure to grab the [64bit cocoa
    version](http://get.qt.nokia.com/qt/source/qt-mac-cocoa-opensource-4.6.1.dmg)
    -- DO NOT use qt4-mac delivered through macports. It will give you
    an error messages that some header files are missing e.g. libmad and
    others. This is due to a missing QTCore framework.
  - Bazaar ([Download page](http://bazaar-vcs.org/Download)) -- Get the
    installer for your version of OS X -- This can now be installed
    through "sudo port install bzr"

#### If this is your First Time

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
