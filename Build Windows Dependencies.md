# Building Mixxx's dependencies on Windows

We assume you've installed and configured Visual Studio Express and the
Microsoft Platform SDK as described in steps 1 & 2 [on this
page](compiling_on_windows), and if you want to build x64 versions with
the free Visual Studio Express, that you've done [this
hack](http://whitemarker.blogspot.com/2006/12/c-visual-c-2005-express-edition-x64.html).

## Qt

[Qt](http://qt.nokia.com/downloads/) now provides pre-built binaries for
32-bit Windows for the MSVC 2008 compiler (and the minGW one.) But if
you want to build it from source yourself for whatever reason (like for
x64,) here are the steps:

### Prepare build environment

``` 
  - If using Qt 4.5 & below, to avoid building the Qt examples and demos (you don't need them and it saves ALOT of time,) edit ''C:\qt-win-opensource-src-4.5.3\projects.pro'', remove "examples" and "demos" from QT_BUILD_PARTS toward the top of the file and save it. (In fact, you only need "libs" if you want to save even more time.)
  - Tweak the Qt configuration: (optional)
    - Edit ''C:\qt-everywhere-opensource-src-4.6.1\mkspecs\win32-msvc2008\qmake.conf'':
      - If you have more than one processor/core, add ''/MP'' to ''QMAKE_CFLAGS''.
      - Add -Ox to ''QMAKE_CFLAGS_RELEASE'' for extra optimizations
```

#### Linking with ASMLIB

If you want to link Qt against Agner Fog's optimized
[ASMLIB](http://agner.org/optimize/), do the following:

1.  Download the latest copy of the library from
    [here](http://agner.org/optimize/asmlib.zip)
2.  Unzip it to a directory of your choice, say `C:\asmlib`
3.  Edit
    qt-everywhere-opensource-src-4.6.1\\mkspecs\\win32-msvc2008\\qmake.conf:
    1.  Add `/Oi-` to `QMAKE_CFLAGS`
    2.  Add `/LIBPATH:"C:\asmlib"` to `QMAKE_LFLAGS`
    3.  Add `alibcof32o.lib` (or `alibcof64o.lib` for 64-bit) to each
        `QMAKE_LIBS` entry in front of other `.lib` files

### x64 prep

1.  Tweak the Qt configuration: (required)
    1.  Edit
        qt-everywhere-opensource-src-4.6.1\\mkspecs\\win32-msvc2008\\qmake.conf:
        1.  Add to `QMAKE_CFLAGS`: `/favor:AMD64` (or use `blend` or
            `EM64T` if appropriate), also add `/MP` if you have more
            than one processor/core
        2.  Add to `QMAKE_LFLAGS`: `/MACHINE:X64` (or `IA64`)
        3.  (optional) Add -Ox to `QMAKE_CFLAGS_RELEASE` for extra
            optimizations
    2.  Edit qt-everywhere-opensource-src-4.6.1\\qmake\\makefile.win32:
        1.  add to `CFLAGS`: `/favor:AMD64` (or use `blend` or `EM64T`
            if appropriate,) and -Ox for more optimizations if you want
        2.  add to `LFLAGS`: `/MACHINE:X64` (or `IA64`)

### Build

  - 32-bit: 

<!-- end list -->

``` 
    - Start the Visual Studio command prompt (Start->Microsoft C++ Visual Studio->Visual Studio Tools->Visual Studio Command Prompt)
    - Type ''setenv /xp /x86 /release'' and hit Enter. (The /x86 is for those on x64 OSs to make sure it targets 32-bit platforms.)
* 64-bit: 
    - Start the Visual Studio command prompt (Start->Microsoft Windows SDK->CMD Shell)
    - Type ''setenv /xp /x64 /release'' (or ''/ia64'') and hit Enter.
  - Type ''cd C:\qt-everywhere-opensource-src-4.6.1'' (or wherever you unpacked Qt) and hit Enter.
  - Type ''SET QT_BUILD_PARTS=LIBS'' (and add whatever other parts you want) and hit Enter.
  - Type ''configure -opensource -platform win32-msvc2008 -ltcg -plugin-sql-sqlite'' and press Enter.
  - When it finishes (about 5-10 minutes,) just type ''nmake'' and press Enter and you should be good (takes 1~3 hours.)
    * If you get ''<sdkdir>\winnt.h(1831) : error C2733: second C linkage of overloaded function '_interlockedbittestandset' not allowed'' then edit <sdkdir>\VC\INCLUDE\intrin.h and change the definition of ''_interlockedbittestandset'' and ''_interlockedbittestandreset'' to ''long volatile *''  Do ''nmake'' again and it should finish fine.
```

## libsndfile

[libsndfile](http://www.mega-nerd.com/libsndfile/) fortunately provides
binaries for Win32 and Win64, so all you need to do is:

1.  Download & run the appropriate installer
2.  Copy the following files into `mixxx-win32lib-msvc` or
    `mixxx-win64lib-msvc`:`libsndfile\libsndfile-1.dll
    libsndfile\libsndfile-1.lib (rename to sndfile.lib)
    `
3.  Copy the `.h` files from `libsndfile\include` to
    `mixxx-win[32|64]lib-msvc`

#### Troubleshooting

  - If you get a crapload of `sndfile.h` errors when Mixxx's
    `enginesidechain.cpp` is compiling, edit
    `mixxx-win[32|64]lib-msvc\sndfile.h` and change the line `typedef
    __int64_t sf_count_t ;` to: `typedef __int64 sf_count_t ;`

## PortAudio

[PortAudio](http://www.portaudio.com/download.html) provides MSVC
project files, which makes things nice. Just have the DirectX SDK
installed and open and build. (Step-by-step is given below.)

### x64 prep for VS Express

If you're doing an x64 build with VS Express, you'll first need to
change some things in the vcproj and sln file in a text editor before
you open them in VS:

1.  For the `portaudio\build\msvc\portaudio.sln` file:
    1.  Replace all instances of "Win32" (case-sensitive) with
        "DontWantThis" or something similar
    2.  Then replace all instances of "x64" with "Win32"
2.  For the `portaudio\build\msvc\portaudio.vcproj` file:
    1.  Change the line that says \<code=xml\> \<Configurations\>

<!-- end list -->

``` 
      <Configuration
          Name="Release|Win32"</code> to <code=xml>   <Configurations>
      <Configuration
          Name="Release|DontWantThis"</code>
  - Then change the similar ''Name="Release|x64"'' line to ''Name="Release|Win32"'' in the ''<Configuration'' below that one.
  - Don't worry about stuff below that since they all do the same thing regardless of the platform (at the time of writing (July 2009) at least.)
```

### Build

1.  Download and unpack the latest ASIO SDK (requires license
    agreement):
    <http://www.steinberg.net/en/company/3rd_party_developer.html>
2.  Follow the instructions in the file
    `portaudio\build\msvc\readme.txt` to prepare to build PA with ASIO
    support.
3.  Download and install the latest DirectX SDK:
    <http://msdn.microsoft.com/en-us/directx/aa937788.aspx>
4.  Start the platform SDK command prompt (Start?Microsoft Windows
    SDK?CMD Shell)
5.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
6.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
7.  Add the DirectX SDK paths to the compiler:
    1.  Go to Tools-\>Options-\>Projects and Solutions-\>VC++
        Directories
    2.  Choose "Include files" on the right and add the path to the
        DirectX SDK Include directory, e.g. `C:\Program Files\Microsoft
        DirectX SDK (March 2009)\Include`
    3.  Choose "Library files" on the right and add the path to the
        DirectX SDK Library directory, e.g. `C:\Program Files\Microsoft
        DirectX SDK (March 2009)\Lib\x86`
    4.  Click OK.
8.  Open the `portaudio\build\msvc\portaudio.vcproj` file via
    File-\>Open-\>Project/Solution. After doing the upgrade, you'll only
    see "Win32" targets if you're using VS Express. (If you've made the
    changes to the project files given above, building these will
    actually give you x64 versions. We had to do it this way otherwise
    VS Express would see the x64 targets in the file and refuse to make
    them available to you, since that's a premium feature of non-free
    versions of VS.)
9.  Choose the Release configuration and the Win32 platform
10. Press F7 to build
11. When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `portaudio\include\portaudio.h
    portaudio\build\msvc\Win32\Release\portaudio_x86.dll (or
    portaudio_x64.dll)
    portaudio\build\msvc\Win32\Release\portaudio_x86.lib (or
    portaudio_x64.lib. Rename either to portaudio.lib)
    `

## PortMidi

[PortMidi](http://portmedia.sourceforge.net/portmidi/) provides MSVC
project files, which makes things nice. Just open and build.
(Step-by-step is given below.)

### Build

1.  Start the platform SDK command prompt (Start?Microsoft Windows
    SDK?CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `portmidi\portmidi-VC9.vcproj` file via
    File-\>Open-\>Project/Solution. (If you're on VS 2005, use the
    `portmidi.vcproj` file.)
5.  Choose the Release\[ VC9\] configuration and the Win32 platform
6.  If building for x64
    1.  Go to Build-\>Configuration manager
    2.  Drop down Active Solution Platform and choose New...
    3.  Type x64 and choose copy settings from Win32. Click OK.
    4.  Choose Release on the left, x64 on the right and click Close.
7.  Press F7 to build (Ignore the failed builds since they're only
    tests. As long as two succeeded, (PortMidi and PortTime) you're
    fine.)
8.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `portmidi\pm_common\portmidi.h
    portmidi\pm_win\Release[ VC9]\portmidi.lib
    portmidi\porttime\porttime.h
    portmidi\porttime\Release[ VC9]\porttime.lib
    `

## libogg

[Xiph.org](http://www.xiph.org/downloads/) provides MSVC project files,
which makes things nice. Just open and build. (Step-by-step is given
below.)

### x64 prep for VS Express

If you're doing an x64 build with VS Express, you'll first need to
change some things in the vcproj and sln files in a text editor before
you open them in VS:

1.  Replace all instances of "Win32" (case-sensitive) with
    "DontWantThis" or something similar
2.  Then replace all instances of "x64" with "Win32"

Do this to all of the following files:
`libogg-1.1.4\win32\VS2008\libogg_dynamic.sln
libogg-1.1.4\win32\VS2008\libogg_dynamic.vcproj
libogg-1.1.4\win32\VS2008\libogg_static.sln
libogg-1.1.4\win32\VS2008\libogg_static.vcproj
`

### Build

1.  Start the platform SDK command prompt (Start?Microsoft Windows
    SDK?CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `libogg-1.1.4\win32\VS2008\libogg_dynamic.vcproj` file via
    File-\>Open-\>Project/Solution. You'll only see "Win32" targets if
    you're using VS Express. (If you've made the changes to the project
    files given above, building these will actually give you x64
    versions. We had to do it this way otherwise VS Express would see
    the x64 targets in the file and refuse to make them available to
    you, since that's a premium feature of non-free versions of VS.)
5.  Choose the Release\_SSE2 configuration and the Win32 platform
6.  Press F7 to build
7.  Open the `libogg-1.1.4\win32\VS2008\libogg_static.vcproj` file
8.  Choose the Release\_SSE2 configuration and the Win32 platform
9.  Press F7 to build
10. When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `libogg-1.1.4\win32\VS2008\Win32\Release_SSE2\libogg.dll
    libogg-1.1.4\win32\VS2008\Win32\Release_SSE2\libogg.lib (rename to
    ogg.lib)
    libogg-1.1.4\win32\VS2008\Win32\Release_SSE2\libogg_static.lib
    (rename to ogg_static.lib)
    `
11. Copy the `.h` files from `libogg-1.1.4\include\ogg` into
    `mixxx-win[32|64]lib-msvc\ogg`

## libvorbis

[Xiph.org](http://www.xiph.org/downloads/) provides MSVC project files,
which makes things nice. Just open and build. (Step-by-step is given
below.) Libvorbis depends on libogg, so build that first.

### x64 prep for VS Express

If you're doing an x64 build with VS Express, you'll first need to
change some things in the vcproj and sln files in a text editor before
you open them in VS:

1.  Replace all instances of "Win32" (case-sensitive) with
    "DontWantThis" or something similar
2.  Then replace all instances of "x64" with "Win32"

Do this to all of the following files:
`libvorbis-1.2.3\win32\VS2008\vorbis_dynamic.sln
libvorbis-1.2.3\win32\VS2008\libvorbis\libvorbis_dynamic.vcproj
libvorbis-1.2.3\win32\VS2008\libvorbisfile\libvorbisfile_dynamic.vcproj
libvorbis-1.2.3\win32\VS2008\vorbis_static.sln
libvorbis-1.2.3\win32\VS2008\libvorbis\libvorbis_static.vcproj
libvorbis-1.2.3\win32\VS2008\libvorbisfile\libvorbisfile_static.vcproj
`

### Build

1.  Edit `libvorbis-1.2.3\win32\VS2008\libogg.vsprops` and make sure the
    LIBOGG\_VERSION at the bottom matches the version of libogg you
    built above.
2.  Start the platform SDK command prompt (Start?Microsoft Windows
    SDK?CMD Shell)
3.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
4.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
5.  Open the `libvorbis-1.2.3\win32\VS2008\vorbis_dynamic.sln` file via
    File-\>Open-\>Project/Solution. You'll only see "Win32" targets if
    you're using VS Express. (If you've made the changes to the project
    files given above, building these will actually give you x64
    versions. We had to do it this way otherwise VS Express would see
    the x64 targets in the file and refuse to make them available to
    you, since that's a premium feature of non-free versions of VS.)
6.  Choose the Release\_SSE2 configuration and the Win32 platform
7.  Press F7 to build. (If building for x64, ignore the errors on
    vorbisenc and vorbisdec since we don't need them.)
8.  Open the `libvorbis-1.2.3\win32\VS2008\libvorbis_static.vcproj` file
9.  Choose the Release\_SSE2 configuration and the Win32 platform
10. Press F7 to build
11. When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbis.dll
    libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbis.lib
    (rename to vorbis.lib)
    libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbisfile.lib
    (rename to vorbisfile.lib)
    libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbis_static.lib
    (rename to vorbis_static.lib)
    libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbisfile_static.lib
    (rename to vorbisfile_static.lib)
    `
12. Copy the `libvorbis-1.2.3\include\vorbis` folder from into
    `mixxx-win[32|64]lib-msvc`. You can delete the Makefiles inside, as
    we just need the .h files.

#### Troubleshooting

  - If you get the error `vorbis.def : error LNK2001: unresolved
    external symbol _analysis_output_always` comment the line
    `_analysis_output_always` in `libvorbis-1.2.3\win32\vorbis.def`
    (line 51 in my copy.) Press F7 again and it should build fine.

## libmad

[MAD](http://www.underbit.com/products/mad/) provides MSVC project
files, which makes things nice. Just open and build. (Step-by-step is
given below.)

### Build

1.  Start the platform SDK command prompt (Start?Microsoft Windows
    SDK?CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `libmad-0.15.1b\msvc++\libmad.dsp` file via
    File-\>Open-\>Project/Solution.
5.  Answer 'Yes' to convert & open the project
6.  Choose the Release configuration and the Win32 platform
7.  If building for x64
    1.  Go to Build-\>Configuration manager
    2.  Drop down Active Solution Platform and choose New...
    3.  Type x64 and choose copy settings from Win32. Click OK.
    4.  Choose Release on the left, x64 on the right and click Close.
8.  Press F7 to build. (You can cancel the .sln save dialog if you want
    and it will still build.)
9.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `libmad-0.15.1b\mad.h
    libmad-0.15.1b\msvc++\Release\libmad.lib
    `

## libid3tag

[MAD](http://www.underbit.com/products/mad/) provides MSVC project
files, which makes things nice. Just open and build. (Step-by-step is
given below.)

LibID3Tag needs [ZLib](http://www.zlib.net/) headers, so we have to get
them too (detailed below.)

### Build

1.  Download & unpack the latest [zlib
    source](http://www.winimage.com/zLibDll/)
2.  Start the platform SDK command prompt (Start?Microsoft Windows
    SDK?CMD Shell)
3.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
4.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
5.  Open the `libid3tag-0.15.1b\msvc++\libid3tag.dsp` file via
    File-\>Open-\>Project/Solution.
6.  Answer 'Yes' to convert & open the project
7.  Choose the Release configuration and the Win32 platform
8.  Add the ZLib paths to the compiler:
    1.  Go to Tools-\>Options-\>Projects and Solutions-\>VC++
        Directories
    2.  Choose "Include files" on the right and add the path to the
        directory into which you unpacked the ZLib source, e.g.
        `c:\temp\zlib123`
    3.  Click OK.
9.  If building for x64
    1.  Go to Build-\>Configuration manager
    2.  Drop down Active Solution Platform and choose New...
    3.  Type x64 and choose copy settings from Win32. Click OK.
    4.  Choose Release on the left, x64 on the right and click Close.
10. Press F7 to build. (You can cancel the .sln save dialog if you want
    and it will still build.)
11. When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `libid3tag-0.15.1b\id3tag.h
    libid3tag-0.15.1b\msvc++\Release\libid3tag.lib (rename to
    id3tag.lib)
    `

## libfaad2

[FAAD2](http://www.audiocoding.com/faad2.html) provides MSVC project
files, which makes things nice. Just open and build. (Step-by-step is
given below.)

**This is currently unable to build on x64 due to embedded assembly
code.** The MSVC x64 compiler only supports intrinsics for assembly.

### Build

1.  Edit the `faad2-2.7\libfaad\libfaad2.def` file and add the following
    lines to the bottom: `NeAACDecPostSeekReset @10
    NeAACDecDecode2 @11`
2.  Start the platform SDK command prompt (Start?Microsoft Windows
    SDK?CMD Shell)
3.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
4.  Run the Visual Studio GUI from this command line, specifying the
    `/useenv` switch to have it use the Platform SDK compile tools, libs
    and includes. (e.g. `C:\Program Files (x86)\Microsoft Visual
    Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
5.  Open the `faad2-2.7\libfaad\libfaad2_dll.vcproj` file via
    File-\>Open-\>Project/Solution.
6.  Answer 'Yes' to convert & open the project
7.  Choose the Release configuration and the Win32 platform
8.  Add the FAAD path to the compiler:
    1.  Right-click the `libfaad2_dll` project and go to Properties
    2.  Go to Configuration Properites-\>C/C++-\>General
    3.  Choose "Additional Include Directories" on the right and add
        FAAD's 'include' directory, e.g. `c:\temp\faad2-2.7\include`
    4.  Click OK.
9.  Press F7 to build. (You can cancel the .sln save dialog if you want
    and it will still build.)
10. When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `faad2-2.7\libfaad\include\faad.h
    faad2-2.7\libfaad\include\neaacdec.h
    faad2-2.7\libfaad\include\libfaad\ReleaseDLL\libfaad2.dll
    faad2-2.7\libfaad\include\libfaad\ReleaseDLL\libfaad2.lib (rename to
    libfaad.lib)
    `

## libmp4v2

[MP4V2](http://code.google.com/p/mp4v2/) provides MSVC solution files,
which makes things nice. Just open and build. (Step-by-step is given
below.)

### Build

1.  Start the platform SDK command prompt (Start?Microsoft Windows
    SDK?CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `mp4v2-1.9.1\vstudio9.0\libmp4v2\libmp4v2.vcproj` file via
    File-\>Open-\>Project/Solution.
5.  Choose the Release configuration and the Win32 platform
6.  If building for x64
    1.  Go to Build-\>Configuration manager
    2.  Drop down Active Solution Platform and choose New...
    3.  Type x64 and choose copy settings from Win32. Click OK.
    4.  Choose Release on the left, x64 on the right and click Close.
7.  Tune the project settings to your liking
    1.  Right-click the libmp4v2 project and click Properties.
    2.  Under Configuration Properties, Linker, Debugging, set Generate
        Debug Info to No.
8.  Right click `libmp4v2` and click Build.
9.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `mp4v2-1.9.1\vstudio9.0\Release\libmp4v2.dll
    mp4v2-1.9.1\vstudio9.0\Release\libmp4v2.lib
    mp4v2-1.9.1\include\mp4v2 (the whole directory)`

# Optimizations

Mixxx can benefit from various code optimizations. If you right-click
each MSVC project and click Properties, you can set many optimization
options. You can do any or all of the following:

  - Configuration Properties-\>C/C++-\>Optimization
  - Optimization: Full Optimization (/Ox)
  - Favor Size or Speed: Favor Fast Code (/Ot) (unless building for
    memory-constrained systems)
  - Whole Program Optimization: Enable link-time code generation (/GL)
  - Configuration Properties-\>C/C++-\>Code Generation
  - Enable Enhanced Instruction Set: Streaming SIMD Extensions
    (/arch:SSE) or Streaming SIMD Extensions 2 (/arch:SSE2) if your CPU
    supports either

## Linking with ASMLIB

If you want to link any of the VC++ projects against Agner Fog's
optimized [ASMLIB](http://agner.org/optimize/), do the following:

1.  Download the latest copy of the library from
    [here](http://agner.org/optimize/asmlib.zip)
2.  Unzip it to a directory of your choice, say `C:\asmlib`
3.  Once you've started the VC++ IDE, Go to Tools-\>Options-\>Projects
    and Solutions-\>VC++ Directories
    1.  Choose "Include files" on the right and add the path to the
        ASMLIB directory you set above, e.g. `C:\asmlib`
    2.  Choose "Library files" on the right and add the path to the
        ASMLIB directory you set above, e.g. `C:\asmlib`
    3.  Click OK.
4.  After opening the project/solution file, right-click each project,
    Choose Properties and do:
    1.  Configuration Properties-\>C/C++-\>Optimization: Set Enable
        Intrinsic Functions to **No**.
    2.  Configuration Properties-\>C/C++-\>Command Line: Add `/Oi-` to
        Additional Options.
    3.  Configuration Properties-\>Linker-\>Input: Add `alibcof64o.lib`
        (or `alibcof32o.lib` for 32-bit) to "Additional Dependencies"
