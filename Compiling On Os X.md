# Compiling on macOS

Compiling Mixxx for macOS is simple once you have all the dependencies
installed. This guide assumes you have basic knowledge about using the
command line.

*Note: Mixxx is fading out SCons in favor of [cmake](https://cmake.org)
starting in 2.3 and will completely switch in 2.4. This page isn't
updated with the appropriate instructions yet.*

## 1\. Install Xcode Command Line Tools

Launch the Terminal application, and type the following command string:

``` 
  xcode-select --install
```

Click *Install* on the software update popup window that will appear,
and wait for the download and installation to finish (about 150 MB). It
gets placed in the following directory:
`/Library/Developer/CommandLineTools/`

<span class="underline">Note</span>: If Xcode is already installed in
your system, then Command Line Tools are installed as well (you can
check this by trying to run `clang` or `make` from the terminal). To
install the latest available version of Xcode for your macOS release, go
to <https://developer.apple.com/download/>. Downloading it requires a
free registration at Apple's developer site.

## 2\. Install build dependencies

### Method 1: Homebrew

**There is currently a major performance problem with Qt 5.14 and Mixxx
on macOS. We recommend [using our prebuilt
dependencies](#method-2use-a-pre-built-environment) until this is
[fixed](https://github.com/mixxxdj/mixxx/pull/1974).**

[Homebrew](https://github.com/Homebrew/brew) is yet another package
manager for macOS. It is growing quickly in popularity. Assuming you
have already installed Homebrew and gotten it working:

  - Open the
    [Terminal](http://www.apple.com/macosx/apps/all.html#terminal)
    application and use the following command to install the necessary
    libraries:

<!-- end list -->

    brew install scons pkg-config portaudio libsndfile libogg libvorbis portmidi git taglib libshout protobuf flac libjpeg qt5 chromaprint rubberband fftw vamp-plugin-sdk opusfile lilv lame

Next you need to set your environment variables so that the compiler can
find Homebrew-installed dependencies. In the below code you should
customize `HOMEBREW_PATH` to the path where your Homebrew folder can be
found. Copy and paste the code below into \~/.bash\_profile:

``` 
HOMEBREW_PATH=/usr/local
# See the note below about the Opus workaround.
export CFLAGS="-I$HOMEBREW_PATH/include -I$HOMEBREW_PATH/include/opus"
export CXXFLAGS="-I$HOMEBREW_PATH/include -I$HOMEBREW_PATH/include/opus"
export LDFLAGS=-L$HOMEBREW_PATH/lib
export QTDIR=$HOMEBREW_PATH/Cellar/qt/`brew list --versions qt | ruby -ne 'print $_.split.last'`/

```

then run `source ~/.bash_profile`.

**Opus Workaround:** The version of libopus included with Homebrew has a
bug where opusfile.h includes the file opus\_multistream.h. In order for
this file to be present on the include path, we need to add
$HOMEBREW\_PATH/include/opus to the include path. This will hopefully be
fixed in future versions of libopusfile.

#### Legacy: Qt 4

**Qt 4 is only supported in Mixxx 2.1 and earlier. Newer versions of
Mixxx do not build with it.**

If you will be compiling with Qt4, also run:

    brew tap cartr/qt4
    brew tap-pin cartr/qt4
    brew install qt@4

Set the `$QTDIR` environment variable (e.g. in your `.bash_profile`, as
described above) to point to Qt 4:

    export QTDIR=$HOMEBREW_PATH/Cellar/qt@4/%VERSION%/

Replace %VERSION% with the folder name, e.g. 4.8.7\_5 . Run `brew list
--versions qt@4` to see what version(s) you have installed.

#### Optional: ModPlug support

To enable [libmodplug](http://modplug-xmms.sourceforge.net/) based
module tracker support.

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

#### Optional: Alternative MP3/AAC support

Mixxx supports using macOS-provided versions of the MP3 and AAC codec,
so you do not need this step for MP3/AAC support. If you don't want to
use the macOS versions of these codecs you can build the codecs into
Mixxx directly. To do this, you have to install the MP3 and AAC codecs
using Homebrew:

``` 
    brew install libid3tag libmad mp4v2 faad2
```

### Method 2: Use a pre-built environment

**These instructions only work for Mixxx 2.3 and later.**

The Mixxx build server produces pre-built macOS build environments.

See
[downloads.mixxxx.org](http://downloads.mixxx.org/builds/buildserver/)
and select the series of Mixxx you would like to develop for (e.g.
`2.3.x-macosx`). Download the latest build environment you see, or check
[build/osx/golden\_environment](https://github.com/mixxxdj/mixxx/blob/master/build/osx/golden_environment)
to see the current official version.

After you extract your build environment, you need to tell Mixxx where
to find it:

``` 
export OSXLIB=/path/to/build/environment; 
# Make sure to edit this to match what is actually present in $OSXLIB.
export QTDIR=${OSXLIB}/Qt-5.11.2; 
export PATH=${OSXLIB}/bin:${QTDIR}/bin:$PATH; 
export CXXFLAGS="-isystem ${OSXLIB}/include"; 
export CFLAGS="-isystem ${OSXLIB}/include"
export LDFLAGS="-L${OSXLIB}/lib -F${OSXLIB}/lib -Wl,-rpath,${OSXLIB}/lib"; 
```

You may need to adjust `$QTDIR` in the above example, depending on what
is actually present in the environment.

### Method 3: Manual

You can of course install all of [Mixxx's dependencies](dependencies) by
hand. We don't recommend it.

## 3\. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release from our [downloads
page](https://www.mixxx.org/download), or checkout a snapshot from our
git repository:

  - For the latest development (master) branch: `git clone
    https://github.com/mixxxdj/mixxx.git`
  - For the latest beta branch: `git clone -b 2.2
    https://github.com/mixxxdj/mixxx.git`
  - For the latest stable branch: `git clone -b 2.1
    https://github.com/mixxxdj/mixxx.git`

To update to the latest version of a git branch, enter (`cd` into) the
directory you cloned the git repository into and run `git pull`. Refer
to [Using Git](Using%20Git) for more details.

## 4\. Compile and install

Change to the newly created `mixxx` directory, and use scons to compile
Mixxx:

    cd mixxx
    scons verbose=0

If you get an error about hss1394, set `hss1394=0`.

If you are compiling with Qt 4, set `qt5=0`. Qt 4 is only supported in
Mixxx 2.1 and earlier.

If the build succeeds, there will be a `mixxx` binary in the current
directory that you can run:

    ./mixxx --resourcePath res/

This runs Mixxx, telling it to use the `res` folder as its source of
skins, controller presets, etc. This is usually desirable for local
development.

Alternatively, you can build a macOS `.app` bundle by running:

    scons bundle

This will generate a `Mixxx.app` bundle in the `osx64_build` folder,
which you can run by double-clicking on or typing `open
osx64_build/Mixxx.app`. Generating the .app has some expensive scanning
and relinking steps so for iterative development, we suggest using the
bare binary instead of creating a bundle.

### Optional: Use Clang to build

On macOS, GCC is a wrapper around [Clang](http://clang.llvm.org) -- a
compiler based on [LLVM](http://llvm.org). Using Clang has various
benefits:

  - [Better error messages.](http://clang.llvm.org/diagnostics.html)
  - Colorized compilation output.
  - Better tools for analyzing problems in your program ([Address
    Sanitizer](http://clang.llvm.org/docs/AddressSanitizer.html),
    [Thread Sanitizer](http://clang.llvm.org/docs/ThreadSanitizer.html),
    [MemorySanitizer](http://clang.llvm.org/docs/MemorySanitizer.html),
    etc.)

The GCC wrapper around Clang on macOS tries to behave like GCC which
loses some of these benefits. To use Clang directly, before running
`scons`:

    export CC=clang
    export CXX=clang++

You can now use clang-specific SCons options.

  - To enable colorized output, use the `color=1` scons flag.
  - To enable Address Sanitizer, use the `asan=1` scons flag.

### Optional: Alternative MP3/AAC support

As of Mixxx 2.0, Mixxx will use CoreAudio to decode MP3 and AAC files by
default. If you want to use `libmad` or `libfaad` for MP3 and AAC
decoding, simply set the `mad` and `faad` flags and clear the
`coreaudio` flag. For example:

    scons mad=1 faad=1 coreaudio=0

### Optional: ModPlug Support

To enable libmodplug based module tracker support, set the `modplug`
flag. For example:

    scons modplug=1

\==== Common error messages & solutions ====

##### ld: symbol(s) not found for architecture x86\_64

OSX 10.9 Mavericks has changed the stdlib default to libc++. If you are
on OSX 10.9 Mavericks and get this link error, try the "scons" command
above like this:

    scons stdlib=libc++

##### Error: QT path does not exist or QT5 is not installed.

If you installed Qt to a custom location you will have to provide this
via the `qtdir` flag. For example, you could try:

    scons qtdir=/Developer

Because /Developer is a common place for Qt to drop its frameworks.

##### Missing "initializer\_list".

This most likely means you are building Mixxx with libstdc++ and not
libc++. Mixxx versions newer than 2.0 now require C++11 so libstdc++ is
no longer an option since it does not support C++11 features like
initializer\_list.

##### ld: warning: in /opt/local/lib/libGLU.dylib, file was built for unsupported file format which is not the architecture being linked (i386)

Try the "scons" command above like this:

    scons machine=x86_64

##### Unmet dependency: Could not find libtag or its development headers.

Dependency errors happen from time to time , even if the dependencies
are installed. This is not limited to \`\`libtag\`\`. You are not able
to compile the source, and the mixxx build aborts.

First, try updating brew and upgrading the packages

``` 
 brew update && brew upgrade
```

Force SCons to ignore any cached results, delete temporary files and
return the source tree to the original state. From the Mixxx build
directory, run

``` 
 rm -R config.log .sconsign.dblite .sconf_temp .sconsign.branch
```

Build Mixxx

``` 
 scons
```

If build is finished, start the executable

``` 
 ./mixxx --controllerDebug --developer --resourcePath res/
 
```

## 5\. Configure your development tools

Now that you can build Mixxx, learn about [developer
tools](developer_tools) that make Mixxx development easier.
