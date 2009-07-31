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
  - You will also need to have bzr-xmloutput (apt-get install
    bzr-xmloutput or install from
    <https://launchpad.net/bzr-xmloutput/+download>)
  - Restart Hudson (every time you install plug-in(s) you have to)
  - Go to Manage Hudson
  - Go to System config
  - Add the following settings (some are not shown for security
    reasons):

[[/media/hudson/hudson-scp-settings.png|]]
[[/media/hudson/hudson-publish-settings.png|]]

  - "/home/mixxx/public\_html/packages/autobuilds/"

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
  - Tick the box to "Publish build" (if you want to see builds not over
    write each other, I suggest using $JOB\_NAME/$BUILD\_ID instead of
    just $JOB\_NAME in the destination below)

[[/media/hudson/job-scp_and_publish-settings.png|]]

### Optional Adding BZR Repo polling

[[/media/hudson/job-build-trigger-settings.png|]]

#### Misc

### Installing bzr-xmloutput on OSX running macports

if you run [macports](http://www.macports.org/) you can install
bzr-xmloutput like so (there is no port for it atm):

    cd /opt/local/lib/python2.5/site-packages/bzrlib/plugins
    sudo wget http://launchpad.net/bzr-xmloutput/trunk/0.8.4/+download/bzr-xmloutput-0.8.4.tar.gz
    sudo tar -zxvf bzr-xmloutput-0.8.4.tar.gz 
    sudo mv bzr-xmloutput-0.8.4 xmloutput

### Windows Hudson QMake

  - TortoiseBZR appears to pull proxy settings from IE, so if changing
    networks be aware that you may not get connectivity for checkouts.

<!-- end list -->

``` 
* 
```

    Building QMakeBuilder
    * svn co https://svn.dev.java.net/svn/hudson/trunk/hudson/plugins/qmakebuilder
    * export JAVA_HOME=$(dirname $(dirname $(ls -l /etc/alternatives/javac | cut -d \> -f2))) # on Ubuntu, sets to something like JAVA_HOME=/usr/lib/jvm/java-6-openjdk (depends on your JDK)
    * aptitude install maven2
    * cd qmakebuilder && mvn && cd target && ls qmakebuilder.hpi
