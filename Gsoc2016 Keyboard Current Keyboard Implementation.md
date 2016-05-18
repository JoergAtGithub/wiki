### KeyboardEventFilter

KeyboardEventFilter is an [event
filter](http://doc.qt.io/qt-4.8/eventsandfilters.html).

MixxxMainWindow (mixxx.h/.cpp) initializes and holds a global instance
of KeyboardEventFilter (MixxxMainWindow.m\_pKeyboard). Other Mixxx
objects get a pointer to this instance and install it as their event
filter:

  - MixxxMainWindow calls SkinLoader::loadDefaultSkin passing to it its
    KeyboardEventFilter.
  - SkinLoader constructs a LegacySkinParser and passes the
    KeyboardEventFilter to it. The LegacySkinParser holds a pointer to
    the KeyboardEventFilter. It installs the KeyboardEventFilter to
    every widget it creates.
  - Library features install the KeyboardEventFilter in its bindWidget
    method.
  - Library extra views (such as the view that groups autodj controls)
    get the KeyboardEventFilter installed by their delegates
    constructor.
