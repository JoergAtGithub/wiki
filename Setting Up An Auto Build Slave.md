This page will discuss how to set-up a node that will contribute build
to <http://mixxx.org/packages/autobuilds/>.

The build nodes (also referred to as Private Hudson Instances) are not
slaves, but rather independent Hudson instances that publish their info
to the Public Hudson instance dashboard (currently found at
<http://mixxx.org:8080/>).

Hudson

  - Download hudson (or apt-get install it)
  - Start hudson
  - Go to Manage Hudson
  - Go to plug-ins, install: 
  - SCP
  - Build Publisher
  - BZR from <https://launchpad.net/bzr-hudson/+download>
  - Restart Hudson (every time you install a plug-in you have to)
  - Go to Manage Hudson
  - Go to System config
  - Add the following settings (some are not shown for security
    reasons):

screenshot here

  - Next, go back to Hudson's main screen, create a "new job"
  - Call the job the name of the arch
  - Add a description (can include HTML), I recommend something like
    this where you include the version, build host, distro info, and a
    link to where the autobuild will end up:

Mixxx 1.7.0 Built on QNAP-NAS (Ubuntu 9.04 i386)
<http://mixxx.org/packages/autobuilds/i386>
