# Debian/Ubuntu Package Builder (pbuilder)

## Installation

    sudo aptitude -y install debhelper gnupg pbuilder # ubuntu packaging tools

## Permissions

It's a good idea to grant yourself "no password" sudo permissions on the
pbuilder stuff, so you are not required to type your password while
scons is running... this also makes it possible to run unattended builds
via cron or hudson, if those users are granted the privileges.

Edit your /etc/sudoers to contain at least:

    $USER    ALL=(ALL) NOPASSWD: SETENV: /usr/bin/debsign, /usr/sbin/pbuilder

where $USER is your login name of the user account that will do the
building

## Configuration

[pbuilder](https://wiki.ubuntu.com/PbuilderHowto) configuration files:

  - [[/media/x86_64-dot-pbuilderrc|.pbuilderrc for x86\_64]]
  - .pbuilderrc for i386, download the above file and commented out:
    ***export DEBIAN\_BUILDARCH=amd64*** by putting a \# in front of it

The configuration appropriate file for your build arch should be put
into ***$HOME*** of the build user as ***.pbuilderrc***

## Initializing pbuilder

``` 
 sudo /usr/sbin/pbuilder create
```

Whenever you update your .pbuilderrc file, its a good idea to also run:

``` 
 sudo /usr/sbin/pbuilder update
```

To update your pbuilder environment

## Building a Package

1.  [Build Mixxx using SCons](compiling_on_linux)
2.  next run: **scons -j2 makeubuntu** //\# -j for number of compiler
    threads, i.e. use -j4 if you have a quad core cpu //
3.  finally, if there were no errors, look for packages in the dist
    folder using: **ls ubuntu/mixxx-\*/dist/\*.deb**

## pbuilder Clean-Up

Recommended that you add the following to your root crontab to clean up
any failed builds, it will wipe out any pbuilder build environment over
a day old:

    20 1 * * * find /var/cache/pbuilder/build -maxdepth 1 -type d -mtime +1 -exec rm -rf {} \;

# OSX

It's not an installer, but it certainly is a package, and standard fare
for OSX. Get a .DMG with the .APP, and drag it to your /Applications.
Works as of 1.9+:

## Building a .DMG

see [Making a macOS DMG bundle](https://github.com/mixxxdj/mixxx/wiki/Compiling-on-macOS#build-mixxxapp-bundle-and-dmg-image)

# Windows

see [Making a Windows MSI installer package](https://github.com/mixxxdj/mixxx/wiki/Build-Windows-Installer)
