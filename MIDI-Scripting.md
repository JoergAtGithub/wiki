# Controller Scripting

In order to support the features of many MIDI controllers, Mixxx offers
what we call MIDI Scripting (introduced in Mixxx v1.7.0). It enables
MIDI controls to be mapped to
[QtScript](http://doc.trolltech.com/4.5/qtscript.html) (also known as
[Javascript](http://en.wikipedia.org/wiki/JavaScript_syntax)/[EMCAScript](http://www.ecma-international.org/publications/standards/Ecma-262.htm))
functions, allowing mappings to manage complex behaviors. These
user-created functions can then do anything desired with the MIDI event
info such as affect different controls depending on whether another
button is pressed, adjust incoming control values to work better with
Mixxx (i.e. for [scratching](#Scratching-and-jog-wheels)), send messages
to LED displays on the controller, or even [turn a 2 deck controller
into a 4 deck
controller](#turning-a-2-deck-controller-into-a-4-deck-controller).

If you would like your mapping included in Mixxx, please see the coding
guidelines on the [Contributing Mappings](Contributing%20Mappings) page.

JavaScript is mostly used for programming complex functionality in Web
pages. There are many tutorials online, such as
[W3Schools](http://www.w3schools.com/js/default.asp), aimed at people
who have never programmed before. However, understanding them may
require understanding HTML, the language used to write Web pages. HTML
is fairly simple and easy to learn the basics. It is very similar to
XML, the language used for Mixxx's [MIDI controller mapping file
format](MIDI%20controller%20mapping%20file%20format). The [\#additional
examples](#additional%20examples) section at the bottom of this page is
aimed at people with little or no programming experience. It has
examples for common uses of MIDI scripting to help get you started
writing code in an organized and maintainable way from the start. This
will make it easier for you and other people to edit the code later.

If you have any programming experience, you can probably learn the
basics of JavaScript quickly and easily. Mozilla Developer Network has
helpful resources for JavaScript programming that focus on the language
itself without regards to the Web, although these may not be very easy
to understand for people without any programming experience:

  - [Language basics crash
    course](https://developer.mozilla.org/en-US/Learn/Getting_started_with_the_web/JavaScript_basics#Language_basics_crash_course)
  - [JavaScript
    Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_Types),
    a more thorough tutorial
  - [MDN's A Re-Introduction To
    JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript):
    recommended to understand the more unusual aspects of JavaScript
  - [JavaScript
    Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)

Here are some resources for a deeper understanding of JavaScript:

  - [Douglas Crockford's JavaScript
    website](http://javascript.crockford.com/)
  - [Douglas Crockford on JavaScript -- Act III: Function the
    Ultimate](http://yuiblog.com/blog/2010/02/24/video-crockonjs-3/)
  - [Private Members in
    JavaScript](http://javascript.crockford.com/private.html)
  - [JavaScript: The Definitive
    Guide](http://shop.oreilly.com/product/9780596805531.do)

If you are unfamiliar with MIDI, see the [MIDI Crash
Course](MIDI%20Crash%20Course) page.

**Tip:** If there is already a Mixxx mapping for a controller made by
the same manufacturer as your controller, you may want to look at that
mapping for examples. The controllers likely send similar types of
signals (although they could be very different).

**Tip:** When you're testing your scripts, you don't have to restart
Mixxx. Every time you save your file, Mixxx will reload it immediately.
This can make testing changes very fast.

## Set up a JavaScript mapping

### Specify the JS file

All JavaScript files need an accompanying [XML mapping
file](MIDI%20controller%20mapping%20file%20format). See the [controller
mapping file locations](controller%20mapping%20file%20locations) for
where to put mapping files on your OS.

To specify script files to load, add the following section to the
device's XML file inside the \<controller\> tag:

``` XML
 <controller id="controller">
        <scriptfiles>
            <file filename="Manufacturer-model-scripts.js" functionprefix="MyController"/>
        </scriptfiles>
        
```

The functionprefix attribute specifies the name of the JavaScript object
in the file that has init and shutdown methods called when the
controller is opened and closed by Mixxx (typically when the user opens
and closes Mixxx).

You can add as many \<file\> tags as you like, but be sure to specify
the appropriate functionprefix in every one. These will all be loaded
when the controller is activated.

There is a default script function file called
`common-controller-scripts.js` which contains functions common to all
controllers and is always loaded. See [Helper
functions](#Helper-functions) below for information on these
functions.

### Script file header

In your script file, you need to have a declaration of the controller's
object. It looks like this:

``` js
// eslint-disable-next-line no-var
var MyController = {};
```

...and you would replace `MyController` with whatever you entered for
'functionprefix' in the XML file above. This declares a new JavaScript
variable representing your controller (in this example, called
`MyController`) and assigns it to an empty object.

This object should have properties called "init" and "shutdown" defined
and assigned to functions (in JavaScript, object methods are just
properties whose value is a function). They can be empty, but are useful
for putting controllers into known states and/or lighting certain LEDs
before operation begins or the program exits. Some controllers can be
sent a MIDI message that tells the controller to send back MIDI messages
for the position of the controls on the device. If your controller can
do this, it is helpful to send that message from the init function so
the state of Mixxx's controls match the hardware when Mixxx opens. For
controllers designed for Serato, this can be done by sending the [Serato
sysex](Serato%20sysex) message.

For example, if there are 40 LEDs on your controller that respond to
MIDI note numbers 1 through 40 that turn on when sent value 0x7f and
turn off when sent value 0x00, your script could start with:

``` js
var MyController = {};

MyController.init = function (id, debugging) {
    // turn on all LEDs
    for (var i = 1; i <= 40; i++) { // Repeat the following code for the numbers 1 through 40
                                // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for
        midi.sendShortMsg(0x90, i, 0x7f);
    }
}

MyController.shutdown = function() {
   // turn off all LEDs
   for (var i = 1; i <= 40; i++) {
        midi.sendShortMsg(0x90, i, 0x00);
    }
}
```

The ID parameter of the init function is the `controller id` attribute
from the XML file. This can be used to identify the particular
controller instance in print statements. The `debugging` parameter is
set to 'true' if the user specified the `--controllerDebug` parameter on
the command line (`--midiDebug` until Mixxx 1.10).

**Note**: Instead of using global variables, define properties of your
controller object (`MyController` in this example) to avoid name
collisions with other scripts that may be loaded.

### Link MIDI input signals to JavaScript

To link a script function to an incoming MIDI message, put the full
function name in the \<key\> tag of the MIDI message's \<control\>
element in the XML file, with a \<Script-Binding/\> tag in the
\<options\> block, like so:

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
it is available to the script function as an extra parameter. This can
be useful so one script function can be used for manipulate decks.

When Mixxx receives a MIDI signal with the first two bytes matching the
\`\<status\>\` and \`\<midino\>\` elements, the named script function is
called. That function then determines how to change the state of Mixxx
and/or script variables.

For system exclusive messages, the status byte must be `0xF0` and there
does not need to be a `midino` element. If the controller can send
multiple different SysEx messages, the one script function specified by
the `<key>` element is responsible for deciding which has been received
then taking the appropriate action.

*New in 2.1*: The value of the \<key\> element can be any snippet of
JavaScript code that evaluates to a function (when executed in the
global context).

## JavaScript mapping basics

### MIDI input handling functions

#### Short 3-byte messages

Except for system exclusive message, most MIDI signals are 3 byte
messages. The parameters passed to [functions linked to MIDI input from
the controller in the XML
file](#linking-MIDI-signals-to-JavaScript-functions) are, in order:

1.  MIDI channel (0x00 = Channel 1..0x0F = Channel 16,)
2.  Control/note number (byte 2)
3.  Value of the control (byte 3)
4.  MIDI status byte (byte 1)
5.  MixxxControl group (from the \<group\> value in the XML file)

Therefore, function definitions should look like:

``` javascript
ControllerName.functionName = function (channel, control, value, status, group) {
    // your custom code goes here
}
```

Note that in JavaScript, everything is an
[object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object).
This code does not define a function as is done in many other
programming languages; it defines a property of the [ControllerName
object](#script-file-header) called `functionName` and assigns its value
to the function expression on the right of the `=` assignment operator.
So, `MyController.functionName` is a variable that could be reassigned
to a different function by the script at any time to change how the
mapping handles input for this MIDI signal.

You can leave off parameters you don't need from the end of the function
declaration, but the parameters must stay in order. For example, if you
don't need the `status` or `group` variables, you can define an input
handling function like:

``` javascript
ControllerName.functionName = function (channel, control, value) {
    // your custom code goes here
}
```

#### System Exclusive messages

Data passed from SysEx messages to functions are, in order:

1.  an array of raw data bytes
2.  the length of that array

Therefore, function definition should look like:

``` javascript
ControllerName.inboundSysex = function (data, length) {
    ...
}
```

If the controller can send multiple different SysEx messages, this one
script function is responsible for deciding which has been received then
taking the appropriate action.

*Note that some controllers may send bytes that violate MIDI standards,
e.g. setting the high bit in a data byte or using undefined status bytes
(like `0xF9`.) On Linux, recent versions of ALSA (from November 2012
onward) automatically standardize these by breaking the bytes into two
nybbles and sending two bytes for every one received from the
controller. For example `0xF0 0x97 0x30 0xF7` would become
`0xF0 0x09 0x07 0x03 0x00 0xF7.` Consult the ALSA documentation for full
details.*

### Interact with Mixxx

Scripts can access the state of Mixxx through the [Mixxx
Control](MixxxControls) system using the following functions:

``` javascript
engine.getParameter(string group, string key);
engine.setParameter(string group, string key, double newValue);
engine.getValue(string group, string key);
engine.setValue(string group, string key, double newValue);
```

To check a Mixxx control value, call `engine.getParameter()` with the
"`group`" and "`key`" values for a particular Mixxx Control, a list of
which can be found [here](mixxxcontrols). For example:

``` javascript
var currentValue = engine.getParameter("[Channel1]", "rate");
```

Values can be set by calling `engine.setParameter()` with the `group`
and `key` as above, and the new value to set, like so:

``` javascript
engine.setParameter("[Channel1]", "rate", 0.5);
```

`engine.getParameter` and `engine.setParameter` work with values on a
scale from 0 to 1. These should be used for Mixxx Controls with a
continuous range like `volume`, `rate`, and `parameterN`. The older
`engine.getValue` and `engine.setValue` functions work with values on
the scale listed for each Control on the [MixxxControls](MixxxControls)
page. The `engine.get/setValue` functions should be used for Controls
with discrete states like `orientation`.

Note that since this is a script, you can do calculations and use state
variables so a single function can work for multiple cases, such as a
single controller working with Mixxx's multiple virtual decks (assuming
you've defined `currentDeck` and `currentValue` here):

``` javascript
engine.setValue("[Channel"+currentDeck+"]", "rate", (currentValue+10)/2);
```

**Tip**: For toggling the state of a binary Mixxx Control, the
`script.toggleControl(string group, string key)` function can be used as
a convenient shortcut.

### Connect output callback functions

To keep the state of your controller in sync with the state of Mixxx,
register callback functions that Mixxx will execute when the state of a
[Mixxx Control](MixxxControls) changes. Typically these callback
functions will [\#send MIDI output to the
controller](#send%20MIDI%20output%20to%20the%20controller), but they can
also be used to change the state of script variables.

Callback functions are registered with the `engine.makeConnection`
function, which takes 3 parameters:

1.  group of the Mixxx Control (string)
2.  name of the Mixxx Control (string)
3.  JavaScript function to execute when the Mixxx Control changes. This
    function takes three parameters: the new value of the Mixxx Control,
    the group, and the Mixxx Control name. `this` in the context of the
    function refers to the value of `this` where `engine.makeConnection`
    was called.

For example:

``` javascript
var syncButtonOutputCallback = function (value, group, control) {
    midi.sendShortMsg(byte 1, byte 2, value * 127); // see section below for an explanation of this example line
};

var syncConnection = engine.makeConnection('[Channel1]', 'sync_enabled', syncButtonOutputCallback);
```

`engine.makeConnection` returns an object that represents the callback
connection. This object should be stored in a script variable. To switch
the controller between different modes, such as controlling a different
deck:

 - disconnect the old connection object by calling its ''disconnect'' method (with no arguments)
 - register the new connection with ''engine.makeConnection''
 - call the ''trigger'' method of the new connection object (with no arguments) to immediately execute the callback using the state of the new Mixxx Control.

For example:

``` javascript
// when switching to deck 3:
syncConnection.disconnect();
syncConnection = engine.makeConnection('[Channel3]', 'sync_enabled', syncButtonOutputCallback);
syncConnection.trigger();
```

*New in Mixxx 2.3:* You can check if a connection is disconnected by
checking `isConnected` or by comparing the return value of
`disconnect()`:

``` javascript
var syncConnection = engine.makeConnection('[Channel1]', 'sync_enabled', function () {});

print(syncConnection.isConnected); // prints true
var successful_disconnect = syncConnection.disconnect();
if (successful_disconnect) {
    print("syncConnection has been successfully disconnected");
} else {
    print("There was an error disconnecting SyncConnection");
    // can happen when the connection has already been disconnected
}
print(syncConnection.isConnected); // prints false in most cases

```

#### Mixxx 2.0 and older

These functions are deprecated because there is no way to individually
disconnect or trigger specific callback functions when multiple
callbacks were connected to the same Mixxx Control. Do not use these
functions in new code. This documentation is kept here to help
understand old code.

  - **engine.connectControl**(*control group*, *control name*, *script
    function*) - Connects the specified Mixxx control signal to the
    script function. The script function can either be a JavaScript
    function or a string of JavaScript code that evaluates to a
    function.
  - **engine.connectControl**(*control group*, *control name*, *script
    function name*, **true**) - Tacking a `, true` on to the list of
    parameters disconnects the specified Mixxx Control from the
    specified script function. However, this only works when the script
    function is specified as a string of JavaScript code that evaluates
    to a function, not when an actual JavaScript function is passed.
  - **engine.trigger**(*control group*, *control name*) - Cause the
    specified Mixxx Control signal to fire so the connected script
    function is called with the updated value even if it hasn't changed,
    such as when forcing LEDs to update on a mode change. If multiple
    callbacks are connected, they will all be executed. This will only
    trigger connected JavaScript functions and will not refresh outputs
    connected in XML.

### Send MIDI output to the controller

To light LEDs and change other states of the controller, send MIDI
messages back to the controller from your script. There are different
functions for typical three-byte "short" messages and less common
system-exclusive "long" messages:

``` c++
midi.sendShortMsg(byte1, byte2, byte3);
midi.sendSysexMsg([array of bytes], length);
```

Generally, buttons have their LEDs controlled by sending a 3 byte short
message with the same first two bytes as when the controller sends a
signal for a button press. For example, if the controller sends a
`0x91, 0x11, 0x7F` message when a button is pressed, calling
`midi.sendShortMsg(0x91, 0x11, 0x7F)` will light the LED and calling
`midi.sendShortMsg(0x91, 0x11, 0x00)` will turn the LED off. If the LED
has multiple colors, typically the color is determined by the third
byte.

An explanation of the MIDI signals that your controller sends and
receives should be available from the controller manufacturer. This is
likely in a document on the product page for your controller on the
manufacturer's website. If it is not in a separate document, it is
likely at the end of the manual. If you cannot find this documentation,
contact the manufacturer to ask for it. If they do not provide it, you
will have to intercept the MIDI messages other DJ software uses or guess
and check to figure out the messages to send to your controller. To
intercept MIDI messages from other programs, you can use
[MIDIOX](http://www.midiox.com/) on Windows or [MIDI
Monitor](https://www.snoize.com/MIDIMonitor/) on Mac OS X.

For system-exclusive messages, call `midi.sendSysexMsg()` with:

  - An array of data bytes to send, always leading with `0xF0` and
    ending with `0xF7`
  - The number of bytes in the array, including the 0xF0 and 0xF7 (start
    counting with 1 or just `Array.prototype.length` property as below)

<!-- end list -->

``` javascript
var byteArray = [ 0xF0, byte2, byte3, ..., byteN, 0xF7 ];
midi.sendSysexMsg(byteArray, byteArray.length);
```

Generally, you should not call `midi.sendShortMsg` or
`midi.sendSysexMsg` directly from functions that handle MIDI input.
Instead, the input function should change the state of a [Mixxx
Control](MixxxControls) and you should call
`midi.sendShortMsg`/`midi.sendSysexMsg` in a callback function that
reacts to changes in that Mixxx Control. Refer to the section above for
details. This way, the state of the controller will always be in sync
with what Mixxx is actually doing, even if the user manipulates Mixxx
with the keyboard, mouse, or another controller. If the MIDI input
handling function only changes the state of script variables but not
Mixxx Controls, then it would be appropriate to call
`midi.sendShortMsg`/`midi.sendSysexMsg` from the input handling
function.

## Debugging your mappings

As mentioned above, you don't have to restart Mixxx, when you're testing
your scripts. Every time you save your file, Mixxx will reload it
immediately. Additionally if you specify `--controllerDebug` (or
`--midiDebug` prior to verion 1.11), Mixxx then logs all incoming and
outgoing MIDI messages. Also you can use `print()` in your script to
output further messages. The second parameter passed to your `init()`
functions specifies if the controller debug mode is enabled.

## Components library

Now that you understand the basics, it is suggested to use the
[Components JS](Components%20JS) library for new mappings.

## Soft-takeover

To prevent sudden wide parameter changes when the on-screen control
diverges from a hardware control, use soft-takeover. While it's active
on a particular parameter, manipulating the control on the hardware will
have no effect until the position of the hardware control is close to
that of the software, at which point it will take over and operate as
usual. You can enable and disable it at any point, and it operates on
each MixxxControl independently. Typically, for each control that has
physical limits (typically, knobs and sliders) on your controller, you
would enable soft-takeover in the `init()` script function and just
leave it enabled.

It's very simple to use:

``` javascript
engine.softTakeover(string group, string key, bool enable);
```

So to enable soft-takeover for the pitch control on channel
1:`engine.softTakeover("[Channel1]", "rate", true);
` (You can disable it by changing `true` to `false`, but there generally
is no need to do that.)

Note that this only works for controls manipulated through
`engine.setValue()` or `engine.setParameter()` in a script. It does not
work for controls mapped in an XML file.

If you change the functionality of an absolute control (one that has
hard stops, max and min position, not infinite encoder) which is
controlling [mixxxcontrols](mixxxcontrols) and has soft-takeover
enabled, you will need to tell Mixxx each time you change its
functionality (e.g. press *shift* button) what physical rotary you are
manipulating. This will prevent an abrupt jump to its current value from
the old one, when switching the old functionality back (i.e. *unshift*).
Do this with the following function, supplying the MixxxControl you're
switching control *away* from:

``` javascript
engine.softTakeoverIgnoreNextValue("[Channel1]", "rate");
```

This should be called when receiving MIDI input for the knob/fader that
switches its behavior. If it is called unconditionally when switching to
another layer and the user doesn't actually move the knob/fader before
the next layer change, Mixxx will mistakenly initiate soft takeover if
the user moves the knob/fader fast enough.

## Scratching and jog wheels

Typically jog wheels are mapped so they control scratching when touched
from the top and temporarily bend the pitch (speed up/slow down
playback) when touched from the side, like a turntable. We have an easy
way to scratch with jog wheels that send relative (+1/-1) signals.
(Others can be scaled to work as well.) The applicable functions are:

``` c++
engine.scratchEnable(int deck, int intervalsPerRev, float rpm, float alpha, float beta, bool ramp);
engine.scratchTick(int deck, int interval);
engine.scratchDisable(int deck, bool ramp);
bool engine.isScratching(int deck);
```

Here is how to use them:

**When you want to start scratching** (such as when the wheel is touched,) call `engine.scratchEnable()` with:

- the virtual deck number you want to scratch
- the resolution of the MIDI control (in intervals per revolution, typically 128.)
- the speed of the imaginary record at 0% pitch (in revolutions per minute (RPM) typically 33+1/3, adjust for comfort)
- the [alpha-beta filter](http://en.wikipedia.org/wiki/Alpha_beta_filter) coefficients (together these affect responsiveness and looseness of the imaginary slip mat):
  - the alpha value for the filter (start with 1/8 (0.125) and tune from there)
  - the beta value for the filter (start with alpha/32 and tune from there)
- whether you want Mixxx to ramp the deck speed down or to stop instantly. (TRUE for ramping, which is the default.)

**Each time the MIDI control is moved**, call `engine.scratchTick()` with:

- the virtual deck number this control is currently scratching
- the movement value (typically 1 for one "tick" forwards, -1 for one "tick" backwards)

**When you're done scratching** (like when the wheel is released,) just call `engine.scratchDisable()` with:

- the number of the virtual deck to stop scratching
- whether you want Mixxx to ramp up to the play speed or jump to it instantly. (Default is to ramp which also allows spin-backs with wheels.)

**Note:** You can use `script.deckFromGroup(group)` to get the virtual
deck number from the group string. See [Helper
functions](#Helper-functions) for more information.

Here is an example for the two most common types of wheels. Click the
tab labeled 'scratchingExample.js' below to open this example as a file
in your text editor.

``` javascript
// The button that enables/disables scratching
MyController.wheelTouch = function (channel, control, value, status, group) {
    var deckNumber = script.deckFromGroup(group);
    if ((status & 0xF0) === 0x90) {    // If button down
  //if (value === 0x7F) {  // Some wheels send 0x90 on press and release, so you need to check the value
        var alpha = 1.0/8;
        var beta = alpha/32;
        engine.scratchEnable(deckNumber, 128, 33+1/3, alpha, beta);
    } else {    // If button up
        engine.scratchDisable(deckNumber);
    }
}

// The wheel that actually controls the scratching
MyController.wheelTurn = function (channel, control, value, status, group) {
    // --- Choose only one of the following!
    
    // A: For a control that centers on 0:
    var newValue;
    if (value < 64) {
        newValue = value;
    } else {
        newValue = value - 128;
    }

    // B: For a control that centers on 0x40 (64):
    var newValue = value - 64;
    
    // --- End choice
    
    // In either case, register the movement
    var deckNumber = script.deckFromGroup(group);
    if (engine.isScratching(deckNumber)) {
        engine.scratchTick(deckNumber, newValue); // Scratch!
    } else {
        engine.setValue(group, 'jog', newValue); // Pitch bend
    }
}
```

And that's it\! Just make sure to map the button/touch sensor and wheel
to these script functions [as described
above](#Linking-MIDI-signals-to-JavaScript-functions) and you'll be
ready to tear up some tracks.

## Timed reactions

Sometimes you need to be able to do things at certain time intervals
regardless of whether the controller is manipulated or something changes
in Mixxx. Timed reactions let you do just that with 20ms resolution.
Here are the functions:

  - **engine.beginTimer**(*milliseconds*, *function*, *one-shot*) -
    Starts a timer that will call the specified script function
    repeatedly every time (if *one-shot* is false or not present) or
    just once (if *one-shot* is true) the given number of milliseconds
    (1/1000 second) pass. It returns an ID number for the timer (0 on
    failure) that you'll want to store in a variable so you can stop it
    later if it's a repeating timer. When the function is executed
    `this` is set to whatever `this` was where `engine.beginTimer` was
    called.
  - **engine.stopTimer**(*timer ID*) - Stops the specified timer.

If you need to pass arguments to a function used with
`engine.beginTimer`, wrap the function call in an anonymous function
expression, for example:

``` js
    engine.beginTimer(250, function() {
        someFunctionToExecute(parameter1, parameter2, parameter3);
    });
```

Note that within the function expression, you can access variables from
the surrounding scope because [JavaScript functions create
closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures).

You can create and stop timers as much as you like but be aware that the
operating system has limits on the number of timers it will allow, so
remember to stop them as soon as you're done with them. (Not to mention
that overall performance decreases as the number and/or frequency of
timers increase.)

**NEVER use busy-wait loops\!** (Loops that do nothing but delay. They
can cause Mixxx to stutter.) **Always use a timer instead\!**

See the [script timers](script%20timers) page for more details on best
practices for using timers.

Old controller scripts used strings that evaluate to functions instead
of actual functions as an argument to `engine.beginTimer`. This
functionality is kept for backwards compatibility, but it is deprecated
because it violates JavaScript convention. Passing a function as an
argument to `engine.beginTimer` is preferred for all new controller
scripts.

## Spinback, brake and soft start effect

A forwards or backwards brake effect can be enabled/disabled using
engine.brake() or engine.spinback(). engine.spinback() just calls
engine.brake() with default settings to make it behave like a spinback.

To achieve a forward acceleration effect from standstill to normal speed
use engine.softStart().

When disabled while active, all three functions would jump to normal
playback speed.

Both engine.softStart() and engine.brake()/engine.spinback() can
interrupt each other: slow down a track with engine.brake() and (even
before track has stopped) get it back to normal speed with
engine.softStart(). See last example how to map this to press/release of
just one button.

``` javascript
brake(int deck, bool activate, [float factor])
spinback(int deck, bool activate, [float factor], [float rate])
softStart(int deck, bool activate, [float factor])
```

  - **deck** - the deck number to use, e.g: 1
  - **activate** - true to activate or false to disable. 
  - **factor** (optional) - how quickly the deck should come to a stop,
    normal playback rate respectively. start with a value of 1 and
    increase to increase the acceleration/deceleration. Be aware that
    brake/spinback called with low factors (about 0.5 and lower) would
    keep the deck running altough the resulting very low sounds are not
    audible anymore. Accordingly, softStart with low factors would take
    a while until sound is audible.
  - **rate** (optional) - the initial speed of the deck when enabled.
    "-10" (default) means 10x speed in reverse. Positive values like
    "10" also work, thhough then it's spinning forward obviously.

Examples:

Activate brake on button press, jump to normal speed on button release

``` javascript
    MyControllerPrefix.brake_button = function(channel, control, value, status, group) {
        var deck = parseInt(group.substring(8,9)); // work out which deck we are using 
        var activate = value > 0;
        
        if (activate) {
            engine.brake(deck, true); // enable brake effect
        } else {
            engine.brake(deck, false); // disable brake effect
        }   
    }
```

Activate brake on button press, jump to normal speed on button release
(short version)

``` javascript
    MyControllerPrefix.brake_button = function(channel, control, value, status, group) {
        var deck = parseInt(group.substring(8,9)); // work out which deck we are using 
        engine.brake(deck, value > 0, 1.2, -10); // start at a rate of -10 and decrease at a factor of 1.2
    }
```

Activate spinback on button press, jump to normal speed on button
release

``` javascript
    MyControllerPrefix.spinback_button = function(channel, control, value, status, group) {
        var deck = parseInt(group.substring(8,9)); // work out which deck we are using
        engine.spinback(deck, value > 0, 2.5); // use default starting rate of -10 but decrease speed more quickly
    }
```

Activate softStart on button press, jump to normal speed on button
release

``` javascript
    MyControllerPrefix.softStart_button = function(channel, control, value, status, group) {
        var deck = parseInt(group.substring(8,9)); // work out which deck we are using
        engine.softStart(deck, value > 0, 2.0); // double the default acceleration
    }
```

Brake on button press, softStart on button release

``` javascript
    MyControllerPrefix.brake_SoftStart_button = function(channel, control, value, status, group) {
        var deck = parseInt(group.substring(8,9)); // work out which deck we are using
        var activate = value > 0;
        if (activate) { // act on button press
            engine.brake(deck, true); // slow down the track
        } else { // act on button release
            engine.softStart(deck, true);
        }
    }
```

The effects can also be mapped directly via XML using either
**script.spinback**, **script.brake** or **script.softStart**:

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

## Color API

The color of hotcues is accessible with `engine.getValue('[ChannelN]',
'hotcue_X_color')` (where N and X are the respective Deck and hotcue
whose information is being accessed) as an RGB color code. The scripting
environment provides some functions to make it easier to work with these
RGB color codes:

  - **colorCodeToObject**(*RGB color code*): Converts an RGB color code
    from `[ChannelN]`, `hotcue_X_color` (for example `0xFF0000`) into an
    object with `red`, `green` and `blue` properties with a value range
    of 0-255
  - **colorCodeFromObject**(*RGB object*): Converts an object with
    `red`, `green`, and `blue` properties (value range 0-255) into an
    RGB color code that can be used to set a value for `[ChannelN]`,
    `hotcue_X_color`

Additionally, there is a ColorMapper class to map the MIDI values for
colors supported by the controller to RGB color codes. Mixxx supports
setting hotcues to any arbitrary color which may not exactly match what
the controller hardware supports, so use ColorMapper to match colors to
the nearest color supported by the controller. Create a ColorMapper by
passing an object with RGB codes as the keys and the corresponding MIDI
codes as values:

``` js
    var myControllerColorMapper = new ColorMapper({
        0xFF0000: 1, // red
        0x00FF00: 2, // green
        0x0000FF: 3, // blue
    });
```

In this example, the controller's buttons would be lit red by sending
MIDI code 1, green with MIDI code 2, and blue with MIDI code 3.
ColorMapper has two methods:

  - **getValueForNearestColor**(*RGB color code*): returns the mapped
    value matching the nearest color in the map. For example, if
    `0xFF0000` was passed in the above example, this method would return
    `1`. If `0xFF0001` was passed, it would also return `1`.
  - **getNearestColor**(*RGB color code*): returns an RGB object with
    `red`, `green`, and `blue` properties on a 0-255 scale like
    `colorCodeToObject` for the nearest color in the map

Connect a callback to `[ChannelN]`, `hotcue_X_color` to set LEDs to
match the hotcue color, for example:

``` js
    var hotcueLEDcallback = engine.makeConnection('[Channel1]', 'hotcue_2_color', function (value, group, control) {
      if (value !== -1) { // hotcue is set
        midi.sendShortMsg(0x90, 0x60, myControllerColorMapper.getNearestColor(value));
      } else { // hotcue is unset, turn off LED
        midi.sendShortMsg(0x90, 0x60, 0);
      }
    });
```

The Components library supports passing a ColorMapper object to the
[HotcueButton class](components_js#hotcuebutton) so all the logic for
matching nearest colors to MIDI codes when a hotcue is created or
deleted are taken care of for you.

## Helper functions

Here is a list of functions available to you from the always-loaded
`common-controller-scripts.js` file:

  - **nop**() - Does nothing (No OPeration.) Empty function you can use
    as a place-holder while developing to avoid errors.
  - **print**(*string*) - Prints the passed in string to the console.
  - **secondstominutes**(*seconds*) - Returns the given quantity of
    seconds in `MM:SS` format.
  - **msecondstominutes**(*milliseconds*) - Returns the given quantity
    of milliseconds in `MM:SS.ss` format.
  - **script.toggleControl**(group, [control](mixxxcontrols)) - toggles
    the state of a binary control
  - **script.midiDebug**(channel, control, value, status,
    group)<sup>2</sup> - Prints the values as passed to it. Call this
    from anywhere in your function to see what the current values of
    these variables are. You can also of course put it in the \<key/\>
    tag of your XML to make sure the values being passed to the script
    are what you expect.
  - **script.midiPitch**(LSB, MSB, status) - Intended to be called from
    another script function, pass this the values from a MIDI Pitch
    control and it will return a corresponding value suitable for
    Mixxx's pitch sliders ("rate" controls.) So if you just want to set
    those controls, the calling function need only have the single line:
    `engine.setValue("[Channel"+deck+"]","rate",script.midiPitch(control,
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
  - **script.absoluteLinInverse**(value, low, high, min, max) - The
    inverse of the above function. This is useful for sending MIDI
    values back to controllers.
  - **script.absoluteNonLin**(value, low, mid, high, min, max) - Takes a
    value from an absolute control (0..127 by default, customize with
    min and max) and returns the proportionate value between *low*,
    *mid* and *high* for a non-linear Mixxx control such as EQ or master
    volume. You can then use this returned value to set the desired
    Mixxx control.
  - **script.absoluteNonLinInverse**(value, low, mid, high, min, max) -
    The inverse of the above function. This is useful for sending MIDI
    values back to controllers. *New in 1.12*
  - **script.deckFromGroup**(group) - Takes a group string for a deck
    such as "\[Channel1\]" and returns the deck number (in this case, 1)
    
  - **bpm.tapButton**(deck) - Call this every time the desired tap
    button is pressed. It takes the progressive average of the last 8
    taps and sets the bpm of the specified deck to that value, assuming
    the pitch range is large enough to reach it. (This depends on the
    track having the correct original BPM value.) If more than two
    seconds pass between taps, the history is erased.
  - **String**.prototype**.toInt** - returns an ASCII byte array for all
    the characters in any string. Use like so: `"Test string".toInt()`

<sup>1</sup> Introduced in 1.11.0 <sup>2</sup> Renamed in 1.11.

## Additional examples

Here are some examples to get you started. These examples start simple
and get progressively more complex.

### Button presses

MIDI buttons usually send a signal with a value of 0x7f (127) when the
button is pressed and 0x00 (0) when the button is released. Thus,
JavaScript functions mapped to button presses will be called both when
the button is pressed and released. To make the function only do
something when the button is pressed, wrap the function in an if
statement checking the value parameter:

``` javascript
MyController.someButton = function (channel, control, value, status, group) {
    if (value === 127) {
        // do something when this button is pressed
    }
}
```

### Rescale incoming values

To reduce the sensitivity of a relative-mode (touch strip) pitch slider:
(assuming \<group\> is specified appropriately in the XML file)

``` javascript
MyController.pitchSlider = function (channel, control, value, status, group) {   // Lower the sensitivity of the pitch slider
    var currentValue = engine.getValue(group,"rate");
    engine.setValue(group,"rate",currentValue+(value-64)/128);
}
```

**IMPORTANT NOTE:** You must always declare variables with "var" when
you first use them inside a function since it establishes scope. If you
omit this, the variable becomes global and will clobber anything else
with the same name even if it's in another script file.

### Storing commonly used MIDI codes in JS objects

Putting codes you need to reference many times throughout your script
into a [JavaScript
object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
makes your code more organized, readable, and easier to modify later. A
JavaScript object is a container for variables of any other type
(including functions and other objects), referred to as the object's
attributes. In this case, they are used similar to hash tables in other
programming languages. For example, you could store the MIDI notes for
buttons and the MIDI values for LED colors:

``` javascript
MyController.buttons = {
    '[Channel1]': { // an object within another object
        'play': 0x01,
        'cue': 0x02,
        'sync': 0x03
    },
    '[Channel2]': {
        'play': 0x04,
        'cue': 0x05,
        'sync': 0x06
    }
}

MyController.colorCodes = {
    'off': 0x00,
    'red': 0x01,
    'green': 0x02,
    'blue': 0x03
}
```

Now, when writing code to change an LED to green, instead of typing the
note number for the LED and the value for green directly, you can
reference the object's properties through your code. In addition to
being easier to write, this makes your code easier to read. Easier to
read code helps you remember what it does when you look at it again
later. It also helps other people who may modify the code later. For
example, for a function that [automatically reacts to
changes](#automatic-reactions-to-changes-in-Mixxx) of the play state of
a track (through the play\_indicator [Mixxx Control](MixxxControls)),
you can write:

``` javascript
MyController.playButtonLED = function (value, group, control) {
    midi.sendShortMsg(
                      0x90,
                      MyController.buttons[group].play, // an object's properties can be referenced through either SomeObject.property or SomeObject[property]
                                                        // but with the [] brackets, property can be a variable or other code
                      (value === 1) ? MyController.colorCodes.green : MyController.colorCodes.off
                      // The above line is a shortcut that means: "If value is 1, then send MyController.colorCodes.green; otherwise, send MyController.colorCodes.off"
                      // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
                     )
}
```

rather than:

``` javascript
MyController.playButtonLED = function (value, group, control) {
    if (group === '[Channel1]') {
        if (value === 0x7F) {
            midi.sendShortMsg(0x90, 0x01, 0x02)
        } else {
            midi.sendShortMsg(0x90, 0x01, 0x00)
        }
    } else if (group === '[Channel2]') {
        if (value === 0x7F) {
            midi.sendShortMsg(0x90, 0x04, 0x02)
        } else {
            midi.sendShortMsg(0x90, 0x04, 0x00)
        }
    }
}
```

The two examples above have the same effects, but the first one is more
intuitive because the code more clearly and concisely represents what it
does. The MyController.buttons and MyController.colorCodes objects can
help you refer to numbers by what they do rather than having a bunch of
numbers throughout your code. If you decide to change which MIDI
controls do what later, it will be easier to edit the one line in the
object declaration than go through and find each MIDI code you need to
change.

**Tip:** An explanation of the MIDI signals that your controller sends
to computers and how it reacts to MIDI signals that computers send to it
should be available from the controller manufacturer. This is likely in
a document on the product page for your controller on the manufacturer's
website. If it is not in a separate document, it is likely at the end of
the manual.

### Modifier (shift) buttons and layered mappings

Many controllers send different MIDI signals while a shift button is
held down. In that case, JavaScript may not be needed and using XML may
be sufficient. However, if this is not the case, to have controls do
something different depending on whether a shift button or layer
switching button is active, you need to use JavaScript. There are
multiple ways this can be accomplished.

#### Tracking the state of the modifier in a variable

One approach is to declare a boolean (true/false) variable to keep track
of whether the modifier button is currently pressed. In the XML file,
map the modifier button to a function that toggles the state of this
variable and map other controls to functions that check the state of the
variable. For example:

``` javascript
MyController.shift = false;

MyController.shiftButton = function (channel, control, value, status, group) {
    // Note that there is no 'if (value === 127)' here so this executes both when the shift button is pressed and when it is released.
    // Therefore, MyController.shift will only be true while the shift button is held down
    MyController.shift = ! MyController.shift; // '!' inverts a boolean (true/false) value 
}

MyController.someButton = function (channel, control, value, status, group) {
    if (value === 127) { // only do stuff when the button is pressed, not when it is released
        if (MyController.shift) {
            // do something when this button and the shift button are both pressed
        } else {
            // do something else when this button is pressed but the shift button is not pressed
        }
    }
}
```

While this approach can work well for simple cases, if you are checking
the value of MyController.shift in many functions, it can get
cumbersome. Also, it can get difficult to keep track of everything that
happens in each mode, especially if you have more than two modes for a
control.

#### Reassigning MIDI input functions

An alternative approach is to define different functions for each layer.
Because [\#MIDI input handling
functions](#MIDI%20input%20handling%20functions) are variables that can
be reassigned, the function executed when a shift button or modifier is
activated can reassign the variables to different values. If you have
multiple controls you want to change the behavior of in different
conditions, it helps to group the MIDI input handling functions for each
layer within an object.

``` javascript
// A container for the functions of the active layer.
// In the XML file, map the MIDI input handling functions to
// properties of this object, for example, MyController.activeButtons.buttonA
MyController.activeButtons = {};

MyController.unshiftedButtons = {
    buttonA = function (channel, control, value, status, group) {
        //code to be executed when buttonA is pressed without shift
    },
    buttonB = function (channel, control, value, status, group) {
        //code to be executed when buttonB is pressed without shift
    }
};

MyController.shiftedButtons = {
    buttonA = function (channel, control, value, status, group) {
        //code to be executed when buttonA is pressed with shift
    },
    buttonB = function (channel, control, value, status, group) {
        //code to be executed when buttonB is pressed with shift
    }
};

MyController.init = function(id, debugging) {
    MyController.activeButtons = MyController.unshiftedButtons;
}

MyController.shiftButton = function (channel, control, value, status, group) {
    // This function is mapped to the incoming MIDI signals for the shift button in the XML file
    if (value === 127) { // shift button pressed
        engine.connectControl(group, key, true); // disconnect callbacks for unshifted layer
        // see "Automatic reactions to changes in Mixxx" section above
        MyController.activeButtons = MyController.shiftedButtons;
        engine.connectControl(group, key); // connect callbacks for shifted layer
    } else { // shift button released
        engine.connectControl(group, key, true); // disconnect callbacks for shifted layer
        MyController.activeButtons = MyController.unshiftedButtons;
        engine.connectControl(group, key); // connect callbacks for unshifted layer
    }
}
```

### Turning a 2 deck controller into a 4 deck controller

With the magic of MIDI scripting, you can turn a 2 deck controller into
a 4 deck controller by setting up your script following the example
below. This example is complex, so if you are new to programming, it is
recommended that you read the examples above before trying to understand
this one. If you have trouble understanding this code, please ask for
help [on the forum](http://mixxx.org/forums/viewforum.php?f=3). There
are many different ways to organize the code and this is just one
example.

For every MIDI control that you want to map to a value that changes
something about a specific deck, in the XML mapping file, map it to a
function like the playButton function in the script below that starts
with 'group = MyController.deck\[group\]'. Use \[Channel1\] as the value
for the \<group\> element in the XML file for controls that manipulate
decks 1/3 and \[Channel2\] for decks 2/4. Map the buttons you want to
change between decks 1/3 and decks 2/4 to the deckToggleButton function.

Click the tab below labeled 'deckToggleExample.js' to download this
example as a file to open in your text editor.

``` javascript
function MyController() {}
MyController.init = function () {
    // Set up the controller to manipulate decks 1 & 2 when this script is loaded (when Mixxx starts or you save an edited script file)
    // The MyController.initDeck function is defined below.
    MyController.initDeck('[Channel1]')
    MyController.initDeck('[Channel2]')
}
MyController.shutdown = function() {}

MyController.deck = {
    // a hash table (technically an object) to store which deck each side of the controller is manipulating
    // The keys (object properties) on the left represent the <group> elements in the XML mapping file.
    // The values on the right represent which deck that set of mappings in the XML file is currently controlling.
    // These values are toggled between [Channel1]/[Channel3] and [Channel2]/[Channel4] by the deckToggleButton function below.
    // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer
    '[Channel1]': '[Channel1]',
    '[Channel2]': '[Channel2]'
}
MyController.buttons = { // a hash table that stores the MIDI notes that correspond to LED backlit buttons
    '[Channel1]': {
        'deckToggle': 0x01
        // Add any other LEDs for decks 1/3 here
     },
     '[Channel2]': {
        'deckToggle': 0x02
        // Add any other LEDs for decks 2/4 here
     }
}
MyController.buttons['[Channel3]'] = MyController.buttons['[Channel1]'] // Copy [Channel1] to [Channel3]
MyController.buttons['[Channel4]'] = MyController.buttons['[Channel2]'] // Copy [Channel2] to [Channel4]

MyController.channelRegEx = /\[Channel(\d+)\]/ // a regular expression used in the deckToggleButton function below
// This extracts the number from the strings '[Channel1]' ... '[Channel4]' so we can do math with that number
// see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp
MyController.deckToggleButton = function (channel, control, value, status, group) {
    if (value) { // only execute the below code when the button is pressed but not when it is released
        // First, get the number out of the string '[Channel1]' ... '[Channel4]'
        var deckNumber = parseInt( // convert string to an integer number variable
                             MyController.channelRegEx.exec( // execute the regular expression
                                 MyController.deck[group] // on this string
                             )[1] // Get the string that matches the part of the regular expression inside the first group of parentheses in the regular expression
                                  // which is (\d+)
                                  // this matches any number of digits
                          )
        if (deckNumber <= 2) {
            deckNumber += 2 // This is a shortcut for 'deckNumber = decknumber + 2'
        } else {
            deckNumber -= 2 // This is a shortcut for 'deckNumber = decknumber - 2'
        }
        MyController.deck[group] = '[Channel' + deckNumber + ']'
        MyController.initDeck(MyController.deck[group]) // Initialize the new deck. This function is defined below.
    }
}

MyController.initDeck = function (group) { // This function is not mapped to a MIDI signal; it is only called by this script in the init and deckToggleButton functions
    // Execute code to set up the controller for manipulating a deck
    // Putting this code in a function allows you to call the same code from the script's init function and the deckToggleButton function without having to copy and paste code

    // Figure out which deck was being controlled before so automatic reactions to changes in Mixxx (see above) can be disabled for that deck
    var disconnectDeck = parseInt(MyController.channelRegEx.exec(group)[1])
    if (disconnectDeck <= 2) {
        disconnectDeck += 2
    } else {
        disconnectDeck -= 2
    }
    MyController.connectDeckControls('[Channel'+disconnectDeck+']', true) // disconnect old deck's Mixxx controls from LEDs. This function is defined below.
    MyController.connectDeckControls(group) // connect new deck's Mixxx controls to LEDs

    // Toggle LED that indicates which deck is being controlled
    midi.sendShortMsg(
        0x90,
        MyController.buttons[group]['deckToggle'],
        (disconnectDeck > 2) ? 0x7f : 0x00 // If the condition in parentheses is true, send 0x7f; otherwise, send 0x00
                                           // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
    )
}

MyController.connectDeckControls = function (group, remove) { // This function is not mapped to a MIDI signal; it is only called by this script in the initDeck function below
    // This function either connects or disconnects automatic reactions to changes in Mixxx (see wiki section above), depending on the value of the 'remove' parameter
    // Putting this in its own function allows the same code to be reused for both connecting and disconnecting
    // This is particularly helpful when the list of Mixxx controls connected to LEDs is long
    
    remove = (typeof remove !== 'undefined') ? remove : false // If the 'remove' parameter is not passed to this function, set remove = false
    var controlsToFunctions = { // This hash table maps Mixxx controls to the script functions (not shown in this example) that control LEDs that react to changes in those controls
        'play': 'MyController.playButtonLED',
        'sync_enabled': 'MyController.syncLED',
        'pfl': 'MyController.headphoneLED'
        // ... and any other functions that react to changes in Mixxx controls for a deck
    }
    
    for (var control in controlsToFunctions) { // For each property (key: value pair) in controlsToFunctions, control = that property of controlsToFunctions
                                               // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in
        engine.connectControl(group, control, controlsToFunctions[control], remove)
        if (! remove) { // '!' means "not"; it inverts the value of a boolean (true/false)
            engine.trigger(group, control)
        }
    }
}

MyController.playButton = function (channel, control, value, status, group) {
    group = MyController.deck[group] // Change the value of the group variable to the deck we actually want to manipulate based on the state of the deck toggle button
    if (value) {
        // toggle whether the deck is playing
        engine.setValue(group, 'play', ! (engine.getValue(group, 'play')))
    }
}
```
