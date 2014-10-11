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

VST uses C Float parameter.

They work on the float range of 0.0f to 1.0f for the value of the
parameter. Required scaling should be done inside the PlugIn

    /* this struct taken from http://asseca.com/vst-24-specs/efGetParameterProperties.html */
    struct _VstParameterProperties
    {
       float stepFloat;
       float smallStepFloat;
       float largeStepFloat;
       char label[64];
       int32_t flags;
       int32_t minInteger;
       int32_t maxInteger;
       int32_t stepInteger;
       int32_t largeStepInteger;
       char shortLabel[8];
    };

    /* this enum taken from http://asseca.com/vst-24-specs/efGetParameterProperties.html */
    enum VstParameterFlags
    {
      kVstParameterIsSwitch = 1 << 0, /* parameter is a switch (on/off) */
      kVstParameterUsesIntegerMinMax = 1 << 1, /* minInteger, maxInteger valid */
      kVstParameterUsesFloatStep = 1 << 2, /* stepFloat, smallStepFloat, largeStepFloat valid */
      kVstParameterUsesIntStep = 1 << 3, /* stepInteger, largeStepInteger valid */
      kVstParameterSupportsDisplayIndex = 1 << 4, /* displayIndex valid */
      kVstParameterSupportsDisplayCategory = 1 << 5, /* category, etc. valid */
      kVstParameterCanRamp = 1 << 6 /* set if parameter value can ramp up/down */
    };

# Mixxx

All Parametes in Mixxx are of C Type double.

Mixxx uses the scaled "value" for it's double controls. It is Converted
into a parameter, a linear representation of the position on the scale
by control behavior classes.

If the value of the control does not match the value that should be
indicated in LDS, a separate indicator control is used.

### Parameter Hints

    class EffectManifestParameter {
      public:
        enum ValueHint {
            VALUE_UNKNOWN = 0,
            VALUE_BOOLEAN,
            VALUE_INTEGRAL,
            VALUE_FLOAT
        };
        
        enum ControlHint {
            CONTROL_UNKNOWN = 0,
            CONTROL_KNOB_LINEAR,
            CONTROL_KNOB_LOGARITHMIC,
            CONTROL_TOGGLE
        };
        
        enum SemanticHint {
            SEMANTIC_UNKNOWN = 0,
            SEMANTIC_SAMPLES,
            SEMANTIC_NOTE,
        };   
           
        enum UnitsHint {
            UNITS_UNKNOWN = 0,
            UNITS_TIME,
            UNITS_HERTZ,
            UNITS_SAMPLERATE, // fraction of the samplerate
            UNITS_BEATS, // multiples of a beat
        };
        
        enum LinkType {
            LINK_NONE = 0, // Not controlled by the super knob
            LINK_LINKED, // Controlled by the super knob as it is
            LINK_LINKED_LEFT, // Controlled by the left side of the super knob
            LINK_LINKED_RIGHT, // Controlled by the right side of the super knob
            LINK_LINKED_LEFT_RIGHT, // Controlled by both sides of the super knob
            NUM_LINK_TYPES
        };
        
        ...

# Requirements

  - Value feedback including units 
  - Control a quantization Value with a continuous Knob 
  - Feedback of the Snapped value 
  - Controllable by Super knob 
  - Support all hardware controls on a DJ Console 
  - Continous Knobs
  - Endless knobs
  - Pushbuttons
  - Allow native adaptation of LV2 PlugIns
  - Allow native adaptation of VST PlugIns 
  - Control different common scales including Split scales for
    asymmetric knobs 

# Links

  - Related Bug: <https://bugs.launchpad.net/mixxx/+bug/1378195>
  - Remove of value hint: <https://github.com/mixxxdj/mixxx/pull/356>
  - EQ Rack: <https://github.com/mixxxdj/mixxx/pull/297>
  - Button Parameter: <https://github.com/mixxxdj/mixxx/pull/281>
  - Kill Buttons: <https://github.com/mixxxdj/mixxx/pull/297>

# Proposed Solution

Nicu has proposed a solution during his GSoC proeject.

It can be watched at:

LV2 branch: <https://github.com/mixxxdj/mixxx/pull/316>

EQ Rack: <https://github.com/mixxxdj/mixxx/pull/330>

Essence:

It fetures two types of controls:

  - Knob controls, for all parameters that are intended to be controlled
    by the superknob 
  - Button controls, for all step parameters. It features a normal
    button Widget + a flyout menu with the enumeration values. 

# Discussion

TODO:

Thoughts:

LV2 and VST uses c float type to express all kinds values. Mixxx uses
double types for the same. Conclusion: there is no need to convert
double to QVariant and back. Double parameters are just fine.

We need to have a way to connect to Buttons and Rotaries on the DJ
controller. The effect needs to control from where the value should be
controlled.

All effect parameters that are usable to tweak while the effect is
active should be placed on a Rotary control since not all controllers
are featuring buttons for effects.

We need to extend enum ControlHint() to express more complex Scales.
