As we develop new features and fix bugs for Mixxx, we need feedback from
users. Testing the latest developments is a great way to contribute to
Mixxx.

## Backup settings and database

Before switching from a stable release of Mixxx to a development
version, it is recommended to make a backup copy of your settings and
library database. We try to ensure that upgrading to new versions does
not interfere with settings from older versions, but we might not catch
every potential issue immediately. You can make a backup by copying the
whole folder [where the mixxx.log file
is](Finding%20the%20mixxx.log%20file). If you want to switch back to a
stable release of Mixxx after testing a development version, you can
copy your backed up settings folder to its original location.

## Master builds

Our build server regularly creates new Mixxx installers from our master
git branch [available for
download](http://downloads.mixxx.org/builds/master/release/). We try to
keep the master branch reasonably stable and not merge new features
until we're fairly confident they are not going to create serious
issues. However, if you want to perform with these, do so at your own
risk. If you do decide to perform with a master build, test the same
build for several practice sets before your gig to check that it works
with your particular setup. If you encounter a bug, please [[report
it|reporting-bugs]].

If you are using a GNU/Linux distribution other than Ubuntu or a
derivative distribution that is compatible with Ubuntu .deb packages,
you will need to [[compile from source code|compiling-on-Linux]] to
test the master git branch.

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

For Mac OS X and GNU/Linux, you will need to [compile Mixxx from
source](home#compile-mixxx-from-source-code) yourself.
Refer to the [Using Git](Using%20Git) wiki page for how to set up Git on
your computer for downloading the code to test pull requests.