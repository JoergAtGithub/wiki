### KeyboardEventFilter

*KeyboardEventFilter* is an [event
filter](http://doc.qt.io/qt-4.8/eventsandfilters.html).

*MixxxMainWindow* (mixxx.h/.cpp) initializes and holds a global instance
of *KeyboardEventFilter* (*MixxxMainWindow*.m*\_*pKeyboard). Other Mixxx
objects get a pointer to this instance and install it as their event
filter:

  - *MixxxMainWindow* calls *SkinLoader*::*loadDefaultSkin* passing to
    it its *KeyboardEventFilter*.

<!-- end list -->

  - *SkinLoader* constructs a *LegacySkinParser* and passes the
    *KeyboardEventFilter* to it. The *LegacySkinParser* holds a pointer
    to the *KeyboardEventFilter*. It installs the *KeyboardEventFilter*
    to every widget it creates.

<!-- end list -->

  - Library installs the *KeyboardEventFilter* to some views in its
    *bindWidget* method,

<!-- end list -->

  - Library features install the *KeyboardEventFilter* in its
    *bindWidget* method.

<!-- end list -->

  - Library extra views (such as the view that groups autodj controls)
    get the *KeyboardEventFilter* installed by their delegates
    constructor.

<!-- end list -->

  - *SkinLoader* also uses the *KeyboardEventFilter* in its
    *setupConnection* method to gain information about assigned key
    combinations to fill the tooltips.
