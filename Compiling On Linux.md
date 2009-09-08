Compiling Mixxx is fairly straightforward on Linux. The steps below
outline what a user needs to do in order to compile Mixxx for
themselves, if for instance, they wanted to try the latest changes in
SVN.

## 1\. Install build dependencies

Mixxx relies on several external libraries for various features. If your
distribution is Debian based (such as Ubuntu), you can install them by
running:

    sudo apt-get build-dep mixxx 
    sudo apt-get install bzr
    sudo apt-get install subversion (being phased out)
    sudo apt-get install scons
    sudo apt-get install libqt4-dev

For other distributions, you will need to install the following through
your distribution's package manager:

  - scons
  - libid3tag
  - libmad
  - [PortAudio-v19](http://www.portaudio.com)
  - QT 4.4.0+ (if installing from packages, make sure to get
    libqt4-opengl and libqt4-svg too.)
  - libogg, libvorbis, libvorbisfile
  - libsndfile
  - ~~fftw3~~ - not currently used
  - ~~libdjconsole - optional, for Hercules MK2 users~~ - no longer
    required as of r2380 (\~1.6.2)

## 2\. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release from our [downloads
page](http://www.mixxx.org/download.php), or checkout a snapshot from
BZR: (See [Using Bazaar](Using%20Bazaar) for more details & options.)

    bzr checkout lp:mixxx/1.7

For SVN: (being phased out)

    svn co https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk/mixxx

## 3\. Compile and install

If you got the source code from SVN, change to the newly created "mixxx"
directory, and use scons to compile and install:

    cd mixxx
    sudo scons prefix=/usr install

Strongly recommended: To optimize compilation for the CPU you're on if
using GCC 4.2 and above, add `tuned=1` to the list of scons options. To
optimize for another CPU, use `optimize=#` where \# is in the range 1-7:

1.  single-core (P-III and below)
2.  P4
3.  Intel Core
4.  Core 2
5.  Athlon-4/XP/MP
6.  K8/Opteron/AMD64
7.  K8/Opteron/AMD64 w/ SSE3

If you have a Hercules DJ Console, be sure you ~~enable the
`djconsole=1` (MK2 & RMX) or `djconsole_legacy=1` (mp3, MK1)~~ first
install the offical [Hercules Linux
drivers](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1).

If you wanted to update later to a newer snapshot, you would go back to
the mixxx directory and run:

    bzr update

For SVN:

    svn update

## Troubleshooting

  - If you've got an nVidia card and are on Ubuntu (9.04) and at the end
    of the build, you see `/usr/bin/ld: cannot find -lGL
    collect2: ld returned 1 exit status` install `nvidia-glx-dev` by
    doing `sudo apt-get -y install nvidia-glx-dev`. Then re-run `scons`
    and it should build fine.

<!-- end list -->

  - If you have opensuse 11.0 it can happen that youre libaries are
    somehow named incorrectly. 

following error could occour...

    [after checking the dependencies...]
    
    Install root: /usr
    scons: done reading SConscript files.
    scons: Building targets ...
    scons: *** [src/.obj/input.o] TypeError `File **/usr/share/qt4/include/QtCore** found where directory expected.' 
    trying to evaluate `${_concat(INCPREFIX, CPPPATH, INCSUFFIX, __env__, RDirs, TARGET, SOURCE)}'
    scons: building terminated because of errors.

in this case the file QtCore linked to an non existing
directory(../QtCore/QtCore). Fix the link in a console by following
command(in the directory with the broken link)

    laptop:/usr/share/qt4/include # ln -sf /usr/include/QtCore/ QtCore

with -f you force the binary to discard the old link

it's likely that there are other broken links. commandos are the same

    laptop:/usr/share/qt4/include # ln -sf /usr/include/QtGui/ QtGui
    laptop:/usr/share/qt4/include # ln -sf /usr/include/QtXml/ QtXml
    laptop:/usr/share/qt4/include # ln -sf /usr/include/QtOpenGL/ QtOpenGL 
    laptop:/usr/share/qt4/include # ln -sf /usr/include/QtScript/ QtScript 
    laptop:/usr/share/qt4/include # ln -sf /usr/include/Qt3Support/ Qt3Support//

it worked perfectly for me using opensuse 11.0\_x86, kde
3.5.10\_release55

## Further Reading

  - [Compiling Mixxx on
    Ubuntu 7.10](http://www.transglobal-megacorp.com/doku.php?id=mixxx-compilation)
  - [Compiling on an Asus eeePC](Compiling%20on%20an%20Asus%20eeePC)
