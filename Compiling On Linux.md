Compiling Mixxx is fairly straightforward on Linux. The steps below
outline what a user needs to do in order to compile Mixxx for
themselves, if for instance, they wanted to try the latest changes in
SVN.

## 1\. Install build dependencies

Mixxx relies on several external libraries for various features. If your
distribution is Debian based (such as Ubuntu), you can install them by
running:

    sudo apt-get build-dep mixxx 
    sudo apt-get install subversion
    sudo apt-get install scons
    sudo apt-get install libqt4-dev

For other distributions, you will need to install the following through
your distribution's package manager:

  - scons
  - libid3tag
  - libmad
  - [PortAudio-v19](http://www.portaudio.com)
  - QT 4.3.0+
  - fftw3
  - libogg, libvorbis, libvorbisfile
  - libsndfile
  - libdjconsole - optional, for Hercules MK2 users 

## 2\. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release off our [downloads
page](http://www.mixxx.org/download.php), or checkout a snapshot from
SVN:

    svn co https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk/mixxx

## 3\. Compile and install

If you got the source code from SVN, change to the newly created "mixxx"
directory, and use scons to compile and install:

    cd mixxx
    sudo scons prefix=/usr install

Strongly recommended: To optimize compilation for the CPU you're on if
using GCC 4.2 and above, add `tuned=1` to the list of scons options. To
optimize for another CPU, use `optimize=#` where \# is in the range 1-4:
1 is single-core (P-III and below,) 2 is for P4, 3 is for Intel Core, 4
is for Core 2...

If you wanted to update later to a newer SVN snapshot, you would go back
to the mixxx directory and run:

    svn update

## Further Reading

  - [Compiling Mixxx on
    Ubuntu 7.10](http://www.transglobal-megacorp.com/doku.php?id=mixxx-compilation)
  - [Compiling on an Asus eeePC](Compiling%20on%20an%20Asus%20eeePC)
