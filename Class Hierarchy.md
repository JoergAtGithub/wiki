# Mixxx core application

## ControllerManager

Works alongside **ControllerProcessor** which is a separate thread in
which all Controller-related activities happen. ControllerManager
maintains a list of controllers.

### ControllerEnumerator

  - MidiEnumerator
  - HidEnumerator
  - OscEnumerator

### Controller

May spawn reader threads if needed to create a callback-like system.

  - MidiController
  - HidController
  - OscController

#### ControllerEngine

Contains the QScriptEngine.
