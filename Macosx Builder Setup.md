# Setting up a Mac OS X Builder

As of Q4 2011, Mixxx supports Mac OS X 10.5 and higher on i386 and
x86\_64. PPC and Mac OS 10.4 are no longer supported.

To see the supported version of each library for a given Mixxx version,
see [dependencies](dependencies).

**Thanks to the [Mumble
project](http://mumble.sourceforge.net/BuildingMacOSX) for helping us
figure out how to do a lot of this.**

# Environment

This document assumes you are untarring the source to a directory such
as `~/build`. The goal of this document is to prepare a root directory
that looks like `/usr/local` (e.g. a directory with `bin`, `lib`, and
`include` folders) which has all of Mixxx's dependencies compiled and
installed to it. When compiling Mixxx, simply provide this directory
(`$MIXXX_PREFIX`) to scons via the `osxlib` argument.

Store this file as `environment.sh` in your build directory.

    #!/bin/bash
    
    export CC="$(xcode-select -print-path)/usr/bin/gcc-4.2"
    export CXX="$(xcode-select -print-path)/usr/bin/g++-4.2"
    export CPP="$(xcode-select -print-path)/usr/bin/cpp-4.2"
    export CXXCPP="$(xcode-select -print-path)/usr/bin/cpp-4.2"
    
    export MACOSX_DEPLOYMENT_TARGET="10.5"
    export OSX_SDK=/Developer/SDKs/MacOSX10.5.sdk
    export MIXXX_PREFIX=$OSX_SDK/usr/local/universal/
    
    # If you are not building on a i386 OS X install, change this.
    export HOST="i386-apple-darwin10"
    export TARGET_I386="i386-apple-darwin10"
    export TARGET_X86_64="x86_64-apple-darwin10"
    export TARGET_POWERPC="powerpc-apple-darwin10"
    
    export OSX_CFLAGS="-isysroot $OSX_SDK -mmacosx-version-min=$MACOSX_DEPLOYMENT_TARGET $ARCH_FLAGS"
    export OSX_LDFLAGS="-isysroot $OSX_SDK -Wl,-syslibroot,$OSX_SDK -mmacosx-version-min=$MACOSX_DEPLOYMENT_TARGET $ARCH_FLAGS"
    
    export CFLAGS=$OSX_CFLAGS
    export CXXFLAGS=$OSX_CFLAGS
    export LDFLAGS=$OSX_LDFLAGS
    export SHLIBFLAGS=$OSX_LDFLAGS
    export DYLIBFLAGS=$OSX_LDFLAGS

This guide also assumes you have archives of each source dependency
stored in a folder named `dependencies` located one level above your
build directory.

# XCode

XCode 4 and higher does not support Mac OS X 10.5. Download and install
an XCode 3.x release suitable for your version of OS X. For Mac OS 10.6,
you will need XCode 3.2 as later versions of XCode do not support 10.6.
Try searching for the filename `xcode3210a432.dmg`.

After installing, remove these symbolic links as we don't want to dirty
up /usr/local/lib while building libraries.

    sudo rm /Developer/SDKs/MacOSX10.4.sdk/usr/local/lib
    sudo rm /Developer/SDKs/MacOSX10.5.sdk/usr/local/lib
    sudo rm /Developer/SDKs/MacOSX10.6.sdk/usr/local/lib

# Qt

Download the latest supported version of Qt source tarball. (In Q4 2011,
this is Qt 4.7.4)

Untar the archive and apply qsettings\_appstore.diff from
[QTBUG-16549](https://bugreports.qt.nokia.com//browse/QTBUG-16549). This
is to support configuring Qt for app store restrictions. Once this patch
or a similar solution is in Qt this step will not be required. Without
this step, the resulting packages will not pass the Mac App Store review
process.

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    ./configure -opensource -prefix $MIXXX_PREFIX/Qt-4.7.4/ $ARCH_FLAGS -sdk $OSX_SDK -plugin-sql-sqlite -platform macx-g++42 -no-qt3support -release -nomake examples -nomake demos -confirm-license
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
    source ../environment.sh
    ./configure -opensource -prefix $MIXXX_PREFIX/Qt-4.7.4/ $ARCH_FLAGS -sdk $OSX_SDK -plugin-sql-sqlite -platform macx-g++42 -no-qt3support -release -nomake examples -nomake demos -confirm-license
    make
    sudo make install

# libflac

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target x86_64-apple-darwin10 --disable-cpplibs --disable-dependency-tracking --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    mkdir -p flac-1.2.1-{i386,x86_64,ppc}
    tar -zxvf ../dependencies/flac-1.2.1.tar.gz -C flac-1.2.1-i386 --strip-components 1
    tar -zxvf ../dependencies/flac-1.2.1.tar.gz -C flac-1.2.1-x86_64 --strip-components 1
    tar -zxvf ../dependencies/flac-1.2.1.tar.gz -C flac-1.2.1-ppc --strip-components 1
    cd flac-1.2.1-ppc
    export ARCH_FLAGS="-arch ppc"
    source ../environment.sh
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target $TARGET_POWERPC --disable-cpplibs --disable-dependency-tracking --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
    make
    cd ../flac-1.2.1-i386
    export ARCH_FLAGS="-arch i386"
    source ../environment.sh
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target $TARGET_I386 --disable-cpplibs --disable-dependency-tracking --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
    make
    cd ../flac-1.2.1-x86_64
    export ARCH_FLAGS="-arch x86_64"
    source ../environment.sh
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target $TARGET_X86_64 --disable-cpplibs --disable-dependency-tracking --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
    make
    lipo -create ./src/libFLAC/.libs/libFLAC.8.2.0.dylib ../flac-1.2.1-ppc/src/libFLAC/.libs/libFLAC.8.2.0.dylib ../flac-1.2.1-i386/src/libFLAC/.libs/libFLAC.8.2.0.dylib -output src/libFLAC/.libs/libFLAC.8.2.0.dylib
    sudo make install

# libsndfile

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target x86_64-apple-darwin10 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    mkdir -p libsndfile-1.0.25-{i386,x86_64,ppc}
    tar -zxvf ../dependencies/libsndfile-1.0.25.tar.gz -C libsndfile-1.0.25-i386 --strip-components 1
    tar -zxvf ../dependencies/libsndfile-1.0.25.tar.gz -C libsndfile-1.0.25-x86_64 --strip-components 1
    tar -zxvf ../dependencies/libsndfile-1.0.25.tar.gz -C libsndfile-1.0.25-ppc --strip-components 1
    cd libsndfile-1.0.25-ppc
    export ARCH_FLAGS="-arch ppc"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_POWERPC --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    cd ../libsndfile-1.0.25-i386
    export ARCH_FLAGS="-arch i386"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_I386 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    cd ../libsndfile-1.0.25-x86_64
    export ARCH_FLAGS="-arch x86_64"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_X86_64 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    lipo -create ./src/.libs/libsndfile.1.dylib ../libsndfile-1.0.25-ppc/src/.libs/libsndfile.1.dylib ../libsndfile-1.0.25-i386/src/.libs/libsndfile.1.dylib -output src/.libs/libsndfile.1.dylib
    sudo make install

# libogg

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    mkdir -p libogg-1.3.0-{i386,x86_64,ppc}
    tar -zxvf ../dependencies/libogg-1.3.0.tar.gz -C libogg-1.3.0-i386 --strip-components 1
    tar -zxvf ../dependencies/libogg-1.3.0.tar.gz -C libogg-1.3.0-x86_64 --strip-components 1
    tar -zxvf ../dependencies/libogg-1.3.0.tar.gz -C libogg-1.3.0-ppc --strip-components 1
    cd libogg-1.3.0-ppc
    export ARCH_FLAGS="-arch ppc"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_POWERPC --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    cd ../libogg-1.3.0-i386
    export ARCH_FLAGS="-arch i386"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_I386 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    cd ../libogg-1.3.0-x86_64
    export ARCH_FLAGS="-arch x86_64"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_X86_64 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    lipo -create ./src/.libs/libogg.0.dylib ../libogg-1.3.0-ppc/src/.libs/libogg.0.dylib ../libogg-1.3.0-i386/src/.libs/libogg.0.dylib -output src/.libs/libogg.0.dylib
    sudo make install

# libvorbis

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    mkdir -p libvorbis-1.3.2-{i386,x86_64,ppc}
    tar -zxvf ../dependencies/libvorbis-1.3.2.tar.gz -C libvorbis-1.3.2-i386 --strip-components 1
    tar -zxvf ../dependencies/libvorbis-1.3.2.tar.gz -C libvorbis-1.3.2-x86_64 --strip-components 1
    tar -zxvf ../dependencies/libvorbis-1.3.2.tar.gz -C libvorbis-1.3.2-ppc --strip-components 1
    cd libvorbis-1.3.2-ppc
    export ARCH_FLAGS="-arch ppc"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_POWERPC --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    cd ../libvorbis-1.3.2-i386
    export ARCH_FLAGS="-arch i386"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_I386 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    cd ../libvorbis-1.3.2-x86_64
    export ARCH_FLAGS="-arch x86_64"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_X86_64 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    lipo -create ./lib/.libs/libvorbis.0.dylib ../libvorbis-1.3.2-ppc/lib/.libs/libvorbis.0.dylib ../libvorbis-1.3.2-i386/lib/.libs/libvorbis.0.dylib -output lib/.libs/libvorbis.0.dylib
    lipo -create ./lib/.libs/libvorbisenc.2.dylib ../libvorbis-1.3.2-ppc/lib/.libs/libvorbisenc.2.dylib ../libvorbis-1.3.2-i386/lib/.libs/libvorbisenc.2.dylib -output lib/.libs/libvorbisenc.2.dylib
    lipo -create ./lib/.libs/libvorbisfile.3.dylib ../libvorbis-1.3.2-ppc/lib/.libs/libvorbisfile.3.dylib ../libvorbis-1.3.2-i386/lib/.libs/libvorbisfile.3.dylib -output lib/.libs/libvorbisfile.3.dylib
    sudo make install

# libshout

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    mkdir -p libshout-2.2.2-{i386,x86_64,ppc}
    tar -zxvf ../dependencies/libshout-2.2.2.tar.gz -C libshout-2.2.2-i386 --strip-components 1
    tar -zxvf ../dependencies/libshout-2.2.2.tar.gz -C libshout-2.2.2-x86_64 --strip-components 1
    tar -zxvf ../dependencies/libshout-2.2.2.tar.gz -C libshout-2.2.2-ppc --strip-components 1
    cd libshout-2.2.2-ppc
    export ARCH_FLAGS="-arch ppc"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_POWERPC --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    cd ../libshout-2.2.2-i386
    export ARCH_FLAGS="-arch i386"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_I386 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    cd ../libshout-2.2.2-x86_64
    export ARCH_FLAGS="-arch x86_64"
    source ../environment.sh
    ./configure --host $HOST --target $TARGET_X86_64 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    lipo -create ./src/.libs/libshout.3.2.0.dylib ../libshout-2.2.2-ppc/src/.libs/libshout.3.2.0.dylib ../libshout-2.2.2-i386/src/.libs/libshout.3.2.0.dylib -output src/.libs/libshout.3.2.0.dylib
    sudo make install

# taglib

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_OSX_SYSROOT="$OSX_SDK" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DWITH_ASF=ON -DWITH_MP4=ON
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    # I believe taglib is safe to compile multiple architectures together.
    export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
    source ../environment.sh
    cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_OSX_SYSROOT="$OSX_SDK" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DWITH_ASF=ON -DWITH_MP4=ON
    make
    sudo make install

# portaudio

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    # As of the PA 2011/3/26 snapshot, a deprecated API function of CoreAudio is used which blocks the build due to -Werror. -Wno-deprecated-declarations allows these errors to pass.
    export CFLAGS="$CFLAGS -Wno-deprecated-declarations"
    export CXXFLAGS=$CFLAGS
    ./configure --prefix=$MIXXX_PREFIX --disable-mac-universal
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
    source ../environment.sh
    # As of the PA 2011/3/26 snapshot, a deprecated API function of CoreAudio is used which blocks the build due to -Werror. -Wno-deprecated-declarations allows these errors to pass.
    export CFLAGS="$CFLAGS -Wno-deprecated-declarations"
    export CXXFLAGS=$CFLAGS
    # Mac universal in this case includes ppc64 which we aren't supporting.
    ./configure --prefix=$MIXXX_PREFIX --disable-mac-universal
    make
    sudo make install

# portmidi

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    # Edit CMakeLists.txt to manually remove ppc from the CMAKE_OSX_ARCHITECTURES variable. 
    cmake . -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DCMAKE_OSX_SYSROOT="$OSX_SDK"   
    make 
    sudo make install
    # PortMidi insists on installing to /usr/local/lib. Just move its files to $MIXXX_PREFIX
    sudo mv /usr/local/lib/libportmidi_s.a $MIXXX_PREFIX/lib
    sudo mv /usr/local/lib/libpmjni.dylib $MIXXX_PREFIX/lib
    sudo mv /usr/local/lib/libportmidi.dylib $MIXXX_PREFIX/lib
    sudo mv /usr/local/include/portmidi.h $MIXXX_PREFIX/include
    sudo mv /usr/local/include/porttime.h $MIXXX_PREFIX/include

## 10.5 Universal (ppc/i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
    source ../environment.sh
    # PortMIDI hard-coded ppc, i386, and x86_64 for CMAKE_OSX_ARCHITECTURES. This is what we are building in this case so no change is necessary.
    cmake . -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DCMAKE_OSX_SYSROOT="$OSX_SDK"   
    make 
    sudo make install
    # PortMidi insists on installing to /usr/local/lib. Just move its files to $MIXXX_PREFIX
    sudo mv /usr/local/lib/libportmidi_s.a $MIXXX_PREFIX/lib
    sudo mv /usr/local/lib/libpmjni.dylib $MIXXX_PREFIX/lib
    sudo mv /usr/local/lib/libportmidi.dylib $MIXXX_PREFIX/lib
    sudo mv /usr/local/include/portmidi.h $MIXXX_PREFIX/include
    sudo mv /usr/local/include/porttime.h $MIXXX_PREFIX/include

# hss1394

## 10.5 Intel (i386/x86\_64)

    bzr checkout lp:hss1394
    cd hss1394
    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    scons prefix=$MIXXX_PREFIX
    # Actually, this doesn't work. Just manually copy the files.
    #sudo scons prefix=$MIXXX_PREFIX install
    sudo cp obj/libhss1394.dylib $MIXXX_PREFIX/lib
    sudo mkdir $MIXXX_PREFIX/include/hss1394
    sudo cp inc/HSS1394.h $MIXXX_PREFIX/include/hss1394
    sudo cp inc/HSS1394Types.h $MIXXX_PREFIX/include/hss1394

## 10.5 Universal (ppc/i386/x86\_64)

    bzr checkout lp:hss1394
    cd hss1394
    export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
    source ../environment.sh
    scons prefix=$MIXXX_PREFIX
    # Actually, this doesn't work. Just manually copy the files.
    #sudo scons prefix=$MIXXX_PREFIX install
    sudo cp obj/libhss1394.dylib $MIXXX_PREFIX/lib
    sudo mkdir $MIXXX_PREFIX/include/hss1394
    sudo cp inc/HSS1394.h $MIXXX_PREFIX/include/hss1394
    sudo cp inc/HSS1394Types.h $MIXXX_PREFIX/include/hss1394

# Mixxx

To test your new build environment, we will build Mixxx.

``` 
bzr branch lp:mixxx ./mixxx-trunk
cd mixxx-trunk/mixxx
export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
source ../../environment.sh
export CFLAGS="$CFLAGS -I$MIXXX_PREFIX/include"
export CXXFLAGS="$CFLAGS -I$MIXXX_PREFIX/include"
export LDFLAGS="$LDFLAGS -L$MIXXX_PREFIX/lib -F$MIXXX_PREFIX/Qt-4.7.4/lib"
scons bundle package osxlib=$MIXXX_PREFIX/lib coreaudio=1 mad=0 
```

Take the DMG in the `osx32_build` folder and try it out on the CPUs you
built it for.

# Potential Issues

    Traceback (most recent call last):  File "/usr/local/bin/scons", line 95, in <module>
        import pkg_resources  File "/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/pkg_resources.py", line 651, in <module>    class Environment(object):
      File "/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/pkg_resources.py", line 654, in Environment
        def __init__(self, search_path=None, platform=get_supported_platform(), python=PY_MAJOR):
      File "/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/pkg_resources.py", line 55, in get_supported_platform
        plat = get_build_platform(); m = macosVersionString.match(plat)
      File "/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/pkg_resources.py", line 181, in get_build_platform
        plat = get_platform()
      File "/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/util.py", line 97, in get_platform    cfgvars = get_config_vars()  File "/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/sysconfig.py", line 525, in get_config_vars    func()  File "/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/distutils/sysconfig.py", line 408, in _init_posix    raise DistutilsPlatformError(my_msg)
    distutils.errors.DistutilsPlatformError: $MACOSX_DEPLOYMENT_TARGET mismatch: now "10.5" but "10.6" during configure

Solution:

    export MACOSX_DEPLOYMENT_TARGET=

    Exception: Qt4 command 'moc' not found. Tried: /Library/Frameworks/bin/moc-qt4 and /Library/Frameworks/bin/moc:
