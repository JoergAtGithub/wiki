# Problems with Launchpad Bugs

Many people have expressed frustration with [bug tracking on
Launchpad](https://bugs.launchpad.net/mixxx). This is a place to
enumerate the problems so we have an objective list when comparing
alternate solutions.

Note that LaunchPad is open-source, so it is possible for us to directly
improve it. (See below.)

([Discussion on the
forum](https://mixxx.org/forums/viewtopic.php?f=1&t=9425).)

  - Login process is complex: it is a multi step process and the
    platform keeps asking about showing some username
  - No formatting
  - Can't edit comments
  - E-mail notifications are slow
  - Running our own instance would fix this
  - Categorization system for issues is inflexible
  - *Give example.*
  - Can't @mention people
  - Posting code and screenshots is clunky
  - *What exactly is wrong? Give an example of what would be good.*
  - Can't make templates for bug reports (e.g. to have people attach
    `mixxx.log` in the initial report)
  - No integration with the code review system (side effect of no longer
    hosting code in LP)
  - Yet another account needed. (Now six total: forum, Freenode, wiki,
    Launchpad, GitHub, mailing list)
  - [OpenID Connect](http://openid.net/connect/faq/) (which uses OAuth)
    would be a good solution to this in general. See [bug
    \#1732715](https://bugs.launchpad.net/mixxx/+bug/1732715).

# Possible solutions

## GitHub Issues

Many have suggested using GitHub's issue tracker since it naturally
integrates with its code review system.

Migration tools:
<http://lp2gh.readthedocs.io/en/latest/moving_issues.html>

### Advantages

  - Integrates with code review system

### Disadvantages

  - Doesn't explicitly support rich states other than just open/closed
  - Using labels for this is just a workaround and might become
    confusing. 
  - Not possible to link related issues
  - Not possible to specify different kinds of relationships
    (parent/child, predecessor/successor, duplicates, etc.)
  - Someone needs to commit to managing migration

## Apache Allura

<http://allura.apache.org/>

### Advantages

  - Integrated code, wiki and tickets/issues
  - Can run our own instance (if ever GitHub closes or decides to
    charge)

### Disadvantages

  - Must run our own instance (no pre-hosted environments, though
    possibly from third party)
  - Need to migrate data from three different systems
  - Someone needs to commit to managing migration

## Improve Launchpad

<https://dev.launchpad.net/>

### Advantages

  - No need to migrate data
  - Can run our own instance (if ever GitHub closes or decides to
    charge)

### Disadvantages

  - Developer resources taken away from Mixxx temporarily
