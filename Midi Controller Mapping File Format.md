# MIDI Controller Mapping File Format

Support for additional MIDI devices can be added to Mixxx by creating a
new "MIDI preset" file. This file tells Mixxx how to translate, or map,
MIDI messages from a controller into commands that Mixxx understands.

**The easiest way to create a new MIDI preset is by using the MIDI
Learning Wizard** in the *Preferences \> Controllers*. This will
generate an XML file located in the [user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder).
You can then modify this XML file it creates (or any of the ones that
ship with Mixxx or found on [the
forum](http://mixxx.org/forums/viewforum.php?f=7)) using the information
on this page. This will work for most basic functions on most
controllers, but most controllers will require some use of [MIDI
scripting](MIDI%20scripting) with JavaScript for a complete mapping.

If you are unfamiliar with how MIDI works, see the [MIDI Crash
Course](MIDI%20Crash%20Course).

Mixxx uses a well defined XML format to store its MIDI mappings. XML is
quite simple to learn enough to edit Mixxx mappings. If you know HTML,
the language that is used to define web pages, that will help because
XML is very similar.

## Header

Each XML mapping file starts with a header like this one:

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

## Inputs

The core part of the file contains a definition for a single controller.
There may be multiple controllers in one file (for more complex setups).
Each controller definition contains two sections: input bindings
(controls) and output bindings.

``` 
        <controls> <!-- One control group -->
            <control> <!-- Several controls -->
                <group>[Master]</group>
                <key>crossfader</key>
                <status>0xB0</status> <!-- CC on channel 1 -->
                <midino>0x07</midino>
                <options>
                    <!-- all control specific options should go here - sensitivity etc. Specifics to be decided by spec -->
                </options>
            </control>
        </controls>
```

The \<group\> and \<key\> elements define the value in Mixxx that this
MIDI signal controls. The [Mixxx Controls](mixxxcontrols) page lists the
available values for these group and key elements.

The \<status\> and \<midino\> elements define the MIDI signal that Mixxx
will listen for. See the [MIDI Crash Course](MIDI%20Crash%20Course) for
a brief introduction to MIDI signals.

### Input options

These are all specified with empty XML elements as children of the
\<options\> element. For example, to use the SelectKnob option, in the
XML, write:

``` 
                <options>
                    <SelectKnob/>
                </options>
```

  - Normal: No modifications
  - Script-Binding: Bind to a MIDI script function given in the "key"
    tag. (See [MIDI Scripting](MIDI%20Scripting) for details.)
  - SelectKnob: For relative controls centered on 64 (0x40)
  - Diff: Adds the current value of a relative control to the previous
    value
  - Invert: Subtracts the value from 127, giving an inverted control
    (-127..0)
  - Rot64inv: ?
  - Rot64fast: ?
  - Rot64: ?
  - Button: a button has a *Down* (non-zero) and an *Up* (zero) state,
    these occur together when pressed/released, this switch only
    triggers on the *Down*, *Up* is ignored. (Herc)
  - Switch: a switch has a *On* (non-zero) and an *Off* (zero) state,
    these occur separately. (Herc)
  - Spread64: Exponential spread either side of 64, aka "relative"
    controller

## Outputs

The next section defines outputs that use "short" (3-byte) MIDI
messages. Use this to control LEDs and other features of your
controller. (For SYSEX messages, you need to use
[scripting](midi_scripting).)

``` 
        <outputs>
            <output>
                <group>[Channel1]</group>
                <key>play</key>
                <status>0x7F</status>  <!-- First byte sent to device -->
                <midino>0x08</midino>  <!-- Second byte -->
                <on>0x01</on>  <!-- Third byte. If not specified, 0x7F is used. -->
                <off>0x00</off> <!-- Alternate third byte. 0x00 is the default. If set to 0xFF, nothing is sent.-->
                <maximum>0.99</maximum>  <!-- Optional upper value for the Mixxx control, above which the 'off' value is sent. 1.0 is the default. -->
                <minimum>0.9</minimum>   <!-- Lower value for the Mixxx control, below which the 'off' value is sent -->
            </output>
        </outputs>
```

This allows you to send any three bytes to the MIDI controller in the
order Status, Midino, on/off. Minimum and maximum define the range
within which the 'on' value is sent. Outside this range, the 'off' value
is sent. If 'off' is set to 0xFF, no message will be sent outside the
range. (Useful for LED sequences.)

## Closing

``` 
    </controller>
</MixxxMIDIPreset>
```
