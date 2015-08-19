# Compiling on Linux

Compiling Mixxx is fairly straightforward on Linux. The steps below
outline what to do in order to compile Mixxx.

## Install build dependencies

Mixxx relies on several external libraries for various features.

### Debian / Ubuntu

If your distribution is Debian based (such as Ubuntu), you can install
them by running:

    sudo apt-get build-dep mixxx 
    sudo apt-get install git scons libqt4-dev libqt4-sql-sqlite libportmidi-dev libopus-dev libshout-dev libtag1-dev libprotobuf-dev protobuf-compiler libvamp-hostsdk3 vamp-plugin-sdk libusb-1.0-0-dev libfftw3-dev libmad0-dev portaudio19-dev libchromaprint-dev librubberband-dev libsqlite3-dev
    sudo apt-get install libjack-dev libjack0 portaudio19-dev # because of Bug #1464120
    sudo apt-get install libfaad-dev libmp4v2-dev # required for M4A support

### Fedora

On Fedora, [enable the RPMFusion package
repository](http://rpmfusion.org/Configuration). You only need to enable
the free repository; the nonfree repository is not necessary for Mixxx.
Then run:

    su
    dnf groupinstall "Development Tools"
    dnf install scons git gcc-c++ rubberband-devel
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

## Get Mixxx

If you are still running as root from installing packages, return to
using your normal unprivileged user account (press Ctrl + D or run
`exit`).

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release from our [downloads
page](http://www.mixxx.org/download.php), or checkout a snapshot from
our git repository: (See [Using Git](Using%20Git) for more details &
options.)

  - For the latest stable branch: `git clone -b 1.11
    https://github.com/mixxxdj/mixxx.git`
  - For the beta branch: `git clone -b 1.12
    https://github.com/mixxxdj/mixxx.git`
  - For the latest development (master) branch: `git clone
    https://github.com/mixxxdj/mixxx.git`

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
need to specify a prefix and can leave it as the default /usr/local. If
you only want to install Mixxx for your user, you can specify a location
in your home directory such as \~/local

Running `scons` will take some time, depending on the speed of your
computer. Specifying NUMBER\_OF\_CPU\_CORES will tell scons to run that
many threads at a time while compiling. This speeds up compilation on
multicore CPUs.

Once Mixxx has compiled, if you set the prefix options for scons to a
directory that your normal user does not have write access to, run

    sudo scons prefix=INSTALLATION_DIRECTORY install

to install it. If you set the prefix to a directory your user does have
write access to, then you do not need `sudo` before `scons`. The prefix
option must be the same as before or scons will recompile Mixxx before
installing it.

If you want to be able to run Mixxx on different types of CPUs, change
`optimize=native` to `optimize=portable`

### Build with m4a/AAC file support

If you want to play m4a files, use **`scons faad=1`** flag. This
requires the libraries faad2 and libmp4v2 (or libmp4) are installed.

## Clean up

If `scons` fails with mysterious errors about not finding dependencies
that you know are installed, it may be using outdated cached information
to look for the dependencies. This can happen after upgrading your
distro. To resolve this, try running `scons -c` and recompiling.

## Run without installing

If you want to just run this copy without installing, from the same
directory, run: (WARNING this uses and may overwrite user-wide configs)

    ./mixxx --resourcePath res/

To also run from a different settings folder use:

    ./mixxx --resourcePath res/ --settingsPath /*the folder you like*/
