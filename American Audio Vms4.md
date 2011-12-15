# American Audio VMS4

[[/media/hardware/american_audio/vms4_angle.jpg|]]

Link to the website: <http://www.vms4dj.com/>

## Latest MIDI mapping & script files

[Mixxx user's guide for the VMS4](aa_vms4_mixxx_user_guide)

### Instructions

*Recommended setup for Mixxx v1.9.0 and up:*

**Important: Mixxx expects the VMS4 to be set to "Post EQ" mode for best
sound quality.** Do this by holding down the Cue button on Midilog 4
while powering on the unit. You only need to do this once. (Each time
you do it, it changes the mode back and forth.) Consult the [user
manual](http://vms4dj.com/Files/vms4.pdf) for more information.

1.  Download the files below.
2.  Save the files into:

<!-- end list -->

  - Windows: `C:\Program Files\Mixxx\midi` (technically
    `%PROGRAMFILES%\Mixxx\midi`)
  - OS X: `/Applications/Mixxx.app/Contents/Resources/midi`
  - Linux: `/usr[/local]/share/mixxx/midi`

<!-- end list -->

1.  Make sure the VMS4 is off
2.  Slide the switch on the front of the VMS4 to "4 OUT"
3.  Turn on the unit (and plug in the USB cable if you haven't yet)
4.  Start Mixxx
5.  Open Preferences
6.  Click Sound Hardware. In the right pane:
    1.  Set the sample rate to 44100Hz
    2.  Set the Master output to **None**
    3.  Set the Headphone output to **None**
    4.  Set the Deck 1 output to the **VMS4** device and **Channel 1-2**
        (may show as "USB Audio Device" on Windows)
    5.  Set the Deck 2 output to the **VMS4** device and **Channel 3-4**
7.  Plug your headphones into the VMS4's jack on the front. You will use
    the VMS4's CUE buttons and knobs for headphone control.
8.  Still in the Preferences, expand "MIDI Controllers" on the left
9.  Select the "VMS4 MIDI" device (may show as "USB Audio Device" on
    Windows)
10. Click the Enable checkbox in the right pane
11. Click the drop-down and choose the "American Audio VMS4" mapping
12. Click OK and the controller should light up. (In 1.9.x, the
    controller will light up when you load a track to a deck.)

### 1.10.x mapping

The latest official MIDI mapping and script file are in the 1.10 release
branch and can be downloaded from here:

  - [American Audio
    VMS4.midi.xml](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.10.x/download/head%3A/mixxxresmidiamerican-20101219215709-tp4stz5vume6p4ba-2/American%20Audio%20VMS4.midi.xml)
  - [American-Audio-VMS4-scripts.js](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.10.x/download/head%3A/mixxxresmidiamerican-20101219215709-tp4stz5vume6p4ba-1/American-Audio-VMS4-scripts.js)

### 1.9.x mapping

The latest official MIDI mapping and script file are in the 1.9 release
branch and can be downloaded from here:

  - [American Audio
    VMS4.midi.xml](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.9.x/download/head%3A/mixxxresmidiamerican-20101219215709-tp4stz5vume6p4ba-2/American%20Audio%20VMS4.midi.xml)
  - [American-Audio-VMS4-scripts.js](http://bazaar.launchpad.net/%7Emixxxdevelopers/mixxx/release-1.9.x/download/head%3A/mixxxresmidiamerican-20101219215709-tp4stz5vume6p4ba-1/American-Audio-VMS4-scripts.js)
