# Creating a new Waveform View handler for Mixxx (GSoC 2008 project)

  - Student: **Russell Ryan**
  - Mentor: **Albert Santoni**

### Abstract

The current Mixxx waveform view is in need of a refresh. In its current
state it is not flexible enough to support desirable new features, and
it also causes performance issues that can cause skipping in the audio.
Redesigning the waveform view will both provide Mixxx with a more
feature-full waveform view and hopefully alleviate these performance
issues.

The goal of the project is to rewrite the Mixxx waveform view. The new
waveform view will support all the current features of the waveform
view, and more. The new viewer will be designed to be flexible enough to
support improvements and features that could come in the future.

Features of the waveform viewer include:

  - A display of a waveform with time on the horizontal axis and
    amplitude on the vertical axis.
  - A center 'mark' which indicates the current position of the player
    on the waveform.
  - 'beat frames' which coordinate with Mixxx's beat detection
    algorithms to render markers on each detected beat in the waveform
  - Coloring of the waveform based on the 'timbre' or sound feel of the
    waveform.
  - Integration with the GUI (or vinyl control interfaces) to support
    dragging of the waveform back and forth
  - Support for drag-and-dropping a song onto a 'virtual deck' to load
    the song into that deck
  - Support for an arbitrary number of audio streams for which to
    display waveforms
  - Support for markers or other meta-indicators to be set on the
    waveform to serve as visual feedback to the user. This will be
    useful for implementing features such as looping controls.

These features will be implemented over the course of the summer of
2008. Checkpoints and measurable progress indicators will be used to
ensure development is on schedule.

### General Design Overview

(warning: i'm dumping some free-written text that might not make
complete sense. i'll clean it up as I go)

  - Need a WaveformViewerFactory that produces waveform viewer widgets.
    This gets rid of the awkward dance done in mixxx/mixxxview to create
    a waveform viewer, but then fallback to WVisualSimple if OpenGL is
    not available.
  - In order to do this, we need a standard interface for talking with a
    waveform viewer widget.
  - With enough abstraction, it shouldn't be too hard to do an OpenGL
    approach, a QPainter approach, AND a Simple approach (the current
    non-opengl path).
  - This requires changes to the way that Mixxx talks with the waveform
    viewer. Currently it is a little messy -- I'll be cleaning that up.
  - Accordingly -- need two widget types (QGLWidget and QWidget)
    Unfortunately to formally standardize the Mixxx interface for the
    two, they may need to use multiple inheritance to inherit from a
    WAbstractWaveformViewer-ish type that will codify the existence of
    'setup()', etc. 

## WaveformViewerFactory

A factory for producing waveform viewer widgets. During Mixxx
initialization, all Mixxx will do is ask for a waveform widget given the
config object. The factory will worry about whether GL is available,
etc.

As it stands, Mixxx calculates whether the waveform preference is set
and passes this as a boolean to the MixxxView constructor. Also
MixxxView worries about setting up shared context between QGLWidgets,
and whether to instantiate a GL waveform viewer or a simple one. The
factory will hide all of this, and ultimately make
Mixxx.cpp/MixxxView.cpp cleaner.

## AbstractWaveformViewer

A base waveform viewer type that will setup the standard interface for
Mixxx to with a generic waveform viewer. The code currently stores a
pointer to the waveform viewer as a QObject and then casts wherever
necessary to represent the tyep as a waveform object.

## WGLWaveformViewer

A QGLWidget that renders the

## WWaveformViewer

## AbstractWaveformRenderer

Base type/interface for a renderer (like the 3 below) to inherit from.

## GLWaveformRenderer

Uses an OpenGL context to render the waveform using accelerated graphics
hardware. Requires direct rendering in Linux, which is a downside.

## WaveformRenderer

Uses a regular Widget with QPainter to draw the waveform without
hardware acceleration. This could throttle the CPU on some systems, so
the user may want to disable it.

## SimpleRenderer

For the most barebone of systems -- equivalent to the current 'Simple'
renderer

## Performance Tradeoffs

One idea that I tried was keeping an entire song's worth of samples in
RAM. This allows for instant-access to the data when a seek occurs, so
there's no time that the waveform display doesn't have data. The current
downside is that the general process is to loop over the sample buffer
for the width of the screen, and draw a line to represent the sample.

This has proven to be taxing at 60fps. It's not as fast as it could be.
In order to make this faster, pre-rendering the entire song to a pixmap
or image canvas, is the next step in time/space tradeoff. I've written
this up, and QImage and QPixmap seem to get very buggy around 47457x68
pixels (about 9MB of memory). The QPixmaps generate tons of X11 errors
about being out of resources. This seems completely unreasonable as apps
like firefox routinely store many hundreds of pixmaps in the X server.
Just the same, this looks like an area where we can't afford to be
relying on a person's X server for good behavior.

I have an idea that is a hybrid of the previous two ideas. I'm going to
jot down a loose spec here. It's basically a pixmap or image that is a
ring-buffer. The width is about 3 or 4 times the width of the waveform
viewer in pixels, and the same height as it. This will hopefully
amortize the cost of drawing per frame in the best case to one bitblt,
second best case, two bitblts, third best case, 2 bitblts and a few line
drawings, and worst case drawing the 'width' of lines, which is the
current 'best' case for the waveform viewer with the draw-lines
approach.

SampleRingBuffer

  - 3-4 times the width of visual waveform viewer
  - keeps track of both a read pointer and write pointer. 
  - the read and write pointer originally start at 0. 
  - per frame, no more than 'width' lines will be drawn onto the buffer.
    
  - EACH FRAME: (assuming forward progression) 
  - 1\) if the read pointer is less than the write pointer, it will
    bitblit a rectangle of width min(WP-RP,width) into the widget
  - 2\) if the read pointer is greater than the write pointer, it will
    bitblit a rectangle of width (bufstart+buflen-RP) into the widget. 
  - 3\) If the width written is less than the width of the widget, and
    the WP \< RP, then loop to the beginning of the buffer and draw a
    rectangle of width min(remaining\_pixels, (wp-bufstart)) into the
    widget. 
  - 4\) If the width written is less than the width of the widget, and
    the WP \> RP, then draw that take in that many samples from the
    sample buffer, and write them at the write pointer, and increment
    the write pointer. 

The end effect here is that, for the first frame, you have to do 'width'
drawlines, but do it in a pixmap, so you save the data. The next frame,
bitblit the portion of the previous frame that was on screen into the
screen, and do drawlines for the amount that is not in the buffer. If
you make the buffer size 4 \* the length of the visual waveform, you
will always be doing some fast memcopy's of the previous image, and then
a couple drawlines, and sometimes not even any drawlines.

A benefit to having a big buffer is that if the user scratches the
waveform back and forth, it will not have to seek backwards and re-draw,
it can go up to 4 times the size of the waveform back before it has to
draw new data.

When a seek occurs, the buffer is invalidated, and on the first frame
after the seek, you have to do 'width' drawlines, but after that one
frame you're only drawing a few lines per frame.

If the user starts playing the audio in reverse, some nasty logic will
have to happen that just flips the direction of the read/write pointers.
