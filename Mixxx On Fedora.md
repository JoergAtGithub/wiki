**Mixxx** is not available directly from Fedora because Mixxx statically
links to libmad in order to support mp3 files.

*Fedora is unable to include encoding and decoding support for the MP3
format because it requires patented technologies and the patent holder
has not provided licenses that are compatible with Fedora's
requirements*

<https://fedoraproject.org/wiki/Multimedia/MP3>

Instead Mixxx is available from RPM Fusion.

Enable RPM Fusion using the instructions here:

<http://rpmfusion.org/Configuration>

Then run 'sudo -c yum install mixxx'

Currently only Mixxx 1.8.2 is available in rpmfusion. There is a
[bug](https://bugzilla.rpmfusion.org/show_bug.cgi?id=1667) open in
rpmfusion to update the RPM to 1.9.0. In the mean time you can use this
RPM:

<http://people.redhat.com/~jbrier/mixxx/mixxx-1.9.0-1.fc14.src.rpm>

There is a [bug](https://bugzilla.redhat.com/show_bug.cgi?id=691148) in
the version of portaudio included in Fedora which causes audio to hang
in Mixxx.

In order to not hit that bug you can install this newer version of
portaudio from this RPM:

<http://people.redhat.com/~jbrier/portaudio/portaudio-19-10.fc14.x86_64.rpm>
