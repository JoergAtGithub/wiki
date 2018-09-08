To use the original version of the Native Instruments Traktor Audio 2
(the one with two 1/4 inch/6.35 mm jacks; the one with 1/8" inch/3.5mm
jacks is the newer model) with Mixxx on Linux, copy and paste this to
`~/.asoundrc`. Select "djAB" as the output device with Channels 1-2 for
Mixxx's Master output and channels 3-4 for Mixxx's Headphones output:

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
