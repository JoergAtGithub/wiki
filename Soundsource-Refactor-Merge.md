## Reducing Number of Input Libraries

Possibly migrating to a single file decoding solution such as
libavformat.

### Pros

  - Reduces library dependency count
  - Increases playable formats
  - I specifically want m4a/aac playback in our next version - [Adam
    d](/User/Adam%20d)
  - User can recompile library to add new format support to an old
    version of mixxx

### Cons

  - Lots of work to make the change
  - All our eggs are in one basket

### Possible Libraries

  - [libsox](http://sox.sourceforge.net/libsox.html)
  - supports nearly every format known to man
  - can write many of them as well (for recording your set)
  - has built-in effects processing
  - libavformat/libavcodec (the library used by ffmpeg and mplayer)
  - support lots of formats
  - support utf8
  - xine-lib
  - supports lots of formats and is extensible
  - use to play audio from (multiplexed) video files
  - future VJ support?
  - It's not totally cross-platform yet but progress is ongoing:
    <http://www.xine-project.org/about>
  - gstreamer
  - used by Songbird
  - plugins allow more formats (QuickTime, WMA, FFMPEG, etc.)
