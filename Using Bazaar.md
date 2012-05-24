# Using Bazaar

**[Official documentation](http://bazaar-vcs.org/Workflows)**

## GUI clients

Here's a list of graphical Bazaar clients that Mixxx developers have
tested:

#### Windows

  - [Bazaar w/ TortoiseBZR](http://bazaar-vcs.org/Download) - Works well
    in check-out mode. Distributed online mode is slow in large
    directories. (Tested by Pegasus)

#### Mac OS X

  - [Bazaar Explorer](http://wiki.bazaar.canonical.com/MacOSXDownloads)
    - Full featured desktop application providing an easy-to-use
    interface to the Bazaar version control system for MacOS 10.5+.
    (Tested by Jus)

<!-- end list -->

  - Launch Bazaar Explorer after install from the terminal with *bzr
    explorer*

#### Linux

  - Olive (bzr-gtk) - Looks promising but is god-awful slow on large
    directories like our src/ (Tested by Pegasus)

#### Cross-Platform

  - [QBzr](http://wiki.bazaar.canonical.com/QBzr) - QBzr provides GUI
    frontend for many core bzr commands and several universal dialogs
    and helper commands. Equivalents for core bzr commands has the same
    names as CLI commands but with prefix "q" (qlog, qcommit etc).
    Tested on linux, seems convenient sometimes if you are used to
    command-line workflow.

## List of available branches

<http://code.launchpad.net/mixxx>

## General procedure for distributed use

1.  **Create a personal copy** (called a "branch") of the Mixxx
    trunk/branch you want to work on using `bzr branch lp:mixxx` for
    trunk or `bzr branch lp:mixxx/1.8` for the 1.8 release branch. This
    copies the code to your local system. (**Be patient** as the Mixxx
    code base is fairly large and older versions of bzr sometimes have
    difficulty reporting progress.)
2.  **Make changes** to the code as desired. Every so often issue `bzr
    commit -m 'log message`' which will "commit" the changes to your
    local store, allowing you to review or revert later.
3.  To periodically **update** from the parent, issue `bzr pull`. If
    that gives you errors, (and it likely will if changes have been made
    to both) use `bzr merge` instead, since you're technically "merging"
    the parent repository with your local one.
4.  **Register a new personal branch** with Launchpad if you haven't
    already: <https://code.launchpad.net/people/+me/+addbranch>. You can
    create as many as you want, such as when working on different
    features. To create new branches on launchpad you can just \`bzr
    push lp:\~$USER/mixxx/$NEW\_BRANCH\_NAME\`.
5.  When you're ready to share with others, or if you're doing lots of
    local commits and want to prevent losing data, issue `bzr push
    lp:~<your-lp-name>/mixxx/<your-branch-name>` which actually copies
    your local store to your personal LP-hosted branch.
6.  When your branch is stable and ready for inclusion into trunk or the
    corporate branch, go to your branch's web page and click "**Propose
    for merging** into another branch" and fill in the form. You'll want
    to specify "mixxxdevelopers" as the reviewer. When you click the
    "Propose Merge" button, the Mixxx developers will be notified and
    will review & test your branch when they have a chance. They will
    then either merge it with the corporate code base or make notations
    on the proposal page with questions or suggested changes.

## General Procedure for Distributed Use With Push Access

If you have push/commit permissions on Launchpad and you are using
distributed mode (i.e. branches), **do not push from your local
branch**. Because of the way that Launchpad represents branch history,
this will cause the history view to bunch commits by others into single
commits by you from when you merge changes from upstream. The proper way
to work in this mode is to maintain two branches, a features branch, and
a clean branch. The following example will use the Mixxx 1.8 release
branch as an example.

1.  **Create a clean branch**: `bzr branch lp:mixxx/1.8 ./mixxx-1.8`
2.  **Create a features branch**: `bzr branch ./mixxx-1.8
    ./mixxx-1.8-features`
3.  **Add features/code to your features branch**: hack away at your
    features branch, and commit whenever you want at whatever interval
    you want. Ideally you will commit often with brief messages about
    what the commit did. These commit messages will not be displayed to
    everyone once you push the changes back to Mixxx. They will only
    show up if somebody decides they want to see the details of the
    commits you made for your feature branch. 
4.  **When you are ready to push the changes upstream**: from your clean
    branch (the `mixxx-1.8` folder): `bzr pull`, `bzr merge
    ../mixxx-1.8-features`. Now your branch is merged with the latest
    upstream changes, but it isn't committed yet. Resolve conflicts,
    compile Mixxx, run the test suite, and make sure that the feature
    and the upstream changes work well together.
5.  **Commit the merge of your feature branch**: `bzr commit --fixes
    lp:XXXXXX`. The commit message you enter here will be what the rest
    of the developers see. They will only see this message, the commit
    messages you made in your features branch will not be immediately
    available unless they drill-down into the merge on the history view.
    If you provide a `--fixes` argument to commit, then this will attach
    the launchpad bug \#XXXXXX to the branch you commit to (mixxx-1.8 in
    this case). 
6.  **Push the merged feature branch upstream**: `bzr push`

Your clean branch will represent the clean state of the remote Mixxx
codebase once you `bzr pull`, but your features branch will never update
unless you do it manually. **To bring your features branch up to date**:

1.  **Make sure your features branch does not have uncommitted
    changes\!**: This is very important, or you will end up committing
    your changes when you commit the merge, and you usually do not want
    to do this. You can easily temporarily put changes away by using
    `bzr shelve`, if you do not have it then you need to install
    `bzrtools`. `bzr shelve` is similar to `git stash`. 
2.  **Update your clean branch**: From your clean branch (the
    `mixxx-1.8` folder): `bzr pull`
3.  **Merge the upstream changes from your clean branch to your features
    branch**: From your features branch (the `mixxx-1.8-features`
    folder): `bzr merge ../mixxx-1.8`
4.  **Commit the merge**: Resolve any conflicts, and when you are done
    `bzr commit`. You usually will provide a commit message with
    something along the lines of `Merging changes from upstream.` This
    commit message will not show up when you push your changes to
    Launchpad using the guide above, since bzr will realize that the
    merge was applying patches that were already applied to the remote
    branch. 

## Making it work like SVN (a.k.a. Centralized Mode)

(For those of us scared of this "distributed" thing...)

  - **Check out** with `bzr checkout lp:mixxx` for trunk or `bzr
    checkout lp:mixxx/1.8` for the 1.8 release branch. (**Be patient**
    as the Mixxx code base is fairly large and older versions of bzr
    sometimes have difficulty reporting progress.)
  - **Update** to latest version with `bzr update`
  - **Create a patch** with `bzr diff > mychanges.patch` and attach it
    to a bug at [Launchpad](http://bugs.launchpad.net/mixxx).
  - If you have commit access, **commit** with `bzr commit -m "Log
    message"` (You'll need to register an SSH key first under your
    personal LP page: <https://launchpad.net/people/+me/+editsshkeys>.)

## Automatic submission to CIA

Mixxx has a CIA bot in our freenode channel that will dutifully announce
any commits to the codebase. To make this work for you, do the
following:

1.  Set up an account at <http://cia.vc/>
2.  Install your distribution's `cia-clients` package, or manually
    install the plugin from [the Launchpad project
    page](https://launchpad.net/bzr-cia)
3.  At a command prompt in at the root directory of the branch/checkout
    you're working on, enter `bzr cia-project Mixxx`
4.  In \~/.bazaar/bazaar.conf, set 'cia\_user' to your username on the
    CIA.vc system

That's it. The next time you push/commit code from this branch/checkout,
CIA will be notified.

## Troubleshooting

### Pull or Checkout

If when trying to pull/checkout a shared branch, you get an error like
`bzr: ERROR: Connection closed:
Unexpected end of message. Please check connectivity and permissions,
and report a bug if problems persist.` then you need to either:

  - Edit \~/.bazzar/bazzar.conf and remove the `launchpad_username` line
  - Or register your SSH key with Launchpad. (See details below.)

### Push or Commit

If when trying to push/commit to a shared branch, you get an error like
`bzr: ERROR: Cannot lock
LockDir(http://bazaar.launchpad.net/~mixxxdevelopers/mixxx/.bzr/branch/lock):
Transport operation not possible: http does not support mkdir()` then
you need to do the folllowing:

1.  Register your SSH key with Launchpad as above and tell Bazaar about
    it.
    [Instructions](https://help.launchpad.net/Code/UploadingABranch#Pushing%20your%20Bazaar%20branch%20to%20Launchpad)
2.  Issue the command `bzr launchpad-login <your lp username>`
3.  If it still doesn't work, issue the command `bzr bind
    bzr+ssh://<your lp
    username>@bazaar.launchpad.net/~mixxxdevelopers/mixxx/<branch name>`

## Tips and Tricks

Note that I (bkgood, ping me if you have issues) have no idea if any of
this works in "centralized" mode, I like branches =)

### Save disk space and bandwidth

Each mixxx branch can take (and transfer) something like 80MB for
history. As most of that is common throughout all your mixxx branches,
bazaar can share the common history throughout your branches, with a
*shared repository*. Follow the [directions (see "Shared Repository
Example")](http://wiki.bazaar.canonical.com/SharedRepositoryTutorial) to
learn more. For example, I have a repository at `~/src/mixxx` and then
have my branches (`trunk`, `1.9`, ...) under that. There's a large
(`79MB`) `.bzr` directory in the repository directory, and then each
branch under it has a `.bzr` directory in the `.5-2MB` range, so the
payoff is quite significant versus `79MB` for each branch. Note that
branch directories will still be huge when built because of the massive
amount of space the object files take.
