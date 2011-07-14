Compiling Mixxx is fairly straightforward on Linux. The steps below
outline what a user needs to do in order to compile Mixxx for
themselves, if for instance, they wanted to try the latest changes in
our code repository (BZR).

## 1\. Install build dependencies

Mixxx relies on several external libraries for various features. If your
distribution is Debian based (such as Ubuntu), you can install them by
running:

    sudo apt-get build-dep mixxx 
    sudo apt-get install bzr scons libqt4-dev libqt4-sql-sqlite libportmidi-dev libshout-dev libtag1-dev
    sudo apt-get install libfaad-dev libmp4v2-dev # required for M4A support

On Fedora 13 and 14, you need enable rpmfusion repo and then:

    yum install scons alsa-lib-devel qt4-devel libGL-devel libGLU-devel \
    libid3tag-devel libmad-devel libmp4v2-devel libsndfile-devel libvorbis-devel \
    portaudio-devel ffmpeg-devel libshout-devel python-devel lua-devel \
    tolua++-devel portmidi-devel qt-webkit-devel

For other distributions, you will need to install the following through
your distribution's package manager:

  - scons
  - libid3tag
  - libmad
  - [PortAudio-v19](http://www.portaudio.com)
  - QT 4.6.0+ (if installing from packages, make sure to get
    libqt4-opengl and libqt4-svg too.)
  - libogg, libvorbis, libvorbisfile
  - libsndfile
  - [PortMidi & PortTime](http://portmedia.sourceforge.net/portmidi)
  - [libmp4](http://www.mpeg4ip.net/) (or
    [libmp4v2](http://code.google.com/p/mp4v2/)) (optional, for M4A file
    support)
  - libshout 
  - taglib

## 2\. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release from our [downloads
page](http://www.mixxx.org/download.php), or checkout a snapshot from
BZR: (See [Using Bazaar](Using%20Bazaar) for more details & options.)

  - For the latest stable release: `bzr checkout lp:mixxx/1.9`
  - For trunk: `bzr checkout lp:mixxx`

## 3\. Compile and install

If you got the source code from BZR, change to the newly created "mixxx"
directory, and use scons to compile. As a regular user, do:

    cd 1.9  # or  cd mixxx  if you downloaded trunk
    cd mixxx  # (again)
    scons

### Multi-threaded build

If you have a multi-core CPU (or just multiple CPUs) use scons' **-j**
flag to specify the number of build threads to speed up building.
Generally, use as many threads as you have cores. (Note that if you have
a CPU with HyperThreading (which looks like two cores to the OS,) ignore
the extra apparent one\!)

So for example, if you have two dual-core CPUs for a total of four
cores, just do: **`scons -j4`**

If you have two single-core HT CPUs, do: **`scons -j2`** even though it
looks like you have 4 cores. (You don't. Specifying more threads will
only slow down the build.)

If you want to just run this copy without installing, from the same
directory, run:

    ./mixxx --resourcePath res/

If you want to install it system-wide, do:

    sudo scons prefix=/usr install

If you are upgrading, it is recommended to first uninstall the previous
version of mixxx with the following:

    sudo scons -c install

before compiling as described above.

**Strongly recommended**: To optimize compilation for the CPU you're on
if using GCC 4.2 and above, add `tuned=1` to the list of scons options.
To optimize for another CPU, use `optimize=#` where \# is in the range
1-7:

1.  single-core (P-III and below)
2.  P4
3.  Intel Core
4.  Core 2
5.  Athlon-4/XP/MP
6.  K8/Opteron/AMD64
7.  K8/Opteron/AMD64 w/ SSE3

If you have a Hercules DJ Console, be sure you install the official
[Hercules Linux
drivers](http://ts.hercules.com/eng/index.php?pg=view_files&gid=2&fid=28&pid=215&cid=1#section1).

If you wanted to update later to a newer snapshot, you would go back to
the mixxx directory and run:

    bzr update

## Troubleshooting

#### nVidia

If you've got an nVidia card and are on Ubuntu (9.04) and at the end of
the build, you see `/usr/bin/ld: cannot find -lGL
collect2: ld returned 1 exit status` install `nvidia-glx-dev` by doing
`sudo apt-get -y install nvidia-glx-dev`. Then re-run `scons` and it
should build fine.

#### opensuse

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

#### Ubuntu 9.04 or higher

If soundmanger hangs on Ubuntu 9.04 or higher replace PortAudio with an
older version.

  - Download »`pa_stable_v19_20071207.tar.gz`« from
    [portaudio.com](http://www.portaudio.com/download.html)
  - Deflate and change into PortAudio directory
  - Run »`./configure`« maybe try »`./configure --prefix=/usr`«
  - Run »`make`«
  - Run »`sudo make install`«

This overwrites files installed by portaudio2 and portaudio19-dev
package from ubuntu. Thus don't reinstall them.

  - See also: [Bug
    \#383431](https://bugs.launchpad.net/ubuntu/+source/portaudio/+bug/383431)

#### Debian Squeeze on AMD64 jack/portaudio issues

So in Ubuntu the issue is solved for Lucid and later Releases (see [Bug
\#360590](https://bugs.launchpad.net/ubuntu/+source/portaudio/+bug/360590))  
In debian we still hafta wait for that. Portaudio is still compiled
without jack support  
on AMD64. So mixxx won't detect jack :/

Solution: build your own portaudio deb:
([reference](http://forkbomb.dadacafe.org/blog/Squeeze_Mixxx_Jack_Portaudio_AMD64/))

    # apt-get source portaudio19  
    # apt-get build-dep portaudio19
    
    # cd /portaudio19-*/debian
    
    ####  ENABLE_JACK must be explicitely set to "yes" in debian/rules (line 48)
    # nano debian/rules
    
    # dpkg-buildpackage -rfakeroot -b
    
    # cd ../
    # dpkg -i *.deb

Now restart jack & mixxx.  
  
Now World domination :)

## Further Reading

  - [Compiling on an Asus eeePC](Compiling%20on%20an%20Asus%20eeePC)
  - [Mixxx on Fedora](Mixxx%20on%20Fedora)
