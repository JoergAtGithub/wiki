# MIDI Extension Proposal 2008-11-23 (Draft)

To enable support for newer state based MIDI controllers (i.e.
controllers which dynamically remap buttons by hitting certain mode
buttons) the Mixxx MIDI mappings specs will need to be extended.

The extensions will enable controls to be mapped to QtScript (aka
Javascript/EMCAScript) functions stored in a functions library file.

Scope of required changes:

1.  Changes to the current and new MIDI mapping file formats
2.  Additional script option MIDI event type handlers (configobject.cpp
    midiobject.cpp)
3.  A script file loaded at start-up that contains a library of
    functions, add all those functions will need to be parsed and made
    available to midi learning.
4.  Interface definition for arguments passed to mapped script methods
    (to include the raw MIDI event details, which channel, and any
    options associated with the mapping)

## Example of Hercules Mk2 FX/Cue/Loop mode switch button

[[/media/hercules_mk2_top_face.png|]] For the purposes of this document we
will use the Hercules Mk2 controller to illustrate how these changes
would be configured. The Mk2 is a simple controller that features a
FX/Cue/Loop Mode selector button (see area 3, selector is triangle
shaped), and 3 trigger buttons numbered 1, 2, and 3 respectively (also
part of area 3).

## Old -\> New Mapping

### XML

Currently, Mixxx does not support modes, so the function of the mode
selector button is mapped to reverse. The new mapping would change that
to call a javascript function, the function would be designated by a
"\<script-binding/\>" option tag. Similarly the mappings for the buttons
would be changed from their current mappings to call the second script
method, though that is not shown in the snippets here. (mapping for
Tom's branch is at the bottom)

Old mapping to reverse:

``` xml
        <control>
            <group>[Channel1]</group>
            <key>reverse</key>
            <miditype>Ctrl</miditype>
            <midino>0x07</midino>
            <options>
                <switch/>
            </options>
        </control>
```

New mapping to mode selection:

``` xml
        <control>
            <group>[Channel1]</group>
            <key>HerculesMk2.fx_cue_loop_mode</key> <!-- changed -->
            <miditype>Ctrl</miditype>
            <midino>0x07</midino>
            <options>
                <script-binding/> <!-- changed -->
            </options>
        </control>

```

### QtScript Function

When a midi event arrives in controlobject/midiobject the \<script/\>
tag triggers an evaluation of the functions stored in the library. Here
is an example implementation of the library which shows the basics of
managing the controller's state. The implementation isn't complete as
the callbacks to control objects to trigger the various button actions
or set the LED values are only comments or stubs to alert().

(Note: you'll need to compile Mixxx with option script=1 to enable
QtScript parsing.)

``` javascript
function HerculesMk2() {}
HerculesMk2.mode_store = { "[Channel1]":0, "[Channel2]":0 };
HerculesMk2.fx_button_map = { 13:3, 14:2, 15:1, 16:1, 17:2, 18:3 };
HerculesMk2.mode_def = { "[Channel1]": { "min":15, "inc":-1, "max":13 } , "[Channel2]": { "min":16, "inc":1, "max":18 } };
HerculesMk2.modes = { 13:"loop", 14:"cue", 15:"fx", 16:"fx", 17:"cue", 18:"loop" };

HerculesMk2.fx_cue_loop_mode = function (msg) {
        if (msg.midino.value == 0) return; // ignore button up
        var ch = msg.channel;
        var B0 = 176; // Hex MIDI code for Hercules Mk2 LED output
        var mode = HerculesMk2.mode_store[msg.channel];
        if (mode != 0) {
            midi.send(B0, mode, 0) // clear previous LED status
        }
        if (mode == HerculesMk2.mode_def[msg.channel]["min"] || mode == HerculesMk2.mode_def[msg.channel]["min"] + HerculesMk2.mode_def[msg.channel]["inc"]) { // In one of the first two modes
            mode = mode + HerculesMk2.mode_def[msg.channel]["inc"];
        } else { // either uninitialized (mode == 0) or in the final mode and need to roll back to first mode.
            mode = HerculesMk2.mode_def[msg.channel]["min"];
        }
        HerculesMk2.mode_store[msg.channel] = mode;
        midi.send(B0, mode, 127) // set new LED status
    }
    
HerculesMk2.fx_cue_loop_button = function (msg) {
        if (msg.midino.value == 0) return; // ignore button up
        var mode = HerculesMk2.mode_store[msg.channel];
        if (mode == 0) { HerculesMk2.fx_cue_loop_mode(msg); mode = HerculesMk2.mode_store[msg.channel]; }
        var trigger_no = HerculesMk2.fx_button_map[msg.midino];
        switch (HerculesMk2.modes[mode]) {
            case "fx": /* trigger trigger_no on/off toggle event for fx on msg.channel */ ; break;
            case "cue": /* seek trigger_no cue point on msg.channel */; break;
            case "loop": /* trigger_no 1 to loop in/out, 2/3 to lengthen/shorten loop */ ; break;
        }
        alert(msg.channel + " " + HerculesMk2.modes[mode] + " button #" + trigger_no + " hit.");
    }
```

### QtScript Test

Test code, which cycles through the buttons modes and triggers a few
button events.

``` javascript
// --- Test stuff below
function midi(){
}
midi.send = function (status, midino, value) {
       alert("midi.send - status: " + status + " midino: "+ midino + " value: " + value);
}

function msg(){
}
msg.channel = "[Channel1]";
msg.midino = 13;
msg.value = 127; // button down

function msg2(){
}
msg2.channel = "[Channel2]";
msg2.midino = 17;
msg2.value = 127; // button down

HerculesMk2.fx_cue_loop_mode(msg);
HerculesMk2.fx_cue_loop_button(msg);
HerculesMk2.fx_cue_loop_mode(msg2);
HerculesMk2.fx_cue_loop_button(msg2);
HerculesMk2.fx_cue_loop_mode(msg);
HerculesMk2.fx_cue_loop_button(msg);
HerculesMk2.fx_cue_loop_mode(msg);
HerculesMk2.fx_cue_loop_button(msg);
HerculesMk2.fx_cue_loop_mode(msg);
HerculesMk2.fx_cue_loop_button(msg);
HerculesMk2.fx_cue_loop_mode(msg2);
HerculesMk2.fx_cue_loop_button(msg2);
```

### Loading / Executing library of functions

Library should be called something descriptive like
'midi-mappings-scripts.js' (.js so editors highlight properly).

Steps to loading:

1.  read file 'midi-mappings-scripts.js' into a QString (refered to from
    here on as scriptFile)
2.  parse all lines matching mappable function signatures into a
    QStringList (refered to from here on as functionsMap). Pure regex
    equivalent of this: `grep 'function' midi-mappings-scripts.js|grep
    -i '(msg)'|sed -e 's/function \(.*\)(msg).*/\1/i' -e 's//[= ]//g'`
    should just about do it.
3.  Load mapping file, verify that all \<script-binding/\> references
    are present in functionsMap, else pop-up an error message indicating
    unmapped option. (don't assert, otherwise app dies and it will be
    impossible to correct inside the learning prefs screen).
4.  QtScriptEngine works by accepting a string argument. Pass
    scriptFile, check can evaluate -\> false throw a pop-up indicating a
    scripting error... 
5.  Whenever a mapping with a \<script-binding/\> option is triggered,
    evaluate that method in the QtScript, passing in the msg (w/ with
    channel data and data from raw midi event that triggered it).

Phase 2: a \<script\> block will be added to the XML to hold controller
specific QtScript functions. There are considerations such as function
name collisions and remapping to consider, global functions generic to
all controllers will still be loaded from the mid-mapping-script.js file
as well.

### Tom's branch midi mapping

Old mapping to reverse:

``` xml
                <control>
                    <group>[Channel1]</group>
                    <key>reverse</key>
                    <miditype>Ctrl</miditype>
                    <midino>7</midino>
                    <midichan>1</midichan>
                    <controltype>button</controltype>
                    <options>
                        <button/>
                    </options>
                </control>
```

New mapping to mode selection ??:

``` xml
                <control>
                    <group>[Channel1]</group>
                    <key>HerculesMk2.fx_cue_loop_mode</key> <!-- changed -->
                    <miditype>Ctrl</miditype>
                    <midino>7</midino>
                    <midichan>1</midichan>
                    <controltype>script-binding</controltype> <!-- changed -->
                    <options>
<!--
                        <button/>
-->
                    </options>
                </control>
```
