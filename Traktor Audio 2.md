if you're running ubuntu you need this ppa, install the latest
linux-alsa-driver-modules-2.6.35 module for your kernel.
<https://launchpad.net/~ubuntu-audio-dev/+archive/ppa>

then you need this .asoundrc file:

I found that I was then able to drive headphones at djA which is as far
as I've test so far.

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Native Instruments :: Audio2DJ ALSA Configuration
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #
    #    device channels        ports
    #    --------   ---             ---------
    #    djA        2               12xx
    #    djB        2               xx34
    #
    #    djAB       4               1234
    
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # dj(a-d) :: Raw 1x1 Stereo Devices
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    pcm.djA { type plug; slave.pcm "hw:TraktorAudio2,0,0"; }
    pcm.djB { type plug; slave.pcm "hw:TraktorAudio2,0,1"; }
    
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # djAB :: Multi 2x2 Stereo Device (Ports 1-4, Channels A+B)
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    pcm.djAB {
            type multi
    
            # bind hardware devices
            slaves.a.pcm djA
            slaves.a.channels 2
            slaves.b.pcm djB
            slaves.b.channels 2
    
            # bind channels to virtual device
            bindings.0.slave a
            bindings.0.channel 0
            bindings.1.slave a
            bindings.1.channel 1
            bindings.2.slave b
            bindings.2.channel 0
            bindings.3.slave b
            bindings.3.channel 1
    }
