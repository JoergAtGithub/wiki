*(If you're looking to make an installable release, [go to this
page](Build%20Windows%20installer).)*

# Building Mixxx on Windows

## Programs to install

  - [Visual Studio 15 Update 3 for Windows
    Desktop](https://www.visualstudio.com/downloads/#visual-studio-2015-update-3).
    You need a Microsoft account. Make sure you check the `Programming
    Languages -> Visual C++` feature in the installer. previous versions
    of visual studio are not suitable to build mixxx because their lack
    of support for some C++11 features used in Mixxx code like
    constexpr.
  - Visual Studio 2015 or newer comes with the latest Windows SDK. The
    following links are only needed if you're building for Windows XP.
  - [Microsoft Windows 7 (& .NET 3.5)
    SDK](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=c17ba869-9671-4330-a63e-1fd44e0e2505&displaylang=en)
  - Or the [Windows 7.1 (& .NET 4)
    SDK](http://go.microsoft.com/fwlink/?LinkID=191420) which is
    smaller, newer and includes the compilers (so you may not need
    Visual Studio above if you're just looking to build Mixxx from a
    command line.) This one has a few bugs however (see
    [below](#Prepare-build-environment)) and is missing files needed to
    build 64-bit versions if used without Visual Studio.)
  - [Python](http://python.org/download/) 2.7.x Install for user only\!
    Otherwise scons can't find the installation. Mixxx build scripts are
    not yet compatible with python3 \!
  - [SCONS 2.3.6](http://scons.org/pages/download.html) (version 2.3.6
    is the minimal version that work with visual studio 2015). scons
    version 3.0.0+ has not been validated yet to successfully build
    Mixxx.
  - Install [CMake 3.3.x](http://www.cmake.org/download) with default
    options. The CMake directory does not need to be added to the PATH
    environment variable.
  - A Git client like [Git for
    Windows](https://git-scm.com/download/win),
    [TortoiseGit](https://code.google.com/p/tortoisegit/) or the [github
    windows
    client](http://github-windows.s3.amazonaws.com/GitHubSetup.exe)
    (featuring a unix like command line)

## Prepare build environment

1.  Add to or create the following system environment variables
    ([HowTo](http://www.chem.gla.ac.uk/~louis/software/faq/q1.html),)
    adjusting the paths to match where you actually installed the above.
    `PATH = ;C:\Python27;C:\Python27\Scripts # append to the existing
    variable
    `
2.  There is a bug in at least the Windows 7.1 SDK where it looks in the
    wrong place for the SDK path. (You will get errors like `fatal error
    C1083: Cannot open include file: 'windows.h': No such file or
    directory` unless this is corrected.)
    1.  As an administrator, edit the file `C:\Program Files
        (x86)\Microsoft Visual
        Studio 10.0\Common7\Tools\VCVarsQueryRegistry.bat` and examine
        the `regquery` path under the section `:GetWindowsSdkDirHelper`
        (`%1` is replaced by HKEY\_LOCAL\_MACHINE at runtime.)
    2.  Run `regedit` and browse to that path to make sure it exists and
        that the version number is correct.
    3.  If not, adjust the path in the file to match what you found in
        the registry. (E.g. If you've installed SDK 7.1, change the
        `v7.0A` to `v7.1` in the `regquery` path.

## Acquire Mixxx dependencies

To build Mixxx, you need built copies of its dependencies. You may build
these from source, or download pre-built versions of them from the Mixxx
team.

### Option 1: Download pre-built Mixxx dependencies

You can download a pre-built version of the Mixxx dependencies
[here](http://downloads.mixxx.org/builds/appveyor/environments/2.1/).

You may choose between the "release-fastbuild" and "release" variants.

  - release-fastbuild is built with link-time code-generation (LTCG)
    disabled. This leads to faster builds but potentially results in a
    slower version of Mixxx (we haven't measured it so we don't know).
    When we build Mixxx on AppVeyor for continuous integration, this is
    the version we use.
  - release is the version used to produce Mixxx releases. It is
    compiled with LTCG enabled. 

If you want to build a 32-bit version of Mixxx, choose an "x86" variant.
For 64-bit, choose an "x64" variant.

Download and unzip one of these environments. Remember the folder to
which the repository was saved. We will refer to that folder as
**WINLIB\_PATH** later.

### Option 2: Compile Mixxx dependencies from source

If you want to build the Mixxx dependencies from source instead of
downloading pre-built ones:

1.  Clone the [Mixxx
    buildserver](https://github.com/mixxxdj/buildserver/tree/2.1.x-windows)
    repository. Remember the folder to which the repository was saved.
    We will refer to that folder as **WINLIB\_PATH** later.
2.  In the buildserver repository, checkout the **2.1.x-windows** branch
3.  Edit `%WINLIB_PATH%\build_environment.bat` and change the following
    lines:
    1.  `SET MSVC_PATH=<Visual Studio installation directory>`
    2.  If you're using only the Windows 7.1 SDK (no Visual Studio,)
        `SET MSBUILD=msbuild /p:PlatformToolset=Windows7.1SDK`
          - If using the VC++ Build Tools, you may need to add/replace
            `/p:VCTargetsPath="C:\Program Files
            (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\\"`
4.  Download the [Qt 4.8.7
    Sources](http://download.qt-project.org/official_releases/qt/4.8/4.8.7/qt-everywhere-opensource-src-4.8.7.zip).
    Unpack the zip archive into **WINLIB\_PATH\\build**
5.  Download the [ASIO
    SDK](http://www.steinberg.net/en/company/developers.html). You will
    need a free steinberg development account to do that. Extract the
    files and rename the directory to remove the version number, so
    **ASIOSDK2.3** becomes **ASIOSDK**. Move **ASIOSDK** to
    **WINLIB\_PATH\\build\\pa\_stable\_v19\_20140130\\src\\hostapi\\asio\\**.

<!-- end list -->

1.  Start a Windows command prompt (you do not need a Windows SDK
    command prompt). Open the Start Menu and type "cmd" into the search
    box and hit enter. 
2.  change into the **WINLIB\_PATH** directory.
    1.  `cd WINLIB_PATH_GOES_HERE`
3.  Build the environment:
    1.  `build_environment x86 Release`

This step will take 2-3 hours depending on how many CPU cores you have.
Go have lunch.

### Download Mixxx's source code

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

REM XP Compatibility requires the v7.1A SDK
REM No quotes needed here!
set MSSDK_DIR=C:/Program Files (x86)/Microsoft SDKs/Windows/v7.1A

REM this can be either release or debug. For development you want to use debug
set BUILD_TYPE=release

REM This determines if you build a 32bit or 64bit version of mixxx. 
REM 32bit = i386, 64bit = amd64
set ARCHITECTURE=i386

REM set this to the folder where you built the dependencies
set WINLIB_PATH="**Enter Path to WINLIB_PATH**"
SET BIN_DIR=%WINLIB_PATH%\bin
set QT_VERSION=4.8.7
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
rem /Zc:threadSafeInit- disable C++11 magic static support (Bug #1653368)
set CL=/MP /FS /EHsc /Zc:threadSafeInit-

set PATH=%BIN_DIR%;%PATH%
REM Set the -j value to the number of CPU cores (not HT "virtual" cores but physical cores) you have
scons -j2 toolchain=msvs winlib=%WINLIB_PATH% build=%BUILD_TYPE% staticlibs=1 staticqt=1 verbose=0 machine=%TARGET_MACHINE% qtdir=%QTDIR% hss1394=1 mediafoundation=1 opus=1 localecompare=1 optimize=portable virtualize=0 test=1 qt_sqlite_plugin=0 mssdk_dir="%MSSDK_DIR%" build_number_in_title_bar=0 bundle_pdbs=1
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
