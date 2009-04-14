# MIDI Controller Mapping File Format

**Current XML file schema revision is: 1, but the spec may change before
release**

## Introduction

Support for additional MIDI devices can be added to Mixxx by created a
new "MIDI mapping" file. This mapping file tells Mixxx how to translate
MIDI commands from a controller into commands that Mixxx will
understand.

The MIDI mapping files are located in the following paths:

  - Windows: C:\\Program Files\\Mixxx\\midi
  - Linux: /usr/share/mixxx/midi (or /usr/local/share/mixxx/midi)
  - OS X: /Applications/Mixxx.app/Contents/midi

The easiest way to create a new MIDI mapping is by modifying an existing
one. When you've finished creating your MIDI mapping, **please send it
to us** and we'll include it in Mixxx.

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

These tags define the MIDI event that Mixxx will listen for:

  - status - MIDI Message Category (high nibble) and channel (low
    nibble) - CC (0xBn), NOTE\_ON (0x9n), NOTE\_OFF (0x8n), or Pitch
    Bend (0xEn), where n is the channel number (0-15 inclusive).
  - midino - The MIDI control or note number (leave this out for the
    Pitch miditype)
  - options - Further refine the behaviour of the control (e.g.
    translations, sensitivity, acceleration) Necessary options will have
    default values, eg a jogwheel might have no acceleration by default.
    Can only handle one element currently.
  - Invert
  - Rot64inv
  - Rot64fast
  - Rot64
  - Diff - Add the value to the control's current value
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
  - status - MIDI "Status" byte (e.g. Note on (0x9n), Control Change
    (0xBn), Pitch (0xEn). n is the MIDI channel 0x0..0xF in hex.)
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

|  |                  |  |                              |  |                |  |                                                                                 |  |                                                           |  |
|  | ---------------- |  | ---------------------------- |  | -------------- |  | ------------------------------------------------------------------------------- |  | --------------------------------------------------------- |  |
|  | **\[Group\]**    |  | **Key/Control**              |  | **Range**      |  | **What it does**                                                                |  | **On-screen feedback**                                    |  |
|  | **\[Flanger\]**  |  | lfoDepth                     |  | default        |  | Adjusts the intensity of the flange effect                                      |  | Depth knob                                                |  |
|  | \[Flanger\]      |  | lfoDelay                     |  | 50..10000      |  | Adjusts the phase delay of the flange effect in microseconds                    |  | Delay knob                                                |  |
|  | \[Flanger\]      |  | lfoPeriod                    |  | 50000..2000000 |  | Adjusts the wavelength of the flange effect in microseconds                     |  | LFO knob                                                  |  |
|  | \----            |  | \----                        |  | \----          |  | \----                                                                           |  | \----                                                     |  |
|  | **\[Master\]**   |  | balance                      |  | default        |  | Adjusts the left/right channel balance on the Master output                     |  | Center Balance knob                                       |  |
|  | \[Master\]       |  | crossfader                   |  | \-1.0..1.0     |  | Adjusts the crossfader between players/decks (-1.0 is all the way left, Deck 1) |  | Crossfader slider                                         |  |
|  | \[Master\]       |  | headVolume                   |  | default        |  | Adjusts the headphone output volume                                             |  | Head Vol knob                                             |  |
|  | \[Master\]       |  | headMix                      |  | \-1.0..1.0     |  | Adjusts the cue/main mix in the headphone output                                |  | Pre/Main knob                                             |  |
|  | \[Master\]       |  | latency                      |  | absolute value |  | Latency setting (sound buffer size) in milliseconds (default 64)                |  | Latency slider in the prefs                               |  |
|  | \[Master\]       |  | samplerate                   |  | absolute value |  | The current output sample rate in Hz (default 44100)                            |  | (none)                                                    |  |
|  | \[Master\]       |  | volume                       |  | 0.0..5.0       |  | Adjusts the Master output volume                                                |  | Center Volume knob                                        |  |
|  | \----            |  | \----                        |  | \----          |  | \----                                                                           |  | \----                                                     |  |
|  | **\[Playlist\]** |  | LoadSelectedIntoFirstStopped |  | binary         |  | Loads the currently highlighted song into the first stopped deck                |  | Waveform view                                             |  |
|  | \[Playlist\]     |  | SelectNextPlaylist           |  | binary         |  | Switches to the next view (Library, Queue, etc.)                                |  | Playlist/tracktable display                               |  |
|  | \[Playlist\]     |  | SelectNextTrack              |  | binary         |  | Scrolls to the next track in the Playlist/tracktable                            |  | Playlist/tracktable highlight                             |  |
|  | \[Playlist\]     |  | SelectPrevPlaylist           |  | binary         |  | Switches to the previous view (Library, Queue, etc.)                            |  | Playlist/tracktable display                               |  |
|  | \[Playlist\]     |  | SelectPrevTrack              |  | binary         |  | Scrolls to the previous track in the Playlist/tracktable                        |  | Playlist/tracktable highlight                             |  |
|  | (N=1 or 2 below) |  | \----                        |  | \----          |  | \----                                                                           |  | \----                                                     |  |
|  | **\[ChannelN\]** |  | back                         |  | binary         |  | Fast rewind (REW)                                                               |  | \< button                                                 |  |
|  | \[ChannelN\]     |  | beatsync                     |  | binary         |  | Syncs the BPM to that of the other track (if BPM is detected on both)           |  | SYNC button & Pitch slider snaps to the appropriate value |  |
|  | \[ChannelN\]     |  | bpm                          |  | absolute value |  | Reads or sets the track's current BPM (changing the pitch)                      |  | BPM value display                                         |  |
|  | \[ChannelN\]     |  | cue\_default                 |  | binary         |  | Same behavior as pressing the CUE button on screen                              |  | CUE button                                                |  |
|  | \[ChannelN\]     |  | cue\_point                   |  | binary         |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | cue\_preview                 |  | binary         |  | Plays from the current cue point                                                |  | CUE button lights & waveform moves                        |  |
|  | \[ChannelN\]     |  | cue\_set                     |  | binary         |  | Sets a cue point?                                                               |  | Cue mark appears on the waveform?                         |  |
|  | \[ChannelN\]     |  | cue\_simple                  |  | binary         |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | duration                     |  | absolute value |  | Outputs the length of the current song in seconds                               |  | (none)                                                    |  |
|  | \[ChannelN\]     |  | file\_bpm                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | filterHigh                   |  | 0.0..4.0       |  | Adjusts the gain of the high EQ filter                                          |  | HIGH knob                                                 |  |
|  | \[ChannelN\]     |  | filterHighKill               |  | binary         |  | Holds the gain of the high EQ to -inf while active                              |  | HIGH knob                                                 |  |
|  | \[ChannelN\]     |  | filterLow                    |  | 0.0..4.0       |  | Adjusts the gain of the low EQ filter                                           |  | LOW knob                                                  |  |
|  | \[ChannelN\]     |  | filterLowKill                |  | binary         |  | Holds the gain of the low EQ to -inf while active                               |  | LOW knob                                                  |  |
|  | \[ChannelN\]     |  | filterMid                    |  | 0.0..4.0       |  | Adjusts the gain of the mid EQ filter                                           |  | MID knob                                                  |  |
|  | \[ChannelN\]     |  | filterMidKill                |  | binary         |  | Holds the gain of the mid EQ to -inf while active                               |  | MID knob                                                  |  |
|  | \[ChannelN\]     |  | flanger                      |  | binary         |  | Toggles the flange effect                                                       |  | FLANGER button                                            |  |
|  | \[ChannelN\]     |  | fwd                          |  | binary         |  | Fast forward (FF)                                                               |  | \> button                                                 |  |
|  | \[ChannelN\]     |  | Hercules1                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | Hercules2                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | Hercules3                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | Hercules4                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | LoadSelectedTrack            |  | binary         |  | Loads the currently highlighted track into the deck                             |  | Track name & waveform change                              |  |
|  | \[ChannelN\]     |  | loop                         |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | NextTask                     |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | NextTrack                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | pfl                          |  | binary         |  | Toggles headphone cueing                                                        |  | Headphone button                                          |  |
|  | \[ChannelN\]     |  | play                         |  | binary         |  | Toggles playing or pausing the track                                            |  | Play/pause button                                         |  |
|  | \[ChannelN\]     |  | playposition                 |  | default        |  | Sets the absolute position in the track (0=beginning, 1=end)                    |  | Waveform                                                  |  |
|  | \[ChannelN\]     |  | pregain                      |  | 0.0..4.0       |  | Adjusts the pre-fader gain of the track (to avoid clipping)                     |  | GAIN knob                                                 |  |
|  | \[ChannelN\]     |  | PrevTask                     |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | PrevTrack                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | rate                         |  | \-1.0..1.0     |  | Pitch control                                                                   |  | Pitch slider                                              |  |
|  | \[ChannelN\]     |  | rate\_dir                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | rate\_perm\_down\_small      |  | binary         |  | Sets the pitch 1% lower                                                         |  | Perm down button & Pitch slider                           |  |
|  | \[ChannelN\]     |  | rate\_perm\_up\_small        |  | binary         |  | Sets the pitch 1% higher                                                        |  | Perm up button & Pitch slider                             |  |
|  | \[ChannelN\]     |  | rate\_temp\_down             |  | binary         |  | Holds the pitch 4% lower while active                                           |  | Temp down button & Pitch slider                           |  |
|  | \[ChannelN\]     |  | rate\_temp\_up               |  | binary         |  | Holds the pitch 4% higher while active                                          |  | Temp up button & Pitch slider                             |  |
|  | \[ChannelN\]     |  | rateRange                    |  | 0.0..3.0       |  | Sets the range of the pitch slider (0.08 = 8%)                                  |  | none, until you move the pitch slider                     |  |
|  | \[ChannelN\]     |  | reverse                      |  | binary         |  | Toggles playing the track backwards                                             |  | REV button                                                |  |
|  | \[ChannelN\]     |  | scratch                      |  | default        |  | Affects absolute play speed & direction whether currently playing or not        |  | Waveform                                                  |  |
|  | \[ChannelN\]     |  | transform                    |  | ?              |  | ?                                                                               |  | ?                                                         |  |
|  | \[ChannelN\]     |  | volume                       |  | default        |  | Adjusts the channel volume fader                                                |  | VOL fader                                                 |  |
|  | \[ChannelN\]     |  | VuMeter                      |  | default        |  | Outputs the current instantaneous channel volume                                |  | Channel meter                                             |  |
|  | \[ChannelN\]     |  | wheel                        |  | default        |  | Affects relative play speed & direction                                         |  | Waveform                                                  |  |

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
