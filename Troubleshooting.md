# Troubleshooting FAQ

## I have a decently fast Linux system. Why do I have to set the latency so high?

If you're using ALSA, try setting your Master output hardware to just
"default" instead of specific hardware. (This made a huge difference on
a test system with integrated Intel soundcard.) The drawback to this is
that system sounds (KDE beeps and such) will now be mixed in and will
come out the main output.

## I'm using Compiz and Mixxx, and sometimes the waveform view gets corrupted and slows my CPU to a halt

This is a known bug with Qt and Compiz -- the only solution at this time
is to disable Compiz when using Mixxx. In many cases, however, the two
are able to work fine together. It seems this might be specific to
certain graphics hardware.

## I have a decently fast system & video card. Why does Mixxx seem to crawl or pin the CPU?

We've seen this a few times and it has always been a video driver
problem. Make sure you have the latest drivers for your card. (You may
need to get them from the chipset maker (nVidia, AMD/ATI) rather than
the system board or computer manufacturer, since the manufacturer
drivers aren't always the latest.) Also, if you're on Windows, make sure
you have the latest [DirectX](http://www.microsoft.com/directx)
installed.

## No sound cards appear in the preferences dialog - How can I fix this?

When no sound cards/devices appear in the sound preferences dialog, it
usually means that another application is using your sound card(s). This
problem only appears on Linux. To fix it, make sure no other
applications are using your sound card. The usual culprits are Firefox
and the esound daemon. Closing Firefox normally will take care of the
former, and running "killall esd" in a terminal will take care of the
latter. If it's still not working, running "sudo fuser -v /dev/dsp\*"
and "sudo fuser -v /dev/snd/\*" will show you the list of applications
currently using your soundcards. If you're using ALSA, you can also
choose the "default" sound card option which will mix Mixxx's output
with everything else.

## Mixxx freezes, segfaults, or otherwise misbehaves and I have an nVidia graphics card

Before you try anything else, please update or reinstall your nVidia
graphics driver. I don't care if it's the same exact version, apparently
it is fickle and needs to be rebuilt/reinstalled any time things change
in the OS. Try this first before going any further. 90% of the time it
will fix your problem. You might also try getting the latest driver from
nVidia's web site instead of your PC/card manufacturer since they may be
newer.

# Mixxxcelaneous Known Issues

  - Linux Intel Mobile 4 Series chipset with I965 graphics driver causes
    segmentation fault on exit. No known workaround.
