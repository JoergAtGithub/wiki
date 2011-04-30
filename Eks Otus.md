# Eks Otus

![http://eks.fi/img/kuvapankki/image/Otus/Otus\_perspective\_black\_crop.jpg](http://eks.fi/img/kuvapankki/image/Otus/Otus_perspective_black_crop.jpg)

Link to the website: [Eks -
Otus](http://eks.fi/product.php?p=products&id=34).

## Linux

### Set udev permissions

1.  Create/edit `/etc/udev/rules.d/10-local.rules`
2.  Add the line `KERNEL="hiddev*", NAME="usb/%k", GROUP="plugdev"`
3.  Make sure your user account is a member of plugdev: `sudo usermod
    $USER -a -G plugdev`
4.  Reload udev: `sudo /etc/init.d/udev reload`
5.  Now plug in the controller and start Mixxx.
