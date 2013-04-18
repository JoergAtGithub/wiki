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

  - bazaar plugin: <http://wiki.bazaar.canonical.com/BzrEclipse> and
    ***follow*** the instructions there on how to install and configure
  - you can then right-click on the eclipse project and select 'Team -
    Share Project...' and select bzr
