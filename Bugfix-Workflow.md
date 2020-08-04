This is a brief step by step description about a typical workflow of
fixing a first Mixxx bug. Follow the links for more details.
- [Fork](https://help.github.com/articles/fork-a-repo) [Mixxx on GitHub](https://github.com/mixxxdj/mixxx)
- [Set up git for Mixxx](using_git) and [create a branch](https://neval8.wordpress.com/2013/07/07/en-typical-workflow-with-github-on-shared-project)
- [Build Mixxx](home#compile-mixxx-from-source-code)

## Choose a working environment

You can edit Mixxx's code in anything from a basic text editor to a
professional IDE (Integrated Development Environment.) We've had good
experiences with [Eclipse](eclipse), but some of our developers just use
text editors that handle multiple files and support syntax highlighting
such as [Kate](https://www.kde.org/applications/utilities/kate) or
[Notepad++](http://notepad-plus-plus.org/). If you're working from a
text terminal, [GNU Nano](http://www.nano-editor.org/) also supports
syntax highlighting, though it's not quite as thorough as many of the
graphical ones. See [Developer Tools](Developer%20Tools) for more
information.

## Adopt an easy bug on Launchpad

[List of bugs tagged as easy](https://bugs.launchpad.net/mixxx/+bugs?field.tag=easy&field.status%3Alist=CONFIRMED)

[More info about the Bug Tracker](launchpad_bugs)

## Study the code and debug it

Read the code to figure out what it is doing. Insert
[qDebug](http://doc.qt.io/qt-4.8/qdebug.html) statements to help
understand what is happening at specific points in the code. Note that
you must run mixxx with the `--debugLevel 2` argument to have all
debugging messages printed to the console.

## Ask for hints and help

Ask your questions or discuss your ideas on
[Zulip](https://mixxx.zulipchat.com) chat.

Some notes about the Mixxx Control interface:
[developer\_guide\_control](developer_guide_control)

## Fix it\!

Happy coding :-)

And don't forget to ask if you get stuck\!

## Issue a pull request

<https://help.github.com/articles/using-pull-requests>

You can open a pull request before your code is ready to be merged with
Mixxx to show others your code and ask for help, just make sure to say
that your code is not ready for merging when you open the pull request.

If your pull request changes the GUI, please include screenshots of your
changes.

## Fix issues from code review

This is the most annoying part. Because we are sometimes nit pickers ;-)
Don't take it personally if there are a lot of changes requested. Code
review is important to make sure that Mixxx continues to run reliably
and quickly. It is also important so that Mixxx remains maintainable so
we can keep making it better without having to make huge changes.

Be sure that you code follows the Mixxx [coding
guidelines](coding%20guidelines) to avoid extra work.

## Become a Mixxx Contributor

You have to sign a contributor agreement. We will contact you about it
in time.

## Fix is merged to Master

The Bug is fixed now and will be released with the next release cycle.

Your name will appear in the "About" box of Mixxx.
