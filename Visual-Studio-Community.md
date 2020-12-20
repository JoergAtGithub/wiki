## Visual Studio IDE

### Description

**Microsoft Visual Studio** is the full-featured IDE from Microsoft for
multiple languages. Since version 2015, there is a free-to-use Community
edition and 2017 added initial support for CMake projects.

Only version 2019 has good CMake support required for Mixxx, so this one is the recommended version.

### Installation

First, when installing Visual studio, you need to select at least the
following elements on the setup wizard:

  - Desktop development with C++
  - Windows 10 SDK
  - C++ CMake Tools for Windows
  - Optional: MSVC v141 - VS 2017 C++ Build tools (These allow to compile with
    2017 compilers on Visual Studio 2019)

### Opening Mixxx source code

Note: CMake support has been added to Mixxx 2.3. You need this version
or newer in order to use these instructions.

Also note that the script in Mixxx sources tools\windows_buildenv.bat 
can generate a CMakeSettings.json

Open Visual Studio, go to File-Open-\>CMake... and select the
CMakelists.txt from the root of the Mixxx source folder.

Then, open the CMake configuration (One place where you can do this is
selecting the CMakelists.txt file, right click and select the configure
CMake for mixxx).

On top, click on the "CMakeSettings.json".  
This file is a file from visual studio that allows to configure some
settings to pass them to CMake.  
Add the following after "ctestCommandArgs": "", (You might need to add
that last comma)

``` 
     "variables": [
        {
          "name": "CMAKE_PREFIX_PATH",
          "value": "PATH_TO_YOUR_BUILD_ENVIRONMENT;PATH_TO_QT_IN_BUILD_ENVIRONMENT",
          "type": "STRING"
        },
        {
          "name": "MEDIAFOUNDATION",
          "value": "True",
          "type": "BOOL"
        },
        {
          "name": "OPUS",
          "value": "True",
          "type": "BOOL"
        },
        {
          "name": "LOCALECOMPARE",
          "value": "True",
          "type": "BOOL"
        },
        {
          "name": "STATIC_DEPS",
          "value": "True",
          "type": "BOOL"
        },
        {
          "name": "CLCACHE_SUPPORT",
          "value": "False",
          "type": "BOOL"
        },
        {
          "name": "BUILD_TESTING",
          "value": "False",
          "type": "BOOL"
        }
      ]
```

Replace PATH\_TO\_YOUR\_BUILD\_ENVIRONMENT and
PATH\_TO\_QT\_IN\_BUILD\_ENVIRONMENT with the correct paths, example:

``` 
          "value": "D:\\sources\\mixxx\\2.3-j00019-x64-release-fastbuild-static-55e94982-minimal;D:\\sources\\mixxx\\2.3-j00019-x64-release-fastbuild-static-55e94982-minimal\\Qt-5.14.2",

```

Once you are done, you can also duplicate the whole block inside
configuration and add a Release build (since, by default it only adds a
debug build)

``` 
      "name": "x64-Release",
      "generator": "Ninja",
      "configurationType": "RelWithDebInfo",
```

Also, I recommend to add the fastbuild OPTIMIZE flag to avoid having a
4GB build dir. Final exe is a bit bigger but also link time is faster
and requires slightly less memory.

``` 
        {
          "name": "OPTIMIZE",
          "value": "fastbuild",
          "type": "STRING"
        }
```

Note that one of the flags is "BUILD\_TESTING" to False. This flag tells
not to build mixxx-test.exe. I recommend to have this flag off by
default, and only set to on after you've build mixxx and want to build
mixxx-test too. It will build just the additional classes and linking
needed for the mixxx-test.

Save CMakeSettings.json, go back to the CMakelists.txt configuration and
click on "Save and generate the CMake cache memory to load variables".
This should launch a CMake compilation to detect the dependencies and
allow Visual Studio to load the sources properly. Note: If debug mode
does not work, try switching to release mode.

This is a sample output

    1> Generación de CMake iniciada para la configuración: "x64-Release".
    1> Línea de comandos: "cmd.exe" /c ""C:\PROGRAM FILES (X86)\MICROSOFT VISUAL STUDIO\2019\COMMUNITY\COMMON7\IDE\COMMONEXTENSIONS\MICROSOFT\CMAKE\CMake\bin\cmake.exe"  -G "Ninja" -DCMAKE_INSTALL_PREFIX:PATH="D:\programacio\mixxx\mixxx-master\out\install\x64-Release" -DCMAKE_PREFIX_PATH:STRING="D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal;D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/Qt-5.14.2" -DMEDIAFOUNDATION:BOOL="True" -DOPUS:BOOL="True" -DLOCALECOMPARE:BOOL="True" -DSTATIC_DEPS:BOOL="True" -DCLCACHE_SUPPORT:BOOL="False" -DCMAKE_C_COMPILER:FILEPATH="C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.25.28610/bin/HostX64/x64/cl.exe" -DCMAKE_CXX_COMPILER:FILEPATH="C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.25.28610/bin/HostX64/x64/cl.exe"  -DCMAKE_BUILD_TYPE="RelWithDebInfo" -DCMAKE_MAKE_PROGRAM="C:\PROGRAM FILES (X86)\MICROSOFT VISUAL STUDIO\2019\COMMUNITY\COMMON7\IDE\COMMONEXTENSIONS\MICROSOFT\CMAKE\Ninja\ninja.exe" "D:\programacio\mixxx\mixxx-master" 2>&1"
    1> Directorio de trabajo: D:\programacio\mixxx\mixxx-master\out\build\x64-Release
    1> [CMake] -- The C compiler identification is MSVC 19.25.28612.0
    1> [CMake] -- The CXX compiler identification is MSVC 19.25.28612.0
    1> [CMake] -- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.25.28610/bin/HostX64/x64/cl.exe
    1> [CMake] -- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.25.28610/bin/HostX64/x64/cl.exe -- works
    1> [CMake] -- Detecting C compiler ABI info
    1> [CMake] -- Detecting C compiler ABI info - done
    1> [CMake] -- Detecting C compile features
    1> [CMake] -- Detecting C compile features - done
    1> [CMake] -- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.25.28610/bin/HostX64/x64/cl.exe
    1> [CMake] -- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.25.28610/bin/HostX64/x64/cl.exe -- works
    1> [CMake] -- Detecting CXX compiler ABI info
    1> [CMake] -- Detecting CXX compiler ABI info - done
    1> [CMake] -- Detecting CXX compile features
    1> [CMake] -- Detecting CXX compile features - done
    1> [CMake] -- Git branch: master
    1> [CMake] -- Git commit: 35a6a1316f
    1> [CMake] -- Git commit count: 7219+
    1> [CMake] -- Found clcache: C:/Python38/Scripts/clcache.exe
    1> [CMake] -- Support for clcache: False
    1> [CMake] -- Found PythonInterp: C:/Python38/python.exe (found version "3.8.2") 
    1> [CMake] -- Looking for pthread.h
    1> [CMake] -- Looking for pthread.h - not found
    1> [CMake] -- Found Threads: TRUE  
    1> [CMake] -- Found Git: C:/Program Files/Git/cmd/git.exe (found version "2.25.1.windows.1") 
    1> [CMake] -- git Version: v0.0.0-dirty
    1> [CMake] -- Version: 0.0.0
    1> [CMake] -- Performing Test HAVE_STD_REGEX
    1> [CMake] -- Performing Test HAVE_STD_REGEX
    1> [CMake] -- Performing Test HAVE_STD_REGEX -- success
    1> [CMake] -- Performing Test HAVE_GNU_POSIX_REGEX
    1> [CMake] -- Performing Test HAVE_GNU_POSIX_REGEX
    1> [CMake] -- Performing Test HAVE_GNU_POSIX_REGEX -- failed to compile
    1> [CMake] -- Performing Test HAVE_POSIX_REGEX
    1> [CMake] -- Performing Test HAVE_POSIX_REGEX
    1> [CMake] -- Performing Test HAVE_POSIX_REGEX -- failed to compile
    1> [CMake] -- Performing Test HAVE_STEADY_CLOCK
    1> [CMake] -- Performing Test HAVE_STEADY_CLOCK
    1> [CMake] -- Performing Test HAVE_STEADY_CLOCK -- success
    1> [CMake] -- Found Chromaprint: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/chromaprint_p.lib  
    1> [CMake] -- Found FFTW: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libfftw-3.3.lib  
    1> [CMake] -- Could NOT find Ebur128 (missing: Ebur128_LIBRARY Ebur128_INCLUDE_DIR) 
    1> [CMake] -- Preparing internal Ebur128
    1> [CMake] -- Looking for STAILQ_HEAD
    1> [CMake] -- Looking for STAILQ_HEAD - not found
    1> [CMake] -- Linking internal libebur128 statically: D:/programacio/mixxx/mixxx-master/out/build/x64-Release/lib/libebur128-install/lib/ebur128_static.lib
    1> [CMake] -- Found FLAC: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libFLAC.lib  
    1> [CMake] -- Found LAME: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libmp3lame-static.lib  
    1> [CMake] -- Found OpenGL: opengl32   
    1> [CMake] -- Found OggVorbis: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/include  
    1> [CMake] -- Performing Test PortAudio2_FOUND
    1> [CMake] -- Performing Test PortAudio2_FOUND - Success
    1> [CMake] -- Found PortAudio: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/include  
    1> [CMake] -- Found PortMidi: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/portmidi.lib  
    1> [CMake] -- Could NOT find Protobuf (missing: Protobuf_LIBRARIES) (found version "2.6.1")
    1> [CMake] -- Found Rubberband: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/rubberband.lib  
    1> [CMake] -- Found SndFile: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libsndfile.lib  
    1> [CMake] -- Found G72X: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/g72x.lib  
    1> [CMake] -- Found Taglib: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/tag.lib  
    1> [CMake] -- Could NOT find MP4 (missing: MP4_LIBRARY MP4_INCLUDE_DIR) 
    1> [CMake] -- Could NOT find MP4v2 (missing: MP4v2_LIBRARY MP4v2_INCLUDE_DIR) 
    1> [CMake] -- Could NOT find FFmpeg (missing: FFMPEG_LIBRARIES FFMPEG_INCLUDE_DIRS AVCODEC_LIBRARIES AVCODEC_INCLUDE_DIRS AVFORMAT_LIBRARIES AVFORMAT_INCLUDE_DIRS AVUTIL_LIBRARIES AVUTIL_INCLUDE_DIRS SWRESAMPLE_LIBRARIES SWRESAMPLE_INCLUDE_DIRS) 
    1> [CMake] -- Found HSS1394: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libHSS1394.lib  
    1> [CMake] -- Could NOT find Lilv (missing: Lilv_LIBRARY Lilv_INCLUDE_DIR) 
    1> [CMake] -- Found Shout: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libshout.lib  
    1> [CMake] -- Found SQLite3: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/sqlite3.lib  
    1> [CMake] -- Found Opus: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/opus.lib  
    1> [CMake] -- Found Celt: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libfftw-3.3.lib  
    1> [CMake] -- Found Silk: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/silk_common.lib  
    1> [CMake] -- Found MAD: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libmad.lib  
    1> [CMake] -- Found ID3Tag: D:/programacio/mixxx/2.3-j00019-x64-release-fastbuild-static-55e94982-minimal/lib/libid3tag.lib  
    1> [CMake] -- Found MediaFoundation: mf.lib;mfplat.lib;mfreadwrite.lib;mfuuid.lib;strmiids.lib
    1> [CMake] -- Could NOT find Modplug (missing: Modplug_LIBRARY Modplug_INCLUDE_DIR) 
    1> [CMake] -- Could NOT find LibUSB (missing: LibUSB_LIBRARY LibUSB_INCLUDE_DIR) 
    1> [CMake] -- Could NOT find HIDAPI (missing: HIDAPI_LIBRARY HIDAPI_INCLUDE_DIR) 
    1> [CMake] -- Linking internal libhidapi statically
    1> [CMake] -- Could NOT find WavPack (missing: WavPack_LIBRARY WavPack_INCLUDE_DIR) 
    1> [CMake] -- Optimization level: portable
    1> [CMake] -- Enabling SS2 CPU optimizations (>= Pentium 4)
    1> [CMake] -- Configuring done
    1> [CMake] -- Generating done
    1> [CMake] -- Build files have been written to: D:/programacio/mixxx/mixxx-master/out/build/x64-Release
    1> [CMake] 
    1> Variables de CMake extraídas.
    1> Rutas de inclusión extraídas.
    1> Encabezados y archivos de origen extraídos.
    1> Modelo de código extraído.
    1> La generación de CMake ha finalizado.

### Debugging

Now, on the toolbar, next to the dropwdown that select the build (Debug
or release) you can select the file that will be launched for debugging.
Select Mixxx and then go to the Menu "Debug -\> Start and debug
configuration for mixxx". A file vslaunch.json will open.

After  
"name": "mixxx.exe",  
you will need to add the resourcesPath argument in order to launch it.  
Current compilation from Visual studio does not prepare the directory,
so you will need to tell it to use it from the sources, like this:

``` 
      "args": [
        "--resourcePath D:\\sources\\mixxx\\mixxx-master\\res"
      ]
```

Now, you can build Mixxx with Compile -\> Compile All, and run and debug
Mixxx using the Debug menu ( F5 shortcut)

### Generate a working directory

As explained above, you cannot execute mixxxx.exe from the build
directory without adding additional parameters. This is because it will
miss the resources, like skins or translations.

In order to generate a working directory (like an installer would do),
use the Compile-\> Install mixxx option from Visual studio.

This does not install the application to the local machine, but instead
generates a new directory ( out/install/Build-Type/ ) which will have
all the requires files in place.
