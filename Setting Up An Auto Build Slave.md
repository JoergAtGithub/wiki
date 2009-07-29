This page will discuss how to set-up a node that will contribute build
to <http://mixxx.org/packages/autobuilds/>.

The build nodes (also referred to as Private Hudson Instances) are not
slaves, but rather independent Hudson instances that publish their info
to the Public Hudson instance dashboard (currently found at
<http://mixxx.org:8080/>).

##### TODO

  - Turn on SCM polling, so builds are triggered automatically when BZR
    commits happen (Job-\>Build Triggers-\>Poll SCM)
  - Fix [OSX compile issue](http://mixxx.org:8080/job/osx/1/console) so
    that builds + bundles
  - Add info on how to configure pbuilder and hudson on Linux hosts.

### Hudson Config

  - [Download hudson](http://hudson-ci.org/latest/hudson.war) (or
    apt-get install it)
  - Start hudson - either by:
  - java webstart -\> <https://hudson.dev.java.net/hudson.jnlp>
    <span class="underline">**OR**</span>
  - java -jar hudson.war \[options\] (yeah this looks odd, but hudson
    comes with embedded
    [winstone](http://winstone.sourceforge.net/#commandLine))
    <span class="underline">**OR**</span> 
  - you can deploy it to a servlet container like Tomcat
  - Go to Manage Hudson
  - Go to plug-ins, install: 
  - SCP
  - SCons
  - Build Publisher
  - After installing those, go to the plug-ins-\>Advanced tab: 
  - Download the BZR plug-in (from
    <https://launchpad.net/bzr-hudson/+download>) and use the plug-in
    upload feature on this screen to install it.
  - Restart Hudson (every time you install plug-in(s) you have to)
  - Go to Manage Hudson
  - Go to System config
  - Add the following settings (some are not shown for security
    reasons):

[[/media/hudson/hudson-scp-settings.png|]]
[[/media/hudson/hudson-publish-settings.png|]]

### Creating a Build Job

  - From Hudson's main screen select "new job"
  - Select *Build a free-style software project* for the job type
  - Call the job the name of the arch
  - Add a description (can include HTML markup), I recommend something
    like this where you include the version, build host, distro info,
    and a link to where the autobuild will end up:

<!-- end list -->

    Mixxx 1.7.0
    Built on QNAP-NAS (Ubuntu 9.04 i386)
    http://mixxx.org/packages/autobuilds/i386

  - Complete the BZR settings

[[/media/hudson/job-bzr-settings.png|]]

  - Complete Scons + build params settings (you have to choose "invoke a
    scons script" and then click on the "Advanced" button to get blanks
    for these settings) \*\*NOTE: \*\* These are just an example, your
    scons args and what packages you upload will vary by build machine
    and target OS respectively.

[[/media/hudson/job-scons-settings.png|]]

  - Tick the box to "Publish artifacts to SCP Repository"
  - Tick the box to "Publish build"

[[/media/hudson/job-scp_and_publish-settings.png|]]
