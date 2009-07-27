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
  - SCons
  - Build Publisher
  - After installing those, go to the plug-ins-\>Advanced tab: 
  - Download the BZR plug-in (from
    <https://launchpad.net/bzr-hudson/+download>) and use the plug-in
    upload feature on this screen to install it.
  - Restart Hudson (every time you install a plug-in you have to)
  - Go to Manage Hudson
  - Go to System config
  - Add the following settings (some are not shown for security
    reasons):

screenshot here

  - Next, go back to Hudson's main screen, create a "new job"
  - Select *Build a free-style software project* for the job type
  - Call the job the name of the arch
  - Add a description (can include HTML markup), I recommend something
    like this where you include the version, build host, distro info,
    and a link to where the autobuild will end up:

<!-- end list -->

    Mixxx 1.7.0
    Built on QNAP-NAS (Ubuntu 9.04 i386)
    http://mixxx.org/packages/autobuilds/i386

  - Complete Scons build info

Screenshot

  - Tick the box to "Publish artifacts to SCP Repository"
  - Tick the box to "Publish build"

Screenshot

[[/media/hudson-publish-settings.png|]]
