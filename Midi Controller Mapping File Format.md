# MIDI Controller Mapping File Format

**Current XML file schema revision is: 1**

## Introduction

Support for additional MIDI devices can be added to Mixxx by creating a
new "MIDI preset" file. This file tells Mixxx how to translate, or map,
MIDI messages from a controller into commands that Mixxx understands.

The MIDI mapping files are located in the following paths:

  - Windows: C:\\Program Files\\Mixxx\\midi
  - Linux: /usr/share/mixxx/midi (or /usr/local/share/mixxx/midi)
  - OS X: /Applications/Mixxx.app/Contents/Resources/midi

By far, the easiest way to create a new MIDI preset is by using the MIDI
Learn wizard in the Preferences (available in Mixxx 1.7.0 and higher.)
You can then modify the XML file it creates (or any of the ones that
ship with Mixxx) using the information on this page if you'd like to
fine-tune it or add more mappings. Note that the wizard puts its presets
in your user data directory:

  - Windows: %LOCALAPPDATA%\\Mixxx\\midi
  - Linux: /home/\<username\>/.mixxx/midi
  - OS X: /home/\<username\>/.mixxx/midi

When you've finished creating your MIDI mapping, please send it to us or
post it [on the forums](http://mixxx.org/forums/viewforum.php?f=7) and
we'll include it in the next Mixxx version.

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
table](http://www.wavosaur.com/download/midi-note-hex.php) to convert
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
Failing that, you can usually sniff the MIDI data the controller sends
with the following procedure:

1.  Start Mixxx (1.8.0 and later) from a command prompt using the
    `--midiDebug` option like so: 

<!-- end list -->

  - Linux: `user@machine:~$ mixxx --midiDebug`
  - Windows: (v1.7.0 and later) `C:\Program Files\Mixxx>mixxx
    --midiDebug`
  - Mac OSX: `$ open -a mixxx --args --midiDebug`

<!-- end list -->

1.  Look at the output

<!-- end list -->

  - Watch the console output or look at the
    [Mixxx.log](troubleshooting#where_is_the_mixxxlog_file) file which
    will contain all of the MIDI messages Mixxx receives. As you
    manipulate the controller, the MIDI commands it sends will be
    printed to the screen/logged to the file. Compare the status (first)
    byte in each line with the table above and note which
    button/slider/control sends what message.
  - For example, when you move a slider, you might see`Debug: [...]:
    "MIDI ch 1: opcode: B0, ctrl: 2, val: 3D" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3A" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3D" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3B" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3C" 
    `In this instance, it's sending 0xB0 (which when we look at the
    [table above](#midi-crash-course), we see that it's a Control Change
    message on channel 1) We also see that the second byte, 0x02 in this
    case, is the control number that was moved, and the third is the
    value or position of that control, which you can ignore for the
    purposes of mapping. 

<!-- end list -->

1.  Add the byte values to a `<control>` block in the XML file

<!-- end list -->

  - Just plug the first two bytes into a `<control>` XML block for
    `<status>` and `<midino>` respectively. This is detailed in the next
    section.

#### Additional tools

##### Linux

Open a console and issue `amidi -l`. This will list the attached MIDI
device(s) like so:

    Dir Device    Name
    IO  hw:1,0,0  SCS.3d MIDI 1

Then, to dump the data, you just issue `amidi -p hw:1,0,0 -d` (Replace
hw:1,0,0 with whatever device ID your controller shows in the list.)
You'll get output like this:

    B0 02 3D
    B0 02 3A
    B0 02 3D
    B0 02 3B
    B0 02 3C

See above for how to interpret this data.

##### Windows

You can download [tail.exe](http://tailforwin32.sourceforge.net/) to
watch mixxx.log as new messages are added or [build
Mixxx](Compiling%20on%20Windows) with `scons msvcdebug=1` and run it
with the `--midiDebug` option. This will cause it to pop up a console
window when you run it and the MIDI messages received by your controller
will be displayed there.

##### Mac OSX

Download the free [MIDI Monitor](http://www.snoize.com/MIDIMonitor/)
utility and run it. MIDI Monitor is a utility for Mac OS X which
displays MIDI signals in a variety of formats. It can watch both
incoming and outgoing MIDI streams, and can filter them by message type
and channel.

Download the free
[MIDISimulator](http://www.macupdate.com/info.php/id/35645/midisimulator/)
utility and run it. MidiSimulator is a tool to test midi devices like
pianos or dj controllers. It allows you to receive and send midi events.

## File Format

Mixxx uses a well defined XML format to store its MIDI mappings. The
format is used for storing and distributing MIDI mappings from multiple
scopes.

    <?xml version="1.0" encoding="utf-8"?>
        <MixxxMIDIPreset schemaVersion="1" mixxxVersion="1.7.0+"> <!-- Schema version number to help compatibility, should the MIDI format change -->
        <info><!-- Optional but recommended - information about the preset file -->
            <name>Example MIDI Preset for Mixxx</name>
            <author>Tom Care</author>
            <description>This is an example XML MIDI preset for Mixxx. The scope of the preset could be from a small functionality addition, to a complete mapping for a controller, to a complex personal setup with multiple controllers. This description is intended for distribution and could include comments about the extent of the functionality.</description>
                    <wiki>Encoded URL to official Mixxx wiki page for this controller</wiki>
                    <wiki>Encoded URL to Mixxx discussion forums page for this controller</wiki>
        </info>

The first part of the file defines the version of the mapping (for
future compatibility, as the Mixxx MIDI abilities become more complex)
and an optional info tag which contains information about the preset
(primarily used for distribution of presets). All info fields are used
in Mixxx controller selection dialogs and we highly recommend filling
all fields in, creating appropriate documentation pages to wiki and
forums if necessary.

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

***This information has been moved to [MixxxControls](mixxxcontrols)***
