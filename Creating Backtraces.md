# Creating back-traces for debugging

Found a crash? Generate a back-trace so we can see exactly where Mixxx
crashed.

## Windows

1.  Download [GDB for
    Windows](http://www.equation.com/servlet/equation.cmd?fa=gdb) (get
    the official release version) and save it to the root of your C:
    drive. (`C:\`)
2.  Download Mixxx's debug symbol file:
    1.  32-bit: FIXME
    2.  64-bit: FIXME
3.  Open a Windows prompt: 

<!-- end list -->

  - Win 7: Open a command prompt by clicking Start-\>Run... then type
    `cmd` in the box and press Enter.
  - Win 10: Type `cmd` to the task bar search box and press Enter

<!-- end list -->

1.  Change to the the directory where Mixxx is installed: type the
    following then press Enter: `cd %PROGRAMFILES%\Mixxx`
2.  Run GDB: type the following command and press Enter: `C:\gdb
    mixxx.exe`
3.  Load optional debug symbols \*.pdb installed on your system.
    `add-symbol-file mixxx.pdb`
4.  Continue with step 2 in the section below 

## Linux & Mac OS X with Xcode 4.x

1.  From a command prompt/terminal, type "gdb mixxx" and press Enter.

<!-- end list -->

  - **OSX users** need to specify the path for the executable file, e.g
    `gdb /Applications/Mixxx.app/Contents/MacOS/mixxx`
  - Use the gdb "--args" option to pass arguments, e.g. `gdb --args
    ./mixxx --controllerDebug --developer --resourcePath res`

<!-- end list -->

1.  When the gdb prompt appears, type `set height 0` and press enter to
    disable screen paging.
2.  Type `run` and press enter.
3.  Make Mixxx crash. When it does, type the following into the gdb
    prompt: `thread apply all bt`. (There may be multiple pages of
    output. Make sure to hit \<Enter\> enough times to see it all.)
4.  To close the Mixxx window and end gdb, type the following into the
    gdb prompt: `quit`
5.  Copying the gdb info:

<!-- end list -->

  - **Windows users** can copy the terminal buffer into a text file:
    1.  Click the window's icon in the top left corner.
    2.  Choose *Edit*--\>*Select All*. Everything selected will be
        inverted (so black becomes white, white becomes black, etc)
        *Note:* a Windows console will not update while any part of it
        is selected.
    3.  Press *Enter* to copy the selection to the clipboard and
        de-select everything.
    4.  Paste the clipboard buffer into a Notepad text document.
    5.  Attach that to a bug report. (See below.)
  - **Linux/OSX users** should be able to select terminal output by
    using the mouse, and then doing a right click and selecting *Copy*.

<!-- end list -->

1.  [Report a bug](https://bugs.launchpad.net/mixxx/+filebug) using the
    [Mixxx bug reporting system on
    Launchpad](https://bugs.launchpad.net/mixxx/). Bugs filed here are
    tracked by developers and will not fall through the cracks as easily
    as using the IRC channel or mixxx-devel. (If another bug matches
    your issue, please make a comment on that one including your system
    details instead of filing a new bug.) Make sure to **attach** your
    back-trace (click *Add attachment or patch*.) Do not paste it in the
    comment.
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
