# Hercules DJ Console RMX

The Hercules DJ Console RMX is a USB MIDI controller with a built in
sound card. Both audio and MIDI works in Linux (at least from kernel
2.6.27), Windows (XP, Vista, 7), and MAC OS X (10.4.11 (Tiger)/ 10.5.x
(Leopard)/ 10.6.x (Snow Leopard) 32-bit)

## Audio

The sound card has 4 inputs and 4 outputs (2 stereo in/out). The two
inputs are switchable between line-in and phono, so you can connect both
cd-players and turntables on the inputs. The inputs require a high input
signal (\~10mV+) for turntables if you want to record or mix audio to
output. Time-coded vinyls, for Vinyl Control, should work ok with lower
input signal.

### Drivers

#### Linux

The audio device on the RMX is USB class compliant and works well with
the ordinary ALSA [USB-audio
driver](http://www.alsa-project.org/main/index.php/Matrix:Module-usb-audio).
This should work out of the box on most distributions.

#### MAC OS

#### Windows

## MIDI
