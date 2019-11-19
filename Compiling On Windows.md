*(If you're looking to make an installable release, [go to this
page](Build%20Windows%20installer).)*

# Building Mixxx on Windows

## Programs to install

  - Visual Studio 2017 Community Edition or the Visual Studio 2017 Build
    Tools.
  - (Visual Studio 2015 may work, but will likely stop working once we
    start using C++ features that are not implemented by VS2015).
  - [Python](http://python.org/download/) 2.7.x. Ensure Python is on
    your system PATH (there is an option in the installer to do this).
    Don't use Python 3.x as [Scons is not compatible with
    it](https://github.com/SCons/scons/wiki/FrequentlyAskedQuestions#what-version-of-python-do-i-need).
  - [SCONS](http://scons.org/pages/download.html) (download the latest
    version).
  - A Git client like [Git for
    Windows](https://git-scm.com/download/win),
    [TortoiseGit](https://code.google.com/p/tortoisegit/) or the [github
    windows
    client](http://github-windows.s3.amazonaws.com/GitHubSetup.exe)
    (featuring a unix like command line)

## Acquire Mixxx dependencies

To build Mixxx, you need built copies of its dependencies. You may
download pre-built versions of them from the Mixxx team (recommended) or
build them from source.

### Option 1: Download pre-built Mixxx dependencies

You can find pre-built Mixxx dependencies at the bottom of this [Github
Page](https://github.com/mixxxdj/buildserver).

The folder `2.?.x-windows` contains build environments for the `2.?`
release of Mixxx. If you are working on the master branch, always pick
the latest version. If you want to work on a specific branch, pick the
corresponding folder. Check the
[build/windows/golden\_environment](https://github.com/mixxxdj/mixxx/blob/master/build/windows/golden_environment)
file in the Mixxx codebase to see what version of the build environment
is currently used for builds.

You may choose between the "release-fastbuild" and "release" variants.

  - release-fastbuild is built with link-time code-generation (LTCG)
    disabled. This leads to faster builds but potentially results in a
    slower version of Mixxx (we haven't measured it so we don't know).
    When we build Mixxx on AppVeyor for continuous integration, this is
    the version we use.
  - release is the version used to produce Mixxx releases. It is
    compiled with LTCG enabled and requires at least 8 GB of memory (or
    equivalent free space on the disk with your [paging
    file](https://www.howtogeek.com/126430/htg-explains-what-is-the-windows-page-file-and-should-you-disable-it/))
    to link Mixxx.

If you want to build a 32-bit version of Mixxx, choose an "x86" variant.
For 64-bit, choose an "x64" variant.

Download and unzip one of these environments. Remember the folder to
which the repository was saved. We will refer to that folder as
**WINLIB\_PATH** later.

### Option 2: Compile Mixxx dependencies from source

If you want to build the Mixxx dependencies from source instead of
downloading pre-built ones:

1.  Clone the [Mixxx
    buildserver](https://github.com/mixxxdj/buildserver) repository.
    Remember the folder to which the repository was saved. We will refer
    to that folder as **WINLIB\_PATH** later.
2.  In the buildserver repository, checkout the **2.?.x-windows**
    branch, depending on which version of Mixxx you are building the
    dependencies for.
3.  Start a Windows command prompt (you do not need a Windows SDK
    command prompt). Open the Start Menu and type "cmd" into the search
    box and hit enter. 
4.  change into the **WINLIB\_PATH** directory.
    1.  `cd WINLIB_PATH_GOES_HERE`
5.  Build the environment:
    1.  32-bit: `build_environment x86 Release`
    2.  64-bit: `build_environment x64 Release`

This step will take 2-3 hours depending on how many CPU cores you have.
Go have lunch.

## Download Mixxx's source code

1.  Clone the [Mixxx](https://github.com/mixxxdj/mixxx.git) repository.
    Remember the folder to which the repository was saved. We will refer
    to that folder as **MIXXX\_REPO** later.
2.  Start a command prompt (it doesn't need to be a Windows SDK prompt)
    and change into the **MIXXX\_REPO** directory.
3.  create a file called `build.bat` with the following content:

<!-- end list -->

``` 
@echo off
SETLOCAL
REM Clean up after old builds.
del /q /f *.exe
rmdir /s /q dist32
rmdir /s /q dist64

REM this can be either release or debug. For development you want to use debug
set BUILD_TYPE=release

REM This determines if you build a 32bit or 64bit version of mixxx. 
REM 32bit = i386, 64bit = amd64
set ARCHITECTURE=i386

REM set this to the folder where you built the dependencies
set WINLIB_PATH="**Enter Path to WINLIB_PATH**"
SET BIN_DIR=%WINLIB_PATH%\bin
REM make sure the Qt version matches the version in WINLIB_PATH.
set QT_VERSION=5.11.2
SET QTDIR=%WINLIB_PATH%\Qt-%QT_VERSION%

if "%ARCHITECTURE%" == "i386" (
  set TARGET_MACHINE=x86
  set VCVARS_ARCH=x86
) else ( 
  set TARGET_MACHINE=amd64
  set VCVARS_ARCH=x86_amd64
)

REM Adjust to your environment
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" %VCVARS_ARCH%

rem /MP Use all CPU cores.
rem /FS force synchronous PDB writes (prevents PDB corruption with /MP)
rem /EHsc Do not handle SEH in try / except blocks.
set CL=/MP /FS /EHsc

set PATH=%BIN_DIR%;%PATH%
REM Set the -j value to the number of CPU cores (not HT "virtual" cores but physical cores) you have
scons -j2 toolchain=msvs winlib=%WINLIB_PATH% build=%BUILD_TYPE% staticlibs=1 staticqt=1 verbose=0 machine=%TARGET_MACHINE% qtdir=%QTDIR% hss1394=1 mediafoundation=1 opus=1 localecompare=1 optimize=portable virtualize=0 test=1 qt_sqlite_plugin=0 build_number_in_title_bar=0 bundle_pdbs=1
ENDLOCAL
 
```

This script will setup the build environment and call scons with the
appropriate flags. You have to edit the **WINLIB\_PATH** variable and
set it to the absolute path of the folder where you compiled the
dependencies for mixxx. If you build the environment yourself instead of
using the precompiled environment, you will need to adjust the **QTDIR**
variable too. When you are ready, type:

    build.bat

## Build 64bit version of Mixxx

You have to follow the above guide with two changes.

1.  Build the dependencies with: `build_environment x64 Release` or make
    sure you have downloaded the x64 version of the pre-built
    dependencies.
2.  Use **set ARCHITECTURE=amd64** in **build.bat**

**WARNING**: DO NOT mix 32 and 64 bits build in the same CMD Shell
window or you will have undetermined results. If you need 32 and 64 bits
environments together, use different terminal window for 32 bits and 64
bits build\_environment and mixxx compilation

## Build debug version of Mixxx

You have to follow the above guide with two changes.

1.  Build the dependencies with: `build_environment xxx Debug`
2.  Use **set BUILD\_TYPE=debug** in **build.bat**
