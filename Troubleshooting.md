# Troubleshooting FAQ

## I have a decently fast Linux system. Why do I have to set the latency so high?

If you're using ALSA, try setting your Master output hardware to just
"default" instead of specific hardware. (This made a huge difference on
a test system with integrated Intel soundcard.) The drawback to this is
that system sounds (KDE beeps and such) will now be mixed in and will
come out the main output.

## I have a decently fast system & video card. Why does Mixxx seem to crawl or pin the CPU?

We've seen this a few times and it has always been a video driver
problem. Make sure you have the latest drivers for your card. (You may
need to get them from the chipset maker (nVidia, AMD/ATI) rather than
the system board or computer manufacturer, since the manufacturer
drivers aren't always the latest.) Also, if you're on Windows, make sure
you have the latest [DirectX](http://www.microsoft.com/directx)
installed.
