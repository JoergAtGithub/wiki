# Reverse Engineering Communication Protocols of DJ Hardware

For most controllers, watching the incoming MIDI messages sent to Mixxx
and referring to the manufacturer's documentation is enough to find all
you need to map a controller to Mixxx. Unfortunately, it is common for
manufacturers' documentation to be incomplete (for example, not
documenting the MIDI message to request the position of all the knobs
and faders when the DJ application starts) or completely missing. In
these cases, you'll need to reverse engineer how the hardware
communicates with other DJ software to get it working with Mixxx.

The [MIDI Crash Course](MIDI%20Crash%20Course) page has more background
information about interpreting MIDI messages.

## Observing MIDI/HID messages with Mixxx

1.  Start Mixxx from a command prompt using the `--controllerDebug`
    option like so: 

<!-- end list -->

  - Linux: `user@machine:~$ mixxx --controllerDebug`
  - Windows: `C:\Program Files\Mixxx>mixxx --controllerDebug`
  - macOS: `$ open -a mixxx --args --controllerDebug`

<!-- end list -->

1.  Look at the output

<!-- end list -->

  - Watch the console output or look at the
    [Mixxx.log](troubleshooting#where_is_the_mixxxlog_file) file which
    will contain all of the MIDI messages Mixxx receives. As you
    manipulate the controller, the MIDI commands it sends will be
    printed to the screen/logged to the file. Compare the status (first)
    byte in each line with the table above and note which
    button/slider/control sends what message.
  - For example, when you move a slider, you might see`Debug: [...]:
    "MIDI ch 1: opcode: B0, ctrl: 2, val: 3D" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3A" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3D" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3B" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3C" 
    `

In this instance, it's sending 0xB0 (which when we look at the
[table](MIDI%20crash%20course#midi%20messages), we see that it's a
Control Change message on channel 1). We also see that the second byte,
0x02 in this case, is the control number that was moved, and the third
is the value or position of that control, which you can ignore for the
purposes of mapping.

1.  Add the byte values to a `<control>` block in the XML file

<!-- end list -->

  - Just plug the first two bytes into a `<control>` XML block for
    `<status>` and `<midino>` respectively. This is detailed on the
    [MIDI Controller Mapping File
    Format](midi_controller_mapping_file_format#inputs) page.

## Observing MIDI/HID messages with other DJ software

[Wireshark](https://wireshark.org/) is an excellent, free, cross
platform program to record and analyze computer communication data. It
is most known for analyzing network traffic, but it can also be used for
USB traffic. Wireshark has a [USB Audio
filter](https://www.wireshark.org/docs/dfref/u/usbaudio.html) that can
be used to analyze traffic for USB Audio and MIDI devices (MIDI is part
of the USB Audio Class standard). Wireshark also has a [USB HID
filter](https://www.wireshark.org/docs/dfref/u/usbhid.html).

Use `usbaudio.midi.event` as the filter in Wireshark to separate audio
signals from MIDI. The `usbaudio.sysex.reassembled.data` filter shows
only system exclusive (sysex) messages.

### Running VMs on a Linux host

If you are using Linux, you can run other DJ software in a Windows
virtual machine and record the USB traffic with Wireshark (macOS is a
hassle to run in a VM but Windows is easy). You can run Wireshark on the
Linux host or inside the virtual machine, but if you run Wireshark in
Linux you don't need to bother transferring the captured traffic files
out of the VM. You need to redirect the USB device to the VM for the VM
to use it.

If you use VirtualBox, you need to install the VirtualBox guest
extensions with experimental 3D acceleration to run VirtualDJ or Serato.

TODO: Is there anything in particular to configure for QEMU?

Wireshark has both GUI and CLI applications.

#### Wireshark CLI

First, you need to load the kernel module that allows monitoring the USB
connection:

    $ sudo modprobe usbmon

Now run `lsusb` to find out with USB bus your controller is connected
to, e.g.:

    $ lsusb
    [...]
    Bus 001 Device 016: ID 0582:0208 Roland Corp. DJ-505

The controller in the example is connected to Bus 001, which means that
you need to use the `usbmon1` interface for capturing data.

Next, you can start monitoring the outgoing USB packets by using
`tshark` or `Wireshark`. If you're using the former, just run:

    $ tshark -i usbmon1 -Y 'usb.capdata && usb.src == host' -e usb.capdata -Tfields
    Capturing on 'usbmon1'

This will print all outgoing USB packets on interface `usbmon1` that
have a `usb.capdata` field (that contains the MIDI messages).

The captured data will start with an extra byte which you'll have to
ignore, e.g.:

| Captured USB data | MIDI message |
| ----------------- | ------------ |
| `0990007f`        | `90 00 7f`   |
| `0bbf6400`        | `bf 64 00`   |
| `09900100`        | `90 01 00`   |

### Windows

1.  explain software used
2.  explain minimizing bus traffic
3.  mention wsl as workflow accelerator
4.  usb RE-workflows
5.  timed captures
6.  Explain the difference between real USB vs USB-capture

[MIDI OX](http://www.midiox.com/) can intercept MIDI messages from
programs other than Mixxx.

### macOS

[MIDI Monitor](http://www.snoize.com/MIDIMonitor/) and
[MIDISimulator](http://www.macupdate.com/app/mac/35645/midisimulator)
are two different applications that can be used to observe MIDI signals
on macOS.

## Linux alsa-utils MIDI tools

alsa-utils on Linux has a few tools helpful for working with MIDI
devices.

Open a console and issue `amidi -l`. This will list the attached MIDI
device(s) like so:

    Dir Device    Name
    IO  hw:1,0,0  SCS.3d MIDI 1

Then, to dump the data, you just issue `amidi -p hw:1,0,0 -d` (Replace
hw:1,0,0 with whatever device ID your controller shows in the list.)
You'll get output like this:

    B0 02 3D
    B0 02 3A
    B0 02 3D
    B0 02 3B
    B0 02 3C

See above for how to interpret this data.

amidi can also be used to send MIDI messages to your controller with the
-S option. Specify each byte as a hexadecimal number and separate the
bytes by spaces. For example:

    amidi -p hw:1,0,0 -S "b0 02 7f"

The program `aseqdump` works similarly, but is a bit more verbose than a
series of hexadecimal numbers:

    $ aseqdump -l
     Port    Client name                      Port name
      0:0    System                           Timer
      0:1    System                           Announce
     14:0    Midi Through                     Midi Through Port-0
     20:0    Tweaker                          Tweaker MIDI 1
     20:1    Tweaker                          Tweaker MIDI 2
    $ aseqdump -p 20:0
    Waiting for data. Press Ctrl+C to end.
    Source  Event                  Ch  Data
     20:0   Note on                 0, note 1, velocity 127
     20:0   Note off                0, note 1
     20:0   Note on                 0, note 2, velocity 127
     20:0   Note off                0, note 2
     20:0   Note on                 0, note 3, velocity 127
     20:0   Note off                0, note 3