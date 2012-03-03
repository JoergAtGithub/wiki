**Mixxx** is not available directly from Fedora because Mixxx statically
links to libmad in order to support mp3 files.

*Fedora is unable to include encoding and decoding support for the MP3
format because it requires patented technologies and the patent holder
has not provided licenses that are compatible with Fedora's
requirements* [source](https://fedoraproject.org/wiki/Multimedia/MP3)

Instead Mixxx is available from RPM Fusion.

Enable RPM Fusion using the instructions here:

<http://rpmfusion.org/Configuration>

Then run:

su -c 'yum install mixxx'
