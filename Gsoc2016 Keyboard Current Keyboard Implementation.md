### KeyboardEventFilter

This is an [event
filter](http://doc.qt.io/qt-4.8/eventsandfilters.html). Mixxx installs
it in the following widgets:

MixxxMainWindow (mixxx.h/.cpp) initializes and holds a global instance
of KeyboardEventFilter (MixxxMainWindow.m\_pKeyboard). Other Mixxx
objects get this instance and install it as their event filter.

  - Library features install the event filter in its bindWidget method.
  - Library extra views (such as the view that groups autodj controls)
    get the event filter installed by their delegates constructor.
