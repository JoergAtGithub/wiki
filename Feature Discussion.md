# Feature Discussion

This page is to discuss possible future features along with some
implementation details. Lengthy discussions will probably get moved to
their own page.

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

  - libavformat/libavcodec (the library used by ffmpeg and mplayer)
  - support lots of formats
  - support utf8
  - libxine
  - supports lots of formats and is extensible
  - use to play audio from (multiplexed) video files
  - future VJ support?
  - Is libxine cross-platform? What does Songbird use? --- *[Albert
    Santoni](albert@santoni.ca) 2008/11/11 01:40*

## Playqueue and Library Improvements Proposals

[See the dedicated
page](http://mixxx.org/wiki/doku.php/playqueue_and_library_improvements_proposals).

## Other Ideas

(Copied from [feature\_wishlist](feature_wishlist))

If you think of a feature that we need to implement at some time, jot it
down here so you don't forget.

Some of these are copied over from the forums and the old wiki, so they
may be done already or irrelevant.

  - Split cue/master headphone support
  - Visual 'track ending' indicator for visual waveform
  - Effects panel integration with UI
  - SVG/Vector based skins so hitting fullscreen can automatically
    resize the widgets.
  - Looping controls
  - A mode where the looping would start at the next beat / end of the
    bar and would jump x beats \_backwards\_ when starting to loop
  - 'Online' BPM detection so that visual waveform beat marks can
    actually be accurate.
  - M4A support
  - hotkey support (maybe configurable?)
  - adjustable drag sensitivity on visual waveform view
  - also a way to change the direction ("scratching motion")
  - direct outs (table 1, table 2, master, headphones)
  - [Effect plugins](PluginIdeas)
  - live input (switchable input at first, maybe a delay/pitchable input
    later)
  - OSC controlled backend [Details from Old
    Wiki](http://mixxx.sourceforge.net/wiki/index.php/OSC_Backend)
  - some more physically modelled turntable styles, with concepts of
    inertia, slipmat vector, and motor drive. [Details from Old
    Wiki](http://mixxx.sourceforge.net/wiki/index.php/Deck_Remodeling)
  - Normalize to the waveform, track volume and output (over longer
    perioid in the master output)
  - Channel gain to affect the waveform
  - BPM sync lock like in virtual dj (keep tracks in sync)
  - Play lock feature so that you can't change a track that is currently
    playing
  - A button to switch between the vinyl emulation & pitch independent
    time stretch ("master temp in cdjs")
  - Remain / played time display switch
  - "Loading" animation for the waveforms
  - Clipping light to stay on (dimmer?) after clipping, reset by
    clicking
