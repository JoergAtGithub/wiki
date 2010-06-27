Here is a proposal for the new [skinning engine](skinning_engine) based
on Qt4 and Qt Style Sheets.

# On-disk file format

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

### Generic Widget

All widgets (children of WWidget) will have the following properties:

  - objectName (inherited property of QObject)
  - maximumSize (inherited from QWidget)
  - minimumSize (inherited from QWidget)
  - toolTip (inherited from QWidget)
  - whatsThis (inherited from QWidget)
  - [QWidget
    Properties](http://doc.qt.nokia.com/latest/qwidget.html#properties)

All widget declarations will take a form similar to the following:

    <WidgetType name="MyWidget">
      <Tooltip>Helpful text for MyWidget</Tooltip>
      <Size> <!-- Size hints for the widget. Make max the same as min for a fixed size widget. -->
        <MaxSize>100,100</MaxSize>
        <MinSize>10,10</MinSize> 
      </Size>
      <Connections> <!-- Control connections to the widget. -->
        <Connection>
          <Control>mixxx.player1.play_button</Control>
          <EmitOnDownPress>true</EmitOnDownPress>
          <ButtonState>LeftButton</ButtonState>
        </Connection>
      </Connections>
    </WidgetType>

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

### Widget Group

A Widget Group is a container for widgets. It is a normal WWidget and
can have a name. The group can use a Qt layout to manage its children.
Potentially, this should be a subclass of QGroupBox.

The options for layouts are simply the main Qt layouts: VBoxLayout,
HBoxLayout, GridLayout, StackedLayout. **TODO: For things like
GridLayout, adding a widget takes arguments (e.g. row, column). The
example below cannot handle this.**

**Example:**

    <group name="PlayerGroup" layout="VBoxLayout">
      <children>
        <!-- Widgets for this group go here. -->
      </children>
    </group>
