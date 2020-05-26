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

## Running VMs on a Linux host

If you are using Linux, you can run other DJ software in a Windows
virtual machine and record the USB traffic with Wireshark. You can run
Wireshark on the Linux host or inside the virtual machine, but if you
run Wireshark in Linux you don't need to bother transferring the
captured traffic files out of the VM.

If you use VirtualBox, you need to install the VirtualBox guest
extensions with experimental 3D acceleration to run VirtualDJ or Serato.
