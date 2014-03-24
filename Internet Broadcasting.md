# Broadcasting your Mixxx over the Internet

Starting with version 1.9.0, Mixxx directly supports live broadcasting
which allows you to connect to Shoutcast and Icecast servers. Using the
preferences dialogue, you can simply supply Mixxx with all information
needed to establish a server connection. To enable live broadcasting you
can either use the options menu or the checkbox within the preference
dialogue.

[[/media/mixxx-111-preferences-livebroadcasting.png|]]

For an Icecast server, you'll need to provide the mount point (of the
form "/mount"). You can enter the host as either a host name or an IP
address. In the "login" field, the default is to enter "source" –
without this, you will not connect successfully to the server. The
password will be provided by your streaming server provider, unless you
run your own radio server.

Do *not* enter a URL as the host\! "<http://example.com:8000>" does not
work. Use "example.com" in the host field and "8000" in the port field
instead.

If you connect to an Shoutcast server the default login name is "admin".
It is **not** necessary to specify a mount point. The password will be
provided by your streaming server provider.

An Icecast server can stream either mp3 or Ogg. However, although Ogg is
more efficient and effective - you get a better sound than mp3 at a
lower data rate - not all players can play Ogg streams, so as a result
mp3 is probably a better choice unless you know your listeners can hear
an Ogg stream successfully. You may need the LAME libraries to stream in
mp3. See the next section for details.

By default, Mixxx broadcasts artist and title information to your
listeners. You can disable this feature by selecting "enable custom
metadata". For technical reasons, broadcasting artist and title
information is not supported for OGG streams.

## MP3 streaming

Dependent on the server technology you can stream in OGG and MP3 format.
Due to licensing restrictions, MP3 streaming is disabled by default in
Mixxx. In order to enable MP3 streaming you must install the *LAME* MP3
codec. The following section explains how to do that.

If you have activated MP3 streaming support, you'll be also able to
record your mixes in MP3 format.

### Linux

On Ubuntu and Linux-based operating systems MP3 streams can be activated
by installing the package `libmp3lame`. Dependent on your Linux
distribution the package might be slightly named different such as
`lame`.

    sudo apt-get install libmp3lame0

### Windows

To activate MP3 streaming on Windows, the following steps are necessary:

1.  Download LAME libmp3lame binaries from
    <http://www.rarewares.org/mp3-lame-libraries.php>. The download page
    includes 32-bit and 64-bit versions. Make sure the version you
    download matches the version of Mixxx that you use, not the version
    of Windows. If you are on 64bit Windows but are using 32bit Mixxx,
    you need the 32bit ("x86") version of the library.
2.  Unpack the downloaded ZIP archive. You need a utility for
    manipulating archives like the free [7zip](http://www.7-zip.org).
3.  Copy *libmp3lame.dll* to the location you have installed Mixxx,
    probably C:\\Program Files\\Mixxx\\

**Windows Troubleshooting**

Double check that the version of LAME you use ("x86" = 32-bit vs. "x64"
= 64-bit) matches the version of **Mixxx** you use.

Make sure you put the DLL in the same folder that contains the
installation of Mixxx you are using.

Please note that Audacity and other web sites provide `lame` binaries
too. **DO NOT USE THESE VERSIONS.** If you do, Mixxx will show an error
when activating live broadcasting.

### Mac OSX

To activate MP3 streaming on Mac OSX, the following steps are necessary:

1.  Download [LAME 3.98.4
    Intel](https://mega.co.nz/#!WdwHHTzA!UkdJwUQiihwHb0ShdOBTYj8noSwXluxiKjdWvFQRgOU)(OS
    X 10.5+ 32-bit & 64-bit) or [LAME 3.98.4
    PowerPC](https://mega.co.nz/#!TMZ2HCrK!CakYABav9WbgAgsUpc7tBkFS488mkoPzhooPK9PfEeY)
    (OS X 10.5 32-bit) 
2.  Unpack & install the archive

Another easy way to achieve MP3 streaming is to use
[MacPorts](http://www.macports.org/) which is a repository manager (like
apt on Ubuntu) for Open Source software. Having installed this piece of
software, installing MP3 support is rather simple.

    sudo port install lame

# Alternate methods

Here are some other ways our users have found to broadcast their mix
sessions, useful for Mixxx versions 1.8.x and earlier.

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
