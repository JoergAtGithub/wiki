# Setting up a Windows Builder

# Environment

    SET MIXXX_LIB_BASE=C:\Mixxx\lib\1.12
    SET MIXXX_LIB_X86=%MIXXX_LIB_BASE%\x86\
    SET MIXXX_LIB_X64=%MIXXX_LIB_BASE%\x64\

# FFTW3

Use version 3.2.2 with VS2008 build files.

# chromaprint

chromaprint 0.7

    cmake . -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DWITH_FFTW3=ON -DLIB_INSTALL_DIR:STRING="%MIXXX_LIB_X86%" -DINCLUDE_INSTALL_DIR:STRING="%MIXXX_LIB_X86%" -DBIN_INSTALL_DIR:STRING="%MIXXX_LIB_X86%" -DFFTW3_DIR:STRING="%MIXXX_LIB_X86%" -DCMAKE_INSTALL_PREFIX:STRING="%MIXXX_LIB_X86%"
    nmake /f Makefile
    COPY .\src\chromaprint.lib %MIXXX_LIB_X86%
    COPY .\src\chromaprint_p.lib %MIXXX_LIB_X86%
