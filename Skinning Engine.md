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

## New On-Disk Format

Given the above requirements, we can begin to hash out the new XML
format:

### Document Root

As in the legacy skinning system, the `<skin>` tag is the root document
element. All valid skins must include a doctype with a reference to the
Mixxx.org skin DTD.

**Example:**

    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE skin SYSTEM "http://mixxx.org/skin.dtd">
    <skin>
      <manifest>..</manifest>
      <style>..</style>
      <layout>..</layout>
    </skin>

### Skin Manifest

The skin manifest contains various metadata about the skin. Only one
manifest is allowed, and it must be the first immediate child of the
`<skin>` tag.

  - Supports basic attributes: title, author, language, description,
    uri, version
  - The URI attribute allows specifying a URI from which to download a
    skin update file. 
  - The update file will contain a list of versions available. 
  - Mixxx may check the skin version against the list of available
    versions and notify the user of an update.
  - Supports attributes. Control system properties that are set to the
    given values on skin load.

**Example:**

    <manifest>
      <title>Rainbow Mixin'</title>
      <author>RJ Ryan</author>
      <language>en</language>
      <description>Mixxxin' on Rainbows</description>
      <uri>http://rustyryan.net/mixxx/skins/rainbow.skin</uri>
      <version>1.0</version>
      <attributes>
        <attribute name="mixxx.master.enabled">false</attribute>
        <attribute name="mixxx.headphone.enabled">false</attribute>
        <attribute name="mixxx.vinylcontrol.enabled">true</attribute>
        <attribute name="mixxx.players.count">4</attribute>
      </attributes>
    </manifest>

### Style

Style controls the styling and presentation of on-screen widgets. The
Style tag can directly embed QSS or provide a relative path to a QSS
file.

**Should styles provided by a skin apply to Mixxx dialogs as well? Pro:
Better skin integration. Con: Potentially poor user experience if the
skin does not work well on the dialogs.**

For more information about QSS, please refer the following:

  - [Qt Style Sheet
    Documentation](http://doc.trolltech.com/latest/stylesheet.html)
  - [QSS Syntax](http://doc.trolltech.com/latest/stylesheet-syntax.html)
  - [QSS Selector
    Types](http://doc.trolltech.com/latest/stylesheet-syntax.html#selector-types)
  - [QSS
    Reference](http://doc.trolltech.com/latest/stylesheet-reference.html)
  - [List of All
    Properties](http://doc.trolltech.com/latest/stylesheet-reference.html#list-of-properties)

**Example:**

    <style>
    /* Can style Mixxx-classes with these selectors: */
    WWidget { color: #FA0; }
    WPushButton { background-color: #FFF; }
    
    /* Can style Qt widget classes like this: */
    QLineEdit { border: 1px solid #333; }
    
    /* Can style individually named elements like this: */
    #Channel1BpmDisplay { font: bold large "Sans Mono"; }
    </style>

#### How can QSS be used to dynamically represent Mixxx controls?

One way that we can use QSS to style dynamic elements of the Mixxx user
interface works like this:

QSS selectors can select based on a property of a widget. Let's say we
have a button widget that represents the End of Track mode. The
`[ChannelX],TrackEndMode` control takes on different values based on the
current end of track mode. The WPushButton that is connected to this
control will provide a [Qt
property](http://doc.trolltech.com/latest/properties.html) named `value`
that indicates the current value of the control. We can style this using
QSS using QSS selectors:

The old skin XML for this button was previously defined as this:

    <PushButton>
        <Tooltip>Helpful text</Tooltip>
        <NumberStates>3</NumberStates>
        <State>
          <Number>0</Number>
          <Pressed>stop.png</Pressed>
          <Unpressed>stop.png</Unpressed>
        </State>
        <State>
          <Number>1</Number>
          <Pressed>next.png</Pressed>
          <Unpressed>next.png</Unpressed>
        </State>
        <State>
          <Number>2</Number>
          <Pressed>loop.png</Pressed>
          <Unpressed>loop.png</Unpressed>
        </State>
        <Pos>X,Y</Pos>
        <Connection>
          <ConfigKey>[ChannelX],TrackEndMode</ConfigKey>
        </Connection>
    </PushButton>

So it's clear the button showed a different PNG based on the state of
the control. The new specification will go something like this:

    <PushButton name="Channel1EndOfTrack">
    ...
    </PushButton>

And its corresponding QSS will be as follows:

    WPushButton#Channel1EndOfTrack {
      background-image: url(eot_bg.png);
    }
    
    /* Show a border while hovering */
    WPushButton#Channel1EndOfTrack:hover {
      border: 1px solid red;
    }
    
    /* Show a different background based on the widget's 'value' property. */
    
    WPushButton#Channel1EndOfTrack[value=0] {
      background-image: url(eot_stop.png);
    }
    
    WPushButton#Channel1EndOfTrack[value=1] {
      background-image: url(eot_next.png);
    }
    
    WPushButton#Channel1EndOfTrack[value=2] {
      background-image: url(eot_loop.png);
    }

### Layout

The layout section is the root description of the skin's layout. Each
layout section is made up of a number of `<window>` tags depending on
how many windows the skin would like to create.

**Example:**

    <layout>
      <window name="Window1">
        <!-- Widgets/layout for window 1 go here -->
      </window>
      <window name="Window2">
        <!-- Widgets/layout for window 2 go here -->
      </window>
    </layout>

### Window

A window is a normal WWidget with all the same attibutes as the base
Mixxx widget.

**Example:**

    <window name="Window 1">
      <size> <!-- Fixed size of 100x100 -->
        <maxsize>100,100</maxsize>
        <minsize>100,100</minsize>
      </size>
      <style>
        <!-- 
        This style is set via http://doc.trolltech.com/latest/qwidget.html#styleSheet-prop
        Is this a good idea? Perhaps it should be considered poor form. 
        -->
        color: red;
      </style>
      <children>
        <!-- Widgets for this window go here. -->
      </children>
    </window>

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
