*(If you're looking to make an installable release, [go to this
page](Build%20Windows%20installer).)*

# Building Mixxx on Windows

## Build 32bit version of Mixxx

### Programs to install

  - [Visual Studio 13 for Windows
    Desktop](http://www.visualstudio.com/downloads/download-visual-studio-vs).
    You need a Microsoft account.
  - [Microsoft Windows 7 (& .NET 3.5)
    SDK](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=c17ba869-9671-4330-a63e-1fd44e0e2505&displaylang=en)
  - Or the [Windows 7.1 (& .NET 4)
    SDK](http://go.microsoft.com/fwlink/?LinkID=191420) which is
    smaller, newer and includes the compilers (so you may not need
    Visual Studio above if you're just looking to build Mixxx from a
    command line.)
  - [Python](http://python.org/download/) 2.7.x Install for user only\!
    Otherwise scons can't find the installation
  - [SCONS 2.3.3](http://www.scons.org/download.php)
  - A Git client like
    [TortoiseGit](https://code.google.com/p/tortoisegit/) or the [github
    windows
    client](http://github-windows.s3.amazonaws.com/GitHubSetup.exe)
    (featuring a unix like command line)
  - [CMake 3.3.x](http://www.cmake.org/download) Install with the
    default options. The CMake directory does not need to be added to
    the PATH environment variable.

### Prepare build environment

Add to or create the following system environment variables
([HowTo](http://www.chem.gla.ac.uk/~louis/software/faq/q1.html),)
adjusting the paths to match where you actually installed the above.
`PATH = ;C:\Python27;C:\Python27\Scripts # append to the existing
variable
`

### Download mixxx dependencies

1.  Clone the [Mixxx
    buildserver](https://github.com/mixxxdj/buildserver/tree/windows_environment)
    repository. Remember the folder to which the repository was saved.
    We will refer to that folder as **WINLIB\_PATH** later.
2.  In the buildserver repository, checkout the **windows\_environment**
    branch
3.  Download the [Qt
    Sources](http://download.qt-project.org/official_releases/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.zip).
    Unpack the zip archive into **WINLIB\_PATH\\build**
4.  Download the [ASIO
    SDK](http://www.steinberg.net/en/company/developers.html). You will
    need a free steinberg development account to do that. Extract the
    files and rename the directory to remove the version number, so
    **ASIOSDK2.7** becomes **ASIOSDK**. Move **ASIOSDK** to
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
environments together, use diffrent windows for 32 bits and 64 bits
build\_environment and mixxx compilation

## Build debug version of Mixxx

You have to follow the above guide with two changes.

1.  Build the dependencies with: `build_environment xxx Debug`
2.  Use **set BUILD\_TYPE=debug** in **build.bat**
