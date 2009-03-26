# Creating Backtraces for Debugging

## Linux and OS X Users

Found a crash? Generate us a backtrace:

1.  Run "gdb mixxx"
2.  When the gdb prompt appears, type "run".
3.  When Mixxx crashes, type the following into the gdb prompt: "thread
    apply all bt"
4.  Windows users can copy the terminal buffer by clicking on the
    Window's icon in the top left corner and then selecting
    *Edit*--\>*Select All*. Everything selected will be inverted (so if
    black becomes white, white becomes black, etc) and hitting *Enter*
    will copy the selection to the clipboard and unselect everything,
    then paste the clipboard buffer into a bug report, pastebin or
    notepad. *Note:* selecting in the terminal can suspend execution of
    application in Windows, a good thing to check if you find the app
    has stopped responding and you are running from a within a console
    window.
5.  Submit the bug using the [Mixxx bug reporting system on
    Launchpad](https://launchpad.net/mixxx). Bugs filed here are
    trackable by developers and will not fall through the cracks as
    easily as using the IRC channel or mixxx-devel. Make sure that the
    bug you are filing is new, and if you think that another bug might
    be the same one, post comments on it with your backtrace and any
    other useful info.
6.  If you do not want to use Launchpad, post the results in the forum,
    email them to mixxx-devel, or [pastebin](http://www.pastebin.ca)
    them and drop the link on IRC. We'll then try to figure out where
    the crash is. Do not assume a developer will hear you in IRC, using
    a static system (bug tracker, e-mail, forum) is much preferred. The
    IRC channel is great for technical support though.

**Note:** To get a backtrace for a thread freeze you can do the same
thing as above, but to get the gdb prompt, you have to press CTRL+Z in
the terminal window to suspend Mixxx.
