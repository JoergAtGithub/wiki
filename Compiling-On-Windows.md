*(If you're looking to make an installable release, [go to this
page](Build%20Windows%20installer).)*

# Building Mixxx on Windows
Note: These instructions are valid for Mixxx 2.3 onwards. 
 You will find instructions for older release in the History of this wiki page.

## Programs to install

  - [Visual Studio 2022 Community Edition](Visual-Studio-Community.md) or the Visual Studio 2022 Build Tools.

    * 'Visual Studio 2019' and 'Visual Studio 2017' are **too old** for building Mixxx, but only because the CMake version that comes with it is too old.
    * 'Visual Studio Code' is **not suitable** for building Mixxx on Windows!

  - A Git client like [Git for Windows](https://git-scm.com/download/win),
    [TortoiseGit](https://tortoisegit.org) (requires Git for Windows to be installed) or the
	[github windows client](http://github-windows.s3.amazonaws.com/GitHubSetup.exe)

    Both Git for Windows and github windows feature a unix like command line.

  - Windows Powershell 5.1 or later
    
    (Windows 10 comes with 5.1) for older Windows releases it need to be downloaded here: https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/install/installing-windows-powershell?view=powershell-5.1#upgrading-existing-windows-powershell

  - **Optional** and **Not Recommended**: The compiler cache [sccache](https://github.com/mozilla/sccache) and the [Rust](https://www.rust-lang.org/) framework

    This can accelerate repeated builds, when you often switch between different branches. But in many other cases the build without sccache, but with pre-compiled headers (PCH) instead (enabled by default), is faster.

    When Rust is installed, open a console window and type
    `cargo install --git https://github.com/Be-ing/sccache.git --branch fix_msvc_fp`  
    (Temporarily using a fork to fix an error with the /FP parameter)

## Download Mixxx's source code

If you want to compile Mixxx, you'll need to download the source code. Source archives for releases are on [downloads.mixxx.org](https://downloads.mixxx.org/), but if you want to contribute to Mixxx, we recommend forking the project. Check out [Set up Git](https://github.com/mixxxdj/mixxx/wiki/Using-Git.md#set-up-git) to get started.

## Acquire Mixxx dependencies

To build Mixxx, you need built copies of its dependencies. Mixxx uses the VCPKG pacakge manager to build the dependencies (also called build environment or buildenv). this is maintained in the repo https://github.com/mixxxdj/vcpkg
You may download pre-built versions of them from the Mixxx team (recommended)
or build them from source.

### Option 1: Download pre-built Mixxx dependencies automatically

The easiest option to get the built dependencies is to use the script located in 
**MIXXX\_REPO**/tools/windows_buildenv.bat.

This script will download the appropriate file from Mixxx servers, and autogenerate a 
CMakeSettings.json file which can later be used to build Mixxx with 
the default settings from Visual Studio.

It will download the dependencies to **MIXXX\_REPO**\buildenv\mixxx-deps-2.4-x64-windows-92b7b90.zip and extract the ZIP archive to a directory with the same name.

### Option 2: Download pre-built Mixxx dependencies manually

You find the ZIP archives at: https://downloads.mixxx.org/dependencies/2.4/Windows/
The folder `2.?.x-windows` contains build environments for the `2.?`
release of Mixxx. If you are working on the Main branch, always pick
the latest version. If you want to work on a specific branch, pick the
corresponding folder. Check the
[packaging/windows/build\_environment](https://github.com/mixxxdj/mixxx/blob/main/packaging/windows/build_environment)
file in the Mixxx codebase to see what version of the build environment
is currently used for builds.

Download and unzip one of these environments. 
The current recommended folder is inside **MIXXX\_REPO**\buildenv 
(example: **MIXXX\_REPO**\buildenv\mixxx-deps-2.4-x64-windows-92b7b90).

### Option 3: Compile Mixxx dependencies from source

If you want to build the Mixxx dependencies from source instead of
downloading pre-built ones:

1.  Clone the [Mixxx buildserver repository](https://github.com/mixxxdj/VCPKG).  
    Remember the folder to which the repository was saved.
2.  Github actions will build it automatically according the setup (including the list of dependencies) in https://github.com/mixxxdj/vcpkg/blob/2.4/.github/workflows/build.yml
3.  When Github Action finishes the build, you can download the buildenv as ZIP file from the artifacts.

The build will take some hours.

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
   The CMakeSettings uses names like x64__portable and so on. Most likely, the one you want is x64_portable.
   By default it will also generate the CMake cache using the configuration. 
   You can also run it manually (and clean and regenerate it) by selecting the 
   CMakeLists.txt file, and use the options Generate cache or CMake cache -> delete cache.

3. Go to Build-> Build All Menu option. The build should start. 
   Depending on your processor, a full build can take from 5 to 20 minutes.


### From commandline

1. Open the application "x64 Native Tools command prompt for VS2022" from the Windows Start menu.
   There, go to **MIXXX\_REPO** folder

2. Create a folder where we will setup cmake and build the sources. 
   Usually we call this **MIXXX\_REPO**\build\
   It is recommended that you actually create subfolders for different builds, as in: 

   `**MIXXX\_REPO**\build\x64__portable`

   `**MIXXX\_REPO**\build\x64__native`

   `**MIXXX\_REPO**\build\x64__off`

   Do the same for the install subdir ( **MIXXX\_REPO**\install\x64_portable)

3. enter into this directory, ` cd build\x64__portable` and type the following:
   `cmake -DCMAKE_INSTALL_PREFIX=**MIXXX\_REPO**\install\x64_portable 
 -DDEBUG_ASSERTIONS_FATAL=ON -DHSS1394=ON -DKEYFINDER=OFF -DLOCALECOMPARE=ON 
 -DMAD=ON -DMEDIAFOUNDATION=ON -DSTATIC_DEPS=ON -DBATTERY=ON -DBROADCAST=ON -DBULK=ON 
 -DHID=ON -DLILV=ON -DOPUS=ON -DQTKEYCHAIN=ON -DVINYLCONTROL=ON ..\..`

  The last part of the command "..\\.." means **MIXXX\_REPO** as seen from 
  the cmake build dir (in our case  **MIXXX\_REPO**\build\x64__portable, so two subfolders)

  Set -DDEBUG_ASSERTIONS_FATAL=OFF instead of ON if you need a stable release build - without
  assertions that close Mixxx with error message.
  This behavior is intended to detect errors quickly, in development builds.

4. Once it completes without errors, you can type `cmake --build .` so that it starts building. 
  Depending on your processor, a full build can take from 5 to 20 minutes.

  In order to do a clean build, you can do so with `cmake --build . --clean-first`
