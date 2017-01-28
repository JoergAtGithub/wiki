# Creating a macOS X build worker

Creating a macOS build worker virtual machine is not a trivial task, so
we outline the steps we took here for reference.

## Proxmox VE hypervisor, AMD CPUs

We owe a large debt of gratitude to the following intrepid people who
made this process much easier by doing most of the hard work:

  - [Nicholas Sherlock](http://www.nicksherlock.com/)
  - [Shaneee of AMD OS X](http://amd-osx.com/)

These instructions apply to macOS X 10.11 and the QEMU/KVM-based
[Proxmox VE](http://www.proxmox.com/) hypervisor/VM management software
suite running on AMD Opteron CPUs.

1.  Create a macOS installation DVD image as instructed on [Nicholas
    Sherlock's blog
    post](http://www.nicksherlock.com/2016/10/installing-macos-sierra-on-proxmox-4-3-qemu-2-6-1/)
    but we'll need to add a few things to it.
2.  Download the following items from [AMD OS
    X](http://amd-osx.com/download.html) into a temporary folder:

<!-- end list -->

  - Kernel matching the version of macOS you're installing
  - VoodooPState
  - Generic Extra

<!-- end list -->

1.  Mount the DVD image you created above ([see here for help doing so
    on Linux](http://it.bmc.uu.se/andlov/docs/macosx/mountdvd.php) as
    it's not as easy as a regular disc image.)
2.  From the place you unzipped the above AMD OS X packages, copy the
    following to the DVD image: 
    1.  the kernel `cp -R kernel
        /PATH-TO-MOUNTED-DVD/System/Library/Kernels/`
    2.  the Extra folder `cp -R Extra /PATH-TO-MOUNTED-DVD/`
    3.  the kernel extensions `cp -R *.kext
        /PATH-TO-MOUNTED-DVD/System/Library/Extensions/`
3.  Unmount the image and continue with the steps on Nicholas' blog
    starting from transferring the ISO DVD image and [Enoch boot
    loader](http://www.insanelymac.com/forum/files/file/71-enoch/) to
    your Proxmox box.
4.  Continue following his instructions up to where the VM reboots
    itself after the first stage of installation.
5.  We need to do some post-install prep work to get the newly-installed
    system to boot. Boot back into the installer and follow the
    instructions in [this AMD OS X
    post](http://forum.amd-osx.com/viewtopic.php?f=24&t=80). Wherever he
    says "USB installer" read "DVD image".
6.  At the end of that, when attempting to boot into the installed
    system image, if you experience a kernel panic "Unable to find a
    driver for this platform: ACPI", reset the VM and try again using
    the boot parameter `KernelBooter_kexts=Yes`
7.  The system should now start successfully. Configure as desired.
8.  Make the kernel read-only with `chmod -w
    /Volumes/HD-NAME/System/Library/Kernels/kernel` so system updates
    don't overwrite it with a non-AMD-compatible one and cause a boot
    loop.
9.  *Optional*: download and install the [VirtIO OSX network
    driver](https://github.com/pmj/virtio-net-osx) and change the
    network device on the VM from `e1000` to **VirtIO** for optimal
    performance.
