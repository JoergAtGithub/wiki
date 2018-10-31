# Xcode

Xcode is a proprietary IDE developed by Apple.

## Creating an Xcode project.

If you want to work on Mixxx with XCode for an IDE:

This is taken from the Scons site, who have a pretty good description of
how to get a scons project up and running in XCode:

``` 
  - File->New Project->Mac OSX ->Others, choose "External Build System" \\ {{:compiling:xcode_scons_step_1.png|}}
  - Save the project into the same directory as your SConstruct file.
  - In Groups and Files -> Targets, double click the target that was automatically created.
  - Fill in the blanks, i.e. the full path to scons - like "/System/Library/Frameworks/Python.framework/Versions/2.3/bin/scons" or "/usr/local/bin/scons" \\ {{:compiling:xcode_scons_step_4.png|}}
  - You should now be able to build using the Build command from Xcode
  - Right click "Executables" and choose "Add new custom executable" and point it to the executable you are building and then you can debug using Xcode.
    - Note: In Xcode 4 there is no "Add new custom executable" option---you must instead edit the current scheme in order to choose an executable to run.  You can do this by clicking the project name in the upper-left corner of the window and choosing "Edit Scheme..." or by going to Product -> Scheme -> Edit Scheme.  In the edit menu you can also add arguments to be passed to the executable (such as a resource path) when it is launched.
  - Use Debug -> Breakpoints menu to add a symbolic breakpoint at main() - just type main where it says 'Double click for Symbol' - if you don't add this break point none of the breakpoints set in the editors will work, because gdb doesn't have the symbol information until you start debugging ([[http://www.cocoabuilder.com/archive/message/xcode/2006/8/15/8869|Jim Ingham suggests]] turning off "Lazy Symbol Loading" in Debug Preferences.)
```
