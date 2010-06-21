# Skinning Engine

Mixxx has used the same old skinning engine for a long time now.
Although the current skinning engine is usable, it is not very flexible.
Developers can discuss their ideas for a new skinning engine on this
page.

## Current System

See description of XML format here: [Creating Skins](creating_skins)

Supported Widgets

  - Push-buttons
  - Multi-state push buttons
  - Sliders
  - horizontal or vertical
  - Text labels
  - hardcoded to duration, track title, bpm, rate, etc
  - Knobs
  - Waveform overview
  - Waveform display
  - VU meter
  - Embed library widget
  - Status light

## Requirements

Base Widget

  - Nameable
  - Tooltip
  - Connections
  - EmitOnDownPress and EmitOnRelease properties (to obviate need for
    double-connections)
  - Choose mouse button.
  - Tab ordering?

Widgets

  - Push button
  - Support pixmaps for each button position
  - Slider 
  - Allow vertical or horizontal orientation 
  - Separate image for slider and knob
  - Knobs
  - Single knob image that is rotated plus background image.
  - Allow specification of 'translation' function (i.e. log-potmeter or
    potmeter)

<!-- end list -->

``` 
* 
```

## Forum discussion

There was a productive discussion that happened in the forums:
<http://mixxx.org/forums/viewtopic.php?f=1&t=729> Please check the
forums for additional information.

## Ideas for Skinning Engines

Feel free to add your cons and pros for any of the ideas to this page

The current ideas are:

## Qt 4 based Skinning Engine

Qt 4 is the cross-platform framework that is used for many things by
Mixxx itself.

For the creation of a skinning system, Qt supports many things: layouts,
style sheets, vector graphics, raster/OpenVG/OpenGL rendering, useful
low-level painting system, XML, animation framework (since 4.6 or as
official add-on), declarative UI technology (since 4.6)...

By combining some of these technologies it should be possible to create
an advanced skinning engine for Mixxx.

#### To investigate

  - Explore the Declarative UI Technology in Qt 4.6 to see if it can
    help in creating a skinning engine.
  - It looks very promising:
    <http://labs.trolltech.com/blogs/category/labs/graphics/kinetic/declarative_ui/>
  - Explore QWidget versus QGraphicsView for layout.
  - How does the performance stack up?
  - QWidgets can be rendered in a QGV, but how does this affect
    performance?

<!-- end list -->

``` 
    * But when the visualization is rendered in OpenGL, we'll probably have to render the whole QGV in OpenGL
* QGV will give us a really cool and flexible UI in combination with the Animation/DUI framework
* QGV will give us fast software-based UI rendering, as well as support for rendering the UI through OpenGL and since Qt 4.6 also OpenVG
* Explore if and how style sheets can help
* Style sheets are very useful to skin stuff like scrollbars and other default widgets
* The more important stuff like buttons should probably be skinned by reimplementing paintEvent, because this gives more possibilities
    * Style sheets may be slower than reimplementing paintEvent - although it has to be investigated to be sure
    * More advanced animations (besides simple hover/overroll effects) cannot be created with style sheets only
```

#### Pro

  - Support pixmap skins (porting of current skins will be easier this
    way, and performance will probably be higher than using SVG)
  - Support SVG skins (for those who want, SVG skins should be an option
    as well
  - Performance may be lower, but we could optionally render SVG as
    pixmaps to improve performance
  - Possibility to implement a layout system (because interface elements
    should not stretch)
  - The window itself should be themable/deformable too. Could be
    achieved by either composite or with a mask (or both)

## Vector-based Skinning Engine

A vector graphics based GUI (like with SVG files) which would allow
dynamic resizing and storage efficiency.

  - [Qt SVG Renderer class
    info](http://doc.trolltech.com/4.5/qsvgrenderer.html#details)

#### Pro

  - Qt supports SVG functionality.

#### Con

  - Interface elements will stretch - a layout system instead would look
    much cleaner and would be more usable on most systems.
  - Current skins will have to be abandoned or recreated using SVG
  - Slow. Must implement pre-rendering and caching layer for any hope of
    this being usable.

# Ideas that are no longer under consideration

## Nui3 based Skinning Engine

Libnui is a cross-platform 3D accelerated GUI library. More information
is available at <http://www.libnui.net/>

#### Pro

  - Examples of software skinned by Nui3 looks great (examples at
    <http://www.libnui.net/>)

#### Con

  - Will take a lot of work to implement, because at the moment Mixxx is
    tightly integrated with Qt
  - User will need OpenGL or DirectX support and a suitable GPU if they
    want a responsive GUI
  - There is a software renderer included, but it is very slow at the
    moment. *Developers are improving it, but it's not a big priority.*
