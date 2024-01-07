# Creating back-traces for debugging

Found a crash? Generate a back-trace so we can see exactly where Mixxx
crashed.

## Windows (using x64dbg)

x64dbg is an open-source x64/x32 debugger for Windows that runs without 
installation from any directory and supports the symbols file mixxx.pdb.

1.  Download x64dbg from [https://x64dbg.com/](https://x64dbg.com/)
    (when writing this we get snapshot\_2024-01-06\_21-29.zip)
2.  Extract the downloaded zip file into a directory of your choice. 
3.  Copy Mixxx's debug symbol file `mixxx.pdb` from the mixxx installation directory  
    `%PROGRAMFILES%\Mixxx\mixxx.pdb`  
    to the x64dbg symbols folder (create that directory if does not exist)  
    `snapshot_2024-01-06_21-29\release\x64\symbols`  
    **Note:** If mixxx.pdb does not exist you need to re-install Mixxx, select "Change"
    and enable "PDB debug files"
4.  Start x64dbg via double click on the bug icon of 
    * 64 bit: `snapshot_2017-03-19_13-21\release\x96dbg.exe`
    * Select x64dbg in the Launcher dialog       
      ![grafik](https://github.com/mixxxdj/mixxx/assets/64457745/24bcb5cb-4a17-4121-b923-90193e554bf5)
    * Uncheck all 'Break on' checkboxes in Menu -> Options -> Preferences -> Events
      ![grafik](https://github.com/mixxxdj/mixxx/assets/64457745/5f407eb1-b0cf-4861-adf7-10422419f838)

5.  Load mixxx.exe: File -\> open -\> browse to Mixxx.exe (F3) 
    * 64 bit: %PROGRAMFILES%\\Mixxx\\mixxx.exe
6.  Start and continue Mixxx: Debug -\> Run (F9)
7.  Make Mixxx crash. 
8.  When it does, Go to the Call Stack View: View -\> Call Stack
    (Ctrl+K)
9. Right Click: Copy -\> Full Table, To Log 
10. Go to the log: View -\> Log Window (Ctrl+L) 
11. Right Click: Copy 
12. [Continue below at 5.](#for-all-of-the-above)

## Linux & Mac OS X with Xcode 4.x


1.  Make sure you have the debug symbols installed. This is the case if you have build 
Mixxx yourselves like described here https://github.com/mixxxdj/mixxx/wiki/compiling%20on%20linux or if you have installed a debug symbol package via your package manager. If you are using a Mixxx version installed from our Launchpad PPA, you can install
the dbgsym package as follows (Make sure to replace `YOUR_UBUNTU_VERSION_HERE` with your Ubuntu version like `focal` and use the right ppa `mixxx`, `mixxxbetas` or `nightlies`): 

```
echo "deb http://ppa.launchpad.net/mixxx/mixxx/ubuntu YOUR_UBUNTU_VERSION_HERE main/debug" | sudo tee /etc/apt/sources.list.d/mixxx-ubuntu-mixxx-YOUR_UBUNTU_VERSION_HERE.list
sudo apt-get update
sudo apt-get install mixxx-dbgsym
```

2.  From a command prompt/terminal, type "gdb mixxx" and press Enter.

  - **OSX users** need to specify the path for the executable file, e.g
    `gdb /Applications/Mixxx.app/Contents/MacOS/mixxx`
  - Use the gdb "--args" option to pass arguments, e.g. `gdb --args
    ./mixxx --controllerDebug --developer --resourcePath res`

3.  [Continue below](#for-all-of-the-above)

## For all of the above

1.  When the gdb prompt appears, type `set height 0` and press enter to
    disable screen paging.
2.  Type `run` and press enter.
3.  Make Mixxx crash. When it does, type the following into the gdb
    prompt: `thread apply all bt full`. (There may be multiple pages of
    output. Make sure to hit \<Enter\> enough times to see it all.)
4.  To close the Mixxx window and end gdb, type the following into the
    gdb prompt: `quit`
5.  Copying the gdb info:

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

6.  [Report a bug](https://bugs.launchpad.net/mixxx/+filebug) using the
    [Mixxx bug reporting system on
    Launchpad](https://bugs.launchpad.net/mixxx/). Bugs filed there are
    tracked by developers and will not fall through the cracks as easily
    as posting them in the forum. (If another bug matches
    your issue, please make a comment on that one including your system
    details instead of filing a new bug.) Make sure to **attach** your
    back-trace (click *Add attachment or patch*.) Do not paste it in the
    comment.
7.  If you do not want to use Launchpad, post the results in the [Help & Suport forum](https://mixxx.discourse.group/c/support/6)

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

For more information, go to <http://lldb.llvm.org/lldb-gdb.html>


**Note:**

To debug a code-signed application on macOS, you need to turn off System Integrity Protection (SIP). This manifests itself in *lldb* error messages like ``error: process exited with status -1 (Error 1)``. For current state of SIP run ``csrutil status``. You can disable parts of SIP while leaving others enabled while booted into Recovery mode.  ``csrutil enable --without debug``

# Windows: creating a dump file

When reporting crashes on Windows in addition to the instructions above
for creating a backtrace, it is extremely useful if you can provide a
"dump" file. This contains important information about why Mixxx crashed
and will help the development team find a fix.

To take a crash dump, follow these instructions:

1.  When Mixxx crashes, you'll see a dialog similar to the following: 
    1.  [[/media/wincrashreport_windows_7.png|]]
2.  **Do not click "Close the program"\!**
3.  Hit the keys "control", "alt", and "delete" on your keyboard at the
    same time and click "Start Task Manager" on the screen that follows.
    
    1.  [[/media/start-task-manager.jpg|]].
4.  Find `mixxx.exe` in the list of programs, right-click it and hit
    "Create Dump File".
    1.  [[/media/create-dump-file.jpg|]]
5.  The dump file will be located on your computer in
    `%APPDATA%\..\Local\Temp\mixxx.dmp` or similar. 
    1.  **Tip:** You can copy/paste `%APPDATA%\..\Local\Temp\` into the
        start menu search box to open this folder.
6.  Upload `mixxx.dmp` (or whatever the file was called) to the bug
    report on the [Mixxx bug reporting system on
    Launchpad](https://bugs.launchpad.net/mixxx/).
7.  **Important:** Dump files must be matched to the exact version of
    Mixxx you are using. **A dump file is useless if we do not know the
    exact build number of Mixxx you are using and whether Mixxx is
    32-bit or 64-bit.**
    1.  To find the build number:
        1.  See Help -\> About inside of Mixxx and look for `gitXXXX`.
        2.  OR right-click mixxx.exe -\> Properties -\> Details -\> File
            Version and look for a number like `2.1.0.XXXX`
    2.  The easiest way to resolve all confusion is to provide us with
        the exact filename of the installer you used to install Mixxx
        (and the URL you downloaded it from if you know it). This will
        contain both the build number (`gitXXXX`) and whether the build
        is 32-bit or 64-bit.
