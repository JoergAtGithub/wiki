# Components JS Library

Components JS is a JavaScript library that makes it easier to code
controller mappings for Mixxx. It lets you focus more on your controller
and less on the details MIDI signals and how Mixxx works. It is centered
around JavaScript objects called Components that represent a physical
component of a controller, such as a button, knob, fader, or encoder.
Components provide generic functions that can be made to work for most
use cases just by changing some attributes of the Component, without
having to write many or any custom functions. The library also provides
more specialized Components for common use cases. Components can be
organized into ComponentContainer objects, making it easy to iterate
over them and change their behavior to switch between different modes.

To use the library, in the `<scriptfiles>` element at the top of your
mapping's [XML file](MIDI%20controller%20mapping%20file%20format), load
the Lodash library and the Components library:

    <file filename="lodash.mixxx.js"/>
    <file filename="midi-components-0.0.js"/>

Components JS uses a few functions from [Lodash](http://lodash.com/),
which is why they both need to be loaded. Importing the
midi-components-0.0.js file makes the library accessible by an object
called `components` (plural, lower case).

## Component

A Component represents a physical component of a controller, such as a
button, knob, fader, or encoder. It encapsulates all the information
needed to receive MIDI input from that component and send MIDI signals
out to the controller to activate its LED(s). In general, you should not
use the Component object directly; instead, use one of its subtypes
([\#Button](#Button), [\#Pot](#Pot), or [\#Encoder](#Encoder)). If you
do need to use Component directly, do not confuse it with the
`components` object (plural, lower case) that contains all the objects
for the library; access Component as `components.Component`.

Components should generally be properties of a
[\#ComponentContainer](#ComponentContainer) object. Most Components
should be properties of a custom [\#Deck](#Deck) object, which is a
derivative of ComponentContainer.

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

In the future Mixxx will be able to register MIDI inputs from
JavaScript, so that will not be necessary. The output does not need to
be mapped in XML. It is handled by the library in JavaScript.

Create Components by calling the constructor with JavaScript's "new"
keyword. The Component constructor takes a single argument. This is an
options object containing properties that get merged with the Component
when it is created, making it easy to customize the functionality of the
Component. The constructors for all Component subtypes work the same
way. Most Components need at least these properties defined:

  - **midi** (array with 2 numbers): the first two MIDI bytes that the
    controller sends/receives when the physical component changes state
  - **group** (string): the group that both the inKey and outKey
    manipulate, for example `'[Channel1]`' for deck 1
  - **inKey** (string): the [Mixxx ControlObject](mixxxcontrols) that
    this Component manipulates when it receives a MIDI input signal
  - **outKey** (string): when this [Mixxx ControlObject](mixxxcontrols)
    changes value, the `output` function will be called

For example:

    var quantizeButton = new components.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]'
        inKey: 'quantize',
        outKey: 'quantize',
    });

### Methods

The following methods (in JavaScript, methods are just object properties
that happen to be functions) must be defined for every Component, but in
most cases the defaults will work so you do not need to define them
yourself:

  - **input**: the [function that receives MIDI
    input](MIDI%20scripting#MIDI%20input%20handling%20functions)
  - **output**: the [function that gets called when outKey changes
    value](midi%20scripting#Automatic%20reactions%20to%20changes%20in%20Mixxx).
    Typically this sends MIDI output to the controller to change the
    state of an LED, but it can do anything.
  - **connect**: register `output` as the callback function that gets
    executed when the value of `group`, `outKey` changes. Implement a
    custom function if you need to connect callbacks for multiple [Mixxx
    ControlObjects](mixxxcontrols) in one Component. Refer to the source
    code of [SamplerButton.prototype.connect](#SamplerButton) for an
    example.

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
    The first two bytes of the MIDI message are specified by the `midi`
    property. The third MIDI byte is provided as the first argument to
    the `send` function.
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

### Shift layers

Components can be used to manage alternate behaviors in different
conditions. The most common use case for this is for shift buttons. For
that case, assign functions to the `shift` and `unshift` properties that
manipulate the Component appropriately. If you ever need to check
whether a Component is in a shifted state, set its boolean `isShifted`
property in your `shift`/`unshift` functions (in most cases this is not
necessary). In some cases, using the `shift`/`unshift` functions to
change the Component's `inKey`, `outKey`, or `group` properties will be
sufficient. Refer to the source code for [\#HotcueButton](#HotcueButton)
for an example.

In more complex cases, overwriting the `input` and `output` functions
may be required. Refer to [\#SamplerButton](#SamplerButton) and
[\#EffectUnit](#EffectUnit) for examples.

For convenience, the Component constructor will automatically call the
`unshift` function if it exists. The `shift` and `unshift` functions of
[\#ComponentContainer](#ComponentContainer) will call the corresponding
function of all the Components within it that have that function defined
and will recursively descend into ComponentContainers that are
properties of the parent ComponentContainer.

To use separate `output` callback functions in shifted and unshifted
modes, the Component's `shift` and `unshift` functions need to call
`disconnect`/`connect` and `trigger`. ComponentContainer's
`shift`/`unshift` methods will not do this automatically. Generally, you
should avoid making LEDs change when a shift button is pressed. This is
distracting if the user is pressing shift to use the shifted
functionality of a different part of the controller. For layers that
stay activated after a button is released, this is not as much of an
issue.

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
  - **shiftComponent** (boolean, default false): whether the shifted
    MIDI message changes the MIDI control number (second byte) of the
    MIDI signal
  - **shiftOffset** (number, default 0): how much to shift the MIDI
    channel or control number by

To avoid having to define those properties for every Component, you can
change the properties of components.Component.prototype in your
controller's `init` function. For example:

    components.Component.prototype.shiftOffset = 3;
    components.Component.prototype.shiftChannel = true;
    components.Component.prototype.sendShifted = true;

### Syntactic sugar

Components JS provides convenient shortcuts for common situations. If
`inKey` and `outKey` are the same, you can specify `key` in the options
object for the constructor to set both `inKey` and `outKey`. For
example:

    var quantizeButton = new components.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]'
        key: 'quantize'
    });

Setting the `co` property after calling the constructor will not
automatically set `inKey` and `outKey`; you would need to do that
manually if necessary.

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

A Button is a subtype of Component for buttons/pads.

For example:

    var quantize = new components.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]',
        co: 'quantize',
    });

Button's `input` function toggles the value of `group`, `inKey` when the
button is pressed, but not when the button is released. For buttons that
toggle `inKey` when they are pressed and released, set the onlyOnPress
property to false. For example:

    var tempSlow = new components.Button({
        midi: [0x91, 0x44],
        inKey: 'rate_temp_down',
        onlyOnPress: false,
    });

Button's `output` function sends the value of the `on` property as the
third MIDI byte when outKey \> 0 and `off` when outKey \<= 0. By
default, `on` is 127 (0x7F) and `off` is 0. For buttons/pads with
multicolor LEDs, you can change the color of the LED by defining the
`on` and `off` properties to be the MIDI value to send for that state.
For example, if the LED turns red when sent a MIDI value of 127 and blue
when sent a value of 126:

    MyController.padColors = {
        red: 127,
        blue: 126
    };
    MyController.quantize = new components.Button({
        midi: [0x91, 0x01],
        group: '[Channel1]',
        co: 'quantize',
        on: MyController.padColors.red,
        off: MyController.padColors.blue,
    });

Derivative Buttons are provided for many common use cases, documented in
the subsections below. These make it easy to map those kinds of buttons
without having to worry about particularities of Mixxx's ControlObjects.
The PlayButton, SyncButton, HotcueButton, and SamplerButton objects also
provide alternate functionality for when a shift button is pressed. To
use these, you only need to specify their `midi` and `group` properties,
except for HotcueButton and SamplerButton.

By default, Button works for controllers that send MIDI messages with a
different 3rd byte of the MIDI message (value) to indicate the button
being pressed/released, with the first two bytes (status and control)
remaining the same for both press and release. If your controller sends
separate MIDI note on/off messages with a button press indicated by the
first nybble (hexadecimal digit) of the first (status) byte being 9 and
a button release by the first nybble being 8, in your script's init
function, set `component.Button.prototype.separateNoteOnOff = true;` and
map both the note on and off messages in XML to the Button object's
input property.

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
                this.setParameterIn(this.getParameterIn() - .05);
            } else if (value === 127) {
                this.setParameterIn(this.getParameterIn() + .05);
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

## ComponentContainer

A ComponentContainer is an object that contains Components as
properties. It has methods to help iterate over those Components:

  - **forEachComponent**: Iterate over all Components in this
    ComponentContainer and perform an operation on them. The operation
    is a function provided as the first argument to `forEachComponent`.
    The operation function takes each Component as its first argument.
    In the context of the operation function, `this` refers to the
    ComponentContainer. `forEachComponent` iterates recursively through
    the Components in any ComponentContainers that are properties of
    this ComponentContainer. If you do not want `forEachComponent` to
    operate recursively, pass `false` as the second argument to
    `forEachComponent`.
  - **reconnectComponents**: Disconnect and reconnect output callbacks
    for each Component. Optionally perform an operation on each
    Component between disconnecting and reconnecting the output
    callbacks. Arguments are the same as `forEachComponent`.
  - **shift**: Call each Component's `shift` method if it exists. This
    iterates recursively on any Components in ComponentContainers that
    are properties of this ComponentContainer, so there is no need to
    call `shift` on each child ComponentContainer. This function takes
    no arguments.
  - **unshift**: same as `shift`, but call each Component's `unshift`
    method
  - **applyLayer**: Activate a new layer of functionality. Layers are
    merely objects with properties to overwrite the properties of the
    Components within this ComponentContainer. Layer objects are deeply
    merged. If a new layer does not define a property for a Component,
    the Component's old property will be retained.

In the most common case, for providing alternate functionality when a
shift button is pressed, using `applyLayer` is likely overcomplicated
and may be slow. Use `shift`/`unshift` instead. `applyLayer` may be
useful for cycling through more than two alternate layers.

For example:

    someComponentContainer.applyLayer({
        someButton: { inKey: 'alternate inKey' },
        anotherButton: { outKey: 'alternate outKey' }
    });

By default, `applyLayer` disconnects old layer's output callbacks and
the new layer's output callbacks are connected. To avoid this behavior,
which would be desirable if you are not changing any output
functionality, pass `false` as the second argument to `applyLayer`.

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

To map your own controller, create a custom derivative of Deck and
create instances of your custom Deck objects in your controller's `init`
function. Use a constructor function to create all the Components you
need for your particular controller and assign your custom derivative's
prototype to components.Deck. For example:

    MyController.init = function () {
        this.leftDeck = new MyController.Deck([1, 2]);
        this.rightDeck = new MyController.Deck([2, 4]);
    };
    MyController.Deck = function (deckNumbers, midiChannel) {
        // Call the Deck constructor to setup the currentDeck and deckNumbers properties.
        components.Deck.call(this, deckNumbers);
        this.playButton = new components.PlayButton([0x90 + midiChannel, 0x01]);
        this.CueButton = new components.CueButton([0x90 + midiChannel, 0x02]);
        this.hotcueButtons = [];
        for (var i = 1; i <= 8; i++) {
            this.hotcueButtons[i] = new components.HotcueButton({
                midi: [0x90 + midiChannel, 0x10 + i],
                number: i
            });
        }
        // ... define as many other Components as necessary ...
    
        // Set the group properties of the above Components and connect their output callback functions
        // Without this, the group property for each Component would have to be specified to its
        // constructor.
        this.reconnectComponents(function (c) {
            if (c.group === undefined) {
                // 'this' inside a function passed to reconnectComponents refers to the ComponentContainer.
                c.group = this.currentDeck;
            }
        });
    };
    MyController.Deck.prototype = new components.Deck();

## EffectUnit

EffectUnit is a [\#ComponentContainer](#ComponentContainer) that
contains Components designed to be mapped to the common arrangement of 4
knobs and 4 buttons for controlling effects. If your controller's
effects section has fewer components, the EffectUnit object provided by
Components JS probably will not be very helpful. You may want to read
the source code for the library's EffectUnit to get an idea for how to
map your controller though.

3 knobs are used for controlling effect metaknobs or parameters,
depending on whether the effects' parameters are shown. The other knob
is used for the dry/wet knob of the whole chain or the superknob when
shift is pressed. 3 buttons are used for enabling effects and the other
button toggles the effect unit between hiding and showing effect
parameters. The Components provided are:

  - dryWetKnob ([\#Pot](#Pot))
  - showParametersButton ([\#Button](#Button))
  - enableButtons\[1-3\] ([\#ComponentContainer](#ComponentContainer) of
    [\#Button](#Button)s)
  - knobs\[1-3\] ([\#ComponentContainer](#ComponentContainer) of
    [\#Pot](#Pot)s)
  - enableOnChannelButtons ([\#ComponentContainer](#ComponentContainer)
    of [\#Button](#Button)s)

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
call the EffectUnit's `init` method to set up the output callbacks. For
example:

    MyController.effectUnit = new components.EffectUnit(1);
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
EffectUnit's `showParametersButton`, otherwise map that to the "Tap"
button. To use the `dryWetKnob` Pot with an encoder, replace its `input`
function with a function that can appropriately handle the signals sent
by your controller. Refer to the [\#Encoder](#Encoder) documentation for
an example.

For the shift functionality to work, the shift button of your controller
must be mapped to a function that calls the `shift`/`unshift` methods of
the EffectUnit on button press/release. If the EffectUnit is a property
of another [\#ComponentContainer](#ComponentContainer) (for example a
[\#Deck](#Deck)), calling `shift` and `unshift` on the parent
ComponentContainer will recursively call it on the EffectUnit too (just
like it will for any other ComponentContainer).
