# Broadcasting your Mixxx over the Internet

Direct Shoutcast/Icecast support will be included in Mixxx 1.9.0.
(However, an unstable version is present in the 1.7-1.8 source code that
the more adventurous among you are free to try by building with the
`shoutcast=1` flag.)

In the meantime, please use one of the following methods that our users
have used for years:

## Linux via JACK and edcast

Hello, all\! It's **thread** here with a quick description of how I have
Mixxx stream out to dnbradio.com's shoutcast servers every Tuesday.

I run mixxx under the Ubuntu-based linux distribution, Crunchbang Linux.
Using Jack, I feed Mixxx's main L/R outputs to the simple, console-based
edcast (<http://www.oddsock.org/tools/edcast_jack/>), which is then able
to encode the audio to mp3 in realtime and feed it up to the remote
server.

I fire up Jack using the very simple frontend, qjackctl. Then I start
Mixxx and set it to output its audio via Jack. After some
straightforward editing of the edcast configuration file, I launch it,
specifying the configuration file and the jack sockets to stream from,
with something like this:

`~/apps/edcast$ bin/edcast -c etc/edcast.conf PortAudio:out_0
PortAudio:out_1`

And if all goes well, edcast will start telling you how many kilobits
were sent up every second, until it is killed with ctrl+c.

## Linux via JACK and IDJC

This is Madjester (pwhelan). I broadcast from Mixxx using JACK and IDJC.
IDJC is a fully featured program for Streaming like a Radio Jockey.

I fire up Jack using the qjackctl frontend, just like thread. Next step,
I fire up Mixxx. I then connect the Mixxx Portaudio:out\_0 and
Portaudio:out\_1 connectors to idjc:aux\_lt and idjc:aux\_rt using
Patchage.

You should be able to press the Auxilary button in IDJC to hear and/or
broadcast Mixxx.

# Broadcasting your Mixxx over the Internet (for Mixxx 1.9)

As of version 1.9 Mixxx supports live broadcasting which allows you to
connect to Shoutcast and Icecast servers. Using the preferences
dialogue, you can simply supply Mixxx with all information needed to
establish a server connection. To enable live broadcasting you can
either use the options menu or the checkbox within the preference
dialogue.

[[/media/shoutcast_prefs.png|]]

## MP3 streaming

Dependent on the server technology you can stream in OGG and MP3 format.
However, MP3 streams are not supported out of the box for some legal
reasons. On Ubuntu and Linux-based operating systems MP3 streams can be
activated by installing the package libmp3lame. Dependent on your Linux
distribution the package might be slightly named different such as lame.

`sudo apt-get install libmp3lame0`

To activate MP3 stream on Windows, the following steps are necessary.

1.  Download LAME 3.98.4 binaries from <http://lame.bakerweb.biz/>. The
    ZIP file includes x86 and x64 DLLs
2.  Unpack the archive
3.  If you downloaded the 32 bit version of Mixxx, copy libmp3lame.dll
    from the x86 folder to the location you have installed Mixxx.
4.  If you downloaded the 64 bit version of Mixxx, copy libmp3lame.dll
    from the x64 folder to the location you have installed Mixxx.
5.  Rename the DLL to lame\_enc.dll

Please note that Audacity and other web-sites provide lame binaries,
too. DO NOT USE THESE VERSIONS. Otherwise Mixxx shows an error when
activating live broadcasting.
