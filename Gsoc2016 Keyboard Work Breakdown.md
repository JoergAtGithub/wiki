## 1 - Sub class Controller

Add tests

## 2 - Sub class *ControllerEnumerator*

## 3 - Modify *ControllerManager*

1.  Append *KeyboardEnumerator* in the *slotInitialize* method.

## 3 - Sub class *ControllerPreset*

### Get keyboard events

Possible approaches:

  - Install a global event filter or something similar to get all Qt
    keyboard events. Easier approach, but I think this won't let us
    differentiate between different physical keyboards.
  - Access keyboards with a lower level API.

Reference: <http://doc.qt.io/qt-4.8/eventsandfilters.html>

don't break tooltips, make them read current keyboard preset.

add CO (if not already existent) to enable/disable controllers (make a
special one for keyboard controllers?). this is to keep support for the
"enable keyboard shortcuts" option of the options menu.

mixxx currently leaks some keyboard events to Qt. This allows library
lists to respond to arrow key presses for example. Do we want this?
Better manage this via mapping like Traktro does?
