# Packages

Ubuntu Packages to Install (Eclipse 3.2 which comes with Gutsy/Hardy is
a bit old, but it will work) install:

  - eclipse-cdt
  - eclipse-pydev

for Unit testing:

  - libcppunit-dev

# Plugins

  - SconsBuilder -
    <http://nic-nac-project.de/~lothar/eclipse/update/SConsBuilderPlugin.html>
  - Subclipse - <http://subclipse.tigris.org/install.html>

# IDE Setup

To edit SCons files with the Python syntax color highlighting: General
-\> Editors -\> File Associations

  - Add "SConscript" file type -\> Python Editor
  - Add "SConstruct" file type -\> Python Editor
  - Add "SConstruct.ext" file type -\> Python Editor

Pydev -\> Interpreters -\> Python

  - New python interpreter -\> /usr/bin/python

# Conditional Defines

You have to do this for CDT to provide completion if you are working
inside a ifdef block

Project Properties -\> Include Paths and Symbols

  - Add Preprocessor Symbol -\>
    <span class="underline">LIBDJCONSOLE</span>=1

# See Also

  - SConsBuilder example project -
    <http://nic-nac-project.de/~lothar/eclipse/update/scons-example.tar.gz>
  - Build C++ Programs With SCons in Eclipse Using SConsBuilder
    Plugin(MS Windows) -
    <http://beans.seartipy.com/2007/10/24/build-c-programs-with-scons-in-eclipse-using-sconsbuilder-pluginms-windows/>
