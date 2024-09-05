### Core Team Guidelines ###
Mixxx core team members are contributors who have write access to the [upstream mixxxdj repositories](https://github.com/mixxxdj/) on GitHub, and access to the private Zulip stream for the core team.

Core Team members should follow these guidelines:

* Enable [two-factor authentication (2FA)](https://help.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa) for your GitHub account.
* _Never_ force push to an upstream repository (mixxxdj). If you encounter an error from Git saying you would need to force push, stop what you are doing and discuss the situation on Zulip.
* Only push directly to an upstream repository (mixxxdj) for trivial, uncontroversial changes like fixing a typo.
* All non-trivial contributions should be made with a pull request, just like any other contributor who does not have write access. Do not merge your own pull requests.
* You may merge someone else's pull request as the only reviewer if no other contributors have expressed concerns about the changes or said they want to review the code. Please do not merge pull requests immediately; allow at least a day or two for others to comment. Remember we are all volunteers and cannot respond to everything immediately.
* If there is disagreement about changes in a pull request, do not merge it until a consensus has been reached.
* Check CI to ensure builds work and tests pass before merging. If CI timed out, either manually restart it or build the branch and run the tests locally before merging.
* When you merge a pull request to a stable branch, merge the stable branch to the beta branch afterwards. If you merge a pull request to a beta branch, merge the beta branch to master afterwards. When backporting, cherry-pick or rebase rather than merge.
* Default to open; only post in the private Zulip stream for discussions that have a reason to be private. Most of the time, post to a public Zulip stream so anyone can participate in the discussion.
* When Mixxx participates in Google Summer of Code, you may volunteer as a mentor if you like.