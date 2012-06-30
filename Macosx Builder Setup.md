# Setting up a Mac OS X Builder

As of Q4 2011, Mixxx supports Mac OS X 10.5 and higher on i386, x86\_64,
and PPC. Mac OS 10.4 are no longer supported.

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
    
    # If you are not building on a i386 OS X install, change this.                                                                                            
    export HOST=i386-apple-darwin10
    export TARGET_I386="i386-apple-darwin10"
    export TARGET_X86_64="x86_64-apple-darwin10"
    export TARGET_POWERPC="powerpc-apple-darwin10"
    
    if [ "$1" == "i386" ]; then
      export TARGET=$TARGET_I386
      export ARCH_FLAGS="-arch $1"
    elif [ "$1" == "x86_64" ]; then
      export TARGET=$TARGET_X86_64
      export ARCH_FLAGS="-arch $1"
    elif [ "$1" == "ppc" ]; then
      export TARGET=$TARGET_POWERPC
      export ARCH_FLAGS="-arch $1"
    else
      # Custom $ARCH_FLAGS is set by caller.                                                                                                                  
    fi
    
    export CC="$(xcode-select -print-path)/usr/bin/gcc-4.2"
    export CXX="$(xcode-select -print-path)/usr/bin/g++-4.2"
    export CPP="$(xcode-select -print-path)/usr/bin/cpp-4.2"
    export CXXCPP="$(xcode-select -print-path)/usr/bin/cpp-4.2"
    
    export MACOSX_DEPLOYMENT_TARGET="10.5"
    export OSX_SDK=/Developer/SDKs/MacOSX10.5.sdk
    export MIXXX_PREFIX=$OSX_SDK/usr/local/universal/
    export PATH=$PATH:$MIXXX_PREFIX/bin/
    
    export COMMON_OPT_FLAGS="-O2 -ffast-math"
    # Core Solo and Core Duo are the only 32-bit mac machines. These support MMX, SSE, SSE2, SSE3. -march=prescott is safe to assume
    export I386_OPT_FLAGS="-mmmx -msse -msse2 -msse3 -mfpmath=sse -march=prescott -mtune=generic"
    export X86_64_OPT_FLAGS="-mmmx -msse -msse2 -msse3 -mfpmath=sse -mtune=generic"
    export POWERPC_OPT_FLAGS=""
    
    export OSX_CFLAGS="-isysroot $OSX_SDK -mmacosx-version-min=$MACOSX_DEPLOYMENT_TARGET $ARCH_FLAGS $COMMON_OPT_FLAGS"
    export OSX_LDFLAGS="-isysroot $OSX_SDK -Wl,-syslibroot,$OSX_SDK -mmacosx-version-min=$MACOSX_DEPLOYMENT_TARGET $ARCH_FLAGS $COMMON_OPT_FLAGS"
    
    if [ "$1" == "i386" ]; then
      echo "Setting options for $1";
      export CFLAGS="$OSX_CFLAGS $I386_OPT_FLAGS"
      export CXXFLAGS="$OSX_CFLAGS $I386_OPT_FLAGS"
      export LDFLAGS="$OSX_LDFLAGS $I386_OPT_FLAGS"
      export SHLIBFLAGS="$OSX_LDFLAGS $I386_OPT_FLAGS"
      export DYLIBFLAGS="$OSX_LDFLAGS $I386_OPT_FLAGS"
    elif [ "$1" == "x86_64" ]; then                                                                                                                             echo "Setting options for $1";
      export CFLAGS="$OSX_CFLAGS $X86_64_OPT_FLAGS"
      export CXXFLAGS="$OSX_CFLAGS $X86_64_OPT_FLAGS"
      export LDFLAGS="$OSX_LDFLAGS $X86_64_OPT_FLAGS"
      export SHLIBFLAGS="$OSX_LDFLAGS $X86_64_OPT_FLAGS"
      export DYLIBFLAGS="$OSX_LDFLAGS $X86_64_OPT_FLAGS"
    elif [ "$1" == "ppc" ]; then
      echo "Setting options for $1";
      export CFLAGS="$OSX_CFLAGS $POWERPC_OPT_FLAGS"
      export CXXFLAGS="$OSX_CFLAGS $POWERPC_OPT_FLAGS"
      export LDFLAGS="$OSX_LDFLAGS $POWERPC_OPT_FLAGS"
      export SHLIBFLAGS="$OSX_LDFLAGS $POWERPC_OPT_FLAGS"
      export DYLIBFLAGS="$OSX_LDFLAGS $POWERPC_OPT_FLAGS"
    else
      echo "ERROR: Unknown arch type, setting default."
      export CFLAGS=$OSX_CFLAGS
      export CXXFLAGS=$OSX_CFLAGS
      export LDFLAGS=$OSX_LDFLAGS
      export SHLIBFLAGS=$OSX_LDFLAGS
      export DYLIBFLAGS=$OSX_LDFLAGS
    fi

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

Qt 4.8.2 doesn't build on OSX SDK 10.5 without this patch:
<https://bugreports.qt-project.org/browse/QTBUG-23258>

    export VERSION=qt-everywhere-opensource-src-4.8.2
    export ARCHIVE=$VERSION.tar.gz
    export QTDIR=$MIXXX_PREFIX/Qt-4.8.2
    
    tar -zxvf ../dependencies/$ARCHIVE
    cd $VERSION
    export ARCH=
    # Qt gets sad if you use -arch in your CFLAGS/CXXFLAGS. For some reason it does some cutting / munging of your flags and you end up with lone '-arch' flags in your CFLAGS/CXXFLAGS which breaks the build.
    export ARCH_FLAGS=
    source ../environment.sh
    # Qt uses -arch x86 not -arch i386
    ./configure -opensource -prefix $QTDIR -arch x86 -arch x86_64 -arch ppc -sdk $OSX_SDK -plugin-sql-sqlite -platform macx-g++42 -no-qt3support -release -nomake examples -nomake demos -confirm-license
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

    export VERSION=flac-1.2.1
    export ARCHIVE=$VERSION.tar.gz
    export DYLIB=src/libFLAC/.libs/libFLAC.8.2.0.dylib
    export STATICLIB=src/libFLAC/.libs/libFLAC.a
    
    for ARCH in i386 x86_64 ppc
    do
      mkdir -p $VERSION-$ARCH
      tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
      cd $VERSION-$ARCH
      source ../environment.sh $ARCH
      export CC="$CC $CFLAGS"
      export CXX="$CXX $CXXFLAGS"
      ./configure --host $HOST --target $TARGET --disable-cpplibs --disable-dependency-tracking --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
      make
      cd ..
    done
    
    # Install the i386 version in case there are binaries we want to run (our host is i386)
    export ARCH=i386
    cd $VERSION-$ARCH
    source ../environment.sh $ARCH
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    lipo -create ./$DYLIB ../$VERSION-ppc/$DYLIB ../$VERSION-x86_64/$DYLIB -output ./$DYLIB
    lipo -create ./$STATICLIB ../$VERSION-ppc/$STATICLIB ../$VERSION-x86_64/$STATICLIB -output ./$STATICLIB
    sudo make install
    cd ..

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

    export VERSION=libsndfile-1.0.25
    export ARCHIVE=$VERSION.tar.gz
    export DYLIB=src/.libs/libsndfile.1.dylib
    export STATICLIB=src/.libs/libsndfile.a
    
    for ARCH in i386 x86_64 ppc
    do
      mkdir -p $VERSION-$ARCH
      tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
      cd $VERSION-$ARCH
      source ../environment.sh $ARCH
      ./configure --host $HOST --target $TARGET --disable-dependency-tracking --prefix=$MIXXX_PREFIX
      make
      cd ..
    done
    
    # Install the i386 version in case there are binaries we want to run (our host is i386)
    export ARCH=i386
    cd $VERSION-$ARCH
    source ../environment.sh $ARCH
    lipo -create ./$DYLIB ../$VERSION-ppc/$DYLIB ../$VERSION-x86_64/$DYLIB -output ./$DYLIB
    lipo -create ./$STATICLIB ../$VERSION-ppc/$STATICLIB ../$VERSION-x86_64/$STATICLIB -output ./$STATICLIB
    sudo make install
    cd ..

# libogg

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    export VERSION=libogg-1.3.0
    export ARCHIVE=$VERSION.tar.gz
    export DYLIB=src/.libs/libogg.0.dylib
    export STATICLIB=src/.libs/libogg.a
    
    for ARCH in i386 x86_64 ppc
    do
      mkdir -p $VERSION-$ARCH
      tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
      cd $VERSION-$ARCH
      source ../environment.sh $ARCH
      ./configure --host $HOST --target $TARGET --disable-dependency-tracking --prefix=$MIXXX_PREFIX
      make
      cd ..
    done
    
    # Install the i386 version in case there are binaries we want to run (our host is i386)
    export ARCH=i386
    cd $VERSION-$ARCH
    source ../environment.sh $ARCH
    lipo -create ./$DYLIB ../$VERSION-ppc/$DYLIB ../$VERSION-x86_64/$DYLIB -output ./$DYLIB
    lipo -create ./$STATICLIB ../$VERSION-ppc/$STATICLIB ../$VERSION-x86_64/$STATICLIB -output ./$STATICLIB
    sudo make install
    cd ..

# libvorbis

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    export VERSION=libvorbis-1.3.3
    export ARCHIVE=$VERSION.tar.gz
    export VORBIS_DYLIB=lib/.libs/libvorbis.0.dylib
    export VORBIS_STATICLIB=lib/.libs/libvorbis.a
    export VORBISENC_DYLIB=lib/.libs/libvorbisenc.2.dylib
    export VORBISENC_STATICLIB=lib/.libs/libvorbisenc.a
    export VORBISFILE_DYLIB=lib/.libs/libvorbisfile.3.dylib
    export VORBISFILE_STATICLIB=lib/.libs/libvorbisfile.a
    
    for ARCH in i386 x86_64 ppc
    do
      mkdir -p $VERSION-$ARCH
      tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
      cd $VERSION-$ARCH
      source ../environment.sh $ARCH
      ./configure --host $HOST --target $TARGET --disable-dependency-tracking --prefix=$MIXXX_PREFIX
      make
      cd ..
    done
    
    # Install the i386 version in case there are binaries we want to run (our host is i386)
    export ARCH=i386
    cd $VERSION-$ARCH
    source ../environment.sh $ARCH
    lipo -create ./$VORBIS_DYLIB ../$VERSION-ppc/$VORBIS_DYLIB ../$VERSION-x86_64/$VORBIS_DYLIB -output ./$VORBIS_DYLIB
    lipo -create ./$VORBIS_STATICLIB ../$VERSION-ppc/$VORBIS_STATICLIB ../$VERSION-x86_64/$VORBIS_STATICLIB -output ./$VORBIS_STATICLIB
    lipo -create ./$VORBISENC_DYLIB ../$VERSION-ppc/$VORBISENC_DYLIB ../$VERSION-x86_64/$VORBISENC_DYLIB -output ./$VORBISENC_DYLIB
    lipo -create ./$VORBISENC_STATICLIB ../$VERSION-ppc/$VORBISENC_STATICLIB ../$VERSION-x86_64/$VORBISENC_STATICLIB -output ./$VORBISENC_STATICLIB
    lipo -create ./$VORBISFILE_DYLIB ../$VERSION-ppc/$VORBISFILE_DYLIB ../$VERSION-x86_64/$VORBISFILE_DYLIB -output ./$VORBISFILE_DYLIB
    lipo -create ./$VORBISFILE_STATICLIB ../$VERSION-ppc/$VORBISFILE_STATICLIB ../$VERSION-x86_64/$VORBISFILE_STATICLIB -output ./$VORBISFILE_STATICLIB
    sudo make install
    cd ..

# libshout

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    export VERSION=libshout-2.3.0
    export ARCHIVE=$VERSION.tar.gz
    export DYLIB=src/.libs/libshout.3.dylib
    export STATICLIB=src/.libs/libshout.a
    
    for ARCH in i386 x86_64 ppc
    do
      mkdir -p $VERSION-$ARCH
      tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
      cd $VERSION-$ARCH
      source ../environment.sh $ARCH
      ./configure --host $HOST --target $TARGET --disable-dependency-tracking --prefix=$MIXXX_PREFIX
      make
      cd ..
    done
    
    # Install the i386 version in case there are binaries we want to run (our host is i386)
    export ARCH=i386
    cd $VERSION-$ARCH
    source ../environment.sh $ARCH
    lipo -create ./$DYLIB ../$VERSION-ppc/$DYLIB ../$VERSION-x86_64/$DYLIB -output ./$DYLIB
    lipo -create ./$STATICLIB ../$VERSION-ppc/$STATICLIB ../$VERSION-x86_64/$STATICLIB -output ./$STATICLIB
    sudo make install
    cd ..

# taglib

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_OSX_SYSROOT="$OSX_SDK" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DWITH_ASF=ON -DWITH_MP4=ON
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

``` 
export VERSION=taglib-1.7.2
export ARCHIVE=$VERSION.tar.gz
export DYLIB=taglib/libtag.1.7.2.dylib
export STATICLIB=taglib/libtag.1.7.2.dylib

for ARCH in i386 x86_64 ppc
do
  mkdir -p $VERSION-$ARCH
  tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
  cd $VERSION-$ARCH
  source ../environment.sh $ARCH
  # To build static, use -DENABLE_STATIC=ON but this turns off building a shared library.
  cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_OSX_SYSROOT="$OSX_SDK" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DWITH_ASF=ON -DWITH_MP4=ON
  make
  cd ..
done

# Install the i386 version in case there are binaries we want to run (our host is i386)
export ARCH=i386
cd $VERSION-$ARCH
source ../environment.sh $ARCH
lipo -create ./$DYLIB ../$VERSION-ppc/$DYLIB ../$VERSION-x86_64/$DYLIB -output ./$DYLIB
# Taglib's build system only builds either a shared library or a dynamic one. We use the dynamic one for now.
#lipo -create ./$STATICLIB ../$VERSION-ppc/$STATICLIB ../$VERSION-x86_64/$STATICLIB -output ./$STATICLIB
sudo make install
cd ..

```

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

    export VERSION=pa_stable_v19_20111121
    export ARCHIVE=$VERSION.tgz
    export DYLIB=lib/.libs/libportaudio.2.dylib
    export STATICLIB=lib/.libs/libportaudio.a
    
    for ARCH in i386 x86_64 ppc
    do
      mkdir -p $VERSION-$ARCH
      tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
      cd $VERSION-$ARCH
      source ../environment.sh $ARCH
      # As of the PA 2011/3/26 snapshot, a deprecated API function of CoreAudio is used which blocks the build due to -Werror. -Wno-deprecated-declarations allows these errors to pass.
      export CFLAGS="$CFLAGS -Wno-deprecated-declarations"
      export CXXFLAGS=$CFLAGS
      # Mac universal in this case includes ppc64 which we aren't supporting.
      ./configure --host $HOST --target $TARGET --prefix=$MIXXX_PREFIX --disable-mac-universal
      make
      cd ..
    done
    
    # Install the i386 version in case there are binaries we want to run (our host is i386)
    export ARCH=i386
    cd $VERSION-$ARCH
    source ../environment.sh $ARCH
    lipo -create ./$DYLIB ../$VERSION-ppc/$DYLIB ../$VERSION-x86_64/$DYLIB -output ./$DYLIB
    lipo -create ./$STATICLIB ../$VERSION-ppc/$STATICLIB ../$VERSION-x86_64/$STATICLIB -output ./$STATICLIB
    sudo make install
    cd ..

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

    export VERSION=portmidi-src-217
    export ARCHIVE=$VERSION.zip
    
    unzip ../dependencies/$ARCHIVE
    cd portmidi
    export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
    source ../environment.sh
    # PortMIDI hard-coded ppc, i386, and x86_64 for CMAKE_OSX_ARCHITECTURES. This is what we are building in this case so no change is necessary.
    cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DCMAKE_OSX_SYSROOT="$OSX_SDK" -DCMAKE_C_FLAGS="$CFLAGS" -DCMAKE_CXX_FLAGS="$CXXFLAGS" -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" 
    make 
    sudo make install
    # PortMidi insists on installing to /usr/local/lib. Just move its files to $MIXXX_PREFIX
    sudo mv /usr/local/lib/libportmidi_s.a $MIXXX_PREFIX/lib
    sudo mv /usr/local/lib/libpmjni.dylib $MIXXX_PREFIX/lib
    sudo mv /usr/local/lib/libportmidi.dylib $MIXXX_PREFIX/lib
    sudo mv /usr/local/include/portmidi.h $MIXXX_PREFIX/include
    sudo mv /usr/local/include/porttime.h $MIXXX_PREFIX/include
    cd ..

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
    export MACOSX_DEPLOYMENT_TARGET=
    scons prefix=$MIXXX_PREFIX
    # Actually, this doesn't work. Just manually copy the files.
    #sudo scons prefix=$MIXXX_PREFIX install
    sudo cp obj/libhss1394.dylib $MIXXX_PREFIX/lib
    sudo mkdir $MIXXX_PREFIX/include/hss1394
    sudo cp inc/HSS1394.h $MIXXX_PREFIX/include/hss1394
    sudo cp inc/HSS1394Types.h $MIXXX_PREFIX/include/hss1394

# libprotobuf

## 10.5 Intel (i386/x86\_64)

**warning untested**

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target $TARGET_X86_64 --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

    export VERSION=protobuf-2.4.1
    export ARCHIVE=$VERSION.tar.gz
    export PROTOBUF_DYLIB=src/.libs/libprotobuf.7.dylib
    export PROTOBUF_STATICLIB=src/.libs/libprotobuf.a
    export PROTOBUF_LITE_DYLIB=src/.libs/libprotobuf-lite.7.dylib
    export PROTOBUF_LITE_STATICLIB=src/.libs/libprotobuf-lite.a
    
    # Note, i386 is first so that we get a working i386 version of protoc which the ARCH's use (our host system is i386).
    for ARCH in i386 x86_64 ppc
    do
      mkdir -p $VERSION-$ARCH
      tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
      cd $VERSION-$ARCH
      source ../environment.sh $ARCH
      if [ "$ARCH" == "i386" ]; then
        ./configure --host $HOST --target $TARGET --disable-dependency-tracking --prefix=$MIXXX_PREFIX
      else
        ./configure --host $HOST --target $TARGET --disable-dependency-tracking --prefix=$MIXXX_PREFIX --with-protoc=../$VERSION-i386/src/protoc
      fi 
      make
      cd ..
    done
    
    # Install the i386 version in case there are binaries we want to run (our host is i386)
    export ARCH=i386
    cd $VERSION-$ARCH
    source ../environment.sh $ARCH
    lipo -create ./$PROTOBUF_DYLIB ../$VERSION-ppc/$PROTOBUF_DYLIB ../$VERSION-x86_64/$PROTOBUF_DYLIB -output ./$PROTOBUF_DYLIB
    lipo -create ./$PROTOBUF_STATICLIB ../$VERSION-ppc/$PROTOBUF_STATICLIB ../$VERSION-x86_64/$PROTOBUF_STATICLIB -output ./$PROTOBUF_STATICLIB
    lipo -create ./$PROTOBUF_LITE_DYLIB ../$VERSION-ppc/$PROTOBUF_LITE_DYLIB ../$VERSION-x86_64/$PROTOBUF_LITE_DYLIB -output ./$PROTOBUF_LITE_DYLIB
    lipo -create ./$PROTOBUF_LITE_STATICLIB ../$VERSION-ppc/$PROTOBUF_LITE_STATICLIB ../$VERSION-x86_64/$PROTOBUF_LITE_STATICLIB -output ./$PROTOBUF_LITE_STATICLIB
    sudo make install
    cd ..
    
    # The binary is going to be called $TARGET_I386-protoc so alias it to protoc
    sudo ln -s $MIXXX_PREFIX/bin/$TARGET_I386-protoc $MIXXX_PREFIX/bin/protoc

# Mixxx

To test your new build environment, we will build Mixxx.

    bzr branch lp:mixxx ./mixxx-trunk
    cd mixxx-trunk/mixxx
    export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
    source ../../environment.sh
    export CFLAGS="$CFLAGS -I$MIXXX_PREFIX/include"
    export CXXFLAGS="$CFLAGS -I$MIXXX_PREFIX/include"
    export LDFLAGS="$LDFLAGS -L$MIXXX_PREFIX/lib -F$MIXXX_PREFIX/Qt-4.7.4/lib"
    export QTDIR=$MIXXX_PREFIX/Qt-4.7.4/
    # qtplugindir is required until we remove hardcoding of /Developer/Applications/Qt/ from our build system :(
    scons bundle package osxlib=$MIXXX_PREFIX/lib coreaudio=1 mad=0 qtplugindir=$QTDIR optimize=1

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

Solution:

    export QTDIR=$MIXXX_PREFIX/Qt-4.7.4/
