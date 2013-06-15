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
(`$MIXXX_PREFIX`) to scons via the `osxlib` argument. This guide also
assumes you have archives of each source dependency stored in a folder
named `dependencies` located one level above your build directory.

For ease of maintaining multiple build environments (e.g. different
versions of Mixxx were released with different library versions) our
convention is to install all dependencies to `$OSX_SDK/usr/local/XXX`
where XXX is the name of the environment. For example, we call a 10.5
universal build environment for Mixxx 1.11 `universal-1.11`, and it's
located in `/Developer/SDKs/MacOSX10.5.sdk/usr/local/universal-1.11`. If
you are setting up your own build environment and don't care about this,
you could just set your `$MIXXX_PREFIX` to something standard like
`/usr/local`.

For ease of automation, we give ownership permission to our build
environments while building them so that we can run `make install`
without `sudo`. This allows the build to proceed without user
intervention. We literally copy/paste all the code from each section of
this document into a shell script and run it to create our build
environment. We have left `sudo make install` throughout this document,
but you can remove the `sudo` if your user role is an owner of
`$MIXXX_PREFIX`.

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
    export MIXXX_PREFIX=$OSX_SDK/usr/local/universal-1.11/
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

Download the latest supported version of Qt source tarball. (In Q3 2012,
this is Qt 4.8.3)

Untar the archive and apply qsettings\_appstore.diff from
[QTBUG-16549](https://bugreports.qt.nokia.com//browse/QTBUG-16549). This
is to support configuring Qt for app store restrictions. Once this patch
or a similar solution is in Qt this step will not be required. Without
this step, the resulting packages will not pass the Mac App Store review
process.

## Qt 4.8.2 OSX QLocale fix

Qt 4.8.2 has a NULL-pointer dereference segfault when you do
QLocale::system().uiLanguages() (WTF, right?). This is fixed in Qt
4.8.3.

    --- src/corelib/tools/qlocale_mac.mm.original   2012-09-06 21:59:25.000000000 -0400
    +++ src/corelib/tools/qlocale_mac.mm    2012-09-06 22:00:33.000000000 -0400
    @@ -439,7 +439,7 @@
                      kCFPreferencesAnyApplication,
                      kCFPreferencesCurrentUser,
                      kCFPreferencesAnyHost);
    -        const int cnt = CFArrayGetCount(languages);
    +        const int cnt = languages == NULL ? 0 : CFArrayGetCount(languages);
             QStringList result;
             result.reserve(cnt);
             for (int i = 0; i < cnt; ++i) {

## 10.5 Universal (ppc/i386/x86\_64)

Qt 4.8.2 doesn't build on OSX SDK 10.5 without this patch:
<https://bugreports.qt-project.org/browse/QTBUG-23258>

    export VERSION=qt-everywhere-opensource-src-4.8.3
    export ARCHIVE=$VERSION.tar.gz
    
    tar -zxvf ../dependencies/$ARCHIVE
    cd $VERSION
    export ARCH=
    # Qt gets sad if you use -arch in your CFLAGS/CXXFLAGS. For some reason it does some cutting / munging of your flags and you end up with lone '-arch' flags in your CFLAGS/CXXFLAGS which breaks the build.
    export ARCH_FLAGS=
    source ../environment.sh
    export QTDIR=$MIXXX_PREFIX/Qt-4.8.3
    
    # Apply patch from QTBUG-23258 to fix Qt 4.8.2 and 4.8.3 build on OS X 10.5 SDK
    curl https://bugreports.qt-project.org/secure/attachment/26712/Patch-Qt-4.8-for-10.5 > Patch-Qt-4.8-for-10.5
    patch -p1 < Patch-Qt-4.8-for-10.5
    
    # Qt uses -arch x86 not -arch i386
    ./configure -opensource -prefix $QTDIR -arch x86 -arch x86_64 -arch ppc -sdk $OSX_SDK -plugin-sql-sqlite -platform macx-g++42 -no-qt3support -release -nomake examples -nomake demos -confirm-license
    
    # NOTE: Using -ffast-math will fail when building SQLite so either remove -ffast-math from environment.sh temporarily or remove --fast-math from the SQLite Makefiles (you'll have to do it for QtWebkit and QtSql). You can do this as the build fails since it will complain about -ffast-math. We remove it with sed:
    find src/sql -name 'Makefile*' -exec sed -i -e 's/-ffast-math //g' "{}" \;
    find src/plugins/sqldrivers/sqlite -name 'Makefile*' -exec sed -i -e 's/-ffast-math //g' "{}" \;
    find src/plugins/sqldrivers/sqlite2 -name 'Makefile*' -exec sed -i -e 's/-ffast-math //g' "{}" \;
    find src/3rdparty/webkit/Source/WebCore -name 'Makefile*' -exec sed -i -e 's/-ffast-math //g' "{}" \;
    
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

    export VERSION=libshout-2.3.1
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
    # PortMidi insists on installing to /usr/local/lib. Just move its files to $MIXXX_PREFIX
    #sudo make install
    cp libportmidi_s.a $MIXXX_PREFIX/lib
    install_name_tool -id $MIXXX_PREFIX/lib/libportmidi.dylib libportmidi.dylib
    cp libportmidi.dylib $MIXXX_PREFIX/lib
    cp porttime/porttime.h $MIXXX_PREFIX/include
    cp pm_common/portmidi.h $MIXXX_PREFIX/include
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
    install_name_tool -id $MIXXX_PREFIX/lib/libhss1394.dylib obj/libhss1394.dylib
    sudo cp obj/libhss1394.dylib $MIXXX_PREFIX/lib
    sudo mkdir $MIXXX_PREFIX/include/hss1394
    sudo cp inc/HSS1394.h $MIXXX_PREFIX/include/hss1394
    sudo cp inc/HSS1394Types.h $MIXXX_PREFIX/include/hss1394
    cd ..

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

# chromaprint

## 10.5 Intel (i386/x86\_64)

    export ARCH_FLAGS="-arch i386 -arch x86_64"
    source ../environment.sh
    cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_OSX_SYSROOT="$OSX_SDK" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DWITH_VDSP=TRUE
    make
    sudo make install

## 10.5 Universal (ppc/i386/x86\_64)

``` 
export VERSION=chromaprint-0.7
export ARCHIVE=$VERSION.tar.gz
export DYLIB=src/libchromaprint.0.2.0.dylib
export STATICLIB=src/libchromaprint_p.a

for ARCH in i386 x86_64 ppc
do
  mkdir -p $VERSION-$ARCH
  tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
  cd $VERSION-$ARCH
  source ../environment.sh $ARCH
  cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_OSX_SYSROOT="$OSX_SDK" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DWITH_VDSP=TRUE
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

```

# rubberband

## 10.5 Intel (i386/x86\_64)

## 10.5 Universal (ppc/i386/x86\_64)

    export VERSION=rubberband-1.8.1
    export ARCHIVE=$VERSION.tar.bz2
    export DYLIB=lib/librubberband.dylib
    export STATICLIB=lib/librubberband.a
    export DYLIB_LIST=()
    export STATICLIB_LIST=()
    
    
    for ARCH in i386 x86_64 ppc
    do
      mkdir -p $VERSION-$ARCH
      tar -zxvf ../dependencies/$ARCHIVE -C $VERSION-$ARCH --strip-components 1
      cd $VERSION-$ARCH
      source ../environment.sh $ARCH
      export LDFLAGS="$LDFLAGS -framework vecLib"
      SRC_CFLAGS="-I." SRC_LIBS=" " SNDFILE_CFLAGS=" " SNDFILE_LIBS=" " FFTW_CFLAGS=" " FFTW_LIBS=" " Vamp_LIBS=" " Vamp_CFLAGS=" " ./configure --host $HOST --target $TARGET --prefix=$MIXXX_PREFIX
      # Hack up the Makefile since it sucks.
      sed -i -e 's/LIBRARY_INCLUDES := \\/LIBRARY_INCLUDES := src\/speex\/speex_resampler.h \\/g' Makefile
      sed -i -e 's/LIBRARY_SOURCES := \\/LIBRARY_SOURCES := src\/speex\/resample.c \\/g' Makefile
      sed -i -e 's/\.so/\.dylib/g' Makefile
      sed -i -e 's/-Wl,-Bsymbolic //g' Makefile
      sed -i -e 's/-shared.*$/-dynamiclib/g' Makefile
      sed -i -e 's/-DHAVE_LIBSAMPLERATE -DHAVE_FFTW3 -DFFTW_DOUBLE_ONLY /-DHAVE_VDSP -DUSE_SPEEX -DMALLOC_IS_ALIGNED /g' Makefile
      make lib
      make static
      make dynamic
      DYLIB_LIST+=("../$VERSION-$ARCH/$DYLIB")
      STATICLIB_LIST+=("../$VERSION-$ARCH/$STATICLIB")
      cd ..
    done
    
    # Install the i386 version in case there are binaries we want to run (our host is i386)
    export ARCH=i386
    cd $VERSION-$ARCH
    source ../environment.sh $ARCH
    lipo -create ./$DYLIB ../$VERSION-ppc/$DYLIB ../$VERSION-x86_64/$DYLIB -output ./$DYLIB
    lipo -create ./$STATICLIB ../$VERSION-ppc/$STATICLIB ../$VERSION-x86_64/$STATICLIB -output ./$STATICLIB
    # We can't make install because the stupid Makefile insists on creating the VAMP plugin and the LADSPA plugin and the binary.
    export RUBBERBAND_INCLUDE=$MIXXX_PREFIX/include/rubberband
    export RUBBERBAND_LIB=$MIXXX_PREFIX/lib
    mkdir -p $RUBBERBAND_INCLUDE
    mkdir -p $RUBBERBAND_LIB
    cp rubberband/rubberband-c.h rubberband/RubberBandStretcher.h $RUBBERBAND_INCLUDE
    cp lib/librubberband.a lib/librubberband.dylib $RUBBERBAND_LIB
    cd ..

# Mixxx

To test your new build environment, we will build Mixxx.

    git clone https://github.com/mixxxdj/mixxx.git ./mixxx-trunk
    cd mixxx-trunk/mixxx
    export ARCH_FLAGS="-arch i386 -arch x86_64 -arch ppc"
    source ../../environment.sh
    export CFLAGS="$CFLAGS -I$MIXXX_PREFIX/include"
    export CXXFLAGS="$CFLAGS -I$MIXXX_PREFIX/include"
    export LDFLAGS="$LDFLAGS -L$MIXXX_PREFIX/lib -F$MIXXX_PREFIX/Qt-4.7.4/lib"
    export QTDIR=$MIXXX_PREFIX/Qt-4.8.2/
    # Python/SCons complains if it was built for a more modern SDK version than what you define here. It doesn't matter at this point so clear it.
    export MACOSX_DEPLOYMENT_TARGET=
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
