## Build using Microsoft Visual Studio Express

(Currently the official way to build Mixxx on Windows, frequently
referred to as MSVC in discussions. (MicroSoft Visual C++))

//(Taken from
<http://mixxx.sourceforge.net/wiki/index.php/HowtoBuildWin32)//>

### Steps

1.  Download & install prerequisites

<!-- end list -->

  - [Microsoft Visual Studio C++
    Express](http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=f3fbb04e-92c2-4701-b4ba-92e26e408569#filelist)
    (2005 or later. You just need the vcsetup.exe file.)
  - [Microsoft Platform SDK 2003
    R2](http://www.microsoft.com/downloads/results.aspx?pocId=&freetext=platform%20sdk%20web%20install&DisplayLang=en)
  - [Qt 4.5 for Windows source
    package](http://download.qtsoftware.com/qt/source/qt-win-opensource-src-4.5.0.zip)
  - [Python](http://python.org/ftp/python/2.6.1/python-2.6.1.msi)
  - [SCONS](http://prdownloads.sourceforge.net/scons/scons-1.2.0.win32.exe)
  - An SVN or BZR client like
    [TortoiseSVN](http://tortoisesvn.net/downloads) or [Bazaar w/
    TortoiseBZR](http://bazaar-vcs.org/Download)

<!-- end list -->

1.  Get the source code

<!-- end list -->

  - Checkout the mixxx subversion repository:

<!-- end list -->

``` 
    * with TortoiseSVN: right-click in the folder you want to checkout to, choose SVN Checkout... and enter the following source: ''https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk''
    * with TortoiseBZR: right-click in the folder you want to checkout to, choose Bazaar Checkout/Branch... and enter the following source: ''lp:mixxx''
- Prepare build environment
  - Add to or create the following system environment variables ([[http://www.chem.gla.ac.uk/~louis/software/faq/q1.html|HowTo]],) adjusting the paths to match where you actually installed the above:<code>
```

QTDIR = C:\\qt\\4.5.0 INCLUDE =
C:\\MSVC2008\\VC\\Include;C:\\PSDK\\Include;C:\\DXSDK\\Include LIB =
C:\\MSVC2008\\VC\\Lib;C:\\PSDK\\Lib;C:\\DXSDK\\Lib\\x86 PATH =
C:\\qt\\4.5.0\\bin;C:\\Python26\</code\>

``` 
  - At the command prompt, change to the \bin subdirectory of your Visual C++ installation. Run "vcvars32.bat" to set the Path and Environment Variables for Command-Line Builds
  - Edit your C:\Program Files\Microsoft Visual Studio 8\Common7\Tools\vsvars32.bat and add to it:<code>
```

INCLUDE=C:\\Program Files\\Microsoft Platform SDK\\Include;C:\\Program
Files\\Microsoft Platform
SDK\\Include\\atl;C:\\qt\\4.5.0\\include;%INCLUDE% LIB=C:\\Program
Files\\Microsoft Platform SDK\\Lib;C:\\qt\\4.5.0\\lib;%LIB%\</code\>

1.  Build QT

<!-- end list -->

  - Start the MSVC command prompt and follow these instructions:
    <http://doc.trolltech.com/4.5/install-win.html>

<!-- end list -->

1.  Create the Visual Studio Project
    1.  Start the command prompt and change into your Mixxx source
        directory
    2.  Type `scons qtdir=C:\qt\4.5.0 msvc` (you may need to use
        `scons.bat` instead of just `scons`.) This will generate a
        Visual Studio project file called mixxx.vcproj.
    3.  Double-click the mixxx.vcproj file to open the project.
    4.  Open the Menu-\>Projects-\>Mixxx Properties... Dialog Go to the
        C/C++ -\> Preprocessor/Definitions Tab and add \_DEBUG to the
        preprocessor definitions. This lets you backtrace (debug) Mixxx.
2.  Build the project

<!-- end list -->

  - Press F7 to build the project

## Build using the Qt Creator SDK (easier)

The following is an alternate, currently experimental way to build Mixxx
from trunk using the [Qt Creator
IDE](http://www.qtsoftware.com/developer/qt-creator). It differs from
the normal way of building in that it uses qmake and minGW/GCC, but does
not depend on Python, SCons, or Microsoft Visual Studio.

### Steps

1.  Download & install the Qt SDK Bundle which includes Qt Creator:
    <http://www.qtsoftware.com/downloads/sdk-windows-cpp> \~200MB
    download. Requires \~2GB free space on your user profile drive for
    temporary unpacking, and \~2GB free on the target drive.
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

To create an Windows installer package from a debug build (which is
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
    <http://mixxx.org/packages/windows/mixxx-SVN2740M-20090321_2129-win.exe>
    installable package people can play with -G
  - Until the MSVC-free libraries are 100%, some users may need to
    install the Microsoft Visual C++ 2005 Redistributable Package from
    here (depending on which CPU architecture Mixxx was compiled for):
    [x86](http://www.microsoft.com/downloads/info.aspx?na=22&p=1&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=&u=%2fdownloads%2fdetails.aspx%3fFamilyID%3d200b2fd9-ae1a-4a14-984d-389c36f85647%26DisplayLang%3den),
    [x64](http://www.microsoft.com/downloads/info.aspx?na=22&p=4&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=&u=%2fdownloads%2fdetails.aspx%3fFamilyID%3deb4ebe2d-33c0-4a47-9dd4-b9a6d7bd44da%26DisplayLang%3den),
    [ia64](http://www.microsoft.com/downloads/info.aspx?na=45&p=1&srcdisplaylang=en&srccategoryid=&srcfamilyid=90548130-4468-4bbc-9673-d6acabd5d13b&u=details.aspx?familyid=526bf4a7-44e6-4a91-b328-a4594adb70e5&displaylang=en)

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
