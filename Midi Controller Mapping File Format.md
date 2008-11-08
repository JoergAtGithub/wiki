# MIDI Controller Mapping File Format

## Introduction

Support for extra MIDI devices can be added to Mixxx by created a new
"MIDI mapping" file. This mapping file tells Mixxx how to translate MIDI
commands from a controller into commands that Mixxx will understand.

The MIDI mapping files are located in the following paths:

  - Windows: C:Program FilesMixxxmidi
  - Linux: /usr/share/mixxx/midi (or /usr/local/share/mixxx/midi)
  - OS X: /Applications/Mixxx.app/Contents/midi

The easiest way to create a new MIDI mapping is by modifying an existing
one. When you've finished creating your MIDI mapping, **please send it
to us** and we'll include it in Mixxx.

## File Format

The midi mapping format is xml based. It looks something like this:

\<\!DOCTYPE controller\> \<controller\>

``` 
 <controls>
   <control>
     <group>[[Master]]</group>
     <key>crossfader</key>
     <miditype>Ctrl</miditype>
     <midino>0x31</midino>
     <options>
       <hercjog/>
     </options>
   </control>
   ...
 </controls>
 <lights>
   <light>
     <group>[[Channel1]]</group>
     <key>VuMeter</key>
     <status>0xB0</status>
     <midino>0x16</midino>
     <threshold>0.5</threshold>
   </light>
   ...
 </lights>
```

\</controller\>

Definitions of the elements:

  - group - The controlobject group
  - key - The controlobject key, a list of which can be found on the
    [UI/MIDI Controls and Names](ui_midi_controls_and_names) page.
  - miditype - Midi object type: Ctrl, Key or Pitch
  - midino - The MIDI control or note number
  - midichan - The MIDI channel
  - options - Can only handle one element currently but expandable,
    these aren't well described here: *(Then where?)*
  - invert
  - rot64inv
  - rot64fast
  - rot64
  - diff - Add the value to the control's current value
  - button - a button has a *Down* (non-zero) and an *Up* (zero) state,
    these occur together when pressed/released, this switch only
    triggers on the *Down*, *Up* is ignored. (Herc)
  - switch - a switch has a *On* (non-zero) and an *Off* (zero) state,
    these occur separately. (Herc)
  - hercjog - Handle hercules jog wheels
  - spread64 - Exponential spread either side of 64, aka "relative"
    controller (NEW)
  - status - Status code to send to control lights
  - threshold - Turn on light when control exceeds this value

## Future

Expanding the options tag should be done by changing the
configobjectmidi structure to hold the QDomNode related to the options
element. This can then be parsed when a value is received and used to
modify the incoming value. If this is too slow it can be compiled in
some way but i'd be surprised.
