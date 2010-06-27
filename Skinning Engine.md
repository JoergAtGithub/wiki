# Skinning Engine

## Summary and Rationale

**Status**: This specification is **in drafting**. Please feel free to
add comments.

Mixxx has used the same old skinning engine for a long time now.
Although the current skinning engine is usable, it is not very flexible.

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

Metadata/Manifest

  - Include the following metadata:
  - author
  - title
  - description
  - language
  - skin version
  - license
  - update-URL
  - mixxx version required (min/max)
  - suggested screen resolution
  - min screen resolution

Base Widget

  - Nameable
  - Position, Size
  - Potentially offer absolute positioning mode for legacy support, but
    in general deprecate absolute positioning. 
  - Use size-hints (max-min size) instead of single size.
  - Tooltip
  - Connections
  - EmitOnDownPress and EmitOnRelease properties (to obviate need for
    double-connections)
  - Choose mouse button.
  - Tab ordering?
  - Support hovering MIDI-assign. Can we do this with some QSS :hover
    attribute? 

Widget Layout

  - Widget Grouping
  - Nameable
  - Have a size hint and optionally an absolute position.
  - Provide a hide/show-control. Uses the group's name.
  - Layouts
  - Allow a widget group to have a layout assigned to it.
  - Windows
  - Windows are the root of each hierarchy of widgets
  - Widget Templates
  - Ability to specify some template for a widget for saving time,
    sanity.
  - Seems a lot like CSS. Can we use QSS to get the same effect? 

Widgets

  - Buttons
  - Allow multi-state button or push-button.
  - Support pixmaps for each button position
  - Allow non-pixmap buttons. Use QSS to styling.
  - Slider 
  - Allow vertical or horizontal orientation 
  - Separate image for slider and knob
  - Allow non-pixmap sliders. Use QSS for styling.
  - Drop-down Chooser
  - Allow styling via QSS. 
  - No pixmap option, as it's text-only. 
  - Requires [Control 2.0](revamped_control_system), since if you
    connect it to a text control it must know what values it may take
    on. 
  - Knobs
  - Single knob image that is rotated plus background image.
  - Allow specification of 'translation' function (i.e. log-potmeter or
    potmeter)
  - Allow non-pixmap knobs. Use QSS for styling.
  - Library Widget
  - Still a monolithic widget. Don't think it adds value to allow much
    customization here. 
  - Use QSS for all appearance styling.
  - Waveform Widget
  - Still monolithic, but configurable as in current system.
  - Waveform Overview
  - Needs overhaul to be as configurable as the waveform widget.
  - Text labels
  - Make use of Controls to display text instead of hard-coding text.
    (Depends on [Control 2.0](revamped_control_system))
  - Potentially allow scripts to dynamically affect what is shown. 
  - Allow Marquee effect so you can read text that goes out of the
    control.
  - VU Meter
  - Allow QSS styling (how???) or pixmaps.
  - Status light
  - Connects to a control and dynamically switches its pixmap or QSS
    property based on the control's value
  - Sampler Widget
  - Requirements unknown.
  - Effects Widget
  - Requirements unknown. 
  - Potentially with a much better control system we can support neat
    things, e.g. A Traktor like dynamic effect control.

## Skinning Engine Proposals

Given the above requirements, list various proposals for skin formats
here:

  - [Qt4, Qt Style Sheet-based approach](skinning_engine_qt4)

## How QT Quick and QML might be used in QT 4.7.x

It might be possible to describe a Mixxx skin by using pure QML.
According to
<http://doc.qt.nokia.com/4.7-snapshot/qml-extending-tutorial-index.html>
QML can be extended to match our own language concepts. In other words,
we may extend our existing widget classes in a way they can be accessed
by QML,see
<http://doc.qt.nokia.com/4.7-snapshot/declarative-tutorials-extending-chapter1-basics.html>
for a simple example.

Tobias Rafreider has created a branch for that purpose.

More information about Qt Quick and QML may be found on
<http://doc.qt.nokia.com/4.7-snapshot/declarativeui.html>

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

# Ideas that are no longer under consideration

## Vector-based Skinning Engine

\*\*Supporting SVG as an image format does not mean we cannot do the Qt4
based skinning engine approach above. We can support a number of
formats, including SVG. Making an exclusively vector-based skinning
engine is too limiting for skin designers. \*\*

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
