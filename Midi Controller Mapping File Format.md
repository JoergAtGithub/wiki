# MIDI Controller Mapping File Format

**Current XML file schema revision is: 1**

## Introduction

Support for additional MIDI devices can be added to Mixxx by creating a
new "MIDI mapping" file. This mapping file tells Mixxx how to translate
MIDI commands from a controller into commands that Mixxx will
understand.

The MIDI mapping files are located in the following paths:

  - Windows: C:\\Program Files\\Mixxx\\midi
  - Linux: /usr/share/mixxx/midi (or /usr/local/share/mixxx/midi)
  - OS X: /Applications/Mixxx.app/Contents/midi

By far, the easiest way to create a new MIDI mapping is by using the
MIDI Learn wizard in the Preferences (available in Mixxx 1.7.0 and
higher.) You can then modify the XML file it creates (or any of the ones
that ship with Mixxx) using the information on this page if you'd like
to fine-tune it or add more mappings. When you've finished creating your
MIDI mapping, **please send it to us** and we'll include it in Mixxx.

## MIDI Crash Course

Most MIDI messages are three bytes long. The first byte of any MIDI
message is called the **Status** byte. The first nybble (hex digit) is
the op-code and the second is the MIDI channel number. So if you have
`0x90` the op-code is `0x9` and the channel number is `0x0` (Ch 1.) The
full list of MIDI messages is below, where *n* represents the channel
number (0..F inclusive):

| Status     | Function                  | Data bytes         |                   |
| ---------- | ------------------------- | ------------------ | ----------------- |
| **0x8*n*** | **Note off**              | **Note number**    | **Note velocity** |
| **0x9*n*** | **Note on**               | **Note number**    | **Note velocity** |
| 0xAn       | Polyphonic after-touch    | Note number        | Amount            |
| **0xB*n*** | **Control/mode change**   | **Control number** | **Value**         |
| 0xC*n*     | Program change            | Program number     | (n/a)             |
| 0xD*n*     | Channel after-touch       | Amount             | (n/a)             |
| **0xE*n*** | **Pitch wheel**           | **LSB**            | **MSB**           |
| 0xF0       | System Exclusive message  | Vendor ID          | (data)            |
| 0xF1       | MIDI Time Code Qtr. Frame | (see spec)         |                   |
| 0xF2       | Song Position Pointer     | LSB                | MSB               |
| 0xF3       | Song Select               | Song number        | (n/a)             |
| 0xF4       | Undefined                 |                    |                   |
| 0xF5       | Undefined                 |                    |                   |
| 0xF6       | Tune request              | (n/a)              |                   |
| 0xF7       | End of SysEx (EOX)        | (n/a)              |                   |
| 0xF8       | Timing clock              | (n/a)              |                   |
| 0xF9       | Undefined                 | (n/a)              |                   |
| 0xFA       | Start                     | (n/a)              |                   |
| 0xFB       | Continue                  | (n/a)              |                   |
| 0xFC       | Stop                      | (n/a)              |                   |
| 0xFD       | Undefined                 | (n/a)              |                   |
| 0xFE       | Active Sensing            | (n/a)              |                   |
| 0xFF       | System Reset              | (n/a)              |                   |

The boldface entries in the table above are the messages we are most
concerned with since most DJ controllers use only these for all
functions. You'll need to consult the MIDI spec for the DJ controller
you're working with to determine which messages and note/control numbers
correspond to the DJ controller functions & LEDs. If your controller's
MIDI spec gives only note names and not numbers, [use this
table](http://www.harmony-central.com/MIDI/Doc/table2.html) to convert
them. To convert from decimal to hex, [use
this](http://www.geocities.com/binary_converter/).

(Note that in order to use System Exclusive messages, you will need
[MIDI Scripting](MIDI%20Scripting).)

### Sniffing your controller

*First, try using the MIDI Learn functionality in the Preferences-\>MIDI
Devices window at the bottom (in Mixxx 1.7.0 and higher.) It will help
you get many of the essential functions mapped quickly without having to
do any hacking.*

If you don't have the MIDI spec for your controller, first check the
manufacturer's web site under Support. Look for Manuals or User Guides.
MIDI specs are usually given in an appendix at the back of the manual.
Failing that, you can usually sniff the MIDI data the controller sends.

#### Linux

Open a console and issue `amidi -l`. This will list the attached MIDI
device(s) like so:

    Dir Device    Name
    IO  hw:1,0,0  SCS.3d MIDI 1

Then, to dump the data, you just issue `amidi -p hw:1,0,0 -d` (Replace
hw:1,0,0 with whatever device ID your controller shows in the list.) See
"All" below for how to interpret this data.

#### Windows & All OSs using Mixxx \>=1.8.0

Start Mixxx from a command prompt using the `--midiDebug` option like
so: `C:\Program Files\Mixxx>mixxx --midiDebug` Then look at the
Mixxx.log file which will contain all of the MIDI messages Mixxx
receives.

On Windows, you can download
[tail.exe](http://tailforwin32.sourceforge.net/) to watch it as new
messages are added or [build Mixxx](Compiling%20on%20Windows) with
`scons msvcdebug=1` and run it with the `--midiDebug` option. This will
cause it to pop up a console window when you run it and the MIDI
messages received by your controller will be displayed there.

#### Mac OSX

Download the free [MIDI Monitor](http://www.snoize.com/MIDIMonitor/)
utility and run it.

#### All

Then as you press buttons or move sliders, the MIDI commands the
controller sends will be printed to the screen. Compare the status
(first) byte in each line with the table above and then just write down
which button/slider/control sends what command.

For example, when you move a slider, you might see

| Linux & Mac                                     | Windows                                                                                                                                                                                                                                            |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `B0 02 3D
B0 02 3A
B0 02 3D
B0 02 3B
B0 02 3C
` | `Debug: []: "MIDI status: B0, ctrl: 2, val: 3D" 
Debug: []: "MIDI status: B0, ctrl: 2, val: 3A" 
Debug: []: "MIDI status: B0, ctrl: 2, val: 3D" 
Debug: []: "MIDI status: B0, ctrl: 2, val: 3B" 
Debug: []: "MIDI status: B0, ctrl: 2, val: 3C" 
` |

In this instance, it's sending 0xB0, which when we look at the [table
above](#midi-crash-course), we see that it's a Control Change message on
channel 1. We also see that the second byte, 0x02 in this case, is the
control number, and the third is the value, which you can ignore for the
purposes of mapping. You would then just plug the first two bytes into a
\<control\> XML block (detailed below) for \<status\> and \<midino\>
respectively.

## File Format

Mixxx uses a well defined XML format to store its MIDI mappings. The
format is used for storing and distributing MIDI mappings from multiple
scopes.

    <?xml version="1.0" encoding="utf-8"?>
        <MixxxMIDIPreset schemaVersion="1" mixxxVersion="1.7.0+"> <!-- Schema version number to help compatibility, should the MIDI format change -->
        <info><!-- Optional - information about the preset file -->
            <name>Example MIDI Preset for Mixxx</name>
            <author>Tom Care</author>
            <description>This is an example XML MIDI preset for Mixxx. The scope of the preset could be from a small functionality addition, to a complete mapping for a controller, to a complex personal setup with multiple controllers. This description is intended for distribution and could include comments about the extent of the functionality.</description>
        </info>

The first part of the file defines the version of the mapping (for
future compatibility, as the Mixxx MIDI abilities become more complex)
and an optional info tag which contains information about the preset
(primarily used for distribution of presets).

``` 
    <controller id="controller name" port=""> <!-- Many controllers in one file supported. A controller should only appear once -->
```

The "controller id" is the brand & model of the controller, e.g.
"Stanton SCS.3d". Leave "port" empty.

The core part of the file contains a definition for a single controller.
There may be multiple controllers in one file (for more complex setups).
Each controller definition contains two sections: input bindings
(controls) and output bindings.

``` 
        <controls> <!-- One control group -->
            <control> <!-- Several controls -->
                <group>[Master]</group>
                <key>crossfader</key>
```

Group and key define the part of Mixxx that is being controlled. For a
list of what these values can be, [see
below](midi_controller_mapping_file_format#ui_midi_controls_and_names).

``` 
                <status>0xB0</status> <-- CC on channel 1 -->
                <midino>0x07</midino>
```

These tags define the MIDI event that Mixxx will listen for.

``` 
                <options>
                    <!-- all control specific options should go here - sensitivity etc. Specifics to be decided by spec -->
                </options>
```

The options further refine the behavior of the control. The list of
generic options may expand as Mixxx development continues, but any
controller-specific refinements (translations, sensitivity,
acceleration, etc.) belong in a [MIDI script](midi_scripting). Necessary
options will have default values, eg a jogwheel might have no
acceleration by default.

``` 
            </control>
        </controls>
        <outputs>
```

The next section defines outputs that use "short" (3-byte) MIDI
messages. (For SYSEX messages, you need to use
[scripting](midi_scripting).)

``` 
            <output>
                <group>[Channel1]</group>
                <key>play</key>
                <status>0x7F</status>  <!-- First byte sent to device -->
                <midino>0x08</midino>  <!-- Second byte -->
                <on>0x01</on>  <!-- Third byte. If not specified, 0x7F is used. -->
                <off>0x00</off> <!-- Alternate third byte. 0x00 is the default. If set to 0xFF, nothing is sent.-->
                <maximum>0.99</maximum>  <!-- Optional upper value for the Mixxx control, above which the 'off' value is sent. 1.0 is the default. -->
                <minimum>0.9</minimum>   <!-- Lower value for the Mixxx control, below which the 'off' value is sent -->
```

This allows you to send any three bytes to the MIDI controller in the
order Status, Midino, on/off. Minimum and maximum define the range
within which the 'on' value is sent. Outside this range, the 'off' value
is sent. If 'off' is set to 0xFF, no message will be sent outside the
range. (Useful for LED sequences.)

``` 
            </output>
        </outputs>
    </controller>
</MixxxMIDIPreset>
```

### Definitions of the elements:

These define the part of Mixxx that is being controlled:

  - group - The MixxxControl (controlobject) group
  - key - The MixxxControl (controlobject) key, a list of which can be
    found
    [below](midi_controller_mapping_file_format#ui_midi_controls_and_names).

These tags define the MIDI event that Mixxx will listen for or send out:

  - status - MIDI "Status" byte. See the [MIDI crash
    course](#midi-crash-course) above.
  - midino - The MIDI control or note number (leave this out for the
    Pitch Bend status.) Also see the [crash course](#midi-crash-course).

Input tags:

  - options - Further refine the behaviour of the control (e.g.
    translations, sensitivity, acceleration) Necessary options will have
    default values, eg a jogwheel might have no acceleration by default.
    Can only handle one element currently.
  - Normal - No modifications
  - Invert - Subtracts the value from 127, giving an inverted control
    (-127..0)
  - Rot64inv - 
  - Rot64fast - 
  - Rot64 - 
  - SelectKnob - For relative controls centered on 64 (0x40)
  - Diff - Adds the current value of a relative control to the previous
    value
  - Button - a button has a *Down* (non-zero) and an *Up* (zero) state,
    these occur together when pressed/released, this switch only
    triggers on the *Down*, *Up* is ignored. (Herc)
  - Switch - a switch has a *On* (non-zero) and an *Off* (zero) state,
    these occur separately. (Herc)
  - Spread64 - Exponential spread either side of 64, aka "relative"
    controller
  - Script-Binding - Bind to a MIDI script function given in the "key"
    tag. (See [MIDI Scripting](MIDI%20Scripting) for details.)
  - Hercjog - Handle hercules jog wheels (**deprecated**...please
    replace with a MIDI script function.)

Output tags:

  - maximum - Send the 'on' value when the Mixxx control drops below
    this value.
  - minimum - Send the 'on' value when the Mixxx control exceeds this
    value. Send the 'off' value otherwise.

### Old format (before schema versioning, Mixxx 1.6.1 and prior.)

The old midi mapping format is here for reference. The same options
apply as above, except use \<threshold\> for \<minimum\>, there's no
\<maximum\> (it's always 1.0,) and obviously \<Script-Binding\> won't
work. It looks like this:

``` 
 <!DOCTYPE controller>
 <controller>
   <controls>
     <control>
       <group>[[Master]]</group>
       <key>crossfader</key>
       <miditype>Ctrl</miditype>
       <midino>0x31</midino>
       <options>
         <hercjog/>
       </options>
     </control>
     ...
   </controls>
   <lights>
     <light>
       <group>[[Channel1]]</group>
       <key>VuMeter</key>
       <status>0xB0</status>
       <midino>0x16</midino>
       <threshold>0.5</threshold>
     </light>
     ...
   </lights>
 </controller>
```

# UI/MIDI Controls and Names

Each control inside Mixxx is identified by a unique string. These
strings are used in the keyboard mappings, the MIDI mappings, and inside
Mixxx to gain access to the controls. The following is a list of
controls that can be used in any of the above contexts.

## List of Controls

The default range is 0.0 to 1.0, unless otherwise noted. Binary means
it's either on (non-zero) or off (zero.)

*Please keep the controls in alphabetical order by group*

|  |                    |  |                              |  |                |  |                                                                                                                                                                                                     |  |                                                           |  |
|  | ------------------ |  | ---------------------------- |  | -------------- |  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | --------------------------------------------------------- |  |
|  | **\[Group\]**      |  | **Key/Control**              |  | **Range**      |  | **What it does**                                                                                                                                                                                    |  | **On-screen feedback**                                    |  |
|  | **\[Flanger\]**    |  | lfoDepth                     |  | default        |  | Adjusts the intensity of the flange effect                                                                                                                                                          |  | Depth knob                                                |  |
|  | \[Flanger\]        |  | lfoDelay                     |  | 50..10000      |  | Adjusts the phase delay of the flange effect in microseconds                                                                                                                                        |  | Delay knob                                                |  |
|  | \[Flanger\]        |  | lfoPeriod                    |  | 50000..2000000 |  | Adjusts the wavelength of the flange effect in microseconds                                                                                                                                         |  | LFO knob                                                  |  |
|  | \----              |  | \----                        |  | \----          |  | \----                                                                                                                                                                                               |  | \----                                                     |  |
|  | **\[Master\]**     |  | balance                      |  | \-1.0..1.0     |  | Adjusts the left/right channel balance on the Master output                                                                                                                                         |  | Center Balance knob                                       |  |
|  | \[Master\]         |  | crossfader                   |  | \-1.0..1.0     |  | Adjusts the crossfader between players/decks (-1.0 is all the way left, Deck 1)                                                                                                                     |  | Crossfader slider                                         |  |
|  | \[Master\]         |  | headVolume                   |  | 0.0..1.0..5.0  |  | Adjusts the headphone output volume                                                                                                                                                                 |  | Head Vol knob                                             |  |
|  | \[Master\]         |  | headMix                      |  | \-1.0..1.0     |  | Adjusts the cue/main mix in the headphone output                                                                                                                                                    |  | Pre/Main knob                                             |  |
|  | \[Master\]         |  | latency                      |  | absolute value |  | Latency setting (sound buffer size) in milliseconds (default 64)                                                                                                                                    |  | Latency slider in the prefs                               |  |
|  | \[Master\]         |  | samplerate                   |  | absolute value |  | The current output sample rate in Hz (default 44100)                                                                                                                                                |  | (none)                                                    |  |
|  | \[Master\]         |  | volume                       |  | 0.0..1.0..5.0  |  | Adjusts the Master output volume                                                                                                                                                                    |  | Center Volume knob                                        |  |
|  | \[Master\]         |  | VuMeter                      |  | default        |  | Outputs the current instantaneous master volume (composite)                                                                                                                                         |  | Master meter (mono)                                       |  |
|  | \[Master\]         |  | VuMeterL                     |  | default        |  | Outputs the current instantaneous master volume for the left channel                                                                                                                                |  | Master meter L                                            |  |
|  | \[Master\]         |  | VuMeterR                     |  | default        |  | Outputs the current instantaneous master volume for the right channel                                                                                                                               |  | Master meter R                                            |  |
|  | \----              |  | \----                        |  | \----          |  | \----                                                                                                                                                                                               |  | \----                                                     |  |
|  | **\[Playlist\]**   |  | LoadSelectedIntoFirstStopped |  | binary         |  | Loads the currently highlighted song into the first stopped deck                                                                                                                                    |  | Waveform view                                             |  |
|  | \[Playlist\]       |  | SelectNextPlaylist           |  | binary         |  | Switches to the next view (Library, Queue, etc.)                                                                                                                                                    |  | Playlist/tracktable display                               |  |
|  | \[Playlist\]       |  | SelectNextTrack              |  | binary         |  | Scrolls to the next track in the Playlist/tracktable                                                                                                                                                |  | Playlist/tracktable highlight                             |  |
|  | \[Playlist\]       |  | SelectPrevPlaylist           |  | binary         |  | Switches to the previous view (Library, Queue, etc.)                                                                                                                                                |  | Playlist/tracktable display                               |  |
|  | \[Playlist\]       |  | SelectPrevTrack              |  | binary         |  | Scrolls to the previous track in the Playlist/tracktable                                                                                                                                            |  | Playlist/tracktable highlight                             |  |
|  | \[Playlist\]       |  | SelectTrackKnob              |  | relative value |  | Scrolls the given number of tracks in the Playlist/tracktable (can be negative for reverse direction)                                                                                               |  | Playlist/tracktable highlight                             |  |
|  | (*N*=1 or 2 below) |  | \----                        |  | \----          |  | \----                                                                                                                                                                                               |  | \----                                                     |  |
|  | **\[Channel*N*\]** |  | back                         |  | binary         |  | Fast rewind (REW)                                                                                                                                                                                   |  | \< button                                                 |  |
|  | \[Channel*N*\]     |  | beatsync                     |  | binary         |  | Syncs the BPM to that of the other track (if BPM is detected on both)                                                                                                                               |  | SYNC button & Pitch slider snaps to the appropriate value |  |
|  | \[Channel*N*\]     |  | bpm                          |  | absolute value |  | Reads or sets the track's current BPM (changing the pitch)                                                                                                                                          |  | BPM value display                                         |  |
|  | \[Channel*N*\]     |  | cue\_default                 |  | binary         |  | In CDJ mode, when playing, returns to the cue point & pauses. If stopped, sets a cue point at the current location. If stopped and at a cue point, plays from that point until released (set to 0.) |  | CUE button                                                |  |
|  | \[Channel*N*\]     |  | cue\_point                   |  | absolute value |  | The current position of the cue point in samples                                                                                                                                                    |  | Cue point marker                                          |  |
|  | \[Channel*N*\]     |  | cue\_preview                 |  | binary         |  | Plays from the current cue point                                                                                                                                                                    |  | CUE button lights & waveform moves                        |  |
|  | \[Channel*N*\]     |  | cue\_set                     |  | binary         |  | Sets a cue point?                                                                                                                                                                                   |  | Cue mark appears on the waveform?                         |  |
|  | \[Channel*N*\]     |  | cue\_simple                  |  | binary         |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | duration                     |  | absolute value |  | Outputs the length of the current song in seconds                                                                                                                                                   |  | (none)                                                    |  |
|  | \[Channel*N*\]     |  | file\_bpm                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | filterHigh                   |  | 0.0..1.0..4.0  |  | Adjusts the gain of the high EQ filter                                                                                                                                                              |  | HIGH knob                                                 |  |
|  | \[Channel*N*\]     |  | filterHighKill               |  | binary         |  | Holds the gain of the high EQ to -inf while active                                                                                                                                                  |  | HIGH knob                                                 |  |
|  | \[Channel*N*\]     |  | filterLow                    |  | 0.0..1.0..4.0  |  | Adjusts the gain of the low EQ filter                                                                                                                                                               |  | LOW knob                                                  |  |
|  | \[Channel*N*\]     |  | filterLowKill                |  | binary         |  | Holds the gain of the low EQ to -inf while active                                                                                                                                                   |  | LOW knob                                                  |  |
|  | \[Channel*N*\]     |  | filterMid                    |  | 0.0..1.0..4.0  |  | Adjusts the gain of the mid EQ filter                                                                                                                                                               |  | MID knob                                                  |  |
|  | \[Channel*N*\]     |  | filterMidKill                |  | binary         |  | Holds the gain of the mid EQ to -inf while active                                                                                                                                                   |  | MID knob                                                  |  |
|  | \[Channel*N*\]     |  | flanger                      |  | binary         |  | Toggles the flange effect                                                                                                                                                                           |  | FLANGER button                                            |  |
|  | \[Channel*N*\]     |  | fwd                          |  | binary         |  | Fast forward (FF)                                                                                                                                                                                   |  | \> button                                                 |  |
|  | \[Channel*N*\]     |  | Hercules1                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | Hercules2                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | Hercules3                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | Hercules4                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | jog                          |  | \-3.0..3.0     |  | Affects relative play speed & direction for short instances (additive & is automatically reset to 0)                                                                                                |  | Waveform                                                  |  |
|  | \[Channel*N*\]     |  | LoadSelectedTrack            |  | binary         |  | Loads the currently highlighted track into the deck                                                                                                                                                 |  | Track name & waveform change                              |  |
|  | \[Channel*N*\]     |  | loop                         |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | NextTask                     |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | NextTrack                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | PeakIndicator                |  | binary         |  | Indicates when the signal is clipping (too loud for the hardware and is being distorted)                                                                                                            |  | Clip light                                                |  |
|  | \[Channel*N*\]     |  | pfl                          |  | binary         |  | Toggles headphone cueing                                                                                                                                                                            |  | Headphone button                                          |  |
|  | \[Channel*N*\]     |  | play                         |  | binary         |  | Toggles playing or pausing the track                                                                                                                                                                |  | Play/pause button                                         |  |
|  | \[Channel*N*\]     |  | playposition                 |  | default        |  | Sets the absolute position in the track (0=beginning, 1=end)                                                                                                                                        |  | Waveform                                                  |  |
|  | \[Channel*N*\]     |  | pregain                      |  | 0.0..1.0..4.0  |  | Adjusts the pre-fader gain of the track (to avoid clipping)                                                                                                                                         |  | GAIN knob                                                 |  |
|  | \[Channel*N*\]     |  | PrevTask                     |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | PrevTrack                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | rate                         |  | \-1.0..1.0     |  | Pitch control                                                                                                                                                                                       |  | Pitch slider                                              |  |
|  | \[Channel*N*\]     |  | rate\_dir                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | rate\_perm\_down\_small      |  | binary         |  | Sets the pitch 1% lower                                                                                                                                                                             |  | Perm down button & Pitch slider                           |  |
|  | \[Channel*N*\]     |  | rate\_perm\_up\_small        |  | binary         |  | Sets the pitch 1% higher                                                                                                                                                                            |  | Perm up button & Pitch slider                             |  |
|  | \[Channel*N*\]     |  | rate\_temp\_down             |  | binary         |  | Holds the pitch 4% lower while active                                                                                                                                                               |  | Temp down button & Pitch slider                           |  |
|  | \[Channel*N*\]     |  | rate\_temp\_up               |  | binary         |  | Holds the pitch 4% higher while active                                                                                                                                                              |  | Temp up button & Pitch slider                             |  |
|  | \[Channel*N*\]     |  | rateRange                    |  | 0.0..3.0       |  | Sets the range of the pitch slider (0.08 = 8%)                                                                                                                                                      |  | none, until you move the pitch slider                     |  |
|  | \[Channel*N*\]     |  | reverse                      |  | binary         |  | Toggles playing the track backwards                                                                                                                                                                 |  | REV button                                                |  |
|  | \[Channel*N*\]     |  | scratch                      |  | \-3.0..3.0     |  | Affects play speed & direction ([differently whether currently playing or not](https://bugs.launchpad.net/mixxx/+bug/530281)) (multiplicative)                                                      |  | Waveform                                                  |  |
|  | \[Channel*N*\]     |  | transform                    |  | ?              |  | ?                                                                                                                                                                                                   |  | ?                                                         |  |
|  | \[Channel*N*\]     |  | volume                       |  | default        |  | Adjusts the channel volume fader                                                                                                                                                                    |  | VOL fader                                                 |  |
|  | \[Channel*N*\]     |  | VuMeter                      |  | default        |  | Outputs the current instantaneous channel volume                                                                                                                                                    |  | Channel meter                                             |  |
|  | \[Channel*N*\]     |  | wheel                        |  | \-3.0..3.0     |  | Affects relative play speed & direction persistently (additive offset & must manually be undone)                                                                                                    |  | Waveform                                                  |  |

**And coming up in v1.8:**

|  |                |  |                        |  |                   |  |                                                                                                                                   |  |                                                                     |  |
|  | -------------- |  | ---------------------- |  | ----------------- |  | --------------------------------------------------------------------------------------------------------------------------------- |  | ------------------------------------------------------------------- |  |
|  | **\[Group\]**  |  | **Key/Control**        |  | **Range**         |  | **What it does**                                                                                                                  |  | **On-screen feedback**                                              |  |
|  | \[Channel*N*\] |  | loop\_in               |  | binary            |  | Sets the player loop in position to the current play position.                                                                    |  | Loop-in marker changes on waveform.                                 |  |
|  | \[Channel*N*\] |  | loop\_out              |  | binary            |  | Sets the player loop out position to the current play position.                                                                   |  | Loop-out marker changes on waveform.                                |  |
|  | \[Channel*N*\] |  | reloop\_exit           |  | binary            |  | Toggles the current loop on or off.                                                                                               |  | Loop range in waveform activates or deactivates.                    |  |
|  | \[Channel*N*\] |  | loop\_in\_position     |  | positive integer  |  | The player loop-in position, -1 if not set.                                                                                       |  | Loop-in marker changes on waveform.                                 |  |
|  | \[Channel*N*\] |  | loop\_out\_position    |  | positive integer  |  | The player loop-out position, -1 if not set.                                                                                      |  | Loop-out marker shows on waveform.                                  |  |
|  | \[Channel*N*\] |  | hotcue\_X\_position    |  | positive integer  |  | The position of hotcue X, -1 if not set.                                                                                          |  | Hotcue X marker changes on waveform.                                |  |
|  | \[Channel*N*\] |  | hotcue\_X\_enabled     |  | read-only, binary |  | 1 if hotcue X is active, (position is not -1), 0 otherwise.                                                                       |  |                                                                     |  |
|  | \[Channel*N*\] |  | hotcue\_X\_set         |  | binary            |  | Set hotcue X to the current play position. If hotcue X was previously set, clears its hotcue status.                              |  | Hotcue X marker changes on waveform.                                |  |
|  | \[Channel*N*\] |  | hotcue\_X\_clear       |  | binary            |  | If hotcue X is set, clears its hotcue status.                                                                                     |  | Hotcue X marker changes on waveform.                                |  |
|  | \[Channel*N*\] |  | hotcue\_X\_goto        |  | binary            |  | If hotcue X is set, seeks the player to hotcue X's position.                                                                      |  | Player may change position.                                         |  |
|  | \[Channel*N*\] |  | hotcue\_X\_gotoandstop |  | binary            |  | If hotcue X is set, seeks the player to hotcue X's position and stops.                                                            |  | Player may change position.                                         |  |
|  | \[Channel*N*\] |  | hotcue\_X\_activate    |  | binary            |  | If hotcue X is set, seeks the player to hotcue X's position. If hotcue X is not set, sets hotcue X to the current play position.  |  | Player may change position. Hotcue X marker may change on waveform. |  |
|  | \[Channel*N*\] |  | scratch2\_enable       |  | binary            |  | Takes over play speed & direction for *scratch2*.                                                                                 |  | Waveform                                                            |  |
|  | \[Channel*N*\] |  | scratch2               |  | \-3.0..3.0        |  | Affects **absolute** play speed & direction whether currently playing or not when *scratch2\_enabled* is active. (multiplicative) |  | Waveform                                                            |  |

This list contains nearly all of the controls that are useful to MIDI
mapping developers.

If you were so inclined, the full list (with mixed up \[Groups\],
internal objects and other things you shouldn't touch...be warned\!) can
be generated by running the following script in your mixxx/src
directory:

\======

    #!/bin/sh
    # set -x
    IFS='
    '
    last_control=
    
    for ck in `grep ConfigKey *.cpp | sed -e 's/ConfigKey(group/ConfigKey("[Master]"/g' | grep 'ConfigKey("' | grep -v "Channel2" | sed -e 's/.*ConfigKey(//g' -e 's/, */,/g' | cut -d\) -f1 | sed -e 's/\[Channel1\]/\[ChannelN\] (where N is a number 1 or 2)/g' | sort -fu`; do
      control=`echo $ck|cut -d\" -f2`
      if [ "$control" != "$last_control" ]; then
        echo
        echo $control
        last_control=$control
      fi
      key=`echo $ck|cut -d\" -f4`
      if [ ! -z "${key}" ]; then echo "* ${key}"; fi
    done

## Using Controls Inside Mixxx (for developers)

If you want to access one of these controls inside Mixxx, you can do so
with something like this:

``` 
 ControlObjectThreadMain* controlRightPitch = new ControlObjectThreadMain(ControlObject::getControl(ConfigKey("[[Channel2]]", "rate")));
```

That line will give you a ControlObject which allows you to read and
control the pitch of the right channel in Mixxx. For example, to
increase the pitch of the track in the right channel, one could do
something like this:

``` 
 float fRightPitch = controlRightPitch->get();
 controlRightPitch->slotSet(fRightPitch + 0.10);
```

This would increase the pitch of the right channel inside Mixxx, and the
GUI controls would automatically reflect this change. Access to
ControlObjects is also thread-safe when used this way.

**Important note:** Different types of ControlObject wrappers must be
used depending on what thread your code is running in. This example
assumes the code will run in the GUI (ie. main) thread. The
ControlObjects wrappers should be used as follows:

  - **ControlObjectThreadMain** - GUI (main) thread
  - **ControlObject** - The audio callback thread (most audio processing
    happens here)
  - **ControlObjectThread** - Other threads
