# Adjusting Audio Latency

The smaller the Audio Buffer you select in Mixxx's Sound Hardware
Preferences, the faster you will hear changes when you manipulate
controls in Mixxx, on a controller, or with timecode vinyl. However,
lowering it beyond what your system can handle will cause audible
glitches (pops). Here are some tips to configure your system to handle
lower latency audio:

## All operating systems

### Disable HyperThreading/SMT

Simultaneous Multithreading (SMT), or HyperThreading (HT) as Intel calls
it (AMD CPUs can also have SMT), can make some programs faster but makes
realtime audio software like Mixxx much more likely to glitch. On some
computers, it can be disabled in the BIOS/EFI firmware settings when
booting your computer. These settings can be accessed by pressing a key
as the computer is turning on. Which key you need to press is different
on every computer, so watch if it says on screen or refer to the
computer manufacturer's documentation. Unfortunately some computers do
not have an option to disable SMT/HyperThreading in the BIOS/EFI
settings. On Linux, this can be disabled by setting the "nosmt" kernel
parameter as described below.

SMT makes the CPU appear to the OS as if each physical CPU core was 2
cores (thus a dual core processor seems like it has 4 cores or a quad
core processor seems like it has 8 cores). This allows two threads to
switch off between using one CPU core, which may be beneficial for
software that makes heavy use of parallel processing. However, realtime
audio software like Mixxx requires reliable, uninterrupted time to use
the CPU to avoid audio glitches (xruns). When two threads share the same
CPU core with SMT, it is much more likely that Mixxx (or other realtime
audio software) will not generate the audio it needs in time so you and
your audience will hear a glitch.

## Linux

### Disable HyperThreading/SMT

Disable HyperThreading/SMT by adding "nosmt" to the kernel boot
parameters. How to do this may vary depending on your distribution, so
refer to your distribution's documentation for details. On Fedora, edit
the text file /etc/default/grub as root. There should be a line that
shows something like:

    GRUB_CMDLINE_LINUX="rd.lvm.lv=fedora/root rd.luks.uuid=luks-8847b15d-fd3c-4b93-a107-1e5166685508 rd.lvm.lv=fedora/swap rhgb quiet"

Add the "nosmt" parameter to the end of this:

    GRUB_CMDLINE_LINUX="rd.lvm.lv=fedora/root rd.luks.uuid=luks-8847b15d-fd3c-4b93-a107-1e5166685508 rd.lvm.lv=fedora/swap rhgb quiet nosmt"

Then, regenerate your GRUB configuration file:

    grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg

On other distributions, use "grub-mkconfig" instead of "grub2-mkconfig"
and the file path grub.cfg (after the "-o") will change as well. Then
reboot your computer.

SMT can also be toggled while Linux is running with the command:

    echo off > /sys/devices/system/cpu/smt/control

but this will be reset when you reboot unless you change the kernel boot
options as decribed above.

### Enable realtime scheduling

In Preferences \> Sound hardware, if there is a link to this page, Mixxx
is not running with real time priority. To enable Mixxx to run with real
time priority, you will need to set up your kernel and scheduling
permissions.

#### Kernel setup

To use real time scheduling, you will either need to boot Linux with the
"threadirqs" parameter or use a kernel with the [realtime patch
set](https://wiki.linuxfoundation.org/realtime/start). To always boot
with the "threadirqs" kernel argument, add it to your grub.cfg by
editing /etc/default/grub as root, adding "threadirqs" to the line for
GRUB\_CMDLINE\_LINUX, then generate a new grub.cfg file. On most
distributions, do this by running `grub-mkconfig -o
/boot/grub/grub.cfg`. On Fedora, run `grub2-mkconfig -o
/boot/grub2/grub.cfg` if you boot with BIOS (legacy) or `grub2-mkconfig
-o /boot/efi/EFI/fedora/grub.cfg` if you boot with EFI (if /boot/efi
does not exist, you boot with BIOS). Reboot. Check that you have booted
with the "threadirqs" kernel parameter by running `grep threadirqs
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
realtime patched kernel. Arch Linux users can install the
[linux-rt](https://aur.archlinux.org/packages/linux-rt/) or
[linux-rt-lts](https://aur.archlinux.org/packages/linux-rt-lts/)
packages. Note that kernels with the realtime patch set may have some
stability issues.

#### User permissions to create realtime threads.

Whether you are using a generic kernel or a kernel with the "real-time
patch set", your user needs permission to create threads with a
real-time scheduling policy (`SCHED_FIFO` or `SCHED_RR`). This
permission is disabled by default on major distributions due to
denial-of-service risks (a user with realtime permissions can easily
hard-lock a machine, requiring reboot). Distributions such as Ubuntu
Studio enable this permission by default.

Set the maximum rtprio for your user by editing
`/etc/security/limits.conf` as root and add `<your user name> -
rtprio 99` to allow Mixxx (and other processes you run) to increase
their thread priority to maximum. Reboot for this to take effect.

On Arch linux, install
[realtime-privileges](https://www.archlinux.org/packages/community/any/realtime-privileges/),
and `usermod $USER -a -G realtime` to add your user to the `realtime`
group. Logout and log back in for the changes to take effect.

You can use `cyclictest` (see below) to verify that your user has
permission to schedule realtime threads.

#### Testing your scheduling latency.

To test your best-case latency (CPU-only) using realtime threads,
`cyclictest` and `hackbench` from the
[rt-tests](https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/rt-tests)
package are useful.

    # Generate some load on the kernel scheduler.
    hackbench -l 10000000& 
    # Test the latency a SCHED_FIFO thread sees when attempting to wake up once per millisecond.
    cyclictest -s -i 1000 -l 10000000 -m --policy fifo
    # Don't forget to kill hackbench when you're done:
    pkill -9 hackbench

**Do not run the above commands via sudo\!** If you cannot run these as
an unprivileged user, then your `/etc/security/limits.conf` change did
not work.

The output will look like this:

``` 
T: 0 ( 8078) P: 2 I:1000 C:   3601 Min:      9 Act:   13 Avg:   11 Max:     254

```

The number to watch is the "Max", which tells you the maximum observed
latency in microseconds between the desired wake-up time and the actual
wake-up time. For a `SCHED_FIFO` thread on a realtime kernel, a max
latency of under 10 microseconds is easily achievable. For a generic
kernel, this will be harder.

To see how a non-realtime thread behaves, try `--policy other`, which
uses the `SCHED_OTHER` scheduling policy (the default).

### Raise the IRQ priority of your sound card

IRQs (interrupt requests) allow devices to get the operating system
kernel's attention. You can improve the audio performance of your
computer by configuring your OS to give more attention to your sound
card than other devices. This will not have any effect unless you have
enabled threadirqs with a generic kernel, or are running a kernel with
the realtime patchset.

The easiest way to raise the IRQ priority of your sound card is by
installing [rtirq](http://www.rncbc.org/archive/#rtirq) and setting it
to run on boot. To set rtirq to run on boot on distributions using
systemd (which is most distros), run `systemctl enable rtirq`. Check
that rtirq set your IRQ priorities correctly by running `rtirq status`.
The IRQ for your sound card will end in ehci\_hcd for devices plugged
into USB 2.0 ports and xhci\_hcd for USB 3.0 ports. If it is not a USB
sound card, look for "snd" in the last column. This should be above
other IRQs listed by `rtirq status`. The configuration file for rtirq is
located at `/etc/sysconfig/rtirq` in Fedora and `/etc/default/rtirq` in
Ubuntu. If you use a USB sound card, you may want to put "usb" in front
of "snd" in the RTIRQ\_NAME\_LIST in rtirq's configuration file (or
remove "snd") to give your USB sound card higher priority than your
onboard sound card.

To set IRQ priorities manually, see [this
guide](http://subversion.ffado.org/wiki/IrqPriorities).

### Disable CPU frequency scaling and using the performance governor

CPU frequency scaling is a main cause of Mixxx skipping on laptops. You
can disable it by running this shell script as root:

    for i in /sys/devices/system/cpu/cpu[0-9]*; do
      echo performance >$i/cpufreq/scaling_governor;
    done

Alternately, you can use the `cpupower` utility: `sudo cpupower
frequency-set -g performance`

The CPU governor will be reset when rebooting your computer. To run this
every time your computer boots, save the above shell script to
/etc/rc.d/rc.local and set that file to be executable `chmod +x
/etc/rc.d/rc.local` (this should work even on distributions using
systemd). Note that this will run through your battery's charge much
faster.

### Disable chipcard2

This utility polls for smart cards every few seconds, and when it does,
it can cause Mixxx's audio to skip, even with the latency set really
high.

### References

  - [Linux Audio Wiki: System
    Configuration](https://wiki.linuxaudio.org/wiki/system_configuration)
  - [Arch Linux Wiki: Realtime Kernel
    Patchset](https://wiki.archlinux.org/index.php/Realtime_kernel_patchset)
  - [cyclictest](https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/cyclictest/start)

## Windows

  - **Sound API**: See [the
    manual](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api)
    for information on choosing the best sound API for your setup
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

For more tips, see [Windows Tuning Tips for Audio
Processing](https://support.native-instruments.com/hc/en-us/articles/209571729-Windows-Tuning-Tips-for-Audio-Processing/)
from Native Instruments (this information applies to versions of Windows
newer than Vista as well).

## macOS

Raise the priority of Mixxx. While Mixxx is running, open Terminal and
run `` sudo renice -20 `pidof mixxx` `` (your user must be in
`/etc/sudoers`).

If you know of any more tips for reducing audio latency on macOS, please
edit this page and add them here.
