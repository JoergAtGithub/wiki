***This document is a draft for a proposal that has not even begun
implementation. It probably will not be implemented for a while.***

# New control mapping design

## Design goals

  - reduce barriers to entry: the easier it is to work with, the more
    people will contribute high quality mappings. This by itself could
    grow community. Hopefully, when Mixxx is compatible with a broader
    range of more common hardware, this will further attract users &
    developers and lead to overall improvement of Mixxx.
  - do not require programming skills to edit basic mappings
  - easy to program complex functions even for people who have never
    programmed before. Complex functions include but are not limited to:
    modifiers, deck toggle buttons, jog wheels, scratching, sending
    output in response to changes in Mixxx, and soft takeover with
    customized thresholds
  - no dichotomy of simple mapping vs scripted mapping. Functionality
    currently specified by \<option\> tags would be provided by
    prototype send/receive (or input/output) functions that could be
    overridden by scripts. 
  - straightforward to edit via GUI or manually with minimal boilerplate
    code cluttering the screen
  - [JSON rather than XML](http://www.json.org/xml.html)
  - [Mixxxcontrols](Mixxxcontrols) conveniently accessible to scripts,
    for example, getting & setting `Channel1.play.value` (or better yet,
    `this.value`) rather than `engine.getValue('[Channel1]', 'play')` &
    `engine.setValue('[Channel11]', 'play', newValue)`
  - intuitively organized code

<!-- end list -->

``` 
    *inputs and outputs for the same button/knob/slider/whatever organized together rather than separate input/output sections
    *code for various modes toggled by modifiers organized together rather than scattered across many functions
      *functions for handling these signals would manipulate mapping objects rather than having a bunch of different functions each checking the values of global variables or engine states
* unite MIDI, HID, and keyboard mappings into one coherent API
* This could facilitate adding support for other kinds of signals like [[OSC backend|OSC]] and generic Linux input events for [[https://bugs.launchpad.net/mixxx/+bug/1432442|old Native Instuments Traktor controllers]] and whatever else the future brings (touchscreens?)
* maximum flexibility
* facilitate bindings to other languages, particularly Python
* JSON is good for this
* Could Python be the primary scripting language?
* Python-Qt bindings: [[http://pythonqt.sourceforge.net|PythonQt]], [[http://www.riverbankcomputing.com/software/pyqt/intro|PyQt]], [[https://wiki.qt.io/PySide|PySide]]
* communications between scripts that don't require manipulating a Mixxx control
* Scripts could manipulate the mappings of other devices. For example, if a MIDI controller has one less button than a mapper would like, they could map a keyboard button press to toggle between layers on the MIDI controller.
* performance better than or equal to current XML/JS format
```

## Possible implementations

    -objects representing MIDI/HID/keyboard signals with attributes linking them to Mixxx controls
    -objects representing Mixxx controls with attributes linking them to MIDI/HID/keyboard signals

Maybe have a prototype function that automatically transforms mapping
specified by Approach 1 into objects like those in Approach 2? This
could allow scripts to override the default function.

### Approach 1

``` javascript
MyController.midiMap = {
    {channel: 1, status: 0x90, control: Channel1.play, type: 'button'}
}

// The below would not need to be explicitly specified by the mapping; it would be the default MIDI receive behavior for all objects with a type attribute equal to 'button'.
Channel1.play.MyController.receive = function (velocity) {
    if (velocity) {
        this.value = ! this.value // what would be proper JS way to access Channel1.play.value?
    }
}
```

  - more similar to current XML approach
  - probably easier to adapt existing scripts to (or they might not need
    any adaptation)

### Approach 2

``` javascript
Channel1.play = { midi: { input: { MyController: {channel: 1, status, 0x90} }, output: this.input } }
// Also could be written as:
Channel1.play = {
    input:
        midi: {
            MyController: {
                channel: 1,
                status: 0x90
            }
        },
    output: this.input // Send output with same channel & status with value determined by return value of the send method below
}

Object.defineProperties(Channel1.play.output.midi.MyController, {
    get send () {
        if (this.value) { // What would be proper JS to reference Channel1.play.value here?
            return colorCode['green']
        }
        return colorCode['red']
    }
})
```

  - inputs and outputs organized together

### Approach 3

What about a DSL, and some decoupling? User would need to learn the
order of arguments for a handful of functions; which would be a very
small cost to pay compared to having to learn their names then type them
out every time. Being compact conceptually as well as visually, this
design is easy to figure out on a basic level even without having to
reach for the docs. Obligatory shout out to [Eric S.
Raymond](http://catb.org/~esr/writings/taoup/html/).

Off the top of my head, here's what the user would write:

``` javascript
Channels[1].controls = [
  MIDI.button([1, 1], 'mixer.kill.hi',  1, 'toggle'),
  MIDI.button([1, 2], 'mixer.kill.mid', 1, 'toggle'),
  MIDI.button([1, 3], 'mixer.kill.lo',  1, 'toggle'),
  
  MIDI.linear([1, 16], 'mixer.eq.hi'),
  MIDI.linear([1, 17], 'mixer.eq.mid'),
  MIDI.linear([1, 18], 'mixer.eq.lo'),
  
  MIDI.encoder( ... ),
  
  OSC.handler('/address/foo', function (...) { ... }),
  
  HID.handler( ... )
];
```

And Mixxx would in turn provide pre-defined controls (buttons, pots,
encoders, jog wheels, etc) and actions (EQ tweak/kill, FX parameter
tweak, scrub, loop, etc etc).

``` javascript
Events = new EventEmitter();
Events.on('mixer.kill.hi', function (channel, value) {
  if (value === 'toggle') {
    Channels[channel].hiKill = !Channels[channel].hiKill;
  } else if (value === true || value === false) {
    Channels[channel].hiKill = value
  } else {
    // throw error?
  }
});

MIDI = {
  button: function (mask, event /* + optional arg1, arg2 ... argN */) {
    var args = [].slice.call(arguments, 2); // gets list of optional arguments
    return function buttonPressed (midiMessage) {
      if (midiMessage.matches(mask)) {
        Events.emit.apply(Events, [event].concat(args))
        // that was a fancy way of saying `Events.emit(event, arg1, arg2 ... argN)`+
      }
    }
  },
  linear: function (mask, event) {
    var args = [].slice.call(arguments, 2); // gets list of optional arguments
    return function potRotated (midiMessage) {
      if (midiMessage.matches(mask)) {
        Events.emit.apply(Events, [event].concat(args).concat([midiMessage.data2]));
      }
    }
  }
}

// at the top of the chain sits a function which
// simply runs every received MIDI message through
// every registered MIDI handler.
Events.on('midi.input', function (midiMessage) {
  Channel1.controls.map(function (control) { control(midiMessage); });
});
```

Event names can be parameterized too (have one event handler for
\`mixer.kill.\*\` and dispatch on event name), see
<https://github.com/asyncly/EventEmitter2> for one nice implementation.
