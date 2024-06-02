Did you ever DJ‐ed with the material of another DJ? It is fun, it's a kind of exploration, it's like being a
child again that received a new toy.

Did you ever had to DJ on a party with the collection of another DJ? It is hell!

Not being able to find your favorite tracks because the organization of the records, CD's is different.
In stead of the alphabetical order that you're used to the records are ordered by genre or by bpm or

....

The same music collection can be ordered in many different ways.

For Digital DJ's is their most precious instrument their PC and data. A Digital DJ's data is irreplaceable, 
it contains their tracks with their adjusted metadata (cues, loops ...) and their lists (preparations,
playlists, crates, history ...).

Loosing data can be caused by system crashes, viruses, ransomware, hardware failure.

A controller or PC can be replaced but the data can't.

I'd like to explain some precautions that can be helpful for different calamities
* Playing with new software at home makes your PC extremely slow.
* An OS‐Update fails, you need to reinstall everything.
* PC crashes on location PC can't be used anymore, a clean spare PC is at your disposal.
* Someone gives you a song on a USB‐stick, the stick contains a virus and your OS crashes.

So in order to avoid laying awake in bed, continue reading, take notes and please take actions to
safeguard your data.

DJ‐ing with Mixxx? Your important Data contains:
* Your music collection
* The Mixxx settings directory, especially the Mixxxx‐Database, your Mixxx config file and your
controller‐mapping. For stable DJ‐ing with Mixxx keep the Mixxx settings folder your DJ‐ing
with on your local drive (Not on an external device to avoid problems with the database due
to possible speed‐problems or lose connections). Try to avoid different versions of your database, if you’ve got a
different PC for live gigs, copy your database to your live PC before leaving home and back to
your home PS after the gig (new cues, loops, playlists…)
* All other files can be regenerated.

## Separation between system/software disk and the Music‐collection ##
Make a division between a System‐disk and a Data‐disk. The System‐disk is only used for OS and
software, all data is put on the Data‐disk. If you keep this separation it will make it easy to
create/restore images from your System Disk (see below) without implicating your data.
The Data‐disk can be a partition of your internal disk or can be an external disk (can also be on a NAS
Network Attached Storage but this will be difficult for Live‐DJ‐ing).

If your new bought PC with huge capacity internal storage came with a drive with one single partition
(and maybe some hidden partitions) you can shrink this partition in order to create a 2<sup>nd</sup> (3<sup>rd</sup> 4<sup>th</sup>
partition) A system Disk of 250 Gb is enough for a work/home PC, for a Live‐DJ PC is 100 Gb more
than enough. https://en.wikipedia.org/wiki/Disk_partitioning

## Separation between home/work PC and live‐DJ‐PC... dual or multi‐boot ##
If you have the opportunity, separate your live‐DJ‐PC from your home/work PC. This way you can
keep a clean Live‐DJ‐PC, only necessary software is installed, no software that can influence the
behaviour of your PC’s CPU and RAM (programs working in the background) or can influence the use
of your soundcard. A clean PC will have a positive effect on your latency settings.

If you have only one PC, you can divide your hard drive in several partitions and install a 2<sup>nd</sup>
operating system on another partition. (for partitioning see earlier) When you start your PC you’ll
have a boot menu to select the OS you want to use. In this case you can have a clean DJ‐PC and a
home/work PC on the same machine with a multi‐boot.

Important: Keep your data on an extra different partition or external drive to make it accessible from
each OS, this allows you to maintain your library at home.

Multi boot opens the world of experimenting, what you do in one environment has no influence on
another environment. When one OS has a problem / crashes / needs an update … It won’t influence
the OS on other partitions. https://en.wikipedia.org/wiki/Multi‐booting

## Creating backups ##
Most Operating Systems contain a Backup/Restore program, if not you can install 3<sup>rd</sup> party BU
software. With this software you can set up a timely routine to copy selected files to a dedicated
location (tape/drive/USB/cloud), in case you have a problem with a (some) files you can restore these
files.

Positive
* selection on file level

Negative
* Rather slow

https://en.wikipedia.org/wiki/Backup_and_Restore

## Creating images ##
Besides of making Backups on file‐base there’s also the possibility to make an image file, this is a
snapshot of the complete drive / partition to a dedicated location. This means the complete drive is
copied (with a compression) to 1 or more files (depending on the size of the drive). Creating and
restoring an image file is really fast.
Using images makes it very easy to experiment and test software, because you can restore your OS
very fast to ‘normal’.

Positive
* very fast
* easy to configure routines
* easy to maintain

Negative
* Difficult to restore a single file
* You have to be very attentive when selecting the drive/partition

https://en.wikipedia.org/wiki/Disk_image

## Creating boot disk/stick ##
No matter which operating you have, make sure you can boot your PC in case there’s a problem with
your hard drive that prevents your PC from booting.

Create a boot device that can access the restore from a Backup or Image to easily restore your
system.

Nowadays the size of external media even support to have a complete OS on a USB‐Stick or SD‐Card.
This is an extremely secure backup. https://simple.wikipedia.org/wiki/Boot_device

## Cloud Storage ##
Storing your Mixxx core‐files in the cloud is a good idea, it’s an extra always accessible copy. Maybe
in the future huge Cloud Storage will be cheaper and faster (maybe with 5G or 6G) and when Mixxx
will be able to use Cloud Storage there will still be the problem of Network coverage. So Cloud Storage
is only a an extra copy.

Positive
* Always accessible

Negative
* Price
* Size
* Speed

https://en.wikipedia.org/wiki/Cloud_storage

## External Storage ##
Choose the size depending on the file file‐format you use (MP3/FLAC/WAV…). Make sure there’s
enough space to keep also images of your OS‐Partitions.

Make a Mixxx‐BU directory with a folder for Mixxx‐installation files, copy regularly the Mixxx‐settings
folder to this location.

Please invest in a 2<sup>nd</sup> (maybe a 3<sup>rd</sup> ) external device of the same size. There are different tools to
maintain the 2<sup>nd</sup> drive as a perfect clone / synchronized copy of your 1<sup>st</sup> live‐drive. Keep the 2<sup>nd</sup> device on a safe place (preferable not at home). This will safeguard your music https://en.wikipedia.org/wiki/External_storageSize

## Good practice ##
* Divide your Hard drive in partition
  * Partition 1 : System : OS 1 (live)
  * Partition 2 : System : OS 2 (work/home)
  * Partition 3 : Data / BU (containing images from Pat 1 & 2
  * ( Partition 4 : System : OS 3 (test) )
* Multi‐boot able to start following
  * 1. Part 1
  * 2. Part 2
  * 3. (Part 3)
  * 4. Image Restore Boot
* Create a Boot Device that can start the restore of an image and or contains a working OS,
keep it with your PC.
* Make images of your OS‐Partitions to the Data / BU partition, copy the images also to an
external device.
* Depending on the format of your music‐files and the amount of music you take to a live‐gig it
can be preferable to put your music on a partition on your internal drive, if the size of your
music is to big choose a fast external drive. Even external USB3 SSD drives are affordable
nowadays.
* Synchronize your external device
* Maintain the images / synchronization up to date.

## Extra ##
* Better safe than sorry, make yourself a routine to Backup (Copy) your Mixxx‐Data before
leaving home to your external device / cloud storage / usb …..
* Boot and reboot your live‐PC at home, disable automatic updates, avoid installation of not
necessary software on your Live‐PC
* Choose to invest in multiple smaller BU‐options then in 1 big. Make different copies of your
Data. Take fi a USB‐stick with you with a BU of your Mixxx‐settings directory. Keep a copy of
your Data not only at home but make a 2<sup>nd</sup> (3<sup>rd</sup> ...) copy to store at the home of a
friend/relative.
* Have a device with a 3.5 Jack output (iPod, Phone …) that can be connected to your mixer
and store a recorded live mix on it, in case of emergency the public won’t notice. A booing
crowd is not stimulating error free and logical decisions.