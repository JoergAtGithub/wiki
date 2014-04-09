# Reporting Bugs

If you think you've found a bug in the software, first make sure you're
using the latest version from www.mixxx.org, then **check the
[FAQ](FAQ), the [Troubleshooting](Troubleshooting) page and the
[forums](http://mixxx.org/forums)** to see if there is a known solution
or workaround or if other people are having the same problem.

If you don't find anything there, our bug tracking system is located at
<https://bugs.launchpad.net/mixxx>. First try a few searches on various
keywords related to the problem to see if it's already been reported and
what the current status is. If you find one or more that relate, click
change on "This bug doesn't affect me" to "vote" for the bug (you may
need to sign in to see this.)

If no existing bugs cover your issue, please gather the following
information:

  - Operating system (Windows, Linux, OSX, etc.) and version
  - CPU architecture (Athlon, Core 2 Duo, Celeron, Pentium II, etc.) and
    speed (in MHz or GHz)
  - Your video and sound hardware (Brands, models, options, etc.)
  - Steps to reproduce the problem
  - [Information logs](reporting_bugs#gathering_logs)

Much of the system information can be gathered from System Information
in Windows (found under Control Panel-\>Administrative Tools-\>Computer
Management-\>System Information,) and with the commands uname -a and
lspci -v on Linux.

## Gathering logs

Obtain the following information and add it as an attachment to your bug
report:

### Linux & Mac OSX

  - Most recent console output at the time of the error (About 50 lines
    or so.)
  - *[Back-traces](creating_backtraces)* from gdb are also extremely
    helpful. To capture one you need to install the gdb package (GNU
    Debugger), then from a console window run: `gdb --eval-command=run
    mixxx`Reproduce the crash mixxx and then type ***thread apply all
    bt*** at the *(gdb)* prompt and copy the lines from your terminal
    and paste them into the bug report.

### Windows

#### Mixxx.log

Find and attach this file to the bug. (Don't just paste it into the text
area because it's long\!) See the [Troubleshooting
FAQ](troubleshooting#where_is_the_mixxxlog_file) for information on
where it can be found.

#### Debugging Logs

If Mixxx crashes on you and you know how to reproduce the crash, please
do the following:

##### Ensure Windows Error Reporting is enabled

1.  Go to Start
2.  Select Control Panel
3.  Select Action Center
4.  Select Change Action Center settings
5.  Select Problem reporting settings
6.  Select Change report settings for all users
7.  Select Automatically check for solutions (Recommended)
8.  Select the Ok button to apply the settings

Now collect information from the following three sources:

##### Debug diagnostic tool

1.  Download & install the [Microsoft debug diagnostic
    tool](http://www.microsoft.com/en-us/search/DownloadResults.aspx?q=Microsoft+debug+diagnostic+tool&sortby=-availabledate)
    
2.  Start Mixxx from inside the tool (or attach it to a running Mixxx
    process)
3.  Make Mixxx crash
4.  Save the output from the debugging tool to a text file and attach it
    to your bug report

##### Event logs

1.  Go to Control Panel -\> Administrative Tools -\> Event Viewer
2.  Click Application Log and System Log. Make note of what the most
    recent event is in both.
3.  Start Mixxx, make it give the error
4.  Refresh the display of both logs (F5 key) and look at any new events
    logged (double click them.)
5.  Click the Copy button (looks like two pieces of paper)
6.  Paste the text into your bug report (do this for each new event
    logged since you started the program.)

##### Windows Error Reporting

*WER will automatically appear if an application crashes.*

1.  Click Send
2.  Click View Details
3.  Save the files to a folder of your choice
4.  Attach the files **WER*xxxx*.tmp.appcompat.txt** and
    **WER*xxxx*.tmp.version.txt** to your bug report. (*xxxx* is some
    number.) **Do not** include the .dmp file\! (You can just delete
    that since it's very large.)
