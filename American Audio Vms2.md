# American Audio VMS2

[[/media/hardware/American-Audio-VMS2.png|American-Audio-VMS2.png]]

  - [Manufacturer's product
    page](http://www.americandj.eu/en/vms2.html), provides manual and
    drivers for download.
  - [Forum
    thread](http://www.mixxx.org/forums/viewtopic.php?f=7&t=3202), for
    discussion of mapping options.
  - [Latest controller
    mapping](https://github.com/mixxxdj/mixxx/pull/876), which this wiki
    page describes.

The American Audio VMS2 is a 2-deck all-in-one controller. It is a USB
class compliant MIDI and audio device that works with GNU/Linux, Mac OS
X, and Windows. It features a 4 channel input and 4 channel output sound
card with 2 phono preamps. The main output has XLR and RCA outputs (do
not use both at once). There is a separate RCA booth output. The VMS2
can also be used as a stand-alone mixer with analog sources without a
computer by setting the USB/Analog switches on the front of the device
to "Analog".

## Audio Setup

Because the sound card is USB Audio Class compliant, it works on
GNU/Linux, Mac OS X, and Windows without needing to install any special
drivers. However, on Windows, it is recommended to install the driver
from the manufacturer to be able to use the [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api).

Unlike most controllers with built in sound cards, which rely on Mixxx
to do all mixing in software, the VMS2 mixes signals from the sound card
in hardware. To use it with Mixxx:

  - Bypass the built-in hardware equalizer of the VMS2 (i.e. use Post-EQ
    Mode). Hold the forward search button on the right deck as you turn
    the VMS2 on to switch between Post-EQ and Pre-EQ modes. See section
    15 of the [manufacturer's
    manual](http://adjmedia.s3-website-eu-west-1.amazonaws.com/manuals/vms2_print_EN.pdf)
    for details.
  - Set the USB/Analog switches on the front side of the VMS2 to "USB"
  - In Mixxx's Sound Hardware Preferences:
  - Set the sample rate to 48000 Hz 
  - Select channels 1-2 for Deck 1 output
  - Select channels 3-4 for Deck 2 output

*Note*: You cannot use the preview deck to pre-listen in this setup, as
Mixxx routes the preview deck directly to the headphone output, which is
not mixed with the Deck 1/2 outputs. You could use a separate soundcard
and route the headphone output there to also pre-listen using the
preview deck. Of course, if you do so, attach the headphones to that
other soundcard instead of the VMS2.

### Input and Recording

The analog inputs are captured by the built-in soundcard as input
signals. They can be used for timecode signals (e.g. timecode vinyl), as
the VMS2 also features built-in phono preamps. FIXME I did not try that,
please verify\!

The microphone input is mixed directly into the master output signal of
the VMS2 in hardware and cannot be captured through software. If you
want to record voice over using the Mixxx software, you will need a
different solution. You can use a separate microphone attached to the
computer, but that signal will not be routed to the VMS2 and therefore
not be on the VMS2 master output (but in the Mixxx recording from the
software master/record output).

Mixxx's Deck 1/2 outputs are affected by the Mixxx software EQs.
However, the VMS2's volume faders and crossfader (as well as the
headphone buttons) control the VMS2's hardware mixer and do not affect
Mixxx's Deck 1 and Deck 2 output signals. Therefore, a recording using
the Mixxx software will sound different from what is played through the
VMS2 master output, as the crossfader curve and signal mixing are not
the same in hardware and software. If you require a recording that
captures exactly what the audience will hear, use a separate soundcard
and recording software to record from the VMS2 booth output.

### 4-Deck Setup

The 4 Deck routing for this controller is of very limited use, as the
volume- and crossfader directly influence the sound output in hardware.

  - Route Mixxx "Left Bus" to the VMS2 output channels 1-2 (Left Deck
    Stereo).
  - Route Mixxx "Right Bus" to the VMS2 output channels 3-4 (Right Deck
    Stereo).
  - Bypass the built-in hardware equalizer of the VMS2 (i.e. use Post-EQ
    Mode).
  - Route the headphone output to a separate soundcard.

In this mode, you cannot use the built-in headphone jack to pre-listen,
as the Mixxx software controls for deck volume already affect the
signals going into the VMS2. You need a separate soundcard to attach
your headphones.  
The two decks on the same bus are always directly affected by the volume
fader, therefore you cannot fade between two tracks playing on the same
bus without going over a point of silence. The faders are pretty much
useless in that setup as they cannot be used intuitively.  
FIXME The left and right bus are also affected by the software
crossfader\! That is bad and possibly wrong, as it means the hardware
and software crossfader are both applied. I need to file a bug report
(and link to it from here)\!

## MIDI Mapping

### Mixxx Versions / History

The VMS2 has been fully mapped for Mixxx by the community. Different
versions of the mapping exist. Most of them are linked somewhere in the
Mixxx VMS2 forum thread. As of Mixxx 1.11, two mappings were included
with Mixxx: the first one by Groschi, and a second, called
"(Alternative)" by snu (that's me ;-)).

Groschis mapping mapped the controls also found on the VMS4 for the
VMS2. The rotary knob in the middle section was left unmapped. The
"Alternative" mapping improved on that by mapping all controls. The
rotary knob was used for library browsing. It also featured EQ kill
buttons on the secondary IN/OUT/RELOOP buttons and an obscure way switch
between scratch mode and pitch mode.

As of January 2016, a new mapping has been proposed and a pull request
is filed (see Links section). If everything goes well, it will be
shipped with Mixxx 2.1.0, and replace both older mappings.

### Mapping Description

This description is for the latest VMS2 mapping, currently available in
a pull request against master (see Links section). This is currently
only a 2 deck mapping.

#### Main Mixer Section and Headphones

All main functions are mapped straightforward:

| VMS2 Control   | Mixxx Control          |
| -------------- | ---------------------- |
| Crossfader     | Crossfader             |
| Volume Fader   | Volume Fader           |
| Cue (PFL)      | PFL                    |
| Cue Mix        | Cue Mix (PFL / Master) |
| Headphone Gain | Headphone Gain         |
| Channel Gain   | Channel Gain           |
| Master Gain    | Master Gain            |

#### Deck Control

Deck control is straightforward, too:

| VMS2 Control          | Mixxx Control                                   |
| --------------------- | ----------------------------------------------- |
| Play                  | Toggle deck play/pause                          |
| Pause                 | Pause the deck                                  |
| Cue                   | Cue Point (configure behavior in software)      |
| Pitch +/-             | Temporary pitch bend +/-                        |
| Pitch Fader           | Pitch Fader                                     |
| Range (Shift+Sync)    | Cycle pitch fader range (+-8/10/30/100%)        |
| Sync                  | Sync to other deck                              |
| Search \<\</\>\>      | Search through currently loaded track           |
| Keylock (Shift+Vinyl) | Toggle pitch independent time stretch (KeyLock) |
| Vinyl                 | Toggle between Scratch mode and Pitch mode      |
| Platter               | Touch sensitive platters\! Scratch or Pitch     |

If you touch a platter in scratch mode, the track will stop there
immediately\! The backlight of the Vinyl button lights up when in
scratch mode. When in pitch mode, touching the platters is safe.

#### Library and Track loading

Use the rotational knob in the center of the controller to browse
through the library. Press the rotational knob to switch between library
main window and sidebar. Unfortunately there seems to be no way to
expand entries in the sidebar through the controller script.

Use the \[LOAD\] buttons to load the currently selected track into
either the left or right deck.

The four directional buttons around the knob also control the library:

| Button | Library function       |
| ------ | ---------------------- |
| Up     | Previous library entry |
| Down   | Next library entry     |
| Left   | Previous sidebar entry |
| Right  | Next sidebar entry     |

If you hold Shift and then rotate a platter, you can scroll through the
library much faster (but not as precise). This is sometimes handy to
scroll through very long library lists. However, as you should organize
your tracks in crates and playlists or simply use the library search
function to filter the list, this might be remapped to something
different in the future (maybe faster skimming through very long
tracks).

#### Equalizer

The per deck EQ rotaries are mapped to their software counterparts. The
VMS2 has no dedicated kill switches for the EQ. However, in Mixxx it has
(using the secondary Loop controls)\!

| VMS2 Control | Mixxx Control    |
| ------------ | ---------------- |
| Shift+IN     | Kill Switch Lo   |
| Shift+OUT    | Kill Switch Mid  |
| Shift+RELOOP | Kill Switch High |

#### Hot Cues

The VMS2 features 6 Hot Cues per deck.

| VMS2 Control                                    | Mixxx Control             |
| ----------------------------------------------- | ------------------------- |
| 1 / 2 / 3                                       | Set/Jump HotCue 1 / 2 / 3 |
| Vinyl + 1 / 2 / 3                               | Delete HotCue 1 / 2 / 3   |
| 4 / 5 / 6 = (Shift + 1 / 2 / 3)                 | Set/Jump HotCue 4 / 5 / 6 |
| Vinyl + 4 / 5 / 6 = (Vinyl + Shift + 1 / 2 / 3) | Delete HotCue 4 / 5 / 6   |

The controller script tries hard not to confuse Vinyl/KeyLock and HotCue
actions. So deleting HotCues should neither toggle KeyLock nor Scratch
Mode.

#### Loops

| VMS2 Control         | Mixxx Control                             |
| -------------------- | ----------------------------------------- |
| IN                   | Mark beginning of loop                    |
| OUT                  | Mark end of loop                          |
| RELOOP               | Leave / Reenter current loop              |
| LOOP                 | Start a 4 Beat loop from current position |
| Smart (Shift + Loop) | Toggle beat grid snapping                 |
| (:2) / (\*2)         | Halve or double the current loop length   |

As Mixxx currently only supports one active loop per deck, the secondary
loop controls have been remapped to EQ kill switches.

### Soft Takeover

The soft takeover feature shall prevent software controls from making
sudden jumps, when hardware and software controls got out of sync. A
hardware control needs to be moved close to were the software control
is, before hardware control changes are also applied in software. While
the idea is nice, it does not always work reliably, especially in hectic
situations when controls are moved very fast. Soft Takeover has
therefore been disabled for all controls in the mapping. If you want to
re-enable it, just search for "soft-takeover" in the mapping XML file
and uncomment the option. Soft takeover will probably be a required
feature for 4-Deck support.

### 4-Deck Support

As of Mixxx version 1.12, it is theoretically possible to control 4
decks by using the redundant \[PAUSE\] button as deck switch.
Unfortunately, this has not been mapped, yet. Stay tuned for updates or
get coding\!

### Effects

The VMS2 does not have enough spare buttons and rotaries to control
effects. It is probably best to use a dedicated effects controller for
that. In theory it would be possible to overlay the library search
rotary and the direction buttons around it, but this requires some
scripting effort and may be confusing, as the direction buttons do not
have backlights.
