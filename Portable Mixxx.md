# Portable Mixxx

## Windows

Goal: to make a build option for the Windows target that will allow
Mixxx to be run from a USB, CD/DVD, network share or other removable
media type.

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

## Bare metal

Goal: to make a USB stick/CD image that boots into
[DSL](http://www.damnsmalllinux.org/),
[DSL-N](http://www.damnsmalllinux.org/dsl-n/) or [Tiny Core
Linux](http://tinycorelinux.com/) that contains Mixxx (and JACK and
FFADO if possible,) ready to run. The idea is that you can walk up to
any PC with your MixxxStixxx and music media (external HD, MP3 DVD,
etc.) and be up & running about a minute.
