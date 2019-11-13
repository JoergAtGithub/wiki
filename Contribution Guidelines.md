\======= Mixxx Contribution Guidelines ======

## All contributors

  - Each feature/bug fix should be done on its own Git branch so they
    can be reviewed and merged independently. Refer to [Using
    Git](Using%20Git) for how to do this. Please ask for help on
    [Zulip](https://mixxx.zulipchat.com/) if you have questions about
    using Git after reading that page.
  - If you are making changes to the GUI with a pull request, please
    post screenshots of the changes.
  - Low risk bug fixes should be targeted at the stable branch
    (currently 2.2). However, bug fixes for the stable branches must
    have a direct impact on users. If you spot a minor bug reading the
    code or only want to clean up the code, target that at the master or
    beta branch.
  - Controller mappings should be targeted at the stable branch unless
    they use features that are new in the beta or master branch.
  - Generally, prefer merging to rebasing. Do not rebase unless you have
    discussed that with whoever is reviewing the pull request. When you
    rebase a branch with an open pull request, prior review comments
    made inline in the code on GitHub lose their connection to that spot
    in the code. If you want to correct minor mistakes with a rebase or
    `git commit --amend` within a few minutes of pushing commits, that
    is okay as long as no one has started reviewing those commits yet.
  - Please help review other people's pull requests. When others review
    your pull requests, please return the favor. The continued progress
    of Mixxx depends on all of us working together. Even if you are not
    familiar with the area of the code being changed in a pull request,
    you can be helpful by building the branch, verifying that it works
    as described, and commenting with feedback about the user experience
    design.
  - If you demonstrate good coding skills, help review pull requests,
    contribute major features, and show a commitment to Mixxx over time,
    we may invite you to the core team.

## Core team

Mixxx core team members are contributors who have write access to the
[upstream mixxxdj repositories](https://github.com/mixxxdj/) on GitHub,
access to the Jenkins web interface for the build servers, and access to
the private Zulip stream for the core team.

  - Enable [two-factor authentication
    (2FA)](https://help.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa)
    for your GitHub account.
  - *Never* force push to an upstream repository (mixxxdj). If you
    encounter an error from Git saying you would need to force push,
    stop what you are doing and discuss the situation on Zulip.
  - Only push directly to an upstream repository (mixxxdj) for trivial,
    uncontroversial changes like fixing a typo.
  - All non-trivial contributions should be made with a pull request,
    just like any other contributor who does not have write access. Do
    not merge your own pull requests.
  - You may merge someone else's pull request as the only reviewer if no
    other contributors have expressed concerns about the changes or said
    they want to review the code. Please do not merge pull requests
    immediately; allow at least a day or two for others to comment.
    Remember we are all volunteers and cannot respond to everything
    immediately.
  - If there is disagreement about changes in a pull request, do not
    merge it until a consensus has been reached.
  - Check CI to ensure builds work and tests pass before merging. If CI
    timed out, either manually restart it or build the branch and run
    the tests locally before merging.
  - Default to open; only post in the private Zulip stream for
    discussions that have a reason to be private. Most of the time, post
    to a public Zulip stream so anyone can participate in the
    discussion.
  - When Mixxx participates in Google Summer of Code, you may volunteer
    as a mentor if you like.
