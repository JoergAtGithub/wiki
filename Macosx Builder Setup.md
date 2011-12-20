# Setting up a Mac OS X Builder

As of Q4 2011, Mixxx supports Mac OS X 10.5 and higher on x86 and
x86\_64. PPC and Mac OS 10.4 is no longer supported.

**Thanks to the [Mumble
project](http://mumble.sourceforge.net/BuildingMacOSX) for helping us
figure out how to do a lot of this.**

# Environment

    export CC="$(xcode-select -print-path)/usr/bin/gcc-4.2"
    export CXX="$(xcode-select -print-path)/usr/bin/g++-4.2"
    
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

    export CFLAGS="$OSX_CFLAGS -arch i386"
    export LDFLAGS="$OSX_LDFLAGS -arch i386"
    ./configure --build i386-apple-darwin10 --disable-cpplibs --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
    make 
    sudo make install
    export CFLAGS="$OSX_CFLAGS -arch x86_64"
    export LDFLAGS="$OSX_LDFLAGS -arch x86_64"
    ./configure --host $HOST --build x86_64-apple-darwin10 --disable-cpplibs --disable-asm-optimizations --disable-ogg --prefix=$MIXXX_PREFIX
    make
