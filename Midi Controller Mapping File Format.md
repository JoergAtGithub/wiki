# MIDI Controller Mapping File Format

Support for additional MIDI devices can be added to Mixxx by creating a
new "MIDI preset" file. This file tells Mixxx how to translate, or map,
MIDI messages from a controller into commands that Mixxx understands.

**The easiest way to create a new MIDI preset is by using the MIDI
Learning Wizard** in the *Preferences \> Controllers*. You can then
modify the XML file it creates (or any of the ones that ship with Mixxx)
using the information on this page if you'd like to fine-tune it or add
more mappings. This will work for most basic functions on most
controllers, but most controllers will require some use of [MIDI
scripting](MIDI%20scripting) with JavaScript for a complete mapping.

If you are unfamiliar with how MIDI works, see the [MIDI Crash
Course](MIDI%20Crash%20Course).

## File locations

Put custom mappings in the following folder. The MIDI Learning Wizard
puts its mapping files here:

  - GNU/Linux: `/home/<username>/.mixxx/controllers`
  - OS X: `/Users/<username>/Library/Application
    Support/Mixxx/controllers`
  - Windows: `%USERPROFILE%\AppData\Mixxx\controllers`

`%USERPROFILE%` on Windows is typically `C:\Users\<username\`. On
Windows XP and earlier, `%USERPROFILE%` is typically `C:\Documents and
Settings\<username>\`. The `%USERPROFILE%\AppData` folder is hidden, so
if you have not already, you will need to set Windows explorer to [show
hidden files and
folders](https://support.quickbooks.intuit.com/support/Articles/INF12729).

The default MIDI mapping files, which you can look at for examples or a
starting point for your own custom mapping, are located in the following
directory:

  - GNU/Linux: `/usr/share/mixxx/controllers` or
    `/usr/local/share/mixxx/controllers`
  - OS X: `/Applications/Mixxx.app/Contents/Resources/controllers/`
  - Windows: `C:\Program Files\Mixxx\controllers`

For Mixxx 1.10 and earlier, replace 'controllers' with 'midi' in the
above paths.

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
                    <wiki>Encoded URL to Mixxx wiki page documenting this controller mapping</wiki>
                    <forums>Encoded URL to Mixxx discussion forums page for this controller mapping</forums>
        </info>

The first part of the file defines the version of the mapping (for
future compatibility, as the Mixxx MIDI abilities become more complex)
and an optional info tag which contains information about the preset
(primarily used for distribution of presets). While optional, all info
fields are visible in Mixxx controller configuration dialogs and we
highly recommend properly filling in all fields, creating appropriate
documentation pages to wiki and forums if necessary.

**Note:** When a preset does not have a name in its \<info\> section,
Mixxx 1.11+ use the filename without extension.

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

### Definitions of the elements

These define the part of Mixxx that is being controlled:

  - group - The [Mixxx control object](mixxxcontrols) group
  - key - The [Mixxx control object](mixxxcontrols) key

These tags define the MIDI event that Mixxx will listen for or send out:

  - status - MIDI "Status" byte. See the [MIDI crash
    course](#midi-crash-course) above.
  - midino - The MIDI control or note number (leave this out for the
    Pitch Bend status.) Also see the [crash course](#midi-crash-course).

### Input tags

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

### Output tags

  - maximum - Send the 'on' value when the Mixxx control drops below
    this value.
  - minimum - Send the 'on' value when the Mixxx control exceeds this
    value. Send the 'off' value otherwise.
