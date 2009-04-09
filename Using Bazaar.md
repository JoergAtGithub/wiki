# Using Bazaar

## GUI clients

Here's a list of graphical Bazaar clients that Mixxx developers have
tested:

#### Windows

  - [Bazaar w/ TortoiseBZR](http://bazaar-vcs.org/Download) - Works well
    in check-out mode. Distributed online mode is slow in large
    directories. (Tested by Pegasus)

#### Mac OS X

#### Linux

  - Olive (bzr-gtk) - Looks promising but is god-awful slow on large
    directories like our src/ (Tested by Pegasus)

## General procedure for distributed use

1.  **Create a personal copy** (called a "branch") of the Mixxx
    trunk/branch you want to work on using `bzr branch lp:mixxx` for
    trunk or `bzr branch lp:mixxx/1.7` for the 1.7 release branch. This
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

## Making it work like SVN

(For those of us scared of this "distributed" thing...)

  - **Check out** with `bzr checkout lp:mixxx` for trunk or `bzr
    checkout lp:mixxx/1.7` for the 1.7 release branch. (**Be patient**
    as the Mixxx code base is fairly large and older versions of bzr
    sometimes have difficulty reporting progress.)
  - **Update** to latest version with `bzr update`
  - **Create a patch** with `bzr diff` \> mychanges.patch and send it to
    the [mixxx-devel mailing
    list](https://lists.sourceforge.net/lists/listinfo/mixxx-devel)
  - If you have commit access, **commit** with `bzr commit -m "Log
    message"` (You'll need to register an SSH key first under your
    personal LP page: <https://launchpad.net/people/+me/+editsshkeys>.)
