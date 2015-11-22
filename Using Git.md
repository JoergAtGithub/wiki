# Using Git for Mixxx Development

Mixxx uses [Git](http://git-scm.com/) for source control. Git is a
distributed version control system that allows us to develop, share, and
maintain code easily. For code hosting, we use
[GitHub](https://github.com).

**[Click here to go to the Mixxx GitHub
repository.](https://github.com/mixxxdj/mixxx)**

# Tutorials

A full guide for how to use Git is outside the scope of this article.
This article aims to get you up to speed with the basics of Git and we
are glossing over a lot of finer details about Git. Git is an awesome
tool, but it can be confusing to learn, so we **strongly suggest** you
have a look at one of these tutorials. They are sorted according to the
time needed to complete them. The first one is the shortest.

1.  [git - the simple guide by Roger Dudler (in 14
    languages)](http://rogerdudler.github.io/git-guide/)
2.  [introduction to Git by
    GitHub](http://try.github.io/levels/1/challenges/1)
3.  [Ry's git Tutorial](http://rypress.com/tutorials/git/index)
4.  [Learn Git Branching](http://pcottle.github.io/learnGitBranching/)
5.  [Pro Git (the big manual)](http://git-scm.com/book)

All of these tutorials are interactive and guide you with helpful
graphics. Don't worry if you don't understand everything the first time.

# Installing Git

You need to install Git to work with the Mixxx Git repository.

## Debian / Ubuntu

Install the `git` package from the software center or install it from
the command-line using `apt-get`.

    sudo apt-get install git

If you like you may install a additional GUI Tools like:

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

This is typically as easy as running this in a terminal:

``` 
brew install git 
```

Download and install git from
[git-scm.org](http://git-scm.com/downloads/).

## IDE Plug-Ins

It is also helpful to use a IDE integrated Git GUIs.

``` 
 * [[eclipse]] has very advanced Git PlugIn [[http://www.eclipse.org/egit/|EGit]] bundled with the C/C++ edition of Eclipse 
 * [[qtcreator]] has built in support of Git (but be warned, it has is own opinion which files will be added to the Index)
 * [[KDevelop]] also has built in support of Git
```

# Cloning the Mixxx Repository

Note: If you plan fixing a bug or contributing a feature, you should
[fork](https://help.github.com/articles/fork-a-repo) the mixxx
repository on GitHub first. Replace "mixxxdj" with your user name in
following paragraphs.

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

# Using Branches

Branches give you scratch space to work on new features and ideas
without having to commit on top of an existing branch (like the `master`
branch). This allows you to work on multiple bugs/features in parallel
and independently propose them for inclusion in Mixxx whenever each one
is ready.

## Check what branch you are currently on

    $ git branch
    * master

## Create a new branch

    $ git checkout -b experimental
    Create a new branch called 'experimental' and switch to it
    
    $ git branch # show which branch you are on
    * experimental
      master

**Every time you start fixing another bug or working on a new feature,
switch back to the master or beta branch before starting your new
branch.** This will allow you to propose your new set of changes for
inclusion in Mixxx independently of what you were working on before. If
you do not do this first, when you make a pull request for inclusion in
Mixxx (see below), both what you were working on before and your new
changes will be included in the pull request.

## Switch between branches

    $ git branch
    * experimental
      master
    [make some changes in your IDE of choice]
    $ git stash # save uncommitted changes to git's temporary stash.
    # Do this if you have made edits that you are not yet ready to commit to the branch you are switching from.
    # If you have created new files, be sure to run 'git add' on them before running 'git stash'
    
    $ git checkout master # switch to the master branch
    
    $ git branch 
      experimental
    * master
    
    $ scons install # build latest version of master branch
    # see http://mixxx.org/wiki/doku.php/start#compile_mixxx_from_source_code for details
    $ mixxx # test new version of mixxx
    
    $ git checkout experimental
    $ git stash pop # reapply uncommitted changes from git's temporary stash
    [continue working on experimental branch and make commits when you are ready]

## Delete a local branch

    $ git branch -d experimental  # requires the branch is fully merged
    $ git branch -D experimental  # deletes the branch regardless of whether it is merged

# Committing changes

**Important: First you need to set your name and email address. If you
don't do this then your commits will not be associated with your name
(or your account on GitHub) and you won't get the glory and recognition
you deserve\!** For your commits to be associated with your GitHub
account, make sure to use an email address that is associated with your
GitHub account.

    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"

### Reviewing your changes

Running `git status` will show which files have changes that have not
been committed. Running `git diff` will show a color coded diff
comparing your uncommitted changes to the last commit made on that
branch. [\#GUI clients](#GUI%20clients) are helpful for this.

### Making the commit

Git is a little different from other version control systems you might
have tried. Before committing, you first have to tell it what changes
you want to "stage". You do this using the `git add` command. Once you
have staged your changes, you can issue a `git commit` (which will feel
familiar to `bzr` and `svn`)

    emacs src/engine/enginebuffer.cpp # Change enginebuffer.cpp
    git add src/engine/enginebuffer.cpp # Tip: pressing tab will only autocomplete file names of files that have changed.
    git commit -m "Bugfixes to EngineBuffer."

This commits the change locally only. In contrast to Bazaar and
Subversion, there is no concept of committing and automatically pushing
the changes to the remote repository in Git. If you omit the -m "COMMIT
MESSAGE" at the end, git will automatically open the editor specified in
your $EDITOR environment variable with a new file. Type your commit
message, then save this file in the editor to make the commit.

To automatically stage all changes that have been made to the repository
(i.e. every change that shows up in `git diff`) then you can use `git
commit -a`:

    emacs src/engine/enginebuffer.cpp # Change enginebuffer.cpp
    git commit -a -m "Bugfixes to EngineBuffer."

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

**NOTE: If you push new commits to a branch you have made a pull request
for, those commits will be included in the pull request.** To address
comments of reviewers, push new commits to the same branch that you
opened the pull request for. To work on a different bug or feature,
checkout the master or beta branch then create another branch so your
new changes are not included in the pull request that you already
opened.

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

# GUI clients

Here's a list of graphical Git clients that Mixxx developers have
tested:

#### Cross-Platform

  - gitk, comes with git
  - [Git Cola](http://git-cola.github.io/)
  - [Meld](http://meldmerge.org/) helps review diffs

#### Windows

  - [TortoiseGit](https://tortoisegit.org/)
  - [Git Extensions](http://gitextensions.github.io/)

#### Mac OS X

#### Linux

  - [GitG](http://freecode.com/projects/gitg)

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
