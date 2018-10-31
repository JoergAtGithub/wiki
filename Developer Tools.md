# Graphical development tools

It is recommended to use an Integrated Development Environment that
works with C++. Mixxx is a large C++ project spread across many files.
Without an IDE that can help navigate around code split across multiple
files, it can be difficult to understand how the code fits together.

## Linux

  - Integrated Development Environments (IDEs):
    [KDevelop](https://www.kdevelop.org/),
    [Eclipse](http://eclipse.org/), [Qt
    Creator](http://wiki.qt.io/Category:Tools::QtCreator)
  - Text editors:
    [gedit](http://www.gnome.org/projects/gedit/screenshots.html),
    [kate](http://kate-editor.org/),
    [SciTE](http://www.scintilla.org/SciTE.html),
    [emacs](https://www.gnu.org/software/emacs/)
  - Git tools: gitk (comes with git),
    [git-cola](http://git-cola.github.io/),
    [gitg](https://wiki.gnome.org/Apps/Gitg/)

## Windows

  - Integrated Development Environments (IDEs):
    [Eclipse](http://eclipse.org/), [Qt
    Creator](http://wiki.qt.io/Category:Tools::QtCreator)
  - Text editors: [Notepad++](http://notepad-plus.sourceforge.net/),
    [emacs](https://www.gnu.org/software/emacs/)
  - Git tools: [Tortise Git](https://tortoisegit.org/), [Git
    Extensions](http://gitextensions.github.io/)

## macOS

  - Integrated Development Environments (IDEs):
    [Eclipse](http://eclipse.org/), [Qt
    Creator](http://wiki.qt.io/Category:Tools::QtCreator),
    [XCode](https://developer.apple.com/xcode/)
  - Text editors: [emacs](https://www.gnu.org/software/emacs/)

## Using IDEs

  - Set up [Eclipse](eclipse)
  - Set up [KDevelop](KDevelop)
  - Set up [Emacs](emacs)
  - Set up [QtCreator](QtCreator)
  - Set up [Xcode](Xcode)

# Debugging Tools

## GammaRay

[KDAB's GammaRay](https://www.kdab.com/gammaray) is a tool for
dynamically inspecting applications built with Qt. Its feature set is
too long to list, but of particular use for Mixxx development is:

  - The ability to see all current signals/slots being fired by Mixxx,
    with the ability to jump to the object that is firing them.
  - The ability to inspect the tree of all QObjects that exist, and for
    each object being able to see its properties, methods and
    inbound/output connections.
  - The ability to debug the render process of a QWidget, showing you at
    each step of a QPainter what the widget looks like, including
    performance details about each step.

## Debuggers

Debuggers allow you to inspect the state of Mixxx while its running (and
after Mixxx has crashed, via a core dump file).

  - [gdb](https://www.gnu.org/software/gdb/) (for gcc)
  - [lldb](https://lldb.llvm.org/) (for Clang)
  - Visual Studio (Windows-only)

## Profilers

See [profiling](profiling).

# Command-line Tools

## grep / ack / ag / ripgrep

`grep` is nice for searching files with regexes, but it isn't designed
specifically for looking through source code. There are a number of
tools that make searching through source repositories much nicer (e.g.
they won't go searching in the `.git` subfolder, or digging through
binary files for your regex).

  - [ack](https://beyondgrep.com/)
  - [ripgrep](https://blog.burntsushi.net/ripgrep/)
  - [ag / The Silver Searcher](https://geoff.greer.fm/ag/)
