# Setting up a Mac OS X Builder

As of Q4 2011, Mixxx supports Mac OS X 10.5 and higher on x86 and
x86\_64. PPC and Mac OS 10.4 is no longer supported.

**Thanks to the [Mumble
project](http://mumble.sourceforge.net/BuildingMacOSX) for helping us
figure out how to do a lot of this.**

# Environment

    export CC="$(xcode-select -print-path)/usr/bin/gcc-4.2"
    export CXX="$(xcode-select -print-path)/usr/bin/g++-4.2"
    export CPP="$(xcode-select -print-path)/usr/bin/cpp-4.2"
    
    export MACOSX_DEPLOYMENT_TARGET="10.5"
    export OSX_SDK=/Developer/SDKs/MacOSX10.5.sdk
    export MIXXX_PREFIX=$OSX_SDK/usr/local
    
    # If you are not building on a i386 OS X install, change this.
    export HOST=i386-apple-darwin10
    
    export OSX_CFLAGS="-isysroot $OSX_SDK -mmacosx-version-min=$MACOSX_DEPLOYMENT_TARGET"
    export OSX_LDFLAGS="-isysroot $OSX_SDK -Wl,-syslibroot,$OSX_SDK -mmacosx-version-min=$MACOSX_DEPLOYMENT_TARGET"

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

Configure Qt like this:

    ./configure -opensource -prefix $MIXXX_PREFIX/Qt-4.7.4/ -arch x86 -arch x86_64 -sdk $OSX_SDK -plugin-sql-sqlite -platform macx-g++42 -no-qt3support -release

# libflac

    mkdir -p flac-1.2.1-{i386,x86_64}
    tar -zxf flac-1.2.1.tar.gz -C flac-1.2.1-x86_64 --strip-components 1
    tar -zxf flac-1.2.1.tar.gz -C flac-1.2.1-i386 --strip-components 1
    cd flac-1.2.1-x86_64
    export CFLAGS="$OSX_CFLAGS -arch x86_64"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch x86_64"
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target x86_64-apple-darwin10 --disable-cpplibs --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
    make
    cd ../flac-1.2.1-i386
    export CFLAGS="$OSX_CFLAGS -arch i386"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch i386"
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target i386-apple-darwin10 --disable-cpplibs --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
    make 
    sudo make install
    sudo lipo -create src/libFLAC/.libs/libFLAC.8.2.0.dylib ../flac-1.2.1-x86_64/src/libFLAC/.libs/libFLAC.8.2.0.dylib -output $MIXXX_PREFIX/lib/libFLAC.8.2.0.dylib

# libsndfile

    mkdir -p libsndfile-1.0.25-{i386,x86_64}
    tar -zxf libsndfile-1.0.25.tar.gz -C libsndfile-1.0.25-x86_64 --strip-components 1
    tar -zxf libsndfile-1.0.25.tar.gz -C libsndfile-1.0.25-i386 --strip-components 1
    cd libsndfile-1.0.25-x86_64
    export CFLAGS="$OSX_CFLAGS -arch x86_64"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch x86_64"
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target x86_64-apple-darwin10 --prefix=$MIXXX_PREFIX
    make
    cd ../libsndfile-1.0.25-i386
    export CFLAGS="$OSX_CFLAGS -arch i386"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch i386"
    export CC="$CC $CFLAGS"
    export CXX="$CXX $CXXFLAGS"
    ./configure --host $HOST --target i386-apple-darwin10 --prefix=$MIXXX_PREFIX
    make 
    sudo make install
    sudo lipo -create ./src/.libs/libsndfile.1.dylib ../libsndfile-1.0.25-x86_64/src/.libs/libsndfile.1.dylib -output $MIXXX_PREFIX/lib/libsndfile.1.dylib

# libogg

    # not sure if ARCHS does anything
    export ARCHS="i386 x86_64"
    export CFLAGS="$OSX_CFLAGS -arch i386 -arch x86_64"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch i386 -arch x86_64"
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

# libvorbis

    # not sure if ARCHS does anything
    export ARCHS="i386 x86_64"
    export CFLAGS="$OSX_CFLAGS -arch i386 -arch x86_64"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch i386 -arch x86_64"
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

# libmad

    # not sure if ARCHS does anything
    export ARCHS="i386 x86_64"
    export CFLAGS="$OSX_CFLAGS -arch i386 -arch x86_64"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch i386 -arch x86_64"
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    # libmad's build system is broken as of this release and does not respect LDFLAGS for the dylib. copy and paste this equivalent line in your build log and insert "-arch i386 -arch x86_64" somewhere into the line. This will rebuild the dylib with support for both architectures. 
    /Developer/usr/bin/gcc-4.2 -dynamiclib -undefined dynamic_lookup -o .libs/libmad.0.2.1.dylib  .libs/version.o .libs/fixed.o .libs/bit.o .libs/timer.o .libs/stream.o .libs/frame.o .libs/synth.o .libs/decoder.o .libs/layer12.o .libs/layer3.o .libs/huffman.o  -mmacosx-version-min=10.5 -Wl,-syslibroot -Wl,/Developer/SDKs/MacOSX10.5.sdk -arch i386 -arch x86_64 -mmacosx-version-min=10.5 -install_name  /Developer/SDKs/MacOSX10.5.sdk/usr/local/lib/libmad.0.dylib -compatibility_version 3 -current_version 3.1
    sudo make install

# libid3tag

    # not sure if ARCHS does anything
    export ARCHS="i386 x86_64"
    export CFLAGS="$OSX_CFLAGS -arch i386 -arch x86_64"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch i386 -arch x86_64"
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    # libid3tag's build system is broken as of this release and does not respect LDFLAGS for the dylib. copy and paste this equivalent line in your build log and insert "-arch i386 -arch x86_64" somewhere into the line. This will rebuild the dylib with support for both architectures. 
    /Developer/usr/bin/gcc-4.2 -dynamiclib -undefined dynamic_lookup -o .libs/libid3tag.0.3.0.dylib  .libs/version.o .libs/ucs4.o .libs/latin1.o .libs/utf16.o .libs/utf8.o .libs/parse.o .libs/render.o .libs/field.o .libs/frametype.o .libs/compat.o .libs/genre.o .libs/frame.o .libs/crc.o .libs/util.o .libs/tag.o .libs/file.o  -lz -mmacosx-version-min=10.5 -Wl,-syslibroot -Wl,/Developer/SDKs/MacOSX10.5.sdk -mmacosx-version-min=10.5 -install_name  /Developer/SDKs/MacOSX10.5.sdk/usr/local/lib/libid3tag.0.dylib -compatibility_version 4 -current_version 4.0
    sudo make install

# libshout

    # not sure if ARCHS does anything
    export ARCHS="i386 x86_64"
    export CFLAGS="$OSX_CFLAGS -arch i386 -arch x86_64"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch i386 -arch x86_64"
    ./configure --disable-dependency-tracking --prefix=$MIXXX_PREFIX
    make
    sudo make install

# taglib

    export ARCHS="i386 x86_64"
    export CFLAGS="$OSX_CFLAGS -arch i386 -arch x86_64"
    export CXXFLAGS=$CFLAGS
    export LDFLAGS="$OSX_LDFLAGS -arch i386 -arch x86_64"
    cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$MIXXX_PREFIX" -DCMAKE_OSX_DEPLOYMENT_TARGET="$MACOSX_DEPLOYMENT_TARGET" -DCMAKE_OSX_SYSROOT="$OSX_SDK" -DCMAKE_VERBOSE_MAKEFILE=TRUE -DWITH_ASF=ON -DWITH_MP4=ON
    make
    sudo make install
