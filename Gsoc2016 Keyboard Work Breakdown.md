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
