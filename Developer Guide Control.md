# Introduction

Mixxx's control system is best described as a thread-safe communication
channel that allows different threads to have shared access to read and
modify values by name.

# Control Naming

Controls are referred to by a 2-part name called a `ConfigKey`.
`ConfigKey`s have a `group` and an `item`. The group is used to explain
the category of the control while the item describes specifically what
the control is.

Examples:

  - Group: `[Microphone]` Item: `volume`
  - This control is holds the value of the microphone's volume. 
  - Group: `[Sampler1]` Item: `hotcue_1_activate`
  - This control is used to conceptually represent a button that
    activates the first hotcue of the first sampler. Setting it to a
    value of 1 indicates that the virtual button is down while setting
    it to 0 indicates that the virtual button is released.

For a mostly complete list of controls that exist, see the
[MixxxControls](mixxxcontrols) page.
