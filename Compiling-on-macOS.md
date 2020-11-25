Compiling Mixxx for macOS is simple if you follow the step-by-step instructions below. This guide assumes you have basic knowledge about using the command line. If you need help after reading this page, feel free to ask questions on our [Zulip chat](https://mixxx.zulipchat.com/#narrow/stream/247620-development-help).

# Install Xcode command line tools

First, install the clang compiler and macOS SDK in the Xcode command line tools. If you have the Xcode IDE installed, you already have the command line tools too. To install them, launch the Terminal application, and type the following command:

```shell
xcode-select --install
```

Click "Install" on the software update popup window that will appear and wait for the download and installation to finish (about 150 MB).

# Download Mixxx source code

If you want to compile Mixxx, you'll need to download the source code. Source archives for the latest release are on our [downloads
page](https://www.mixxx.org/download), but if you want to contribute to Mixxx, we recommend checking out a snapshot from our git repository instead:

  - For the latest development (main) branch: `git clone https://github.com/mixxxdj/mixxx.git`
  - For the latest beta branch: `git clone -b 2.3 https://github.com/mixxxdj/mixxx.git`
  - For the latest stable branch: `git clone -b 2.2 https://github.com/mixxxdj/mixxx.git`

To update to the latest version of a git branch, enter (`cd` into) the directory you cloned the git repository into and run `git pull`. Refer to [Using Git](https://github.com/mixxxdj/mixxx/wiki/Using%20Git) for more details.

# Install build dependencies

You have several options how to install the libraries and build tools Mixxx requires.

## Recommended: Pre-built environment

There is a script at `tools/macos_buildenv.sh` inside the Mixxx source code repository which automatically downloads an archive with all the precompiled dependencies and build tools that Mixxx requires (apart from the Xcode command line tools [explained above](#install-xcode-command-line-tools)). The script also sets environment variables needed to compile Mixxx. Run the script with `source` to set up your build environment. Assuming you have the Mixxx source code in ~/mixxx, run the following command (replace ~/mixxx if you put the source code elsewhere):

```shell
source ~/mixxx/tools/macos_buildenv.sh setup
```

To avoid having to manually run this to set the environment variables every time you start a new shell, you can have your shell automatically run it on startup. If you use zsh (the default shell with macOS >= 10.15), set this up by running this once:

```shell
echo "source ~/mixxx/tools/macos_buildenv.sh setup --profile" >> ~/.zprofile
```

If you use bash (the default shell with macOS <= 10.14), set this up by running this once:

```shell
echo "source ~/mixxx/tools/macos_buildenv.sh setup --profile" >> ~/.profile
```

The `--profile` option prevents the script from spamming your terminal every time you start a new shell.

The script is compatible with both zsh and bash.

## Homebrew

**There is currently a major performance problem with current versions of Qt in Homebrew and Mixxx on macOS. We recommend [using our prebuilt
dependencies](#Recommended-Pre-built-environment) with Qt 5.12 until this is [fixed](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/QOpenGLWidget.20migration).**

We generally recommend using the [prebuilt environment](#recommended-pre-built-environment) so that you are using the same versions of dependencies as our official builds from GitHub Actions. However, if you want to use [Homebrew](https://github.com/Homebrew/brew) instead, you can do so. Assuming you have already installed Homebrew and gotten it working, open the [Terminal](http://www.apple.com/macosx/apps/all.html#terminal) application and use the following command to install the necessary libraries:

```shell
brew install scons cmake ccache pkg-config portaudio libsndfile libogg libvorbis portmidi git taglib libshout protobuf flac libjpeg qt5 chromaprint rubberband fftw vamp-plugin-sdk opusfile lilv lame qtkeychain
```

Then set some environment variables which will be used to configure `cmake` below: 

```shell
export CMAKE_PREFIX_PATH=/usr/local/opt/
export Qt5_DIR=/usr/local/opt/qt5/cmake/Qt5/
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

You can use the [scripts used to make the prebuilt environment](https://github.com/mixxxdj/buildserver) locally if you want to do it yourself. Generally this is a waste of time unless you are working on changing the prebuilt environment. Refer to the [GitHub Actions CI script](https://github.com/mixxxdj/buildserver/blob/2.3.x-unix/.github/workflows/build-environment-build.yml) for how to use the build scripts.

# Configure CMake

Before configuring the build, make sure to disable macOS Gatekeeper as described in [this article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave). Otherwise, macOS will prevent the pre-built environment bundled binaries from executing.

Run the following `cmake` command to configure the project with the recommended default settings for development. This assumes you have set the environment variables after installing dependencies as [described above](#install-build-dependencies) and you have the Mixxx source code in `~/mixxx`. If you have the source code elsewhere, substitute that for `~/mixxx` in the following commands.

```shell
cmake -DCMAKE_BUILD_TYPE=Debug -DDEBUG_ASSERTIONS_FATAL=ON -S ~/mixxx -B ~/mixxx/cmake_build
```

Now you can enable Gatekeeper again as described in this [article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave).

This step only needs to be done once or repeated when you want to change the cmake configuration. Otherwise you can simply rerun the build step below to compile different code.

# Build Mixxx

Run:
```shell
cmake --build ~/mixxx/cmake_build --parallel $(sysctl -n hw.physicalcpu)
```
This could take a long time depending on the speed of your CPU. Future builds will be much faster (depending on how much code has changed) because cmake automatically uses [ccache](https://ccache.dev/). ccache is included in the [prebuilt environment](#recommended-pre-built-environment).

# Run Mixxx

The `mixxx` binary is output in the cmake build directory:
```shell
~/mixxx/cmake_build/mixxx
```

If you get an error saying `Could not find the Qt platform plugin "cocoa" in ""`, you have not set the `QT_QPA_PLATFORM_PLUGIN_PATH` environment variable. Source the [macos_buildenv.sh script](#recommended-pre-built-environment) to set it.

# Build Mixxx.app bundle and DMG image

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
