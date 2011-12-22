Just some quick notes on how to get the eclipse IDE together with its
bazaar plugin and scons plugin working.

# Install eclipse (packages or source)

Of course, install eclipse and CDT. Either simply from their homepage or
use the packages for your operating system.

Ubuntu Packages to Install would be:

  - eclipse-cdt
  - eclipse-pydev

for Unit testing:

  - libcppunit-dev

# setup mixxx source

If not done already you need to have a valid source directory of mixxx,
as outlined here: [compiling\_on\_linux](compiling_on_linux) or
[compiling\_on\_os\_x](compiling_on_os_x) or
[compiling\_on\_windows](compiling_on_windows))

# Eclipse plugins to install

  - scons plugin: <http://sconsolidator.com> and ***follow*** the
    instructions there on how to install and configure
  - From eclipse menu, you can use File-\>Import-\>c/c++-\>new scons
    project from existing source 
  - if you run into problems, please see:
    <http://www.sconsolidator.ch/wiki/sconsolidator/FAQ>

<!-- end list -->

  - bazaar plugin: <http://wiki.bazaar.canonical.com/BzrEclipse> and
    ***follow*** the instructions there on how to install and configure
  - you can then right-click on the eclipse project and select 'Team -
    Share Project...' and select bzr
