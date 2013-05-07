# Setting up a Windows Builder

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

# FFTW3

Use version 3.2.2 with VS2008 build files.

# chromaprint

chromaprint 0.7

    cmake . -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DWITH_FFTW3=ON -DFFTW3_DIR:STRING=%MIXXX_LIB% -DCMAKE_INSTALL_PREFIX:STRING=%MIXXX_LIB%
    nmake /f Makefile
    COPY .\src\chromaprint.lib %MIXXX_LIB%
    COPY .\src\chromaprint_p.lib %MIXXX_LIB%
