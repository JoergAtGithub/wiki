*(If you're looking to make an installable release, [go to this
page](Build%20Windows%20installer).)*

# Building Mixxx on Windows

## Build 32bit version of Mixxx

### Programs to install

  - [Visual Studio 13 for Windows
    Desktop](http://www.visualstudio.com/downloads/download-visual-studio-vs).
    You need a Microsoft account.

We are currently also testing the [Microsoft Visual C++ Build
Tools](http://go.microsoft.com/fwlink/?LinkId=691132) package which
explicitly enables building applications without Visual Studio
installed. It's currently a technical preview, but you can [search
here](https://www.microsoft.com/en-gb/search/DownloadsDrillInResults.aspx?q=C%2b%2b+build+tools&cateorder=1_5_2_3&sortby=-availabledate)
(order by newest to oldest) to see when it's officially released. If you
use this, you do not need to download any Windows SDKs below since this
will install the one(s) you select as well. (Currently it won't build
unless you install the Windows 10 SDK as well as the 8.1 SDK.) If
however you are building for Windows XP, you **will** need the Windows
7.1 SDK below as well.

  - If you install Visual Studio 2013 or newer, it comes with the latest
    Windows SDK. The following links are only needed if you have a
    version of Visual Studio older than this or if you're building for
    Windows XP.
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
    Otherwise scons can't find the installation
  - [SCONS 2.3.3](http://scons.org/pages/download.html)
  - Install [CMake 3.3.x](http://www.cmake.org/download) with default
    options. The CMake directory does not need to be added to the PATH
    environment variable.
  - A Git client like [Git for
    Windows](https://git-scm.com/download/win),
    [TortoiseGit](https://code.google.com/p/tortoisegit/) or the [github
    windows
    client](http://github-windows.s3.amazonaws.com/GitHubSetup.exe)
    (featuring a unix like command line)

### Prepare build environment

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

### Download mixxx dependencies

1.  Clone the [Mixxx
    buildserver](https://github.com/mixxxdj/buildserver/tree/windows_environment)
    repository. Remember the folder to which the repository was saved.
    We will refer to that folder as **WINLIB\_PATH** later.
2.  In the buildserver repository, checkout the **windows\_environment**
    branch
3.  Edit `%WINLIB_PATH%\build_environment.bat` and change the following
    lines:
    1.  `SET MSVC_PATH=<path containing the vcvarsall.bat file>`
    2.  If you're using only the Windows 7.1 SDK (no Visual Studio,)
        `SET MSBUILD=msbuild /p:PlatformToolset=Windows7.1SDK`
          - If using the VC++ Build Tools, you may need to add/replace
            `/p:VCTargetsPath="C:\Program Files
            (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\\"`
4.  Download the [Qt
    Sources](http://download.qt-project.org/official_releases/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.zip).
    Unpack the zip archive into **WINLIB\_PATH\\build**
5.  Download the [ASIO
    SDK](http://www.steinberg.net/en/company/developers.html). You will
    need a free steinberg development account to do that. Extract the
    files and rename the directory to remove the version number, so
    **ASIOSDK2.3** becomes **ASIOSDK**. Move **ASIOSDK** to
    **WINLIB\_PATH\\build\\pa\_stable\_v19\_20140130\\src\\hostapi\\asio\\**.

### Build dependencies

Start the Windows SDK command prompt (E.g. Start Menu\\Microsoft Windows
SDK v.7.0\\CMD Shell) and change into the **WINLIB\_PATH** directory.
Type:

    build_environment x86 Release

This step may take a while depending on your computer.

### Download mixxx-sources

1.  Clone the [Mixxx](https://github.com/mixxxdj/mixxx.git) repository.
    Remember the folder to which the repository was saved. We will refer
    to that folder as **MIXXX\_REPO** later.
2.  Start the Windows SDK command prompt (E.g. Start Menu\\Microsoft
    Windows SDK v.7.0\\CMD Shell) and change into the **MIXXX\_REPO**
    directory.
3.  create a file called `build.bat` with the following content:

<!-- end list -->

    REM Clean up after old builds.
    del /q /f *.exe
    rmdir /s /q dist32
    rmdir /s /q dist64
    
    REM XP Compatibility requires the v7.1A SDK
    set MSSDK_DIR="c:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A"
    
    REM this can be either release or debug. For development you want to use debug
    set BUILD_TYPE=release
    
    REM This determines if you build a 32bit or 64bit version of mixxx. 
    REM 32bit = i386, 64bit = amd64
    set ARCHITECTURE=i386
    
    REM set this to the folder where you build the dependencies
    set WINLIB_PATH= **Enter Path to WINLIB_PATH**
    
    if "%ARCHITECTURE%" == "i386" (
      set TARGET_MACHINE=x86
      set VCVARS_ARCH=x86
    ) else ( 
      set TARGET_MACHINE=amd64
      set VCVARS_ARCH=x86_amd64
    )
    
    call "c:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat" %VCVARS_ARCH%
    
    scons winlib=%WINLIB_PATH% qtdir=%WINLIB_PATH%\build\qt-everywhere-opensource-src-4.8.6 hss1394=1 mediafoundation=1 opus=0 build=%BUILD_TYPE% machine=%TARGET_MACHINE% toolchain=msvs virtualize=0 test=1 sqlitedll=0 mssdk_dir=%MSSDK_DIR% force32=1

This script will setup the build environment and call scons with the
appropriate flags. You have to edit the **WINLIB\_PATH** variable and
set it to the absolute path of the folder where you compiled the
dependencies for mixxx. Then type:

    build.bat

NOTE : if Mixxx compilation complains that libtag and chromaprint are
not available, apply the following workaround :
<http://sourceforge.net/p/mixxx/mailman/message/32981948/> Remove the
entire \<ItemGroup\> that contains the cmake invocations in tag.vcxproj
and chromaprint vcxproj and rebuild your build env

## Build 64bit version of Mixxx

You have to follow the above guide with two changes.

1.  Build the dependencies with: `build_environment x64 Release`
2.  Use **set ARCHITECTURE=amd64** and **force32=0** in **build.bat**

**WARNING**: DO NOT mix 32 and 64 bits build in the same CMD Shell
window or you will have undetermined results. If you need 32 and 64 bits
environments together, use different terminal window for 32 bits and 64
bits build\_environment and mixxx compilation

## Build debug version of Mixxx

You have to follow the above guide with two changes.

1.  Build the dependencies with: `build_environment xxx Debug`
2.  Use **set BUILD\_TYPE=debug** in **build.bat**
