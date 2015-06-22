***This document is a draft for a proposal that has not even begun
implementation. It probably will not be implemented for a while.***

# New control mapping design

## Design goals

  - reduce barriers to entry: the easier it is to work with, the more
    people will contribute high quality mappings
  - do not require programming skills to edit basic mappings
  - easy to program complex functions like modifiers, deck toggle
    buttons, jog wheels, and scratching even for people who have never
    programmed before
  - straightforward to edit via GUI or manually with minimal boilerplate
    code cluttering the screen
  - JSON rather than XML
  - [Mixxxcontrols](Mixxxcontrols) conveniently accessible to scripts,
    for example, getting & setting `Channel1.play.value` (or better yet,
    `this.value`) rather than `engine.getValue('[Channel1]', 'play')` &
    `engine.setValue('[Channel11]', 'play', newValue)`
  - intuitively organized code

<!-- end list -->

``` 
    *inputs and outputs for the same button/knob/slider/whatever organized together rather than separate input/output sections
    *code for various modes organized together rather than scattered across many functions
* trivial to implement modifiers, including buttons that toggle different modes or between decks
* functions for handling these signals would manipulate mapping objects rather than having a bunch of different functions each checking the values of global variables or engine states
* unite MIDI, HID, and keyboard mappings into one coherent API
* maximum flexibility
* facilitate bindings to other languages, particularly Python
* communications between scripts that don't require manipulating a Mixxx control
```

## Possible implementations

    -objects representing MIDI/HID/keyboard signals with attributes linking them to Mixxx controls
    -objects representing Mixxx controls with attributes linking them to MIDI/HID/keyboard signals

### Approach 1

``` javascript
MyController.midiMap = {
    {channel: 1, status: 0x90, control: Channel1.play}
}

Channel1.play.MyController.receive = function (velocity) {
    this.value = (velocity) ? 1 : 0 // what would be proper JS way to access Channel1.play.value?
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
    output: this.input
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

Maybe have a function that automatically transforms mapping specified by
Approach 1 into objects like those in Approach 2?
