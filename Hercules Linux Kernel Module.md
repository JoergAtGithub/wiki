# Hercules Linux kernel module

Hercules released a linux driver for the MIDI part of their DJ consoles
and controllers. Since it's been outdated by newer kernel versions,
community members are now maintaining it, so it works also in newer
kernel versions.

## Package .deb

For Ubuntu 10.04 and up, you'll want lightrush's patched version:

<https://sites.google.com/site/lightrush/random-1/herculesdjconsoleonkernel2635orubuntumaverick>.

## Package dkms

dkms means: Dynamic Kernel Module Support

It is supported by all recent linux distros. When your distro will
update the kernel, it will automatically rebuild and reinstall the
drivers\!

Please follow instruction file: readme\_driver\_dkms.txt

<http://slist.lilotux.net/linux/deejay/mixxx/>

Update :

  - Ubuntu 10.10 : OK
  - Ubuntu 11.04 : Not tested (I'm working on it, it compiles, but I did
    have time to check it yet...)

## Old information

Some more (older) information can be found on these pages:

[Hercules/Guillemot DJ Console Series Controllers](hercules)

[](hercules_pc_dj_console)
