## Summary

**Status**: This specification is **in progress**. Please feel free to
edit this page and add your comments.

This is a proposal to introduce a **module system** into the controller
script engine.

It's time to bring software engineering practices to the script system.
There are numerous practices that we could introduce to controller
scripts that would help improve the quality and reliability of
controller script -- static analysis tools, linting, versioning, tests,
and more. Due to the lack of a module system, the script engine is stuck
where the web was in the 90s. The way you include scripts is via the XML
file:

``` xml
<?xml version="1.0" encoding="utf-8"?>
<MixxxControllerPreset schemaVersion="1" mixxxVersion="1.11+">
    <info>
        <name>My Cool Controller</name>
        <author>Jane DJ</author>
    </info>
    <controller id="CoolController">
        <scriptfiles>
            <file filename="common-hid-packet-parser.js" functionprefix=""/>
            <file filename="common-hid-devices.js" functionprefix=""/>
            <file filename="Cool-Controller.js" functionprefix="CoolController"/>
        </scriptfiles>
    </controller>
</MixxxControllerPreset>
```

These scripts are loaded sequentially into the global script
environment. If one script defines a variable `foo` and the next one
loaded does the same, the first script's variable will be overwritten\!
Further, within a script there is no way to enforce that you have been
loaded after a script you depend on.

Modern Javascript development has evolved past this. Various groups
(e.g. the Node community) have developed module systems for Javascript
and standardized them into [CommonJS](http://www.commonjs.org). In ES6 a
[module system](http://www.2ality.com/2014/09/es6-modules-final.html)
was introduced into the language itself, validating the value modules
bring to the table.

## Benefits

### Declarative Dependencies

It is possible to statically analyze what files a given script file
depends on.

### No Implicit Globals

Explicitly importing a module serves double duty as giving it a binding
in the local scope. In all controller scripts, certain globals are
assumed to exist such as `engine`. Static analyzers will complain that
`engine` is an unbound variable without an explicit definition.

### Explicit Exports / Modularity / Abstraction

Modules are isolated from each other and can only make use of what is
provided from other modules via explicit exports. This promotes
abstractions and clean separations between modules.

The sprawling and disorganized common script files are an example of
what happens when you don't have a standard way to organize code.

### Testability

Once functionality is bundled into a coherent unit, it becomes easier to
write a unit test for that functionality. Having
[Jasmine](https://github.com/jasmine/jasmine) unit tests would be
awesome.

### 3rd Party Libraries

If we support a standard like CommonJS then we will be better able to
include 3rd-party libraries with Mixxx that support the CommonJS
standard.

### Versioning

Once logic is contained within a module, it will be possible to come up
with a versioning scheme. This way, we can allow scripts to depend on a
certain version of script by declaring what that version is in their
manifest somehow.

## Design

### Module Definition

Modules will be defined as per the [CommonJS 1.0
Spec](http://www.commonjs.org/specs/modules/1.0/).

### Standard Modules

We will need to define some standard modules that we provide. All global
variables that were previously defined will become modules that scripts
can `require`. For backwards compatibility, the root module will have
the usual global variables defined.

  - engine
  - controller
  - console

### Module Search Paths

### Security Considerations

### Misc

We should employ a module cache so that multiple requires of the same
module in one script engine don't double-parse the module.

## Example

### Cool Controller.xml

``` xml
<?xml version="1.0" encoding="utf-8"?>
<MixxxControllerPreset schemaVersion="1" mixxxVersion="1.11+">
    <info>
        <name>My Cool Controller</name>
        <author>Jane DJ</author>
    </info>
    <controller id="CoolController">
        <scriptfiles>
            <file filename="Cool-Controller.js" functionprefix="CoolController"/>
        </scriptfiles>
    </controller>
</MixxxControllerPreset>
```

### Cool-Controller.js

**Don't focus too hard on the code, just the module part.**

``` javascript

var HIDController = require('hid-controller');
var Engine = require('engine');
var HidPacketParser = require('common-hid-packet-parser');
var HidDevice = require('common-hid-device');
var Button = require('button');
var Knob = require('knob');

function CoolControllerDevice() { 
  this.controls = [ new Button('[Channel1]', 'hotcue_1_activate'),
                    new Knob('[Channel1]', 'pregain') ];
}

CoolControllerDevice.prototype.onKnobUpdate = function(knob, parameter) {
  Engine.setParameter(knob.getGroup(), knob.getKey(), parameter); 
}

// Inherit from HIDController.
CoolControllerDevice.prototype = Object.create(HIDController.prototype);
CoolControllerDevice.prototype.constructor = CoolControllerDevice;

var CoolController = new CoolControllerDevice();
```

### knob.js

``` javascript

var AbstractControl = require('abstract-control');

function Knob(group, key) {
  // Call parent constructor. 
  // Let's say AbstractControl defines getGroup and getKey.
  AbstractControl.call(group, key);
}
Knob.prototype = Object.create(AbstractControl.prototype);
Knob.prototype.constructor = Knob;

exports = Knob;
```

## Work Breakdown

## Current Progress

  - rryan has a WIP implementation of `require` working.

## Team

## Questions

  - Won't this further increase the barrier to entry for would-be
    controller script writers? Not saying that should stop us, I just
    want to assess the impact. (Sean)
