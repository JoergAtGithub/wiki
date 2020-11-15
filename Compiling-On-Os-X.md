# Compiling on macOS

Compiling Mixxx for macOS is simple once you have all the dependencies
installed. This guide assumes you have basic knowledge about using the
command line.

1. [Install Xcode Command Line Tools](#1-install-xcode-command-line-tools)
1. [Install build dependencies](#2-install-build-dependencies)
    1. [Method 1: Homebrew](#method-1-homebrew)
    1. [Method 2: Use a pre-built environment](#method-2-use-a-pre-built-environment)
    1. [Method 3: Manual](#method-3-manual)
1. [Get Mixxx](#3-get-mixxx)
1. [Compile and install](#4-compile-and-install)
    1. [Configure the build for Homebrew dependencies](#configure-the-build-for-homebrew-dependencies)
    1. [Configure the build for pre-built environment](#configure-the-build-for-pre-built-environment)
1. [Configure your development tools](#5-configure-your-development-tools)

## 1. Install Xcode Command Line Tools

Launch the Terminal application, and type the following command string:

```shell
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

## 2. Install build dependencies

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

```shell
brew install scons pkg-config portaudio libsndfile libogg libvorbis portmidi git taglib libshout protobuf flac libjpeg qt5 chromaprint rubberband fftw vamp-plugin-sdk opusfile lilv lame qtkeychain
```

#### Optional: ModPlug support

To enable [libmodplug](http://modplug-xmms.sourceforge.net/) based
module tracker support.

```shell
brew install libmodplug
```

If you get the error `No available formula for libmodplug` , enter the
following:

```shell
brew create http://sourceforge.net/projects/modplug-xmms/files/latest/download
```

Enter Formula name `libmodplug` if asked for, then enter:

```shell
brew install libmodplug
```

#### Optional: Alternative MP3/AAC support

Mixxx supports using macOS-provided versions of the MP3 and AAC codec, so you do not need this step for MP3/AAC support. If you don't want to
use the macOS versions of these codecs you can build the codecs into Mixxx directly. To do this, you have to install the MP3 and AAC codecs using Homebrew:

```shell
brew install libid3tag libmad mp4v2 faad2
```

### Method 2: Use a pre-built environment

**These instructions only work for Mixxx 2.3 and later.**

Download the [prebuilt environment here](https://github.com/Be-ing/buildserver/suites/1503889010/artifacts/26328962). The GitHub Action artifact wraps the tar.gz archive within a redundant zip archive.

There is currently an issue with a hardcoded path in the PkgConfig file for taglib in the build environment, so you must fix it before building or your build will fail to link at the end.
```shell
export PREBUILT_ENV_NAME=2.3-7b6dfe7-sdk10.15-macosminimum10.12-x86_64
unzip ~/Downloads/macOS-build-environment.zip -d ~/Downloads
tar xf ~/Downloads/${PREBUILT_ENV_NAME}.tar.gz -C ~
rm -rf ~/Downloads/${PREBUILT_ENV_NAME}.tar.gz
export PREBUILT_ENV_PATH=~/${ENVIRONMENT_PATH} # or wherever you extracted the tar.gz archive to
find "${}" -name "*.pc" -or -path "*/bin/taglib-config" -exec sed -i".orig" -e "s|/Users/runner/work/buildserver/buildserver/environment/${PREBUILT_ENV_NAME}|${PREBUILT_ENV_PATH}|g" {} \;
```

### Method 3: Manual

You can of course install all of [Mixxx's dependencies](dependencies) byhand. We don't recommend it.

<a name="getMixxx"/>

## 3. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code. Either grab the source for the latest release from our [downloads
page](https://www.mixxx.org/download), or checkout a snapshot from our git repository:

  - For the latest development (main) branch: `git clone https://github.com/mixxxdj/mixxx.git`
  - For the latest beta branch: `git clone -b 2.3 https://github.com/mixxxdj/mixxx.git`
  - For the latest stable branch: `git clone -b 2.2 https://github.com/mixxxdj/mixxx.git`

To update to the latest version of a git branch, enter (`cd` into) the
directory you cloned the git repository into and run `git pull`. Refer
to [Using Git](Using%20Git) for more details.

<a name="compile"/>

## 4. Compile and install

Change to the newly created `mixxx` directory:

```shell
cd mixxx
```

Create the folder where the build files will be written and navigate into it:

```shell
mkdir cmake_build && cd cmake_build
```

The next steps you need to follow depend on whether you are using a pre-built environment or you installed dependencies with Homebrew:

### Configure the build for Homebrew dependencies

Run the following cmake command to configure the project with the recommended default settings for development. You don't need to run this command each time you want to build Mixxx, you only need to run this command again whenever you want to change the build settings.

```shell
cmake -DCOREAUDIO=ON -DCMAKE_BUILD_TYPE=Debug -DDEBUG_ASSERTIONS_FATAL=ON -DQt5_DIR=/usr/local/opt/qt5/cmake/Qt5/ -DCMAKE_PREFIX_PATH=/usr/local/opt/ ..
```

### Configure the build for pre-built environment
You don't need to follow this steps each time you want to build Mixxx, you only need to run again the commands on this section whenever you want to change the build settings.

Before configuring the build, make sure to disable macOS Gatekeeper as described in [this article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave). Otherwise, macOS will prevent the pre-built environment bundled binaries from executing.

Run the following cmake command to configure the project with the recommended default settings for development.

```shell
export PREBUILT_ENV_PATH=~/2.3-7b6dfe7-sdk10.15-macosminimum10.12-x86_64 # path where you extracted the build environment archive
export PATH="${PREBUILT_ENV_PATH}:/bin:$PATH" # to add ccache to your $PATH
cmake -DCOREAUDIO=ON -DCMAKE_BUILD_TYPE=Debug -DDEBUG_ASSERTIONS_FATAL=ON -DQt5_DIR=${PREBUILT_ENV_PATH}/Qt-5.12.3/lib/cmake/Qt5 -DCMAKE_PREFIX_PATH=${PREBUILT_ENV_PATH} ..
```

Now you can enable Gatekeeper again as described in this [article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave).

### Build Mixxx
Now you are ready to build Mixxx. To build Mixxx simply run the following command. Note that this has to be run inside the `cmake_build` folder:

```shell
cmake --build .
```

If the build succeeds, there will be a `run-mixxx.sh` script in the current directory that you can run:

```shell
./run-mixxx.sh
```

You can pass arguments to this as if you were running the `mixxx` binary directly. For example:

```shell
./run-mixxx.sh --logLevel debug
```

You can run the `mixxx` binary directly, but you would need to set the `QT_QPA_PLATFORM_PLUGIN_PATH` environment variable to point to the `plugins` directory under the Qt directory in the build environment.

### Building a DMG image with an .app bundle inside
Generating the .app has some expensive scanning and relinking steps. So, for development, we recommend using the bare binary instead of creating a bundle. Generally you would only need to build a bundle locally if you are working on the bundle building process.

Add `-DMACOS_BUNDLE=ON` to the first `cmake` command above when configuring the build.

To sign the `.app` bundle inside the DMG image, add `-DAPPLE_CODESIGN_IDENTITY=<your signing identity>` to the `cmake` command. This must be done at the initial `cmake` configure step, not when running `cpack` later. You can run `security find-identity -p codesigning` to find what identities you have installed on your keychain.

To create the DMG image with the .app bundle inside, run
```shell
cpack -G DragNDrop
```
You can run the bundle by double clicking the DMG image in Finder then dragging and dropping the Mixxx.app file inside to /Applications or wherever you would like.

## 5. Configure your development tools

Now that you can build Mixxx, learn about [developer
tools](https://github.com/mixxxdj/mixxx/wiki/Developer-Tools) that make Mixxx development easier.
