# Creating back-traces for debugging

Found a crash? Generate a back-trace so we can see exactly where Mixxx
crashed.

## Windows

1.  Download [GDB for
    Windows](http://www.equation.com/servlet/equation.cmd?fa=gdb) (get
    the official release version) and save it to the root of your C:
    drive. (`C:\`)
2.  Download a debug build of Mixxx (TODO)
3.  Open a command prompt by clicking Start-\>Run... then type `cmd` in
    the box and press Enter.
4.  Change to the the directory where Mixxx is installed: type the
    following then press Enter: `cd %PROGRAMFILES%\Mixxx`
5.  Run GDB: type the following command and press Enter: `C:\gdb
    mixxx.exe`
6.  Continue with the instructions below for all platforms

## Linux & Mac OS X with Xcode 4.x

1.  From a command prompt/terminal, type "gdb mixxx" and press Enter.

<!-- end list -->

  - **OSX users** need to specify the path for the executable file, e.g
    `gdb /Applications/Mixxx.app/Contents/MacOS/mixxx`
  - Use the gdb "--args" option to pass arguments, e.g. `gdb --args
    ./mixxx --controllerDebug --developer --resourcePath res`

<!-- end list -->

1.  When the gdb prompt appears, type "set height 0" and press enter to
    disable screen paging.
2.  Type "run" and press enter.
3.  Make Mixxx crash. When it does, type the following into the gdb
    prompt: "thread apply all bt". (There may be multiple pages of
    output. Make sure to hit \<Enter\> enough times to see it all.)
4.  To close the Mixxx window and end gdb, type the following into the
    gdb prompt: "quit"
5.  Copying the gdb info:

<!-- end list -->

  - **Windows users** can copy the terminal buffer by clicking the
    window's icon in the top left corner and then selecting
    *Edit*--\>*Select All*. Everything selected will be inverted (so
    black becomes white, white becomes black, etc) and hitting *Enter*
    will copy the selection to the clipboard and deselect everything.
    Paste the clipboard buffer into a notepad document and attach that
    to a bug report. *Note:* a Windows console will not update while any
    part of it is selected.
  - **Linux/OSX users** should be able to select terminal output by
    using the mouse, and then doing a right click and selecting *Copy*.

<!-- end list -->

1.  Submit the bug using the [Mixxx bug reporting system on
    Launchpad](https://launchpad.net/mixxx). Bugs filed here are
    trackable by developers and will not fall through the cracks as
    easily as using the IRC channel or mixxx-devel. Make sure that the
    bug you are filing is new, and if you think that another bug might
    be the same one, post comments on it with your backtrace and any
    other useful info.
2.  If you do not want to use Launchpad, post the results in the forum,
    email them to mixxx-devel, or [pastebin](http://www.pastebin.ca)
    them and drop the link on IRC. We'll then try to figure out where
    the crash is. Do not assume a developer will hear you in IRC, using
    a static system (bug tracker, e-mail, forum) is much preferred. The
    IRC channel is great for technical support though.

**Note:** To get a backtrace for a thread freeze you can do the same
thing as above, but to get the gdb prompt, you have to press CTRL+Z in
the terminal window to suspend Mixxx.

## Mac OS X with Xcode 5.x

Apple switched to clang/lldb. Xcode 5 does not include the GNU compiler
or tools.

1.  Open a terminal window.
2.  Specify the path for the executable file

<!-- end list -->

  - `lldb /Applications/Mixxx.app/Contents/MacOS/mixxx`
  - lldb output should read `Current executable set to
    '/Applications/Mixxx.app/Contents/MacOS/mixxx' (x86_64)`
  - If want to pass flag-like arguments to Mixxx, you have to terminate
    the actual flags with "--" `lldb -- ./mixxx --controllerDebug
    --developer --resourcePath res`

<!-- end list -->

1.  At the lldb prompt, type `run` and press enter.
2.  Make Mixxx crash.
3.  When it does, type the following into the lldb prompt: `thread
    backtrace all`
4.  To close the Mixxx window and end lldb, type the following at the
    lldb prompt: `quit`
5.  Copy the lldb output. Select the terminal output by using the mouse,
    and then doing a right click and selecting *Copy*

For more informations, go to <http://lldb.llvm.org/lldb-gdb.html>
