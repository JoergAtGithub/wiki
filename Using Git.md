# Using Git for Mixxx Development

Mixxx uses [Git](http://git-scm.com/) for source control. Git is a
distributed version control system that allows us to keep track of how
our code changes and work together on it. Our code is hosted on
[GitHub](https://github.com/mixxxdj/mixxx). This page aims to get you up
to speed with the basics of Git and how to use it with our workflow on
GitHub. We are intentionally glossing over a lot of finer details which
are explained in other [\#Tutorials](#Tutorials).

# Install Git

Git comes preinstalled on macOS and many GNU/Linux distributions. If
not, then install the `git` package through your distribution's package
manager. On Windows, download and install Git from
[git-scm.org](http://git-scm.com/downloads/). In addition to the command
line tool, there are lots of [GUI Git
Clients](https://git-scm.com/downloads/guis) available. Many IDEs have
some integrated Git functionality or have a plugin for using Git within
the IDE.

# Set up Git

First, [sign up for an account on GitHub](https://github.com/). Then, go
to the [mixxxdj/mixxx repository](https://github.com/mixxxdj/mixxx) and
click the "Fork" button in the top right. To download the Mixxx code,
run this command in your shell:

    git clone https://github.com/YOUR-GITHUB-USER-NAME/mixxx.git

Open the `.git/config` file in the new `mixxx` folder that was created
by the above `git clone` command with your favorite text editor. Copy
and paste the following lines at the top of the file:

    [remote "upstream"]
        url = git@github.com:mixxxdj/mixxx.git
        fetch = +refs/heads/*:refs/remotes/upstream/*
        fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*

This makes it easy to interact with the upstream [mixxxdj/mixxx
repository on GitHub's server](https://github.com/mixxxdj/mixxx). To
download the latest updates, run

    git fetch upstream

That will only download the updates though. To change the files on your
computer to match the latest updates, run

    git checkout upstream/master

to switch to the upstream master branch.

# Test a pull request

Developers propose changes to the Mixxx code by opening "pull requests"
on GitHub. The currently active pull requests are listed [on the GitHub
website](https://github.com/mixxxdj/mixxx/pulls). Testing these pull
requests and providing your feedback is really helpful and a great way
to start getting involved in Mixxx even if you don't know how to
program. To test a pull request, first download the latest updates:

    git fetch upstream

Find the number of the pull request from the [the GitHub
website](https://github.com/mixxxdj/mixxx/pulls), then run

    git checkout upstream/pr/PULL-REQUEST-NUMBER

to switch the code files on your computer to the proposed changes. Now
you can [start\#Compile Mixxx From Source
Code](start#Compile%20Mixxx%20From%20Source%20Code) to test the proposed
changes. Give feedback by commenting on the pull request on the GitHub
website.

# Create a new branch

When you are ready to start editing the Mixxx code, create a new Git
branch for your work. Git branches are a way to organize your changes
into separate workspaces, which allows you to work on multiple
bugs/features in parallel and independently propose them for inclusion
in Mixxx whenever each one is ready. **Every time you start fixing
another bug or working on a new feature, make a new branch** following
these steps:

First, download the latest updates before you start working on new
changes:

    git fetch upstream

Switch the files on your computer to the master branch from the upstream
repository:

    git checkout upstream/master

If you want your changes included in a current beta release or a bugfix
point release (such as 2.1.1), checkout the release branch instead of
the master branch, for example:

    git checkout upstream/2.1

Create a new branch on your computer called 'fixing\_some\_bug' and
switch to it:

    git checkout -b fixing_some_bug

Doing this every time you start working on a new feature or bug fix will
allow you to propose your new set of changes for inclusion in Mixxx
independently of what you were working on before. If you do not do this
first, when you make a pull request for inclusion in Mixxx (see below),
both what you were working on before and your new changes will be
included in the pull request.

# Commit changes

First you need to set your name and email address. If you don't do this
then your commits will not be associated with your name (or your account
on GitHub) and you won't get the glory and recognition you deserve\! For
your commits to be associated with your GitHub account, make sure to use
an email address that is associated with your GitHub account.

    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"

Also, configure Git to use the text editor of your choice. This will be
used when writing messages describing your commits:

    git config --global core.editor nano

### Review your changes

Running `git status` will show which files have changes that have not
been committed. Running `git diff` will show a color coded diff
comparing your uncommitted changes to the last commit made on that
branch. [\#GUI Tools](#GUI%20Tools) are helpful for this. When working
on code, you may end up trying some changes that you do not end up
needing. Reviewing your own code is helpful for making sure you only
commit the changes that are needed.

### Make the commit

Before committing your changes in Git, you first have to tell it what
changes you want to "stage" for inclusion in the commit. You do this
using the `git add` command. Once you have staged your changes, you can
use `git commit`

    emacs src/engine/enginebuffer.cpp # Change enginebuffer.cpp
    git add src/engine/enginebuffer.cpp # Tip: pressing tab will only autocomplete file names of files that have changed.
    git commit -m "Bugfixes to EngineBuffer."

If you omit the -m "COMMIT MESSAGE" at the end, Git will automatically
open the editor you have configured for Git. Type your commit message,
then save this file in the editor to make the commit.

Instead of using `git add` and `git commit`, you can use a [GUI Git
client](https://git-scm.com/downloads/guis) to pick what changes to
include in a commit. This is helpful for splitting a large set of
changes into smaller, independent commits, which makes it easy for other
developers to review your code.

# Push commits

When you make a commit in Git, that commit only exists on your computer
until you push it to a remote repository to share with others. To push
commits to another repository, configure the branch on your computer to
follow a branch in a remote repository. You can do this in one step
together with your first push:

    git push --set-upstream origin your_branch_name

This sets up your branch to push commits to the fork for your user on
GitHub's server. Once you have run this initial command, you can push
more commits on that branch by simply running `git push`.

# Open a pull request

When you are ready to propose the commits in your branch for inclusion
in Mixxx, first push your latest commits (refer to the sections above).
Then, go to the [upstream mixxxdj/mixxx repository on GitHub's
website](https://github.com/mixxxdj/mixxx). If you have pushed to your
fork recently, you will see a message prompting you to make a new pull
request. If you see that, click it. Otherwise, click the "New pull
request" button.

On the page for making a new pull request, click the link that says
"compare across forks". Leave the base fork as mixxxdj/mixxx. By
default, the base branch is the master branch, but if you want your
changes included in a release branch, be sure to select it here. For the
"head fork", select the fork for your GitHub user. Where it says
"compare", select the branch on your fork that you have been working on.
Write a title and description for your pull request. Scroll down to
check that the changes in the pull request only include the changes you
intend. When you are ready, click the "Create pull request" button.

A Mixxx team member will review and comment on your pull request. Work
with your reviewer to address their comments. To add new changes to your
pull request in response to review comments, add commits to the branch
on your computer and push them. When you push new commits, they will
automatically be included in the pull request you already have open.
When the changes are approved, we will merge them into the upstream
Mixxx code\!

To work on another bug or feature, [\#create a new
branch](#create%20a%20new%20branch).

# Merging new changes from upstream

If there have been new changes in the upstream code that you would like
to include in a branch you are working on, run:

    git checkout your_branch_name
    git fetch upstream
    git merge upstream/master

If you want to merge changes from a beta or release branch, change
`upstream/master` to that branch, for example `upstream/2.1`.

# Tutorials

A full guide for how to use Git is outside the scope of this article.
Git is an awesome tool, but it can be confusing to learn, so we
**strongly suggest** you have a look at one of these tutorials now that
you know the basics. They are sorted according to the time needed to
complete them. The first one is the shortest.

1.  [git - the simple guide by Roger Dudler (in 14
    languages)](http://rogerdudler.github.io/git-guide/)
2.  [introduction to Git by
    GitHub](http://try.github.io/levels/1/challenges/1)
3.  [Ry's git Tutorial](http://rypress.com/tutorials/git/index)
4.  [Learn Git Branching](http://pcottle.github.io/learnGitBranching/)
5.  [Pro Git (the big manual)](http://git-scm.com/book)

All of these tutorials are interactive and guide you with helpful
graphics. Don't worry if you don't understand everything the first time.

![https://imgs.xkcd.com/comics/git.png](https://imgs.xkcd.com/comics/git.png)

# Working on mappings and skins separately from other changes

If you are working on a mapping or skin and you want to work on other
changes to Mixxx at the same time, you can have both git branches open
simultaneously with git's handy [worktree
feature](https://git-scm.com/docs/git-worktree). This will let you use
your mapping or skin in development while testing your other branches.
If your git repository is at \~/software/mixxx, you can set this up for
a controller mapping by running:

    $ cd ~/software/mixxx
    $ git worktree add mapping your_mapping_branch_name
    $ echo mapping >> .git/info/exclude # Tell git to ignore your mapping branch when looking at ~/software/mixxx
    $ ln -s ~/software/mixxx/mapping/res/controllers ~/.mixxx/controllers

Now your mapping branch is open at \~/software/mixxx/mapping. This does
not have to be under \~/software/mixxx (in which case you can skip
adding the directory name to .git/info/exclude). You can work on your
mapping in \~/software/mixxx/mapping/res/controllers and make commits
when your current directory is \~/software/mixxx/mapping or any
directory under that. In \~/software/mixxx, you can work on any other
changes and switch between branches without affecting your mapping
branch open at \~/software/mixxx/mapping.

If you want to work on a skin, you can set up another git worktree and
run mixxx with the `--resourcePath` option set to the `res` directory
under that worktree.
