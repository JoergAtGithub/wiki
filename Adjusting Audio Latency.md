# Adjusting Audio Latency

Being able to lower the Latency in Mixxx's Sound Hardware Preferences as
much as possible makes a huge difference in its responsiveness. However,
lowering it beyond what your system can handle will cause audible
glitches (pops). Here are some tips to configure your system to handle
lower latency audio:

## Linux

### Enable realtime scheduling

In Preferences \> Sound hardware, if there is a link to this page, Mixxx
is not running with real time priority. To enable Mixxx to run with real
time priority, you will need to set up your kernel and scheduling
permissions.

#### Kernel setup

To use real time scheduling, you will either need to boot Linux with the
"threadirqs" parameter or use a kernel with the [realtime patch
set](https://rt.wiki.kernel.org/index.php/Main_Page). To always boot
with the "threadirqs" kernel argument, add it to your grub.cfg by
editing /etc/default/grub as root, adding "threadirqs" to the line for
GRUB\_CMDLINE\_LINUX, then running `grub2-mkconfig -o
/boot/grub2/grub.cfg`. Reboot. Check that you have booted with the
"threadirqs" kernel parameter by running `grep threadirqs
/proc/cmdline`. If you booted with the "threadirqs" kernel parameter,
all the parameters you booted with will be printed. If there is no
output, you did not boot with the "threadirqs" kernel parameter.

To use a kernel with the realtime patch set, Fedora users can install
the kernel-rt package from the [Planet
CCRMA](http://ccrma.stanford.edu/planetccrma/software/) repository.
Ubuntu users can install the [kernel-rt or
kernel-lowlatency](https://help.ubuntu.com/community/UbuntuStudio/RealTimeKernel)
packages. [Crossfade](http://nongnu.org/crossfade) and [Ubuntu
Studio](http://ubuntustudio.org/) are distributions that come with a
realtime patched kernel. Note that kernels with the realtime patch set
may have some stability issues.

#### User permissions

Enabling real time scheduling in your kernel will only have an effect if
your user has permission to run Mixxx with realtime priority. Set the
maximum rtprio for your user by editing `/etc/security/limits.conf` as
root and add `<your user name> - rtprio 99` to allow Mixxx (and other
processes you run) to increase their thread priority to maximum. Reboot
for this to take effect.

### Raise the IRQ priority of your sound card

IRQs (interrupt requests) allow devices to get the operating system
kernel's attention. You can improve the audio performance of your
computer by configuring your OS to give more attention to your sound
card than other devices. This will not have any effect unless you have
enabled realtime scheduling in your kernel as described above.

The easiest way to raise the IRQ priority of your sound card is by
installing [rtirq](http://www.rncbc.org/archive/#rtirq) and setting it
to run on boot. To set rtirq to run on boot on distributions using
systemd (which is most distros), run `systemctl enable rtirq` as root.
Check that rtirq set your IRQ priorities correctly by running `rtirq
status`. The IRQ for your sound card will end in ehci\_hcd for devices
plugged into USB 2.0 ports and xhci\_hcd for USB 3.0 ports. If it is not
a USB sound card, look for "snd" in the last column. This should be
above other IRQs listed by `rtirq status`. The configuration file for
rtirq is located at `/etc/sysconfig/rtirq` in Fedora and
`/etc/default/rtirq` in Ubuntu. If you use a USB sound card, you may
want put "usb" in front of "snd" in the RTIRQ\_NAME\_LIST in rtirq's
configuration file (or remove "snd") to give your USB sound card higher
priority than your onboard sound card.

To set IRQ priorities manually, see [this
guide](http://subversion.ffado.org/wiki/IrqPriorities).

### Disable CPU frequency scaling or use the 'performance' mode

CPU Frequency Scaling is a main cause of Mixxx skipping on laptops. (Do
`ps aux | grep cpufreq` and kill any processes you find.) -- Actually it
is better to remove the kernel modules, do \`lsmod | grep freq\` and
then remove each of the modules using rmmod, note that if you are using
a notebook it will burn through battery **much** quicker when doing
this.

### Disable chipcard2

This utility polls for smart cards every few seconds, and when it does,
it can cause Mixxx's audio to skip, even with the latency set really
high.

## Windows

  - **ASIO**: ASIO bypasses the normal sound processing software in
    Windows which is too slow for programs that require low latency like
    Mixxx. Select ASIO in the API in Mixxx's Sound Hardware Preferences.
    This requires that you have ASIO drivers installed for your sound
    card. If not, search for them at the web sites of your sound card
    manufacturer and/or the chipset manufacturer (for integrated cards).
    If they don't offer ASIO drivers, try using
    [ASIO4ALL](http://www.asio4all.com/).
  - **ASIO sample rate**: The sample rate used by ASIO should be the
    same as the sample rate in Mixxx's Sound Hardware preferences.
  - **Sound card IRQ priority**: IRQs (interrupt requests) allow devices
    to get the attention of your operating system's kernel. For better
    sound performance, raise the priority of your sound card relative to
    other devices in your computer. Open Device Manager (Start-\>Control
    Panel-\>System, Hardware tab, Device Manager button) find your sound
    card, right-click it, choose Properties, then the Resources tab.
    Drop down to IRQs and see if anything else is sharing it. If so,
    this affects you, and you can try changing the IRQ assignment for
    your sound card in this window.
  - **Disable anti-spyware/anti-virus software**: It has been reported
    that doing this for Ad-Aware makes a huge difference in latency.
    This has not been confirmed with other anti-spyware or anti-virus
    programs, but is worth testing since these programs are known to
    slow systems down in general. Doing this may put your system at risk
    of infection if it is connected to the Internet.
  - **Disable nVidia's "PowerMizer."** nVidia's laptop drivers have a
    feature called "PowerMizer" that has been reported to cause all
    kinds of problems for audio and overall latency. It can be disabled
    with a registry tweak:
    <http://forum.notebookreview.com/showthread.php?t=261929>
  - **Disable the "Microsoft ACPI-Compliant Control Method Battery"**:
    Disable this in the Device Manager (under Control
    Panel-\>System-\>Hardware)

## Mac OS X

Raise the priority of Mixxx. While Mixxx is running, open Terminal and
run `` sudo renice -20 `pidof mixxx` `` (your user must be in
`/etc/sudoers`).

If you know of any more tips for reducing audio latency in Mac OS X,
please edit this page and add them here.
