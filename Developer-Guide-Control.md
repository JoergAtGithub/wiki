# Introduction to Mixxx's Control System

Mixxx's control system is best described as a thread-safe communication
channel that allows different threads to have shared access to read and
modify values by name.

You can think of the Control system as Mixxx's internal API. Since we
have one single API for accomplishing most things in Mixxx, we do not
have duplicate logic to support keyboard control, MIDI/HID control, and
GUI control. The keyboard, MIDI/HID, and GUI all use the same API to
interact with Mixxx's mixing engine and other subsystems.

The first version (present since the very beginnings of Mixxx) of the
control system is limited to only double-precision floating point
values.

# Control Naming

Controls are referred to by a 2-part name called a `ConfigKey`.
`ConfigKey`s have a `group` and an `item`. The group is used to explain
the category of the control while the item describes specifically what
the control is.

By convention, the group of a ConfigKey is wrapped with square brackets.
This is because the `ConfigKey` class is also used to indicate values to
store in the Mixxx preferences file which is organized like a [Windows
INI file](http://en.wikipedia.org/wiki/INI_file).

Control items mostly use the `snake_case` naming, although some use
`PascalCase` for legacy reasons. When adding new controls, `snake_case`
should be used.

Examples:

  - Group: `[Microphone]` Item: `volume`
  - This control is holds the value of the microphone's volume. 
  - Group: `[Sampler1]` Item: `hotcue_1_activate`
  - This control is used to conceptually represent a button that
    activates the first hotcue of the first sampler. Setting it to a
    value of 1 indicates that the virtual button is down while setting
    it to 0 indicates that the virtual button is released.

For a mostly complete list of controls which are intended to use in
skins or controller mappings, see the [MixxxControls](mixxxcontrols)
page. For a complete list, which contains also unstable internal
controls, start Mixxx from the command line using `mixxx --developer`.
Now you can open the list by the menu: "Developer" -\> "Developer Tools"
here you can also watch and edit the current values.

# Creating Controls

To create a new control you must instantiate a `ControlObject`. Once
you've done this, you've created a global control that is accessible by
the `ConfigKey` you name it with.

As an example, let's say we want to create a control that keeps track of
whether the microphone is enabled:

``` c++
ConfigKey micEnabledKey = ConfigKey("[Microphone]", "enabled");
ControlObject* pMicEnabled = new ControlObject(micEnabledKey);

// Sets [Microphone],enabled to 1 (on)
pMicEnabled->set(1.0);

// Sets [Microphone],enabled to 0 (off)
pMicEnabled->set(0.0);
```

Once you have created a `ControlObject`, it is inserted into a global
registry of controls and any other Mixxx thread can look it up by name
using a `ControlProxy`.

For example, if you wanted to create a GUI widget that looked up whether
the microphone was enabled or not, you would do this:

``` c++
ControlProxy* pMicEnabled = new ControlProxy("[Microphone]", "enabled");
bool mic_enabled = pMicEnabled->toBool();
    
if (mic_enabled) {
    // draw a red light indicating the mic is enabled
} else {
   // draw a dim off light indicating the mic is disabled
}

```

Note that we used a `ControlProxy` to access the `ControlObject` we
looked up from the control system. This is because we are not the
original "owner" of this `ControlObject`. Using a `ControlProxy` allows
you to safely access other `ControlObject`s from other places within
Mixxx.

To change the microphone-enabled value from elsewhere in Mixxx, it's as
simple as this:

``` c++
// Disable the microphone from elsewhere in Mixxx.
pMicEnabled->set(0.0);
```

# Types of Controls

`ControlObject` has a variety of subclasses. Each of these subclasses
allows you to express constraints on the value stored in the
`ControlObject`. For example, if you wanted to represent a knob that had
values between -1 and 1 then you could use a `ControlPotmeter` and set
its min and max value to -1 and 1. This would prevent any other part of
Mixxx from setting the control to an invalid value.

Another use of using a subclass of `ControlObject` is that you can make
a control that is non-linear in the values that it produces. For
example, a `ControlLogpotmeter` is a knob/potentiometer whose output
follows a logarithmic curve even though the input coming from a MIDI
controller of the GUI is linear.

## ControlPushButton

A `ControlPushButton` is a control that emulates a button. The name is a
misnomer since it doesn't only emulate push-buttons -- it can also
emulate multi-state toggle buttons.

`ControlPushButton` has the following modes:

  - Push-button -- acts like a push button where a value \> 0 means it
    is pressed and a value of 0 means it is not pressed.
  - Toggle button -- acts like a multi-state toggle button. Pressing it
    and releasing it will increment its value by one. Once it increments
    past the total number of states it has it will wrap around to 0. For
    a 2-state toggle button this means it will toggle between 0 and 1
    every time you press it. 
  - Power-Window button -- acts like a power-window button on your car.
    Pressing and holding it makes it act like a push-button (e.g. power
    window goes down or up only as you hold it) but pressing and
    releasing it quickly will toggle it (e.g. power window goes down or
    up automatically). 

Relevant Methods:

  - To change the mode, call `ControlPushButton::setButtonMode(enum
    ButtonMode)` 
  - To change the number of states call
    `ControlPushButton::setStates(int)`

## ControlPotmeter

A `ControlPotmeter` represents a knob or potentiometer that has a
minimum and maximum value. All modifications to the control are checked
and snapped within the specified range.

All `ControlPotmeter`s have a set of additional controls that are
automatically created for them. Assuming a `ConfigKey` of
`[Group]`,`item`, the controls that are created are:

  - `[Group]`,`item_up` -- Increment (coarse adjustent, default 10% of
    range)
  - `[Group]`,`item_down` -- Decrement (coarse adjustent, default 10% of
    range)
  - `[Group]`,`item_up_small` -- Increment by a small amount (fine
    adjustent, default 1% of range)
  - `[Group]`,`item_down_small` -- Decrement by a small amount (fine
    adjustent default 1% of range)
  - `[Group]`,`item_set_default` -- Sets the value to default (the
    default default is the half-way point
  - `[Group]`,`item_set_zero` -- Sets the value to 0
  - `[Group]`,`item_set_one` -- Sets the value to 1
  - `[Group]`,`item_set_minus_one` -- Sets the value to -1
  - `[Group]`,`item_toggle` -- Toggle between 0 and 1
  - `[Group]`,`item_minus_toggle` -- Toggle between 0 and -1

## ControlLogpotmeter

## ControlBeat

## ControlTTRotary

## Read-only Controls

A control can be marked read-only by using `ControlObject`'s
`setReadOnly` method.

This method intercepts calls to the `set` method of the `ControlObject`
and any associated `ControlProxy`s and prints a warning message that the
control is read-only. As the owner, to set the control's value, you must
use the `ControlObject`'s `forceSet` method. Only the owner of the
control (see above) should update it this way -- do not bypass this by
using `ControlObject::getControl`.

``` c++
ControlObject track_loaded(ConfigKey(group, "track_loaded"));
track_loaded.setReadOnly();

// Sets on the ControlObject are ignored.
track_loaded.set(1);
assert(track_loaded.get() == 0);

// Sets from proxies are also ignored.
ControlProxy proxy(group, "track_loaded");
proxy.set(1);
assert(track_loaded.get() == 0);

// As the owner, the only way to change the control's value is via forceSet.
track_loaded.forceSet(1);
assert(track_loaded.get() == 1);
```

# Automatically reacting to control changes

As different parts of Mixxx change controls that you create, you will
likely want to react to those changes. Similarly, if you are relying on
certain controls created elsewhere in Mixxx, you may want to
automatically take action when one of them changes.

If you are the creator of a control, i.e. you are using the raw
`ControlObject` and not a `ControlProxy` then you can listen to changes
in your control by connecting to the `ControlObject`'s
`valueChanged(double)` signal.

``` c++
ControlObject* pMicEnabled = new ControlObject(ConfigKey("[Microphone]", "enabled"));
connect(pMicEnabled, SIGNAL(valueChanged(double)), 
        this, SLOT(slotMicrophoneEnabledRequest(double)));

// In your slot, handle the changes to the [Microphone],enabled control
void MicrophoneManager::slotMicrophoneEnabledRequest(double v) {
  // The microphone's enabled value has changed
  bool mic_enabled = v > 0.0;
  
  if (mic_enabled) {
    // some other part of Mixxx is requesting to enable the microphone, do that
  }  else {
    // some other part of Mixxx is requesting to disable the microphone, do that
  }
}
```

`ControlObject` actually has two value-change signals
`valueChanged(double)` and `valueChangedFromEngine(double)`. These two
signals should really be named `valueChangedByProxy(double)` and
`valueChangedByControlObject(double)`, respectively. The first signal is
fired when a proxy (`ControlObjectThread`, etc.) was used to change the
control while the second is fired when the `ControlObject` itself is
used to change the value by its `set(double)` method. The reason for
having two signals is to prevent infinite loops of signal processing. If
you create the `ControlObject` and then call `set(1.0)` on it but you
also connect to its `valueChanged(double)` signal, then you will get a
call for the `valueChanged(double)` signal which you might want to react
to by in turn changing the enabled `ControlObject`. If you do this and
get a callback for the value you changed then you will go into an
infinite loop of setting and reacting to your `ControlObject`. For this
reason, there are two different types of value-changed signals.

Going back to the microphone-enabled GUI widget example, if you are
using a `ControlProxy`, you can listen to changes in the control by
doing the following:

``` c++
ControlObjectThread* pMicEnabled = new ControlProxy("[Microphone]", "enabled", this);
pMicEnabled->connectValueChanged(SLOT(slotMicrophoneEnabledChanged(double v)));
  
// In your slot, handle the changes to the [Microphone],enabled control
void MicrophoneWidget::slotMicrophoneEnabledChanged(double v) {
  // The microphone's enabled value has changed
  bool mic_enabled = v > 0.0;
  
  if (mic_enabled) {
    // redraw the widget with a red light to indicate the microphone is enabled
  }  else {
    // redraw the widget with a dark light to indicate the microphone is not enabled
  }
}      
```

# Deleting Controls

Be sure you delete all ControlObjects after they are not used anymore to
avoid memory leaks. In general once you create a control you should not
delete it until Mixxx shuts down. Since creating a control is like
setting up an API call.
