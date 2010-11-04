# Hercules DJ Console RMX

The Hercules DJ Console RMX is a USB MIDI controller with a built in
sound card. Both audio and MIDI works in Linux (from kernel \~2.6.27+),
Windows (XP, Vista, 7), and MAC OS X (10.4.11 (Tiger)/ 10.5.x (Leopard)/
10.6.x (Snow Leopard) 32-bit)

## Audio

The sound card has 4 inputs and 4 outputs (2 stereo in/out). The inputs
are switchable between line-in and phono, so you can connect both
cd-players and turntables on the inputs. The inputs require a high input
signal (\~10mV+) for turntables if you want to record audio or mix it to
the output. Time-coded vinyls, for Vinyl Control, should work ok with
lower input signal.

### Linux

The audio device on the RMX is USB-audio class compliant and works well
with the ordinary ALSA [USB-audio
driver](http://www.alsa-project.org/main/index.php/Matrix:Module-usb-audio).
This should work out of the box on most distributions.

### MAC OS / Windows

Drivers for MAC OS X and Windows can be found on [Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=215&cid=1).
Same package for both Audio and MIDI.

## MIDI

The midi device on the RMX is NOT USB-midi class compliant. For that
reason it requires specific drivers to be working on each OS.

### Linux

Hercules has released a common MIDI-driver for their DJ controllers.
Read more on the page for [Hercules Linux kernel
module](Hercules%20Linux%20kernel%20module)

### MAC OS / Windows

Drivers for MAC OS X and Windows can be found on [Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=215&cid=1).
Same package for both Audio and MIDI.

## MIDI Mappings

### Hercules DJ Console RMX

| Control | Default Mixxx Mapping |                                                                                            |  |
| ------- | --------------------- | ------------------------------------------------------------------------------------------ |  |
|         | Play/Pause            | Starts playing a loaded track if stopped. If track is currently playing it stops the track |  |
|         | Stop                  | Stops a currently playing track and moves to the beginning.                                |  |
|         | Cue                   | Cue behaviour is change-able from preferences.                                             |  |

### Hercules DJ Console RMX Advanced
