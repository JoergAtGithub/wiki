*(If you're looking to build the dependencies including Qt, [go to this
page](Build%20Windows%20dependencies).)*

*(If you're looking to make an installable release, [go to this
page](Build%20Windows%20installer).)*

## Build the 32-bit version using Microsoft Visual Studio Express

(Currently the official way to build Mixxx on Windows, frequently
referred to as MSVC in discussions.
(<span class="underline">M</span>icro<span class="underline">s</span>oft
<span class="underline">V</span>isual
<span class="underline">C</span>++))

### Steps

1.  Download & install prerequisites

<!-- end list -->

  - [Microsoft Visual C++
    Express](http://www.microsoft.com/express/download/) ([Direct link
    to 2008 w/
    SP1](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=f3fbb04e-92c2-4701-b4ba-92e26e408569#filelist).
    You only need vcexpress.exe.)
  - [Microsoft Windows 7
    SDK](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=c17ba869-9671-4330-a63e-1fd44e0e2505&displaylang=en)
  - [Qt library for Windows
    (MSVC2008)](http://qt.nokia.com/downloads/windows-cpp-vs2008)
  - [Python](http://python.org/download/) 2.x
  - [SCONS](http://www.scons.org/download.php)
  - A Bazaar client like [Bazaar w/
    TortoiseBZR](http://bazaar-vcs.org/Download) ([TortoiseBZR
    info](http://wiki.bazaar.canonical.com/TortoiseBzr))

<!-- end list -->

1.  Prepare build environment

<!-- end list -->

  - Add to or create the following system environment variables
    ([HowTo](http://www.chem.gla.ac.uk/~louis/software/faq/q1.html),)
    adjusting the paths to match where you actually installed the above
    `QTDIR = C:\Qt\4.7.4
    PATH = C:\Qt\4.7.4\bin;C:\Python26;C:\Python26\Scripts`
  - Open the Visual Studio command promt and type the following:`cd /D
    C:\Qt\4.7.4
    configure
    nmake`

<!-- end list -->

1.  Get the source code

<!-- end list -->

  - Checkout the mixxx repository: with TortoiseBZR, right-click in the
    folder you want to checkout to, choose Bazaar Checkout/Branch... and
    enter the following source:`lp:mixxx`

<!-- end list -->

1.  Get our precompiled dependencies

<!-- end list -->

  - Checkout the dependencies repository (and have it placed beside your
    "mixxx" directory)
    from:`lp:~mixxxdevelopers/mixxx/mixxx-win32lib-msvc90-release`

<!-- end list -->

1.  Build Mixxx:
    1.  Start the Microsoft Windows SDK v.7.0 command prompt (E.g. Start
        Menu\\Microsoft Windows SDK v.7.0\\CMD Shell) and change into
        the "mixxx" subdirectory of the checkout directory. (E.g.
        trunk\\mixxx)
    2.  Type `setenv /xp /x86 /release` and hit Enter.
    3.  Type `scons toolchain=msvs
        winlib=path_to_mixxx-win32lib-msvc90-release_directory` and
        press Enter. (You may need to use `scons.bat` instead of just
        `scons`.)
          - Add `msvcdebug=1` to build the debug version (with console
            output window.)
          - Add `win32=1` if you're on a 64-bit platform with 64-bit
            Python installed, otherwise it will try to build the x64
            version of Mixxx.
              - Note that this now seems to be `force32=1` in recent
                branches (1.10).
2.  Run it: When Mixxx is done compiling, run mixxx.exe in the
    "mixxx/dist32/" directory.
3.  (Optional) If you'd like to generate a MSVC project for use with
    Visual Studio, run `scons msvc`and open the newly generated
    "mixxx.vcproj" file with Visual Studio.

## Build the 64-bit version using Microsoft Visual Studio Express

### Steps

*(You may need to be running an x64/ia64 version of Windows, such as XP
Professional x64, Vista x64, Server 2003 x64 or 2008 x64, etc.)*

1.  Download & install prerequisites

<!-- end list -->

  - [Microsoft Visual Studio 2008 C++
    Express](http://www.microsoft.com/express/download/)
    ([Download](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=f3fbb04e-92c2-4701-b4ba-92e26e408569#filelist)
  - [Microsoft Windows 7
    SDK](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=c17ba869-9671-4330-a63e-1fd44e0e2505&displaylang=en)
    You only need to install the following:

<!-- end list -->

``` 
    * Vista Headers & x64 libraries
    * x64 C++ compiler
    * Debugging tools (optional, but recommended for troubleshooting)
    * Win32 Development Tools (I don't think you need this, but I'm not sure. I installed it just incase.)
* [[http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-4.6.1.zip|Qt source for Windows]]
* [[http://python.org/ftp/python/2.6.1/python-2.6.1.msi|Python]]...get the [[http://www.python.org/ftp/python/2.6.2/python-2.6.2.amd64.msi|AMD64 version]] if you want scons to auto-detect the fact that you're on a 64-bit platform (requires 64-bit OS,) otherwise you'll have to manually specify which version you want to build
* [[http://prdownloads.sourceforge.net/scons/scons-1.2.0.win32.exe|SCONS]]...get the [[http://prdownloads.sourceforge.net/scons/scons-1.2.0.zip|source]] if using the 64-bit Python and follow the piece-of-cake instructions in the README
* A Bazaar client like [[http://bazaar-vcs.org/Download|Bazaar w/ TortoiseBZR]]. Get the standalone version (unless you are a Python whiz since the 32-bit installer can't see the 64-bit Python installation.)
- Prepare build environment
  - Add to or create the following system environment variables ([[http://www.chem.gla.ac.uk/~louis/software/faq/q1.html|HowTo]],) adjusting the paths to match where you actually installed/unpacked the above:<code>
```

QTDIR = C:\\qt-everywhere-opensource-src-4.6.1 PATH =
C:\\qt-everywhere-opensource-src-4.6.1\\bin;C:\\Python26;C:\\Python26\\Scripts\</code\>

``` 
  - Follow the instructions [[http://whitemarker.blogspot.com/2006/12/c-visual-c-2005-express-edition-x64.html|on this page]] to configure VS C++ to use the x64 compiler, includes, and libs
- Build Qt. [[http://mixxx.org/wiki/doku.php/build_windows_dependencies#qt|Click here for details.]]
- Get the Mixxx source code
* Checkout the mixxx repository: with TortoiseBZR, right-click in the folder you want to checkout to, choose Bazaar Checkout/Branch... and enter the following source: ''lp:mixxx''
- Get our precompiled dependencies
* Checkout the dependencies repository with TortoiseBZR, using the following location: ''lp:~mixxxdevelopers/mixxx/mixxx-win64lib-msvc90-release''
- Build Mixxx
  - Start the Microsoft Windows SDK 7 command prompt (E.g. Start Menu\Microsoft Windows SDK v.7.0\CMD Shell) and change into the “mixxx” subdirectory of the checkout directory. (E.g. trunk\mixxx)
  - Type ''setenv /xp /x64 /release'' (or ''/ia64'') and hit Enter.
  - Type ''scons toolchain=msvs winlib=path_to_mixxx-win64lib-msvc90-release_directory'' (you may need to use scons.bat instead of just scons.)
    * Add ''msvcdebug=1'' to build the debug version.
    * Add ''win64=1'' if you installed the 32-bit version of Python to force a 64-bit Mixxx build (otherwise it will think you're on a 32-bit platform and build that version.)
    * If you get an error saying that it couldn't find PortAudio, do the following:
      - Edit C:\Python26\Lib\site-packages\scons-1.2.0\SCons\Tool\msvc.py
      - Comment out the ''def get_msvc_paths'' function (starts around line 536)
      - replace it with the following: <code>
      def get_msvc_paths(env, version=None, use_mfc_dirs=0):
  """Return a 3-tuple of (INCLUDE, LIB, PATH) as the values
  of those three environment variables that should be set
  in order to execute the MSVC tools properly."""
  exe_path = os.environ['PATH']
  lib_path = os.environ['LIB']
  include_path = os.environ['INCLUDE']
```

``` 
  return (include_path, lib_path, exe_path)</code>
      - Re-run ''scons'' and it should work.
* Once the build is finished, you will find everything needed to run Mixxx in the "dist" subdirectory of the checkout directory. Just double-click mixxx.exe and you're off.
```

#### If you'd like to generate an MSVC project for use with Visual Studio (optional)

1.  Start the SDK command prompt as above and change into the "mixxx"
    subdirectory of the checkout directory. (E.g. trunk\\mixxx)
2.  Type `scons msvc` (you may need to use `scons.bat` instead of just
    `scons`.) This will generate a Visual Studio project file called
    mixxx.vcproj.

<!-- end list -->

  - If you get an error saying that it couldn't find PortAudio, see
    above

<!-- end list -->

1.  Run the Visual C++ GUI from this command line to have it use the
    64-bit compile tools (e.g. `C:\Program Files (x86)\Microsoft Visual
    Studio 9.0\Common7\IDE\VCExpress.exe`)
2.  Open the `mixxx\trunk\mixxx\src\mixxx.vcproj` file.
3.  Follow the instructions [on this page
    again](http://whitemarker.blogspot.com/2006/12/c-visual-c-2005-express-edition-x64.html)
    to modify the default settings in the project to get it to build for
    x64.
4.  Open the Menu-\>Projects-\>Mixxx Properties... Dialog Go to the
    C/C++ -\> Preprocessor/Definitions Tab and add \_DEBUG to the
    preprocessor definitions. This lets you backtrace (debug) Mixxx.
5.  Press F7 to build the project

## MSVC Troubleshooting

  - If you get errors like `src\engine\ratecontrol.cpp(267) : error
    C3861: 'isnan': identifier not found` then you need to edit that
    source file and add the following at the top under the \#includes:
    `#ifdef _MSC_VER
    #include <float.h> // for _isnan() on VC++
    #define isnan(x) _isnan(x) // VC++ uses _isnan() instead of isnan()
    //#else
    //#include <math.h> // for isnan() everywhere else
    #endif`

## Build a 32-bit version using the Qt Creator SDK (easier)

The following is an alternate, currently experimental way to build Mixxx
from trunk using the [Qt Creator IDE](http://qt.nokia.com/downloads/).
It differs from the normal way of building in that it uses qmake and
minGW/GCC, but does not depend on Python, SCons, or Microsoft Visual
Studio.

### Steps

1.  Download & install the Qt SDK Bundle which includes Qt Creator:
    <http://qt.nokia.com/downloads/> \~200MB download. Requires \~2GB
    free space on your temp drive (change in user environment variables)
    for temporary unpacking, and \~2GB free on the target drive.
2.  Download & install an SVN or Bazaar Client (i.e.
    [TortoiseSVN](http://tortoisesvn.net/downloads) -OR- [SilkSVN's
    Windows svn build](http://www.sliksvn.com/en/download) which can be
    used with Qt Creator's SVN plugin)
3.  SVN checkout or BZR branch/checkout *mixxx* and *mixxx-winlib* as in
    the above instructions.
4.  Open *mixxx.pro* inside Qt Creator which lives in the *mixxx*
    directory you made in the previous step.
5.  Click on the *Projects* side button -\> *Run Settings* tab -\> type:
    `--resourcePath ../res` in the *Arguments* Box 
6.  Hit the green run (\>) button

You can track your progress approximately by your compiler warnings
count, a full uninterrupted build will produce \~8000 warnings. ^\_^ (If
the build fails only warnings after where it stopped will be shown on
the next compile run)

#### Making an Windows Installable Package

To create a Windows installer package from a debug build (which is
default):

  - Build and Run Mixxx from the above instructions so you have
    something to package
  - Install [NSIS](http://nsis.sourceforge.net/)
  - open a cmd window and go to your Mixxx directory (this is where your
    mixxx.pro file is found)
  - C:/Qt/QtCreator/mingw/bin/mingw32-make -f Makefile.Debug nsis
  - If everything works, you'll get an installable file with a name like
    mixxx-SVN**REV**-**YYYYMMDD**\_**HHMM**-win.exe (where REV is the
    SVN revision, YYYYMMDD - is year,month,day and HHMM is hour and
    minute at packaging time)

### Current Issues/Fixes TODO:

  - Implement a [safe NSIS
    uninstaller](http://nsis.sourceforge.net/Advanced_Uninstall_Log_NSIS_Header),
    currently the uninstall calls *RMDir /r /REBOOTOK $INSTDIR* as per
    the NSIS Help Manual example, this is problematic if users do
    something silly like put their music in there or install Mixxx into
    *My Documents* --\> very bad things would happen on an uninstall.
  - Fix the build script patch for PortAudio to enable ASIO when
    compiling with MinGW/qmake -\> see portaudio TODO (bottom of this
    page)
  - Update INCLUDEPATH to use the new libsndfile.h header
  - Recompile libsndfile with flac, ogg, & vorbis support
  - Figure out why application icon does not get linked.
  - \<del\>You need to change "*script/ui\_scriptstudio.h*" to
    "*ui\_scriptstudio.h*" on *scriptstudio.h* line \#5. - Why can't we
    use an \#ifdef to take care of this? And why are we compiling with
    scriptstudio on anyway? -S If you enable normal scripting, you get
    script studio, proper solution is to get all of the generated crap
    out of the src folder... but ifdef for MINGW may do for a quick
    workaround. -G \</del\> - using QMAKE ifdef to work around this
    now... yuck, but works. -G
  - ~~Package this MSVC-free version for distribution~~ --\>
    ~~[http://mixxx.org/packages/windows/](http://mixxx.org/packages/windows/?C=M;O=D)~~(Broken
    Link) \<- installable package people can play with -G
  - Until the MSVC-free libraries are 100%, some users may need to
    install the Microsoft Visual C++ Redistributable Package from the
    table on [this page](build_windows_installer#preparation) (depending
    on the CPU architecture for which Mixxx was compiled.)

### Tip: Debugging and Capturing Backtraces on Windows

My build setup is to keep my mixxx and mixxx-winlib directories inside
"My Documents". Unfortunately as I discovered, minGW's gdb can does not
initialize properly when the target application executable has spaces in
it's file paths. (*gdb C:\\mixxx\\bin\\mixxx.exe* = okay, *gdb
"C:\\Program Files\\mixxx\\bin\\mixx.exe"* = error 193)... Fortunately,
as Sean (Pegasus\_RPG) pointed out, Windows file paths can be mangled to
8.3 (you can see them by doing *dir /x*)

Here is the batch file I use to run gdb Mixxx from *C:\\Documents and
Settings\\**%USERNAME%**\\My Documents\\mixxx\\bin* (if your USERNAME
variable is not 8.3 remember find mangled equivalent by doing *dir /x
C:\\Documents and Settings\\*).

    @echo off
    REM gdb can not be run from a path that contains a space... otherwise you get (error 193)
    cd "C:\DOCUME~1\%USERNAME%\MYDOCU~1\mixxx"
    gdb -silent --eval-command=run --args bin\mixxx --resourcePath res

Once Mixxx is running in gdb, and you crash it... Jump to step \#3 of
[Creating Backtraces](creating_backtraces) and you'll be able to find
what line caused it or post the backtrace for dev team to look at.

### Tip: Reduce Disk Space Used by Qt

To cut down on the 2GB that Qt Creator install takes, You may want to
delete or zip-n-delete:

  - C:\\Qt\\QtCreator\\qt\\examples (\~600MB -\> zip to \~120MB)
  - C:\\Qt\\QtCreator\\qt\\bin\\QtWebKitd4.dll (\~230MB, Mixxx doesn't
    use WebKit yet -\> zip to \~30MB)
  - C:\\Qt\\QtCreator\\qt\\lib\\QtWebKitd4.dll (\~230MB 2nd copy)

### Tip: Optimize compilation

*Please fill these in, I don't know the answers\! -S*

To have Qt Creator tell the compiler to optimize for the processor
you're on, do:

1.  ?

To tell it to optimize for a particular processor, do:

  - For x86 (the default,) do nothing
  - For AMD64, 
  - For IA64, 
  - For Intel ATOM, 

### Optional: Building PortAudio in MinGW

1.  get Msys
    ([MSYS-1.0.10.exe](http://sourceforge.net/project/downloading.php?group_id=2435&filename=MSYS-1.0.10.exe)),
    install and configuring mingw (*C:/Qt/QtCreator/mingw*)
2.  download PortAudio snapshot from
    <http://www.portaudio.com/archives/pa_snapshot.tgz> to
    *C:\\msys\\1.0\\home\\%USERNAME%*
3.  download <http://trent.gamblin.ca/dx/dx9mgw.zip> to
    *C:\\msys\\1.0\\home\\%USERNAME%\\dx9mgw*
4.  Open an MSys window
5.  tar -zxvf pa\_snapshot.tgz && cd portaudio 
6.  patch portaudio with the
    *PA-Snapshot-20090222-mingw-DirectSound.patch* patch
7.  ./configure --with-winapi=directx --with-dxdir=../dx9mgw
8.  copy the contents of *portaudio\\lib\\.libs* to
    *mixxx-winlibs\\portaudio-snapshot\\minGW-bin*
9.  copy the contents of *portaudio\\include* to
    *mixxx-winlibs\\portaudio-snapshot\\include*

#### PA-Snapshot-20090222-mingw-DirectSound.patch

    \--- C:/msys/1.0/home/Administrator/portaudio-snapshot-clean/src/hostapi/dsound/pa_win_ds.c   Wed Jan 21 07:07:32 2009
    +++ C:/msys/1.0/home/Administrator/portaudio/src/hostapi/dsound/pa_win_ds.c   Sat Feb 21 23:36:13 2009
    @@ -95,8 +95,9 @@
     #include "pa_win_ds.h"
     #include "pa_win_ds_dynlink.h"
     #include "pa_win_waveformat.h"
    +#ifdef PAWIN_USE_WDMKS_DEVICE_INFO
     #include "pa_win_wdmks_utils.h"
    -
    +#endif
     
     #if (defined(WIN32) && (defined(_MSC_VER) && (_MSC_VER >= 1200))) /* MSC version 6 and above */
     #pragma comment( lib, "dsound.lib" )
    --- C:/msys/1.0/home/Administrator/portaudio-snapshot-clean/configure Thu Mar 06 12:14:06 2008
    +++ C:/msys/1.0/home/Administrator/portaudio/configure    Sat Feb 21 23:51:24 2009
    @@ -21410,10 +21410,10 @@
                 PADLL="portaudio.dll"
                 THREAD_CFLAGS="-mthreads"
                 SHARED_FLAGS="-shared"
    -            DLL_LIBS="${DLL_LIBS} -lwinmm -lm -L./dx7sdk/lib -ldsound -lole32"
    +            DLL_LIBS="${DLL_LIBS} -lwinmm -lm -L$DXDIR/lib -ldsound -lole32"
                 #VC98="\"/c/Program Files/Microsoft Visual Studio/VC98/Include\""
                 #CFLAGS="$CFLAGS -I$VC98 -DPA_NO_WMME -DPA_NO_ASIO"
    -            CFLAGS="$CFLAGS -I\$(top_srcdir)/include -I$DXDIR/include -DPA_NO_WMME -DPA_NO_ASIO" -DPA_NO_WDMKS
    +            CFLAGS="$CFLAGS -I\$(top_srcdir)/include -I$DXDIR/include -DPA_NO_WMME -DPA_NO_ASIO -DPA_NO_WDMKS"
             elif [ $with_winapi = "asio" ] ; then
                 if [ $with_asiodir ] ; then
                   ASIODIR="$with_asiodir"

#### TODO to get multiple windows sound APIs working:

  - download asiosdk2.2.zip
  - wimme, directsound, asio all at once patch (doesn't apply cleanly)
    --
    <http://www.nabble.com/configure-patch-for-MSYS-users-p20138278.html>

## Build a 64-bit version using Qt Creator & MingW64

***Experimental*** - Doesn't currently build because MinGW64 isn't
working correctly.

### Steps

*(You may need to be running an x64/ia64 version of Windows, such as XP
Professional x64, Vista x64, Server 2003 x64 or 2008 x64, etc.)*

1.  Download & install prerequisites

<!-- end list -->

  - [MingW64 binary tool chain](http://www.drangon.org/mingw/)

<!-- end list -->

``` 
    * Might need stuff from [[http://www.esnips.com/web/MinGW64?docsPage=1#files|here]] as well
* [[http://www.qtsoftware.com/downloads/qt-creator-binary-for-windows|Qt Creator for Windows]] (32-bit but works fine)
* [[http://qt.nokia.com/downloads/windows-cpp-vs2008|Qt source for Windows]]
* An SVN or BZR client like [[http://tortoisesvn.net/downloads|TortoiseSVN]] or [[http://bazaar-vcs.org/Download|Bazaar w/ TortoiseBZR]]
- Prepare build environment
  - Add to or create the following system environment variables ([[http://www.chem.gla.ac.uk/~louis/software/faq/q1.html|HowTo]],) adjusting the paths to match where you actually installed/unpacked the above:<code>
```

QTDIR = C:\\qt\\qt-win-opensource-src-4.5.1 PATH =
C:\\qt\\qt-win-opensource-src-4.5.1\\bin;C:\\mingw64\</code\>

1.  Tweak the Qt configuration
    1.  Edit
        qt-win-opensource-src-4.5.1\\mkspecs\\win32-g++\\qmake.conf:
        1.  Add to QMAKE\_CFLAGS: `-m64 -O3 -march=k8-sse3 -msse4.2
            -m3dnow -fomit-frame-pointer -ffast-math -funroll-loops` (or
            other optimization options as desired)
        2.  (optional) Add -Ox to QMAKE\_CFLAGS\_RELEASE for extra
            optimizations
    2.  Edit qt-win-opensource-src-4.5.1\\qmake\\makefile.win32-g++:
        1.  add to CFLAGS: `-m64 -O3 -march=k8-sse3 -msse4.2 -m3dnow
            -fomit-frame-pointer -ffast-math -funroll-loops` (or other
            optimization options as desired)
    3.  To avoid building the examples and demos (you don't need them
        and it saves ALOT of time,) edit
        qt-win-opensource-src-4.5.1\\projects.pro:
          - Remove "examples" and "demos" from QT\_BUILD\_PARTS toward
            the top of the file.
2.  Build Qt
    1.  Start a command prompt (Start-\>Programs-\>Accessories-\>Command
        Prompt)
    2.  Type `cd %QTDIR%` and hit Enter.
    3.  Type `configure -platform win32-g++ -no-webkit` and for more
        optimization, add `-mmx -3dnow -sse -sse2` & hit Enter.
    4.  When it finishes (about 5-10 minutes,) just type `mingw32-make`
        and press Enter and you should be good (takes 1\~3 hours.)
3.  Configure Qt Creator
    1.  Open Qt Creator
    2.  Go to Tools-\>Options-\>Qt4-\>Qt Versions
    3.  Click the plus sign
    4.  Enter something meaningful in the Name field like
        `4.5.1-x64-mingw`
    5.  Enter `C:\qt\qt-win-opensource-src-4.5.1` in the Path field
    6.  Enter `C:\mingw64` in the MinGw directory field
4.  Get the Mixxx source code

<!-- end list -->

  - Checkout the mixxx repository:

<!-- end list -->

``` 
    * with TortoiseSVN: right-click in the folder you want to checkout to, choose SVN Checkout... and enter the following source: ''https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk''
    * with TortoiseBZR: right-click in the folder you want to checkout to, choose Bazaar Checkout/Branch... and enter the following source: ''lp:mixxx''
- Build Mixxx
  - Open //mixxx-x64-mingw.pro// (found in the //mixxx// directory you made in the previous step) in Qt Creator
  - Click on the //Projects// side button -> //Run Settings// tab -> type: <code>--resourcePath ../res</code> in the //Arguments// Box 
  - Hit the green run (>) button
```
