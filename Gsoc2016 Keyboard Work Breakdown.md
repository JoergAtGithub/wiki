### Get keyboard events

Possible approaches:

  - Install a global event filter or something similar to get all Qt
    keyboard events. Easier approach, but I think this won't let us
    differentiate between different physical keyboards.
  - Access keyboards with a lower level API.

Reference: <http://doc.qt.io/qt-4.8/eventsandfilters.html>
