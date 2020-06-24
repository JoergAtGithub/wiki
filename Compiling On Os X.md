# How to compile Mixxx for Mac OS X

Compiling Mixxx for Mac OS X is a simple process once you have all
dependancies and Qt set up properly. This guide assumes you have basic
knowledge about using and compiling with the command line (eg:
./configure, make). If you don’t, there is a basic guide available at
<http://www.ee.surrey.ac.uk/Teaching/Unix/unix7.html>.

This guide is written for Snow Leopard (10.6.x) and Leopard (10.5.x) but
should work up to Mavericks (10.9.x).

## 1\. Install Xcode development tools

You will need the [Xcode development
tools](http://developer.apple.com/technologies/tools/) installed. Xcode
is a package provided by Apple containing compilers, libraries and
additional tools required to develop applications for Mac OS X.

#### Install Xcode on Mac OS X 10.7 Lion or later

Get the latest version of Xcode for free using the [Mac App
Store](http://itunes.apple.com/us/app/xcode/id448457090?mt=12).
Alternatively download Xcode as a disk image from the [Apple developer
website](https://developer.apple.com/downloads/index.action).
Downloading it requires a free registration at Apple's developer site.

After installing Xcode, the Command Line Tools for Xcode must be
installed. Goto *Xcode \> Preferences \> Downloads \> Components \>
Command line tools* and click *Install* or download the latest version
for your OS manually from the [Apple developer
website](https://developer.apple.com/downloads/index.action).

#### Install Xcode on Mac OS X 10.6 Snow Leopard

Xcode 3.2.6 is the last version that can be downloaded for free for
users of Snow Leopard (10.6.x) . Downloading it requires a free
registration at Apple's developer site (but a paid developer program
membership is not required).
[Download](https://developer.apple.com/devcenter/download.action?path=/Developer_Tools/xcode_3.2.6_and_ios_sdk_4.3__final/xcode_3.2.6_and_ios_sdk_4.3.dmg)

Xcode 4.2 for Snow Leopard (10.6.x) requires that you have a [PAID
(99$/year) developer account](http://developer.apple.com/programs/mac/),
it can NOT be downloaded or updated from the Mac App Store (MAS).
[Download](https://developer.apple.com/devcenter/download.action?path=/Developer_Tools/xcode_4.2_with_ios_5_sdk/xcode_4.2_and_ios_5_sdk_for_snow_leopard.dmg)

#### Install Xcode on Mac OS X 10.5 Leopard or earlier

If you have an earlier release of Mac OS X, you may download the latest
version of Xcode for OS X 10.5
([v3.1.4](http://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/getSoftware?bundleID=20491))
or for 10.4
([v2.5](http://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/getSoftware?bundleID=19907)).

Older versions of Xcode can be be installed from your original Mac OS X
Install Disc 2 as well, look at [this
page](http://www.techsww.com/tutorials/operating_systems/macosx/tools/configuring_macosx_compile_install_software_xcode_tools.php)
for a guide. Run Software Update after installation to get the latest
version for your OS.

If you need a specific older version, check the [Apple Developer Tools
download
archive](https://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wo/5.1.17.2.1.3.3.1.0.1.1.0.3.1.3.3.1).
Downloading it requires a free registration at Apple's developer site.

## 2\. Install build dependencies

### Method 1 - Install using Homebrew

**This is the preferred method of compiling Mixxx on OS X**

[Homebrew](http://mxcl.github.com/homebrew/) is yet another package
manager for OS X. It is growing quickly in popularity. Assuming you have
already installed Homebrew and gotten it working:

  - Open the
    [Terminal](http://www.apple.com/macosx/apps/all.html#terminal)
    application and use the following command to install the necessary
    libraries:

<!-- end list -->

``` 
    brew install scons portaudio libsndfile libogg libvorbis portmidi git taglib libshout protobuf flac libjpeg qt chromaprint rubberband vamp-plugin-sdk
```

If you have trouble compiling *rubberband* and *vamp-plugin-sdk*, try
the following Homebrew formulas:

  - <http://tuohela.net/irc/vamp-plugin-sdk.rb>
  - <http://tuohela.net/irc/rubberband.rb>

<!-- end list -->

``` 
    brew install http://tuohela.net/irc/vamp-plugin-sdk.rb http://tuohela.net/irc/rubberband.rb
```

**OPTIONAL:** To enable
[libmodplug](http://modplug-xmms.sourceforge.net/) based module tracker
support.

``` 
    brew install libmodplug
```

If you get the error `No available formula for libmodplug` , enter the
following:

``` 
    brew create http://sourceforge.net/projects/modplug-xmms/files/latest/download     
```

Enter Formula name `libmodplug` if asked for, then enter:

``` 
    brew install libmodplug
```

**OPTIONAL:** Mixxx supports using OSX-provided versions of the MP3 and
AAC codec. If you don't want to use the OSX versions of these codecs you
can build the codecs into Mixxx directly. To do this, you have to
install the MP3 and AAC codecs using Homebrew:

``` 
    brew install libid3tag libmad mp4v2 faad2
```

### Method 2 - MacPorts

Mixxx relies on several external libraries for various features.
Fortunately, you can automatically download and install most of these
dependencies through [MacPorts](http://www.macports.org/). MacPorts is a
package management system that simplifies the installation of software
on Mac OS X.

  - Start by downloading and installing one of the .dmg disk images for
    MacPorts: <http://www.macports.org/install.php>
  - Next, open the
    [Terminal](http://www.apple.com/macosx/apps/all.html#terminal)
    application and use the following command to install the necessary
    libraries:

<!-- end list -->

``` 
    sudo port install scons libid3tag libmad portaudio libsndfile libogg libvorbis mp4v2 portmidi faad2 git taglib libshout2 protobuf-cpp 
```

  - Finally, after that has completed, download and install the [Qt SDK
    package](https://qt-project.org/downloads) for your platform (qt-mac
    and qt-mac-debug-libs required, SDK-Installer will not work with
    standard settings). 

<!-- end list -->

  - Optionally, also install HSS1394 (a high-speed MIDI-over-Firewire
    protocol). See the entry for HSS1394 under the section "[Install
    build dependencies (Method 2 - Compile by
    hand)](compiling_on_os_x#install_build_dependencies_method_2_-_compile_by_hand)"
    for details about installation or exclusion.

#### If This is Your First Time Using MacPorts

After installing MacPorts, using MacPorts to install the required
libraries is a simple process. Using the command `sudo port install X`,
where X is the name of each library you’ll need, MacPorts will
automatically download and install the required dependencies. This can
be done one at time by entering single entries like `sudo port install
scons` for each library listed above or all at once by entering the
entire command given above.

Note that if you attempt to install everything at once and an error
occurs in installation of a library, MacPorts will not continue past the
library that caused the error. For example, if after entering the full
command you receive an error with `git`, you’ll need to sort out the
error and then finish the installation by entering `sudo port install
git taglib libshout2` to properly install `git` and then continue with
installing `taglib` and `libshout2`.

If a library already happens to be installed on your computer, that's a
time-saver, and you'll see something similar to this:

``` 
 ~/Music/mixxx>sudo port install libmad
 Skipping org.macports.activate (libmad ) since this port is already active
 --->  Cleaning libmad
```

Otherwise, MacPorts will automatically install the library and you'll
see something similar to this:

``` 
 ~/Music/mixxx>sudo port install libid3tag
 Password:
 --->  Fetching libid3tag
 --->  Attempting to fetch libid3tag-0.15.1b.tar.gz from ftp://ftp.mars.org/pub/mpeg/
 --->  Verifying checksum(s) for libid3tag
 --->  Extracting libid3tag
 --->  Configuring libid3tag
 --->  Building libid3tag with target all
 --->  Staging libid3tag into destroot
 --->  Installing libid3tag 0.15.1b_0
 --->  Activating libid3tag 0.15.1b_0
 --->  Cleaning libid3tag
```

Note that the password asked for is an admin password for your local
machine. This is because you are going into super-user mode in order to
write the libraries to your hard drive. It's basically a safe operation,
but they put it behind a password so the area where the libraries are
stored doesn't get touched very often.

If you get a message like this:

``` 
 Error: Target org.macports.fetch returned: fetch failed
```

It probably means that the config file for port hasn't been updated.
Perhaps there has been a newer version of the library released. You may
be hosed at this point, but if you have an older version of the library
already installed on your system, it may still compile and run properly.

### Method 3 - Compile by hand

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
  - mp4v2 ([Download](http://code.google.com/p/mp4v2/downloads/list)) or
    "sudo port install mp4v2"
  - portmidi
    ([Download](http://sourceforge.net/apps/trac/portmedia/wiki/portmidi),
    or "sudo port install portmidi"
  - faad2 ([Download](http://sourceforge.net/projects/faac/)) or "sudo
    port install faad2"
  - QT 4.6.0+ ([Download](https://qt-project.org/downloads)) -- get the
    Cocoa Mac binary package for Mac OS X 10.5 - 10.6 (32-bit and
    64-bit) and install to the default location. -- DO NOT use qt4-mac
    delivered through macports. It will give you an error messages that
    some header files are missing e.g. libmad and others. This is due to
    a missing QTCore framework.
  - Git ([Download](http://git-scm.com/)) -- Get the installer for your
    version of OS X. 
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
  - [protobuf](http://code.google.com/p/protobuf/) -- or "sudo port
    install protobuf-cpp"
  - [vamp-plugin-sdk](http://www.vamp-plugins.org/develop.html)
    (**optional** if not installed, Mixxx uses an internal version)

## 3\. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release off our [downloads
page](http://www.mixxx.org/download.php), or checkout the latest Mixxx
code from our git repository:

    git clone -b 1.11 https://github.com/mixxxdj/mixxx.git (for current stable)
    git clone https://github.com/mixxxdj/mixxx.git (for latest trunk)

If you wanted to update later to a newer git snapshot, you would go back
to the mixxx directory and run:

    git pull

## 4\. Compile and install

If you used Homebrew, you need to set your compiler paths accordingly.
In the below code you should customize `HOMEBREW_PATH` to be the path to
your homebrew installation. In this example we will use
`/usr/local/homebrew` (default is `/usr/local`).

    HOMEBREW_PATH=/usr/local/homebrew
    export CFLAGS=-I$HOMEBREW_PATH/include
    export CXXFLAGS=-I$HOMEBREW_PATH/include
    export LDFLAGS=-L$HOMEBREW_PATH/lib
    export QTDIR=$HOMEBREW_PATH/Cellar/qt/4.8.5/

If you got the source code from Git, change to the newly created `mixxx`
directory, and use scons to compile and install:

If you used the 1.11 branch, you must type `cd mixxx` twice.

    cd mixxx
    scons hss1394=0 mad=0 faad=0 coreaudio=1 verbose=0
    scons bundle

As of v1.12, Mixxx will use CoreAudio to decode MP3 and AAC files by
default. If you want to use `libmad` or `libfaad` for MP3 and AAC
decoding, simply set the `mad` and `faad` flags and clear the
`coreaudio` flag. To enable libmodplug based module tracker support, set
the `modplug` flag. For example:

    scons hss1394=0 mad=1 faad=1 coreaudio=0 modplug=1 verbose=0

If it you get a message like:

    Error: QT path does not exist or QT4 is not installed.

If you installed Qt to a custom location you will have to provide this
via the `qtdir` flag. For example, you could try:

    scons qtdir=/Developer

Because /Developer is a common place for Qt to drop its frameworks.

If it you get a message like:

    d: warning: in /opt/local/lib/libGLU.dylib, file was built for unsupported file format which is not the architecture being linked (i386)

Then try the "scons" command above like this:

    scons machine=x86_64

OSX 10.9 Mavericks has changed the stdlib default to libc++. So if you
are on OSX 10.9 Mavericks and get a link error like:

    ld: symbol(s) not found for architecture x86_64

Then try the "scons" command above like this:

    scons stdlib=libc++

This should generate `Mixxx.app` which you can run by double-clicking on
or typing `open Mixxx.app`. Generating the .app has some expensive
scanning and relinking steps so if you want to avoid this you can skip
`scons bundle` and instead on the first run of mixxx run it as:

    ./mixxx --resourcePath res/

So that it records res/ in mixxx.cfg as where to find skins etc instead
of dying at startup.

## 5\. Create an XCode project (optional)

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
    - Note: In Xcode 4 there is no "Add new custom executable" option---you must instead edit the current scheme in order to choose an executable to run.  You can do this by clicking the project name in the upper-left corner of the window and choosing "Edit Scheme..." or by going to Product -> Scheme -> Edit Scheme.  In the edit menu you can also add arguments to be passed to the executable (such as a resource path) when it is launched.
  - Use Debug -> Breakpoints menu to add a symbolic breakpoint at main() - just type main where it says 'Double click for Symbol' - if you don't add this break point none of the breakpoints set in the editors will work, because gdb doesn't have the symbol information until you start debugging ([[http://www.cocoabuilder.com/archive/message/xcode/2006/8/15/8869|Jim Ingham suggests]] turning off "Lazy Symbol Loading" in Debug Preferences.)
```
