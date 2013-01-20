# MIDI Scripting

In order to support the advanced features of many MIDI controllers,
Mixxx offers what we call MIDI Scripting (introduced in Mixxx v1.7.0.)
It enables MIDI controls to be mapped to
[QtScript](http://doc.trolltech.com/4.5/qtscript.html) (aka
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
`<manufacturer>-<device>-scripts.js` (e.g. `Stanton-SCS3d-scripts.js`)
and are found in the midi/ subdirectory wherever your Mixxx shared data
is stored. (Usually `/usr/share/mixxx` on Linux/Mac, and `C:\Program
Files\Mixxx` on Windows.) Functions use the naming convention
`<manufacturer><device>.<function name>` (e.g.
`StantonSCS3d.pitchSlider`). Global variables use
`<manufacturer><device>.<variable name>` (e.g. `StantonSCS3d.deck`).
These are very important to avoid name collisions with other scripts
that may be loaded.

## Linking scripts to device controls

MIDI controller mapping files are described on [MIDI controller mapping
file
format](http://www.mixxx.org/wiki/doku.php/midi_controller_mapping_file_format)
page. This XML file defines how MIDI controls are mapped to MIDI
commands.

To link a script function to a particular control in the device's XML
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
it still needs to be valid or the XML parser will report an error. It is
also passed to the function as an extra parameter (since v1.8.) (This is
useful for dual-deck controllers since you only need one function that
checks the \<group\> and reacts appropriately.) No tags or options are
considered other than those shown above, so you can leave them out.

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
when the controller is activated.

### Script file header

At the top of your script file, you need to have a declaration of the
controller name. It looks like this:

    function StantonSCS3d() {}

...and you would replace the name with whatever you entered for
'functionprefix' in the XML file above.

### Init and Shutdown functions

**All device script files are expected to contain initialize and
shutdown functions** (called `<manufacturer><device>.init(ID,debugging)`
and `<manufacturer><device>.shutdown()` ) which will be called when
Mixxx opens and closes the device, respectively. They can be empty, but
are useful for putting controllers into known states and/or lighting
certain LEDs before operation begins or the program exits. The ID
parameter is the `controller id` attribute from the XML file and is
useful for identifying the particular controller instance in print
statements and the `debugging` parameter is set to **true** if the user
specified controller debugging on the command line. (v1.11 and higher.)

### Function definitions

Data passed to functions are, in order:

1.  MIDI channel (0x00 = Channel 1..0x0F = Channel 16,)
2.  Control/note number (byte 2)
3.  Value of the control (byte 3)
4.  MIDI status byte (Note (0x9\#), Control Change (0xB\#), Pitch
    (0xE\#) etc.)
5.  MixxxControl group (from the \<group\> value in the XML file, since
    v1.8)

Therefore, function definitions should look like:

``` javascript
ControllerName.functionName = function (channel, control, value, status, group) {
    ...
}
```

You can leave off any parameters at the end that you don't need; the
function is identified only by name (so make sure it's unique\!) For
example, if you only need the MIDI channel and control number, just do:

``` javascript
ControllerName.functionName = function (channel, control) {
    ...
}
```

*(If more than one function have the same name, only the last one listed
in the script file(s) will be called, regardless of the number of
parameters.)*

### Reading and setting Mixxx control values

Script functions can check and set Mixxx control values using the
following functions:

``` c++
engine.getValue(string group, string key);
engine.setValue(string group, string key, double newValue);
```

To check a Mixxx control value, call `engine.getValue()` with the
"`group`" and "`key`" values for a particular Mixxx control, a list of
which can be found
[here](midi_controller_mapping_file_format#ui_midi_controls_and_names).
So for example:

``` javascript
var currentValue = engine.getValue("[Channel1]","rate");
```

Values can be set just as easily by calling `engine.setValue()` with the
`group` and `key` as above, and the new value to set, like so:

``` javascript
engine.setValue("[Channel1]","rate",0.5);
```

Note that since this is a script, you can do calculations and use state
variables so a single function can work for multiple cases, such as a
single controller working with Mixxx's multiple virtual decks (assuming
you've defined `currentDeck` and `currentValue` here):

``` javascript
engine.setValue("[Channel"+currentDeck+"]","rate",(currentValue+10)/2);
```

### Soft-takeover

*Introduced in v1.10.0.*

To prevent sudden wide parameter changes when the on-screen control
diverges from a hardware control, use soft-takeover. While it's active
on a particular parameter, manipulating the control on the hardware will
have no effect until the position of the hardware control is close to
that of the software, at which point it will take over and operate as
usual. You can enable and disable it at any point, and it operates on
each MixxxControl independently. Typically, for each control that has
physical limits on your controller, you would enable soft-takeover in
the `init()` script function and just leave it enabled.

It's very simple to use:

``` c++
engine.softTakeover(string group, string key, bool enable);
```

So to enable soft-takeover for the pitch control on channel
1:`engine.softTakeover("[Channel1]","rate",true);
` ...and to disable it: `engine.softTakeover("[Channel1]","rate",false);
`

### Scratching

*Introduced in v1.8, ramp toggles and isScratching() added in v1.11*

We have an easy way to scratch with any MIDI control that sends relative
(+1/-1) signals. (Others can be scaled to work as well.) The applicable
functions are:

``` c++
engine.scratchEnable(int deck, int intervalsPerRev, float rpm, float alpha, float beta, bool ramp);
engine.scratchTick(int deck, int interval);
engine.scratchDisable(int deck, bool ramp);
bool engine.isScratching(int deck);
```

Here is how to use them:

1.  When you want to start scratching (such as when the wheel is
    touched,) call `engine.scratchEnable()` with:

<!-- end list -->

  - the virtual deck number you want to scratch
  - the resolution of the MIDI control (in intervals per revolution,
    typically 128.)
  - the speed of the imaginary record at 0% pitch (in revolutions per
    minute (RPM) typically 33+1/3, adjust for comfort)
  - the filter coefficients (these affect responsiveness and looseness
    of the imaginary slipmat)

<!-- end list -->

``` 
    * the alpha value for the filter (start with 1/8 (0.125) and tune from there)
    * the beta value for the filter (start with alpha/32 and tune from there)
* whether you want Mixxx to ramp the deck speed down or to stop instantly. (TRUE for ramping, which is the default.)
- Each time the MIDI control is moved, call ''engine.scratchTick()'' with:
* the virtual deck number this control is currently scratching
* the movement value (typically 1 for one "tick" forwards, -1 for one "tick" backwards)
- When you're done scratching (like when the wheel is released,) just call ''engine.scratchDisable()'' with the number of the virtual deck to stop scratching and whether you want Mixxx to ramp up to the play speed or jump to it instantly. (Default is to ramp which also allows spin-backs with wheels.)
```

Here is an example for the two most common types of wheels:

``` javascript
// The button that enables/disables scratching
MyController.wheelTouch = function (channel, control, value, status) {
    if ((status & 0xF0) == 0x90) {    // If button down
  //if (value == 0x7F) {  // Some wheels send 0x90 on press and release, so you need to check the value
        var alpha = 1.0/8;
        var beta = alpha/32;
        engine.scratchEnable(MyController.currentDeck, 128, 33+1/3, alpha, beta);
        // Keep track of whether we're scratching on this virtual deck - for v1.10.x or below
        // MyController.scratching[MyController.currentDeck] = true;
    }
    else {    // If button up
        engine.scratchDisable(MyController.currentDeck);
        //MyController.scratching[MyController.currentDeck] = false;  // Only for v1.10.x and below
    }
}

// The wheel that actually controls the scratching
MyController.wheelTurn = function (channel, control, value, status) {
    // See if we're scratching. If not, skip this.
    if (!engine.isScratching(MyController.currentDeck)) return; // for 1.11.0 and above
    //if (!MyController.scratching[MyController.currentDeck]) return; // for 1.10.x and below
    
    // --- Choose only one of the following!
    
    // A: For a control that centers on 0:
    var newValue;
    if (value-64 > 0) newValue = value-128;
    else newValue = value;
    
    // B: For a control that centers on 0x40 (64):
    var newValue=(value-64);
    
    // --- End choice
    
    // In either case, register the movement
    engine.scratchTick(MyController.currentDeck,newValue);
}
```

And that's it\! Just make sure to map the button/touch sensor and wheel
to these script functions [as described
above](#linking-scripts-to-device-controls) and you'll be ready to tear
up some tracks.

### Sending messages to the controller

You can send three-byte "short" messages and arbitrary-length
system-exclusive "long" ones to the controller using the following
functions:

``` c++
midi.sendShortMsg(status, byte2, byte3);
midi.sendSysexMsg(data, length);
```

Together, these cover virtually all types of MIDI messages you would
need to send. (This is how you light LEDs, change displays, etc.)

For short messages, call `midi.sendShortMsg()` with:

  - the MIDI status byte
  - the second data byte
  - the third data byte

It's completely up to you (and your controller's MIDI spec) what those
bytes can be. (Status will usually be 0x90, 0x80 or 0xB0.) For example:

``` javascript
midi.sendShortMsg(0x90,0x11,0x01);   // This might light an LED
```

For system-exclusive messages, call `midi.sendSysexMsg()` with:

  - An array of data bytes to send, always leading with `0xF0` and
    ending with `0xF7`
  - The number of bytes in the array, including the 0xF0 and 0xF7 (start
    counting with 1 or just use the .length property as below)

<!-- end list -->

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
MyController.playButton1 = function (channel, control, value, status) {    // Play button for deck 1
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
(assuming \<group\> is specified appropriately in the XML file)

``` javascript
MyController.pitchSlider = function (channel, control, value, status, group) {   // Lower the sensitivity of the pitch slider
    var currentValue = engine.getValue(group,"rate");
    engine.setValue(group,"rate",currentValue+(value-64)/128);
}
```

To find the current elapsed time in seconds of a track on the specified
deck (intended to be called from another function):

``` javascript
MyController.elapsedTime = function (deck) {
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
controller to react. Here are the related functions:

  - **engine.connectControl**(*control group*, *control name*, *script
    function name*) - This connects the specified Mixxx control signal
    to the specifed script function. It returns true if the connection
    was successful.
  - **engine.connectControl**(*control group*, *control name*, *script
    function name*, **true**) - Tacking a `,true` on to the list of
    parameters disconnects the specified Mixxx control signal from the
    specified script function. It returns true if the disconnection was
    successful.
  - **engine.trigger**(*control group*, *control name*) - An easy way to
    cause the specified Mixxx control signal to fire so the connected
    script function is called with the updated value even if it hasn't
    changed, such as when forcing LEDs to update on a mode change.

As of at least Mixxx 1.10, connected functions are passed three
parameters: the new value of the MixxxControl, the group, and the Mixxx
control name. So, your connected function can look like this:

``` javascript
MyController.volumeLEDs = function (value, group, control) {
    //...what to do with the value goes here...
}
```

Or like this:

``` javascript
MyController.volumeLEDs = function (value) {
    //...what to do with the value goes here...
}
```

#### Examples

To connect the volume of the current virtual deck to a function called
MyController.volumeLEDs, do:

``` javascript
engine.connectControl("[Channel"+MyController.currentDeck+"]","volume","MyController.volumeLEDs");
```

To force the above-mentioned volume LEDs to sync up, just do:

``` javascript
engine.trigger("[Channel"+MyController.currentDeck+"]","volume");
```

If you change what the volume LEDs represent (like when switching
modes,) you would disconnect the Mixxx "volume" control from them like
this:

``` javascript
engine.connectControl("[Channel"+MyController.currentDeck+"]","volume","MyController.volumeLEDs",true);
```

### Timed reactions

*Introduced in v1.8*

Sometimes you need to be able to do things at certain time intervals
regardless of whether the controller is manipulated or something changes
in Mixxx. Timed reactions let you do just that with 20ms resolution.
Here are the functions:

  - **engine.beginTimer**(*milliseconds*, `"function"`, *one-shot*) -
    Starts a timer that will call the specified script function (with
    parameters if desired) repeatedly every time (if *one-shot* is false
    or not present) or just once (if *one-shot* is true) the given
    number of milliseconds (1/1000 second) pass. It returns an ID number
    for the timer (0 on failure) that you'll want to store in a variable
    so you can stop it later if it's a repeating timer. Note that the
    function must be enclosed in quotes.
  - **engine.stopTimer**(*timer ID*) - Stops the specified timer.

You can create and stop timers as much as you like but be aware that the
operating system has limits on the number of timers it will allow, so
remember to stop them as soon as you're done with them. (Not to mention
that overall performance decreases as the number and/or frequency of
timers increase.)

**NEVER use busy-wait loops\!** (Loops that do nothing but delay. They
can cause Mixxx to stutter.) **Always use a timer instead\!**

#### Examples

To start a timer to flash LEDs on a controller 4 times per second
(250ms) and store the ID in an array for later you would do:

``` javascript
    MyController.timer[0] = engine.beginTimer(250,"MyController.flash()");
```

When the LEDs need to stop flashing, just do:

``` javascript
    engine.stopTimer(MyController.timer[0]);
```

This one-shot timer example causes an LED (note number 0x3A in this
case) to light up red one second after the beginTimer call: (Note the
escaped quotes in the target function call.)

``` javascript
...
    if (engine.beginTimer(1000,"MyController.lightUp(0x3A,\"red\")",true) == 0) {
        print("LightUp timer setup failed");
    }
...

MyController.lightUp = function (led,color) {
    switch (color) {
        case "red": 
            midi.sendShortMsg(0x90,led,0x01);
            break;
        case "green": 
            midi.sendShortMsg(0x90,led,0x02);
            break;
        default:
            print("Warning: no color specified, using blue");
            midi.sendShortMsg(0x90,led,0x03);
            break;
    }
}
...
```

### Spinback and Brake effect

*Introduced in v1.11*

A forwards or backwards brake effect can be enabled/disabled using one
of the two following functions. engine.spinback() just calls
engine.brake() with default settings to make it behave like a spinback.

``` javascript
brake(int deck, bool activate, [float factor], [float rate])
spinback(int deck, bool activate, [float factor], [float rate])
```

  - **deck** - the deck number to use, e.g: 1
  - **activate** - true to activate or false to disable. 
  - **factor** (optional) - how quickly the deck should come to a stop.
    start with a value of 1 and increase to increase the deceleration
  - **rate** (optional) - the initial speed of the deck when enabled.
    "1" means normal speed forwards, "-10" means 10x speed in reverse

Example:

``` javascript
    MyControllerPrefix.brake_button = function(channel, control, value, status, group) {
        var deck = parseInt(group.substring(8,9)); // work out which deck we are using 
        var activate = value > 0:
        
        if (activate) {
            engine.brake(deck, true); // enable brake effect
        }
        else {
            engine.brake(deck, false); // disable brake effect
        }   
    }
```

``` javascript
    MyControllerPrefix.spinback_button = function(channel, control, value, status, group) {
        var deck = parseInt(group.substring(8,9)); // work out which deck we are using 
        engine.brake(deck, value > 0, 1.2, -10); // start at a rate of -10 and decrease at a factor of 1.2
    }
```

``` javascript
    MyControllerPrefix.spinback_button = function(channel, control, value, status, group) {
        var deck = parseInt(group.substring(8,9)); // work out which deck we are using
        engine.spinback(deck, value > 0, 2.5); // use default starting rate of -10 but decrease speed more quickly
    }
```

The effects can also be mapped directly via XML using either
**script.spinback** or **script.brake**:

``` XML
    <control>
        <group>[Channel1]</group>
        <key>script.spinback</key>
        <status>0x90</status>
        <midino>0x04</midino>
        <options>
            <Script-Binding/>
        </options>
    </control>
```

### Object prototype enhancements

**String**.prototype**.toInt** - returns an ASCII byte array for all the
characters in any string. Use like so: `"Test string".toInt()`

### Available common functions

Here is a list of functions available to you from the always-loaded
common-controller-scripts.js file:

  - **nop**() - Does nothing (No OPeration.) Empty function you can use
    as a place-holder while developing to avoid errors.
  - **secondstominutes**(*seconds*) - Returns the given quantity of
    seconds in `MM:SS` format.
  - **msecondstominutes**(*milliseconds*) - Returns the given quantity
    of milliseconds in `MM:SS.ss` format.
  - **script.midiDebug**(channel, control, value, status,
    group)<sup>2</sup> - Prints the values as passed to it. Call this
    from anywhere in your function to see what the current values of
    these variables are. You can also of course put it in the \<key/\>
    tag of your XML to make sure the values being passed to the script
    are what you expect.
  - **script.pitch**(LSB, MSB, status) - Intended to be called from
    another script function, pass this the values from a MIDI Pitch
    control and it will return a corresponding value suitable for
    Mixxx's pitch sliders ("rate" controls.) So if you just want to set
    those controls, the calling function need only have the single line:
    `engine.setValue("[Channel"+deck+"]","rate",script.pitch(control,
    value, status));`
  - **script.crossfaderCurve**(value, min, max)<sup>1</sup> - Sets the
    cross-fader's curve based on a value from an absolute control
    (0..127 by default, customize with min and max.)
  - **script.absoluteLin**(value, low, high, min, max)<sup>2</sup> -
    Takes a value from an absolute control (0..127 by default, customize
    with min and max) and returns the proportionate value between *low*
    and *high* for a linear Mixxx control like deck volume or LFO depth.
    You can then use this returned value to set the desired Mixxx
    control.
  - **script.absoluteNonLin**(value, low, mid, high, min, max) - Takes a
    value from an absolute control (0..127 by default, customize with
    min and max) and returns the proportionate value between *low*,
    *mid* and *high* for a non-linear Mixxx control such as EQ or master
    volume. You can then use this returned value to set the desired
    Mixxx control.

<!-- end list -->

  - **bpm.tapButton**(deck) - Call this every time the desired tap
    button is pressed. It takes the progressive average of the last 8
    taps and sets the bpm of the specified deck to that value, assuming
    the pitch range is large enough to reach it. (This depends on the
    track having the correct original BPM value.) If more than two
    seconds pass between taps, the history is erased.

<sup>1</sup> Introduced in 1.11.0 <sup>2</sup> Renamed in 1.11.0
