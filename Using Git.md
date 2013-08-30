# Using Git for Mixxx Development

Mixxx uses [Git](http://git-scm.com/) for source control. Git is a
distributed version control system that allows us to develop, share, and
maintain code easily. For code hosting, we use
[GitHub](https://github.com).

**[Click here to go to the Mixxx GitHub
repository.](https://github.com/mixxxdj/mixxx)**

A full guide for how to use Git is outside the scope of this article.
This article aims to get you up to speed with the basics of Git and we
are glossing over a lot of finer details about Git. We **strongly
suggest** you walk through this [introduction to Git by
GitHub](http://learn.github.com/p/) and [Pro
Git](http://git-scm.com/book), a free Creative Commons eBook about using
Git.

# Installing Git

You need to install Git to work with the Mixxx Git repository.

## Debian / Ubuntu

Install the `git` package from the software center or install it from
the command-line using `apt-get`.

    sudo apt-get install git

If you like you may install a additional GUI Tool.

Like

``` 
 * meld for a comparing revisions 
 * gitk for viewing history 
```

    sudo apt-get install meld
    sudo apt-get install gitk

## Windows

Download and install git from
[git-scm.org](http://git-scm.com/downloads/).

We recommend using [TortoiseGit](https://code.google.com/p/tortoisegit/)
on Windows since using the terminal on Windows is a giant pain.

## OS X

Download and install git from
[git-scm.org](http://git-scm.com/downloads/).

Alternatively, you may install it from a package manager for OS X such
as [Homebrew](http://mxcl.github.io/homebrew/) or
[MacPorts](http://www.macports.org/).

This is typically as easy as typing:

``` 
brew install git 
```

In a terminal.

# Cloning the Mixxx Repository

From the commandline, simply type:

    git clone https://github.com/mixxxdj/mixxx.git

This will clone the `master` branch by default which is where the latest
Mixxx code is developed.

If you would like to clone a specific branch, use the `-b` argument:

    git clone -b 1.11 https://github.com/mixxxdj/mixxx.git

This clones the `1.11` branch. You can view a web summary of the
available branches here on
[GitHub](https://github.com/mixxxdj/mixxx/branches).

Once the command succeeds, you will have a new folder (typically named
`mixxx`) in the current directory. Congrats, you've cloned the Mixxx
code repository to your local machine\!

# Committing Changes

**Important: First you need to set your name and email address. If you
don't do this then your commits will not be associated with your name
(or your account on GitHub) and you won't get the glory and recognition
you deserve\!** For your commits to be associated with your GitHub
account, make sure to use an email address that is associated with your
GitHub account.

    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"

Git is a little different from other version control systems you might
have tried. Before committing, you first have to tell it what changes
you want to "stage". You do this using the `git add` command. Once you
have staged your changes, you can issue a `git commit` (which will feel
familiar to `bzr` and `svn`)

    emacs src/engine/enginebuffer.cpp # Change enginebuffer.cpp
    git add src/engine/enginebuffer.cpp
    git commit -m "Bugfixes to EngineBuffer."

This commits the change locally only. In contrast to Bazaar and
Subversion, there is no concept of committing and automatically pushing
the changes to the remote repository in Git.

To automatically stage all changes that have been made to the repository
(i.e. every change that shows up in `git diff`) then you can use `git
commit -a`:

    emacs src/engine/enginebuffer.cpp # Change enginebuffer.cpp
    git commit -a -m "Bugfixes to EngineBuffer."

# Creating Patches

Once you've worked on fixing a bug or adding a feature to Mixxx, you may
want to generate a patch -- a file that represents the aggregate changes
you made. This is useful for posting the patch to our bug tracker or for
emailing it to someone, etc.

## Uncommitted Changes

Creating a patch of your uncommitted changes is as simple as running the
command `git diff`.

    git diff > my_changes.patch

`my_changes.patch` now contains the changes you made.

Note: In git-parlance, this is actually a patch of your "unstaged"
differences.

## Changes relative to the remote master branch

If you have committed your changes locally either to a personal branch
or to an existing branch like `master`, then you may be interested in
creating a patch of the changes in your branch relative to the remote
branch on GitHub. Doing this is also simple:

    git diff origin/master > my_changes.patch

`my_changes.patch` is now a patch of the changes (both committed and
uncommitted) in your branch relative to the `master` branch on GitHub.

# Using Branches

Local branches give you scratch space to work on new features and ideas
without having to commit on top of an existing branch (like the `master`
branch). This allows you to track ongoing development in the `master`
branch and delay having to merge with `master` until you are ready.

**To check what branch you are currently on:**

    $ git branch
    * master

**To create a new branch:**

    $ git checkout -b experimental
    Switched to a new branch 'experimental'
    
    $ git branch
    * experimental
      master

**To rename a branch:**

    $ git branch -m experimental expt
    
    $ git branch
    * expt
      master

**To switch between existing branches:**

    $ git checkout experimental
    
    $ git branch
    * experimental
      master
    
    $ git checkout master
    
    $ git branch 
      experimental
    * master

**To delete a local branch:**

    $ git branch -d experimental  # requires the branch is fully merged
    $ git branch -D experimental  # deletes the branch regardless of whether it is merged

# Issuing a Pull Request

Once you are done hacking up a new feature in your clone of the Mixxx
repository, it's time to get that branch merged into Mixxx. The standard
way we prefer you to submit branches is via GitHub pull requests.

1.  Create an account on GitHub.
2.  Push your branch to a forked version of the [Mixxx GitHub
    repository](https://github.com/mixxxdj/mixxx).
3.  Create a pull request from GitHub. 
4.  A Mixxx team member will review and comment on your pull request.
    Work with your reviewer to address their comments. 
5.  Once it receives an `LGTM` \[1\] then it will be merged into Mixxx\!

# Keeping Track of Updates from Other Developers

Sometimes there may be another developer you would like to keep track of
or regularly merge updates from.

Let's say I would like to keep track of `ywwg`, another GitHub user who
is working on Mixxx. First, add the developer's Git repository as a
remote to your repository.

    $ git remote add ywwg https://github.com/ywwg/mixxx.git

Adding a repository as a remote is a way to assign a shortcut name to an
external repository you would like to pull changes from or push changes
to. Adding a remote doesn't do anything but add the alias. Next, you
need to fetch the latest changes from `ywwg`'s repository.

    $ git fetch ywwg 
    remote: Counting objects: 1771, done.
    remote: Compressing objects: 100% (714/714), done.
    remote: Total 1522 (delta 1301), reused 1014 (delta 804)
    Receiving objects: 100% (1522/1522), 469.46 KiB, done.
    Resolving deltas: 100% (1301/1301), completed with 154 local objects.
    From https://github.com/ywwg/mixxx
     * [new branch]      1.11       -> ywwg/1.11
     * [new branch]      master     -> ywwg/master
     * [new branch]      master_sync -> ywwg/master_sync

Cool\! Now I have all of `ywwg`'s branches as remote heads in my
repository. We can confirm this by looking at the remote branch list.

    $ git branch -r
    ...
      remotes/ywwg/1.11
      remotes/ywwg/master
      remotes/ywwg/master_sync
    ...

Now, if I want to merge the latest changes from `ywwg`'s `master_sync`
branch, I can just merge them directly into my current branch.

    git merge ywwg/master_sync

Or, if I want to work on my own changes to master\_sync, I can create a
new local branch with `remotes/ywwg/master_sync` set as its "tracking
branch". This means that when you type `git pull` with no arguments,
your local `master_sync` branch knows to pull changes from `ywwg`'s
`master_sync` branch.

To checkout a branch as a tracking branch:

    git checkout -b master_sync --track ywwg/master_sync

Once you've made local changes you would like `ywwg` to accept, you can
submit a pull request to `ywwg` on GitHub or just contact him in person
to ask him to merge changes from your branch.

# GUI clients

Here's a list of graphical Git clients that Mixxx developers have
tested:

#### Cross-Platform

  - [SourceTree](http://www.sourcetreeapp.com/) - Is a free Mercurial
    and Git Client for Windows and Mac that provides a graphical
    interface for your Hg and Git repositories. (Tested by Jus on Mac)
  - [SmartGit/HG](http://www.syntevo.com/smartgithg/) - Is a full
    featured Git, Mercurial or SVN client for Windows, Mac and Linux. It
    is free for non-commercial use. (Tested by Jus on Linux)

#### Windows

#### Mac OS X

#### Linux

# Other Resources

Here are some handy and great guides to learning how to use Git.

  - [Typical workflow with GitHub on shared
    project](http://neval8.wordpress.com/2013/07/07/en-typical-workflow-with-github-on-shared-project/)
  - [Git Cheat Sheet](http://cheat.errtheblog.com/s/git)
  - [Pro Git -- the official Git book, free](http://git-scm.com/book)
  - [Git for Computer
    Scientists](http://eagain.net/articles/git-for-computer-scientists/)
    
  - [git ready -- git tips and tricks](http://gitready.com/)
  - [git
    stash](http://gitready.com/beginner/2009/01/10/stashing-your-changes.html)
    -- a command to temporarily store local changes to a "stash".
  - [A successful Git branching
    model.](http://nvie.com/posts/a-successful-git-branching-model/)
  - [magit -- an emacs mode for Git](https://github.com/magit/magit)
  - [Git Rebase](http://git-scm.com/book/en/Git-Branching-Rebasing) --
    An advanced Git technique for keeping a clean history.
  - [git - the simple guide](http://rogerdudler.github.io/git-guide/) --
    Just a simple guide for getting started with git

<!-- end list -->

1.  Looks Good To Me
