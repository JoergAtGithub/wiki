\======= How to setup Eclipse for developing on Mixxx =======

Just some notes on how to setup Eclipse IDE for developing on Mixxx.

# Setup mixxx source

First you have to setup the Mixxx source and manage to compile it on
command line, as outlined here:
[compiling\_on\_linux](compiling_on_linux) or
[compiling\_on\_os\_x](compiling_on_os_x) or
[compiling\_on\_windows](compiling_on_windows)

# Install Eclipse (packages or source)

Of course, install Eclipse and CDT (C/C++ developer toolkit). Either
simply from their homepage or use the packages for your operating
system.

It is the best to install the ready to use setup **"Eclipse IDE for
C/C++ Developers"**:

  - <http://www.eclipse.org/downloads/>

Or you might install the CDT into your exiting eclipse

  - <http://www.eclipse.org/cdt/downloads.php>

Ubuntu Packages to Install (but possible outdated) would be:

  - eclipse-cdt
  - eclipse-pydev

# Step by Step Setup

For Eclipse Indigo (and Kepler)

  - Start Eclipse.
  - File -\> New -\> Makefile Project with Existing Code (or do import
    as described above).
  - Set Project name to your mixxx branch name e.g. `mixxx`.
  - Browse to your mixxx folder e.g. `~/workspace/mixxx/mixxx`.
  - Check only C++ language (uncheck C).
  - Select Toolchain for indexer setting = `Linux GCC` (in case of Linux
    host).
  - Finish.
  - Right click on the new project in Project Explorer -\> Properties
    -\> C/C++ Build (if Project Explorer is not visible, go to Window
    -\> Show View -\> Project Explorer).
  - Uncheck "Use default build command".
  - Build command = `scons`.
  - Switch to Behavior tab.
  - Built: remove `all`.
  - Clean: remove `clean` and set instead `-c`.
  - Check "Enable parallel builds".

Now Mixxx should build within Eclipse with "Build Project" (Hammer
icon).

**Setup Run:**

  - Run -\> Run configurations.
  - Select C/C++ Application.
  - Press "New" button. 
  - Main tab:
  - C/C++ Application = `mixxx`.
  - Disable auto build.
  - Arguments tab 
  - Program arguments = `--resourcePath res --developer`
  - "Run" button for run Mixxx

**Setup Debug:**

  - Run -\> Debug configurations 
  - Next step similar to "Setup run"
  - You `.gdbinit` should be setup before, but that's an other story.
  - Sample:
    [.gedbinit](http://bazaar.launchpad.net/~daschuer/mixxx/daschuers_trunk/view/head:/mixxx/.gdbinit).
  - Qt pretty printer
    [qt4.py](http://quickgit.kde.org/?p=kdevelop.git&a=blob&h=1373a79f38a359f4d0756e0bc7d14317311a16f8&f=debuggers%2Fgdb%2Fprinters%2Fqt4.py&o=plain).
  - "Debug" button for run Mixxx.

For git integration (in case of using a git clone of mixxx):

  - Right click on the project in Project Explorer -\> Team -\> Share
    Project.
  - Select git.
  - Next -\> Finish.

# Additional hints

## Setting $DISPLAY

Some can get error "Warning \[Main\]: mixxx: cannot connect to X
server".

The general causes for this is that `DISPLAY` is not set in the
environment. So, go to Project properies -\> C/C++ Build -\>
Environment. Here you must add variable `DISPLAY` and set its value to
`${DISPLAY}`.

## Enable full power of Eclipse

This was tested without the SCons plugin installed.

### Eclipse indexer

To enable the full power of Eclipse indexer Eclipse needs to know all
include files and symbols. Eclipse is able to discover path and symbols
from the scons output. After a build, you can check it at

Project -\> Properties -\> C/C++ General -\> Path and Symbols

by checking "Show build-in values"

If the discovering fails, you may add the required info manually:

  - Right click on the project -\> Properties -\> C/C++ General -\> Path
    and Symbols -\> Fill in tabs "Includes" and "Symbols".
  - Add the src/ folder in your workspace, and select "add to all
    languages" and "add to all configurations."
  - Add the lib/ folder. Again, add to all languages and configurations.
  - Also add /usr/include as a filesystem path.
  - Also add:
  - /usr/include/qt4/Qt
  - /usr/include/qt4/QtCore
  - /usr/include/qt4/QtGui

<!-- end list -->

  - If are you using Qt5:
  - /usr/include/qt5/Qt 
  - /usr/include/qt5/QtCore
  - /usr/include/qt5/QtWidgets
  - /usr/include/qt5/QtGui
  - /usr/include/qt5/QtTest
  - /usr/include/qt5/QtXml
  - /usr/include/qt5/QtSvg

<!-- end list -->

  - Alternative you can start with my project files (.cproject .project
    .gdbinit) and adapt them to your
    system:<http://bazaar.launchpad.net/%7Edaschuer/mixxx/daschuers_trunk/files/head:/mixxx/>

<!-- end list -->

  - Or merge from git@github.com:daschuer/mixxx.git

After changing these settings, The index needs to be rebuild

Project -\> C/C++ Index -\> Rebuild

### Eclipse code formatter

You should also configure the code formatter to Mixxx code style:
<http://www.mixxx.org/wiki/doku.php/coding_guidelines>

Right Click on the project -\> Properties -\> C/C++ General -\>
Formatter -\> Configure workspace settings

  - New -\> Profile name = `Mixxx` from Template K\&R
  - Indentation = Spaces only
  - New Lines = check before ....

### Other tweaks

You can improve the compile speed if you only enable required error
parsers

  - Preferences -\> C/C++ Build -\> Settings -\> Error Parsers 

To see the whole build in the Console tab

  - Preferences -\> C/C++ -\> Build -\> console
  - Limit console output = 10000
