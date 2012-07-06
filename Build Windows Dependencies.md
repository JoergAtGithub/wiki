# Building Mixxx's dependencies on Windows

We assume you've installed and configured Visual Studio Express and the
Microsoft Platform/Windows SDK as described in steps 1 & 2 [on this
page](compiling_on_windows), and if you want to build x64 versions with
the free Visual Studio Express 2008, that you've done [this
hack](http://jenshuebel.wordpress.com/2009/02/12/visual-c-2008-express-edition-and-64-bit-targets/)
(or [this
one](http://whitemarker.blogspot.com/2006/12/c-visual-c-2005-express-edition-x64.html)
if you're using VS 2005.) VS 2010 Express supports x64 projects out of
the box (but it uses alot more resources than earlier versions due at
least in part to its (needless) dependence on .NET 4.)

## Qt

[Qt](http://qt.nokia.com/downloads/) now provides pre-built binaries for
32-bit Windows for the MSVC 2008 compiler (and the minGW one.) But if
you want to build it from source yourself for whatever reason (like for
x64,) here are the steps:

### Prepare build environment

``` 
  - Tweak the Qt configuration:
    - **Full-text search:** Edit ''C:\qt-everywhere-opensource-src-4.6.1\src\plugins\sqldrivers\sqlite\sqlite.pro''
      - Add this, after the first DEFINES += :<code>DEFINES += SQLITE_ENABLE_FTS3 SQLITE_ENABLE_FTS3_PARENTHESIS</code>
    - **Speed** (optional): Edit ''C:\qt-everywhere-opensource-src-4.6.1\mkspecs\win32-msvc2008\qmake.conf'':
      - If you have more than one processor/core, add ''/MP'' to ''QMAKE_CFLAGS''.
      - Add ''-Ox'' to ''QMAKE_CFLAGS_RELEASE'' for "full optimization" (Though ''-O2'' is preferred.)
      - Add ''/arch:SSE'' to ''QMAKE_CFLAGS_RELEASE'' for SSE support (use SSE2 if your CPU supports it)
      - Change ''QMAKE_LFLAGS_LTCG'' to ''/LTCG:STATUS'' so it tells you how long it will take to generate each executable (Some of them take a loooong time (WebKit and QtScript) so it's nice to know.)
      - You can do the same in ''C:\qt-everywhere-opensource-src-4.6.1\qmake\makefile.win32'' but **don't** add ''-GL'' to CFLAGS on x86 or qmake won't work. Otherwise, you can add any options suitable for your particular system since qmake is just going to run there. (e.g. /arch:SSE2)
    - **Static libraries** (no msvcrtXX.dll dependence, optional): Edit ''C:\qt-everywhere-opensource-src-4.6.1\mkspecs\win32-msvc2008\qmake.conf'':
      - Change the ''QMAKE_CFLAGS_RELEASE'' from ''-MD'' to ''-MT''
      - Add ''/NODEFAULTLIB:"MSVCRT"'' to ''QMAKE_LFLAGS_RELEASE''.
```

#### Linking with ASMLIB

If you want to link Qt against Agner Fog's optimized
[ASMLIB](http://agner.org/optimize/), do the following:

1.  Download the latest copy of the library from
    [here](http://agner.org/optimize/asmlib.zip)
2.  Unzip it to a directory of your choice, say `C:\asmlib`
3.  Edit
    qt-everywhere-opensource-src-4.6.1\\mkspecs\\win32-msvc2005\\qmake.conf:
    1.  Add `-Oi-` to `QMAKE_CFLAGS`
    2.  Add `/LIBPATH:"C:\\asmlib"` to `QMAKE_LFLAGS`
    3.  Add `alibcof32o.lib` (or `alibcof64o.lib` for 64-bit) to
        `QMAKE_LFLAGS` (this ensures it's linked into every module)

### x64 prep (optional)

1.  Tweak the Qt configuration:
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
  - Type ''configure -opensource -platform win32-msvc2005 -qt-sql-sqlite'' and press Enter.
    - For more optimized code, also add ''-ltcg''.
    - To configure faster, also add ''-fast -no-vcproj -no-dsp''.
  - When it finishes (about 5-10 minutes,) just type ''nmake'' and press Enter and you should be good (takes 1~3 hours.)
    * If you get ''<sdkdir>\winnt.h(1831) : error C2733: second C linkage of overloaded function '_interlockedbittestandset' not allowed'' then edit <sdkdir>\VC\INCLUDE\intrin.h and change the definition of ''_interlockedbittestandset'' and ''_interlockedbittestandreset'' to ''long **volatile** *'' like so:<code>__MACHINEI(unsigned char _interlockedbittestandset(long volatile *a, long b))
```

\_\_MACHINEI(unsigned char \_interlockedbittestandreset(long volatile
\*a, long b))\</code\> Do `nmake` again and it should finish fine.

``` 
    * If on x64 and you get the similar ''<sdkdir>\winnt.h(1831) : error C2733: second C linkage of overloaded function '_interlockedbittestandset64' not allowed'' then edit <sdkdir>\VC\INCLUDE\intrin.h and change the definition of ''_interlockedbittestandset64'' and ''_interlockedbittestandreset64'' to to ''_ _int64 **volatile** *'' like so:<code>__MACHINEX64(unsigned char _interlockedbittestandset64(__int64 volatile *a, __int64 b))
```

<span class="underline">MACHINEX64(unsigned char
\_interlockedbittestandreset64(</span>int64 volatile \*a, \_\_int64
b))\</code\> Do `nmake` again and it should finish fine.

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

### VS 2005 x64 hacks

[Follow these instructions](#x64-prep-for-vs-express-2005) for the
following files:

    portaudio\build\msvc\portaudio.sln
    portaudio\build\msvc\portaudio.vcproj

### Build

1.  Download and unpack the latest [ASIO
    SDK](http://www.steinberg.net/nc/en/company/developer/sdk_download_portal/asio_sdk.html)
    (requires login and license agreement)
2.  Follow the instructions in the files
    `portaudio\build\msvc\readme.txt` and
    `portaudio\src\hostapi\asio\ASIO-README.txt` to prepare to build PA
    with ASIO support.
3.  Download and install the latest DirectX SDK:
    <http://msdn.microsoft.com/en-us/directx/aa937788.aspx>
4.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
5.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
6.  Run `dx_setenv.cmd`, the DirectX SDK environment variable setup
    script here to add the DirectX paths. (e.g. `C:\Program
    Files\Microsoft DirectX SDK
    (March 2009)\Utilities\Bin\dx_setenv.cmd`)
7.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files\Microsoft Visual
    Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
8.  Open the `portaudio\build\msvc\portaudio.vcproj` file via
    File-\>Open-\>Project/Solution. After doing the upgrade, you'll only
    see "Win32" targets if you're using VS Express. (If you've made the
    changes to the project files given above, building these will
    actually give you x64 versions. We had to do it this way otherwise
    VS Express would see the x64 targets in the file and refuse to make
    them available to you, since that's a premium feature of non-free
    versions of VS.)
9.  Choose the Release configuration and the Win32 platform
10. Right-click the `portaudio` project and click Properties
11. Navigate to Configuration Properties-\>C/C++-\>Preprocessor, then
    under Preprocessor Definitions, change **`PA_USE_ASIO=1`** and
    **`PA_USE_DS=1`**
12. Press F7 to build
13. When it finishes, copy the following files into
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

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `portmidi\ALL_BUILD.vcproj` file via
    File-\>Open-\>Project/Solution.
5.  Choose the Release configuration and the Win32 platform
6.  If building for x64
    1.  Edit the portmidi-dynamic and portmidi-static projects and
        change Linker-\>Advanced-\>Target Machine to `/MACHINE:X64`
7.  Right-click portmidi-dynamic and click Build
8.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `portmidi\pm_common\portmidi.h
    portmidi\Release\portmidi.lib
    portmidi\Release\portmidi.dll
    `

## PortTime

[PortMidi](http://portmedia.sourceforge.net/portmidi/) provides MSVC
project files, which makes things nice. Just open and build.
(Step-by-step is given below.)

### Build

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `portmidi\porttime\porttime.vcproj` file via
    File-\>Open-\>Project/Solution. (If on VS2005, use the
    `porttime-VC8.vcproj` file.)
5.  Choose the Release configuration and the Win32 platform
6.  Press F7 to build

<!-- end list -->

  - If you get `portmidi\porttime\porttime.h(20) : fatal error C1083:
    Cannot open include file: 'stdint.h': No such file or directory`
    then edit the project properties and add `mixxx-win32lib-msvc` (or
    64) to Additional Include Directories

<!-- end list -->

1.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `portmidi\porttime\porttime.h
    portmidi\porttime\Release\porttime.lib
    `

## libogg

[Xiph.org](http://www.xiph.org/downloads/) provides MSVC project files,
which makes things nice. Just open and build. (Step-by-step is given
below.)

### VS 2005 x64 hacks

[Follow these instructions](#x64-prep-for-vs-express-2005) for the
following files:

    libogg-1.1.4\win32\VS2008\libogg_dynamic.sln
    libogg-1.1.4\win32\VS2008\libogg_dynamic.vcproj

### Build

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
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
5.  Choose the Release configuration and the Win32 platform
6.  Press F7 to build
7.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `libogg-1.1.4\win32\VS2008\Win32\Release_SSE2\libogg.dll
    libogg-1.1.4\win32\VS2008\Win32\Release_SSE2\libogg.lib (rename to
    ogg.lib)
    `
8.  Copy the `.h` files from `libogg-1.1.4\include\ogg` into
    `mixxx-win[32|64]lib-msvc\ogg`

## libvorbis

[Xiph.org](http://www.xiph.org/downloads/) provides MSVC project files,
which makes things nice. Just open and build. (Step-by-step is given
below.) Libvorbis depends on libogg, so build that first.

### VS 2005 x64 hacks

[Follow these instructions](#x64-prep-for-vs-express-2005) for the
following files:

    libvorbis-1.2.3\win32\VS2008\vorbis_dynamic.sln
    libvorbis-1.2.3\win32\VS2008\libvorbis\libvorbis_dynamic.vcproj
    libvorbis-1.2.3\win32\VS2008\libvorbisfile\libvorbisfile_dynamic.vcproj

### Build

1.  Edit `libvorbis-1.2.3\win32\VS2008\libogg.vsprops` and make sure the
    LIBOGG\_VERSION at the bottom matches the version of libogg you
    built above.
2.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
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
7.  Right-click `libvorbis` and click Build
8.  Right-click `libvorbisfile` and click Build
9.  When finished, copy the following files into `mixxx-win32lib-msvc`
    or `mixxx-win64lib-msvc`:
    `libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbis.dll
    libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbis.lib
    libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbisfile.dll
    libvorbis-1.2.3\win32\VS2008\Win32\Release_SSE2\libvorbisfile.lib
    `
10. Copy the `libvorbis-1.2.3\include\vorbis` folder from into
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

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
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
    1.  Right-click `libmad` and click Properties
    2.  Go to Configuration Properties-\>C/C++-\>Preprocessor and under
        Preprocessor Definitions, change `FPM_INTEL` to `FPM_64BIT`
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
2.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
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
    1.  Right-click `libid3tag` and click Properties
    2.  Go to Configuration Properties-\>C/C++-\>General and under
        Additional Include Directories, add the path to the directory
        into which you unpacked the ZLib source, e.g. `c:\temp\zlib123`
    3.  Click OK.
9.  Press F7 to build. (You can cancel the .sln save dialog if you want
    and it will still build.)
10. When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `libid3tag-0.15.1b\id3tag.h
    libid3tag-0.15.1b\msvc++\Release\libid3tag.lib (rename to
    id3tag.lib)
    `

#### Troubleshooting

  - If you get the error `..\file.c(33) : fatal error C1083: Cannot open
    include file: 'unistd.h': No such file or directory` then edit the
    file `libid3tag-0.15.1b-patched\file.c` and change the line `#
    include "config.h"`to`# include "msvc++/config.h"` Save that and
    press F7 to rebuild.

## libfaad2

[FAAD2](http://www.audiocoding.com/faad2.html) provides MSVC project
files, which makes things nice. Just open and build. (Step-by-step is
given below.)

### x64 prep

1.  Edit `faad2-2.7\libfaad\common.h`:
    1.  Delete line 315, `#if defined(_WIN32) && !defined(__MINGW32__)`
        and replace it with \<code\> \#if defined(\_WIN64) &&
        \!defined(<span class="underline">MINGW64</span>)

<!-- end list -->

``` 
  // No LRINTF until someone writes an .asm file
#elif defined(_WIN32) && !defined(__MINGW32__)</code>
  - Save the file.
```

### Build

1.  Edit the `faad2-2.7\libfaad\libfaad2.def` file and add the following
    lines to the bottom: `NeAACDecPostSeekReset @10
    NeAACDecDecode2 @11`
2.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
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

<!-- end list -->

  - If you get `faad2-2.7\libfaad\common.h(42) : fatal error C1083:
    Cannot open include file: 'neaacdec.h': No such file or directory`
    then under project Configuration properties-\>C/C++-\>General:

<!-- end list -->

``` 
    * Add to Additional Include Directories: ''..\include'' 
- When it finishes, copy the following files into ''mixxx-win32lib-msvc'' or ''mixxx-win64lib-msvc'': <code>faad2-2.7\libfaad\include\faad.h
```

faad2-2.7\\libfaad\\include\\neaacdec.h
faad2-2.7\\libfaad\\include\\libfaad\\ReleaseDLL\\libfaad2.dll
faad2-2.7\\libfaad\\include\\libfaad\\ReleaseDLL\\libfaad2.lib (rename
to libfaad.lib) \</code\>

## libmp4v2

[MP4V2](http://code.google.com/p/mp4v2/) provides MSVC solution files,
which makes things nice. Just open and build. (Step-by-step is given
below.)

### Build

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
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

## libFLAC

[libFLAC](http://flac.sourceforge.net/) provides MSVC solution files,
which makes things nice.

### Dependencies

libFLAC requires [The Netwide Assembler](http://www.nasm.us/) to build.

1.  [Download the ZIP file from
    here](http://www.nasm.us/pub/nasm/releasebuilds/2.09.03/win32/) and
    extract it.
2.  Rename/copy the file `nasm.exe` to `nasmw.exe` since that's what the
    FLAC sources look for

### Preparation

1.  Build libOGG ([see above](#libogg))
2.  [Download](http://sourceforge.net/projects/flac/files/flac-src/) the
    FLAC source and extract it.

**Note:** For x64 as of FLAC v1.2.1, we have been unable to get it to
build. It gives the following errors:`bitreader_asm.obj : error LNK2001:
unresolved external symbol _FLAC__crc16_table
bitreader_asm.obj : error LNK2001: unresolved external symbol
_bitreader_read_from_client_` The only solution currently found is to
download the [OpenCodecs
source](http://downloads.xiph.org/releases/oggdsf/opencodecs_0.85.17777_src.7z)
and use the
`opencodecs\src\lib\codecs\flac\libs\libflac\src\libFLAC\libFLAC_dynamic.vcproj`
as-is and skip the rest of this section.

1.  Copy `libogg-1.1.4\win32\VS2008\Win32\Release_SSE\libogg_static.lib`
    to `flac-1.2.1\obj\release\lib` and rename it to `ogg_static.lib`
2.  **For x64:**
    1.  For each of the following files, search & replace all instances
        of `-f win32` with `-f win64`:
        `flac-1.2.1\src\libFLAC\libflac_dynamic.dsp
        flac-1.2.1\src\libFLAC\libflac_dynamic.vcproj
        flac-1.2.1\src\libFLAC\libflac_static.dsp
        flac-1.2.1\src\libFLAC\libflac_static.vcproj`
    2.  Apply the following patch to
        `flac-1.2.1\src\libFLAC\bitreader.c`:`---
        flac-1.2.1-original\src\libFLAC\bitreader.c Tue
        Sep 11 06:48:56 2007
        +++ flac-1.2.1\src\libFLAC\bitreader.c Tue May 20 12:30:08 2008
        @@ -149,15 +149,37 @@
                                        FLAC__CPUInfo cpu_info;
                };
                
        -#ifdef _MSC_VER
        -/* OPT: an MSVC built-in would be better */
        +
        +/* local_swap32_() */
        +/* Swaps the byte order of a 32 bits integer, converting
        between big-endian and little-endian */
        +#if defined(_MSC_VER)
        +
        +#include <stdlib.h> // Contains _byteswap_ulong() for MSVC
        according to MSDN
                static _inline FLAC__uint32 local_swap32_(FLAC__uint32 x)
                {
        + /* This is an intrinsic and will expanded to minimal asm by
        the compiler */
        + return _byteswap_ulong(x);
        +}
        +
        +#else /* defined(_MSC_VER) */
        +
        +static _inline FLAC__uint32 local_swap32_(FLAC__uint32 x)
        +{
        + /* Manual version, a bit slower but works everywhere */
                                        x = ((x<<8)&0xFF00FF00) | ((x>>8)&0x00FF00FF);
                                        return (x>>16) | (x<<16);
                }
        +
        +#endif /* defined(_MSC_VER) */
        +
        +
        +/* local_swap32_block_() */
        +/* Swaps the byte order of an array of 32 bits integers */
        +#if defined(_MSC_VER) && !defined(FLAC__NO_ASM) ||
        !defined(_M_X64)
        +
                static void local_swap32_block_(FLAC__uint32 *start,
        FLAC__uint32 len)
                {
        + /* MSVC specific 32 bit asm version */
                                        __asm {
                                                                        mov edx, start
                                                                        mov ecx, len
        @@ -173,7 +195,22 @@
                done1:
                                        }
                }
        -#endif
        +
        +#else /* defined(_MSC_VER) && !defined(FLAC__NO_ASM) ||
        !defined(_M_X64) */
        +
        +static void local_swap32_block_(FLAC__uint32 *start,
        FLAC__uint32 len)
        +{
        + /* MSVC specific intrinsic version */
        + while(len > 0)
        + {
        + *start = local_swap32_(*start);
        + ++start;
        + --len;
        + }
        +}
        +
        +#endif /* defined(_MSC_VER) && !defined(FLAC__NO_ASM) ||
        !defined(_M_X64) */
        +
                
                static FLaC__INLINE void crc16_update_word_(FLAC__BitReader *br,
        brword word)
                {
        
        `
3.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
4.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
5.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
6.  Add paths to the environment:
    1.  Go to Tools-\>Options-\>Projects and Solutions-\>VC++
        Directories
    2.  Choose "Executable files" on the right and add the path to the
        NASM directory you extracted to above, e.g. `C:\nasm-2.09.03`
    3.  Choose "Include files" on the right and add the path to the
        libOGG include directory, e.g. `C:\libogg-1.1.4\include`
7.  Open the `flac-1.2.1\FLAC.sln` file and agree to upgrade if asked
8.  Rename the `libFLAC_dynamic` project to just `libFLAC`
9.  Choose the Release configuration and the Win32 platform
10. If building for x64, for both the `libFLAC_dynamic` and
    `libFLAC_static` projects:
    1.  Right-click it and choose Properties...
    2.  Go to Configuration Properties-\>C/C++-\>Preprocessor and enter
        `FLAC__NO_ASM;` at the front of the Preprocessor Definitions
        list
    3.  For the dynamic one only, go to Configuration
        Properties-\>Linker-\>Advanced and choose `/MACHINE:X64` for
        Target Machine
    4.  For the dynamic one only, go to Configuration
        Properties-\>Linker-\>Debugging and ensure Generate Debug Info
        is set to `No`

### Build

1.  Right click `libFLAC_dynamic` and click Build.
2.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `flac-1.2.1\obj\release\lib\libFLAC.lib
    flac-1.2.1\obj\release\lib\libFLAC.dll
    flac-1.2.1\include\FLAC (the whole directory)`

## libHSS1394

[Stanton](http://www.stantondj.com)'s
[HSS1394](https://launchpad.net/hss1394) provides MSVC solution files
(that we've updated) which makes things nice.

### Build

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `HSS1394\code\builds\win32\libHSS1394_dll_VC90.vcproj` file
    via File-\>Open-\>Project/Solution.
5.  Choose the Release configuration and the Win32 platform
6.  If building for x64, 
    1.  Right-click the libHSS1394 project and click Properties.
    2.  Under Configuration Properties-\>C/C++-\>Preprocessor, for
        Preprocessor Definitions, add `;_WIN64_`
7.  Tune the project settings
    1.  Right-click the libHSS1394 project and click Properties.
    2.  Under Configuration Properties-\>Linker-\>General, set Output
        File to `$(OutDir)\HSS1394.dll`
    3.  Under Configuration Properties-\>Linker-\>Advanced, set Import
        Library to `$(OutDir)\HSS1394.lib`
8.  Right click `libHSS1394` and click Build.
9.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `HSS1394\lib\HSS1394.lib
    HSS1394\lib\HSS1394.dll
    HSS1394\inc (the whole directory, and rename it to HSS1394)`
10. Edit the `mixxx-win[32|64]lib-msvc\HSS1394\HSS1394Types.h` source
    file and change line 65 to:\<code\> \#ifdef
    <span class="underline">WINDOWS</span>\</code\>
11. Save the file

## libshout

[Libshout](http://downloads.us.xiph.org/releases/libshout/) is a library
for live audio broadcasting over the Internet. It is developed by the
[icecast.org](http://www.icecast.org/) project.

### Dependencies

libshout requires libogg, libvorbis, and PThreads.

You must have first built [libogg](#libogg) and [libvorbis](#libvorbis)
(see above.)

#### Download/build PThreads

libshout requires [POSIX threads for
Windows](http://sourceware.org/pthreads-win32/). It's a piece of cake to
build:

1.  [Download the source tree](ftp://sourceware.org/pub/pthreads-win32/)
    (look for files named like `pthreads-w32-2-8-0-release.tar.gz` and
    pick the latest one.)
2.  Unpack the directory to the same folder you unpacked libshout's (so
    that the `pthreads` and `libshout` folders are at the same level)
3.  For x64,
    1.  Edit the file `pthread_cancel.c`
    2.  Change line 195 to `ptw32_register_cancelation
        ((PAPCFUNC)ptw32_cancel_callback, threadH, 0);`
4.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
5.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
6.  `cd` to the directory you unpacked it to
7.  Type `nmake clean VC` and hit Enter.
8.  When it finishes, type `mt.exe -manifest pthreadVC2.dll.manifest
    -outputresource:pthreadVC2.dll;2` and hit Enter.
9.  Copy the following file into `mixxx-win32lib-msvc` or
    `mixxx-win64lib-msvc`: `pthreads\pthreadVC2.dll`

### Preparation

1.  [Download the Icecast server source](http://www.icecast.org/)
2.  Extract the file `icecast-2.3.2\src\compat.h` to
    `libshout-2.3.1\include`
3.  Rename/copy `libshout-2.2.2\include\shout\shout.h.in` to `shout.h`
4.  Copy `libshout-2.2.2\include\shout\shout.h` to
    `mixxx-win[32|64]lib-msvc\shout`
5.  Copy `libshout-2.2.2\include\os.h` to
    `mixxx-win[32|64]lib-msvc\shout`
6.  Edit `mixxx-win[32|64]lib-msvc\shout\shout.h`:
    1.  Change `#include <os.h>` to `#include "os.h"`
    2.  Change line 25 to `#ifdef __WINDOWS__`

#### For libshout v2.3.1

1.  Edit the file `libshout-2.3.1\src\timing\timing.h` and add near the
    top: `#if defined(_WIN32)
    #define HAVE_FTIME 1
    #include <sys/timeb.h>
    #endif`
2.  Edit `libshout-2.3.1\src\timing\timing.c` and replace the struct
    definition and ftime call at line 57 with the following:`#if
    defined(_WIN32)
                    struct _timeb t;
                    _ftime(&t);
    #else
                    struct timeb t;
                    ftime(&t);
    #endif`

#### For libshout v2.2.2

*Thanks to [Prokoba's
blog](http://zmei.jeox.com/wordpress/?tag=libshout-win32-windows-libshoutdll)
for guidance\!*

1.  Edit the file `libshout-2.2.2\src\timing\timing.h`:
    1.  Remove the `#ifdef _mangle` block
    2.  Before the first `#ifdef _WIN32` line, add `#undef int64_t
        #undef uint64_t`
2.  Edit the file `libshout-2.2.2\src\shout.c`:
    1.  Search and replace all instances of the word `inline` with
        `__inline`
    2.  Change line 1016 to `ret = sock_write_bytes (self->socket,
        (char*)data + pos, len - pos);`
    3.  Add the following at the top: `#ifndef __MINGW32__
                                        #define va_copy(ap1, ap2) memcpy(&ap1, &ap2, sizeof(va_list))
        #endif` 
3.  Edit `libshout-2.2.2\include\shout\shout.h` and place
    ` __declspec(dllexport)  ` in front of every function definition

### Build

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `libshout-2.2.2\win32\libshout.dsp` file via
    File-\>Open-\>Project/Solution and upgrade if needed.
5.  Choose the Release configuration and the Win32 platform
6.  If building for x64
    1.  Go to Build-\>Configuration manager
    2.  Drop down Active Solution Platform and choose New...
    3.  Type x64 and choose copy settings from Win32. Click OK.
    4.  Choose Release on the left, x64 on the right and click Close.
7.  Change the project to a DLL:
    1.  Go to Configuration Properties-\>General, and change
        Configuration Type to "Dynamic Library (.dll)"
    2.  Change Whole Program Optimization to "Use Link Time Code
        Generation"
    3.  Click OK
8.  Find `libshout-2.2.2\src\vorbis.c` and drag it to the `Source Files`
    folder in the project
9.  Add the paths to the dependencies:
    1.  Right-click `libshout` and choose Properties.
    2.  Under Configuration Properties-\>C/C++-\>General, add the
        following paths under `Additional Include Directories`:
        `..\..\pthreads-w32-2-8-0-release,..\..\libvorbis-1.2.3\include,..\..\libogg-1.1.4\include
        `
        1.  If you didn't copy `compat.h`, add the path to the Icecast
            server source as well, `..\..\icecast-2.3.2\src`
    3.  Go to Configuration Properties-\>Linker
        1.  Under General, for Additional Library Directories, enter the
            semicolon-separated paths:
            1.  to the pthreads path you created above (e.g.
                `..\..\pthreads`)
            2.  to ogg.lib and vorbis.lib (which should be in
                `mixxx-win[32|64]lib-msvc` at this point, so you can
                just enter the path to that.)
        2.  Under Linker, for Additional Dependencies, enter
            `pthreadVC2.lib Ws2_32.lib winmm.lib ogg.lib vorbis.lib`
    4.  Click OK.
10. Right click `libshout` and click Build. (If you get a bunch of
    "already defined" errors, go to Configuration Properties-\>Linker
    and under Linker, for Ignore Specific Library, enter `LIBCMT.lib`.)
11. When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `libshout-2.2.2\win32\Release\libshout.lib
    libshout-2.2.2\win32\Release\libshout.dll
    `

## TagLib

[TagLib](http://developer.kde.org/~wheeler/taglib.html) uses the
[CMake](http://www.cmake.org/) build system to build on Windows.

### Dependencies

#### ZLib

You downloaded the zlib source above for libid3tag, but we actually need
to build it for taglib.

##### VS 2005 x64 hacks

[Follow these instructions](#x64-prep-for-vs-express-2005) for the
following files:

    zlib-1.2.5\contrib\vstudio\vc9\zlibvc.sln
    zlib-1.2.5\contrib\vstudio\vc9\zlibvc.vcproj

##### Pre-build

1.  If you don't have MASM installed, just [download the MASM object
    files from
    here](http://www.winimage.com/zLibDll/zlib125_masm_obj.zip) and
    unpack into your zlib source tree. (Or choose the ReleaseWithoutASM
    configuration.)
2.  If you do:
    1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
        SDK-\>CMD Shell)
    2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp
        /x86 /release` for 32-bit.)
    3.  Type `cd zlib-1.2.5\contrib\masmx64` or `cd
        zlib-1.2.5\contrib\masmx86` depending on your platform.
    4.  Type `bld_ml64` or `bld_ml32` depending on your platform.

##### Build

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `zlib-1.2.5\contrib\vstudio\vc9\zlibvc.vcproj` file via
    File-\>Open-\>Project/Solution.
5.  Choose the Release configuration and the Win32 platform.
6.  Right-click the `zlibvc` project and choose Properties
7.  Under Configuration Properties-\>C/C++-\>Preprocessor, add
    **`ZLIB_DLL`** to the list of Preprocessor Definitions
8.  Under Code Generation, ensure that Runtime Library is set to
    **`Multi-threaded DLL (/MD)`**
9.  Click OK
10. Right-click the `zlibvc` project again and click Build
11. When it's done, copy the following file to
    `mixxx-win[32|64]lib-msvc`:`zlib-1.2.5\contrib\vstudio\vc9\x86\ZlibDllRelease\zlibwapi.dll`
    (We don't need .h or .lib files for this since Mixxx itself doesn't
    use it.)

#### Install CMake

1.  [Download CMake](http://www.cmake.org/cmake/resources/software.html)
    (the binary installer is all you need)
2.  Install it (The 32-bit version is fine for 64-bit systems)

### Preparation

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  `cd` to where taglib is extracted, e.g. `C:\sources\taglib-1.6.3`
4.  Enter the command `cmake -DWITH_ASF=ON -DWITH_MP4=ON
    -DZLIB_LIBRARY="C:\path\to\zlib123\projects\visualc6\Win32_DLL_Release\zlib1.lib"
    -DZLIB_INCLUDE_DIR="C:\path\to\zlib123" -G "Visual Studio 9 2008"`
    (for x64 use `"Visual Studio 9 2008 Win64"`)
5.  For VS Express 2008 on x64:
    1.  The above command will return a failure. Run it again but hit
        CTRL-C before it finishes.
    2.  Run it a third time and it will generate the x64 project files.
        ^\_^
    3.  Run it a fourth time to ensure the generated files are coherent.
    4.  For VS Express 2005 on x64, [follow these
        instructions](#x64-prep-for-vs-express-2005) for the following
        files: `taglib-1.6.3\taglib.sln
        taglib-1.6.3\taglib\tag.vcproj`

### Build

1.  Run the Visual Studio GUI from this command line, telling it to use
    the environment variables, to have it use the Platform SDK compile
    tools, libs and includes. (e.g. `C:\Program Files (x86)\Microsoft
    Visual Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
2.  Open the `taglib-1.6.3\taglib\tag.vcproj` file via
    File-\>Open-\>Project/Solution. (If on x64, ignore the platform
    warnings. The "tag" project should appear build-able.)
3.  Choose the Release configuration and the Win32 platform
4.  Right click `tag` and click Build.
5.  When it finishes, copy the following files into
    `mixxx-win32lib-msvc` or `mixxx-win64lib-msvc`:
    `taglib-1.6.3\taglib\Release\tag.lib
    taglib-1.6.3\taglib\Release\tag.dll`
6.  If you get an error about unresolved external symbols, do the
    following:
    1.  Re-open the zlib project above
    2.  Right-click zlibvc and click Properties
    3.  Go to Configuration
        Properties-\>C/C++-\>Preprocessor-\>Preprocessor Definitions and
        remove `ZLIB_WINAPI` from the list. (You may also need to add
        `ZLIB_DLL`.)
    4.  Rebuild zlib & copy the dll file as above to the Mixxx lib
        folder
    5.  Re-open taglib and rebuild
7.  ~~Copy the following files into a `taglib` folder in
    `mixxx-win[32|64]lib-msvc`: `taglib-1.6.3\taglib\toolkit\tfile.h
    taglib-1.6.3\taglib\toolkit\taglib.h
    taglib-1.6.3\taglib\toolkit\tbytevector.h
    taglib-1.6.3\taglib\taglib_export.h
    taglib-1.6.3\taglib_config.h
    taglib-1.6.3\taglib\ape\apetag.h
    taglib-1.6.3\taglib\tag.h
    taglib-1.6.3\taglib\toolkit\tstring.h
    taglib-1.6.3\taglib\toolkit\tmap.h
    taglib-1.6.3\taglib\toolkit\tmap.tcc
    `~~
8.  Just copy every `.h` file from the taglib source tree into
    `mixxx-win[32|64]lib-msvc\taglib`. Some of the files just \#include
    their counterparts in other directories with the actual content, so
    be careful to get the actual content ones. (Do a directory search
    for `*.h`, then sort by size. Copy everything that's over 2K, then
    copy everything 2K and under, rejecting conflicts.)
9.  Also copy the following files to
    `mixxx-win[32|64]lib-msvc`:`taglib-1.6.3\taglib\toolkit\tmap.tcc
    taglib-1.6.3\taglib\toolkit\tlist.tcc
    taglib-1.6.3\taglib_config.h`

## protobuf

Google's [protobuf](http://code.google.com/p/protobuf/) provides MSVC
project files, which makes things nice. Just open and build.
(Step-by-step is given below.)

### Build

1.  Start the platform SDK command prompt (Start-\>Microsoft Windows
    SDK-\>CMD Shell)
2.  Type `setenv /xp /x64 /release` and hit Enter. (Or `setenv /xp /x86
    /release` for 32-bit.)
3.  Run the Visual Studio GUI from this command line, specifying the
    `/useenv` switch to have it use the Platform SDK compile tools, libs
    and includes. (e.g. `C:\Program Files (x86)\Microsoft Visual
    Studio 9.0\Common7\IDE\VCExpress.exe /useenv`)
4.  Open the `protobuf-2.4.1\vsprojects\libprotobuf-lite.vcproj` file
    via File-\>Open-\>Project/Solution.
5.  Answer 'Yes' to convert & open the project
6.  Choose the Release configuration and the Win32 platform
7.  Right-click `libprotobuf-lite` and click build.
8.  When it finishes, run the batch file
    `protobuf-2.4.1\vsprojects\extract_includes.bat`
9.  Copy the following files into `mixxx-win32lib-msvc` or
    `mixxx-win64lib-msvc`:
    `protobuf-2.4.1\vsprojects\Release\libprotobuf-lite.lib
    protobuf-2.4.1\vsprojects\include\google (the entire directory)
    `

# x64 prep for VS Express 2005

If you're doing an x64 build with VS Express 2005, you'll first need to
change some things in the `vcproj` and `sln` files in a text editor
before you open them in VS:

1.  For the `sln` files:
    1.  Replace all instances of "Win32" (case-sensitive) with
        "DontWantThis" or something similar
    2.  Then replace all instances of "x64" with "Win32"
    3.  Save the files
2.  For the `vcproj` files:
    1.  Replace all instances of "|Win32" (case-sensitive) with
        "|DontWantThis" or something similar
    2.  Replace all instances of "|x64" with "|Win32"
    3.  In the \<Platforms\> section at the top of the file, change
        `Name="Win32"` to `Name="DontWantThis"` and `Name="x64"` to
        `Name="Win32"`
    4.  Save the files
3.  Continue with the Build instructions above for the dependency in
    question. (Press your browser's Back button.)

# Optimizations

Mixxx can benefit from various code optimizations. If you right-click
each MSVC project and click Properties, you can set many optimization
options. You can do any or all of the following:

  - Configuration Properties-\>C/C++-\>Optimization
  - Optimization: Maximize Speed (/O2) or Full Optimization (/Ox)
  - Favor Size or Speed: Favor Fast Code (/Ot) (unless building for
    memory-constrained systems)
  - Whole Program Optimization: Enable link-time code generation (/GL)
  - Configuration Properties-\>C/C++-\>Code Generation
  - Enable Enhanced Instruction Set: Streaming SIMD Extensions
    (/arch:SSE) or Streaming SIMD Extensions 2 (/arch:SSE2) if your CPU
    supports either
  - On x64, Configuration Properties-\>C/C++-\>Command Line
  - Add `/favor:AMD64`, `/favor:EM64T` (Intel64,) or `/favor:blend`
    (about the same on both)
  - Configuration Properties-\>Linker-\>Optimization
  - Eliminate Unreferenced Data (/OPT:REF)
  - Remove Redundant COMDATs (/OPT:ICF)
  - Use Link Time Code Generation (/ltcg)
  - Configuration Properties-\>Librarian-\>Command line
  - Add `/LTCG`

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

**Note:** Don't link libid3tag, libmad, taglib, or libshout with ASMLIB
if you want to be able to link Mixxx itself with it.
