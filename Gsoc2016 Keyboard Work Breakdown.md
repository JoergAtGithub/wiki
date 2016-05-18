## 1 - Sub class Controller

You have to implement the pure virtual methods. Take *MidiController*
and *PortMidiController* or *HidController* as a reference.

1.  Implement destructor.
2.  Implement *presetExtension* method. Add corresponding \#define in
    defs\_controller.h.
3.  Implement the *accept* method (part of the visitor pattern).
4.  Implement the *savePreset* method (just prepare it for the upcoming
    *KeyboardPresetFileHandler*).
5.  Implement the *getPreset* method.
6.  Implement the *isMappable* method.
7.  What do you need to do with the *matchPreset* method?
8.  What do you need to do with the *receive* method?
9.  ...
10. Add tests.

### Get keyboard events

Possible approaches:

  - Install a global event filter or something similar to get all Qt
    keyboard events. Easier approach, but I think this won't let us
    differentiate between different physical keyboards.
  - Access keyboards with a lower level API.

Reference: <http://doc.qt.io/qt-4.8/eventsandfilters.html>

## 2 - Sub class ControllerEnumerator

1.  Add tests.

## 3 - Sub class ControllerPreset

1.  Create a *KeyboardPresetFileHandler* class (like
    *MidiControllerPresetFileHandler*).
2.  Add tests.

## 4 - Modify ControllerManager

1.  Append *KeyboardEnumerator* in the *slotInitialize* method.

Notes:

don't break tooltips, make them read current keyboard preset.

add CO (if not already existent) to enable/disable controllers (make a
special one for keyboard controllers?). this is to keep support for the
"enable keyboard shortcuts" option of the options menu.

mixxx currently leaks some keyboard events to Qt. This allows library
lists to respond to arrow key presses for example. Do we want this?
Better manage this via mapping like Traktro does?
