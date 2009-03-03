**Documentation available on our old wiki:**

<http://mixxx.sourceforge.net/wiki/index.php/HowtoBuildWin32>

Will move this over when I get a chance - Albert

Don't bother - Sean :P

-----

## Qt Creator Build Off of Trunk

The following is alternate way to build Mixxx from trunk using the [Qt
Creator IDE](http://www.qtsoftware.com/developer/qt-creator). It differs
from the normal way of building in that it uses qmake and minGW/GCC, but
does not depend on Python, SCons, or Microsoft Visual Studio.

### Steps

1.  Get the Qt Creator Bundle:
    [qtcreator-0.9.2-rc1-windows-bundle-setup.exe](http://www.qtsoftware.com/developer/qt-creator/qt-creator#qt-creator-binary-packages)
    \~390MB
2.  Get an SVN Client (i.e.
    [TortoiseSVN](http://tortoisesvn.net/downloads) -OR- [SilkSVN's
    Windows svn build](http://www.sliksvn.com/en/download) which can be
    used with Qt Creator's SVN plugin)
3.  Install both
4.  SVN check out *mixxx* and *mixxx-winlib* from trunk - repo is
    <https://mixxx.svn.sourceforge.net/svnroot/mixxx/trunk/>
5.  Open *mixxx.pro* inside Qt Creator which lives in the *mixxx* svn
    checkout you made in the previous step.
6.  Click on the *Projects* side button -\> *Run Settings* tab -\> type:
    `--resourcePath ../res` in the *Arguments* Box 
7.  Hit the green run (\>) button

You can track your progress approximately by your compiler warnings
count, a full uninterrupted build will produce \~8000 warnings. ^\_^ (If
the build fails only warnings after where it stopped will be shown on
the next compile run)

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
    <http://mixxx.org/packages/windows/mixxx-mingw-20090226-msvc-free.zip>,
    not an msi... but people can play with it.

### Tip: Debugging and Capturing Stacktraces on Windows

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
