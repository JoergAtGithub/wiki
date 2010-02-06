How to compile in linux.

\-\> You need to uninstall mixxx if it's already installed.

**1. Download mixxx.**

``` 
 You need to install bazaar first.
 
 On ubuntu: sudo apt-get install bzr
 
 [[http://wiki.bazaar.canonical.com/Download]]
 
 
```

\-\> Download mixxx development branch using bazaar:

  - bzr co lp:mixxx

**2. Install mixxx dependencies**

  - scons
  - libid3tag
  - libmad
  - QT 4.4.0+ (if installing from packages, make sure to get
    libqt4-opengl and libqt4-svg too.)
  - libogg, libvorbis, libvorbisfile
  - libsndfile 
  - [PortAudio-v19](http://www.portaudio.com)
  - [PortMidi & PortTime](http://portmedia.sourceforge.net/portmidi)
  - [libmp4](http://www.mpeg4ip.net/) (or
    [libmp4v2](http://code.google.com/p/mp4v2/))
  - sqllite

**3. Compile mixxx and install.**

``` 
  \->Go to the directory where you downloaded mixxx.
 \->Change to the directory /mixxx/mixxx.
```

``` 
  Compile with scons:
   
       sudo scons prefix=/usr install
  
  You can also optimize for a particular CPU if you are using GCC 4.2 and above:
  
       sudo scons preix=/usr install **optimize=#**
  
  "#" depends on your CPU. You can optimize with the following:
  
  1:  single-core (P-III and below)
  2:  P4
  3:  Intel Core
  4:  Core 2
  5:  Athlon-4/XP/MP
  6: K8/Opteron/AMD64
  7:  K8/Opteron/AMD64 w/ SSE3
      
```

Here are step by step instructions for ubuntu studio.

[Compile in ubuntu studio, karmic
koala](Compile%20in%20ubuntu%20studio,%20karmic%20koala)
