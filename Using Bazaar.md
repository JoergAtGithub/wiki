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

1.  Grab a personal copy (called a "branch") of the Mixxx trunk/branch
    you want to work on using `bzr branch lp:mixxx` for trunk or `bzr
    branch lp:~mixxxdevelopers/mixxx/release-1.6.2` for the 1.6.2
    release branch. This copies the code to your local system.
2.  Make changes to the code as desired. Every so often issue `bzr
    commit -m 'log message`' which will "commit" the changes to your
    local store, allowing you to review or revert later.
3.  Register a new personal branch with Launchpad if you haven't
    already: <https://code.launchpad.net/people/+me/+addbranch>. You can
    create as many as you want, such as when working on different
    features.
4.  When you're ready to share with others, or if you're doing lots of
    local commits and want to prevent losing data, issue `bzr push`
    which actually copies your local store to your personal LP-hosted
    branch.

<!-- end list -->

``` 
- 
```
