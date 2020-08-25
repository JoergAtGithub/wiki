# How to set up Eclipse for developing on Mixxx

Just some notes on how to setup Eclipse IDE for developing on Mixxx.

## Set up mixxx source

The default location on Linux would be

    ~/eclipse-workspace/mixxx

This guide assumes you have already setup you personal GitHub repository
as described [here](using_git). From you terminal or git shell
(Windows):

``` bash
mkdir eclipse-workspace # if not already exists 
cd eclipse-workspace
git clone https://github.com/YOUR-GITHUB-USER-NAME/mixxx.git
git remote add upstream https://github.com/mixxxdj/mixxx.git
```

Now have to setup the Mixxx source and manage to compile it via the
command line, as outlined here:
[compiling\_on\_linux](compiling_on_linux) or
[compiling\_on\_os\_x](compiling_on_os_x) or
[compiling\_on\_windows](compiling_on_windows) This may take up to 60
min on the fist time.

**Using Scons:**

``` bash
scons -j4 # replace 4 with the number of CPU cores that can be utilized 
```

**Using CMake (experimental):**

To save during comiling time after switching branches make sure ccache
is installed.

``` bash
mkdir build/Debug 
cd build/Debug
cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON ../.. 
cmake --build . -j4 # replace 4 with the number of CPU cores that can be utilized
```

**Test your build:**

``` bash
./mixxx
./mixxx_test
```

## Install Eclipse (packages or source)

Of course, install Eclipse and CDT (C/C++ developer toolkit). Either
simply from their homepage or use the packages for your operating
system.

It is best to install the ready to use setup **"Eclipse IDE for C/C++
Developers"**:

  - <http://www.eclipse.org/downloads/eclipse-packages/>

Or use the installer as described here

  - <https://askubuntu.com/questions/695382/how-to-install-eclipse-using-its-installer>

Or you might install the CDT into your existing eclipse

  - <http://www.eclipse.org/cdt/downloads.php>

Ubuntu Packages to install (possibly outdated) would be:

  - eclipse
  - eclipse-cdt

The latest Eclipse 2018-9 requires Oracle JDK 8 This can be installed on
Ubuntu like that:

``` bash
sudo apt-get install default-jre
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
# Oracle JDK 8 is activated by default you can switch between your Java installations using
sudo update-alternatives --config java
```

## Step-by-Step Setup

For Eclipse 2018-09

General:

  - Start Eclipse.
  - Window -\> Preferences
  - Expand General -\> Editors -\> Autosave 
  - Check Save automatically before build
  - Uncheck Build automatically 
  - Expand C/C++ -\> Indexer
  - Skip files larger than 80 MB
  - Skip include files larger than 160 MB 
  - Expand C/C++ -\> Build -\> console
  - Limit console output = 10000
  - Verify Project Explorer is visible. If not go to Window -\> Show
    View -\> Project Explorer
  - In the Project tree, right-click on the build folder and choose
    Properties
  - Check 'Exclude resource from build', Apply and Close
  - Repeat for the cache folder 

For Scons builds:

  - File -\> New -\> Makefile Project with Existing Code.
  - Set Project Name to `mixxx`.
  - Browse to your Mixxx folder e.g. `~/eclipse-workspace/mixxx`.
  - Check only C++ language (uncheck C).
  - Select Toolchain for indexer setting = `Linux GCC` (this would be
    for a Linux host, substitute your OS as applicable).
  - Finish.
  - Right click on the new project in Project Explorer -\> Properties
    -\> C/C++ Build 
  - Uncheck "Use default build command".
  - Build command 

<!-- end list -->

``` 
   * Linux ''scons faad=1 test=1'' 
   * Mac ''scons stdlib=libc++ hss1394=0 mad=0 coreaudio=1 test=1''
* Switch to Behavior tab.
* Build: remove ''all''.
* Clean: remove ''clean'' and set instead ''-c''.
* Check "Enable parallel builds".
* On Mac only: Expand C/C++ Build -> Environment
* Add the following Variable-Value pairs: <code>
```

CFLAGS | -I/usr/local/include -I/usr/local/include/opus CXXFLAGS |
-I/usr/local/include -I/usr/local/include/opus LDFLAGS |
-L/usr/local/lib QTDIR | /\<path to Qt install directory\>/%VERSION%
\#eg /usr/local/Cellar/qt5/5.10.1 \</code\>

  - Replace `%VERSION%` with the folder name for your version of Qt.
  - You may also have to manually add to the system PATH setting to
    include, for example, /usr/local/bin and /usr/local/include. Do this
    the same way as the above. Separate individual paths with colons.
  - To build with clang (recommended) rather than gcc add the below: `CC
    | clang 
    CXX | clang++
    `
  - Expand "C/C++ General" -\> "Preprocessor Include Paths, Macros etc."
  - Select Providers Tab -\> CDT GCC Build Output Parser
  - Set Compiler command pattern to
    `(g?cc)|([gc]\+\+)|(clang)|([clang]\+\+)`
  - Under 'Container to keep discovered entries' (you may need to expand
    the window for this to be visible) select 'Project (use when
    settings are the same for all files in the project)':

[[/media/outputparser.png|]]

  - Select "Providers Tab" -\> "CDT GCC Built-In Compiler settings" 
  - Uncheck "Use global providers ..."
  - Edit the command to `${COMMAND} ${FLAGS} -std=c++11 -E -P -v -dD
    "${INPUTS}"` 
  - Note: The indexer should work after a full rebuild that allows
    Eclipse to parse all compiler arguments.

For CMake Builds (experimental)

  - Install cmake4eclipse via the Eclipse Marketplace 
  - Help -\> Eclipse Marketplace...
  - search for cmake4eclipse and press Install. 
  - Follow the install Wizzard and restart Eclipse
  - File -\> New -\> Project... -\> C++ Project (\!**Not** File -\> New
    -\> C/C++ Project) 
  - Set Project Name to `mixxx`
  - Uncheck "Use default location"
  - Browse to your Mixxx source folder e.g. `~/eclipse-workspace/mixxx`.
  - Project Type: CMake driven -\> Empty Project
  - click Finish 
  - Right click on the new project in Project Explorer -\> Properties
    -\> C/C++ Build
  - Switch to Behavior tab.
  - Check "Enable parallel builds" and select "Use optimal jobs"

Now Mixxx should build within Eclipse with "Build Project" (Hammer
icon).

  - Right click on the new project in Project Explorer -\> Clean Project
  - Right click on the new project in Project Explorer -\> Build Project

**Set up Run:**

  - Run -\> Run configurations.
  - Select C/C++ Application.
  - Press "New launch configuration" button. 
  - Main tab:
  - C/C++ Application = `mixxx`.
  - Disable auto build.
  - Arguments tab 
  - Program arguments = `--resourcePath res --developer`
  - "Run" button for run Mixxx

**Set up Debug:**

  - Run -\> Debug configurations 
  - Next step similar to "Setup run"
  - Arguments tab 
  - Program arguments = `--resourcePath res --developer
    --debugAssertBreak`
  - For stepping through the Qt source, you need to place it in your
    workspace folder `cd eclipse-workspace
    apt-get source qtbase5-dev
    ln -s qtbase-opensource-src-5.2.1+dfsg qt5 # adjust version 
    sudo apt-get install qtbase5-dbg
    `
  - Non-Mac users should use GDB for debugging in Eclipse
    ([GDB](https://www.gnu.org/software/gdb/)).
  - Your `.gdbinit` should be setup before
    ```
    dir ~/eclipse-workspace/qt5/src/corelib
    dir ~/eclipse-workspace/qt5/src/corelib/io
    dir ~/eclipse-workspace/qt5/src/corelib/tools
    dir ~/eclipse-workspace/qt5/src/gui
    dir ~/eclipse-workspace/qt5/src/gui/image
    dir ~/eclipse-workspace/qt5/src/gui/kernel
    dir ~/eclipse-workspace/qt5/src/network
    dir ~/eclipse-workspace/qt5/src/sql
    dir ~/eclipse-workspace/qt5/src/sql/drivers/sqlite
    dir ~/eclipse-workspace/qt5/src/opengl
    dir ~/eclipse-workspace/sqlite/sqlite3-3.7.4
    dir ~/eclipse-workspace/portaudio/src/hostapi/alsa/
    
    python
    import sys
    
    sys.path.insert(0, '/home/<user_name>/eclipse-workspace')
    from qt import register_qt_printers
    register_qt_printers (None)
    end
    set print pretty 1
    set charset UTF-8
    ```

  - Qt pretty printer
    [qt.py](https://github.com/KDE/kdevelop/blob/master/plugins/gdb/printers/qt.py).
  - "Debug" button for run Mixxx.
  - Mac users running OS X 10.9 Mavericks or later are recommended to
    use LLDB for debugging. In recent versions of OS X, it is difficult
    if not impossible to get GDB working properly in Eclipse. LLDB seems
    somewhat problematic from within Eclipse, so debugging may be better
    done via Terminal.

For git integration (in case of using a git clone of mixxx):

  - Right click on the project in Project Explorer -\> Team -\> Share
    Project.
  - Select git.
  - Next -\> Finish.

## Additional hints

### Setting $DISPLAY

Some can get error "Warning \[Main\]: mixxx: cannot connect to X
server".

The general causes for this is that `DISPLAY` is not set in the
environment. So, go to Project properties -\> C/C++ Build -\>
Environment. Here you must add variable `DISPLAY` and set its value to
`${DISPLAY}`.

### Enable full power of Eclipse

This was tested without the SCons plugin installed.

#### Eclipse indexer

To enable the full power of Eclipse indexer Eclipse needs to know all
include files and symbols. Eclipse is able to discover path and symbols
from the scons output. After a build, you can check it at

Project -\> Properties -\> C/C++ General -\> Path and Symbols

by checking "Show built-in values"

This process does not always work perfectly. If the discovering fails,
you can help things along by adding the required info manually:

#### Linux

  - Right click on the project -\> Properties -\> C/C++ General -\> Path
    and Symbols -\> Fill in tabs "Includes" and "Symbols".
  - Add the src/ folder in your workspace, and select "add to all
    languages" and "add to all configurations."
  - Add the lib/ folder. Again, add to all languages and configurations.
  - Also add /usr/include as a filesystem path.
  - Also add:
  - /usr/include/qt4
  - /usr/include/qt4/Qt
  - /usr/include/qt4/QtCore
  - /usr/include/qt4/QtGui

<!-- end list -->

  - If you are using Qt5:
  - /usr/include/qt5/Qt 
  - /usr/include/qt5/QtCore
  - /usr/include/qt5/QtWidgets
  - /usr/include/qt5/QtGui
  - /usr/include/qt5/QtTest
  - /usr/include/qt5/QtXml
  - /usr/include/qt5/QtSvg

After changing these settings, the index needs to be rebuilt. Eclipse
will usually detect that changes have been made to Symbols settings and
will rebuild the index on clicking Apply and Close. To do it manually:

Right-click in Project Explorer Pane -\> Index -\> Rebuild

Troubleshooting:

The indexer preferences can be set here:

Window -\> Preferences -\> C/C++ -\> Indexer

You may set "Heap Size" to 20 % and "Absolute Limit" to 100 MB

#### macOS

  - Right click on the project -\> Properties -\> C/C++ General -\>
    Paths and Symbols
  - Under the 'Includes' tabs, choose GNU C++ and add:
  - /usr/local/include
  - ${QTDIR}/include
  - ${QTDIR}/include/QtCharts
  - ${QTDIR}/include/QtConcurrent
  - ${QTDIR}/include/QtCore
  - ${QTDIR}/include/QtGui
  - ${QTDIR}/include/QtNetwork
  - ${QTDIR}/include/QtOpenGL
  - ${QTDIR}/include/QtScript
  - ${QTDIR}/include/QtScriptTools
  - ${QTDIR}/include/QtSql
  - ${QTDIR}/include/QtSvg
  - ${QTDIR}/include/QtTest
  - ${QTDIR}/include/QtWidgets
  - ${QTDIR}/include/QtXml

Note that the use of ${QTDIR} depends on you having set this variable
under Project Properties \> C/C++ Build \> Environment

After changing these settings, the index needs to be rebuilt. Eclipse
will usually detect that changes have been made and will rebuild the
index on clicking Apply and Close. To do it manually:

Right-click in Project Explorer Pane -\> Index -\> Rebuild

Troubleshooting:

The indexer preferences can be set here:

Window -\> Preferences -\> C/C++ -\> Indexer

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
