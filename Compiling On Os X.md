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
    get this installed
  - libid3tag, libmad ([Download
    page](http://sourceforge.net/project/showfiles.php?group_id=12349))
    -- \`./configure && sudo make install\`
  - [PortAudio-v19](http://www.portaudio.com) -- \`./configure && sudo
    make install\`
  - fftw3 ([Download page](http://www.fftw.org/download.html)) --
    \`./configure && sudo make install\`
  - libsndfile ([Download
    page](http://www.mega-nerd.com/libsndfile/#Download)) --
    \`./configure && sudo make install\`
  - libogg, libvorbis ([Download page](http://xiph.org/downloads/)) --
    \`./configure && sudo make install\`
  - libFLAC ([Overchan Download
    page](http://flac.sourceforge.net/download.html), [Download
    Page](http://sourceforge.net/project/showfiles.php?group_id=13478&package_id=32318)
    (don't try to compile the source directly, you'll need to mess with
    the ld(1) options and just don't, there's enough nuisances in this
    process))
  - QT 4.3.0+ ([Download
    page](http://www.qtsoftware.com/downloads/sdk-mac-os-cpp)) -- get
    the .dmg and install to the default location

### 2\. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release off our [downloads
page](http://www.mixxx.org/download.php), or checkout a snapshot from
SVN:

    svn co https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk/mixxx

### 3\. Compile and install

If you got the source code from SVN, change to the newly created "mixxx"
directory, and use scons to compile and install:

    cd mixxx
    scons
    scons bundle

This should generate Mixxx.app. Generating the .app has some expensive
scanning and relinking steps so if you want to avoid this you can skip
'scons bundle' and instead on the first run of mixxx run it as:

    mixxx --resourcePath res/

So that it records res/ in mixxx.cfg as where to find skins etc instead
of dying at startup.

If you wanted to update later to a newer SVN snapshot, you would go back
to the mixxx directory and run:

    svn update

### 4\. Create an XCode project (optional)

If you want to work on Mixxx with XCode for an IDE:

This is taken from the Scons site, who have a pretty good description of
how to get a scons project up and running in XCode:

``` 
  - File->New Project, choose "External Build System"
  - Save the project into the same directory as your SConstruct file.
  - In Groups and Files -> Targets, double click the target that was automatically created.
  - In the Build Tool field, put the full path to scons - like "/System/Library/Frameworks/Python.framework/Versions/2.3/bin/scons"
  - You should now be able to build using the Build command from Xcode
  - Right click "Executables" and choose "Add new custom executable" and point it to the executable you are building and then you can debug using Xcode.
  - Use Debug -> Breakpoints menu to add a symbolic breakpoint at main() - just type main where it says 'Double click for Symbol' - if you don't add this break point none of the breakpoints set in the editors will work, because gdb doesn't have the symbol information until you start debugging ([[http://www.cocoabuilder.com/archive/message/xcode/2006/8/15/8869|Jim Ingham suggests]] turning off "Lazy Symbol Loading" in Debug Preferences.)
```
