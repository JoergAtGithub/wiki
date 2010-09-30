This page contains information on making portable versions of Mixxx to
use from a USB stick, LiveCD, etc.

# Windows

Goal: to make a build option for the Windows target that will allow
Mixxx to be run from a USB, CD/DVD, network share or other removable
media type.

**Update:** It looks like another group may have beaten us to it:
<http://www.winpenpack.com/main/download.php?view.828>

### TODO:

``` 
 * Avoid saving/reading settings & files to/from absolute paths
 * Settings directories:
   * Modify all locations of SETTINGS_PATH to not be prefixed with QDir::homePath(), but rather use CWD in place of home dir.   
     * Set SETTINGS_PATH to "Mixxx Settings".
 * Review all QWarnings, QCriticals and ASSERTS for write-fail scenerios
   * Fail writing operations gracefully (read-only media)... i.e. no QCrit on BPM Scheme write fail.
 * Library code changes:
    * Use relative file paths for all Music files that exist within the Music Folder [ConfigKey("[Playlist]","Directory")]:
```

``` 
       if exists (Music Folder + music path value) --> load // relative to music folder
       else if exists (music path value) --> load // not found, treat as absolute path 
```

# Bare metal

Goal: to make a USB stick/CD image that boots into
[DSL](http://www.damnsmalllinux.org/),
[DSL-N](http://www.damnsmalllinux.org/dsl-n/) or [Tiny Core
Linux](http://tinycorelinux.com/) that contains Mixxx (and JACK and
FFADO if possible,) ready to run. The idea is that you can walk up to
any PC with your MixxxStixxx and music media (external HD, MP3 DVD,
etc.) and be up & running in about a minute.

## MixxxOS

**Update: v1.1 is available for testing**

I'm proud to announce to you the new MixxxOS. MixxxOS is a minimal
Ubuntu 10.04 LTS base system including just enough to run Mixxx, copy
your files around and use the internet.

This release can be used as a livecd/usb but is also perfect for
installation on netbooks and tablets for it does not load a full desktop
but you can login right into Mixxx if you like, also the openbox window
manager is included as the "MixxxOS settings" session available on the
login screen, this session provides nice lightweight graphical tools to
configure the system, copy files and archives and install codecs,
updates or whatever you like. MixxxOS was build using
[Remastersys](http://www.geekconnection.org/remastersys/) wich is also
included on the cd so it's pretty simple to add extra software and
create a custom installable livecd.

Installation on a usb stick is also quite simple, there are two ways:

##### Live system on small USB key 500MB+

This is not really ideal for it does not save your settings but if you
include the audio codecs on the iso or only use flac and ogg files it's
a nice way to bring your old 512MB or 1GB stick back to use. Just
download [Unetbootin](http://unetbootin.sourceforge.net) for the OS of
your choice (included in most Linux distribution repositories) and
install. Next format your USB key and mount it. Open Unetbootin and
point it to the MixxxOS iso file and your USB drive and click install.
Nothing to it ;)

##### Full HD install on external USB disk or SD card

I've just tested this and it works great\!\! I had this 8GB slim USB key
laying around for a while now and wanted to use it with what has become
MixxxOS, here's what I did;

I used another USB key which I created whith Unetbootin to boot the
installer, you can also use a cd. Fill in al questions the installer
asks. For the user's login name choose mixxx, the real name may be
anything, this way you will keep the live cd settings afther
installation. At the disk partitioning choose the manual approach. Now
partition your USB drive, Be carefull to choose the right drive\!\!\!\!
watch size and filesystem type, it will probably be /dev/sdb or /dev/sdc
for sda is your internal drive. I've created a 3GB ext4 partition for /,
a 512MB swap and formatted the remaining space FAT32 and mounted it on
/home/music, this is the directory that is linked to the Music folder in
the user's home. Make sure before starting the install in the final
screen to check if the bootloader will be installed to the MBR of your
usb drive NOT THE MBR of sda\!\!\! If all goes well you'll end up with a
1.4GB installation that can be used on multiple computers.

##### HD installation

Just boot it up and install, it's easy as pie but for now use mixxx as
your login name otherwise you will not have the livecd settings afther
installation, the realname may be anything. If you like to set up a big
disk or partition for storing music you can mount it at /home/music, if
you like to create users you can simply link this folder in their homes
if you like.

#### Download

[MixxxOS 1.1
x86](http://dl.dropbox.com/u/4426037/MixxxOS/MixxxOS-1.1.iso)
[MD5SUM](http://dl.dropbox.com/u/4426037/MixxxOS/MixxxOS-1.1.iso.md5)
[Torrent](http://dl.btjunkie.org/torrent/MixxxOS-the-OS-created-for-digital-DJs/3676516823cbbc61916ec67214eaf0f8b7673f664c02/download.torrent)

Please use my [contact form](http://socialdefect.nl/contact/) (sorry I
get spammed a lot) or the mixxx forums to sent me bugs and feature
requests. Have fun, Socialdefect aka Arjan van Lent
