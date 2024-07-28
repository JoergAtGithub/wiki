Compiling software is the process of turning human-readable source code into machine code a computer can execute. Compiling Mixxx is fairly
straightforward on Linux. The steps below outline what to do. If you need help after reading this page, feel free to ask questions on our [Zulip chat](https://mixxx.zulipchat.com/#narrow/stream/247620-development-help).

# Download Mixxx source code

If you want to compile Mixxx, you'll need to download the source code. Source archives for releases are on [downloads.mixxx.org](https://downloads.mixxx.org/), but if you want to contribute to Mixxx, we recommend forking the project. Check out [Set up Git](https://github.com/mixxxdj/mixxx/wiki/Using%20Git#set-up-git) to get started.

# Install build dependencies

## Debian & Derivatives (e.g. Ubuntu, Raspbian)

There is a script in the code repository that will download and install all dependencies:
```sh
tools/debian_buildenv.sh setup
```

## Fedora

### Using the buildenv script (recommended)

For building the `main` branch, the recommended approach is to use the script, which will add the RPM Fusion repository and automatically install all dependencies:
```sh
tools/rpm_buildenv.sh setup
```

### Manually

[Enable the RPM Fusion package repository](http://rpmfusion.org/Configuration).
You only need to enable the *free* repository; the *nonfree* repository is not necessary for Mixxx.

Then run:
``` sh
sudo dnf install gcc-c++ ccache ninja-build
sudo dnf builddep mixxx
```

The following dependencies are needed for building the *main* branch in addition to those
from *2.4* that have been installed by `builddep`:
``` sh
sudo dnf install qt6-qt{5compat,base,base-private,declarative,shadertools,svg}-devel qtkeychain-qt6-devel
```

## Arch & Derivatives

If you are developing on Arch, you should have the
[base-devel group](https://www.archlinux.org/groups/x86_64/base-devel)
installed.

The tools you are going to need for working with Mixxx are:
``` sh
sudo pacman -S --needed git gcc cmake
```
Alternatively, you can substitute gcc with clang.

Then install the dependencies:
``` sh
sudo pacman -S --needed protobuf vamp-plugin-sdk rubberband soundtouch \
    chromaprint libid3tag taglib \
    lame libogg libmad libvorbis libmp4v2 faad2 opusfile wavpack \
    libshout libsndfile portmidi portaudio \
    sqlite upower lilv libopenmpt-modplug \
    qt5-declarative qtkeychain-qt5 qt5-svg
```

> Note: This will soon be integrated with the AUR packages (https://aur.archlinux.org/packages/mixxx-git and https://aur.archlinux.org/packages/mixxx_beta-git)

## Nix & NixOS

### Creating a release

```
nix-build shell.nix --arg releaseMode true --arg defaultLv2Plugins true
```
This will build a fully functional mixxx derivate to run at any time.

### Development Environment

To get a working development environment start a nix-shell like this:

```
nix-shell --arg enableKeyfinder true --arg defaultLv2Plugins true
```
You can then use the commands `configure`, `build`, `run`, `debug` for your workcycle. The result will be placed in the folder cbuild.
ccache is used inside the development shell to speed up your recompile times.

### VSCode support

You can use following task for building mixxx inside the nix development environment and have proper error parsing:

```json
{
    "label": "build",
    "type": "shell",
    "command": "nix-shell --arg enableKeyfinder true --arg defaultLv2Plugins true --command 'build;'",
    "options": {
        "cwd": "${workspaceFolder}"
    },
    "problemMatcher": {
        "base": "$gcc",
        "fileLocation": ["absolute"]
    },
    "group": {
        "kind": "build",
        "isDefault": true
    },
    "runOptions": { "instances": 1}
}
```

## Guix & Guix System

### Create a development environment

To create a development shell for Mixxx 2.4 use:
```bash
rm -rf build && guix shell -D mixxx
```

To create a development shell for main branch or Mixxx >=2.5 use:
```bash
rm -rf build && \
guix shell -D mixxx \
    --container \
    --with-commit=libdjinterop=0.21.0 \
    qtbase qtdeclarative qtkeychain-qt6 qtsvg qtshadertools qt5compat libxkbcommon
```
If you have ccache installed on your system you might come across the following compilation error:
```
The C compiler

    "/usr/lib64/ccache/cc"

  is not able to compile a simple test program.
```
To fix it, make sure to:
1. Use the `--container` option of `guix shell`
2. Remove the build folder before entering the development shell: `rm -rf build`

### Build Mixxx

Once inside the Mixxx shell you can build Mixxx simply by:
```
cmake -B build && cmake --build build
```

Once Mixxx is built, run the Mixxx binary in the <src_folder>/build from outside the development shell.

## Non-system Qt

To build Mixxx with a version of Qt older or newer than your distribution's package manager, download the latest [Qt source
code](https://download.qt.io/archive/qt/). For each Qt version, it is available at that link in a directory called "single" and has a filename like `qt-everywhere-src-VERSION.tar.xz`. Extract that archive and compile the source code:

```shell
tar xf qt-everywhere-src-VERSION.tar.xz
cd qt-everywhere-src-VERSION
./configure -prefix /path/to/qt/install -system-sqlite -sql-sqlite -qt-zlib -opensource -confirm-license -nomake examples -nomake tests -skip qt3d -skip qtwebengine
make -j`nproc`
make install
```

# Configure
_If you're building Mixxx 2.2 or earlier, refer to the [old instructions below](#mixxx--22)._

Mixxx uses the CMake build system. Building and installing Mixxx follows the standard CMake procedures.

Before compiling, you need to configure with CMake. This only needs to be done once; you don't need to repeat it when you compile Mixxx again.

This step checks if you have all the dependencies installed, similar to the configure script of GNU autotools. `/usr/local` is used as the installation path in this example, but you can set this to anywhere as long as your `$PATH` environment variable includes a `bin` directory under the installation path (`/usr/local/bin` if the installation path is `/usr/local`). Don't use the prefix /usr, because it is reserved for packaged version of Mixxx (deb/rpm/...) and will interfere with the update process of your package manager.

These examples assume you have the Mixxx source code at `~/mixxx`. If you have it elsewhere, use that path instead in the following commands.

```shell
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -S ~/mixxx -B ~/mixxx/build
```

# Compile
```shell
cmake --build ~/mixxx/build --parallel `nproc`
```

# Install
```shell
cmake --build ~/mixxx/build --target install --parallel `nproc`
```

If you want to compile and install in one step, you can skip the compilation step above and just run this command.

# Run without installing
The `mixxx` binary will be in the CMake build directory. You can simply run it directly:
```shell
~/mixxx/build/mixxx
```

If you use Wayland you need to add `-platform xcb` when running the mixxx executable for the waveforms to work. Unfortunately this will not be resolved until we switch to Qt6 and rewrite the waveform renderers.

# ccache

We highly recommend installing [CCache](https://ccache.dev/) if you are building Mixxx frequently, whether for development or testing. CCache drastically speeds up the time to recompile Mixxx, especially when switching between git branches. CMake works with CCache automatically.

You will probably want to increase the default ccache size of 5.0GB to something much larger to accommodate Mixxx's large build sizes. You can adjust the cache size with the --set-config flag:
```sh
ccache --set-config=max_size=20.0G
```

# Development tips

## Debug build and assertions

If you want to make a debug build, add `-DCMAKE_BUILD_TYPE=Debug -DDEBUG_ASSERTIONS_FATAL=ON` to the end of the cmake configure command.
Debug builds should be started with the command line option `--debugAssertBreak` to trigger a breakpoint in the debugger if debug
assertions are violated or to abort Mixxx immediately. This ensures that messages about violated debug assertions are not missed between various other debug log messages. We recommend this if you are working on Mixxx code, but not if you are performing with Mixxx.

## Non-System Qt

Append `-DCMAKE_PREFIX_PATH=/path/to/qt/install` (where `/path/to/qt/install` is the path you used when [building Qt](compiling_on_linux#non-system_qt)) to the cmake configure command to instruct cmake to prefer the Qt version from that path.

# Mixxx <= 2.2

Mixxx 2.2 and earlier used the SCons build system.

Once you have the source code, change to the newly created "mixxx" directory (run `cd mixxx`). Running `scons -h` in the "mixxx" directory shows a complete list of build flags if you'd like to customize. To compile without any special options, as a regular user, run:
```shell
scons prefix=INSTALLATION_DIRECTORY -j `nproc` optimize=native
```
Change INSTALLATION_DIRECTORY to the location you want to install Mixxx to. If you want to install Mixxx for all users of the OS, you do not
need to specify a prefix and can leave it as the default, which is /local. If you only want to install Mixxx for your user, you can specify a location in your home directory such as ~/local

Running `scons` will take some time, depending on the speed of your computer. Specifying NUMBER_OF_CPU_CORES will tell scons to run that
many threads at a time while compiling. This speeds up compilation on multi-core CPUs. You can check how many threads your CPU can run
simultaneously with the `lscpu` command (look for the `CPU(s)` field in the output). Setting more threads than your CPU can handle will decrease performance.

Once Mixxx has compiled, if you set the prefix options for scons to a directory that your normal user does not have write access to, run
```shell
sudo scons prefix=INSTALLATION_DIRECTORY install
```
to install it. If you set the prefix to a directory your user does have write access to, then you do not need `sudo` before `scons`. The prefix option must be the same as before or scons will recompile Mixxx before installing it.

If you want to be able to run Mixxx on different types of CPUs, change `optimize=native` to `optimize=portable`. If you want to contribute code to Mixxx and use a debugger, use `optimize=off`.

To compile on a Raspberry Pi (only compatible on Rapsberry Pi 3 and later), use the arguments: `optimize=native machine=armhf` with scons.

### Debug build

To catch bugs early during development build and run Mixxx with the following options.

```
build=debug debug_assertions_fatal=1
```

Debug builds should be started with the command line option `--debugAssertBreak` to trigger a breakpoint in the debugger if debug
assertions are violated or to abort Mixxx immediately. This ensures that messages about violated debug assertions are not missed between various other debug log messages. We recommend this if you are working on Mixxx code, but not if you are performing with Mixxx.

### Optional: Build with m4a/AAC file support

If you want to play m4a files, add `faad=1` to your scons commands above. This requires the libraries faad2 and libmp4v2 (or libmp4) to be
installed.

### Optional: Compile with Clang

[Clang](http://clang.llvm.org) is a C/C++ compiler based on [LLVM](http://llvm.org).
Using Clang has various benefits:

  - [Better error messages](http://clang.llvm.org/diagnostics.html)
  - Colorized compilation output
  - Better tools for analyzing problems in your program (
    [Address Sanitizer](http://clang.llvm.org/docs/AddressSanitizer.html),
    [Thread Sanitizer](http://clang.llvm.org/docs/ThreadSanitizer.html),
    [MemorySanitizer](http://clang.llvm.org/docs/MemorySanitizer.html),
    etc.)

On Debian, Clang is provided as a package with a version number attached. Using 6.0 as an example, install it like this:

    sudo apt-get install clang-6.0

To compile Mixxx using Clang 6.0, before running `scons`:

    export CC=clang-6.0
    export CXX=clang++-6.0

You can now use clang-specific SCons options.

  - To enable colorized output, use the `color=1` scons flag.
  - To enable Address Sanitizer, use the `asan=1` scons flag.

### Troubleshooting scons

If scons can't find installed dependencies, try

    scons --config=force

### Uninstall

To uninstall a copy of Mixxx that you compiled with SCons, `cd` into the directory where you ran `scons` before, then run:

    scons -c prefix=INSTALLATION_DIRECTORY install

INSTALLATION_DIRECTORY must be the same as that used when compiling and installing. If you needed to use `sudo` to install, also use `sudo` to
uninstall.

### Clean up

If `scons` fails with mysterious errors about not finding dependencies that you know are installed, it may be using outdated cached information to look for the dependencies. This can happen after upgrading your GNU/Linux distribution. To resolve this, try running `scons -c` and recompiling Mixxx.

### Run without installing

If you want to run your compiled version without installing, from the same directory, run:

    ./mixxx --resourcePath res/ --settingsPath <folder>

You can omit the `--settingsPath` argument, but then mixxxx will use and potentially overwrite your user-wide configs.