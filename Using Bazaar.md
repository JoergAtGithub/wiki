# Using Bazaar

## GUI clients

Here's a list of graphical Bazaar clients that Mixxx developers have
tested:

#### Windows

#### Mac OS X

#### Linux

  - Olive (bzr-gtk) - Looks promising but is god-awful slow on large
    directories like our src/ (Tested by Pegasus)

## General procedure

1.  **Grab a personal copy** (called a "branch") of the Mixxx
    trunk/branch you want to work on using `bzr branch lp:mixxx` for
    trunk or `bzr branch lp:~mixxxdevelopers/mixxx/release-1.6.2` for
    the 1.6.2 release branch. This copies the code to your local system.
    (**Be patient** as the Mixxx code base is fairly large and older
    versions of bzr sometimes have difficulty reporting progress.)
2.  **Make changes** to the code as desired. Every so often issue `bzr
    commit -m 'log message`' which will "commit" the changes to your
    local store, allowing you to review or revert later.
3.  **Register a new personal branch** with Launchpad if you haven't
    already: <https://code.launchpad.net/people/+me/+addbranch>. You can
    create as many as you want, such as when working on different
    features.
4.  When you're ready to share with others, or if you're doing lots of
    local commits and want to prevent losing data, issue **`bzr push`**
    which actually copies your local store to your personal LP-hosted
    branch.
5.  When your branch is stable and ready for inclusion into trunk or the
    corporate branch, go to your branch's web page and click "**Propose
    for merging** into another branch" and fill in the form. You'll want
    to specify "mixxxdevelopers" as the reviewer. When you click the
    "Propose Merge" button, the Mixxx developers will be notified and
    will review & test your branch when they have a chance. They will
    then either merge it with the corporate code base or E-mail you back
    with questions or suggested changes.
