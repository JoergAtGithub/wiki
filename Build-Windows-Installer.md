FIXME Mixxx is fading out SCons in favor of cmake starting in 2.3 and will completely switch in 2.4. This page isn't updated with the appropriate instructions yet.

# Making a Windows installer package

Mixxx uses the [WIX Toolset](http://wixtoolset.org/releases/) for
building Windows self-extracting installers. This page contains
information on making such packages.

First, we assume you've built & run Mixxx successfully from the
instructions on the [Compiling on Windows](Compiling-on-Windows.md)
page.

## Preparation

You first need to download and install [WIX
Toolset](http://wixtoolset.org/releases/) version 3.9+ and add it to
your %PATH%

When built with MSVC, Mixxx requires that certain MSVC DLL files be
present in order to run. Many people have these already installed on
their systems, but many do not (or have different versions,) so we must
include them with our packages.

To do that, you need to download the vcredist installation package and
install it at the root of your build env directory.

There's a different one for each architecture and compiler combination,
as shown below:

| Visual Studio \< 2015 | Not supported to build Mixxx                                                          |                                                         |
| --------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Visual Studio 2015    | [x86, amd64 and IA64](https://www.microsoft.com/en-us/download/details.aspx?id=53587) |                                                         |
| Visual Studio 2017    | [x86](https://aka.ms/vs/15/release/vc_redist.x86.exe)                                 | [amd64](https://aka.ms/vs/15/release/vc_redist.x64.exe) |

It is strongly recommended that you use Visual Studio 2015. If you
choose a different version, make sure the installers are named
`vc_redist.x86.exe` and `vc_redist.x64.exe`. Once you've located the
vcredist installer, if you're doing a 32-bit build, copy the x86
installer in the root of your build env. If a 64-bit build, copy the
x64/AMD64 installer.

## Make the package

  - Create a `makerelease.bat` file containing the following:

<!-- end list -->

    REM XP Compatibility requires the v7.1A SDK
    set MSSDK_DIR="c:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A"
    
    REM this can be either release or debug. For development you want to use debug
    set BUILD_TYPE=release
    
    REM This determines if you build a 32bit or 64bit version of mixxx. 
    REM 32bit = i386, 64bit = amd64
    set ARCHITECTURE=i386
    
    REM set this to the folder where you build the dependencies
    set WINLIB_PATH=D:\mixxx-buildserver32
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
    
    call "c:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" %VCVARS_ARCH%
    
    rem /MP Use all CPU cores.
    rem /FS force synchronous PDB writes (prevents PDB corruption with /MP)
    rem /EHsc Do not handle SEH in try / except blocks.
    rem /Zc:threadSafeInit- disable C++11 magic static support (Bug #1653368)
    set CL=/MP /FS /EHsc /Zc:threadSafeInit-
    
    set PATH=%BIN_DIR%;%PATH%
    scons.py mixxx makerelease toolchain=msvs winlib=%WINLIB_PATH% build=%BUILD_TYPE% staticlibs=1 staticqt=1 verbose=0 machine=%TARGET_MACHINE% qtdir=%QTDIR% hss1394=1 mediafoundation=1 opus=1 localecompare=1 optimize=portable virtualize=0 test=1 qt_sqlite_plugin=0 mssdk_dir="%MSSDK_DIR%" build_number_in_title_bar=0 bundle_pdbs=1

Note: If you want to build 64 bits package, set `ARCHITECTURE=amd64`
