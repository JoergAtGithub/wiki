Note: These instructions are for compiling a development version of
Mixxx. These tend to be unstable. Don't compile Mixxx using these
instructions if you intend on DJing live with it.

First remove default mixxx install.

Using synaptic remove the following:

``` 
 mixxx
 mixxx-data
```

``` 
 NOTE:  if you see a message saying ubuntustudio-audio will be removed, just click OK.
```

On the following steps you can use synaptic or use apt-get.

\#Install bazaar

    * 
        sudo apt-get install bzr

CD to the directory where you want to download mixxx and download it:

    * 
        bzr co lp:mixxx

–\>Let it download, you can install the following packages at the same
time

\#\#download software that will allow you to compile mixxx

    * 
        sudo apt-get install scons
    * 
        sudo apt-get install libqt4-sql-sqlite #mixxx uses sql lite database
    * 
        sudo apt-get build-dep mixxx #download mixxx dependencies
    * 
        sudo apt-get install libmp4v2-dev
    * 
        sudo apt-get install libfaad-dev
    * 
        sudo apt-get libportmidi-dev #← PortTime dev header, for v1.8

\#on the folder downloaded by bzr, go into this directory:

cd /mixxx/mixxx

\#Compile mixxx, this example is optimized for pentium M

    * 
        sudo scons prefix=/usr install optimize=2

NOTE: you can change optimize so you can optimize it for your CPU.
