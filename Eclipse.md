Just some notes on how to setup Eclipse IDE for developing on Mixxx.

# setup mixxx source

First you have to setup the Mixxx source and manage to compile it on
command line, as outlined here:
[compiling\_on\_linux](compiling_on_linux) or
[compiling\_on\_os\_x](compiling_on_os_x) or
[compiling\_on\_windows](compiling_on_windows)

# Install eclipse (packages or source)

Of course, install Eclipse and CDT. Either simply from their homepage or
use the packages for your operating system.

It is the best to install a ready to use setup:

  - <http://www.eclipse.org/downloads/>

Or you might install the CDT into your exiting eclipse

  - <http://www.eclipse.org/cdt/downloads.php>

Ubuntu Packages to Install (but possible outdated) would be:

  - eclipse-cdt
  - eclipse-pydev

# Optional Eclipse plugins

  - scons plugin: 
  - <http://sconsolidator.com> and ***follow*** the instructions there
    on how to install and configure
  - From eclipse menu, you can use File-\>Import-\>c/c++-\>new scons
    project from existing source 
  - if you run into problems, please see:
    <http://www.sconsolidator.ch/wiki/sconsolidator/FAQ>

<!-- end list -->

  - Eclipse GitHub plugin:
  - <http://eclipse.github.com/>

# Step by Step Setup

For Eclipse Indigo

  - Start Eclipse
  - File \> New \> Makefile Project with Existing Code
  - Set Project name to your mixxx branch name e.g. mixxx
  - Brows to your mixxx folder e.g. \~/workspace/mixxx/mixxx
  - Ceck Language C++ (Uncheck C)
  - Select Toolchain for indexer setting = Linux GCC (in case of Linux
    host) 
  - Finish 
  - Right click on the new project in Project Explorer \> Properties \>
    C/C++ Build
  - Uncheck "Use default build command"
  - Build command = scons
  - Switch to Behaviour tab
  - Built: remove "all"
  - Clean: remove "clean" and set "-c"
  - check "Enable paralel builds" 

For git integration (in case of using a git clone of mixxx):

  - Right click on the project in Project Explorer \> Team \> Share
    Project
  - Select git 
  - Next \> Finish 

# Additional hints

This was tested without the scons plugin installed:

To enable the full power of Eclipse indexer you have to tell Eclipse
where to find the include files and symbols. Eclipse can dicover it by
reading the compiler commands, but it is saver to do the job manual:

Right Klick on the project \> Properties \> C/C++ General \> Path and
Symbols \> Register Card Includes/Symbols

Alternative you can start with my project files (.cproject .project
.gdbinit) and adapt them to your system. \*
<http://bazaar.launchpad.net/%7Edaschuer/mixxx/daschuers_trunk/files/head:/mixxx/>

You should also configure the code formatter to Mixxx code style:
<http://www.mixxx.org/wiki/doku.php/coding_guidelines>

Right Click on the project \> Properties \> C/C++ General \> Formatter
\> Configure workspace settings New \> Profile name = Mixxx from
Template K\&R Indentation = Spaces only New Lines = check before ....

Now you can setup run configurations: Menu Run \> Run configurations \>
New Icon C/C++ Application = mixxx Project = mixxx Arguments =
--resourcePath res --developer
