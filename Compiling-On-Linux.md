Compiling software is the process of turning human-readable source code
into machine code a computer can execute. Compiling Mixxx is fairly
straightforward on Linux. The steps below outline what to do.

## Install build dependencies

Mixxx relies on several external libraries for various features.

### Debian / Ubuntu / Raspbian

If your distribution is Debian 9/10 based (such as Ubuntu 16.04/18.04), you can install
them by running:

```sh
sudo apt-get install g++ git scons libportmidi-dev libopusfile-dev \
  libshout-dev libtag1-dev libprotobuf-dev protobuf-compiler \
  libusb-1.0-0-dev libfftw3-dev libmad0-dev portaudio19-dev \
  libchromaprint-dev librubberband-dev libsqlite3-dev \
  libid3tag0-dev libflac-dev libsndfile-dev libupower-glib-dev \
  libavcodec-dev libavformat-dev \
  libgl-dev liblilv-dev \
  libjack-dev libjack0 portaudio19-dev \
  libfaad-dev libmp4v2-dev \
  libmp3lame-dev libebur128-dev
```

Note: `libfaad-dev libmp4v2-dev` are required for M4A support. The
installation order is [important](https://bugs.launchpad.net/mixxx/+bug/1464120).

Beginning with Debian 11 (Ubuntu 20.04) support for libmp4v2 has been dropped.
Instead install additional FFmpeg packages to build Mixxx with FFmpeg enabled:

```sh
sudo apt-get install g++ git scons libportmidi-dev libopusfile-dev \
  libshout-dev libtag1-dev libprotobuf-dev protobuf-compiler \
  libusb-1.0-0-dev libfftw3-dev libmad0-dev portaudio19-dev \
  libchromaprint-dev librubberband-dev libsqlite3-dev \
  libid3tag0-dev libflac-dev libsndfile-dev libupower-glib-dev \
  libavcodec-dev libavformat-dev libavutil-dev libswresample-dev \
  libgl-dev liblilv-dev \
  libjack-dev libjack0 portaudio19-dev \
  libmp3lame-dev libebur128-dev
```

If you are building the Mixxx **master** or **2.3** git branch, additionally run:

``` sh
sudo apt-get install qt5-default qt5keychain-dev qtdeclarative5-dev libqt5opengl5-dev qtscript5-dev libqt5svg5-dev libqt5x11extras5-dev libvamp-sdk2v5 libhidapi-libusb0 libqt5sql5-sqlite libmodplug-dev
```

If you are building Mixxx **2.2**, additionally run:
``` sh
sudo apt-get install qt5-default qtdeclarative5-dev libqt5opengl5-dev qtscript5-dev libqt5svg5-dev libqt5x11extras5-dev libqt5sql5-sqlite libmodplug-dev
```

If you are building Mixxx **2.1**, additionally run:
``` sh
sudo apt-get install libqt4-dev libqt4-sql-sqlite libqt4-opengl-dev libqt4-svg libqt4-xmlpatterns libqt4-sql
```

### Fedora

On Fedora, [enable the RPMFusion package repository](http://rpmfusion.org/Configuration).
You only need to enable the *free* repository; the *nonfree* repository is not necessary for Mixxx.
Then run:
``` sh
sudo dnf groupinstall "Development Tools"
sudo dnf install gcc-c++ lame-devel
sudo dnf builddep mixxx
```

### Arch & Derivatives

If you are developing in Arch, you should have the
[base-devel group](https://www.archlinux.org/groups/x86_64/base-devel/)
installed.

The tools you are going to need for working with Mixxx are:
``` sh
pacman -S git gcc cmake
```
Alternatively, you can substitute gcc with clang.

Then install the dependencies:
``` sh
sudo pacman -S libid3tag libmad portaudio qt libogg \
    libvorbis libsndfile portmidi libmp4v2 faad2 libshout \
    taglib protobuf vamp-plugin-sdk rubberband \
    chromaprint sqlite upower lilv lame
```

### Non-system Qt

If your distribution's Qt package is older than the version required by
Mixxx, download the latest [Qt source
code](https://download.qt.io/archive/qt/). For each Qt version, it is
available at that link in a directory called "single" and has a filename
like `qt-everywhere-src-VERSION.tar.xz`. Extract that archive and
compile the source code:

    tar xf qt-everywhere-src-VERSION.tar.xz
    cd qt-everywhere-src-VERSION
    ./configure -prefix /path/to/qt/install -system-sqlite -sql-sqlite -qt-zlib -opensource -confirm-license -nomake examples -nomake tests -skip qt3d -skip qtwebengine
    make -j4 # replace 4 with however many threads your CPU can run. This will take a long time.
    make install

### Other

For other distributions, you will need to install the following through
your distribution's package manager. On most distributions, you will
also need the corresponding -dev or -devel packages for each package. If
you cannot find a package listed here that starts with "lib", try
searching for the package name without the "lib" prefix.

  - scons
  - libid3tag
  - libmad
  - [PortAudio-v19](http://www.portaudio.com)
  - Qt 5
  - libogg, libvorbis, libvorbisfile
  - libsndfile
  - [PortMidi & PortTime](http://portmedia.sourceforge.net/portmidi)
  - [libmp4](http://www.mpeg4ip.net/) (or
    [libmp4v2](http://code.google.com/p/mp4v2/)) (optional, for M4A file
    support)
  - [faad2](http://www.audiocoding.com/faad2.html) (optional, for M4A
    file support)
  - libshout 
  - taglib
  - [protobuf](http://code.google.com/p/protobuf/) 
  - [vamp-plugin-sdk](http://www.vamp-plugins.org/develop.html)
    (**optional** if not installed, Mixxx uses an internal version)
  - [librubberband](http://breakfastquay.com/rubberband/)
  - libchromaprint
  - libsqlite3
  - libupower-glib-dev
  - [lilv](http://drobilla.net/software/lilv)
  - [libmodplug](http://modplug-xmms.sourceforge.net/) (optional, for
    MOD file playback support)

## Get Mixxx

If you are still running as root from installing packages, return to
using your normal unprivileged user account (press Ctrl + D or run
`exit`).

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release from the
[downloads page on the website](https://www.mixxx.org/download), 
or checkout a snapshot from our git repository:

  - For the latest development (master) branch: `git clone https://github.com/mixxxdj/mixxx.git`
  - For the latest stable branch: `git clone -b <version> https://github.com/mixxxdj/mixxx.git`

To update to the latest version of a git branch, enter (`cd` into) the
directory you cloned the git repository into and run `git pull`. Refer
to [Using Git](Using%20Git) for more details.

## Compile and install

### CMake

Mixxx uses the CMake build system as of Mixxx 2.3 (currently the master
branch). Building and installing Mixxx follows the standard CMake
procedures.

To build with CMake, first create a new directory and enter it.
This is typically under the project root, but it can be anywhere you want.
```sh
mkdir cmake_build
cd cmake_build
```

Now configure CMake. This only needs to be done once; you don't need to
repeat it when you compile Mixxx again. This step checks if you have all
the dependencies installed, similar to the configure script of GNU
autotools. `/usr` is used as the installation path in this example, but
you can set this to anywhere as long as your `$PATH` environment
variable includes a `bin` directory under the installation path
(`/usr/bin` if the installation path is `/usr`).
```sh
cmake -DCMAKE_INSTALL_PREFIX=/usr .. # Replace .. with the path to the project root if you are outside it
```

##### Compile Mixxx
Set the `--parallel` option to the number of CPU cores
you have. This will take a while, depending on the speed of your
computer.
```sh
cmake --build . --parallel `nproc`
```

Contrary to the behavior of SCons, CMake does not move the produced
binaries into the root folder of the project.

##### Install Mixxx
If you want to compile and install in one step, you can
skip the compilation step above and just run this command.
```sh
cmake --build . --target install --parallel `nproc`
```
#### Debug build

If you want to make a debug build, add `-DCMAKE_BUILD_TYPE=Debug
-DDEBUG_ASSERTIONS_FATAL=ON` to the end of the cmake configure command.
Debug builds should be started with the command line option
`--debugAssertBreak` to trigger a breakpoint in the debugger if debug
assertions are violated or to abort Mixxx immediately. This ensures that
messages about violated debug assertions are not missed between various
other debug log messages. We recommend this if you are working on Mixxx
code, but not if you are performing with Mixxx.

#### ccache

We highly recommend installing [CCache](https://ccache.dev/) if you will
be contributing code to Mixxx. If you won't be writing or testing code
and are just building Mixxx to use it for yourself, you can skip
installing CCache. CCache drastically speeds up the time to recompile
Mixxx, especially when switching between git branches. CMake works with
CCache automatically.

You will probably want to increase the default ccache size of 5.0GB to
something much larger to accommodate Mixxx's large build sizes. You can
adjust the cache size with the --set-config flag:
```sh
ccache --set-config=max_size=20.0G
```

#### Non-System-Qt

Append `-DCMAKE_PREFIX_PATH=/path/to/qt/install` (where
`/path/to/qt/install` is the path you used when [building
Qt](compiling_on_linux#non-system_qt)) to the cmake configure command to
instruct cmake to prefer the Qt version from that path.

### SCons

Mixxx 2.2 and earlier use the SCons build system. Mixxx 2.3 also
supports SCons, but SCons support will be removed in Mixxx 2.4.

Once you have the source code, change to the newly created "mixxx"
directory (run `cd mixxx`). Mixxx uses the [SCons](http://scons.org/)
build system rather than the more common GNU autotools and GNU make.
Running `scons -h` in the "mixxx" directory shows a complete list of
build flags if you'd like to customize. To compile without any special
options, as a regular user, run:
```sh
scons prefix=INSTALLATION_DIRECTORY -j NUMBER_OF_CPU_CORES optimize=native
```
Change INSTALLATION\_DIRECTORY to the location you want to install Mixxx
to. If you want to install Mixxx for all users of the OS, you do not
need to specify a prefix and can leave it as the default, which is
/usr/local. If you only want to install Mixxx for your user, you can
specify a location in your home directory such as \~/local

Running `scons` will take some time, depending on the speed of your
computer. Specifying NUMBER\_OF\_CPU\_CORES will tell scons to run that
many threads at a time while compiling. This speeds up compilation on
multi-core CPUs. You can check how many threads your CPU can run
simultaneously with the `lscpu` command (look for the `CPU(s)` field in
the output). Setting more threads than your CPU can handle will decrease
performance.

Once Mixxx has compiled, if you set the prefix options for scons to a
directory that your normal user does not have write access to, run
```sh
sudo scons prefix=INSTALLATION_DIRECTORY install
```
to install it. If you set the prefix to a directory your user does have
write access to, then you do not need `sudo` before `scons`. The prefix
option must be the same as before or scons will recompile Mixxx before
installing it.

If you want to be able to run Mixxx on different types of CPUs, change
`optimize=native` to `optimize=portable`. If you want to contribute code
to Mixxx and use a debugger, use `optimize=off`.

To compile on a Raspberry Pi (only compatible on Rapsberry Pi 3 and
later), use the arguments: `optimize=native machine=armhf` with scons.

#### Debug build

To catch bugs early during development build and run Mixxx with the
following options.

    build=debug debug_assertions_fatal=1

Debug builds should be started with the command line option
`--debugAssertBreak` to trigger a breakpoint in the debugger if debug
assertions are violated or to abort Mixxx immediately. This ensures that
messages about violated debug assertions are not missed between various
other debug log messages. We recommend this if you are working on Mixxx
code, but not if you are performing with Mixxx.

#### Optional: Build with m4a/AAC file support

If you want to play m4a files, add `faad=1` to your scons commands
above. This requires the libraries faad2 and libmp4v2 (or libmp4) to be
installed.

#### Optional: Compile with Clang

[Clang](http://clang.llvm.org) is a C/C++ compiler based on [LLVM](http://llvm.org).
Using Clang has various benefits:

  - [Better error messages](http://clang.llvm.org/diagnostics.html)
  - Colorized compilation output
  - Better tools for analyzing problems in your program (
    [Address Sanitizer](http://clang.llvm.org/docs/AddressSanitizer.html),
    [Thread Sanitizer](http://clang.llvm.org/docs/ThreadSanitizer.html),
    [MemorySanitizer](http://clang.llvm.org/docs/MemorySanitizer.html),
    etc.)

On Debian, Clang is provided as a package with a version number
attached. Using 6.0 as an example, install it like this:

    sudo apt-get install clang-6.0

To compile Mixxx using Clang 6.0, before running `scons`:

    export CC=clang-6.0
    export CXX=clang++-6.0

You can now use clang-specific SCons options.

  - To enable colorized output, use the `color=1` scons flag.
  - To enable Address Sanitizer, use the `asan=1` scons flag.

#### Troubleshooting scons

If scons can't find installed dependencies, try

    scons --config=force

#### Uninstall

To uninstall a copy of Mixxx that you compiled with SCons, `cd` into the
directory where you ran `scons` before, then run:

    scons -c prefix=INSTALLATION_DIRECTORY install

INSTALLATION\_DIRECTORY must be the same as that used when compiling and
installing. If you needed to use `sudo` to install, also use `sudo` to
uninstall.

#### Clean up

If `scons` fails with mysterious errors about not finding dependencies
that you know are installed, it may be using outdated cached information
to look for the dependencies. This can happen after upgrading your
GNU/Linux distribution. To resolve this, try running `scons -c` and
recompiling Mixxx.

## Run without installing

If you want to run your compiled version without installing,
from the same directory, run:

    ./mixxx --resourcePath res/ --settingsPath <folder>

You can omit the `--settingsPath` argument, but then mixxxx will
use and potentially overwrite your user-wide configs.