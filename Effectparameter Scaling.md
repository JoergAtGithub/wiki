On This page we collect all issue and ideas about Scaling of Effect
Parameter.

# Controls

## Hardware Solutions

#### Stomp Boxes / DJ Mixer

  - Rotary Potentiometer 
  - Slider Potentiometer 
  - Rotary Step Switch
  - Rocker Switch (2 or 3 steps) 
  - Slider Switch
  - Pushbuttons 

#### DJ Consoles

  - Rotary Knobs with Midi or higher resolution 
  - Endless Rotary Knobs (Up/Down commands)
  - LED Row for Feedback 
  - Pushbuttons 

## Parameter Examples

  - Gain
  - Center/Cut-off Frequency 
  - Mode Switch 
  - Periods 
  - Bits 
  - Rate 

## Desired Scales / Behaviors

  - Linear 
  - Logarithmic
  - Audio-Taper
  - Steps
  - Split Scale 
  - Pushbutton 
  - Togglebutton 
  - Latching button 
  - Powerwindow button

# Requirements

  - Value Feedback including units 
  - Control a quantization Value with a continuous Knob 
  - \* Feedback of the Snapped value 
  - Controllable by Super knob 

# LV2

<http://lv2plug.in/ns/lv2core/>

Parameters are "Class lv2:ControlPort" they have a value of c type
float.

Example of a ControlPort:

    [
      a lv2:ControlPort, lv2:InputPort;
      lv2:index 1;
      lv2:symbol "balance";
      lv2:name "Balance";
      lv2:minimum -1;
      lv2:maximum 1;
      lv2:default 0;
      lv2:scalePoint [ rdfs:label "Left"; rdf:value -1 ];
      lv2:scalePoint [ rdfs:label "Right"; rdf:value 1 ];
    ],

Additions for Mode Switches:

lv2:enumeration

" Indicates that a port's only reasonable values are the scale points
defined for that port. A host SHOULD NOT allow a user to set the value
of such a port to anything other than a scale point. However, a plugin
MUST operate reasonably even if such a port has an input that is not a
scale point, preferably by simply choosing the largest enumeration value
less than or equal to the actual input value (i.e. round the input value
down). "

    lv2:integer

" Indicates that a port's reasonable values are integers (eg. a user
interface would likely wish to provide a stepped control allowing only
integer input). A plugin MUST operate reasonably even if such a port has
a non-integer input. "

    lv2:toggled

" Indicates that the data item should be considered a Boolean toggle.
Data less than or equal to zero should be considered "off" or "false",
and data above zero should be considered "on" or "true". "

    lv2:sampleRate

" Indicates that any bounds specified should be interpreted as multiples
of the sample rate. For instance, a frequency range from 0Hz to the
Nyquist frequency (half the sample rate) could be requested by this
property in conjunction with lv2:minimum 0.0 and lv2:maximum 0.5. Hosts
that support bounds at all MUST support this property. "

# VST

# Mixxx
