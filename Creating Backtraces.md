## Linux and OS X Users

Found a crash? Generate us a backtrace:

1\) Run "gdb mixxx"

2\) When the gdb prompt appears, type "run".

3\) When Mixxx crashes, type the following into the gdb prompt: "thread
apply all bt"

4\) Paste the results in the forum, email them to mixxx-devel, or
[pastebin](http://www.pastebin.ca) them and drop the link on IRC. We'll
then try to figure out where the crash is.

**Note:** To get a backtrace for a thread freeze you can do the same
thing as above, but to get the gdb prompt, you have to press CTRL+Z in
the terminal window to suspend Mixxx.
