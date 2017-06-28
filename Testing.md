\======= Testing Mixxx development ======

As we develop new features and fix bugs for Mixxx, we need feedback from
users. Testing the latest developments is a great way to contribute to
Mixxx.

## Master builds

Our build server regularly makes new Mixxx installers from our master
git branch [available for
download](http://downloads.mixxx.org/builds/master/release/). We try to
keep the master branch reasonably stable and not merge new features
until we're fairly confident they are not going to create serious
issues. However, if you want to perform with these, do so at your own
risk. If you do decide to perform with a master build, test the same
build for several practice sets before your gig to check that it works
with your particular setup. If you encounter a bug, please [report
it](reporting%20bugs).

## GitHub pull requests

If you would really like to be on the bleeding edge, you can try out
[pull requests on GitHub](https://github.com/mixxxdj/mixxx/pulls) before
they get merged to the master branch. This way you can be involved in
the design of new features as they are being implemented. If there is an
issue with a build from a pull request, comment on the pull request on
GitHub instead of opening a bug on Launchpad.

AppVeyor, our continuous integration system for Windows, builds each
pull request and makes Windows installers. To get the Windows installer
for a pull request, go to the bottom of the page on GitHub, click "Show
all checks", then "Details" for AppVeyor. On the AppVeyor website, click
the 64 bit ("dist64") or 32 bit ("dist32") build, then click "Artifacts"
to get the link to the installer MSI file.

For Mac OS X and GNU/Linux, you will need to [start\#compile Mixxx from
source code](start#compile%20Mixxx%20from%20source%20code) yourself. You
can set up the git repository on your computer to make it easy to
[checkout pull requests
locally](https://gist.github.com/piscisaureus/3342247), then compile
them.
