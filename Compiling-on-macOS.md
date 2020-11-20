Compiling Mixxx for macOS is simple once you have all the dependencies installed. This guide assumes you have basic knowledge about using the command line.

# Install Xcode Command Line Tools

Launch the Terminal application, and type the following command string:

```shell
xcode-select --install
```

Click *Install* on the software update popup window that will appear and wait for the download and installation to finish (about 150 MB). It
gets placed in the following directory: `/Library/Developer/CommandLineTools/`

If Xcode is already installed in your system, then Command Line Tools are installed as well (you can check this by trying to run `clang` or `make` from the terminal). To install the latest available version of Xcode for your macOS release, [download it from Apple](https://developer.apple.com/download/). Downloading it requires a free registration at Apple's developer site.

# Download Mixxx source code

If you want to compile Mixxx, you'll need to download the source code. Either grab the source for the latest release from our [downloads
page](https://www.mixxx.org/download), or checkout a snapshot from our git repository:

  - For the latest development (main) branch: `git clone https://github.com/mixxxdj/mixxx.git`
  - For the latest beta branch: `git clone -b 2.3 https://github.com/mixxxdj/mixxx.git`
  - For the latest stable branch: `git clone -b 2.2 https://github.com/mixxxdj/mixxx.git`

To update to the latest version of a git branch, enter (`cd` into) the directory you cloned the git repository into and run `git pull`. Refer to [Using Git](https://github.com/mixxxdj/mixxx/wiki/Using%20Git) for more details.

# Install build dependencies

You have several options how to install the libraries and build tools Mixxx requires.

## Recommended: Pre-built environment

Download the [prebuilt environment here](https://github.com/Be-ing/buildserver/suites/1506041269/artifacts/26401744). You must be logged into GitHub to download it. It is what we use to build the official builds, so we recommend using it for local development for consistency.

The GitHub Action artifact wraps the tar.gz archive within a redundant zip archive. First, extract it:

```shell
export PREBUILT_ENV_NAME=2.3-1db6c06-sdk10.15-macosminimum10.12-x86_64
unzip ~/Downloads/macOS-build-environment.zip -d ~/Downloads
tar xf ~/Downloads/${PREBUILT_ENV_NAME}.tar.gz -C ~
```

Then set some environment variables which will be used when configuring `cmake` below:

```shell
export DEPENDENCIES_PATH=~/${PREBUILT_ENV_NAME} # or wherever you extracted the tar.gz archive to
export QT_DIR="$(find "${DEPENDENCIES_PATH}" -type d -path "*/cmake/Qt5")"
export PATH="${DEPENDENCIES_PATH}/bin:$PATH" # to add cmake and ccache to your $PATH
```

## Homebrew

**There is currently a major performance problem with current versions of Qt in Homebrew and Mixxx on macOS. We recommend [using our prebuilt
dependencies](#Recommended-Pre-built-environment) with Qt 5.12 until this is [fixed](https://github.com/mixxxdj/mixxx/pull/1974).**

[Homebrew](https://github.com/Homebrew/brew) is a package manager for macOS. Assuming you have already installed Homebrew and gotten it working, open the [Terminal](http://www.apple.com/macosx/apps/all.html#terminal) application and use the following command to install the necessary libraries:

```shell
brew install scons cmake ccache pkg-config portaudio libsndfile libogg libvorbis portmidi git taglib libshout protobuf flac libjpeg qt5 chromaprint rubberband fftw vamp-plugin-sdk opusfile lilv lame qtkeychain
```

Then set some environment variables which will be used to configure `cmake` below: 

```shell
export QT_DIR=/usr/local/opt/qt5/cmake/Qt5/
export DEPENDENCIES_PATH=/usr/local/opt/
```

### Optional: ModPlug support

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

### Optional: Alternative MP3/AAC support

Mixxx supports using macOS-provided versions of the MP3 and AAC codec, so you do not need this step for MP3/AAC support. If you don't want to use the macOS versions of these codecs you can build the codecs into Mixxx directly. To do this, you have to install the MP3 and AAC codecs using Homebrew:

```shell
brew install libid3tag libmad mp4v2 faad2
```

## Build dependencies yourself

You can use the [scripts used to make the prebuilt environment](https://github.com/mixxxdj/buildserver) locally if you want to do it yourself. Generally this is a waste of time unless you are working on changing the prebuilt environment.

# Configure CMake

First, create the directory where `cmake` will output the built files. For convenience we suggest making this within the Mixxx source code directory, which is assumed to be `~/mixxx` for this example, however, the build directory can be located anywhere you have write access. If you have the source code somewhere other than `~/mixxx`, substitute that for `~/mixxx` in the following commands.

```shell
mkdir ~/mixxx/cmake_build
```

Before configuring the build, make sure to disable macOS Gatekeeper as described in [this article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave). Otherwise, macOS will prevent the pre-built environment bundled binaries from executing.

Run the following `cmake` command to configure the project with the recommended default settings for development. This assumes you have set the environment variables after installing dependencies as described above. For convenience, you can substitute the values of those variables in the command so that you can easily go back to it in your shell history (Ctrl + R then start typing `cmake -DC`) without having to set the variables again.

```shell
cmake -DCOREAUDIO=ON -DCMAKE_BUILD_TYPE=Debug -DDEBUG_ASSERTIONS_FATAL=ON -DQt5_DIR="$QT_DIR" -DCMAKE_PREFIX_PATH="$DEPENDENCIES_PATH" -S ~/mixxx -B ~/mixxx/cmake_build
```

Now you can enable Gatekeeper again as described in this [article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave).

This step only needs to be done once or repeated when you want to change the cmake configuration. Otherwise you can simply rerun the build step below to compile different code.

# Build Mixxx

```shell
cmake --build ~/mixxx/cmake_build --parallel $(sysctl -n hw.physicalcpu)
```

# Run Mixxx
```shell
~/mixxx/cmake_build/run-mixxx.sh
```

You can pass arguments to this as if you were running the `mixxx` binary directly. For example:

```shell
~/mixxx/cmake_build/run-mixxx.sh --logLevel debug
```

You can run the `mixxx` binary directly, but you would need to set the `QT_QPA_PLATFORM_PLUGIN_PATH` environment variable to point to the `plugins` directory under the Qt directory in the build environment.

# Build Mixxx.app bundle inside a DMG image

Generating the .app has some expensive scanning and relinking steps. So, for development, we recommend skipping this step. Generally you would only need to build a bundle locally if you are working on the bundle building process.

Add `-DMACOS_BUNDLE=ON` to the first `cmake` command above when configuring the build. You must rerun the `cmake` configure command with this option if you have already run it before.

To sign the `.app` bundle inside the DMG image, add `-DAPPLE_CODESIGN_IDENTITY=<your signing identity>` to the `cmake` command. This must be done at the initial `cmake` configure step, not when running `cpack` later. You can run `security find-identity -p codesigning` to find what identities you have installed on your keychain.

To create the DMG image with the .app bundle inside, run
```shell
cd ~/mixxx/cmake_build
cpack -G DragNDrop
```

The DMG file is created in ~/mixxx/cmake_build. You can run the bundle by double clicking the DMG image in Finder then dragging and dropping the Mixxx.app file inside to /Applications or wherever you would like.

# Set up development tools

Now that you can build Mixxx, learn about [developer tools](https://github.com/mixxxdj/mixxx/wiki/Developer%20Tools) that make Mixxx development easier.
