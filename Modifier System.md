# Modifier System

The modifier system will be an easy to use system for controlling and
configuring behaviours for novice users.

## Summary and Rationale

Allow configuration of behaviours like shift buttons and deck changes
through a UI.

## Use Cases

This is mostly intended for novice users who do not program

  - map the shift button to delete hotcues.
  - map the deck A/C and/or deck B/D buttons.
  - progress through through a combo.

## Design

Four new optional settings are added for controls.

  - modifier name to set.
  - modifier value to set.
  - modifier name to activatated on.
  - modifier value to be activated on.

Modifiers can be of three types:

  - Boolean: switch shift on/off
  - Integer: change to deck 1..N or combostep=3
  - String: turn on mode=Psycho, combo=sidewinder, deck="DeckA" or
    deck="DeckC"

### Internal functioning

These settings then generate Javascript functions which are generated,
evaluated and bound directly to the MIDI mappings. An API in Javascript
will be made specifically for this functionality. Mixing and matching
scripting and modifiers is not yet contemplated.

#### Javascript API (thoughts)

Note: we could just set the values with Qt. The modifier variable then
would just be for use from javascript, mostly...

Modifiers will be handled by a simple Hash map as such:

``` 
  modifier['shift'] = false;
  modifier['deck'] = 0;
  modifier['combostep'] = 0;
  modifier['combo'] = null;
```

The mapping for the shift key would like this:

``` 
  /* Map the control with option button in the UI */
  /* assuming for now note on status = true, note off status = false ... */
  Controller.shift_key = function(channel, control, value, status, group) {
      modifier['shift'] = status ? true : false;
  }
```

The engine internally checks the value of the modifiers before
triggering the MIDI mapping, we also check each MIDI mapping to see if
it has modifier version if it does not have on set (doing it this way is
because of how the format is defined). Generate a mapping internally
that accounts for this more efficiently? We can map these MIDI mappings
to controls or javascript functions, nothing stopping anyone.
