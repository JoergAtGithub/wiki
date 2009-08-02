# MIDI Scripting

***This information may change prior to the 1.7.0 final release.***

In order to support the advanced features of many MIDI controllers,
Mixxx offers what we call MIDI Scripting. It enables MIDI controls to be
mapped to [QtScript](http://doc.trolltech.com/4.5/qtscript.html) (aka
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
                <status>0xB0</status>
                <midino>0x04</midino>
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

## Script files & functions

There is a default script function file called
`midi-mappings-scripts.js` which contains functions common to all
controllers and is always loaded. See
[below](#available-common-functions) for information on these functions.

To specify additional script files to load, add the following section to
the device's XML MIDI mapping file right underneath the \<controller\>
tag:

``` XML
        <scriptfiles>
            <file filename="Stanton-SCS3d-scripts.js" functionprefix="StantonSCS3d"/>
        </scriptfiles>
```

You can add as many \<file\> tags as you like, but be sure to specify
the appropriate function prefix in every one. These will all be loaded
at Mixxx start-up.

### Init and Shutdown functions

All device script files **are expected to contain initialize and
shutdown functions** (called `<manufacturer><device>.init(ID)` and
`<manufacturer><device>.shutdown()` ) which will be called when Mixxx
opens and closes the device, respectively. They can be empty, but are
useful for putting controllers into known states and/or lighting certain
LEDs before operation begins or the program exits. The ID parameter is
the `controller id` attribute from the XML file and is useful for
identifying the particular controller instance in print statements.

### Function definitions

**This API has changed as of 10 April 2009**

  - "Device" has been removed
  - "Category" has become "Status"
  - The .init function now requires acceptance of an ID string parameter
    (but you don't have to do anything with it.)
  - The channel numbers passed to the script now start at zero for
    simpler use in MIDI messages (0x00 = MIDI Channel 1..0x0F = MIDI
    Channel 16.)

Data passed to functions are, in order: MIDI channel, control/note,
value, and MIDI status (Note (0x9\#), Control Change (0xB\#), etc.)
Therefore, function definitions should look like:

``` javascript
ControllerName.functionName = function (channel, control, value, status) {
    ...
}
```

You can leave off any parameters at the end that you don't need; the
function is identified only by name (so make sure it's unique\!) For
example, if you don't need the MIDI status or value bytes, just do:

``` javascript
ControllerName.functionName = function (channel, control) {
    ...
}
```

*(If more than one function have the same name, only the last one listed
in the script file(s) will be called, regardless of the number of
parameters.)*

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
single controller working with Mixxx's two virtual decks (assuming
you've defined currentDeck):

``` javascript
engine.setValue("[Channel"+currentDeck+"]","rate",(currentValue+10)/2);
```

### Sending messages to the controller

You can send three-byte "short" messages and arbitrary-length
system-exclusive "long" ones. Together, these cover virtually all types
of MIDI messages you would need to send.

For short messages:

``` javascript
midi.sendShortMsg(status, byte2, byte3);
```

It's completely up to you (and your controller's MIDI spec) what those
bytes can be. (Status will usually be 0x90, 0x80 or 0xB0.)

For system-exclusive messages:

``` javascript
var byteArray = [ 0xF0, byte2, byte3, ..., byteN, 0xF7 ];
midi.sendSysexMsg(byteArray,byteArray.length);
```

Here again, it's completely up to you (and your controller's MIDI spec)
what those bytes should be for the change you wish to effect.

### Example functions

Here are some simple examples to get you started.

To control the play button for Deck 1 and light its LED:

``` javascript
Controller.playButton1 = function (channel, control, value, status) {    // Play button for deck 1
    var currentlyPlaying = engine.getValue("[Channel1]","play");
    if (currentlyPlaying == 1) {    // If currently playing
        engine.setValue("[Channel1]","play",0);    // Stop
        midi.sendShortMsg(0x80,0x11,0x00);    // Turn off the Play LED
    }
    else {    // If not currently playing,
        engine.setValue("[Channel1]","play",1);    // Start
        midi.sendShortMsg(0x90,0x11,0x7F);    // Turn on the Play LED
    }
}
```

To reduce the sensitivity of a relative-mode (touch strip) pitch slider:

``` javascript
Controller.pitchSlider1 = function (channel, control, value, status) {   // Lower the sensitivity of the pitch slider for channel 1
    var currentValue = engine.getValue("[Channel1]","rate");
    engine.setValue("[Channel1]","rate",currentValue+(value-64)/128);
}
```

To find the current elapsed time in seconds of a track on the specified
deck (intended to be called from another function):

``` javascript
Controller.elapsedTime = function (deck) {
    return engine.getValue("[Channel"+deck+"]","duration") * engine.getValue("[Channel"+deck+"]","playposition");
}
```

**IMPORTANT NOTE:** You must always declare variables with "var" when
you first use them since it establishes scope. If you omit this, the
variable becomes global and will clobber anything else with the same
name even if it's in another script file.

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
called SuperController.volumeLEDs, do:

``` javascript
engine.connectControl("[Channel"+SuperController.currentDeck+"]","volume","SuperController.volumeLEDs");
```

A function is also provided as an easy way to get a connected Mixxx
control signal to fire so the device's LEDs update (such as when
changing modes or decks.) It just sets the Mixxx control to its previous
value. This is done with `engine.trigger(<control group>,<control
name>)`. So to force the above-mentioned volumeLEDs to sync up, just do:

``` javascript
engine.trigger("[Channel"+SuperController.currentDeck+"]","volume");
```

### Object prototype enhancements

**String**.prototype**.toInt** - returns an ASCII byte array for all the
characters in any string. Use like so: `"Test string".toInt()`

### Available common functions

Here is a list of functions available to you from the always-loaded
midi-mappings-scripts.js file:

  - **nop**() - Does nothing (No OPeration.) Empty function you can use
    as a place-holder while developing to avoid errors.
  - **secondstominutes**(seconds) - Returns the given quantity of
    seconds in `MM:SS` format.
  - **msecondstominutes**(milliseconds) - Returns the given quantity of
    milliseconds in `MM:SS.ss` format.
  - **script.debug**(channel, control, value, status) - Prints the
    values as passed to it. Call this from anywhere in your function to
    see what the current values of these variables are. You can also of
    course put it in the \<key/\> tag of your XML to make sure the
    values being passed to the script are what you expect.
  - **script.pitch**(LSB, MSB, status) - Intended to be called from
    another script function, pass this the values from a MIDI Pitch
    control and it will return a corresponding value suitable for
    Mixxx's pitch sliders ("rate" controls.) So if you just want to set
    those controls, the calling function need only have the single line:
    `engine.setValue("[Channel"+deck+"]","rate",script.pitch(control,
    value, status));`
  - **script.absoluteSlider**(group, key, value, low, high) - Takes a
    value from an absolute control (0..127,) calculates the
    proportionate value between *low* and *high*, and sets the given
    Mixxx control group & key with that value.
  - **script.absoluteNonLin**(value, low, mid, high) - Takes a value
    from an absolute control (0..127) and returns the proportionate
    value between *low*, *mid* and *high* for a non-linear Mixxx control
    such as EQ or volume knobs. You can then use this returned value to
    set Mixxx controls.

<!-- end list -->

  - **bpm.tapButton**(deck) - Call this every time the desired tap
    button is pressed. It takes the progressive average of the last 8
    taps and sets the bpm of the specified deck to that value, assuming
    the pitch range is large enough to reach it. (This depends on the
    track having the correct original BPM value.) If more than two
    seconds pass between taps, the history is erased.

<!-- end list -->

  - **scratch.enable**(deck) - Initializes the variables and turns on
    scratching for the functions detailed below. Just give it the number
    of the deck you want to scratch.
  - **scratch.disable**(deck) - Disables scratching for the specified
    deck.
  - **scratch.slider**(deck, sliderValue, revtime, alpha, beta) - Allows
    you to scratch with a slider or a knob (values 0..127.) 0-\>127 is
    the forward track direction. Call this each time there's a new
    control value.
  - Inputs:

<!-- end list -->

``` 
    * The number of the deck you want to scratch (same as above)
    * The new value of the slider/knob
    * Revolution time of the imaginary record (typically 1.8s for a 12-inch record at 33 & 1/3 RPM, adjust for comfort)
    * Coefficients for the filter. Alpha isn't currently used at all, but it needs to be set to something, so just use 0.1.
    * Beta adjusts how quickly Mixxx responds to your motions. The value should be between 0 and 1, though I find that 0.9-1 works well.
* Output: A new value for Mixxx's "scratch" control. Simply call engine.setValue("[Channel"+currentDeck+"]", "scratch", <returned value here>); in your function.
* **scratch.wheel**(deck, wheelValue, revtime, alpha, beta) - Same thing but for a rotary control that wraps from 127 to 0 (or 0 to 127 depending on the direction.)
```
