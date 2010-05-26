# Effects Units based on existing LADSPA integration (GSoC 2010 project)

  - Student: **Bruno Buccolo**

<!-- end list -->

``` 
    * Email: bruno.buccolo.gmail.com
    * IRC Handle: Buccolo
    * Skype Handle: bruno.buccolo
* Mentor: **Russell Ryan**
```

### Abstract

Sometimes playing the right tracks at the right time in a perfect mix is
not enough. Users like to use effects/filters in their mix to squeeze
every bit of energy of a track, make creative mixes using filters, delay
beats to get funky, use reverb on vocals to fill the room and so on.
Mixxx can already host LADSPA plugins, however it lacks a user interface
for proper configuration since there must be a mapping between Mixxx
controls and LADSPA plugins.

I'm proposing not only designing a user interface for configuration of
LADSPA plugins, but also taking the effects on Mixxx to a whole new
level. I'll create Effects Units, that will have standard controls, so
we only have to map MIDI once, and then plug-in the desired effect in
the effect unit to use them. The user will also have the flexibility to
choose how he's going to use these 2 effects units, being able to use
both on a channel, a unit per channel or even both on master.

### More

  - Check out the [LADSPA page](ladspa).
  - See this project's code:
    [features\_ladspa](https://code.launchpad.net/~bruno-buccolo/mixxx/features_ladspa)
  - Read my GSoC posts here: [My
    Blog](http://blog.brunobuccolo.com/tagged/GSoC)
  - Read the complete proposal: [Effects Units based on existing LADSPA
    integration](http://docs.google.com/Doc?docid=0AbM4coH1acQfZGczaGdyaG1fODZmcHdqcHdkdw&hl=en_GB)

### Requirements

#### Effects Units

  - Two independent Effects Units for Mixxx
  - An Effect Unit will be loaded with the desired LADSPA Plugin
  - The input of a Effect Unit will be Channel 1, Channel 2 or Both
  - Effects Chaining should be possible (One Channel as input for two
    Effects Units)
  - An Effect Unit will have 4 Parameters and Wet\&Dry that will
    correpond to the mapped ports of the LADSPA Plugin
  - All controls for the Effects Units can be MIDI Mapped
  - Abstraction of effects backend (ladspa only, for now)

#### Configuration Dialog

  - Mapping of LADSPA Plugin's control ports to Effects Units parameters
  - Selection of plugin's Wet/Dry control port
  - Value range for control ports (Min \~ Max, Default)
  - Adding custom plugins downloaded from the internet (place on
    LADSPA\_PATH?)
  - Save/Load Configuration

### To-Do

#### Effects Units

  - Code: Define code architecture
  - Code: Think about data structures to use
  - Code: Design uml diagram for the code architecture
  - Code: Backend abstraction layer
  - Code: Ladspa \<--\> Effects Unit connector
  - Code: Enabling MIDI Mapping of Effects Units
  - Code: Study how to choose input for effects
  - GUI: Basic tab view for development only.
  - GUI: Display combobox with available effects
  - GUI: Load port names for the selected effect
  - GUI: RFC on Mockup [Effects
    Units](http://picasaweb.google.com/bruno.buccolo/GoogleSummerOfCode2010#5454860218402307986)

#### Configuration Dialog

  - Code: Think about xml structure to save the presets
  - Code: Implement Load/Save xml
  - Code: Adding custom paths to plugins (really necessary?)
  - GUI: Basic preferences panel dialog
  - GUI: Load available LADSA Plugins into list
  - GUI: Load LADSPA Plugin's port names into combo boxes
  - GUI: Min, Max, Default values for each control port
  - GUI: RFC on Mockup [Configuration
    Dialog](http://picasaweb.google.com/bruno.buccolo/GoogleSummerOfCode2010#5454889269445147954)

#### Deployment

  - Select standard Plugins to be shipped
  - Create good presets for them
  - Carefully study how to give instructions for the 

#### Extra

  - See [LADSPA page](ladspa).

### Activity

**Current:** Working my way through designing the structure for this
project as well as organizing myself.

#### History

  - Community Bonding Period:
    [features\_midi\_learn](https://code.launchpad.net/~bruno-buccolo/mixxx/features_midi_learn)
