# Compiling mixxx on Ubuntu 7.10

I could have use the 1.6.0b2 binaries on my machine except for two
problems:

  - I wanted Hercules Control MP3 support
  - ubuntu gutsy PortAudio has a bug that prevents JACK AUDIO from
    showing as a sound API option

A simple compile-time option gets Hercules support. For the latter,
mixxx won't list Jack as a sound API choice unless `libdjconsole0` was
installed when PortAudio was compiled (distro error). Both of these are
easily fixed below.

(Additionally, Robin Sheat has kernel hacks to support the Herc LEDs,
which are not otherwise supported in mixxx at this time due to
system/driver complexities. See
<http://www.kallisti.net.nz/blog/2008/01/making-the-hercules-dj-control-mp3-work-with-mixxx>
which condenses the procedure for making the Hercules DJ Control MP3
work into one handy location. I have not done this.)

Mixxx just moved it's official site to www.mixxx.org, but the old site
has some decent hints at
<http://mixxx.sourceforge.net/wiki/index.php/SVN_Repository> I did start
with that; but one small step was missing.

You need to also fetch and compile the PortAudio package, included
below. PortAudio's compilation info is at
<http://www.portaudio.com/trac/wiki/TutorialDir/TutorialStart>.
Hopefully you can simply paste this crap into an xterm and have it work.

You only need to do this when changing from 1.5.x to 1.6.x, or probably
any major revision change.

    sudo apt-get purge mixxx mixxx-data

    sudo apt-get build-dep mixxx 
    sudo apt-get install subversion scons libqt4-dev

This will allow the soon-to-be-compiled PortAudio to offer JACK as an
option to mixxx.

    sudo apt-get install libjack-dev
    sudo apt-get install libdjconsole-dev

(I keep all my music related compilations in one place, \~/Music/Code
for clarity...)

    cd ~/Music/Code
    svn co https://www.portaudio.com/repos/portaudio/trunk
    cd v19-devel
    ./configure
    make
    make install

This step is missing from the mixxx docs, because real code developers
did this back in 1999 and forgot to tell the rest of us. It tells the
linking loaders (ergh, showing my age) where the new libraries can be
found:

Manually append to the end of file `/etc/ld.so.conf`:

    include /usr/local/lib

then

    ldconfig

That needs to be done *before* compiling mixxx\! Now to finally compile
mixxx...

``` 
cd ~/Music/Code
svn co https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk/mixxx
cd mixxx
sudo scons djconsole_legacy=1 install 
```

That should do it\!
