# Setting up a Mac OS X Builder

As of Q4 2011, Mixxx supports Mac OS X 10.5 and higher on x86 and
x86\_64. PPC and Mac OS 10.4 is no longer supported.

# Install XCode

XCode 4 and higher does not support Mac OS X 10.5. Download and install
an XCode 3.x release suitable for your version of OS X. For Mac OS 10.6,
you will need XCode 3.2 as later versions of XCode do not support 10.6.
Try searching for the filename `xcode3210a432.dmg`.

# Install Qt

Download the latest supported version of Qt source tarball. (In Q4 2011,
this is Qt 4.7.4)

Untar the archive and apply qsettings\_appstore.diff from
[QTBUG-16549](https://bugreports.qt.nokia.com//browse/QTBUG-16549). This
is to support configuring Qt for app store restrictions. Once this patch
or a similar solution is in Qt this step will not be required. Without
this step, the resulting packages will not pass the Mac App Store review
process.

Configure Qt like this:

    ./configure -opensource -arch x86 -arch x86_64 -sdk /Developer/SDKs/MacOSX10.5.sdk/ -plugin-sql-sqlite -platform macx-g++42 -no-qt3support -release
