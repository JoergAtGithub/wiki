# MIDI Scripting

In order to support the advanced features of many MIDI controllers,
Mixxx offers what we call MIDI Scripting (introduced in Mixxx v1.7.0).
It enables MIDI controls to be mapped to
[QtScript](http://doc.trolltech.com/4.5/qtscript.html) (also known as
[Javascript](http://en.wikipedia.org/wiki/JavaScript_syntax)/[EMCAScript](http://www.ecma-international.org/publications/standards/Ecma-262.htm))
functions stored in function library files, freeing Mixxx from a
one-to-one MIDI mapping ideology. These user-created functions can then
do anything desired with the MIDI event info such as have a single
controller button simultaneously affect two or more [Mixxx properties
("controls")](mixxxcontrols), adjust incoming control values to work
better with Mixxx (i.e. for
[\#scratching](#scratching)),-display-a-complex-LED-sequence,-send-messages-to-text-displays-on-the-controller,-or-even-[turn
a 2 deck controller into a 4 deck
controller](#turning-a-2-deck-controller-into-a-4-deck-controller).

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
  - [JavaScript
    Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)

The [last
example](#turning-a-2-deck-controller-into-a-4-deck-controller) at the
bottom of this page utilizes a lot of features of JavaScript. It has
lots of comments with links to the MDN JavaScript Reference. It may be
helpful as a quick introduction to the language for experienced
programmers.

**Tip:** If there is already a Mixxx mapping for a controller made by
the same manufacturer as your controller, you may want to look at that
mapping for examples. The controllers likely send similar types of
signals (although they could be very different).

**Tip:** When you're testing your scripts, you don't have to restart
Mixxx. Every time you save your file, Mixxx will reload it immediately.
This can make testing changes very fast.

## Setting up a JavaScript mapping file

### File locations

Script files use the naming convention
`<manufacturer>-<device>-scripts.js` (e.g. `Stanton-SCS3d-scripts.js`).
Put your custom JS & XML file in this directory:

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

The default mapping files, which you can look at as examples or a
starting point for your custom mapping, are located in the following
directory:

  - GNU/Linux: `/usr/share/mixxx/controllers` or
    `/usr/local/share/mixxx/controllers`
  - OS X: `/Applications/Mixxx.app/Contents/Resources/controllers/`
  - Windows: `C:\Program Files\Mixxx\controllers`

For Mixxx 1.10 and earlier, replace 'controllers' with 'midi' in the
above paths.

### Setting up git and getting your mapping included in Mixxx

Git is software that allows you to keep track of what you have changed
in files. We use it for coordinating Mixxx development. If you want to
have your mapping included in Mixxx, start by creating a
[GitHub](http://github.com/) account and [forking
Mixxx](https://github.com/mixxxdj/mixxx). On GNU/Linux and Mac OS X, you
can directly work on your mapping in your git repository while running
Mixxx to test your changes. To do this, delete the "controllers"
directory in your user preferences folder (backup any work in progress
that you do not want to lose first\!) and make a symbolic link to the
"res/controllers" directory in your git repository. For example, if your
git repository is under the "software" directory in your home directory
on GNU/Linux, run:

`ln -s ~/software/mixxx/res/controllers ~/.mixxx/controllers`

Make a new git branch (run `git checkout -b new_branch_name` from within
your git repository). Make changes to your mapping and commit them when
your changes work. Please prefix your git commit messages with the name
of your controller so others can easily tell what the commits are for
after your changes are merged. Post [on the
forum](http://mixxx.org/forums/viewforum.php?f=7) early so users can
find your mapping and give feedback as you develop it. When you are
ready to submit your mapping for inclusion in Mixxx, make a pull request
on GitHub. See the [Using Git](Using%20Git) wiki page for more
information. If you write functions for your script that you think may
be helpful for mapping other controllers, add them to
common-control-scripts.js under the "script" namespace.

Once your mapping has been accepted, please update the relevant tables
in the [DJ Hardware Guide](hardware%20compatibility) and make a wiki
page for your mapping. To make a wiki page, list your controller on the
Hardware Guide with the name surrounded by double brackets, for example
\[\[My Controller\]\]. Save the wiki page, then click on the red link to
create the new page. On that new wiki page, put a picture of the
controller at the top with a brief description, a link to the
manufacturer's website, and compatibility information for GNU/Linux, Mac
OS X, and Windows. Please link to some reviews of the device too. Then,
describe the mapping with labeled diagrams. If there is no diagram
readily available, ask the manufacturer for one. If they do not provide
one, take pictures of your device and label them. Upload diagrams and/or
pictures by going to the [Media Manager](?do=media) at the top right of
any wiki page and upload your file(s) to the "hardware" namespace.

### Function & variable naming conventions

Functions use the naming convention `<manufacturer><device>.<function
name>` (e.g. `StantonSCS3d.pitchSlider`). Global variables use
`<manufacturer><device>.<variable name>` (e.g. `StantonSCS3d.deck`).
These are very important to avoid name collisions with other scripts
that may be loaded.

### Script file header

At the top of your script file, you need to have a declaration of the
controller name. It looks like this:

    function StantonSCS3d() {}

...and you would replace the name with whatever you entered for
'functionprefix' in the XML file above.

### init and shutdown functions

**All device script files are expected to contain initialization and
shutdown functions** called `<manufacturer><device>.init(ID,debugging)`
and `<manufacturer><device>.shutdown()` which will be called when Mixxx
opens and closes the device, respectively. They can be empty, but are
useful for putting controllers into known states and/or lighting certain
LEDs before operation begins or the program exits. The ID parameter is
the `controller id` attribute from the XML file. This can be used to
identify the particular controller instance in print statements. The
`debugging` parameter is set to 'true' if the user specified the
--mididebug parameter on the command line (v1.11 and higher).

For example, if there are 40 LEDs on your controller that respond to
MIDI note numbers 1 through 40 that turn on when sent value 0x7f and
turn on when sent value 0x00, your init and shutdown functions could be:

    MyController.init = function () {
        for (i = 1; i <= 40; i++) { // Repeat the following code for the numbers 1 through 40
                                    // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for
            midi.sendShortMsg(0x90, i, 0x7f)
        }
    }
    
    MyController.shutdown = function() {
       for (i = 1; i <= 40; i++) {
            midi.sendShortMsg(0x90, i, 0x00)
        }
    }

### Linking a JavaScript mapping file to an XML mapping file

There is a default script function file called
`midi-mappings-scripts.js` which contains functions common to all
controllers and is always loaded. See [\#available common
functions](#available%20common%20functions) below for information on
these functions.

To specify additional script files to load, add the following section to
the device's [XML MIDI mapping
file](MIDI%20controller%20mapping%20file%20format) right underneath the
\<controller\> tag:

``` XML
        <scriptfiles>
            <file filename="Stanton-SCS3d-scripts.js" functionprefix="StantonSCS3d"/>
        </scriptfiles>
```

You can add as many \<file\> tags as you like, but be sure to specify
the appropriate function prefix in every one. These will all be loaded
when the controller is activated.

**Tip:** An explanation of the MIDI signals that your controller sends
to computers and how it reacts to MIDI signals that computers send to it
should be available from the controller manufacturer. This is likely in
a document on the product page for your controller on the manufacturer's
website. If it is not in a separate document, it is likely at the end of
the manual.

### Linking MIDI signals to JavaScript functions

MIDI controller XML mapping files are described on the [MIDI controller
mapping file format](MIDI%20controller%20mapping%20file%20format) page.
This XML file defines how MIDI controls are mapped to MIDI commands.

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
useful for multi-deck controllers because you only need one function
that checks the \<group\> and reacts appropriately.) No tags or options
are considered other than those shown above, so you can leave them out.

When this device control is operated, the named script function is
called. That function then determines what action is taken based on the
MIDI signal, such as changing a Mixxx control, sending a MIDI signal
back to the controller to change an LED, and/or printing a debug
message.

## Programming Mixxx mappings with JavaScript

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
which can be found [here](mixxxcontrols). So for example:

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

### Sending messages to the controller to change LEDs or other controller properties

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

**Tip:** If you send MIDI signals to the controller in functions that
automatically react to changes in Mixxx (see below) rather than
functions that handle incoming MIDI signals, the LEDs and other
properties of your controllers will always be in sync with what Mixxx is
actually doing, even if you manipulate Mixxx with the keyboard, mouse,
or another controller.

**Tip:** An explanation of the MIDI signals that your controller sends
to computers and how it reacts to MIDI signals that computers send to it
should be available from the controller manufacturer. This is likely in
a document on the product page for your controller on the manufacturer's
website. If it is not in a separate document, it is likely at the end of
the manual.

**Tip:** [Store commonly used MIDI values in global hash
tables](#storing-commonly-used-MIDI-codes-in-global-hash-tables)

### Automatic reactions to changes in Mixxx

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
    successful. Note that the script function name must be in quotes.
  - **engine.trigger**(*control group*, *control name*) - An easy way to
    cause the specified Mixxx control signal to fire so the connected
    script function is called with the updated value even if it hasn't
    changed, such as when forcing LEDs to update on a mode change.

Connected functions are passed three parameters: the new value of the
MixxxControl, the group, and the Mixxx control name. So, your connected
function can look like this:

``` javascript
MyController.volumeLEDs = function (value, group, control) {
    //...what to do with the value, group and control arguments goes here...
}
```

Or like this:

``` javascript
MyController.volumeLEDs = function (value) {
    //...what to do with the value goes here...
}
```

If the provided three parameters do not fit your needs, then you can use
the following trick to provide your own parameters to be passed.

``` javascript
// Pass one parameter '1000' to my callback 
engine.connectControl("[Master]", "volume", function(value) { MyController.volumeLEDs(1000); });
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

### Soft-takeover

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

Note that this only works for controls manipulated through
engine.setValue() in a script. It does not work for controls mapped in
an XML file.

### Scratching

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
  - the [alpha-beta
    filter](http://en.wikipedia.org/wiki/Alpha_beta_filter) coefficients
    (together these affect responsiveness and looseness of the imaginary
    slip mat)

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

Here is an example for the two most common types of wheels. Click the
tab labeled 'scratchingExample.js' below to open this example as a file
in your text editor.

``` javascript
// The button that enables/disables scratching
MyController.wheelTouch = function (channel, control, value, status) {
    if ((status & 0xF0) == 0x90) {    // If button down
  //if (value == 0x7F) {  // Some wheels send 0x90 on press and release, so you need to check the value
        var alpha = 1.0/8;
        var beta = alpha/32;
        engine.scratchEnable(MyController.currentDeck, 128, 33+1/3, alpha, beta);
    } else {    // If button up
        engine.scratchDisable(MyController.currentDeck);
    }
}

// The wheel that actually controls the scratching
MyController.wheelTurn = function (channel, control, value, status) {
    // See if we're scratching. If not, skip this.
    if (!engine.isScratching(MyController.currentDeck)) return;
    
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
above](#Linking-MIDI-signals-to-JavaScript-functions) and you'll be
ready to tear up some tracks.

### Timed reactions

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
    midi.sendShortMsg(0x90, led, MyController.colorCodes[color]);
}
```

### Spinback and brake effect

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
        var activate = value > 0;
        
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
  - **script.absoluteNonLinInverse**(value, low, mid, high, min, max) -
    The inverse of the above function. This is useful for sending MIDI
    values back to controllers. *New in 1.12*
  - **bpm.tapButton**(deck) - Call this every time the desired tap
    button is pressed. It takes the progressive average of the last 8
    taps and sets the bpm of the specified deck to that value, assuming
    the pitch range is large enough to reach it. (This depends on the
    track having the correct original BPM value.) If more than two
    seconds pass between taps, the history is erased.

<sup>1</sup> Introduced in 1.11.0 <sup>2</sup> Renamed in 1.11.

### System-exclusive (sysex) message handing functions

Data passed from SysEx messages to functions are, in order:

1.  an array of raw data bytes
2.  the length of that array

Therefore, function definitions should look like:

``` javascript
ControllerName.inboundSysex = function (data, length) {
    ...
}
```

To invoke the above function, add the following mapping to the
`<controls>` section of your XML preset file:

    <control>
        <status>0xf0</status>
        <group>[Master]</group>
        <key>ControllerName.inboundSysex</key>
        <options>
            <Script-Binding/>
        </options>
    </control>

The bytes received are completely up to the controller so consult the
user manual or the manufacturer for details. If the controller can send
different SysEx messages, your single function is responsible for
deciding which has been received then taking the appropriate action.

*Note that some controllers may send bytes that violate MIDI standards,
e.g. setting the high bit in a data byte or using undefined status bytes
(like `0xF9`.) On Linux, recent versions of ALSA (from November 2012
onward) automatically standardize these by breaking the bytes into two
nybbles and sending two bytes for every one received from the
controller. For example `0xF0 0x97 0x30 0xF7` would become
`0xF0 0x09 0x07 0x03 0x00 0xF7.` Consult the ALSA documentation for full
details.*

## Additional examples

Here are some examples to get you started. These examples start simple
and get progressively more complex.

### Button presses

MIDI buttons usually send a signal with a value of 0x7f when the button
is pressed and 0x00 when the button is released. Thus, JavaScript
functions mapped to button presses will be called both when the button
is pressed and released. To make the function only do something when the
button is pressed, wrap the function in an if statement checking the
value parameter:

``` javascript
MyController.someButton = function (channel, control, value, status, group) {
    if (value) { // the number 0 is the same as false; positive numbers are the same as true
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

### Modifier (shift) buttons

To map MIDI signals to different actions depending on whether a modifier
button is pressed, declare a global boolean (true/false) variable at the
top of your JavaScript file to keep track of whether the modifier button
is currently pressed. In the XML file, map the modifier button to a
function that toggles the state of this global variable and map other
controls to functions that check the state of this global variable. For
example:

``` javascript
MyController.shift = false

MyController.shiftButton = function (channel, control, value, status, group) {
    // Note that there is no 'if (value)' here so this executes both when the shift button is pressed and when it is released.
    // Therefore, MyController.shift will only be true while the shift button is held down
    MyController.shift = ! MyController.shift // '!' inverts the value of a boolean (true/false) variable 
}

MyController.someButton = function (channel, control, value, status, group) {
    if (value) { // only do stuff when the button is pressed, not when it is released
        if (MyController.shift) {
            // do something when this button and the shift button are both pressed
        } else {
            // do something else when this button is pressed but the shift button is not pressed
        }
    }
}
```

### Storing commonly used MIDI codes in global hash tables

Putting codes you need to reference many times throughout your script
into a global hash table (technically an
[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
in JavaScript) makes your code more organized, readable, and easier to
modify later. A hash table is simply a list of keys (names) and the
values of those keys (technically in JavaScript, each key is an object
property). Hash tables are like a convenient container for a list of
multiple variables. For example, you could store the MIDI notes for
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

These variables should be declared at the top of your script file,
outside of any functions, to make them global variables that can be used
within any function. Now, when writing code to change an LED to green,
instead of typing the note number for the LED and the value for green
directly, you can reference the hash tables through your code. In
addition to being easier to write, this makes your code easier to read.
Easier to read code helps you remember what it does when you look at it
again later. It also helps other people who may modify the code later.
For example, for a function that [automatically reacts to
changes](#automatic-reactions-to-changes-in-Mixxx) of the play state of
a track, you can write:

``` javascript
MyController.playButtonLED = function (value, group, control) {
    midi.sendShortMsg(
                      0x90,
                      MyController.buttons[group]['play'],
                      (value) ? MyController.colorCodes['green'] : MyController.colorCodes['off']
                      // The above line is a shortcut that means: "If value is greater than 0 (which is equivalent to true), then send MyController.colorCodes['green']; otherwise, send MyController.colorCodes['off']"
                      // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
                     )
}
```

rather than:

``` javascript
MyController.playButtonLED = function (value, group, control) {
    if (group == '[Channel1]') {
        if (value) {
            midi.sendShortMsg(0x90, 0x01, 0x02)
        } else {
            midi.sendShortMsg(0x90, 0x01, 0x00)
        }
    } else if (group == '[Channel2]') {
        if (value) {
            midi.sendShortMsg(0x90, 0x04, 0x02)
        } else {
            midi.sendShortMsg(0x90, 0x04, 0x00)
        }
    }
}
```

The two examples above have the same effects, but the first one is more
intuitive because the code more clearly and concisely represents what it
does. The hash tables can help you refer to numbers by what they do
rather than having a bunch of numbers throughout your code. If you
decide to change which MIDI controls do what later, it will be easier to
edit the one line in the hash table than go through and find each MIDI
code you need to change.

**Tip:** An explanation of the MIDI signals that your controller sends
to computers and how it reacts to MIDI signals that computers send to it
should be available from the controller manufacturer. This is likely in
a document on the product page for your controller on the manufacturer's
website. If it is not in a separate document, it is likely at the end of
the manual.

### Turning a 2 deck controller into a 4 deck controller

With the magic of MIDI scripting, you can turn a 2 deck controller into
a 4 deck controller by setting up your script following the example
below. This example is complex, so if you are new to programming, it is
recommended that you read the examples above before trying to understand
this one. If you have trouble understanding this code, please ask for
help [on the forum](http://mixxx.org/forums/viewforum.php?f=3).

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
        engine.setValue(group, 'play', ! (engine.getValue(group, 'play')
    }
}
```
