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
  - Set up [QtCreator](QtCreator) for developing on Mixxx

You can also use [Qt Creator](http://qt-project.org/downloads) for Mixxx
development by creating a Qt project file for the source files. You can
do this by running `qmake -project` under Mixxx's root directory. When
using the created project file, you are able to use Creators editing
features such as following symbols (F2) and switching between code and
header files (F4). When compiling you will still have to resort to SCons
as the project file will not resolve the dependencies. To accomplish
this, switch to the project tab, remove any build steps and "Add Build
Step"-\>"Custom Process Step". Enter `scons` as Command and any
additional Command arguments (such as `qdebug=1` when in debug
configuration). Respectively, follow the same procedure for the Clean
Steps where you enter `-c` as Command argument.

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

# Console development tools

On Ubuntu Linux, G uses:

## grep (w/ color)

  - [grep](http://packages.ubuntu.com/hardy/grep)

<!-- end list -->

    export GREP_COLOR='1;33'
    export GREP_OPTIONS=--color=auto

## colordiff

  - [colordiff](http://packages.ubuntu.com/hardy/colordiff)

<!-- end list -->

    alias svndiff='(echo "Running SVN diff (your changes vs. the repo)..." && (svn -x -w diff|colordiff))|less -R'
    alias svnbasediff='(echo "Running SVN diff against BASE:HEAD (changes in the repo since last \"svn update\")..." && (svn diff -x -w -rBASE:HEAD|colordiff))|less -R'

  - diff -y with automatic adjustment for term width.

<!-- end list -->

    alias ydiff='y_diff'
    function y_diff() {
      diff --width=${COLUMNS} -b -y "$1" "$2" | colordiff | less -R
    }

## colormake and colorgcc

  - [colormake](http://packages.ubuntu.com/hardy/colormake) &
    [colorgcc](http://packages.ubuntu.com/hardy/colorgcc)

<!-- end list -->

    ### Color GCC
    if [ -z "`which colorgcc`" ]; then
      echo Installing ColorGCC ...
      sudo aptitude install colorgcc
    fi
    if [ ! -z "`which colorgcc`" ]; then
      export CC="colorgcc"
      alias gcc='colorgcc'
      for C in `grep /usr/bin /etc/colorgcc/colorgccrc | sed -e 's/# //' -e 's/:.*//'`; do
        if [ ! -e /usr/local/bin/${C} ]; then
          echo "Installing colorgcc wrapper in /usr/local/bin for ${C}... "
          sudo ln -s /usr/bin/colorgcc /usr/local/bin/${C}
        fi
      done
    fi
    ### Color Make
    if [ -z "`which colormake`" ]; then
      echo Installing ColorMake ...
      sudo aptitude install colormake
    fi
    if [ ! -z "`which colormake`" ]; then
      alias make='colormake'
      if [ ! -e /usr/local/bin/make ]; then
        sudo ln -s /usr/bin/colormake /usr/local/bin/make
      fi
    fi

## source-highlight

  - [source-highlight](http://packages.ubuntu.com/hardy/source-highlight)
  - Usage: 
  - vs somefile.cpp
  - vs SConscript

<!-- end list -->

    alias vs="view_source"
    function view_source {
      lang_def=""
      case "`basename $1`" in
        SConscript|SConstruct) lang_def=python.lang;;
        .bashrc|.bashrc-extra) lang_def=sh.lang;;
        # *) lang_def=cpp;;
      esac
      if [ ! -z "${lang_def}" ]; then lang_def="--lang-def=${lang_def}"; fi
    
      echo -e "\033]0;view-source: $1\007\c"
      source-highlight ${lang_def} --out-format=esc --output=STDOUT "$1" 2>/dev/null | less -RN
    }

## Nano editor

  - [nano editor](http://nano-editor.org) with color syntax highlighting

<!-- end list -->

  - Syntax color highlighting [.nanorc
    file](http://stacktrace.org/archive/.nanorc), you may have to run
    dos2unix on it.

<!-- end list -->

  - Usage: 
  - nano somefile.cpp:326:error: some compiler error message

<!-- end list -->

    alias nano='smart_nano'
    ## Smart nano jumps to a line number when you give it filename:nnn where nnn is the line number (like compile warnings/errors)
    function smart_nano() {
      if [ -z "$(echo \"$@\" | egrep [a-zA-Z0-9]:[0-9]+)" ]; then
        /usr/bin/nano -w -c "$@"
        return
      fi
      unset args
      echo
      while (( "$#" )); do
        if [ ! -z "${1}" ] && [ ! -z "`echo ${1}|cut -d: -f2|grep -e '^[0-9]*$'`" ]; then
          args[${#args[@]}]=+$(echo ${1}|cut -d: -f2|grep -e '^[0-9]*$') # Line Number Offset
          args[${#args[@]}]=$(echo ${1}|cut -d: -f1) # File Name
        elif [ -f "${1}" ]; then
          args[${#args[@]}]=$1
        else
          echo "Nano could not find: $1"; sleep .5
        fi
        shift
      done
      /usr/bin/nano -w -c "${args[@]}"
    }
