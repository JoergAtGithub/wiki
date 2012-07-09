# Introduction

Mixxx's control system is best described as a thread-safe communication
channel that allows different threads to have shared access to read and
modify values by name.

You can think of the Control system as Mixxx's internal API. Since we
have one single API for accomplishing most things in Mixxx, we do not
have duplicate logic to support keyboard control, MIDI/HID control, and
GUI control. The keyboard, MIDI/HID, and GUI all use the same API to
interact with Mixxx's mixing engine and other subsystems.

The first version (present in all Mixxx versions up to Mixxx 1.11.0) of
the control system is limited to only double-precision floating point
values. In the future we would like to replace the control system with
one that can support any type based on Qt's `QVariant` data type. For
more information on this project, see the design document: [Revamped
Control System](revamped_control_system).

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

# Creating Controls

To create a control you must instantiate a `ControlObject`. Once you've
done this, you've created a global control that is accessible by the
`ConfigKey` you name it with.

As an example, let's say we want to create a control that keeps track of
whether the microphone is enabled:

    ConfigKey micEnabledKey = ConfigKey("[Microphone]", "enabled");
    ControlObject* pMicEnabled = new ControlObject(micEnabledKey);
    
    // Sets [Microphone],enabled to 1 (on)
    pMicEnabled->set(1.0);
    
    // Sets [Microphone],enabled to 0 (off)
    pMicEnabled->set(0.0);

Once you have created a `ControlObject`, it is inserted into a global
registry of controls and any other Mixxx thread can look it up by name.

For example, if you wanted to create a GUI widget that looked up whether
the microphone was enabled or not, you would do this:

    ConfigKey micEnabledKey = ConfigKey("[Microphone]", "enabled");
    
    // Lookup the control by ConfigKey in the global registry. Returns NULL if control does not exist!
    ControlObject* pMicEnabledCO = ControlObject::getControl(micEnabledKey);
    
    // If the mic-enabled control exists...
    if (pMicEnabled != NULL) {
        // You could call pMicEnabledCO->get() to get the controls value but this is not thread safe.
        // Instead, wrap it the ControlObject in a ControlObjectThread
        ControlObjectThread* pMicEnabledCOT = new ControlObjectThread(pMicEnabledCO)
        bool mic_enabled = pMicEnabledCOT->get() > 0.0;
        
        if (mic_enabled) {
          // draw a red light indicating the mic is enabled
        } else {
          // draw a dim off light indicating the mic is disabled
        }
    }

Note that we used a `ControlObjectThread` to wrap the `ControlObject` we
looked up from the control system. This is because we are not the
original "owner" of this `ControlObject`. Using a `ControlObjectThread`
allows you to safely access other `ControlObject`s from other places
within Mixxx.

To change the microphone-enabled value from elsewhere in Mixxx, it's as
simple as this:

    // Disable the microphone from elsewhere in Mixxx.
    pMicEnabledCOT->slotSet(0.0);

# Automatically reacting to control changes

As different parts of Mixxx change controls that you create, you will
likely want to react to those changes. Similarly, if you are relying on
certain controls created elsewhere in Mixxx, you may want to
automatically take action when one of them changes.

If you are the creator of a control, i.e. you are using the raw
`ControlObject` and not a `ControlObjectThread` then you can listen to
changes in your control by connecting to the `ControlObject`'s
`valueChanged(double)` signal.

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
using a `ControlObjectThread`, you can listen to changes in the control
by doing the following:

``` 
ControlObjectThread* pMicEnabledCOT = new ControlObjectThread(ControlObject::getControl(ConfigKey("[Microphone]", "enabled")));
connect(pMicEnabledCOT, SIGNAL(valueChanged(double)),
        this, SLOT(slotMicrophoneEnabledChanged(double v)));
  
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

In general once you create a control you should not delete it until
Mixxx shuts down. Since creating a control is like setting up an API
call, deleting it may cause parts of Mixxx that use your control to
break.

# ControlObjectThread vs ControlObjectThreadMain vs ControlObjectThreadWidget

`ControlObjectThread`, `ControlObjectThreadMain` and
`ControlObjectThreadWidget` are the three different types of
`ControlObject` "proxies". These proxies allow you to safely access a
`ControlObject` across different threads. In general, you should use
this rule of thumb:

  - If your code runs in the Main/GUI thread, use a
    `ControlObjectThreadMain`
  - If your code runs in a non-Main/GUI thread, use a
    `ControlObjectThread`
  - Never use a `ControlObjectThreadWidget` -- it is an implementation
    detail of the GUI/Widget system.
