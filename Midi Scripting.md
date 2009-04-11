# MIDI Scripting

***This information may change prior to release.***

In order to support the advanced features of many MIDI controllers,
Mixxx offers what we call MIDI Scripting. It enables MIDI controls to be
mapped to [QtScript](http://doc.trolltech.com/4.3/qtscript.html) (aka
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

## Script functions

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

### Function definitions

**This API has changed as of 10 April 2009**

  - "Device" has been removed
  - "Category" has become "Status"
  - The .init function now requires acceptance of an ID string parameter
    (but you don't have to do anything with it.)

Data passed to functions are, in order: MIDI channel, control/note,
value, and MIDI status (Note (0x9\#), Control Change (0xB\#), etc.)
Therefore, function definitions should look like:

``` javascript
ControllerName.functionName = function (channel, control, value, status) {
    ...
}
```

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

Tying it all together, here is an example of a function that reduces the
sensitivity of the SCS.3d's pitch slider (in relative mode:)

``` javascript
StantonSCS3d.pitchSlider = function (channel, control, value, status) {   // Lower the sensitivity of the pitch slider
    var currentValue = engine.getValue("[Channel"+StantonSCS3d.deck+"]","rate");
    engine.setValue("[Channel"+StantonSCS3d.deck+"]","rate",currentValue+(value-64)/128);
}
```

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

### Init and Shutdown functions

All device script files are expected to contain initialize and shutdown
functions (called \<manufacturer\>\<device\>.init(ID) and
\<manufacturer\>\<device\>.shutdown() ) which will be called when Mixxx
opens and closes the device, respectively. They can be empty, but are
useful for putting controllers into known states and/or lighting certain
LEDs before operation begins or the program exits. The ID parameter is
the `controller id` attribute from the XML file and is useful for
identifying the particular controller instance in print statements.

### Available common functions

Here is a list of functions available to you from the always-loaded
midi-mappings-scripts.js file:

  - **nop**() - Does nothing (No OPeration.) Empty function you can use
    as a place-holder while developing to avoid errors.
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

<!-- end list -->

  - **scratch.enable**(currentDeck) - Initializes the variables and
    turns on scratching for the functions detailed below. Just give it
    the number of the deck you want to scratch.
  - **scratch.disable**(currentDeck) - Disables scratching for the
    specified deck.
  - **scratch.slider**(currentDeck, sliderValue, revtime, alpha, beta) -
    Allows you to scratch with a slider or a knob (values 0..127.)
    0-\>127 is the forward track direction. Call this each time there's
    a new control value.
  - Inputs:

<!-- end list -->

``` 
    * The number of the deck you want to scratch (same as above)
    * The new value of the slider/knob
    * Revolution time of the imaginary record (typically 1.8s for a 12-inch record at 33 & 1/3 RPM, adjust for comfort)
    * Coefficients for the filter. Alpha isn't currently used at all, but it needs to be set to something, so just use 0.1.
    * Beta adjusts how quickly Mixxx responds to your motions. The value should be between 0 and 1, though I find that 0.9-1 works well.
* Output: A new value for Mixxx's "scratch" control. Simply call engine.setValue("[Channel"+currentDeck+"]", "scratch", <returned value here>); in your function.
* **scratch.wheel**(currentDeck, wheelValue, revtime, alpha, beta) - Same thing but for a rotary control that wraps from 127 to 0 (or 0 to 127 depending on the direction.)
```

-----

# MIDI Mapping Object Design Spec

*\*\*Note this block is dedicated to the internal workings of MIDI
Mapping object and dlgprefsmidibindings -- it will not be of interest to
end users \*\**

**NOTE:** It is probably a good idea to do [deep
copies](http://en.wikipedia.org/wiki/Object_copy#Deep_copy) whenever
passing TBAMidiControlObjectType objects between MIDI Mapping and
dlgpref\*, it will be MIDI Mapping's responsibility to create these
copies (since they are for its own protection).

**TODO:** handle LED output mappings.

**TODO:** replace TBAMidiControlObjectType with whatever
data-type/class/struct should be used here.

### Use Cases

  - Auto load Mapping from XML file on start-up

Mixxx Constructor: configkey with mapping name will be read on start,
loadMapFile(configkey) will be called if the configkey is
non-null/non-empty. Apply Mapping will be called if loadMapFile
succeeded.

  - Load Mapping from XML file

dlgprefs will call loadMapFile with the file name obtained from the load
QDialog. MIDI Mapping will open that file and return true on
successfully loading that into a model. (Do we need to create a new MIDI
Mapping object each load or get it from Mixxx object?)

  - User Edit Mapping

dlgprefs will call MIDI Mapping, obtain a copy of the model (MIDI
Mapping - lock/copy/unlock), render the copied model as a table (using
key as a hidden field) -\> done on open of dlg call validateBinding each
time user edits.

  - User Clear Mappings

a copied model will exist in dlg from open dlgprefs will clear it's
copied model's contents -\> then this becomes the same as editing,
calling edit with each new addition

  - Apply Mapping

dlgprefs sends the replacement copied model back to MIDI Mapping, which
must clear all old TBAMidiControlObjectType objects and create all new
TBAMidiControlObjectType from the new returned copied model (MIDI
Mapping - lock/delete/create/unlock).

  - Save Mapping to file

dlgprefs will call saveMapFile with the file name obtained from the save
QDialog, MIDI Mapping will save to that file and return true on
successfully save.

  - Auto save mapping to file on shutdown

dlgprefs will have to be destroyed ahead of MIDI Mapping Object.
dlgprefs destructor will call saveMappingFile("\~/.MixxxMIDIBindings");
if dlgprefs is dirty -\> dlgprefs destructor set the config to load on
next start as "\~/.MixxxMIDIBindings". If dlgprefs is never created,
then user never edited anything so we don't care.

### MIDI Mapping API

##### File Ops access

  - `bool loadMapFile(QString fromFileName)`

true succeeded

  - `bool saveMapFile(QString asFileName)`

true succeeded

##### Model-based access

  - `QList<TBAMidiControlObjectType> getMappingModel()`
  - `void setMappingModel(QList<TBAMidiControlObjectType>
    newMappingModel)`
  - `bool ApplyMapping()`

true if MIDI Mapping object succeeded in applying the loaded or set
model, false Mapping has errors -\> dlgpref should iterate through model
validating each binding and report if one has an error.

##### Binding-based access

  - `bool validateBinding(TBAMidiControlObjectType
    tBAMidiControlObject)`

have Midi Mapping say whether this would be bindable or not, but don't
actually bind it. Having this does not guarantee that only valid objects
will be in the model.

##### DO NOT USE: Binding-based access --- thought about, but not useful

  - `// QString/key createbinding(TBAMidiControlObjectType
    objectToBeCopiedandBound)`

returns null if failed, else returns key string

  - `// bool updateBinding(QString key, TBAMidiControlObjectType
    objectToBeCopiedandBound)`

true mapping was valid + successfully mapped

  - `// void deleteBinding(QString key)`

caller doesn't care about result
