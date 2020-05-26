# Reverse Engineering Communication Protocols of MIDI-/USB-based DJ Hardware

Often to get DJ hardware working with Mixxx, it is necessary to reverse
engineer how it communicates with other DJ software. This page has some
tips to get started with that.

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

## Running VMs on a Linux host

If you are using Linux, you can run other DJ software in a Windows
virtual machine and record the USB traffic with Wireshark (macOS is a
hassle to run in a VM but Windows is easy). You can run Wireshark on the
Linux host or inside the virtual machine, but if you run Wireshark in
Linux you don't need to bother transferring the captured traffic files
out of the VM.

If you use VirtualBox, you need to install the VirtualBox guest
extensions with experimental 3D acceleration to run VirtualDJ or Serato.

TODO: Is there anything in particular to configure for QEMU?

## Bare metal windows workflow

1.  explain software used
2.  explain minimizing bus traffic
3.  mention wsl as workflow accelerator
4.  usb RE-workflows
5.  timed captures
6.  Explain the difference between real USB vs USB-capture
