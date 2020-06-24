# Finding the mixxx.log file

Mixxx logs debugging information, [MIDI/HID/etc.
messages](command_line_options) it receives and script functions it
loads in the `mixxx.log` plain text file. When you [report a
bug](reporting%20bugs) or ask for help on the Mixxx forum or IRC
channel, please attach your `mixxx.log` file to help us help you.

  - **Linux:** \~/.mixxx/mixxx.log
  - **Windows:** `%LOCALAPPDATA%\Mixxx\mixxx.log` on Vista and up,
    `%USERPROFILE%\Local Settings\Application Data\Mixxx\mixxx.log` on
    XP and below. (You can just type either of those into the Location
    bar of a Computer or Folder window, or even under Start -\> Run...
    and press Enter.)
  - Note: The file may not show up as `mixxx.log` unless you've
    unchecked `Hide extensions for known file types` in the Windows
    Explorer folder options. Until then it is just `mixxx`, the only
    text file in that location (with a notepad icon.) By default in
    Windows 7 and up, extensions for known file types are set to hidden.
    See [How to show or hide file name extensions in Windows
    Explorer](http://support.microsoft.com/kb/865219).
  - **Mac OS X:** `/Users/<username>/Library/Application Support/Mixxx`
  - Note: The user library folder is hidden by default, so use one of
    the following methods to open the Mixxx folder.

<!-- end list -->

``` 
    * __Method A__:
    * In the Finder, choose Go > Go To Folder.
    * In the Go To Folder dialog, type ''~Library/Application Support/Mixxx''
    * Click Go.
    * __Method B__:
    * Hold down the Alt (Option) key when using the Go menu
    * The user library folder is listed below the current users home directory
    * Navigate to ''Application Support/Mixxx''
```
