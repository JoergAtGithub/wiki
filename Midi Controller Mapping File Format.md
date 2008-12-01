# MIDI Controller Mapping File Format

## Introduction

Support for extra MIDI devices can be added to Mixxx by created a new
"MIDI mapping" file. This mapping file tells Mixxx how to translate MIDI
commands from a controller into commands that Mixxx will understand.

The MIDI mapping files are located in the following paths:

  - Windows: C:\\Program Files\\Mixxx\\midi
  - Linux: /usr/share/mixxx/midi (or /usr/local/share/mixxx/midi)
  - OS X: /Applications/Mixxx.app/Contents/midi

The easiest way to create a new MIDI mapping is by modifying an existing
one. When you've finished creating your MIDI mapping, **please send it
to us** and we'll include it in Mixxx.

## File Format

Mixxx uses a well defined XML format to store its MIDI mappings. The
format is used for storing and distributing MIDI mappings from multiple
scopes.

\<?xml version="1.0" encoding="utf-8"?\>

``` 
  <MixxxMIDIPreset version="1.6.2"> <!-- Version number to help compatibility, should the MIDI format change -->
  <info><!-- Optional - information about the preset file -->
      <name>Example MIDI Preset for Mixxx</name>
      <author>Tom Care</author>
      <description>This is an example XML MIDI preset for Mixxx. The scope of the preset could be from a small functionality addition, to a complete mapping for a controller, to a complex personal setup with multiple controllers. This description is intended for distribution and could include comments about the extent of the functionality.</description>
  </info>
  
```

The first part of the file defines the version of the mapping (for
future compatibility, as the Mixxx MIDI abilities become more complex)
and an optional info tag which contains information about the preset
(primarily used for distribution of presets).

``` 
  <controller id="Device name of the controller" port="Port"> <!-- Many controllers in one file supported. A controller should only appear once -->
  
```

The core part of the file contains a definition for a single controller.
There may be multiple controllers in one file (for more complex setups).
Each controller definition contains two sections: input bindings
(controls) and output bindings (only lights are supported at the
moment).

``` 
      <controls> <!-- One control group -->
          <control> <!-- Several controls -->
              <group>[Master]</group>
              <key>crossfader</key>
              
```

Group and key define the part of Mixxx that is being controlled. For a
list of what these values can be, [see
below](midi_controller_mapping_file_format#ui_midi_controls_and_names).

``` 
              <miditype>Ctrl</miditype>
              <midino>7</midino>
              <midichan>3</midichan>
              <controltype>fader</controltype>
              
```

These tags define the MIDI event that Mixxx will listen for. Controltype
hints to Mixxx what kind of control this is: for most controls this will
define the behaviour of the control (eg jog wheel, analog knob). There
is also a generic control enabling someone to define the behaviour using
options.

``` 
              <options>
                  <!-- all control specific options should go here - sensitivity etc. Specifics to be decided by spec -->
              </options>
              
```

The options further refine be behaviour of the control. The list of
options will expand as Mixxx development continues. Eg - translations,
sensitivity, acceleration. Necessary options (defined by controltype)
will have default values, eg a jogwheel might have no acceleration by
default.

``` 
          </control>
      </controls>
      <outputs>
      
```

The next section defines the outputs (lights only at the moment).

``` 
          <light>
              <group>[Channel1]</group>
              <key>play</key>
              <status>0x7F</status>
              <midino>0x08</midino>
              <threshold>0.1</threshold>
              
```

Status is the value sent to the MIDI controller. Threshold is the value
at which the light turns on.

``` 
          </light>
      </outputs>
  </controller>
```

\</MixxxMIDIPreset\>

### Definitions of the elements:

    These define the part of Mixxx that is being controlled:

  - group - The controlobject group
  - key - The controlobject key, a list of which can be found
    [below](midi_controller_mapping_file_format#ui_midi_controls_and_names).

<!-- end list -->

    These tags define the MIDI event that Mixxx will listen for:

  - miditype - Midi object type: Ctrl, Key or Pitch
  - midino - The MIDI control or note number
  - midichan - The MIDI channel
  - controltype - Hint to Mixxx what kind of control this is. Possible
    values: knob, wheel, fader, button. For most controls this will
    define the behaviour of the control (eg jog wheel, analog knob).
    There is also a generic control enabling someone to define the
    behaviour using options.
  - options - Further refine the behaviour of the control (e.g.
    translations, sensitivity, acceleration) Necessary options (defined
    by controltype) will have default values, eg a jogwheel might have
    no acceleration by default. Can only handle one element currently
    but expandable, these aren't well described here: *(Then where?)*
  - Invert
  - Rot64inv
  - Rot64fast
  - Rot64
  - Diff - Add the value to the control's current value
  - Button - a button has a *Down* (non-zero) and an *Up* (zero) state,
    these occur together when pressed/released, this switch only
    triggers on the *Down*, *Up* is ignored. (Herc)
  - Switch - a switch has a *On* (non-zero) and an *Off* (zero) state,
    these occur separately. (Herc)
  - Hercjog - Handle hercules jog wheels
  - Spread64 - Exponential spread either side of 64, aka "relative"
    controller
  - status - Status code to send to control lights (e.g. Note on (0x9x),
    Control Change (0xBx))
  - threshold - Turn on light when control exceeds this value

### Old format (pre-1.6.5)

The old midi mapping format is here for reference. It looks something
like this:

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

# UI/MIDI Controls and Names

Each control inside Mixxx is identified by a unique string. These
strings are used in the keyboard mappings, the MIDI mappings, and inside
Mixxx to gain access to the controls. The following is a list of
controls that can be used in any of the above contexts.

## List of Controls

The default range is 0.0 to 1.0, unless otherwise noted.

\[Master\]

  - crossfader: min = -1.0, max = 1.0
  - samplerate

\[ChannelN\] (where N is a number 1 or 2)

  - play
  - cue\_default
  - cue\_simple
  - cue\_cdj
  - volume
  - pregain
  - pfl
  - flanger
  - temporalShapeRate (?)
  - temporalPhaseRate (?)
  - wheel
  - scratch
  - beatsync
  - rate
  - rate\_perm\_down
  - rate\_perm\_up
  - rate\_temp\_down: off = 0.0, on = 1.0
  - rate\_temp\_up: off = 0.0, on = 1.0
  - reverse
  - back: off = 0.0, on = 1.0
  - fwd: off = 0.0, on = 1.0
  - filterLowKill
  - filterMidKill
  - filterHighKill
  - NextTrack
  - PrevTrack
  - playposition
  - LoadSelectedTrack - loads selected track from the
    playlist/tracktable.

\[Playlist\]

  - SelectNextTrack - scrolls to the next track in the
    playlist/tracktable.
  - SelectPrevTrack - scrolls to the previous track in the
    playlist/tracktable.

Note: This is an incomplete list. There are a ton of these controls
mapped inside Mixxx.

The full list can be generated by running the following script in your
mixxx/src directory:

\======

    #!/bin/sh
    # set -x
    IFS='
    '
    last_control=
    
    for ck in `grep ConfigKey *.cpp | sed -e 's/ConfigKey(group/ConfigKey("[Master]"/g' | grep 'ConfigKey("' | grep -v "Channel2" | sed -e 's/.*ConfigKey(//g' -e 's/, */,/g' | cut -d\) -f1 | sed -e 's/\[Channel1\]/\[ChannelN\] (where N is a number 1 or 2)/g' | sort -fu`; do
      control=`echo $ck|cut -d\" -f2`
      if [ "$control" != "$last_control" ]; then
        echo
        echo $control
        last_control=$control
      fi
      key=`echo $ck|cut -d\" -f4`
      if [ ! -z "${key}" ]; then echo "* ${key}"; fi
    done

## Using Controls Inside Mixxx (for developers)

If you want to access one of these controls inside Mixxx, you can do so
with something like this:

``` 
 ControlObjectThreadMain* controlRightPitch = new ControlObjectThreadMain(ControlObject::getControl(ConfigKey("[[Channel2]]", "rate")));
```

That line will give you a ControlObject which allows you to read and
control the pitch of the right channel in Mixxx. For example, to
increase the pitch of the track in the right channel, one could do
something like this:

``` 
 float fRightPitch = controlRightPitch->get();
 controlRightPitch->slotSet(fRightPitch + 0.10);
```

This would increase the pitch of the right channel inside Mixxx, and the
GUI controls would automatically reflect this change. Access to
ControlObjects is also thread-safe when used this way.

**Important note:** Different types of ControlObject wrappers must be
used depending on what thread your code is running in. This example
assumes the code will run in the GUI (ie. main) thread. The
ControlObjects wrappers should be used as follows:

  - **ControlObjectThreadMain** - GUI (main) thread
  - **ControlObject** - The audio callback thread (most audio processing
    happens here)
  - **ControlObjectThread** - Other threads
