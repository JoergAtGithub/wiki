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

It is the best to install a ready to use setup:

  - <http://www.eclipse.org/downloads/>

Or you might install the CDT into your exiting eclipse

  - <http://www.eclipse.org/cdt/downloads.php>

Ubuntu Packages to Install (but possible outdated) would be:

  - eclipse-cdt
  - eclipse-pydev

# Optional Eclipse plugins

  - SCons plugin: 
  - See <http://sconsolidator.com> and ***follow*** the instructions
    there on how to install and configure. 
  - From Eclipse menu, you can use File -\> Import -\> C/C++ -\> New
    SCons project from existing source.
  - If you run into problems, please see:
    [Forum](http://www.sconsolidator.ch/projects/sconsolidator/boards)
    or
    [FAQ](http://www.sconsolidator.ch/projects/sconsolidator/wiki/FAQ)

<!-- end list -->

  - Eclipse GitHub plugin:
  - <http://eclipse.github.com/>

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

To enable the full power of Eclipse indexer you have to tell Eclipse
where to find the include files and symbols. Eclipse can discover it by
reading the compiler commands, but it is safer to do the job manual:

  - Right click on the project -\> Properties -\> C/C++ General -\> Path
    and Symbols -\> Fill in tabs "Includes" and "Symbols".

<!-- end list -->

  - Alternative you can start with my project files (.cproject .project
    .gdbinit) and adapt them to your
    system:<http://bazaar.launchpad.net/%7Edaschuer/mixxx/daschuers_trunk/files/head:/mixxx/>

### Eclipse code formatter

You should also configure the code formatter to Mixxx code style:
<http://www.mixxx.org/wiki/doku.php/coding_guidelines>

Right Click on the project -\> Properties -\> C/C++ General -\>
Formatter -\> Configure workspace settings

  - New -\> Profile name = `Mixxx` from Template K\&R
  - Indentation = Spaces only
  - New Lines = check before ....
