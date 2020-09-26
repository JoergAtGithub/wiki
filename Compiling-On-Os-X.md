# Compiling on macOS

Compiling Mixxx for macOS is simple once you have all the dependencies
installed. This guide assumes you have basic knowledge about using the
command line.

1. [Install Xcode Command Line Tools](#1-install-xcode-command-line-tools)<br/>
1. [Install build dependencies](#2-install-build-dependencies)<br/>
    1. [Method 1: Homebrew](#method-1-homebrew)
    1. [Method 2: Use a pre-built environment](#method-2-use-a-pre-built-environment)
    1. [Method 3: Manual](#method-3-manual)
1. [Get Mixxx](#3-get-mixxx)<br/>
1. [Compile and install](#4-compile-and-install)<br/>
    1. [Configure the build for Homebrew dependencies](#configure-the-build-for-homebrew-dependencies)
    1. [Configure the build for pre-built environment](#configure-the-build-for-pre-built-environment)
1. [Configure your development tools](#5-configure-your-development-tools)

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

<a name="installDependencies"/>

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

    brew install scons pkg-config portaudio libsndfile libogg libvorbis portmidi git taglib libshout protobuf flac libjpeg qt5 chromaprint rubberband fftw vamp-plugin-sdk opusfile lilv lame qtkeychain

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

Extract the build environment and take note of its path.

### Method 3: Manual

You can of course install all of [Mixxx's dependencies](dependencies) by
hand. We don't recommend it.

<a name="getMixxx"/>

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

<a name="compile"/>

## 4\. Compile and install

Change to the newly created `mixxx` directory:

    cd mixxx

Create the folder where the build files will be written and navigate into it:

    mkdir cmake_build && cd cmake_build

The next steps you need to follow depend on whether you are using a pre-built environment or you installed dependencies with Homebrew:

### Configure the build for Homebrew dependencies

Run the following cmake command to configure the project with the recommended default settings for development. You don't need to run this command each time you want to build Mixxx, you only need to run this command again whenever you want to change the build settings.

    cmake -DCOREAUDIO=ON -DCMAKE_BUILD_TYPE=Debug -DDEBUG_ASSERTIONS_FATAL=ON -DQt5_DIR=/usr/local/opt/qt5/cmake/Qt5/ -DCMAKE_PREFIX_PATH=/usr/local/opt/ ..

### Configure the build for pre-built environment
You don't need to follow this steps each time you want to build Mixxx, you only need to run again the commands on this section whenever you want to change the build settings.

Before configuring the build, make sure to disable macOS Gatekeeper as described in [this article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave). Otherwise, macOS will prevent the pre-built environment bundled binaries to execute.

Run the following cmake command to configure the project with the recommended default settings for development.

    PREBUILT_ENVIRONMENT=<...> &&\
    cmake -DCOREAUDIO=ON -DCMAKE_BUILD_TYPE=Debug -DDEBUG_ASSERTIONS_FATAL=ON -DQt5_DIR=${PREBUILT_ENVIRONMENT}/Qt-5.14.2/lib/cmake/Qt5 -DCMAKE_PREFIX_PATH=${PREBUILT_ENVIRONMENT} ..

Now you can enable Gatekeeper again as described in [this article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave).

### Build Mixxx
Now you are ready to build Mixxx. To build Mixxx simply run the following command. Note that this has to be run inside the `cmake_build` folder:

    cmake --build .

If the build succeeds, there will be a `mixxx` binary in the current
directory that you can run:

    ./mixxx --developer --resourcePath res/

This runs Mixxx, telling it to use the `res` folder as its source of
skins, controller presets, etc. This is usually desirable for local
development.

**TODO: Update me for cmake**
~~Alternatively, you can build a macOS `.app` bundle by running:~~

    scons bundle

~~This will generate a `Mixxx.app` bundle in the `osx64_build` folder,
which you can run by double-clicking on or typing `open
osx64_build/Mixxx.app`. Generating the .app has some expensive scanning
and relinking steps so for iterative development, we suggest using the
bare binary instead of creating a bundle.~~

<a name="configureTools"/>

## 5\. Configure your development tools

Now that you can build Mixxx, learn about [developer
tools](https://github.com/mixxxdj/mixxx/wiki/Developer-Tools) that make Mixxx development easier.