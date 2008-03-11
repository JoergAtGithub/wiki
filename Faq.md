# Frequently Asked Questions

If you've got a question that's not answered here, please post in the
[forums](http://www.mixxx.org/forums)\!

## How do I record my Mixxx session?

Mixxx doesn't directly support recording yet. But there are plenty of
external applications that can do it for you.
[Audacity](http://audacity.sourceforge.net/) is generally a good
open-source choice and has excellent editing capabilities to help you
clean up your recording afterwards.

## What's the best hardware DJ controller to use with Mixxx?

The upcoming 1.6.0 release will contain excellent support for the
[Hercules DJ Console
Mk2](http://www.hercules.com/showpage.php?swcty=UK&p=127&b=0&f=0). The
Hercules is a portable little controller with a slick pair of jogwheels
that's a perfect match for Mixxx. If you're looking for something
cheaper, the [Hercules DJ Control
MP3](http://www.hercules.com/showpage.php?swcty=UK&p=126&b=0&f=0) offers
the same control surface, but without the built-in soundcard.

A complete list of tested hardware devices is available on the [Hardware
Compatibility](Hardware%20Compatibility) page.

## Does Mixxx support multiple soundcards?

**Update:** Mixxx 1.6.0 includes support for multiple soundcards,
meaning you can have the headphone output coming out of one soundcard
and have the master ouput going out another soundcard.

Mixxx 1.5.0 doesn't support multiple output devices that span different
soundcards. For example, if you have two soundcards, you cannot
currently use one soundcard for headphone cueing and the other for
master output. However, you **can** use multiple outputs on a single
soundcard. For example, if you purchase a 5.1 USB soundcard, you can use
the "front" output as your master output, and plug your headphones into
the "rear" output for cueing. This is what the majority of Mixxx users
do.

## Is it possible to use Mixxx with an external mixer?

Yes. The trick is to force Mixxx's master output to playback the
left/top track, and the headphone output to playback the right/bottom
track. (Each track will come out a separate output, suitable for
plugging right into an external DJ mixer.) The way one does this is by
sliding Mixxx's crossfader all the way to the left, and turning on the
headphone cue for the right channel. This forces the first track to play
out the master out, and the second track to play out the headphone out.
(Since both outputs are now going straight into an external mixer, you'd
use the headphone cue on the mixer as well as it's crossfader.) Using an
external mixer is also described briefly in the [Threadbox
tutorial](Threadbox%20Tutorial#Using_an_External_Mixer_or_MIDI_Device).

## No soundcards appear in the preferences dialog - How can I fix this?

When no soundcards/devices appear in the sound preferences dialog, it
usually means that another application is using your soundcard(s). This
problem only appears on Linux. To fix it, make sure no other
applications are using your soundcard. The usual culprits are Firefox
and the esound daemon. Closing Firefox normally will take care of the
former, and running "killall esd" in a terminal will take care of the
latter. If it's still not working, running "sudo fuser -v /dev/dsp\*"
and "sudo fuser -v /dev/snd/\*" will show you the list of applications
currently using your soundcards.

## Mixxx behaves weird with Beryl/Compiz/Compiz Fusion - What gives?

Mixxx 1.5 doesn't play nicely with Beryl/Compiz, as reported by several
users. This is due to some funky OpenGL code inside QT3. Fortunately,
Mixxx 1.6.0 no longer uses QT3 and reportedly works very well with
Beryl/Compiz.

## What's vinyl control all about? How do I use it?

See the [Vinyl Control](Vinyl%20Control) page.

## Does Mixxx modify the files or structure of my library?

No, Mixxx does not write to or move any files in your library. It's safe
to use Mixxx with your iTunes library - Mixxx it will not change
anything in your library.
