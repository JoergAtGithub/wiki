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
  - Check CI to ensure builds works and tests pass before merging. If CI
    timed out, either manually restart it or build the branch and run
    the tests locally before merging.
