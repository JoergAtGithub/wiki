# Compiling on Linux

Compiling software is the process of turning human-readable source code
into machine code a computer can execute. Compiling Mixxx is fairly
straightforward on Linux. The steps below outline what to do.

## Install build dependencies

Mixxx relies on several external libraries for various features.

### SCons 2.x

The Mixxx build scripts still rely on SCons 2 and don't work with SCons
3 and Python 3. If your distribution (Fedora 27, ...) already comes with
SCons 3 the build will fail when following the instructions.

As a workaround you can simply install SCons 2 side by side::

1.  Download a standalone version of SCons 2.5.1 from
    [here](https://sourceforge.net/projects/scons/files/scons/2.5.1/scons-2.5.1.tar.gz/download)
2.  Extract the archive into any directory, e.g. /opt or somewhere into
    your home directory
3.  Execute *python2 \<your-installation-dir\>/scons-2.5.1/script/scons*
    instead of *scons*

### Debian / Ubuntu

If your distribution is Debian based (such as Ubuntu), you can install
them by running:

``` bash
sudo apt-get build-dep mixxx 
sudo apt-get install g++ git scons libqt4-dev libqt4-sql-sqlite libportmidi-dev \
  libopusfile-dev libshout-dev libtag1-dev libprotobuf-dev protobuf-compiler \
  libusb-1.0-0-dev libfftw3-dev libmad0-dev \
  portaudio19-dev libchromaprint-dev librubberband-dev libsqlite3-dev \
  libid3tag0-dev libflac-dev libsndfile-dev libupower-glib-dev
sudo apt-get install libjack-dev libjack0 portaudio19-dev # because of Bug #1464120
sudo apt-get install libfaad-dev libmp4v2-dev # required for M4A support
```

NOTE: Updated these for Mixxx 2.0 and Ubuntu 15.10, if this does not
work on recent versions of Debian please split this section up.

TODO: Please consider putting these instructions into version control so
they can be kept in sync with a particular version or branch.

### Fedora

On Fedora, [enable the RPMFusion package
repository](http://rpmfusion.org/Configuration). You only need to enable
the free repository; the nonfree repository is not necessary for Mixxx.
Then run:

    su
    [Enter the password for the user "root" at the prompt]
    dnf groupinstall "Development Tools"
    dnf install gcc-c++ upower-devel
    dnf builddep mixxx

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
  - QT 4.6.0+ (if installing from packages, make sure to get
    libqt4-opengl and libqt4-svg too.)
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

## Get Mixxx

If you are still running as root from installing packages, return to
using your normal unprivileged user account (press Ctrl + D or run
`exit`).

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release from our [downloads
page](http://www.mixxx.org/download.php), or checkout a snapshot from
our git repository: (See [Using Git](Using%20Git) for more details &
options.)

  - For the latest beta branch: `git clone -b 2.1
    https://github.com/mixxxdj/mixxx.git`
  - For the latest development (master) branch: `git clone
    https://github.com/mixxxdj/mixxx.git`
  - For the latest stable branch: `git clone -b 1.12
    https://github.com/mixxxdj/mixxx.git` (the git branch for 2.0 is
    still called 1.12)

To update to the latest version of a git branch, enter (`cd` into) the
directory you cloned the git repository into and run `git pull`. See
[Using Git](Using%20Git) for more details.

## Compile and install

Once you have the source code, change to the newly created "mixxx"
directory (run `cd mixxx`). Mixxx uses the [SCons](http://scons.org/)
build system rather than the more common GNU autotools and GNU make.
Running `scons -h` in the "mixxx" directory shows a complete list of
build flags if you'd like to customize. To compile without any special
options, as a regular user, run:

    scons prefix=INSTALLATION_DIRECTORY -j NUMBER_OF_CPU_CORES optimize=native

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

    sudo scons prefix=INSTALLATION_DIRECTORY install

to install it. If you set the prefix to a directory your user does have
write access to, then you do not need `sudo` before `scons`. The prefix
option must be the same as before or scons will recompile Mixxx before
installing it.

If you want to be able to run Mixxx on different types of CPUs, change
`optimize=native` to `optimize=portable`.

To compile on a Raspberry Pi, use the arguments: `optimize=native
opengles=1 machine=armhf` with scons.

### Optional: Build with m4a/AAC file support

If you want to play m4a files, add `faad=1` to your scons commands
above. This requires the libraries faad2 and libmp4v2 (or libmp4) to be
installed.

### Optional: Build with Qt5

To build with Qt5 instead of Qt4, use the scons option `qt5=1`. This is
currently experimental. It may help with scaling the GUI on high
resolution screens.

### Optional: Compile with Clang

[Clang](http://clang.llvm.org) is a C/C++ compiler based on
[LLVM](http://llvm.org). Using Clang has various benefits:

  - [Better error messages.](http://clang.llvm.org/diagnostics.html)
  - Colorized compilation output.
  - Better tools for analyzing problems in your program ([Address
    Sanitizer](http://clang.llvm.org/docs/AddressSanitizer.html),
    [Thread Sanitizer](http://clang.llvm.org/docs/ThreadSanitizer.html),
    [MemorySanitizer](http://clang.llvm.org/docs/MemorySanitizer.html),
    etc.)

On Debian, Clang is provided as a package with a version number
attached. Using 3.6 as an example, install it like this:

    sudo apt-get install clang-3.6

To compile Mixxx using Clang 3.6, before running `scons`:

    export CC=clang-3.6
    export CXX=clang++-3.6

You can now use clang-specific SCons options.

  - To enable colorized output, use the `color=1` scons flag.
  - To enable Address Sanitizer, use the `asan=1` scons flag.

### Troubleshooting scons

If scons can't find installed dependencies, try

    scons --config=force

## Uninstall

To uninstall a copy of Mixxx that you compiled, `cd` into the directory
where you ran `scons` before, then run:

    scons -c prefix=INSTALLATION_DIRECTORY install

INSTALLATION\_DIRECTORY must be the same as that used when compiling and
installing. If you needed to use `sudo` to install, also use `sudo` to
uninstall.

## Clean up

If `scons` fails with mysterious errors about not finding dependencies
that you know are installed, it may be using outdated cached information
to look for the dependencies. This can happen after upgrading your
GNU/Linux distribution. To resolve this, try running `scons -c` and
recompiling Mixxx.

## Run without installing

If you want to just run this copy without installing, from the same
directory, run: (WARNING this uses and may overwrite user-wide configs)

    ./mixxx --resourcePath res/

To also run from a different settings folder use:

    ./mixxx --resourcePath res/ --settingsPath /*the folder you like*/
