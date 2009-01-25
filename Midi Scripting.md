# MIDI Scripting

***MIDI Scripting is currently a work in progress. This information may
change prior to release.***

In order to support the advanced features of many MIDI controllers,
Mixxx offers what we call MIDI Scripting. It enables MIDI controls to be
mapped to [QtScript](http://doc.trolltech.com/4.3/qtscript.html) (aka
[Javascript](http://en.wikipedia.org/wiki/JavaScript_syntax)/[EMCAScript](http://www.ecma-international.org/publications/standards/Ecma-262.htm))
functions stored in function library files, freeing Mixxx from a
one-to-one MIDI mapping ideology. These user-created functions can then
do anything desired with the MIDI event info such as have a single
controller button simultaneously affect two or more Mixxx properties
("controls",) adjust incoming control values to work better with Mixxx
(scratching,) display a complex LED sequence, or even send messages to
text displays on the controller.

## Naming conventions

Script files use the naming convention
\<manufacturer\>-\<device\>-scripts.js (e.g. Stanton-SCS3d-scripts.js)
and are found in the midi/ subdirectory wherever your Mixxx shared data
is stored. (Usually /usr/share/mixxx on Linux/Mac, and C:\\Program
Files\\Mixxx on Windows.) Functions use the naming convention
\<manufacturer\>\<device\>.\<function name\> (e.g.
StantonSCS3d.pitchSlider). Global variables use
\<manufacturer\>\<device\>.\<variable name\> (e.g. StantonSCS3d.deck).
These are very important to avoid name collisions with other scripts
that may be loaded.

## Linking scripts to device controls

To link a script function to a particular control, in the device's XML
MIDI mapping file, put the full function name in the \<key\> tag, and a
\<Script-Binding/\> tag in the \<options\> block, like so:

``` XML
            <control>    <!--    Pitch slider    -->
                <group>[Master]</group>
                <key>StantonSCS3d.pitchSlider</key>
                <miditype>Ctrl</miditype>
                <midino>0x04</midino>
                <midichan>1</midichan>
                <options>
                    <Script-Binding/>
                </options>
            </control>
```

The value for \<group\> doesn't matter when using a script function, but
it still needs to be valid ("\[Master\]" or "\[Channel\#\]") or the XML
parser will report an error. No tags or options are considered other
than those shown above, so you can leave them out.

When this device control is operated, the named script function is
called. It is then up to the function to effect all desired changes
(Mixxx properties, device LEDs, etc.)

## Script functions

There is a default script function file called
`midi-mappings-scripts.js` which contains functions common to all
controllers and is always loaded.

To specify additional script files to load, add the following section to
the device's XML MIDI mapping file right underneath the \<controller\>
tag:

``` XML
        <scriptfiles>
            <file functionprefix="StantonSCS3d">
                <filename>Stanton-SCS3d-scripts.js</filename>
            </file>
        </scriptfiles>
```

You can add as many \<file\> blocks as you like, but be sure to specify
the appropriate function prefix in every one. These will all be loaded
when the XML file is.

### Function definitions

Data passed to functions are, in order: MIDI channel, device name,
control/note, value, and MIDI category (Note (0x9\#), Control Change
(0xB\#), etc.) Therefore, function definitions should look like:

``` javascript
StantonSCS3d.pitchSlider = function (channel, device, control, value, category) {
    ...
}
```

### Reading and setting Mixxx control values

Script functions can check Mixxx control values using
engine.getValue(\<group\>,\<key\>), where \<group\> and \<key\> are
Mixxx controls, a list of which can be found
[here](midi_controller_mapping_file_format#ui_midi_controls_and_names).
So for example:

``` javascript
var currentValue = engine.getValue("[Channel1]","rate");
```

Values can be set just as easily, using
engine.setValue(\<group\>,\<key\>,\<new value\>):

``` javascript
engine.setValue("[Channel1]","rate",0.5);
```

Note that since this is a script, you can do calculations and use state
variables so a single function can work for multiple cases, such as a
single controller working with Mixxx's two virtual decks:

``` javascript
engine.setValue("[Channel"+currentDeck+"]","rate",(currentValue+10)/2);
```

Tying it all together, here is an example of a function that reduces the
sensitivity of the SCS.3d's pitch slider (in relative mode:)

``` javascript
StantonSCS3d.pitchSlider = function (channel, device, control, value, category) {   // Lower the sensitivity of the pitch slider
    var currentValue = engine.getValue("[Channel"+StantonSCS3d.deck+"]","rate");
    engine.setValue("[Channel"+StantonSCS3d.deck+"]","rate",currentValue+(value-64)/128);
}
```

### Automatic reactions

Up to this point, script functions are only called in response to the
controller being manipulated. They can also be called automatically in
response to some value changing within Mixxx, such as when you use the
mouse to move the channel volume slider, you want the LEDs on the
controller to react.

Mixxx control signals are connected to script functions with
`engine.connectControl(<control group>,<control name>,<script function
name>)`. They are disconnected with `engine.connectControl(<control
group>,<control name>,<script function name>,true)`. (Just tack a
`,true` on to the list of parameters.) connectControl() returns true if
the (dis)connection was successful.

So to connect the volume of the current virtual deck to a function
called volumeLEDs, assuming you've already defined currentDeck, do:

``` javascript
engine.connectControl("[Channel"+currentDeck+"]","volume","volumeLEDs");
```

**Note:** Due to flaws in the current MIDI subsystem code,
<span class="underline">all signals you plan to use must be connected at
least once before any data is sent to the device</span> or they will
have no effect when connected later. (They can be connected to the "nop"
function and disconnected immediately if you wish.) A good place to do
this is in the init() function in your script file.

**Warning:** This functionality is currently unstable and will
eventually crash when controls are manipulated, especially on faster
systems. We are trying to figure out the problem. (We think it's either
a buffer overflow or a bug in QtScript.)

### Init and Shutdown functions

All device script files are expected to contain initialize and shutdown
functions (called \<manufacturer\>\<device\>.init() and
\<manufacturer\>\<device\>.shutdown() ) which will be called when Mixxx
opens and closes the device, respectively. They can be empty, but are
useful for putting controllers into known states before operation begins
or the program exits.

# MIDI Mapping Object Design Spec

*\*\*Note this block is dedicated to the internal workings of MIDI
Mapping object and dlgprefsmidibindings \*\**

### Use Cases

1.  Load Mapping from XML file
2.  User Edit Mapping
3.  Save Mapping to file
