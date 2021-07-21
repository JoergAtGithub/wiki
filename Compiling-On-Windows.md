*(If you're looking to make an installable release, [go to this
page](Build%20Windows%20installer).)*

# Building Mixxx on Windows
Note: These instructions are valid for Mixxx 2.3 onwards. 
Mixxx 2.2 and below used Scons instead of CMake.
 You will find instructions for that older release in the History of this wiki page.

## Programs to install

  - [Visual Studio 2019 Community Edition](Visual%20Studio%20Community) or the Visual Studio 2019 Build Tools.

    Follow the installation instructions on that link to setup the compiler and CMake.

    _'Visual Studio Code' is not suitable for building Mixxx on Windows!<br>_
    _The CMake version that comes with 'Visual Studio 2017' is too old for building Mixxx!_

  - A Git client like [Git for Windows](https://git-scm.com/download/win),
    [TortoiseGit](https://tortoisegit.org) (requires Git for Windows to be installed) or the
	[github windows client](http://github-windows.s3.amazonaws.com/GitHubSetup.exe)

    Both Git for Windows and github windows feature a unix like command line.
  - Optional: [Rust](https://www.rust-lang.org/) and [sccache](https://github.com/mozilla/sccache)

    This is needed if you want to use sccache when building from commandline.

    When Rust is installed, open a console window and type
    `cargo install --git https://github.com/Be-ing/sccache.git --branch fix_msvc_fp`  
    (Temporarily using a fork to fix an error with the /FP parameter)

  - Windows Powershell 5.1 or later
    
    (Windows 10 comes with 5.1) for older Windows releases it need to be downloaded here: https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/install/installing-windows-powershell?view=powershell-5.1#upgrading-existing-windows-powershell

## Download Mixxx's source code

If you want to compile Mixxx, you'll need to download the source code. Source archives for releases are on [downloads.mixxx.org](https://downloads.mixxx.org/), but if you want to contribute to Mixxx, we recommend checking out a snapshot from our git repository instead:

  - For the latest development (main) branch: `git clone https://github.com/mixxxdj/mixxx.git`
  - For the latest beta branch: `git clone -b 2.3 https://github.com/mixxxdj/mixxx.git`
  - For the latest stable branch: `git clone -b 2.2 https://github.com/mixxxdj/mixxx.git`

To update to the latest version of a git branch, enter (`dir` into) the directory you cloned the git repository into and run `git pull`. Refer to [Using Git](https://github.com/mixxxdj/mixxx/wiki/Using%20Git) for more details.

If you plan to contribute back your code changes to the official Mixxx project, you should fork Mixxx and clone your fork instead. See [Using Git](https://github.com/mixxxdj/mixxx/wiki/Using%20Git) for more info.

## Acquire Mixxx dependencies

To build Mixxx, you need built copies of its dependencies.
You may download pre-built versions of them from the Mixxx team (recommended)
or build them from source.

### Option 1: Download pre-built Mixxx dependencies automatically

The easiest option to get the built dependencies is to use the script located in 
**MIXXX\_REPO**/tools/windows_buildenv.bat.

This script will download the appropriate file from Mixxx servers, and autogenerate a 
CMakeSettings.json file which can later be used to build Mixxx with 
the default settings from Visual Studio.

It will download the dependencies to **MIXXX\_REPO**\buildenv\2.3-j00019-x64-release-fastbuild-static-55e94982-minimal
We will refer to this folder as **WINLIB\_PATH** later.

### Option 2: Download pre-built Mixxx dependencies manually

Alternatively, you can find links to pre-built Mixxx dependencies at the bottom 
of this [Github Page](https://github.com/mixxxdj/buildserver).

The folder `2.?.x-windows` contains build environments for the `2.?`
release of Mixxx. If you are working on the master branch, always pick
the latest version. If you want to work on a specific branch, pick the
corresponding folder. Check the
[packaging/windows/build\_environment](https://github.com/mixxxdj/mixxx/blob/master/packaging/windows/build_environment)
file in the Mixxx codebase to see what version of the build environment
is currently used for builds.

The current recommended variant is "release". Release is the version used 
to produce Mixxx releases. It is compiled with LTCG enabled and requires 
at least 8 GB of memory (or equivalent free space on the disk with your [paging
file](https://www.howtogeek.com/126430/htg-explains-what-is-the-windows-page-file-and-should-you-disable-it/))
to link Mixxx.

If you want to build a 32-bit version of Mixxx, choose an "x86" variant.
For 64-bit, choose an "x64" variant.

Download and unzip one of these environments. 
The current recommended folder is inside **MIXXX\_REPO**\buildenv 
(example: **MIXXX\_REPO**\buildenv\2.3-j00019-x64-release-fastbuild-static-55e94982-minimal).
We will refer to this folder as **WINLIB\_PATH** later.

### Option 3: Compile Mixxx dependencies from source

If you want to build the Mixxx dependencies from source instead of
downloading pre-built ones:

1.  Clone the [Mixxx buildserver repository](https://github.com/mixxxdj/buildserver).  
    Remember the folder to which the repository was saved. We will refer
    to that folder as **WINLIB\_PATH** later.
2.  In the buildserver repository, checkout the **2.?.x-windows**
    branch, depending on which version of Mixxx you are building the
    dependencies for.
3.  Start a Windows command prompt (you do not need a Windows SDK
    command prompt). Open the Start Menu and type "cmd" into the search
    box and hit enter. 
4.  Change into the **WINLIB\_PATH** directory.  
    `cd WINLIB_PATH_GOES_HERE`
5.  Build the environment:
    - 32-bit: `build_environment x86 Release`
    - 64-bit: `build_environment x64 Release`

This step will take 2-3 hours depending on how many CPU cores you have.
Go have lunch.

## Build Mixxx
### From Visual Studio
1. If you have not run **MIXXX\_REPO**/tools/windows_buildenv.bat, it is recommended to do so. 
   It will also generate a CMakeSettings.json that is used by Visual Studio 
   so you don't need to generate it manually.

2. Open Visual Studio. 

   It will ask to open a project, select open Folder and select **MIXXX\_REPO**. 
   It will detect it as a CMake project. 
   You can also do so from File-Open->CMake... and select the CMakeLists.txt file 
   from **MIXXX\_REPO**.

   Select the correct build configuration on the toolbar.
   The CMakeSettings uses names like x64__fastbuild and so on. Most likely, the one you want is x64_portable.
   By default it will also generate the CMake cache using the configuration. 
   You can also run it manually (and clean and regenerate it) by selecting the 
   CMakeLists.txt file, and use the options Generate cache or CMake cache -> delete cache.

3. Go to Compile -> Compile All Menu option. The build should start. 
   Depending on your processor, a full build can take from 5 to 20 minutes.


### From commandline

1. Open the application "x64 Native Tools command prompt for VS2019" from the Windows Start menu.
   There, go to **MIXXX\_REPO** folder

2. Create a folder where we will setup cmake and build the sources. 
   Usually we call this **MIXXX\_REPO**\build\
   It is recommended that you actually create subfolders for different builds, as in: 

   `**MIXXX\_REPO**\build\x64__portable`

   `**MIXXX\_REPO**\build\x86__portable`

   `**MIXXX\_REPO**\build\x64__debug`

   Do the same for the install subdir ( **MIXXX\_REPO**\install\x64_portable)

3. enter into this directory, ` cd build\x64__portable` and type the following:
   `cmake -G "Ninja" -DCMAKE_BUILD_TYPE=Release 
 -DCMAKE_PREFIX_PATH="**WINLIB\_PATH**;**WINLIB\_PATH**\Qt-5.14.2" 
 -DCMAKE_INSTALL_PREFIX=**MIXXX\_REPO**\install\x64_portable 
 -DDEBUG_ASSERTIONS_FATAL=ON -DHSS1394=ON -DKEYFINDER=OFF -DLOCALECOMPARE=ON 
 -DMAD=ON -DMEDIAFOUNDATION=ON -DSTATIC_DEPS=ON -DBATTERY=ON -DBROADCAST=ON -DBULK=ON 
 -DHID=ON -DLILV=ON -DOPUS=ON -DQTKEYCHAIN=ON -DVINYLCONTROL=ON ..\..`

  You need to replace **WINLIB\_PATH** and **MIXXX\_REPO** for your paths, 
  as well as adapting the install subdir if you build a different one.
  Also, the last part of the command "..\\.." means **MIXXX\_REPO** as seen from 
  the cmake build dir (in our case  **MIXXX\_REPO**\build\x64__portable, so two subfolders)

  Finally, set -DDEBUG_ASSERTIONS_FATAL=OFF instead of ON if you get assertion errors
  that close Mixxx. This is intended to detect errors quickly, but 
  might be completely unexpected sometimes.

4. Once it completes without errors, you can type `cmake --build .` so that it starts building. 
  Depending on your processor, a full build can take from 5 to 20 minutes.

  In order to do a clean build, you can do so with `cmake --build . --clean-first`

### Build 32bit version of Mixxx
32bit versions are no longer being built, so they might stop working at some point. Anyway, these are some instructions on how you can do that.

1. Get the dependencies for 32bit:
   Either set the environment variable PLATFORM=x86 previous to execute the tools/windows_buildenv.bat script, 
   or manually download the one for x86, 
   or build it manually

2. Follow the instructions to build from commandline, but instead open a 
   *x86 Native tools command prompt for VS2019* 
   (or x86_64 cross compile command prompt for VS2019). (Preferably the latter)

**WARNING**: DO NOT mix 32 and 64 bits builds. Use separate console windows 
and separate precompiled directories and cmake build directories


## Build debug version of Mixxx

1. There are no precompiled environments for debug, so this means that you have to  
    compile Mixxx dependencies from source as explained above. 
    You will need to indicate this commandline to generate them in debug: 
    `build_environment xxx Debug`
2. Follow the instructions to build from commandline, but on the cmake instructions 
   specify **-DCMAKE_BUILD_TYPE=Debug** instead of *DCMAKE_BUILD_TYPE=Release*.

**WARNING**: DO NOT mix release and debug builds. Use separate console windows 
and separate precompiled directories and cmake build directories
