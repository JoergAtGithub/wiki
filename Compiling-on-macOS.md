Compiling software is the process of turning human-readable source code into machine code a computer can execute. Compiling Mixxx is fairly straightforward on macOS. The steps below outline what to do. If you need help after reading this page, feel free to ask questions on our [Zulip chat](https://mixxx.zulipchat.com/#narrow/stream/247620-development-help).

This is a guide for x64 architecture. Building on Apple Silicon/M1/aarch64 is not yet official supported, but possible. Consult our [Zulip chat](https://mixxx.zulipchat.com). You may have to [compile the dependencies](https://github.com/mixxxdj/mixxx/wiki/Compiling-dependencies-for-macOS-arm64) yourself, instead of using the archive with precompiled dependencies as described below.

# Install Xcode command line tools

First, install the clang compiler and macOS SDK from the Xcode command line tools. If you have the Xcode IDE installed, you already have the command line tools too. To install the Xcode command line tools without the Xcode IDE, launch the Terminal application, and type the following command:

```shell
xcode-select --install
```

Click "Install" on the software update popup window that will appear and wait for the download and installation to finish (about 150 MB).

# Download Mixxx source code

If you want to compile Mixxx, you'll need to download the source code. Source archives for releases are on [downloads.mixxx.org](https://downloads.mixxx.org/), but if you want to contribute to Mixxx, we recommend forking the project. Check out [Set up Git](https://github.com/mixxxdj/mixxx/wiki/Using-Git.md#set-up-git) to get started.

# Install build dependencies

There is a script at `tools/macos_buildenv.sh` inside the Mixxx source code repository which automatically downloads an archive with all the precompiled dependencies and build tools that Mixxx requires (apart-from-the-Xcode-command-line-tools-[explained-above](.md#install-xcode-command-line-tools)). The script also sets environment variables needed to compile Mixxx. Run the script with `source` to set up your build environment. Assuming you have the Mixxx source code in ~/mixxx, run the following command (replace ~/mixxx if you put the source code elsewhere):

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

# Configure CMake

_CMake support is new in Mixxx 2.3. The rest of this page does not apply for earlier versions of Mixxx._

Before configuring the build, make sure to disable macOS Gatekeeper as described in [this article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave). Otherwise, macOS will prevent the pre-built environment bundled binaries from executing.

Run the following `cmake` command to configure the project with the recommended default settings for development. This assumes you have set the environment variables after installing dependencies as [described above](#install-build-dependencies) and you have the Mixxx source code in `~/mixxx`. If you have the source code elsewhere, substitute that for `~/mixxx` in the following commands.

```shell
cmake -DCMAKE_BUILD_TYPE=Debug -DDEBUG_ASSERTIONS_FATAL=ON -S ~/mixxx -B ~/mixxx/build
```

Now you can enable Gatekeeper again as described in this [article](https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave).

This step only needs to be done once or repeated when you want to change the cmake configuration. Otherwise you can simply rerun the build step below to compile different code.

# Build Mixxx

Run:
```shell
cmake --build ~/mixxx/build --parallel $(sysctl -n hw.physicalcpu)
```
This could take a long time depending on the speed of your CPU. Future builds will be much faster (depending on how much code has changed) because cmake automatically uses [ccache](https://ccache.dev/). ccache is included in the [prebuilt environment](#recommended-pre-built-environment).

# Run Mixxx

The `mixxx` binary is output in the cmake build directory:
```shell
~/mixxx/build/mixxx
```

If you get an error saying `Could not find the Qt platform plugin "cocoa" in ""`, you have not set the `QT_QPA_PLATFORM_PLUGIN_PATH` environment variable. Source the [macos_buildenv.sh script](#recommended-pre-built-environment) to set it.

# Build Mixxx.app bundle and DMG image

Generating the .app has some expensive scanning and relinking steps. So, for development, we recommend skipping this step. Generally you would only need to build a bundle locally if you are working on the bundle building process. GitHub Actions automatically builds bundles with each Git commit pushed to GitHub (including in your own fork) so you can direct users to download the GitHub Actions artifact if you want to ask someone to test your code.

Add `-DMACOS_BUNDLE=ON` to the first `cmake` command above when [configuring the build](#configure-cmake). You must rerun the `cmake` configure command with this option if you have already run it before.

To sign the `.app` bundle inside the DMG image, add `-DAPPLE_CODESIGN_IDENTITY=<your signing identity>` to the `cmake` command. This must be done at the initial `cmake` configure step, not when running `cpack` later. You can run `security find-identity -p codesigning` to find what identities you have installed on your keychain.

To create the DMG image with the .app bundle inside, run
```shell
cd ~/mixxx/build
cpack -G DragNDrop
```

The DMG file is created in ~/mixxx/build. You can run the bundle by double clicking the DMG image in Finder then dragging and dropping the Mixxx.app file inside to /Applications or wherever you would like.

# Set up development tools

Now that you can build Mixxx, learn about [developer tools](https://github.com/mixxxdj/mixxx/wiki/Developer-Tools.md) that make Mixxx development easier.
