[External Link](http://example.com)====== Setting up a Windows Builder
======

# Environment

First set `MIXXX_X` to either `x64` or `x86`.

    SET MIXXX_X=x86
    SET MIXXX_X=x64

Then, run this snippet:

    SET WINDOWS_SDK_VERSION=7.1
    SET MIXXX_LIB_BASE=C:\Mixxx\lib\1.12
    SET MIXXX_LIB=%MIXXX_LIB_BASE%\%MIXXX_X%\
    "C:\Program Files\Microsoft SDKs\Windows\v%WINDOWS_SDK_VERSION%\Bin\SetEnv.cmd" /xp /release /%MIXXX_X%
    "%DXSDK_DIR%\Utilities\Bin\dx_setenv.cmd" %MIXXX_X%
    SET MIXXX_VCEXPRESS="c:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\IDE\VCExpress.exe"

# Build Settings

## Runtime

**Important:** Every dependency must be built with the same runtime. The
options are:

    /MT - multi-threaded static 
    /MTd - multi-threaded static debug
    /MD - multi-threaded DLL 
    /MDd - multi-threaded DLL debug

We use `/MD` currently. **If you do not use the same runtime, then Mixxx
will have seemingly random segfaults on some Windows platforms and you
will hate your life.**

## Static vs. Dynamic Libraries

You can choose whether to build dependencies as static libraries (`.lib`
files) or dynamic libraries (`.dll` files). Static libraries don't need
to be distributed with Mixxx -- they are baked into `mixxx.exe`. Another
advantage is you don't have to deal with Windows "DLL hell" as much.

## Release vs. Debug

Release configurations of libraries often build with the most efficient
settings and strip debug information out of the library. This is good
for performance but bad for debuggability.

The important thing is that if you cannot mix release and debug
libraries since they often use the debug or release runtime. Some
libraries provide a "release-with-debug-info" option. This is preferable
since providing debug symbols in a binary comes at no performance cost
and a slight size increase. The upshot of this is that stacktraces from
Windows users will come with more information and stack frames filled
in.

# FFTW3

Use version 3.2.2 with VS2008 build files.

# chromaprint

chromaprint 0.7

    cmake . -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DWITH_FFTW3=ON -DFFTW3_DIR:STRING=%MIXXX_LIB% -DCMAKE_INSTALL_PREFIX:STRING=%MIXXX_LIB%
    nmake /f Makefile
    COPY .\src\chromaprint.lib %MIXXX_LIB%
    COPY .\src\chromaprint_p.lib %MIXXX_LIB%
    COPY .\src\chromaprint.h %MIXXX_LIB%

# rubberband

rubberband 1.8.1

  - Edit Project File:
  - Release -\> General -\> Whole Program Optimization -\> Use Link Time
    Code Generation
  - Release -\> C/C++ -\> Optimization -\> Whole Program Optimization
    -\> Enable link-time code generation
  - Release -\> C/C++ -\> Code Generation -\> Runtime Library -\>
    **VERIFY /MD IS SELECTED**
  - Add to source files: `src/kissfft/kiss_fft.c`
    `src/kissfft/kiss_fftr.c`

For the x64 version of rubberband you need to hand-patch
`src/float_cast/float_cast.h` to remove inline assembly (taken from
<http://doxygen.reactos.org/dc/de3/float__cast_8h_source.html> -- the
copyright on the file is the same as `float_cast.h`)

Stick this block before `#if (defined (WIN32) || defined (_WIN32))` and
change it to `#elif`.

    #if (defined (WIN64) || defined(_WIN64))
    #include    <math.h>
    #include    <emmintrin.h>
    #include    <mmintrin.h>
    __inline long int
    lrint(double flt)
    {
        return _mm_cvtsd_si32(_mm_load_sd(&flt));
    }
    
    __inline long int
    lrintf(float flt)
    {
        return _mm_cvtss_si32(_mm_load_ss(&flt));
    }

    %MIXXX_VCEXPRESS% rubberband-library.vcproj /project rubberband-library /build Release /useenv 
    # Wait until rubberband-library.lib shows up in Release/
    COPY .\Release\rubberband-library.lib %MIXXX_LIB%\rubberband.lib
    XCOPY /E rubberband %MIXXX_LIB%\rubberband\
