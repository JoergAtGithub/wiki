# Compiling on Linux

Compiling Mixxx is fairly straightforward on Linux. The steps below
outline what to do in order to compile Mixxx.

## 1\. Install build dependencies

Mixxx relies on several external libraries for various features.

### Debian / Ubuntu

If your distribution is Debian based (such as Ubuntu), you can install
them by running:

    sudo apt-get build-dep mixxx 
    sudo apt-get install git scons libqt4-dev libqt4-sql-sqlite libportmidi-dev libshout-dev libtag1-dev libprotobuf-dev protobuf-compiler libvamp-hostsdk3 vamp-plugin-sdk libusb-1.0-0-dev libfftw3-dev libchromaprint-dev librubberband-dev
    sudo apt-get install libfaad-dev libmp4v2-dev # required for M4A support

### Fedora

On Fedora 19/20, you need enable the rpmfusion repo and then:

    su
    yum groupinstall "Development Tools"
    yum install scons git alsa-lib-devel qt4-devel libGL-devel libGLU-devel \
    libid3tag-devel libmad-devel libmp4v2-devel libsndfile-devel libvorbis-devel \
    portaudio-devel libshout-devel python-devel portmidi-devel qt-webkit-devel taglib-devel flac-devel \
    protobuf-devel vamp-plugin-sdk-devel \
    libchromaprint-devel rubberband-devel libusbx-devel

### Other

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
  - [faad2](http://www.audiocoding.com/faad2.html) (optional, for M4A
    file support)
  - libshout 
  - taglib
  - [protobuf](http://code.google.com/p/protobuf/) 
  - [vamp-plugin-sdk](http://www.vamp-plugins.org/develop.html)
    (**optional** if not installed, Mixxx uses an internal version)
  - [freeglut](http://freeglut.sourceforge.net/)
  - [librubberband](http://breakfastquay.com/rubberband/)
  - libchromaprint

## 2\. Get Mixxx

If you want to compile Mixxx, you'll need to download the source code.
Either grab the source for the latest release from our [downloads
page](http://www.mixxx.org/download.php), or checkout a snapshot from
our git repository: (See [Using Git](Using%20Git) for more details &
options.)

  - For the latest stable branch: `git clone -b 1.11
    https://github.com/mixxxdj/mixxx.git`
  - For the master branch: `git clone
    https://github.com/mixxxdj/mixxx.git`

## 3\. Compile and install

Once you have the source code, change to the newly created "mixxx"
directory, and use scons to compile. As a regular user, do:

    cd mixxx  # To enter the repository.
    cd mixxx  # (again) to enter the mixxx folder within the repository
    scons

(scons -h shows a complete list of build flags if you'd like to
customize.)

### Multi-threaded build

If you have a multi-core CPU (or just multiple CPUs) use **`scons -j`**
flag to specify the number of build threads to speed up building.
Generally, use as many threads as you have cores. (Note that if you have
a CPU with HyperThreading (which looks like two cores to the OS,) ignore
the extra apparent one\!)

So for example, if you have two dual-core CPUs for a total of four
cores, just do: **`scons -j4`**

If you have two single-core HT CPUs, do: **`scons -j2`** even though it
looks like you have 4 cores. (You don't. Specifying more threads will
only slow down the build.)

### Build with m4a/AAC file support

If you want to play m4a files, use **`scons faad=1`** flag.

Attention: You've to install the libraries faad2 and libmp4v2 (or
libmp4).

m4a/AAC support will be built as a plugin, which you'll need to load
with **`--pluginPath`** or by installing Mixxx (see below).

### Build without shoutcast support

If you don't want shoutcast support, use **`scons shoutcast=0`** flag.

### Run or Install

If you want to just run this copy without installing, from the same
directory, run: (WARNING this uses and may overwrite user-wide configs)

    ./mixxx --resourcePath res/

To also run from a different settings Folder use:

    ./mixxx --resourcePath res/ --settingsPath /*The folder you like*/

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

    git pull

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
  - [eclipse](eclipse)
  - [QtCreator](QtCreator)
