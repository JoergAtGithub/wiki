# Setting up a Windows Builder

# Environment

    SET MIXXX_LIB_BASE="C:\Mixxx\lib\1.12"
    SET MIXXX_LIB_X86="%MIXXX_LIB_BASE%\x86\"
    SET MIXXX_LIB_X64="%MIXXX_LIB_BASE%\x64\"

# FFTW3

Use version 3.2.2 with VS2008 build files.

# chromaprint

chromaprint 0.7

    C:\Users\mixxx\Downloads\chromaprint-0.7\chromaprint-0.7-x86>cmake . -DBUILD_SHARED_LIBS=OFF -DWITH_FFTW3=ON -DFFTW3_DIR="%MIXXX_LIB_X86%" -DLIB_INSTALL_DIR="%MIXXX_LIB_X86%" -DINCLUDE_INSTALL_DIR="%MIXXX_LIB_X86%"
