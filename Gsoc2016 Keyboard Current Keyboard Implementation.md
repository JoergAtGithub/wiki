### KeyboardEventFilter

KeyboardEventFilter is an [event
filter](http://doc.qt.io/qt-4.8/eventsandfilters.html).

MixxxMainWindow (mixxx.h/.cpp) initializes and holds a global instance
of KeyboardEventFilter (MixxxMainWindow.m\_pKeyboard). Other Mixxx
objects get this instance and install it as their event filter:

  - MixxxMainWindow calls SkinLoader::loadDefaultSkin passing to it a
    pointer to its KeyboardEventFilter.
  - SkinLoader constructs a LegacySkinParser and passes a pointer to the
    KeyboardEventFilter to it. The LegacySkinParser holds a pointer to
    the instance. It uses it to install the KeyboardEventFilter to every
    widget it creates.
  - Library features install the event filter in its bindWidget method.
  - Library extra views (such as the view that groups autodj controls)
    get the event filter installed by their delegates constructor.
