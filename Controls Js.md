# Controls JS Library

Controls JS is a JavaScript library that makes it easier to code
controller mappings for Mixxx. It lets you focus more on your mapping
and less on the details of how Mixxx works. It is centered around
JavaScript objects called Controls that represent a physical component
on a controller, such as a button, knob, encoder, or fader. Control
provides generic functions that can be made to work for most use cases
just by changing some attributes of the Control, without having to write
many or any custom functions. The library also provides more specialized
Controls for common use cases. Controls can be organized into
ControlContainer objects, making it easy to iterate over them and change
their behavior to switch between different modes.

To use the library, in the `<scriptfiles>` element at the top of your
mapping's [XML file](MIDI%20controller%20mapping%20file%20format), load
the Lodash library and the Controls library:

    <file functionprefix="" filename="lodash.mixxx.js"/>
    <file functionprefix="" filename="midi-controls-0.0.js"/>

Controls JS uses a few functions from [Lodash](http://lodash.com/),
which is why they both need to be loaded. Importing the
midi-controls-0.0.js file makes the library accessible by an object
called `control` (lower case).

This documentation is a work in progress. Not every capability of the
library is fully documented yet. Refer to the source code of the library
if in doubt.

## Control

A Control represents a physical component on a controller, such as a
button, knob, encoder, or fader. It encapsulates all the information
needed to receive MIDI input from that component and send MIDI signals
out to the controller to activate its LED(s).

Controls should generally be properties of a
[\#ControlContainer](#ControlContainer) object. Most Controls should be
properties of a custom [\#Deck](#Deck) object, which is a derivative of
ControlContainer.

### Setup

The input function of each Control needs to be mapped to the incoming
MIDI signals in the XML file. For example:

    <control>
        <group>[Channel1]</group>
        <!-- MyController.leftDeck would be an instance of a custom Deck. -->
        <key>MyController.leftDeck.quantizeButton.input</key>
        <status>0x90</status>
        <midino>0x01</midino>
        <options>
            <script-binding/>
        </options>
    </control>

In the future Mixxx will be able to register MIDI inputs from
JavaScript, so that will not be necessary. The output does not need to
be mapped in XML. It is handled by the library in JavaScript.

Create Controls by calling the constructor with JavaScript's "new"
keyword. The Control constructor takes a single argument. This is an
options object containing properties that get merged with the Control
when it is created, making it easy to customize the functionality of the
Control. Most Controls need at least these properties defined:

  - **midi** (array with 2 numbers): the first two MIDI bytes that the
    controller sends/receives when the physical component changes state
  - **group** (string): the group that both the inCo and outCo
    manipulate, for example `'[Channel1]`' for deck 1
  - **inCo** (string): the [Mixxx ControlObject](mixxxcontrols) that
    this JavaScript Control manipulates when it receives a MIDI input
    signal
  - **outCo** (string): when this [Mixxx ControlObject](mixxxcontrols)
    changes value, the `output` function will be called

For example:

    var quantizeButton = new controls.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]'
        inCo: 'quantize',
        outCo: 'quantize',
    });

### Methods

The following methods (in JavaScript, methods are just object properties
that happen to be functions) must be defined for every Control, but in
most cases the defaults will work so you do not need to define them
yourself:

  - **input**: the [function that receives MIDI
    input](MIDI%20scripting#MIDI%20input%20handling%20functions)
  - **output**: the [function that gets called when outCo changes
    value](midi%20scripting#Automatic%20reaction%20to%20changes%20in%20Mixxx).
    Typically this sends MIDI output to the controller to change the
    state of an LED, but it can do anything.
  - **connect**: register `output` as the callback function that gets
    executed when the value of `group`, `outCo` changes. Implement a
    custom function if you need to connect callbacks for multiple [Mixxx
    ControlObjects](mixxxcontrols) in one Control. Refer to the source
    code of [SamplerButton.prototype.connect](#SamplerButton) for an
    example.

The following methods are called by the default `input` and `output`
methods. If you do not need to implement complex custom behavior,
overwrite these instead of the default `input` and `output` methods:

  - **inValueScale**: takes the third byte of the incoming MIDI signal
    as its first argument and returns the value to set `group`, `inCo`
    to
  - **outValueScale**: takes the value of `group`, `outCo` as its first
    argument and returns the third byte of the outgoing MIDI signal

Each Control also has these methods that you probably should not
overwrite:

  - **disconnect**: disconnect the `output` function from being called
    when `group`, `outCo` changes
  - **trigger**: manually call `output` with the same arguments as if
    `group`, `outCo` had changed
  - **send**: send a 3 byte (short) MIDI message out to the controller.
    The first two bytes of the MIDI message are specified by the `midi`
    property. The third MIDI byte is provided as the first argument to
    the `send` function.
  - **inGetParameter**: returns the value of `group`, `inCo` normalized
    to a 0-1 scale
  - **inSetParameter**: sets the value of `group`, `inCo` to the
    function's first argument, normalized to a 0-1 scale
  - **inGetValue**: returns the value of `group`, `inCo`
  - **inSetValue**: sets the value of `group`, `inCo` to the function's
    first argument
  - **inToggle**: sets `group`, `inCo` to its inverse (0 if it is \>0; 1
    if it is 0)
  - **outGetParameter**: returns the value of `group`, `outCo`
    normalized to a 0-1 scale
  - **outSetParameter**: sets the value of `group`, `outCo` to the
    function's first argument, normalized to a 0-1 scale
  - **outGetValue**: returns the value of `group`, `outCo`
  - **outSetValue**: sets the value of `group`, `outCo` to the
    function's first argument
  - **outToggle**: sets `group`, `outCo` to its inverse (0 if it is \>0;
    1 if it is 0)

### Sending outgoing MIDI messages

The function assigned to the `output()` property of the Control is
responsible for [reacting to
changes](midi%20scripting#Automatic%20reaction%20to%20changes%20in%20Mixxx)
in the outCo [Mixxx ControlObject](mixxxcontrols). The output callback
is automatically connected and called by the constructor if the outCo,
group, and midi properties are specified to the constructor (unless the
outConnect property is set to false to intentionally avoid that). This
makes it easy to map the controller so its LEDs stay synchronized with
the status of Mixxx, whether the outCo changes because of the Control
receiving MIDI input or the user changing it with the keyboard, mouse,
or another controller.

The default Control.prototype.output function calls the Control's
`send()` function, which sends an outgoing MIDI message with the first
two bytes as those specified by the Control's midi property and the
third byte as the new value of outCo. If you want to send a different
third byte, implement an `outValueScale()` function that takes the new
value as its first argument and returns the number to send as the third
MIDI byte. If you implement custom `input()` or `output()` functions,
you can call `this.send(valueToSend)` to send an outgoing MIDI message.

The output callback can be easily connected and disconnected by calling
the Control's `connect()` and `disconnect()` functions. The output
callback can also be manually run with the appropriate arguments simply
by calling the Control's `trigger()` function. This is done by the
constructor if the outCo, group, and midi properties are specified
(unless the outTrigger property is set to false to intentionally avoid
that). The `connect()`, `disconnect()`, and `trigger()` functions are
automatically called by ControlContainer's
[\#reconnectControls](#reconnectControls) and
[\#applyLayer](#applyLayer) functions to make activating different
layers of functionality easy.

A Control can react to changes in multiple [Mixxx
ControlObjects](mixxxcontrols) by overriding its `connect()` function.
Refer to the source code of [\#SamplerButton](#SamplerButton) for an
example.

### Shift layers

Controls can be used to manage alternate behaviors in different
conditions. The most common use case for this is for shift buttons. For
that case, assign functions to the `shift` and `unshift` properties that
manipulate the Control appropriately. In some cases, using the
`shift`/`unshift` functions to change the Control's inCo, outCo, or
group properties will be sufficient. Refer to the source code for
[\#HotcueButton](#HotcueButton) for an example. In more complex cases,
changing `input()` and `output()` may be required. Refer to
[\#SamplerButton](#SamplerButton) and [\#EffectUnit](#EffectUnit) for
examples. To avoid redundancy (like typing the name of the inCo both as
the inCo property and in the `unshift()` function), the Control
constructor will automatically call the `unshift()` function if it
exists. The `shift()` and `unshift()` functions of
[\#ControlContainer](#ControlContainer) will call the appropriate
function of all the Controls within it that have that function defined
and will recursively decend into ControlContainers that are properties
of the parent ControlContainer.

### Tips and tricks

Control and its derivative objects use constructor functions with a
minimal amount of logic. Most of the functionality of Controls comes
from their prototype objects. In JavaScript, making a change to an
object's prototype immediately changes all existing and future objects
that have it in their prototype chain (regardless of the context in
which the derivative objects were created). This makes it easy to change
the behavior for all (of a subtype) of Control to accomodate the MIDI
signals used by a particular controller. For example, the [Hercules P32
DJ](Hercules%20P32%20DJ) controller sends and receives two sets of MIDI
signals for most physical components, one for when the shift button is
pressed and one for when the shift button is not pressed. The controller
changes the state of its LEDs when the shift buttons are pressed, which
is controlled by the alternate set of MIDI signals. These alternate MIDI
signals are the same as the unshifted ones, but the MIDI channel is 3
higher. So, to avoid having the LEDs flicker when the shift button is
pressed or having to define separate JavaScript Controls for every
physical controller component in its shifted and unshifted state, the
P32's init function has this code:

    Control.prototype.shiftOffset = 3;
    Control.prototype.shiftChannel = true;
    Button.prototype.sendShifted = true;

This causes the `Control.prototype.send()` function to send both the
shifted and unshifted MIDI signals when the Control's outCo changes. If
your controller uses the same MIDI channel but different MIDI control
numbers when a shift button is pressed, set
`Control.prototype.shiftControl` to true instead of
`Control.prototype.shiftChannel`.

Controls JS provides more convenient shortcuts for common situations. If
inCo and outCo are the same, you can specify 'co' in the options object
for the constructor to set both inCo and outCo. For example:

    var quantizeButton = new controls.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]'
        co: 'quantize'
    });

Setting the co property after calling the constructor will not
automatically set inCo and outCo; you would need to do that manually if
necessary.

Also, if a Control only needs its midi property specified for its
constructor, this can be provided simply as an array without wrapping it
in an object. For example:

    var playButton = new controls.PlayButton([0x90 + channel, 0x0A]);

instead of

    var playButton = new PlayButton({
        midi: [0x90 + channel, 0x0A]
    });

To avoid typing out the group for the constructor of each Control,
Controls that share a group can be part of a ControlContainer and the
ControlContainer's [\#reconnectControl](#reconnectControl)s method can
assign the group to all of them. Refer to the [\#Deck](#Deck)
ControlContainer documentation for an example.

## Button

A Button is a Control derivative for buttons/pads.

For example:

    var quantize = new controls.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]',
        co: 'quantize',
    });

By default, the inCo is toggled only when the button is pressed. For
buttons that activate an inCo only while they are held down, set the
onlyOnPress property to false. For example:

    var tempSlow = new controls.Button({
        midi: [0x91, 0x44],
        inCo: 'rate_temp_down',
        onlyOnPress: false,
    });

The button's LED is sent the value of the `on` property when outCo \> 0
and `off` when outCo \<= 0. By default, on is 127 (0x7F) and off is 0.
For buttons/pads with multicolor LEDs, you can change the color of the
LED by defining the `on` and `off` properties to be the MIDI value to
send for that state. For example, if the LED turns red when sent a MIDI
value of 127 and blue when sent a value of 126:

    MyController.padColors = {
        red: 127,
        blue: 126
    };
    MyController.quantize = new controls.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]',
        co: 'quantize',
        on: MyController.padColors.red,
        off: MyController.padColors.blue,
    });

Derivative Buttons are provided for many common use cases, documented in
the subsections below. These make it easy to map those kinds of buttons
without having to worry about particularities of Mixxx's ControlObjects
that can make mapping them not so straightforward. The PlayButton,
SyncButton, HotcueButton, and SamplerButton objects also provide
alternate functionality for when a shift button is pressed.

By default, this works for controllers that send MIDI messages with a
different 3rd byte of the MIDI message (value) to indicate the button
being pressed/released, with the first two bytes (status and control)
remaining the same for both press and release. If your controller sends
separate MIDI note on/off messages with on indicated by the first nybble
(hexadecimal digit) of the first (status) byte being 9 and note off with
the first nybble being 8, in your script's init function, set
Button.prototype.separateNoteOnOff to true and map both the note on and
off messages in XML to the Button object's input property.

### PlayButton

Default behavior: play/pause  
Shift behavior: go to start of track and stop

LED behavior depends on cue mode selected by the user in the preferences
Refer to the
[manual](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
for details.

### CueButton

Behavior depends on cue mode configured by the user in the preferences  
Refer to the
[manual](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
for details.

### SyncButton

Default behavior: momentary sync without toggling sync lock  
Shift behavior: toggle sync lock (master sync)

### LoopToggleButton

Toggle a loop on/off

### HotcueButton

Default behavior: set hotcue if it is not set. If it is set, jump to
it.  
Shift behavior: delete hotcue

The LED indicates whether the hotcue is set.

Pass the number of the hotcue as the number property of the options
argument for the constructor. For example:

    var hotcues = [];
    for (var i = 1; i <= 8; i++) {
        hotcues[i] = new controls.HotcueButton({
            number: i,
            group: '[Channel1]',
            midi: [0x91, 0x26 + i],
        });
    }

### SamplerButton

Default behavior: Press the button to load the track selected in the
library into an empty sampler. Press a loaded sampler to play it from
its cue point. Press again while playing to jump back to the cue
point.  
Shift behavior: If the sampler is playing, stop it. If the sampler is
stopped, eject it.

Specify the sampler number as the number property of the object passed
to the constructor. There is no need to manually specify the group. For
example:

    var samplerButtons = [];
    for (var n = 1; n <= 8; n++) {
        samplerButtons[n] = new controls.SamplerButton({
            number: n,
            midi: [0x91, 0x02],
        });
    )};

When the sampler is loaded, the LED will be set to the value of the "on"
property. When the sampler is empty, the LED will be set to the value of
the "off" property. These are inherited from Button.prototype if they
are not manually specified. If your controller's pads have multicolor
LEDs, specify the value to send for a different LED color with the
playing property to set the LED to a different color while the sampler
is playing. For example:

    MyController.padColors = {
    // These values are just examples, consult the MIDI documentation from your controller's
    manufacturer to find the values for your controller. If that information is not available,
    guess and check to find the values.
        red: 125,
        blue: 126,
        purple: 127,
        off: 0
    };
    var samplerButton = [];
    var samplerButton[1] = new controls.SamplerButton(
        midi: [0x91, 0x02],
        number: 1,
        on: MyController.padColors.blue,
        playing: MyController.padColors.red,
        // off is inherited from Button.prototype
    )};

## Pot

A Pot is a Control for potentiometers (faders and knobs) with finite
ranges, although it can be adapted for infintely turning encoders. Using
a Pot Control is helpful because Pot.connect() and Pot.disconnect() take
care of soft takeover when switching layers with
ControlContainer.reconnectControls() and ControlContainer.applyLayer().
Soft takeover is not activated until the first input is received so it
does not interfere with setting initial values for controllers that can
report that information.

To adapt a Pot for an infinitely rotating encoder, replace its
inValueScale() function with a function that increments or decrements
the parameter depending on the direction the encoder is turned. For
example, if the encoder sends a MIDI value of 1 for a left turn and 127
for a right turn:

    MyController.SomePot.inValueScale = function (value) {
        if (value === 1) {
            return this.getParameterIn() - .05;
        } else if (value === 127) {
            return this.getParameterIn() + .05;
        }
    }

## RingEncoder

RingEncoder is a Control for encoders with LED rings around them. These
are different from Pots because they are sent MIDI messages to keep
their LED rings in sync with the state of Mixxx and do not require soft
takeover.

These encoders can often be pushed like a button. Usually, it is best to
use a separate Button Control to handle the MIDI signals from pushing
it.

## ControlContainer

A ControlContainer is an object that contains Controls as properties,
with methods to help iterate over those Controls. Documentation for each
method is below.

### forEachControl

Iterate over all Controls in this ControlContainer and perform an
operation on them.

Function arguments:

1.  operation, function that takes 1 argument: the function to call for
    each Control. Takes each Control as its first argument. "this" in
    the context of the function refers to the ControlContainer.
2.  recursive, boolean, optional: whether to call forEachControl
    recursively for each ControlContainer within this ControlContainer.
    Defaults to true if ommitted.

### reconnectControls

Disconnect and reconnect output callbacks for each Control. Optionally
perform an operation on each Control between disconnecting and
reconnecting the output callbacks. Arguments are the same as
[\#forEachControl](#forEachControl).

### shift

Call each Control's shift() function if it exists. This iterates
recursively on any Controls in ControlContainers that are properties of
this, so there is no need to call shift() on each child
ControlContainer. This function takes no arguments.

### unshift

Call each Control's unshift() function if it exists. This iterates
recursively on any Controls in ControlContainers that are properties of
this, so there is no need to call unshift() on each child
ControlContainer. This function takes no arguments.

### applyLayer

Activate a new layer of functionality. Layers are merely objects with
properties to overwrite the properties of the Controls within this
ControlContainer. Layer objects are deeply merged. If a new layer does
not define a property for a Control, the Control's old property will be
retained.

In the most common case, for providing alternate functionality when a
shift button is pressed, using `applyLayer()` is likely overcomplicated
and may be slow. Use `shift()`/`unshift()` instead. ''applyLayer() ''may
be useful for cycling through more than two alternate layers.

For example:

    someControlContainer.applyLayer({
        someButton: { inCo: 'alternate inCo' },
        anotherButton: { outCo: 'alternate outCo' }
    });

By default, the old layer's output callbacks are disconnected and the
new layer's output callbacks are connected. To avoid this behavior,
which would be desirable if you are not changing any output
functionality, pass false as the second argument to applyLayer().

## Deck

Deck is a ControlContainer with methods for conveniently changing the
group attributes of contained Controls to switch the deck that a set of
Controls is manipulating. The setCurrentDeck() method takes the new deck
as a string and sets the Controls' group property appropriately,
including for equalizer knobs and QuickEffect (filter) knobs.

The Deck constructor takes one argument, which is an array of deck
numbers to cycle through with the toggle() method. Typically this will
be \[1, 3\] or \[2, 4\].

To map your own controller, create a custom derivative of Deck and
create instances of your custom Deck objects in your controller's init()
function. Use a constructor function to create all the Controls you need
for your particular controller and assign your custom derivative's
prototype to Deck. For example:

    MyController.init = function () {
        this.leftDeck = new MyController.Deck([1, 2]);
        this.rightDeck = new MyController.Deck([2, 4]);
    };
    MyController.Deck = function (deckNumbers, midiChannel) {
        // Call the Deck constructor to setup the currentDeck and deckNumbers properties.
        controls.Deck.call(this, deckNumbers);
        this.playButton = new PlayButton([0x90 + midiChannel, 0x01]);
        this.CueButton = new CueButton([0x90 + midiChannel, 0x02]);
        this.hotcueButtons = [];
        for (var i = 1; i <= 8; i++) {
            this.hotcueButtons[i] = new HotcueButton({
                midi: [0x90 + midiChannel, 0x10 + i],
                number: i
            });
        }
        // ... define as many other Controls as necessary ...
    
        // Set the group properties of the above Controls and connect their output callback functions
        // Without this, the group property for each Control would have to be specified to its
        // constructor.
        this.reconnectControls(function (c) {
            if (c.group === undefined) {
                // 'this' inside a function passed to reconnectControls refers to the ControlContainer.
                c.group = this.currentDeck;
            }
        });
    };
    MyController.Deck.prototype = new controls.Deck();

## EffectUnit

This ControlContainer provides Controls designed to be mapped to the
common arrangement of 4 knobs and 4 buttons for controlling effects. 3
knobs are used for controlling effect metaknobs or parameters, depending
on whether the effects' parameters are shown. The other knob is used for
the dry/wet knob of the whole chain or the superknob when shift is
pressed. 3 buttons are used for enabling effects and the other button
toggles the effect unit between hiding and showing effect parameters.
The Controls provided are:

  - dryWetKnob ([\#Pot](#Pot))
  - showParametersButton ([\#Button](#Button))
  - enableButtons\[1-3\] ([\#ControlContainer](#ControlContainer) of
    [\#Button](#Button)s)
  - knobs\[1-3\] ([\#ControlContainer](#ControlContainer) of
    [\#Pot](#Pot)s)
  - enableOnChannelButtons ([\#ControlContainer](#ControlContainer) of
    [\#Button](#Button)s)

When the effect unit is showing the metaknobs of the effects but not
each parameter, the knobs control the metaknobs. The enableButtons
control whether each effect is enabled. Pressing an enableButton with
shift switches to the next available effect.

When the effect unit is showing all the parameters, the knobs behave
differently depending on whether an effect is focused. When there is no
focused effect (the default state), the knobs control the effect
metaknobs like they do when parameters are not showing. When an effect
is focused, the knobs control the first 3 parameters of the focused
effect. An effect can be focused by pressing shift + its enableButton or
clicking the focus button on screen. Pressing shift + the enableButton
for the focused effect again unfocuses the effect.

The enableOnChannelButtons allow assigning the effect unit to different
channels and are named after the Mixxx channel they affect. Not all
controllers have buttons to map these. The following Buttons are
provided by default:

  - Channel1
  - Channel2
  - Channel3
  - Channel4
  - Headphones
  - Master
  - Microphone
  - Auxiliary1

You can easily add more, for example for additional microphones,
auxiliary inputs, or samplers by calling
`enableOnChannelButtons.addButton('CHANNEL_NAME')` (do not put brackets
around the CHANNEL\_NAME).

### Setup

To map an EffectUnit for your controller, call the constructor with the
unit number of the effect unit as the only argument. Then, set the midi
attributes for the showParametersButton, enableButtons\[1-3\], and
optionally enableOnChannelButtons. After the midi attributes are set up,
call EffectUnit.init() to set up the output callbacks. For example:

    MyController.effectUnit = new controls.EffectUnit(1);
    MyController.effectUnit.enableButtons[1].midi = [0x90, 0x01];
    MyController.effectUnit.enableButtons[2].midi = [0x90, 0x02];
    MyController.effectUnit.enableButtons[3].midi = [0x90, 0x03];
    MyController.effectUnit.knobs[1].midi = [0xB0, 0x01];
    MyController.effectUnit.knobs[2].midi = [0xB0, 0x02];
    MyController.effectUnit.knobs[3].midi = [0xB0, 0x03];
    MyController.effectUnit.dryWetKnob.midi = [0xB0, 0x04];
    MyController.effectUnit.showParametersButton.midi = [0x90, 0x04];
    MyController.effectUnit.enableOnChannelButtons.Channel1 = [0x90, 0x05];
    MyController.effectUnit.enableOnChannelButtons.Channel2 = [0x90, 0x06];
    MyController.effectUnit.init();

Controllers designed for Serato and Rekordbox often have an encoder
instead of a dry/wet knob (labeled "Beats" for Serato or "Release FX"
for Rekordbox) and a button labeled "Tap". If the encoder sends a MIDI
signal when pushed, it is recommended to map the encoder push to the
EffectUnit's showParametersButton, otherwise map that to the "Tap"
button. To use the dryWetKnob Pot with an encoder, replace its
inValueScale() function with a function that can appropriately handle
the signals sent by your controller. Refer to the [\#Pot](#Pot)
documentation for an example.

For the shift functionality to work, the shift button of your controller
must be mapped to a function that calls the shift()/unshift() functions
of the EffectUnit on button press/release. If the EffectUnit is a
property of another ControlContainer (for example a Deck), calling
shift() and unshift() on the parent ControlContainer will recursively
call it on the EffectUnit too (just like it will for any other
ControlContainer).
