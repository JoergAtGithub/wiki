# Creating Backtraces for Debugging

## Linux and OS X Users

Found a crash? Generate us a backtrace:

1.  From a command prompt/terminal, type "gdb mixxx" and press Enter.

<!-- end list -->

  - **OSX users** need to specify the path for the executable file, e.g
    "gdb /Applications/Mixxx.app/Contents/MacOS/Mixxx"

<!-- end list -->

1.  When the gdb prompt appears, type "set height 0" and press enter to
    disable screen paging.
2.  Type "run" and press enter.
3.  When Mixxx crashes, type the following into the gdb prompt: "thread
    apply all bt".
    1.  There may be multiple pages of output. Make sure to hit
        \<Enter\> enough times to see it all.
4.  To close the Mixxx window and end gdb, type the following into the
    gdb prompt: "quit"
5.  Copying the gdb info:

<!-- end list -->

  - **Windows users** can copy the terminal buffer by clicking on the
    Window's icon in the top left corner and then selecting
    *Edit*--\>*Select All*. Everything selected will be inverted (so if
    black becomes white, white becomes black, etc) and hitting *Enter*
    will copy the selection to the clipboard and unselect everything,
    then paste the clipboard buffer into a bug report, pastebin or
    notepad. *Note:* a windows console will not update while any part of
    it is selected.
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
