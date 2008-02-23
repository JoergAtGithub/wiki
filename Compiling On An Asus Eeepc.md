## eeePC

These are the compile instructions for building Mixxx on an eeePC. They
also work for (k)Ubuntu 7.10 and may also work for other Debian based
linux distributions.

For Debian / Ubuntu, you can ignore the lines to do with editing your
sources.list.

``` 
 MIXXX_HOME=`pwd`
 sudo aptitude purge mixxx mixxx-data # remove any potential conflicts with packaged versions
 
 # eeePC-only: Add this to sources.list: deb http://http.us.debian.org/debian stable main contrib non-free
 sudo aptitude install scons subversion libqt4-dev portaudio19-dev libmad0-dev libid3tag0-dev libvorbis-dev libsndfile1-dev g++
 
 # eeePC-only: remove from sources.list or you may accidentally upgrade to Debian/Etch: deb http://http.us.debian.org/debian stable main contrib non-free
 
 sudo aptitude update 
 
 # check out SVN work space for Linux
 svn co https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk/mixxx mixxx
 
 cd ${MIXXX_HOME}/mixxx
 scons # build with default options
 
 # create a symlink so mixxx can find skins/ and midi/ subdirs
 sudo ln -s "${MIXXX_HOME}/mixxx/src" "/usr/local/share/mixxx"
 
 # run it
 ./mixxx
```

``` 
 **# The block below is optional and only applies if you have a Hercules DJ Console Mk1/Mk2**
 
 sudo aptitude install libusb-dev # libDJConsole needs this
 
 ## eeePC-only: start##
 # apt-get/aptitude will remove libdjconsole*.deb during system updates, you'll need to reapply the last "dpkg --force-depends" step to get it back. 
 
 # libDJConsole stuff for Hercules Mk1/Mk2 support
 wget http://http.us.debian.org/debian/pool/main/libd/libdjconsole/libdjconsole-dev_0.1.2-3_i386.deb
 wget http://http.us.debian.org/debian/pool/main/libd/libdjconsole/libdjconsole0_0.1.2-3_i386.deb
 wget http://http.us.debian.org/debian/pool/main/libd/libdjconsole/libdjconsole-data_0.1.2-3_all.deb
 
 dpkg -i --force-depends libdjconsole-dev_*_i386.deb libdjconsole0_*_i386.deb libdjconsole-data_*_all.deb
 ## eeePC-only: end ##
 ## non-eeePC users can just 'sudo aptitude install libdjconsole0 libdjconsole-dev' instead of the eeePC-only section here.
 
 cd ${MIXXX_HOME}
 cd mixxx
 scons djconsole=1
```

**Seg Fault Note:** You will get a segmentation fault when running mixxx
after each recompile. This is caused by the UnionFS file system on the
eeePC. A reboot will allow you to run mixxx normally.

**Performance Note:** eeePCs should be configured to use `slow-mixxx` to
bump up the processing priority for reliable skip-free playback. Or get
the eee.ko kernel module to re-clock the CPU from 600Mhz -\> 900Mhz.

``` 
 #!/bin/bash
 # slow-mixxx         by ironstorm@users.sf.net 2008.01.17
 #   a script to start mixxx and renice it.
 #
 # Why we do it this way:
 #     i.   Must 'renice' after starting but before audio playback begins.
 #     ii.  Starting with 'nice' causes sound crackles on the eeePC
 #     iii. 'renice during playback causes skips and crackles on eeePC.
 
 # An stock eeePC runs at 630Mhz and needs nice priority of between -15 to -20 to playback with mimimal skipping, faster PCs can likely run at lesser priorities
 nice_priority=-18
 
 (sudo sleep 3; sudo renice ${nice_priority} `ps -C mixxx -o pid | grep -v PID`)& mixxx
```
