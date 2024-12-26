### Mixxx 

Mixxx is open-source software with a broad community encompassing performing musicians, amateur DJs, internet radio broadcasters and casual users. The Mixxx Wiki contains useful information for users, developers and artists. It covers first steps if you are new to DJing, has a hardware guide to learn about supported controllers, provides help so you don't get stuck when running into trouble and is a great resource for developers. 

Due to spam attacks, wiki editing has been restricted. However you are welcome to add information or change existing documentation. To do so, please send your suggestions by creating a new topic in the [Documentation Stream on Zulip](https://mixxx.zulipchat.com/#narrow/stream/109176-documentation).  If you find outdated, incorrect or incomplete information on the wiki, sending corrections would be very much appreciated.

## User Documentation

### Getting Started

  - [Beginner DJ Links](Beginner-DJ-Links.md)
  - [DJ Hardware Guide](Hardware-compatibility.md)
  - [Manual](https://mixxx.org/manual)
  - [Safeguard your Digital DJ Data](Safeguard-your-Digital-DJ-Data.md)

### Troubleshooting

  - [Troubleshooting](Troubleshooting)
  - [Finding the Mixxx.log file](Finding-the-Mixxx.log-file.md) can
    be helpful when Mixxx isn't working right. Please attach this file
    to bug reports and forum posts when asking for help.
  - [Adjusting Audio Latency](Adjusting-Audio-Latency.md)

### Getting Involved

  - [Reporting bugs](Reporting-bugs.md) is a great way to contribute to
    Mixxx, especially if you don't have programming skills
  - [Testing](Testing) the latest features helps speed up development 
  - [Getting Involved in Mixxx](Getting-Involved.md): Want Mixxx to be
    even more awesome? You don't need to be a programmer to help us.
  - [Google Summer of Code](https://github.com/mixxxdj/mixxx/wiki/Gsoc) 

### Extras

  - [Live GNU/Linux distributions featuring Mixxx](Portable-Mixxx.md):
    Run Mixxx from a USB drive or DVD without having to install anything
    on the computer
  - [Live Calls with Skype and
    Mixxx](https://www.primcast.com/support/live-calls-with-skype-and-mixxx/)
  - [MIDI clock output](MIDI-clock-output.md)

## Community Resources

  - [Mixxx website](https://www.mixxx.org)
  - [Development
    builds](https://downloads.mixxx.org/snapshots/main/): Please
    help us test the latest code and report bugs. We try to make sure
    code is reasonably stable before including it in these, but only use
    development builds if you are comfortable using bleeding edge
    software. Do not upgrade to a new version without adequate time to
    test it before a performance.
  - [List of open-source music production
    software](List%20of%20open-source%20music%20production%20software)

### Contributing

  - [Bug tracker hosted on Github](https://github.com/mixxxdj/mixxx/issues/)
  - [Internationalization](Internationalization): Help translate Mixxx
    into other languages
  - Source code is hosted on [GitHub](https://github.com/mixxxdj/mixxx)

### Communication

  - [Zulip chat](https://mixxx.zulipchat.com): Ask for help, chat with
    users and developers. Native apps can be [downloaded from Zulip's
    website](https://zulipchat.com/apps/) and configured to use the
    server mixxx.zulipchat.com, or use the [web
    app](https://mixxx.zulipchat.com/).
  - [Forums](https://mixxx.discourse.group/): Ask for help, listen to and share
    mixes, download and share controller mappings and skins
  - [mixxx-devel](https://lists.sourceforge.net/lists/listinfo/mixxx-devel)
    email list. Note that most project communication is on Zulip now, so
    you are more likely to get an answer to a question there.

## Controller Mapping Documentation

  - [MIDI controller mapping file
    format](MIDI%20controller%20mapping%20file%20format): create or
    change a MIDI mapping file for your controller
  - [MIDI crash course](MIDI-crash-course.md)
  - [Reverse engineering](Reverse-engineering.md) tips for DJ hardware
  - [Controller scripting with JavaScript](midi-scripting.md): map
    advanced behaviors including jog wheel scratching, modifier (shift)
    buttons, and deck toggle buttons
  - [Components JS](Components-JS.md): JavaScript library to help with
    writing mapping scripts
  - [Contributing mappings](Contributing-mappings.md): describes how to
    get your mapping included in Mixxx
  - [Controller mapping file
    locations](Controller%20mapping%20file%20locations)
  - [Updating controller mappings](Updating-controller-mappings.md):
    how to adapt old mappings for the latest version of Mixxx
  - [HID & USB Bulk controller mappings](hid-mapping.md): create or
    change a mapping for your HID or USB bulk-transfer mode controller
  - [Mixxx Controls](MixxxControls): List of Mixxx's controls that can
    be manipulated by controller mappings
  - [Controller mapping
    forum](https://mixxx.discourse.group/c/controller-mappings/10): search for
    mappings, share your mappings, and ask for help

## Skin Documentation

  - [Creating Skins](Creating-Skins) - the most up to date guide
  - [Skin Guidelines](Skin-Guidelines.md)
  - [Skin Color Scheme Architecture](Skin-Color-Scheme-Architecture.md)
  - [Skin Color Schemes Tips and Tool](Skin-Color-Schemes-Tips-and-Tool.md)
  - [On Icons and Images](On-Icons-and-Images.md)
  - [Skin System Changelog](Skin-System-Changelog.md)
  - [Skins forum](https://mixxx.discourse.group/c/skins/11): search for
    skins, share your skins, and ask for help

## Developer Documentation

### Compile Mixxx From Source Code

  - [Compiling on Linux](Compiling-on-Linux.md)
  - [Compiling on Windows](Compiling-on-Windows.md)
  - [Compiling on macOS](Compiling-on-macOS.md)
  - [Packaging / Making a Mixxx Installer](Packaging-Making-A-Mixxx-Installer)

### Getting Started

  - [Contribution Guidelines](Contribution-Guidelines.md)
  - [Coding Guidelines](Coding-Guidelines.md)
  - [Developer Guide](Developer-Guide.md): high level overview of Mixxx's
    architecture
  - [Developer Tools](Developer-Tools.md)
  - [Using Git](Using-Git.md)
  - [Bug & feautre request tracker](https://github.com/mixxxdj/mixxx/wiki/Mixxx-bugs-and-feature-requests)
  - [Bugfix Workflow](Bugfix-Workflow.md) 
  - [Creating Backtraces](Creating-Backtraces.md): helpful for debugging
    crashes
  - [Code profiling](Profiling) to see what parts of the code are using
    more CPU time than others
  - [Learning Resources](Learning-Resources.md)

### Development Topics

  - [Minimum requirements policy](Minimum-requirements-policy.md)
  - [Unit tests](Unit-tests.md) help prevent regressions. Writing tests
    is essential for new code\!
  - [Iconic Tracks](Iconic-Tracks.md) A list of tracks, useful for
    discussing Mixxx features
  - [Development Roadmap](Development-Roadmap.md)
  - [Feature Design Documents](feature-discussion.md)
  - [Google Summer of Code](gsoc) student projects and information.
  - [Google Code-in](gci) task list and information

### Specs

  - [Pitch percentages for semitones and
    notes](Pitch%20percentages%20for%20semitones%20and%20notes)
  - [Engine Library format](Engine-Library-format.md) (for Denon Prime
    hardware)

## Archives

  - [Press](Press) about Mixxx
  - [Developer meeting archives](meetings-archive.md)
  - Bazaar (legacy) code browsing on
    [Launchpad](https://code.launchpad.net/mixxx/+branches)
  - SVN (even more legacy) code browsing on
    [Sourceforge](https://mixxx.svn.sourceforge.net/viewvc/mixxx/)
  - [Blog](https://mixxxblog.blogspot.com)
