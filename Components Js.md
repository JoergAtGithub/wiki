# Components JS Library

Components JS is a JavaScript library that makes it easier to code
controller mappings for Mixxx. It lets you focus more on your controller
and less on the details of MIDI signals and how Mixxx works. It is
centered around JavaScript objects called Components that represent a
physical component of a controller, such as a button, knob, fader, or
encoder. Components provide generic functions that can be made to work
for most use cases just by changing some attributes of the Component,
without having to write many or any custom functions. The library also
provides more specialized Components for common use cases. Components
can be organized into ComponentContainer objects, making it easy to
iterate over them and change their behavior to switch between different
modes.

Components JS is new in Mixxx 2.1 and does not work with older versions
of Mixxx. To use the library, in the `<scriptfiles>` element at the top
of your mapping's [XML
file](MIDI%20controller%20mapping%20file%20format), load the Lodash
library and the Components library (above the link to your controller's
script file):

    <file filename="lodash.mixxx.js"/>
    <file filename="midi-components-0.0.js"/>
    <file functionprefix="MyController" filename="My_Controller_SCRIPT.js"/>

Components JS uses a few functions from [Lodash](http://lodash.com/),
which is why they both need to be loaded. Importing the
midi-components-0.0.js file makes the library accessible by an object
called `components` (plural, lower case).

If you are not familiar with object oriented programming in JavaScript,
read Mozilla Developer Network's [Object-oriented JavaScript
introduction](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS).
If you are familiar with OOP in other languages but new to JavaScript,
you can skip ahead to the [Constructors and object
instances](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS#Constructors_and_object_instances)
section of that tutorial.

## File structure

To map most controllers, create a custom subtype of [\#Deck](#Deck) and
create instances of your custom Deck objects in your controller's `init`
function. Use the custom Deck's constructor function to create all the
Components you need for your particular controller. The example below is
for a typical 2 deck controller. If you are mapping a controller with a
different layout, some changes to this general structure may be
necessary. There is a lot to explain here, so worry about understanding
every detail yet:

    // Declare the variable for your controller and assign it to an empty object
    var MyController = {};
    
    // Mixxx calls this function on startup or when the controller
    // is enabled in the Mixxx Preferences
    MyController.init = function () {
        // create an instance of your custom Deck object for each side of your controller
        MyController.leftDeck = new MyController.Deck([1, 3], 1);
        MyController.rightDeck = new MyController.Deck([2, 4], 2);
    };
    
    MyController.shutdown = function () {
        // send whatever MIDI messages you need to turn off the lights of your controller
    };
    
    // implement a constructor for a custom Deck object specific to your controller
    MyController.Deck = function (deckNumbers, midiChannel) {
        // Call the generic Deck constructor to setup the currentDeck and deckNumbers properties,
        // using Function.prototype.call to assign the custom Deck being constructed
        // to 'this' in the context of the generic components.Deck constructor
        // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call
        components.Deck.call(this, deckNumbers);
        this.playButton = new components.PlayButton([0x90 + midiChannel, 0x01]);
        this.cueButton = new components.CueButton([0x90 + midiChannel, 0x02]);
        this.syncButton = new components.SyncButton([0x90 + midiChannel, 0x03]);
        this.pflButton = new components.Button({
            midi: [0x90 + channel, 0x04],
            key: 'pfl',
        });
        this.hotcueButtons = [];
        for (var i = 1; i <= 8; i++) {
            this.hotcueButtons[i] = new components.HotcueButton({
                midi: [0x90 + midiChannel, 0x10 + i],
                number: i,
            });
        }
        
        this.volume = new components.Pot({
            midi: [0xB0 + midiChannel, 0x01],
            inKey: 'volume',
        });
        
        this.eqKnob = [];
        for (var k = 1; k <= 3; k++) {
            this.eqKnob[k] = new components.Pot({
                midi: [0xB0 + midiChannel, 0x02 + k],
                group: '[EqualizerRack1_' + this.currentDeck + '_Effect1]',
                inKey: 'parameter' + k,
            });
        }
        
        // ... define as many other Components as necessary ...
    
        // Set the group properties of the above Components and connect their output callback functions
        // Without this, the group property for each Component would have to be specified to its
        // constructor.
        this.reconnectComponents(function (c) {
            if (c.group === undefined) {
                // 'this' inside a function passed to reconnectComponents refers to the ComponentContainer
                // so 'this' refers to the custom Deck object being constructed
                c.group = this.currentDeck;
            }
        });
        // when called with JavaScript's 'new' keyword, a constructor function
        // implicitly returns 'this'
    };
    // give your custom Deck all the methods of the generic Deck in the Components library
    MyController.Deck.prototype = new components.Deck();

## Component

The basic building block of the library are Component objects that
represent a physical component of a controller, such as a button, knob,
fader, or encoder. The JavaScript object encapsulates all the
information needed to receive MIDI input from that component and send
MIDI signals out to the controller to activate its LED(s).

Components should generally be properties of a
[\#ComponentContainer](#ComponentContainer) object. Most Components
should be properties of a custom [\#Deck](#Deck) object as demonstrated
in the example in the previous section.

In general, you should not use the basic Component constructor directly;
instead, use one of its subtypes ([\#Button](#Button), [\#Pot](#Pot), or
[\#Encoder](#Encoder)). If you do need to use Component directly, do not
confuse it with the `components` object (plural, lower case) that
contains all the objects for the library; access Component as
`components.Component` (plural lower case then singular upper case).

### Setup

The input function of each Component needs to be mapped to the incoming
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

In the future Mixxx will be able to [register MIDI inputs from
JavaScript](registering%20midi%20input%20handlers%20from%20javascript),
so that will not be necessary. Until then, if you decide to rename a
Component or map it to different MIDI input signals, you need to edit
the XML file and reload the mapping in Mixxx's Preferences. The output
does not need to be mapped in XML. It is handled by the library in
JavaScript.

Create Components by calling the constructor with JavaScript's "new"
keyword. The Component constructor takes a single object as an argument.
Generally you should provide this as an [object
literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Object_literals).
Each property of that object passed to the constructor becomes a
property of the new Component object, making it easy to customize the
functionality of the Component. The constructors for all Component
subtypes work the same way. Most Components need at least these
properties defined:

  - **midi** (array with 2 numbers): the first two MIDI bytes that the
    controller sends/receives when the physical component changes state.
    Refer to the [MIDI Crash Course](MIDI%20Crash%20Course) if you do
    not understand what this means.
  - **inKey** (string): the key of the [Mixxx
    ControlObject](mixxxcontrols) that this Component manipulates when
    it receives a MIDI input signal
  - **outKey** (string): when the [Mixxx ControlObject](mixxxcontrols)
    specified by this key changes value, the `output` function will be
    called
  - **group** (string): the group of the [Mixxx
    ControlObjects](mixxxcontrols) for both inKey and outKey, for
    example \[Channel1\] for deck 1

For example:

    var quantizeButton = new components.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]'
        inKey: 'quantize',
        outKey: 'quantize',
    });

If `inKey` and `outKey` are the same, you can specify `key` in the
options object for the constructor to set both the `inKey` and `outKey`
properties of the new Component. For example:

    var quantizeButton = new components.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]',
        key: 'quantize',
    });

Setting the `key` property after calling the constructor will not
automatically set `inKey` and `outKey`; you would need to do that
manually if necessary.

### Methods

The following methods (in JavaScript, methods are just object properties
that happen to be functions) must be defined for every Component, but in
most cases the defaults (from the inherited prototype Component) will
work so you do not need to define them yourself:

  - **input**: the [function that receives MIDI
    input](MIDI%20scripting#MIDI%20input%20handling%20functions)
  - **output**: the [function that gets called when outKey changes
    value](midi%20scripting#Connect%20output%20callback%20functions).
    Typically this sends MIDI output to the controller to change the
    state of an LED, but it can do anything.
  - **connect**: register `output` as the callback function that gets
    executed when the value of the [Mixxx ControlObject](mixxxcontrols)
    specified by `group`, `outKey` changes. This is called automatically
    by the Component constructor if `group` and `outKey` are defined
    (otherwise it needs to be called after construction). Implement a
    custom function if you need to connect callbacks for multiple Mixxx
    ControlObjects in one Component. Refer to the source code of
    [SamplerButton.prototype.connect](#SamplerButton) for an example.

The following methods are called by the default Component `input` and
`output` methods, as well as the default `input` functions of
[\#Button](#Button), [\#Pot](#Pot), and [\#Encoder](#Encoder). If you do
not need to implement complex custom behavior, you can overwrite these
instead of the default `input` and `output` methods:

  - **inValueScale**: takes the third byte of the incoming MIDI signal
    as its first argument and returns the value to set `group`, `inKey`
    to
  - **outValueScale**: takes the value of `group`, `outKey` as its first
    argument and returns the third byte of the outgoing MIDI signal

Each Component also has these methods that you probably should not
overwrite:

  - **disconnect**: disconnect the `output` function from being called
    when `group`, `outKey` changes
  - **trigger**: manually call `output` with the same arguments as if
    `group`, `outKey` had changed
  - **send**: send a 3 byte (short) MIDI message out to the controller.
    The first two bytes of the MIDI message are specified by the
    Component's `midi` property. The third MIDI byte is provided as the
    first argument to the `send` function.
  - **inGetParameter**: returns the value of `group`, `inKey` normalized
    to a 0-1 scale
  - **inSetParameter**: sets the value of `group`, `inKey` to the
    function's first argument, normalized to a 0-1 scale
  - **inGetValue**: returns the value of `group`, `inKey`
  - **inSetValue**: sets the value of `group`, `inKey` to the function's
    first argument
  - **inToggle**: sets `group`, `inKey` to its inverse (0 if it is \>0;
    1 if it is 0)
  - **outGetParameter**: returns the value of `group`, `outKey`
    normalized to a 0-1 scale
  - **outSetParameter**: sets the value of `group`, `outKey` to the
    function's first argument, normalized to a 0-1 scale
  - **outGetValue**: returns the value of `group`, `outKey`
  - **outSetValue**: sets the value of `group`, `outKey` to the
    function's first argument
  - **outToggle**: sets `group`, `outKey` to its inverse (0 if it is
    \>0; 1 if it is 0)

### Optional properties

The following properties can be specified in the options object passed
to the Component constructor to customize the Component's
initialization. Changing their value after creating the Component does
not do anything.

  - **outConnect** (boolean, default true): whether to call `connect` in
    the constructor (assuming `group` and `outKey` were specified in the
    options object)
  - **outTrigger** (boolean, default true): whether to call `trigger` in
    the constructor (assuming `group` and `outKey` were specified in the
    options object)

Some controllers send and receive two sets of MIDI signals for most
physical components, one for when the shift button is pressed and one
for when the shift button is not pressed. To avoid defining two
Components for every physical component of your controller, set the
following options as appropriate:

  - **sendShifted** (boolean, default false): whether to send a second,
    shifted MIDI message for every call to `send`
  - **shiftChannel** (boolean, default false): whether the shifted MIDI
    message changes the MIDI channel (second nybble of the first byte of
    the MIDI signal)
  - **shiftControl** (boolean, default false): whether the shifted MIDI
    message changes the MIDI control number (second byte) of the MIDI
    signal
  - **shiftOffset** (number, default 0): how much to shift the MIDI
    channel or control number by

To avoid having to define those properties for every Component, you can
change the properties of `components.Component.prototype` in your
controller's `init` function. For example:

    components.Component.prototype.shiftOffset = 3;
    components.Component.prototype.shiftChannel = true;
    components.Component.prototype.sendShifted = true;

### Syntactic sugar

Components JS provides convenient shortcuts for common situations.

To avoid typing out the group for the constructor of each Component,
Components that share a group can be part of a ComponentContainer and
the [ComponentContainer's](#ComponentContainer) `reconnectComponents`
method can assign the group to all of them. Refer to the [\#Deck](#Deck)
ComponentContainer documentation for an example.

If a Component only needs its `midi` property specified for its
constructor, this can be provided simply as an array without wrapping it
in an object. For example:

    var playButton = new components.PlayButton([0x90 + channel, 0x0A]);

instead of

    var playButton = new components.PlayButton({
        midi: [0x90 + channel, 0x0A]
    });

## Button

A Button is a subtype of Component for buttons/pads. Subtypes of Button
are provided for many common use cases, documented in the subsections
below, making it easy to map those buttons without having to worry about
particularities of Mixxx's ControlObjects. To use the Button subtypes,
you only need to specify their `midi` and `group` properties, except for
HotcueButton and SamplerButton.

A generic Button toggles the state of a binary `inKey` and sends
outgoing MIDI messages indicating whether a binary `outKey` is on or
off. Button adds the following properties to Component:

  - **type**: determines the behavior of the Button. Can be any of these
    values:
  - *Button.prototype.types.push* (default): set inKey to 1 on button
    press and 0 on button release. For example, use this type with the
    beatloop\_activate [Control](mixxxcontrols)
  - *Button.prototype.types.toggle*: invert value of inKey on button
    press. Use this with Controls whose values indicate the state of a
    switch, for example pfl
  - *Button.prototype.types.powerWindow*: like toggle, but toggles the
    value of inKey again on button up when long pressed, for example
    with \[EffectRack1\_EffectUnit2\_Effect1\], enabled Control.
  - **on** (number, default 127): number to send as the third byte of
    outgoing MIDI messages when `group`, `outKey` is on (its value is \>
    0)
  - **off** (number, default 0): number to send as the third byte of
    outgoing MIDI messages when `group`, `outKey` is off (its value is
    0)
  - **isPress** (function): function that takes the same first 4
    arguments as a MIDI input function (channel, control, value, status)
    and returns a boolean indicating whether the button was pressed.

For buttons/pads with multicolor LEDs, you can change the color of the
LED by defining the `on` and `off` properties to be the MIDI value to
send for that state. For example, if the LED turns red when sent a MIDI
value of 127 and blue when sent a value of 126:

    MyController.padColors = {
        red: 127,
        blue: 126
    };
    MyController.quantize = new components.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]',
        key: 'quantize',
        type: Button.prototype.types.toggle,
        on: MyController.padColors.red,
        off: MyController.padColors.blue,
    });

The default `isPress` function works for controllers that indicate
whether a button is pressed or released by sending a different third
MIDI byte (value). Some controllers distinguish between a button press
and release by changing the first nybble (hexadecimal digit) of the
first byte of the MIDI message, also known as an opcode. These
controllers typically use an opcode of 9 to indicate a button press and
8 to indicate a button release. Both the press and release signals need
to be mapped in the XML file to the Button's `input` method. To make
Button work for such a controller, reimplement the prototype `isPress`
function in your mappings's `init` function:

    components.Button.prototype.isPress = function (channel, control, value, status) {
        return (status & 0xF0) === 0x90;
    }

### PlayButton

Default behavior: play/pause  
Shift behavior: reverse playback

LED behavior depends on cue mode selected by the user in the preferences
Refer to the
[manual](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
for details.

### CueButton

Default behavior: depends on cue mode configured by the user in the
preferences  
Shift behavior: stop playback and go to start of track Refer to the
[manual](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
for details.

### SyncButton

Default behavior: momentary sync without toggling sync lock  
Shift behavior: toggle sync lock (master sync)

### HotcueButton

Default behavior: set hotcue if it is not set. If it is set, jump to
it.  
Shift behavior: delete hotcue

The LED indicates whether the hotcue is set.

Pass the number of the hotcue as the `number` property of the options
argument for the constructor. For example:

    var hotcues = [];
    for (var i = 1; i <= 8; i++) {
        hotcues[i] = new components.HotcueButton({
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
        samplerButtons[n] = new components.SamplerButton({
            number: n,
            midi: [0x91, 0x02],
        });
    )};

You can also make the SamplerButtons velocity sensitive by setting the
`volumeByVelocity: true` property on the object that gets passed to the
constructor. This will change the volume at which the sample is being
played at depending on how hard you pressed the button. Obviously, it
will only work if your hardware features velocity sensitive buttons.

    var samplerButtons = [];
    for (var n = 1; n <= 8; n++) {
        samplerButtons[n] = new components.SamplerButton({
            number: n,
            midi: [0x91, 0x02],
            volumeByVelocity: true,
        });
    )};

When the sampler is loaded, the LED will be sent a MIDI message with the
value of the `on` property (default 127) When the sampler is empty, the
LED will be sent a MIDI message with the value of the `off` property
(default 0). If your controller's pads have multicolor LEDs, specify the
value to send for a different LED color with the `playing` property to
set the LED to a different color while the sampler is playing. For
example:

    MyController.padColors = {
    // These values are just examples, consult the MIDI documentation from your controller's
    // manufacturer to find the values for your controller. If that information is not available,
    // guess and check to find the values.
        red: 125,
        blue: 126,
        purple: 127,
        off: 0
    };
    var samplerButton = [];
    var samplerButton[1] = new components.SamplerButton(
        midi: [0x91, 0x02],
        number: 1,
        on: MyController.padColors.blue,
        playing: MyController.padColors.red,
        // off is inherited from Button.prototype
    )};

### EffectAssignmentButton

An EffectAssignmentButton routes a deck through an EffectUnit. It is
separate from the
[\#EffectUnit](#EffectUnit)-ComponentContainer-because-it-is-meant-to-be-a-part-of-a-[\#Deck](#Deck).-Using-[Deck.setCurrentDeck](#Deck)
to switch decks will switch the deck an EffectAssignmentButton assigns
an EffectUnit to.

    var effectAssignmentButtons = [];
    for (var u = 1; u <= 4; u++) {
        effectAssignmentButtons = new components.EffectAssignmentButton({
            midi: [0x92, 0x20 + u],
            effectUnit: u,
            group: '[Channel1]',
        )};
    }

## Pot

A Pot is a Component subtype for potentiometers (faders and knobs) with
finite ranges. Pot's `connect` and `disconnect` methods take care of
soft takeover when switching layers with
[ComponentContainer's](#ComponentContainer) `reconnectComponents` or
`applyLayer` methods. Soft takeover is not activated until the first
input signal is received, so it does not interfere with setting initial
values for controllers that can report that information.

For example:

    var eqKnobs = [];
    for (var i = 1; i <= 3; i++) {
        eqKnobs[i] = new components.Pot({
            midi: [0xB1, 0x02 + i],
            group: '[EqualizerRack1_[Channel1]_Effect1]',
            inKey: 'parameter' + i,
        });
    }

To use a Pot with a fader or knob that uses 14 bit MIDI (sends two MIDI
messages, one with a least significant byte and one with a most
significant byte) for higher precision, map the incoming signals to the
Pot's `inputLSB` and `inputMSB` functions instead of `input` in the XML
file. Nothing extra needs to be done in JavaScript.

Pot Components support an optional relative mode as an alternative to
dealing with soft takeover. To use it, set the `relative` property to
`true` in the options object for the constructor. In this mode, moving
the Pot will adjust the Mixxx Control relative to its current value.
Holding shift and moving the Pot will not affect the Mixxx Control This
allows the user to continue adjusting the Mixxx Control after the Pot
has reached the end of its physical range. This mode may be helpful for
using tempo faders with master sync. If the controller sends different
MIDI signals for the potentiometer when shift is pressed, be sure to map
both the unshifted and shifted signals in the XML file. For example:

    var tempoFader = new components.Pot({
        midi: [0xB1, 0x32],
        group: '[Channel1]',
        inKey: 'rate',
        relative: true,
    });

## Encoder

Encoder is a Component for infinitely turning encoders. The default
`input` function assumes the encoder sends MIDI signals on a continous
scale from 0 to 127 (0x7F). If the encoder sends relative MIDI signals
to indicate whether it turns right or left, you will need to define your
own `input` function. For example, for an encoder that sends a value of
1 when it is turned left and a value of 127 when it is turned right:

    MyController.SomeEncoder = new components.Encoder({
        midi: [0xB1, 0x03],
        group: '[Channel1]',
        inKey: 'pregain',
        input: function (channel, control, value, status, group) {
            if (value === 1) {
                this.inSetParameter(this.inGetParameter() - .05);
            } else if (value === 127) {
                this.inSetParameter(this.inGetParameter() + .05);
            }
        },
    });

To map an Encoder with an LED ring around it that receives MIDI signals
on a continuous 0-127 scale, define an `outKey` property in the options
object for the constructor. Similar to `input`, if the LEDs do not
respond to a continuous 0-127 scale, define your own `output` function.
If `outKey` and `inKey` are the same, you can just specify one `key`
property for the constructor.

Encoders can often be pushed like a button. Usually, it is best to use a
separate Button Component to handle the MIDI signals from pushing it.

## ComponentContainer and Managing Layers

A ComponentContainer is an object that contains Components as
properties. ComponentContainer has methods to easily iterate through the
Components, which makes it easy to manage different layers of
functionality. The basic ComponentContainer methods are:

  - **forEachComponent**: Iterate over all Components in this
    ComponentContainer and perform an operation on them. The operation
    is a function provided as the first argument to `forEachComponent`.
    The operation function takes each Component as its first argument.
    In the context of the operation function, `this` refers to the
    ComponentContainer. `forEachComponent` iterates recursively through
    the Components in any ComponentContainers and arrays that are
    properties of this ComponentContainer. If you do not want
    `forEachComponent` to operate recursively, pass `false` as the
    second argument to `forEachComponent`.
  - **reconnectComponents**: Call each Component's `disconnect` method,
    optionally perform an operation on it, then call its `connect` and
    `trigger` methods to sync the state of the controller's LEDs.
    Arguments are the same as `forEachComponent`.

Typically, `reconnectComponents` is used to switch between layers. The
callback passed to reconnectComponents can manipulate each Component's
properties as appropriate for the new layer. Below is a basic example
for switching between decks 1 and 3. This is a simple example that does
not handle the complexities presented by EQs, QuickEffects, or
EffectAssignmentButtons like [Deck.setCurrentDeck](#Deck) does.

    // Define a constructor for a ComponentContainer that adds some Components to it
    var ExampleContainer = function () {
        this.play = new components.PlayButton({
            midi: [0x91, 0x40],
            group: '[Channel1]',
        });
        this.cue = new components.CueButton({
            midi: [0x91, 0x41],
            group: '[Channel1]',
        });
    };
    // This will give any object created with "new exampleContainer()"
    // the ComponentContainer methods.
    exampleContainer.prototype = new components.ComponentContainer();
    
    var demonstration = new ExampleContainer();
    demonstration.reconnectComponents(function (component) {
        component.group = '[Channel3]';
    )};

In simple cases like the demonstration above, changing a property of
each Component in the callback passed to `reconnectComponents` is
sufficient. When more complex manipulation is required, especially if
the manipulation varies between Components, it is a good idea to use the
`reconnectComponents` callback to call a specific method on each
Component. This keeps all the logic for that Component together instead
of scattering it between the Component construction and the layer
switching function.

### Shift layers

The most common use case for changing layers is for shift buttons. If
your controller sends different MIDI signals depending on whether shift
is pressed, map both the shifted and unshifted input signals to the
Component's `input` function in XML. For each Component that has
different behavior depending on whether shift is pressed, implement
`shift` and `unshift` methods that manipulate the Component
appropriately. When the shift button is pressed call
`ComponentContainer.shift()` and the shift method of each Component in
the ComponentContainer will be executed (if it exists). When the shift
button is released, call `ComponentContainer.unshift()` to call each
Component's `unshift` method.

Note that any *Button.prototype.types.push* type [Buttons](#Button) in
the ComponentContainer will have their inKey reset to 0 if the user
happens to have them pressed when `ComponentContainer.shift()` or
`ComponentContainer.unshift()` is called. This prevents the Button's
inKey from getting stuck in a pressed (1) state, which can cause
confusing behavior with some [MixxxControls](MixxxControls).

For convenience, the Component constructor will automatically call the
`unshift` function if it exists. This allows you to avoid redundancy
when constructing Components.

To use separate `output` callback functions in shifted and unshifted
modes, the Component's `shift` and `unshift` functions need to call
`disconnect`/`connect` and `trigger`. ComponentContainer's
`shift`/`unshift` methods will not do this automatically like
`reconnectComponents`.

Generally, you should avoid making LEDs change when a shift button is
pressed. This is distracting if the user is pressing shift to use the
shifted functionality of a different part of the controller. If the
alternate layer is confined to a specific part of the controller,
changing LEDs is not an issue.

To handle the interaction of shifted and unshifted states with another
layer, you can create another system of methods for each Component that
changes properties of the Component when a layer is activated, and
within those methods, you can assign the `shift` and `unshift`
properties of the Component to different functions. Refer to the source
code of [\#EffectUnit](#EffectUnit) for an example.

## Deck

Deck is a [\#ComponentContainer](#ComponentContainer) with methods for
conveniently changing the `group` attributes of contained Components to
switch the deck that a set of Components is manipulating. The
`setCurrentDeck` method takes the new deck as a string and sets the
Components' `group` property appropriately, including for equalizer
knobs and QuickEffect (filter) knobs.

The Deck constructor takes one argument, which is an array of deck
numbers to cycle through with the `toggle` method. Typically this will
be `[1, 3]` or `[2, 4]`.

Refer to the [\#File structure](#File%20structure) section above for an
example.

## EffectUnit

EffectUnit is a [\#ComponentContainer](#ComponentContainer) that
contains Components designed to be mapped to the common arrangement of 4
knobs and 4 buttons for controlling effects. If your controller's
effects section has fewer components, the EffectUnit object provided by
Components JS probably will not be very helpful. You may want to read
the source code for the library's EffectUnit to get an idea for how to
map your controller though.

There is no need to use Components for the rest of your mapping if you
just want to use the EffectUnit from the library.

The Components provided are:

  - dryWetKnob ([\#Pot](#Pot))
  - effectFocusButton ([\#Button](#Button))
  - enableButtons\[1-3\] ([\#ComponentContainer](#ComponentContainer) of
    [\#Button](#Button)s)
  - knobs\[1-3\] ([\#ComponentContainer](#ComponentContainer) of
    [\#Pot](#Pot)s)

Refer to the [Standard Effects Mapping](Standard%20Effects%20Mapping)
page for a description of how to use the EffectUnit object. On the wiki
page for your controller, link to the [Standard Effects
Mapping](Standard%20Effects%20Mapping) page instead of rewriting a
description for your controller.

### Setup

To map an EffectUnit for your controller, call the constructor like the
[\#Deck](#Deck) constructor. The only argument to the constructor is an
array of numbers that specifies which EffectUnits pressing the
effectFocusButton with shift toggles between. Then, set the midi
attributes for the showParametersButton, enableButtons\[1-3\], and
optionally enableOnChannelButtons. After the `midi` attributes are set
up, call the EffectUnit's `init` method to set up the output callbacks.
For example:

    MyController.effectUnit = new components.EffectUnit([1, 3]);
    MyController.effectUnit.enableButtons[1].midi = [0x90, 0x01];
    MyController.effectUnit.enableButtons[2].midi = [0x90, 0x02];
    MyController.effectUnit.enableButtons[3].midi = [0x90, 0x03];
    MyController.effectUnit.knobs[1].midi = [0xB0, 0x01];
    MyController.effectUnit.knobs[2].midi = [0xB0, 0x02];
    MyController.effectUnit.knobs[3].midi = [0xB0, 0x03];
    MyController.effectUnit.dryWetKnob.midi = [0xB0, 0x04];
    MyController.effectUnit.effectFocusButton.midi = [0x90, 0x04];
    MyController.effectUnit.init();

Controllers designed for Serato and Rekordbox often have an encoder
instead of a dry/wet knob (labeled "Beats" for Serato or "Release FX"
for Rekordbox) and a button labeled "Tap". Map the `effectFocusButton`
to the controller's "Tap" button. To use the `dryWetKnob` Pot with an
encoder, replace its `input` function with a function that can
appropriately handle the signals sent by your controller. For example:

    MyController.effectUnit = new components.EffectUnit([1, 3]);
    MyController.effectUnit.enableButtons[1].midi = [0x90, 0x01];
    MyController.effectUnit.enableButtons[2].midi = [0x90, 0x02];
    MyController.effectUnit.enableButtons[3].midi = [0x90, 0x03];
    MyController.effectUnit.knobs[1].midi = [0xB0, 0x01];
    MyController.effectUnit.knobs[2].midi = [0xB0, 0x02];
    MyController.effectUnit.knobs[3].midi = [0xB0, 0x03];
    MyController.effectUnit.dryWetKnob.midi = [0xB0, 0x04];
    MyController.effectUnit.dryWetKnob.input = function (channel, control, value, status, group) {
        if (value === 1) {
           // 0.05 is an example. Adjust that value to whatever works well for your controller.
           this.inSetParameter(this.inGetParameter() - .05);
        } else if (value === 127) {
           this.inSetParameter(this.inGetParameter() + .05);
        }
    };
    MyController.effectUnit.effectFocusButton.midi = [0x90, 0x04];
    MyController.effectUnit.init();

For the shift functionality to work, the shift button of your controller
must be mapped to a function that calls the `shift`/`unshift` methods of
the EffectUnit on button press/release. Also, if your controller sends
different MIDI signals when shift is pressed, map those as well as the
unshifted signals to the `input` method of each Component in your XML
file. If the EffectUnit is a property of another
[\#ComponentContainer](#ComponentContainer) (for example a
[\#Deck](#Deck)), calling `shift` and `unshift` on the parent
ComponentContainer will recursively call it on the EffectUnit too (just
like it will for any other ComponentContainer).

### Assignment switches

Generally, most controllers should use
[\#EffectAssignmentButton](#EffectAssignmentButton)s in [\#Deck](#Deck)s
to enable effect units on decks. If you have a dedicated effects
controller that does not manipulate decks, the enableOnChannelButtons
provided by EffectUnit would be more appropriate. You can easily create
these by calling `enableOnChannelButtons.addButton('CHANNEL_NAME')` (do
not put brackets around the CHANNEL\_NAME) on the EffectUnit object,
then define their `midi` properties.
