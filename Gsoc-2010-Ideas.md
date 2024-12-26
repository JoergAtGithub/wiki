# Google Summer of Code 2010

These might be suitable for GSoC...

## Scalable User Interface

### Purpose

create a user interface that can be resized by grabbing corners...

### Benefits

  - Better use of increasingly diverse screen sizes (Mixxx runs on
    netbooks with resolutions of 800x480 all the way up to Desktops with
    resolutions of 2560x1600).
  - Reduce the number of duplicate skins (there are 5 variants of
    outline skin currently shipping with mixxx most copy the same
    artwork with different spacing or sizing).

### Possible approach(s)

  - Render Mixxx on an OpenGL canvas similar to way it's done in the Qt4
    demo: [Qt Widgets enter the third dimension:
    WolfenQt](http://www.youtube.com/watch?v=MXS3xKV-UM0).
  - Try to apply Qt4 SVG support to buttons and controls.
  - Investigate CSS stylesheets for helping make skin rendering more
    dynamic (i.e. using percentages for sizing and spacing).
  - Have an option to lock aspect ratio, so skin does not become
    distorted.

## Audio plug-in architecture

### Purpose

Build an audio plug-in framework to make Mixxx's audio engine more
modular and user extensible.

### Benefits

  - Increased modularity
  - 3rd parties could contribute input plug-ins by adhering to the
    proper api
  - 3rd parties could also bundle codecs that they have obtained
    licenses for the benefit of their users (if a hardware vendor wanted
    to ship Mixxx for example)
  - Users in locals where software patients do not apply can add
    plug-ins that can not be distributed in other locals.

### Possible approach(s)

  - Refactor the existing soundsourceproxy (and soundsourceMP3,
    soundsourceM4A, etc...) to make it into similar self-contained input
    plug-ins that can be loaded at runtime similar to that implemented
    as part of the [cmus](http://cmus.sourceforge.net/) project.
