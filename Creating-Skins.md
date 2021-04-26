Skins can change the look and feel of Mixxx. Some skins merely make the
program more aesthetically pleasing while others rearrange elements of
the interface to fit different use-cases.

# Getting started

A skin for Mixxx is basically a folder with various images, a text file
named skin.xml, other XML template files and a [style.qss file](#qss-style).
The skin.xml and template files define all the elements (widgets) of the
skin, what the images are used for and where they are placed on screen.

To create a new skin, navigate to your local [Mixxx skin resource folder](#change-an-existing-skin),
duplicate the directory of the skin you want to base your work on and
rename it. Use the content of the new folder as starting point for your
first skin. Read this page, understand how things were done in the skin
you copied and try to work from there. Familiarity with HTML will have
you feel at home editing the skin.xml.

**You can download the most recent source files for skins from
[Github](https://github.com/mixxxdj/mixxx/tree/master/res/skins), our
code hosting platform.**

It is helpful to run Mixxx in Developer Mode when working on a skin. Use
the `--developer` command line option to start Mixxx in Developer Mode.
A new Developer menu will appear with a Reload Skin item so you do not
have to restart Mixxx to test every change. Also, Developer Mode fills
tooltips with a lot of helpful debugging information. If you do not see
tooltips when you hover your mouse over parts of the skin, go to Options
\> Preferences \> Interface and select "Skin and Library" for the
Tooltip option.

Keep in mind the [Skin Guidelines](Skin%20Guidelines).

### Things to know

##### Positioning

Images are in the .png format and Mixxx does support png transparency.
Element colors are defined in hexadecimal values.  
Element positions are defined with **X,Y** coordinates (from upper left
). Element sizes are defined with **W,H** values (width,heigh). All
values are given in pixels.

[[/media/skinning/creating_skins/mixxx1.9_gui_positioning_outline.png|]]

##### Structure

General structure of the skin.xml. See [Skin.xml in-depth review](#skinxml-in-depth-review) for more in-depth informations on elements and their attributes defined in the skin.xml.

```xml
<!--Comment--><!-- Optional comments (i.e. skin changelog) -->
<!DOCTYPE skin><!-- Doctype declaration -->
<skin><!-- Skin opening tag -->
  <manifest>...</manifest><!-- Manifest describing skin properties (author, title, version, etc.) -->
  <elementname><!-- Elements opening tag -->
    <TooltipId>...</TooltipId><!-- Tooltips to display on mouse-over, available IDs are in src/skin/tooltips.cpp -->
    <Pos>X,Y</Pos><!-- Position on the screen, relative to parent widget -->
    <Size>W,H</Size><!-- Size (depending on the element) -->
    <MinimumSize>W,H</MinimumSize><!-- Minimum Size -->
    <MaximumSize>W,H</MaximumSize><!-- Maximum Size -->
    <SizePolicy>WPolicy,HPolicy</SizePolicy><!-- Size Policy -->
    <options>values(depends)</options><!-- Options(depending on the element) -->
  </elementname><!-- Elements closing tag -->
</skin><!-- Skin closing tag -->
```

### Skin 101

Lets have a look at this simplified example of the Mixxx user interface
(deprecated Outline skin template).  
The various elements of the skin are marked and explained below.

[[/media/skinning/creating_skins/mixxx1.9_gui_explained_outline.png|]]

[1.General](#general)

  - Manifest - specifies information about the skin (title, artist,
    description, version) and allows you to set Mixxx controls when the
    skin is loaded (e.g. enable 4-deck mode).
  - Skin Color Scheme - allows the creation of different [color
    schemes](https://github.com/mixxxdj/mixxx/wiki/Skin-Color-Scheme-Architecture)
    of a skin
  - Library display - Widget holds all your music information,
    playlists, search bar etc.

[2.Visual](#visual)

  - Waveform - shows the loaded tracks waveforms near the playback
    position
  - Waveform overview - shows a waveform visualization of the whole song
  - Volume level display - shows the playback volume of the song /
    master
  - Peak indicator - shows if a songs / master volume is too high

[3.Text](#text)

  - Label - displays a text label
  - Clock - displays the current time
  - Track information - shows some ID3 information of the song ( Name,
    Artist )
  - BPM Information - shows the tempo of the song
  - Musical key - shows the key of the song
  - Playing position / Time remaining - shows current playback position
    or remaining time (click to switch)
  - Pitch rate information - shows how much the song is speed up /
    slowed down (in percent)

[4.Slider](#section-slider)

  - Channel Volume - controls the volume of the selected channel
  - Crossfader - fade between the channels
  - Pitch control - changes the tempo of a song
  - \[InternalClock\], bpm - tempo of the internal master sync clock
    (also viewable as plain text)

[5.Buttons](#section-buttons)

  - Play - plays / pauses a song
  - Cue - places a Cue-point at the current position
  - Hotcue - places a Hotcue-point at the current playback position
  - Looping - places start- and endpoint of a loop , enables the loops
    playback
  - Reverse play - toggles reverse playback during regular playback
  - Fast forward/rewind - seeks trough a song fast in both directions
  - Sync Enabled - Tap to match bpm of playing tracks, or hold to enable
    sync mode.
  - Master - Push to designate an explicit deck master for sync mode.
  - Pitch adjustment - apply fine adjustment to the tempo of a song
  - BPM tap - sets the bpm to the average value of the last 4 taps
  - Key lock - activate pitch-independent time stretch
  - Pitch bend - apply a temporary pitch-bend to the tempo of a song
  - Pre-listen - sends the channel's audio to the Headphones
  - Repeat - repeats track if you go past the end or before the start
  - Frequency Kill - cuts the high, mid and low frequencies

[6.Knobs (Rotary fader)](#section-knobs-rotaryfader-)

  - Master Volume - controls the volume and of the master output
  - Balance - controls the balance (stereo distribution) of the master
    output
  - Headphone volume - controls the volume of the headphone output
  - Headphone mix - controls what you hear on the headphone output
  - Gain - apply extra amplification to a song
  - Channel filter - perform equalization on the high, mid and low
    frequencies

[7.Special nodes (not displayed)](#special-nodes-)

  - TrackProperty - pull advanced informations from tracks and display
    them
  - WidgetGroup - make a group of relatively positioned widgets
  - Splitter - allows proportional splits between WidgetGroup
  - WidgetStack - allows to switch between multiple different widgets to
    occupy a certain space

#### The filters (e.g. blur) used in my svg files are not visible. Why ?

So you created a nice button with a drop shadow blur effect in svg
format, only to find the button is displayed without the drop shadow in
Mixxx? [Qt](https://en.wikipedia.org/wiki/Qt_\(software\)) supports the
[static features](https://www.w3.org/TR/SVGMobile12/feature.html) of SVG
1.2 Tiny. ECMA scripts and DOM manipulation are currently not supported,
see <http://doc.qt.io/qt-5/svgrendering.html>

# How to install a skin

### Install a new skin

Additional skins for Mixxx can be downloaded in the
[skin section of the Mixxx forum](https://mixxx.discourse.group/c/skins/11).

In this example we are going to install the file "NewSkin.zip"

1. Close Mixxx.

2. Create a folder `skins` in the [folder where the Mixxx config file is located](https://github.com/mixxxdj/mixxx/wiki/Finding-the-mixxx.log-file):  
  **Linux**: `~/.mixxx/`  
  **Windows** (Vista and up): `%LOCALAPPDATA%\Mixxx\`  
  **Windows** (XP and below): `%USERPROFILE%\Local Settings\Application Data\Mixxx\`  
  **macOS** (Mixxx 2.2.x and earlier): `~/Library/Application Support/Mixxx`  
  **macOS** (Mixxx 2.3.x): `~/Library/Containers/org.mixxx.mixxx/Data/Library/Application Support/Mixxx`  

3. Download & unzip `NewSkin.zip` and copy the whole unzipped folder `NewSkin` to the new `skins` folder

4. Start Mixxx

5. Open `Options` > `Preferences` > `Interface`, in the `Skin` drop-down menu select `NewSkin`

5. Save preferences with **Apply**.

6. Done, the new skin should now be displayed.

### Change an existing skin

If you want to tweak an existing skin the procedure is the same, except that you pick (and rename) an existing skin folder from the Mixxx resource directory:  
  **Linux**: `/usr/share/mixxx/skins/`  
  **Windows**: `C:\Program Files\Mixxx\SKINS`  
  **macOS**: `/Applications/Mixxx.app/Contents/Resources/skins`  

**Note**: Copy an existing folder, otherwise your changes will be overwritten next time you update Mixxx.

# Skin licensing & copyright

The principles on licensing found on the [Creative Common
Wiki](https://wiki.creativecommons.org/index.php?title=Considerations_for_licensors_and_licensees)
apply for other licenses too.

If you are going to make a skin from scratch , think about which license
to choose for your work. Make sure you have **the rights** to apply the
license.  
Popular choices are [GPL](http://www.gnu.org/licenses/gpl.html) and
[Creative Common](http://creativecommons.org/) license.

**The skins license must be compatible with the
[DebianFreeSoftwareGuidelines](http://wiki.debian.org/DFSGLicenses) or
they can not be distributed with Mixxx. **  
If you are going to make a skin based on others work, make sure you
comply with their license terms. If you are not sure, ask the original
author.

Add the license in the [manifest](creating_skins#skin_manifest) at the
beginning of skin.xml (see
[example](https://github.com/mixxxdj/mixxx/blob/master/res/skins/Deere/skin.xml)).

Further reads:

  - [Which CC license to choose](http://creativecommons.org/choose/)
  - [Non-commercial licenses vs open
    licenses](http://www.appropedia.org/Non-commercial_licenses_vs_open_licenses)
  - [Frequently Asked Questions about the GNU
    GPL](http://www.gnu.org/licenses/gpl-faq.html)

# Tools

  - Free Code editors - Cross-platform ([Visual Code
    Studio](https://code.visualstudio.com/)), ([Atom](https://atom.io/))
  - Free Images editors - Online
    ([Photopea](https://www.photopea.com/),
    [Pixlr](http://www.pixlr.com/)), Windows
    ([Paint.net](http://www.getpaint.net/)) macOS
    ([Pixelmator](http://www.pixelmator.com/) -trial-), Linux (Gimp,
    Inkscape)
  - Free color tools - Online ([Color Palette
    Generator](http://bighugelabs.com/colors.php),
    [Colorblender](http://www.colorblender.com/) , [Paletton, the color
    scheme designer](http://paletton.com/))
  - Free knob tools - Cross-platform
    ([JKnobman](http://www.g200kg.com/en/software/knobman.html))

# Skin.xml in-depth review

In this section all elements and the values of their keys are explained
with examples.  
Open up the skin.xml in the skin folder you duplicated earlier with your
favorite [text editor](#tools) and get started :-)

## General

### Skin Manifest

The skin manifest section tells Mixxx details about the skin:

```xml
<manifest>
  <title>...</title>
  <author>...</author>
  <version>...</version><!-- Skin version (not the Mixxx version) -->
  <description>...</description>
  <language>en</language><!-- Skin language (if language-independent, omit or put *) -->
  <license>...</license>
  <attributes>
    <!-- Set "[Master],num_decks" config key to 4 when skin is loaded.-->
    <attribute config_key="[Master],num_decks">4</attribute>
    <attribute config_key="[Master],num_samplers">16</attribute>
    <attribute config_key="[Master],num_preview_decks">1</attribute>
    
    <!-- Persist a custom skin config key "[Skin],show_some_widget". 
         This allows for hiding/showing/highlighting widgets. (see <Connection> )-->
    <attribute persist="true" config_key="[Skin],show_some_widget">1</attribute>
  </attributes>
</manifest>
```

The main part of the manifest that is the `<attributes>` section.  Attributes
can specify changes to Mixxx controls that should be executed when the skin is
loaded.

For example, Mixxx defaults to 2-decks in its mixing engine but when you load a
skin that supports 4-decks, the skin can specify that the control
`[Master],num_decks` should be set to 4 (as in the above example). This will
enable a 3rd and 4th deck in Mixxx's engine for the skin to interact with.  This
attribute list can change any Mixxx control but will only take effect when the
skin is loaded.

Attributes can also be used to persist settings specific to the skin itself.
Config keys in the form `[GroupFoo],control_bar` (see [control
naming](https://github.com/mixxxdj/mixxx/wiki/developer_guide_control#control-naming))
can be set or unset in conjunction with [`<Connection>`](#connection)
 in order to show, hide or highlight widgets particular to the skin.


### QSS Style

To specify how skins look (for example colors and text sizes), skins use
a [Qt Style Sheet](http://doc.qt.io/qt-4.8/stylesheet.html) (QSS) file
which is similar to a [Cascading Style
Sheet](https://developer.mozilla.org/en-US/docs/Web/CSS) (CSS) file used
to specify how web pages look. The QSS file is linked to the skin XML
with a \<Style\> element that is a child of the root \<skin\> element:
```xml
    <skin>
      <manifest>
        <!-- skin manifest goes here -->
      </manifest>
    
      <Style src="skin:style.qss"
             src-windows="skin:style-windows.qss"
             src-mac="skin:style-mac.qss"
             src-linux="skin:style-linux.qss"/>
    
      <!-- rest of skin goes here -->
    </skin>
```
All the skins included in Mixxx name the QSS file as `style.qss` in the
root directory of the skin. Any name with the `*.qss` or `*.css` file
extension will work. Optionally, you can add up to three additional QSS
files to your skin directory, e.g. to work around platform-dependent
quirks in styling: `src-windows="..."`, `src-mac="..."` `and
src-linux="..."`

**Note:** You can add style sheets to [color
schemes](https://github.com/mixxxdj/mixxx/wiki/Skin-Color-Scheme-Architecture),
as well. They are added to the style sheets described above and will
override attributes in case of conflicts.

Widgets are selected in QSS by the name of their widget type (the "Mixxx
internal name" column in the table below) or by a defined name. To
define a name for a widget, use the `<ObjectName>` element. For example:
```xml
    <WidgetGroup>
      <ObjectName>SomeWidgetGroup</ObjectName>
      <Children>
        <!-- A group of widgets you want to apply style to go here -->
      </Children>
    </WidgetGroup>
```
This is similar to setting an `id` attribute on an element in HTML
except that multiple widgets can share the same `<ObjectName>`. To style
the above `<WidgetGroup>` in QSS, you would select it with `#`. For
example:
```css
    #SomeWidgetGroup {
      background-color: black;
    }
```
Knowing what options are available to style is tricky and it involves
knowing what Qt widget the associated Mixxx widget derives from.

Handy resources:

  - [Qt Style Sheet
    Documentation](https://doc.qt.io/archives/qt-4.8/stylesheet.html)
  - [Qt Style Sheet
    Syntax](https://doc.qt.io/archives/qt-4.8/stylesheet-syntax.html)
  - [Qt Style Sheet Widget
    Reference](https://doc.qt.io/archives/qt-4.8/stylesheet-reference.html)
    -- tells you what widgets support which properties.

Here is a potentially out-of-date list of which Mixxx widgets derive
from which Qt widgets. If not listed, the widget inherits from
`QWidget`.

| Skin Tag          | Mixxx Internal Name   | Qt Widget                     |
| ---------------   | -------------------   | ---------------------------   |
| `WidgetStack`     | `WWidgetStack`        | `QStackedWidget`              |
| `WidgetGroup`     | `WWidgetGroup`        | `QGroupBox`                   |
| (none)            | `WTrackTableView`     | `QTableView`                  |
| (none)            | `WLibraryTableView`   | `QTableView`                  |
| `Library`         | `WLibrary`            | `QStackedWidget`              |
| `LibrarySidebar`  | `WLibrarySidebar`     | `QTreeView`                   |
| `SearchBox`       | `WSearchLineEdit`     | `QLineEdit`                   |
| `Spinny`          | `WSpinny`             | `QGLWidget`                   |
| `Visual`          | `WWaveformViewer`     | `QWidget`                     |
| `NumberRate`      | `WNumberRate`         | `QWidget` with a QLabel child |
| `NumberPos`       | `WNumberPos`          | `QWidget` with a QLabel child |
| `NumberBpm`       | `WNumber`             | `QWidget` with a QLabel child |
| `Number`          | `WNumber`             | `QWidget` with a QLabel child |
| `Label`           | `WLabel`              | `QWidget` with a QLabel child |
| `Text`            | `WTrackText`          | `QWidget` with a QLabel child |
| `TrackProperty`   | `WTrackProperty`      | `QWidget` with a QLabel child |
| `Time`            | `WTime`               | `QWidget` with a QLabel child |
| `Key`             | `WKey`                | `QWidget` with a QLabel child |
| `Splitter`        | `WSplitter`           | `QSplitter`                   |
| `DefineSingleton` | `WSingletonContainer` | `QWidget`                     |
| `EffectSelector`  | `WEffectSelector`     | `QComboBox`                   |

### Using Variables

You can use variables throughout the skin templates for various
purposes, as well as in [color
schemes](https://github.com/mixxxdj/mixxx/wiki/Skin-Color-Scheme-Architecture),
to set channel numbers, effect numbers, `<ObjectName>`s or to define
colors for widgets, just to name a few.  

Set variables like this: 
```xml
<SetVariable name="veryDescriptiveName">String</SetVariable>
```
and recall variables like this:
```xml
<Variable name="veryDescriptiveName"/> <!-- replaced with String -->
```

Global variables are inherited by all child templates. Scheme specific
variables should be set under `<Scheme>` nodes whereas other global variables
in `skin.xml` should be set directly after the first `<Children>` opening tag,
before any other template is loaded.

Variables can also be passed to templates explicitly.  For example, here
we load a deck template, specifying the channel number, side and
background color it should use:

```xml
<Template src="skin:deck_container.xml">
   <SetVariable name="side">Left</SetVariable>
   <SetVariable name="channum">1</SetVariable>
   <SetVariable name="SignalBgColor">#0a0a0a</SetVariable>  <!-- dark grey -->
</Template>
```

The variables defined above might be used in the template to set up a waveform overview
widget for example:

```xml
  <!-- deck_container.xml -->
  <Overview>
    <Size>...</Size>
    <Objectname>Overview<Variable name="side"/></Overview> <!--  <Objectname>OverviewLeft</Overview> -->
    ...
    <Channel><Variable name="channum"/></Channel> <!--  <Channel>1</Channel> -->
    <BgColor><Variable name="SignalBgColor"/></BgColor> <!--  <BgColor>#0a0a0a</BgColor> -->
    ...
  </Overview>
```

**Note:** Variables **cannot** be used within tags or within values:
```xml
<Template src="skin:deck_container_<Variable name="side"/>.xml"/> <!-- Wrong -->
<Template <SetVariable name="Alignment">left|top</SetVariable>src="skin:library.xml"/> <!-- Wrong... -->
```

### Properties Common to All Widgets

Every skin widget is declared in a block with an opening XML tag and a
closing tag. For example, this block defines a musical key widget that
shows the current key of a playing deck:

```xml
    <Key>
        <TooltipId>visual_key</TooltipId>
        <Pos>X,Y</Pos>
        <Size>W,H</Size>
        <Connection>
            <ConfigKey>[ChannelX],visual_key</ConfigKey>
        </Connection>
    </Key>
```

Sub-tags like the `<Size>` tag tell Mixxx how it should size, style and
layout the widget. There are certain sub-tags that are common to all
widgets and behave in the same way regardless of the widget type.

#### \<Pos\>

`<Pos>` tags tell Mixxx where to position a widget. The position is
relative to the widget's parent. For example, if the position is `0,50`
then this means position the widget 0 pixels from the horizontal
location (left edge) of the parent widget and 50 pixels from the vertical location (top edge)
of the widget's parent.

| Examples: |   |
| ----- | ------ |
| `<Pos>0,50</Pos>` | 0 pixels from top left edge of the parent, 50 pixels from the top edge |
| `<Pos>50,0</Pos>` | 50 pixels from the horizontal position of parent, 0 pixels from the vertical position |
| `<Pos>50,50</Pos>` | 50 pixels from the horizontal position of parent, 50 pixels from the vertical position |

#### \<Size\>

`<Size>` tags tells Mixxx what size to make a widget. The size tag has a lot of
historical baggage associated with it because it has been around since the first
version of Mixxx and has a bunch of hacks added to it.

It is formatted as the horizontal size and the vertical size in pixels separated
by a comma. You can also specify a size policy as shown below, however later
versions of Mixxx add the [`<SizePolicy>`](#\<sizepolicy\>) tag for this. 

| Examples: |   |
| ----- | ------ |
| `<Size>100,50</Size>` | 100 pixels wide and 50 pixels tall. |
| `<Size>100me,50p</Size>` | 100 pixels wide and 50 pixels tall. The horizontal size policy is MinimumExpanding and the vertical policy is Preferred. |
| `<Size>100me,50</Size>` | 100 pixels wide and 50 pixels tall. The horizontal size policy is MinimumExpanding. |
| `<Size>me,e</Size>` | The horizontal size policy is MinimumExpanding and the vertical size policy is Expanding. No explicit size is set. |

#### \<MinimumSize\>

_New in Mixxx 2.00.0_

`<MinimumSize>` tags tell Mixxx the smallest size a widget should be.  The
widget will never be resized to be smaller than this size.

It is formatted as the minimum horizontal size and the minimum vertical size in
pixels separated by a comma. A value of -1 for a dimension means no minimum in
that dimension.

| Examples: |   |
| ----- | ------ |
| `<MinimumSize>100,50</MinimumSize>` | minimum width 100, minimum height 50 |
| `<MinimumSize>200,-1</MinimumSize>` | minimum width 200, no minimum height |
| `<MinimumSize>-1,300</MinimumSize>` | no minimum width, minimum height 300 |

#### \<MaximumSize\>

_New in Mixxx 2.00.0_

`<MaximumSize>` tags tell Mixxx the largest size a widget should be. The
widget will never be resized to be larger than this size.

It is formatted as the maximum horizontal size and the maximum vertical size in
pixels separated by a comma. A value of -1 for a dimension means no maximum in
that dimension.

Examples:
| value | result |
| ----- | ------ |
| `<MaximumSize>100,50</MaximumSize>` | maximum width 100, maximum height 50 |
| `<MaximumSize>200,-1</MaximumSize>` | maximum width 200, no maximum height |
| `<MaximumSize>-1,300</MaximumSize>` | no maximum width, maximum height 300 |

#### \<SizePolicy\>

_New in Mixxx 2.00.0_

`<SizePolicy>` tags tell Mixxx how widgets should grow or shrink based on the
available space. Size policy refers to the Qt
[QSizePolicy](https://doc.qt.io/qt-4.8/qsizepolicy.html#Policy-enum).

| SizePolicy       | Skin Abbreviation | What it does |
| ---------------- | ----------------- | ------------ | 
| Fixed | f | The size in the given dimension is fixed and should not grow or shrink. |
| Minimum | min | The widget size in this dimension is the minimum it should be. It can grow but will not be smaller than this. |
| Maximum | max | The widget size in this dimension is the maximum it should be. It can shrink but will not be larger than this. |
| Preferred | p | The widget size in this dimension is the preferred size. It can be shrunk and still be useful. It can grow but there is no advantage to it growing. |
| Expanding | e | The widget size in this dimension can be shrunk and still be useful. The widget can make use of extra space in this dimension so it should receive as much space as possible. |
| MinimumExpanding | me | The widget size in this dimension is the minimum it should be. The widget can make use of extra space in this dimension so it should receive as much space as possible. |
| Ignored | i | The widget size in this dimension is ignored. The widget will get as much space as possible. |

The `<SizePolicy>` property is formatted as the skin abbreviation (from the
above table) for the horizontal size and the skin abbreviation for the vertical
size policy separated by a comma.

| Examples: | |
| ------------------------------------ | ------------ |
| `<SizePolicy>f,min</SizePolicy>` | Fixed horizontal, Minimum vertical |
| `<SizePolicy>me,me</SizePolicy>` | MinimumExpanding for both horizontal and vertical |
| `<SizePolicy>p,f</SizePolicy>` | Preferred horizontal, Fixed vertical |

#### \<TooltipId\>

`<TooltipId>` tags indicate what tooltip Mixxx should use for the widget. We
used to embed tooltips directly into skins but then we found this was
impractical to keep up to date and translate into different languages. As a
result, we have created a list of standard tooltips that you can use in most
cases.

The `<TooltipId>` tag tells Mixxx to use an existing tooltip that is built into
Mixxx.

For an up to date list of tooltips, see
[src/skin/tooltips.cpp](https://github.com/mixxxdj/mixxx/blob/master/src/skin/tooltips.cpp)
and look at all the `add("some_tooltip_id")` lines in the file. You'll use
whatever `some_tooltip_id` actually is as shown below:

| Examples:                              |                                                       |
| -------------------------------------- | ----------                                            |
| `<TooltipId>track_artist</TooltipId>`  | Use the `track_artist` tooltip from the tooltip file. |
| `<TooltipId>eject</TooltipId>`         | Use the `eject` tooltip from the tooltip file.        |

#### \<Tooltip\>

If no existing tooltip meets your needs, you can create a custom tooltip
using the `<Tooltip>` tag.

| Examples: | |
| ----------- | --- |
| `<Tooltip>My Custom Tooltip</Tooltip>` | Use the phrase "My Custom Tooltip" as the widget tooltip. |

Translation or internationalization of these tooltips is not currently
possible, so avoid using them unless really necessary.

#### \<Connection\>

The connection block is a means for widgets to interact with Mixxx's
[control system](https://github.com/mixxxdj/mixxx/wiki/developer_guide_control).

It requires the `<ConfigKey>` tag to specify the control to be bound to the
widget.

If no further tags are present, the widget is bound on its default connection.
For example a `<PushButton>` or a `<Knob>` will update the control specified by
 `<ConfigKey>` with their state as it changes.

The following optional tags are also accepted within a `<Connect>` block:

| Tag              |                                                  |
|------------------|--------------------------------------------------|
| `<BindProperty>` | specify a widget property to bind the control to |
| `<Transform>`    | transform the value of the bound control         |


`<BindProperty>` accepts any property of the underlying QWidget but was testet with only one of the following two properties:

* `visible` displays the widget when the value of the config key is 1
* `highlight` apply a qss style to the widget based on the config key value:
 
  For example, for a widget with `<ObjectName>Foo</ObjectName>`, when 
  `<ConfigKey>`'s values is `N`, apply the QSS defined by `#Foo[highlight="N"] {...}` to the widget.

A `<Transform>` block can accept the following tags:

| Tag                    | Config Key Value | Transformed Value |
|------------------------|------------------|-------------------|
| `<Invert/>`            | value            | -value            |
| `<Not/>`               | value            | !value            |
| `<Add>n</Add>`         | value            | value + `n`       |
| `<IsEqual>n</IsEqual>` | value            | value == `n`      |

Illustratory example (look at existing skins for actual use cases as they're more complex):
```xml
<!-- Show the label below when pressed -->
<PushButton>
  <NumberStates>1</NumberStates>
  <Size>me,me</Size>
  <State>
    <Number>0</Number>
    <Text>Show</Text>
  </State>
  <Connection>
    <ConfigKey>[Foo],show</ConfigKey>
  </Connection>
</PushButton>


<Label>
  <Size>me,me</Size>
  <Text>Hello</Text>
  <Connection>
    <ConfigKey>[Foo],show</ConfigKey>
    <BindProperty>visible</BindProperty>
  </Connection>
</Label>
```

In Mixxx 2.3, to avoid unnecessary GUI updates from frequent changing COs, the resulting property value is only written once.

### Library display

The library manages all of your music files. This is where you can find
the tracks you want to play and load them into a deck or sampler.

The library typically consist of:

  - Library sidebar: Contains different collections of music, and let
    you browse for files.
  - Library table: The track list view displays the tracks in those
    collections.
  - Library searchbox: The search function filters the currently
    displayed list (e.g. a playlist, a crate, or even the whole library)
    for tracks that match your search query.

The following example uses [`splitters`](#splitter) to implement a simple
library with the above elements:

```xml
<WidgetGroup>
  <Layout>vertical</Layout>
  <Children>
    <WidgetGroup>
      <Layout>vertical</Layout>
      <Children>
        <Splitter>
          <Orientation>horizontal</Orientation>
          <SizePolicy>me,me</SizePolicy>
          <Collapsible>0,0</Collapsible>
          <Children>
            <Splitter>
              <Orientation>vertical</Orientation>
              <Collapsible>0,0</Collapsible>
              <Size>f, f</Size>
              <Children>
                <!-- The library searchbox -->
                <SearchBox></SearchBox>
                
                <!-- The library sidebar -->
                <LibrarySidebar></LibrarySidebar>
              </Children>
            </Splitter>
            
            <!-- The library table showing all your tracks -->
            <Library>
              <Size>me, me</Size>
              <ShowButtonText>false</ShowButtonText>
            </Library>
          </Children>
        </Splitter>
      </Children>
    </WidgetGroup>
  </Children>
</WidgetGroup>
```

## Visual

### Waveform

The waveform is a composite element which is central to most user interfaces. It
displays the current play position scrolling through a track's waveform in real
time as audio playback occurs.

It is highly customizable and can be set with various different color
values etc. for most of its constituent elements. It can also be orientated
vertically or horizontally.

```xml
<Visual>
  <TooltipId>waveform_display</TooltipId>
  <Channel>N</Channel>
  <BgColor>#</BgColor>
  <BgPixmap>optional_custom_background.png</BgPixmap>
  <Orientation>X</Orientation> <!-- horizontal (default) or vertical) -->
  <Align>X</Align> <!-- centered (default), bottop or top (if horizontal), 
                                            left or right (if vertical) -->
                                            
  <!-- Color values for various frequencies -->                                           
  <SignalColor>#</SignalColor> 
  <SignalLowColor>#</SignalLowColor>
  <SignalMidColor>#</SignalMidColor>
  <SignalHighColor>#</SignalHighColor>
  <SignalRGBLowColor>#</SignalRGBLowColor>
  <SignalRGBMidColor>#</SignalRGBMidColor>
  <SignalRGBHighColor>#</SignalRGBHighColor>
  <BeatColor>#</BeatColor> <!-- Beatgrid color -->
  <EndOfTrackColor>#</EndOfTrackColor> <!-- The overlay displayed when a track's about to end-->
  <AxesColor>#</AxesColor> <!-- static horizontal line -->
  <PlayPosColor>#</PlayPosColor> <!-- static vertical line -->
  
  <!-- Customize various marks on the waveform (SEE BELOW) -->
  <DefaultMark>
    ...
  </Mark>
  <Mark>
    ...
  </Mark>
  <MarkRange>
    ...
  </MarkRange>
</Visual>
```

#### Marks

Several marks are made on waveforms for for cue points, loop markers, hot cues etc.
They share many of the same basic options which you can use to customize them:

**The cue point:**
```xml
<Visual>
  ...
  <Mark>
    <Control>cue_point</Control> <!-- max one per channel -->
    <Pixmap>option_custom_marker.png</Pixmap> <!-- optional override of the default triangle -->
    <Text>CUEPOINT</Text> <!-- when no custom marker is used -->
    
    <!-- Defines where text is positioned:
         X = left, hcenter or right
         Y = top or vcenter or bottom
         Note: center can be used as a shorthand for hcenter or vcenter. -->
    <Align>X|Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
  </Mark>
  ...
</Visual>
```


**Hot cues:**

```xml
<Visual>
  ...
  <DefaultMark>
    <Pixmap>optional_custom_marker.svg</Pixmap>
    <Align>X|Y</Align>
    
    <!--The below aren't used in Mixxx 2.3 as hotcues are customised
        individually through their context menus -->
    <Color>#</Color>
    <TextColor>#</TextColor>
    <Text> %1 </Text>
  </DefaultMark>
  ...
</Visual>
```

**Loops:**
```xml
<Visual>
  ...
  <Mark>
    <Control>loop_start_position</Control>
    <Pixmap>optional_custom_marker.png</Pixmap>
    <Text>LOOP OUT</Text>
    <Align>X|Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
  </Mark>
  <Mark>
    <Control>loop_end_position</Control>
    <Pixmap>optional_custom_marker.png</Pixmap>
    <Text>LOOP OUT</Text>
    <Align>X|Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
  </Mark>
  <!-- Customize the loop overlay on the area from the start to end position -->
  <MarkRange>
    <StartControl>loop_start_position</StartControl>
    <EndControl>loop_end_position</EndControl>
    <EnabledControl>loop_enabled</EnabledControl>
    <Color>#</Color>
    <Opacity>0.8</Opacity>
    <DisabledColor>#</DisabledColor>
    <DisabledOpacity>0.5</DisabledOpacity>
  </MarkRange>
  ...
</Visual>
```

**Intro/Outro marks and overlays:**

Similar to the loop example above, Mixxx 2.3 adds separate intro and outro
controls which have their own marks to delineate intro and outro sections:

```xml
<Visual>
  ...
  <!-- Outro marks are exactly the same, just replace intro_* for outro_* -->
  <Mark>
    <Control>intro_start_position</Control>
    <Text>START</Text>
    <Align>X|Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
  </Mark>
  <Mark>
    <Control>intro_end_position</Control>
    <Text>END</Text>
    <Align>X|Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
  </Mark>
  <MarkRange>
    <StartControl>intro_start_position</StartControl>
    <EndControl>intro_end_position</EndControl>
    <Color>#0000FF</Color>
    <Opacity>0.1</Opacity>
  </MarkRange>
  ...
</Visual>
```

### Waveform Overview

The waveform overview is probably the most important visual element used by a
DJ. It shares many of the same configuration options as the visual waveform
explained above, including signal colors and marks.

```xml
<Overview>
  <TooltipId>waveform_overview</TooltipId>
  <Channel>X</Channel>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <BgColor>#</BgColor>
  <BgPixmap>optional_custom_background.png</BgPixmap>
  
  <!-- Color values for various frequencies (low, mid, high fallback to
       SignalColor if they're not provided) -->                                           
  <SignalColor>#</SignalColor>
  <SignalLowColor>#</SignalLowColor>
  <SignalHighColor>#</SignalHighColor>
  <SignalLowColor>#</SignalLowColor>
  <EndOfTrackColor>#</EndOfTrackColor> <!-- Overlay shown at end of track -->
  <PlayedOverlayColor>#</PlayedOverlayColor> <!-- Overlay shown over played area -->
  <Orientation>X</Orientation> <!-- horizontal (default) or vertical -->
  <PlayPosColor>#</PlayPosColor>
  <DefaultMark>
  ... 
  </DefaultMark>
  <MarkRange>    <!-- See the previous example -->
  ...
  </MarkRange>
  <Mark>
  ...
  </Mark>
  <Connection><!-- connect to the playposition control of the channel -->
    <ConfigKey>[ChannelX],playposition</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
  </Connection>
</Overview>
```

### Spinning vinyl image (Spinny)
The spinny can be configured to display a spinning image (over optional cover
art) when a track is playing.

```xml
<Spinny>
  <TooltipId>spinny</TooltipId>
  <Channel>X</Channel>
  <Size>W,H</Size>
  <!-- The image sets the overall size unless scalemode="STRETCH" is set -->
  <PathBackground scalemode="STRETCH">background.svg</PathBackground>
  <!-- Used to mask the cover art (e.g., with a circle so it looks like a record) -->
  <PathMask scalemode="STRETCH">mask.svg</PathMask>
  <!-- Shown as the spinning top layer, mostly a bar-like path like a sticker on vinyls -->
  <PathForeground>foreground.svg</PathForeground>
  <!-- Additional spinning layer for indicating the Slip mode position -->
  <PathGhost>foreground_ghost.svg</PathGhost>
  <ShowCover>true</ShowCover>
</Spinny>
```

### Volume level display
```xml
<VuMeter>
  <TooltipId>channel_VuMeter</TooltipId>
  <!-- Main image shown as top layer -->
  <PathVu>active.png</PathVu>
  <!-- Background image shown as bottom layer -->
  <PathBack>default.png</PathBack>
  <Pos>X,Y</Pos>
  <Horizontal>false</Horizontal>
  <!-- Size of peak (in pixels); cropped from top of image defined in <PathVu>,
       default is 5 -->
  <PeakHoldSize>5</PeakHoldSize>
  <!-- Time a peak is displayed (in ms), default is 400 -->
  <PeakHoldTime>400</PeakHoldTime>
  <!-- Time a peak falls down (in ms), default is 20 -->
  <PeakFallTime>80</PeakFallTime>
  <!-- Number of steps (in pixels) a peaks falls down in <PeakFallTime>, Default is 1 -->
  <PeakFallStep>5</PeakFallStep>
  <Connection>
    <!-- Defines connected Channel & Stereo-balance (X = Channel1 .. 4 or
        Master), (Y= VuMeter or VuMeterL or VuMeterR) -->
    <ConfigKey>[X],Y</ConfigKey>
  </Connection>
</VuMeter>
```

### Volume peak indicator
```xml
<StatusLight>
  <TooltipId>PeakIndicator</TooltipId>
  <!-- Main image shown as top layer -->
  <PathVu>active.png</PathVu>
  <!-- Background image shown as bottom layer -->
  <PathBack>default.png</PathBack>
  <Pos>X,Y</Pos>
  <Connection>
    <!-- Defines connected Channel (X = Channel1 .. 4 or Master) -->
    <ConfigKey>[X],PeakIndicator</ConfigKey>
  </Connection>
</StatusLight>
```

## Text

### Label

A simple text label widget:
```xml
<Label>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <Text>Hello</Text>
</Label>
```

### Clock

A widget to display the current time:
```xml
<Time>
  <TooltipId>time</TooltipId>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <ShowSeconds>false</ShowSeconds> <!-- false (default) or true -->
  
  <ClockFormat>24</ClockFormat> <!-- DEPRECATED (defaults to locale) -->
  
  <!-- Overrides ClockFormat. Use QTime::toString expressions 
       see: https://doc.qt.io/qt-5/qtime.html#toString -->
  <CustomFormat>...</CustomFormat>
</Time>
```

### TrackProperty

Used to display track information:

```xml
<TrackProperty>
  <TooltipId>track_title</TooltipId>
  <SizePolicy>me,min</SizePolicy>
  <Property>title</Property>
  <Channel>X</Channel>
  <Elide>right</Elide>
</TrackProperty>
```

The following are some options that can be used with the `<Property>` tag:
- artist            
- title             
- album             
- albumArtist       
- genre             
- composer          
- grouping          
- year              
- track_number      
- track_total       
- times_played      
- comment           
- durationFormatted 
- info              

### BPM display

Used to display the BPM of a track:

```xml
<NumberBpm>
  <TooltipId>visual_bpm</TooltipId>
  <Channel>X</Channel>
  <Connection>
    <ConfigKey>[ChannelX],visual_bpm</ConfigKey>
  </Connection>
</NumberBpm>
```

### Musical key display
Displays the tracks key (in the notation set in Mixxx's preferences):

```xml
<Key>
  <TooltipId>visual_key</TooltipId>
  <DisplayCents>true</DisplayCents> <!-- false (default) or true) -->
  <Connection>
    <ConfigKey>[ChannelX],visual_key</ConfigKey>
  </Connection>
</Key>
```

### Playing position / Time remaining

|                                                                                                                                                                                                                                                |  |                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | ---------------------------------------------------------------------------------------------------------------- |
| `<NumberPos>
  <TooltipId>track_time</TooltipId>
  <Channel>X</Channel>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <NumberOfDigits>6</NumberOfDigits>
  <Connection>
  <ConfigKey>[ChannelX],playposition</ConfigKey>
  </Connection>
</NumberPos>` |  | `


Defines connected Channel (X = 1 or 2)




?

Must be same value as under <Channel> above, (X = 1 or 2)



` |

### Recording duration

_New in Mixxx 2.1_

|                                                                                                                     |  |                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------- |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<RecordingDuration>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <InactiveText>foo</InactiveText>
 </RecordingDuration>
` |  | `
Displays the duration of the running recording.
Defines the element position
Defines the element size
Custom text to be displayed when recording is inactive/stopped, default is “–:–”


` |

### Pitch rate display

|                                                                                                                                                                                                        |  |                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<NumberRate>
  <TooltipId>rate_display</TooltipId>
  <Channel>X</Channel>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <Connection>
  <ConfigKey>[ChannelX],rate</ConfigKey>
  </Connection>
</NumberRate>
` |  | `


Defines connected Channel (X = 1 or 2)




Remove the whole <Connection> </Connection> block for Mixxx v1.10+, needed in older versions
Must be same value as under <Channel> above, (X = 1 or 2)



` |

### dB display

_New in Mixxx 2.00_

|                                                                                                                                        |  |                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------- |  | --------------------------------------------------------------------------------------------------------------- |
| `<NumberDb>
  ...
  <Text>Gain %1 dB</Text>
  <Connection>
    <ConfigKey>[Channel1],pregain</ConfigKey>
  </Connection>
</NumberDb>
` |  | `


Optional Text. %1 is replaced by the bB value.
If this is missing the value is displayed
like "-39 dB"



` |

## Section: Slider

### Channel Volume

|                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SliderComposed>
  <TooltipId>channel_volume</TooltipId>
  <Handle>handle.png</Handle>
  <Slider>slider.png</Slider>
  <Pos>X,Y</Pos>
  <Horizontal>false</Horizontal>
  <Connection>
    <ConfigKey>[ChannelX],volume</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
  </Connection>
</SliderComposed>` | `


Slider image (knob) which can de dragged with mouse
Slider background image the <Handle> moves up and down on

Orientation (false or true, means vertical or horizontal)

Defines connected Channel (X = 1 or 2 )
Can be omitted in Mixxx >= 2.00



` |

### Crossfader

|                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SliderComposed>
  <TooltipId>crossfader</TooltipId>
  <Handle>handle.png</Handle>
  <Slider>slider.png</Slider>
  <Pos>X,Y</Pos>
  <Horizontal>true</Horizontal>
  <Connection>
    <ConfigKey>[Master],crossfader</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
  </Connection>
</SliderComposed>` | `


Slider image (knob) which can de dragged with mouse
Slider background image the <Handle> moves left and right on

Orientation (false or true, means vertical or horizontal)

Use always default value
Can be omitted in Mixxx >= 2.00



` |

### Pitch control

|                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SliderComposed>
  <TooltipId>rate</TooltipId>
  <Handle>handle.png</Handle>
  <Slider>slider.png</Slider>
  <Pos>X,Y</Pos>
  <Horizontal>false</Horizontal>
  <Connection>
    <ConfigKey>[ChannelX],rate</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
  </Connection>
</SliderComposed>` | `


Slider image (knob) which can de dragged with mouse
Slider background image the <Handle> moves up and down on

Orientation (false or true, means vertical or horizontal)

Defines connected Channel (X = 1 .. 4 )
Can be omitted in Mixxx >= 2.00



` |

## Section: Buttons

**Hint:**  
The *\<NumberStates\>* key means "number of states" for the respective
element (Buttons or Knobs/Rotary Fader).  
For example a [Repeat](creating_skins#repeat) button is a 2-state button
(off/activated).  
The *\<Number\>* key identifies the index of the *\<State\>* block. Each
time you click on one of these multi-state buttons, it flips to the next
state.

The *\<EmitOnDownPress\>* key determines when Mixxx will get feedback
when the button goes down or/and when it comes up.  
If you compare that with a regular push button in your OS, the button
triggers only when you release the button (not when you press it). See
[Hotcue](creating_skins#hotcue) for example.

The *\<ButtonState\>* key tells Mixxx that the given connection should
be triggered when that particular mouse button (left or right) is down.

### Recording

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>???</TooltipId>
  <NumberStates>3</NumberStates>
  <LeftClickIsPushButton>true</LeftClickIsPushButton>
  <RightClickIsPushButton>true</RightClickIsPushButton>
  <State>
    <!-- RECORD OFF -->
    <Number>0</Number>
    <Pressed>btn_record_over.png</Pressed>
    <Unpressed>btn_record.png</Unpressed>
  </State>
  <State>
    <!-- RECORD READY-->
    <Number>1</Number>
    <Pressed>btn_record_over.png</Pressed>
    <Unpressed>btn_record_over.png</Unpressed>
  </State>
  <State>
    <!-- RECORD ON-->
    <Number>2</Number>
    <Pressed>btn_record_over.png</Pressed>
    <Unpressed>btn_record_over.png</Unpressed>
  </State>
  <Pos>199,114</Pos>
  <Connection>
    <ConfigKey>[Recording],toggle_recording</ConfigKey>
    <EmitOnPressAndRelease>true</EmitOnPressAndRelease>
    <ButtonState>LeftButton</ButtonState>
    <ConnectValueToWidget>false</ConnectValueToWidget>
  </Connection>
  <Connection>
    <ConfigKey>[Recording],status</ConfigKey>
    <ConnectValueFromWidget>false</ConnectValueFromWidget>
  </Connection>
</PushButton>
` | `New in Mixxx 1.11

Button that allows toggle of recording and notifies "[Recording],status" of status changes.
Can be omitted in Mixxx >= 2.00
Can be omitted in Mixxx >= 2.00






















Can be omitted in Mixxx >= 2.00

Can be omitted in Mixxx >= 2.00

The latest no button connection is the Display connection

Can be omitted in Mixxx >= 2.00


` |

### Play

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>play_cue_set</TooltipId>
  <NumberStates>2</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <State>
    <Number>1</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],play</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
  <ConfigKey>[ChannelX],cue_set</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>RightButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],play_indicator</ConfigKey>
  </Connection>
</PushButton>
` | `

Left Click: Pause/Play, Right Click: Set cue point
Overall quantity of states the button have

First state
Default image displayed
Image displayed on mouse-down


Second state
Default image displayed
Image displayed on mouse-down


Left Button connection
Defines connected Channel (X = 1 .. 4), performed action (play)
Defines if action is performed on down-click on element (true or false)
Which mouse button must be clicked so the action is performed

Right Button connection
Defines connected Channel (X = 1 .. 4), performed action (cue_set)
Defines if action is performed on down-click on element (true or false)
Which mouse button must be clicked so the action is performed

No button connection = Display connection
Defines connected Channel (X = 1 .. 4), performed action (cue_set)



` |

### Cue

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>cue_default_cue_gotoandstop</TooltipId>
  <NumberStates>2</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <State>
    <Number>1</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],cue_default</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
  <ConfigKey>[ChannelX],cue_gotoandstop</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>RightButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],cue_indicator</ConfigKey>
  </Connection>
</PushButton>
` | `

Go to and play (while playing), Set cue point (while stopped), Go to and stop (right-click)













Defines connected Channel (X = 1 .. 2) , performed action (cue_default)
Defines if action is performed on down-click on element (true or false)
Which mouse button must be clicked so the action is performed
Hint: Default cue behavior can be changed in Mixxx preferences

Defines connected Channel (X = 1 .. 2) , performed action (cue_gotoandstop)
Defines if action is performed on down-click on element (true or false)
Which mouse button must be clicked so the action is performed






` |

### Hotcue

**Hint**: Hotcues can utilize more functions in the *\<ConfigKey\>* then
shown in this example. See [MIDI Controller Mapping File
Format](midi_controller_mapping_file_format#ui_midi_controls_and_names)
for details

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>hotcue</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],hotcue_Y_activate</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
  <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],hotcue_Y_activate</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],hotcue_Y_clear</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>RightButton</ButtonState>
  </Connection>
</PushButton>
` | `

Set and play Hotcue (while playing),
play Hotcue (while stopped), delete Hotcue (right-click)







Channel (X=1 or 2), Hotcue # (Y=1-36) & performed action (activate),
depends on  # of Hotcues defined , see hotcue_X_position
Action is performed while playing (true) on click on element


Action is performed while down pressing the element and playback is stopped (false)
Playback from Hotcue X position when the player is stopped (aka Hotcue preview )
Which mouse button must be clicked so the action is performed


Channel (X=1 .. 4 ), Hotcue # (Y=1-36) & performed action (clear)

Which mouse button must be clicked so the action is performed



` |

### Looping

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>loop_in</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],loop_in</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],loop_in</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
</PushButton>
` | `
Click on button sets a "Loop-In" point. The point can not be cleared.
It is instead overwritten by a new "Loop-In" point by clicking the button again.







Channel (X=1 or 2), performed action (loop_in)
Action is performed when clicking on element
Works when playback has stopped too







` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>loop_out</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressd.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],loop_out</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],loop_out</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
</PushButton>
` | `
Click on button sets a "Loop-Out" point. The point can not be cleared.
It is instead overwritten by a new "Loop-Out" point by clicking the button again.

The "Loop-Out" point can not be set if:
* No "Loop-In" point has been set before
* The "Loop-In" point has been set before but the current playback position is prior to the "Loop-In" point



Channel (X=1 or 2), performed action (loop_out)
Action is performed when clicking on element
Works when playback has stopped too







` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>reloop_exit</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],reloop_exit</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],reloop_exit</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
 </PushButton>
` | `
Click on button activate the "Looping" feature.
The playback jumps to "Loop-In" point and loop from there until "Loop-Out" point.
Click on button while "Looping" is activated will de-activate the Looping and ignore "Loop-Out" point.

The "Looping" feature can not be activated if:
* No "Loop-In" point has been set before
* No "Loop-Out" point has been set before


Channel (X=1 or 2), performed action (reloop_exit)
Action is performed when clicking on element








` |

### Reverse playback

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>reverse</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],reverse</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],reverse</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
</PushButton>
` | `
Reverse playback Channel X while playing








Defines connected Channel (X = 1 or 2) , performed action (reverse)









` |

### Fast forward (or rewind)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>fwd_end</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>RightButton</ButtonState>
  </Connection>
</PushButton>` | `
Fast forward (rewind),  Right-click: Jump to end (start) of track








Defines connected Channel (X = 1 or 2) , performed action (Y=fwd or back)




Defines connected Channel (X = 1 or 2) , performed action (Y=fwd or back)




Defines connected Channel (X = 1 or 2) , performed action jump to (Y=end or start)




` |

### Beat sync

|                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>???</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],beatsync</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
</PushButton>` | `
Synchronize tempo with other channel








Defines connected Channel (X = 1 or 2) , performed action (beatsync)




` |

### Pitch control (up and down)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>???</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>RightButton</ButtonState>
  </Connection>
</PushButton>` | `Left Click: Temporary increase (decrease) pitch,
Right Click: Temporary increase (decrease) pitch in small step








Defines connected Channel (X = 1 or 2),
performed action (Y= rate_temp_up or rate_temp_down)



Defines connected Channel (X = 1 or 2),
performed action (Y= rate_temp_up_small or rate_temp_down_small)



` |

### Pitch bend (Nudge)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>???</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>RightButton</ButtonState>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    <ButtonState>RightButton</ButtonState>
  </Connection>
</PushButton>
` | `Left Click: Temporary increase (decrease) pitch,
Right Click: Temporary increase (decrease) pitch in small step








Defines connected Channel (X = 1 or 2) ,
performed action (Y= rate_temp_up or rate_temp_down)








Defines connected Channel (X = 1 or 2) ,
performed action (Y= rate_temp_up_small or rate_temp_down_small)








` |

### Pre-listen / Monitoring

|                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>pfl</TooltipId>
  <NumberStates>2</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <State>
    <Number>1</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],pfl</ConfigKey>
  </Connection>
</PushButton>
` | `
Headphone pre-listen for Channel X



Default button visible




Button visible when active




Defines connected Channel (X = 1 or 2) , performed action (beatsync)


` |

### BPM tap

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>???</TooltipId>
  <NumberStates>1</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],bpm_tap</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
  </Connection>
  <Connection>
    <ConfigKey>[ChannelX],bpm_tap</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
  </Connection>
</PushButton>
` | `

Takes the progressive average of the last 4 taps
and sets the bpm of the deck to that value








Defines connected Channel (X = 1 or 2) , performed action








` |

### Key lock

|                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>keylock</TooltipId>
  <NumberStates>2</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <State>
    <Number>1</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],keylock</ConfigKey>
  </Connection>
</PushButton>
` | `

Activates position-independent time stretch














Defines connected Channel (X = 1 or 2) , performed action



` |

### Repeat

|                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>repeat</TooltipId>
  <NumberStates>2</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <State>
    <Number>1</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],repeat</ConfigKey>
  </Connection>
</PushButton>
` | `

Track repeat if you go past the end or reverse before the start














Defines connected Channel (X = 1 .. 4) , performed action



` |

### Frequency Kill

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>???</TooltipId>
  <NumberStates>2</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <State>
    <Number>1</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],Y</ConfigKey>
    <EmitOnDownPress>true</EmitOnDownPress>
    <ButtonState>LeftButton</ButtonState>
  </Connection>
</PushButton>
` | `

???= filterHighKill or filterMidKill or filterLowKill
Cuts the high, mid and low frequencies on Channel X


Default button visible




Button visible when active




Defines connected Channel (X = 1 .. 4),
performed action (Y= filterHighKill or filterMidKill or filterLowKill)



` |

## Section: Knobs (RotaryFader)

### Master volume & balance

|                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Knob>
  <TooltipId>???</TooltipId>
  <NumberStates>X</NumberStates>
  <Path>knob_rotary_s%1.png</Path>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[Master],Y</ConfigKey>
  </Connection>
</Knob>` | `

???= master_volume or balance
You need X single knobs where #(X/2)+1 is the 0-state.
Example: X=41 states (270 degree rotation / 40 knobs + the 0-state) .
You need 20 knobs rotate from -135 degree to 0 degree, one knob 0 degree (default knob visible) ,
20 knobs rotate from -135 degree to 0 degree
Defines connected Channel (Master) , performed action (Y=volume or balance)


` |

### Headphone volume and mix

|                                                                                                                                                                                                         |                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `<Knob>
  <TooltipId>???</TooltipId>
  <NumberStates>X</NumberStates>
  <Path>knob_rotary_s%1.png</Path>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[Master],Y</ConfigKey>
  </Connection>
</Knob>` | `

???= headVolume or headMix




Defines connected Channel (Master), performed action (Y=headVolume or headMix)



` |

### Channel filter and gain

|                                                                                                                                                                                                     |                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Knob>
  <TooltipId>???</TooltipId>
  <NumberStates>X</NumberStates>
  <Path>knob_rotary_s%1.png</Path>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[X],Y</ConfigKey>
  </Connection>
</Knob>
` | `

???= pregain or filterHigh or filterMid or filterLow




Defines connected Channel (X = 1 or 2),
performed action (Y= pregain or filterHigh or filterMid or filterLow)


` |

## Special nodes

Check out the skins in Mixxx 1.11 as blueprint, they make heavy use of
these special nodes.

### TrackProperty

_New in Mixxx 1.9_

Replace the [Text](/creating_skins#track_information) node with
TrackProperty\`s to display more advanced track informations. You can
display more than one TrackProperty node in a skin.

|                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TrackProperty>
      <TooltipId>???</TooltipId>
      <Property>...</Property>
      <Channel>X</Channel>
      <Pos>x,y</Pos>
      <Size>a,b</Size>
   </TrackProperty>
` | `

???= check //src/skin/tooltips.cpp// for the correct tooltip ID for each key

The "Property" field can be any of:
artist, title, album, genre, year, track_number, times_played, comment, bpm, bpmFormatted, duration, durationFormatted, key (new in Mixxx 1.11)

bpm will be the full precision number (i.e. 1.333333333) while bpmFormatted is to 3 decimal places (1.333),
duration is the duration in seconds, while durationFormatted is the duration in hh:mm:ss.xx format.
` |

### WidgetGroup

_New in Mixxx 1.9_

It is probably cumbersome to have to give the absolute positions of
every node in the tree. WidgetGroups allow to make a group of relatively
positioned widgets. You can display more than one WidgetGroup node in a
skin.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `<WidgetGroup>
  <Pos>100,200</Pos>
  <Size>w,h</Size>
  <BackPath>background.png</BackPath>
  <BackPathHighlighted>alt.png</BackPathHighlighted>
  <Children>
    <PushButton>
      <Pos>0,0</Pos>
    </PushButton>
    <SliderComposed>
      <Pos>20, 0</Pos>
    </SliderComposed>
    <!-- as many regular widgets as you like in here -->
  </Children>
  <Connection>
    <ConfigKey>[EffectRack1_EffectUnit1],single_effect_focus</ConfigKey>
    <BindProperty>highlight</BindProperty>
    <Transform>
      <IsEqual>2<IsEqual>
    <Transform>
  </Connection>
</WidgetGroup>
` | `



New in Mixxx 1.11
New in Mixxx 2.1: if highlight > 0











New in Mixxx 2.1: Can be used in styles

New in Mixxx 2.1




` |

\<size\> is optional, this will limit the size so that any part of a
child widget outside of the size rectangle is not shown

In that example, the PushButton child will be at 0,0 relative to its
parent, or the absolute position 100,200. The SliderComposed widget will
be at 20,0 relative to its parent or 120,200.

New in Mixxx 1.11: Loads a background image from the skin folder.
Support resizing and color schemes. Note: The style sheet is painted on
top of the new background set by the \<BackPath\> node.

New in Mixxx 2.1: The highlight property is used to restyle the widget
with CSS. The declaration \#MyGroup\[highlight="1"\] { } will define the
style for the highlighted state. Note: The background property does not
support color schemes for images, a workaround is to set the background
image via \<BackPath\> and \<BackPathHighlighted\> from the skin.

#### WidgetGroup Layouts

**Never have to specify \<Pos\> again\!**

You can use a `<Layout>` tag in a `WidgetGroup` to have the widget group
automatically layout its children according to their size policies and
minimum/maximum widths (see `<SizePolicy>` info above). As of Mixxx
2.00.0 the valid layout types are "horizontal" and "vertical". These
correspond to putting all the child widgets in a
[QHBoxLayout](https://doc.qt.io/qt-4.8/qhboxlayout.html) and
[QVBoxLayout](https://doc.qt.io/qt-4.8/qvboxlayout.html), respectively.

Example:
```xml
<WidgetGroup>
  <Pos>100,200</Pos>
  <Size>w,h</Size>
  <Layout>horizontal</Layout><!-- Layout widgets horizontally -->
  <BackPath>background.png</BackPath><!-- New in Mixxx 1.11: Loads a background image from the skin folder. Support resizing and color schemes -->
  <!-- Note: The style sheet is painted on top of the new background set by the <BackPath> node -->
  <Children>
    <PushButton>
      ...
    </PushButton>
    <SliderComposed>
      ...
    </SliderComposed>
    <!-- as many regular widgets as you like in here -->
  </Children>
</WidgetGroup>
```

The result of this is that the pushbutton and slider will be
automatically sized and laid out horizontally within the widget group.

### Splitter

_New in Mixxx 1.11.0_

This allows you to create a QSplitter dynamically and to control the
size of child widgets by dragging the boundary between the children.

_New in Mixxx 2.10:_
Allows to specify which children can be collapsed

_New in Mixxx 2.00:_
Remember splitter layout

```xml
    <Splitter>
      <Pos>100,200</Pos>
      <Size>w,h</Size>
      <SplitSizesConfigKey>[$skin_name],$config_key</SplitSizesConfigKey>
      <SplitSizes>60,60,600</SplitSizes>
      <Orientation>horizontal</Orientation>
      <Collapsible>0,0,0</Collapsible>
      <Children>
        <WidgetGroup>
        </WidgetGroup>
        <WidgetGroup>
        </WidgetGroup>
        <WidgetGroup>
        </WidgetGroup>
        <!-- as many regular widgets as you like in here -->
      </Children>
    </Splitter>
```

`SplitSizes` gives the absolute splits between the children of the
'Splitter' in pixels. There must be as many split sizes as there are children or else it
will be ignored.
From the example, the first 2 `WidgetGroup`s will each have 60px of the splitter width initially and the 3rd `WidgetGroup` will have
600px. Any additional/missing space is distributed amongst the widgets according to their size policies.

`Orientation` holds the orientation of the splitter. Default is
horizontal (i.e. the widgets are laid out side by side). The possible
orientations are `horizontal` or `vertical`.

Mixxx remembers remember the position of moveable GUI elements,
`SplitSizesConfigKey` saves the splits in ConfigKey provided by the skin
e.g.
`<SplitSizesConfigKey>[Deere1280x1024-SXGA],LibrarySidebarSplitSize</SplitSizesConfigKey>`.

`Collapsible` gives which of children can be collapsed. From the
example, none of the 3 `WidgetGroup` can collapse. E.g. if you wish to
have the 1st widgetgroup collapsible, just change to
`<Collapsible>1,0,0</Collapsible>`

**NOTE:** `Splitter` derives from `QSplitter`. As of Qt 4.8.3 the
default `SizePolicy` for `QSplitter` is `QSizePolicy::Expanding`
horizontally and `QSizePolicy::Preferred` vertically. If you do not
provide a size for the splitter this is the default policy.

### WidgetStack

_New in Mixxx 1.11.0_

A `WidgetStack` is a widget that only shows one widget at a time. By
default, the shown widget is the first child in the `<Children>` block.
If the `NextControl` or `PrevControl` is set to 1, then the next or
previous widget in the stack is shown and the current widget is hidden.
If an optional `trigger` attribute is given to any child, then the
control named by the attribute will automatically switch to the widget
when the control is set to 1 and when the widget is hidden the control
will be set to 0 by the `WidgetStack`. This allows you to create radio
buttons that let the user switch between multiple different widgets to
occupy a certain space.

Example:
```xml
<WidgetStack>
  <NextControl>[Channel1],hotcuepage_next</NextControl> <!-- Optional: Control that switches to the next widget in the stack. (will be created if doesn't exist) -->
  <PrevControl>[Channel1],hotcuepage_prev</PrevControl> <!-- Optional: Control that switches to the previous widget in the stack. (will be created if doesn't exist) -->
  <Children>
    <WidgetGroup trigger="[Channel1],hotcuepage_show1"></WidgetGroup> <!-- A WidgetGroup that is shown when the 'trigger' control is set to 1. (will be created if doesn't exist) -->
    <WidgetGroup trigger="[Channel1],hotcuepage_show2"></WidgetGroup> <!-- A WidgetGroup that is shown when the 'trigger' control is set to 2. (will be created if doesn't exist) -->
    <WidgetGroup trigger="[Channel1],hotcuepage_show3"></WidgetGroup> <!-- A WidgetGroup that is shown when the 'trigger' control is set to 3. (will be created if doesn't exist) -->
    <!-- as many regular widgets as you like in here -->
  </Children>
</WidgetStack>
```

Some example applications:

  - Multiple pages of hotcue buttons.
  - A collapsed/expanded view of a deck: two children in a
    `WidgetStack`, one with the full deck widgets and one with the
    collapsed deck widgets. A single `<NextControl>` and a
    `<PushButton>` attached to that control allows the user to toggle
    between the collapsed and expanded view of the deck.
  - Tabbed UIs / Screen Sets. The entire skin could be one large
    `WidgetStack` that lets you switch the UI between different layouts.

_New in Mixxx 2.00.0:_<br>
If you need the stacks to remember which index they were closed with so
they can start back up in the right state, do it like this:

    <WidgetStack currentpage="[EffectRack1],current" persist="true">

The "currentpage" CO doesn't need to be defined anywhere else.

_New in Mixxx 2.00.0:_<br>
You can define which page to select if a group gets a hide signal.
`on_hide_select` adds a page to the stack. If this page is hidden, the
the page with the 0-based index given by on\_hide\_select will be shown.
If this value is -1, the next page on the stack will be shown.

Example:
```xml
<WidgetStack>
  <Children>
    <WidgetGroup on_hide_select="0"></WidgetGroup> <!-- First page of the stack -->
    <WidgetGroup trigger="[Channel1],hotcuepage_show1" on_hide_select="0"></WidgetGroup> <!-- When any page is hidden, go back to the first page. -->
    <WidgetGroup trigger="[Channel1],hotcuepage_show2" on_hide_select="0"></WidgetGroup> <!-- When any page is hidden, go back to the first page. -->
    <WidgetGroup trigger="[Channel1],hotcuepage_show3" on_hide_select="0"></WidgetGroup> <!-- When any page is hidden, go back to the first page. -->
    <!-- as many regular widgets as you like in here -->
  </Children>
</WidgetStack>
```

### SizeAwareStack

_New in Mixxx 2.00.0_

A `SizeAwareStack` selects the best fitting widget based on available
space. It allows GUI elements to easily adopt to window size without
manual actions.The algorithm is very basic and requires children sorted
by size, smallest first.

Example:
```xml
<SizeAwareStack>
  <Children>
    <WidgetGroup>
      <MinimumSize>10,10</MinimumSize><!-- A WidgetGroup that is shown when the available screen estate -->
      <MaximumSize>10,10</MaximumSize><!-- is at least 10x10 pixel -->
      <Style>QGroupBox {background: blue;}</Style>
    </WidgetGroup>
    <WidgetGroup>
      <MinimumSize>100,10</MinimumSize><!-- A WidgetGroup that is shown when the available screen estate -->
      <MaximumSize>199,10</MaximumSize><!-- is 100x10 up to 199x10 pixel. -->
      <Style>QGroupBox {background: red;}</Style>
    </WidgetGroup>
    <WidgetGroup>
      <MinimumSize>200,10</MinimumSize><!-- A WidgetGroup that is shown when the available screen estate -->
      <MaximumSize>200,10</MaximumSize><!-- is at least 200x10 pixel -->
      <Style>QGroupBox {background: green;}</Style>
    </WidgetGroup>
  </Children>
</SizeAwareStack>
```



### ComboBox

New in Mixxx 2.00.0

```xml
    <ComboBox>
      <State>
        <Number>1</Number>
        <Text>Text</Text>
        <Icon>icon.png</Icon>
      </State>
      <State>
        <Number>2</Number>
        <Text>Text</Text>
        <Icon>icon.png</Icon>
      </State>
      <Connection>
        <ConfigKey>[XXX],combobox_selector</ConfigKey>
      </Connection>
    </ComboBox>
```

Both \<Text\> and \<Icon\> tags are optional. The order in which the
states are displayed is determined by the order they have in the xml,
not by the \<Number\> tag. What does the \<Number\> tag do?

The control object that holds the state of the combobox is determined
with the \<Connection\> tag.

### Singleton widgets

_New in Mixxx 2.00.0_

Defines widgets that should only be instantiated once but may appear in
multiple places in a skin definition. This is useful for complex widgets
like the library, which are memory intensive. The container mostly looks
like a special WidgetGroup which is defined in special ways.

**Usage:**

First, the Singleton container is defined, meaning it is described to
the skin system by name, and what the singleton consists of. This
definition should be very early in the skin file. Note that the
singleton does not actually appear where it is defined.

Example definition:
```xml
<SingletonDefinition>
  <ObjectName>LibrarySingleton</ObjectName>
  <!-- The ObjectName is used to identify this singleton elsewhere in the skin files -->
  <Children>
    <Template src="skin:library.xml"/>
    <!-- The skin:prefex is replaced by the skin folder first, if this fails the current directory is used -->
  </Children>
</SingletonDefinition>
```

Example usage:

```xml
<WidgetGroup>
  <ObjectName>SomeUiElement</ObjectName>
  <Layout>vertical</Layout>
  <SizePolicy>min,i</SizePolicy>
  <Children>
    <SingletonContainer>
      <ObjectName>LibrarySingleton</ObjectName>
    </SingletonContainer>
    ...
  </Children>
</WidgetGroup>
```

The skin system sees the Singleton tag, and any time the containing
group gets a show event, the Singleton widget is reparented to this
location in the skin. Note that if a Singleton is visible twice at the
same time, behavior is undefined and could be crashy.

### Skin Preview Image

_New in Mixxx 2.1.0, changed in Mixxx 2.3.0_

To provide users a rough impression of what skins look like before they
switch to a different skin, show a preview screenshot when a skin is
selected with the combobox in `Preferences --> Interfaces --> Skin`.

The screenshoot should show skins in their default configuration. Save
as `skin_preview.png` in the root folder of the corresponding skin (was
`preferences_preview_screenshot.png` prior to Mixxx 2.3). Is no
screenshoot provided, a placeholder is displayed.

_New in Mixxx 2.3.0_<br>
If [color schemes](creating_skins#skin_color_scheme) are supported by
the selected skin, show a preview screenshots for a set of color
variations to choose from in Preferences -\> Interface -\> Color Scheme.
Save as `skin_preview_$SchemeName.png` ( replace *$SchemeName* with the
actual value of the respective
[\<Name\>](https://github.com/mixxxdj/mixxx/wiki/Skin-Color-Scheme-Architecture#scheme-format) key) in the
root folder of the corresponding skin.

### Launch Image

New in Mixxx 2.00.0

Mixxx features a default launch image that is shown during Mixxx
launching. It features a centered label with a progress bar below.

All elements are style-able by Qt stylesheets as shown in the example
below:

Example definition:
```xml
<LaunchImageStyle>
  LaunchImage { background-color: #202020; }
  QLabel {
    image: url(skin:/style/mixxx-icon-logo-symbolic.png);
    padding:0;
    margin:0;
    border:none;
    min-width: 208px;
    min-height: 48px;
    max-width: 208px;
    max-height: 48px;
  }
  QProgressBar {
    background-color: #202020;
    <!-- You can also use an image instead. To avoid blur, size it according to data below -->
    background: url(skin:/style/progressbar_bg.svg);
    border:none;
    min-width: 208px;
    min-height: 3px;
    max-width: 208px;
    max-height: 3px;
  }
  QProgressBar::chunk {
    background-color: #ec4522;
    <!-- You can also use an image instead. To avoid blur, size it like the QProgressBar -->
    background: url(skin:/style/progressbar.svg);
  }
</LaunchImageStyle>
```

### Battery

_New in Mixxx 2.1.0_

A a widget to show the laptop battery status.

```xml
<Battery>
  <BackPath>battery_background.png</BackPath><!-- default background -->
  <PixmapUnknown>battery_unknown.png<PixmapUnknown><!-- displayed when battery status is unknown -->
  <PixmapCharged>battery_charged.png</PixmapCharged><!-- displayed when battery is full -->
  <NumberStates>10</NumberStates><!-- number of charging / discharging pixmaps -->
  <PixmapsCharging>battery_%1_charging.png</PixmapsCharging><!-- displayed when battery is charging -->
  <PixmapsDischarging>battery_%1_discharging.png</PixmapsDischarging><!-- displayed when battery is discharging -->
</Battery>
```

The charging/discharging pixmaps are 0-indexed, %1 will be replaced with 0 to [NumberStates - 1].

_Changed in Mixxx 2.3:_<br>
The Battery widget is hidden by default and only becomes visible once
the status is known. This means that the unknown-icons are never
presented to the user.

The status can be unknown if there is no battery present or if there are
problems reading the status.

## Deprecated keys

### Main background

Deprecated in Mixxx 1.11.0, use [WidgetGroup](creating_skins?#widgetgroup) instead.

```xml
<Background><!-- start background tag -->
  <!-- Defines which image in the skins folder to use for the background. All elements are displayed over this image and its size defines the skin size (see Guidelines) -->
  <Path>background.png</Path>
  <!-- Defines a background color. Example: <BgColor>#000000</BgColor> (000000 being the hex value for black) -->
  <BgColor>#</BgColor>
</Background><!-- end background tag -->
```

#### Library TableView

Deprecated in Mixxx 1.11.0, use the different keys of the [Library
display](creating_skins#library_display) instead

|                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TableView>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <BgColor>#</BgColor>
  <FgColor>#</FgColor>
  <BgColorRowEven>#</BgColorRowEven>
  <BgColorRowUneven>#</BgColorRowUneven>
</TableView>

` | `start TableView tag
Defines the element position
Defines the element size
Background color library widget (i.e. background color search widget)
Foreground color library widget (i.e. text in "Analyze" widget)
Background color even line right library pane
Background color uneven lines right library pane
end TableView tag
` |

### End of track mode

Deprecated in Mixxx 1.9.0, use the [Repeat](creating_skins#repeat)
button instead

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <Tooltips></Tooltips>
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
` | `

End of track mode control (see manual)



Button visible in STOP mode




Button visible in NEXT mode




Button visible in LOOP mode




Defines connected Channel (X = 1 .. 2) , performed action (TrackEndMode)



` |

### FX (Flanger)

Deprecated in Mixxx 1.11.0, use the [effects
framework](mixxxcontrols#effects_framework) instead

|                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
  <TooltipId>flanger</TooltipId>
  <NumberStates>2</NumberStates>
  <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <State>
    <Number>1</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
  </State>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[ChannelX],flanger</ConfigKey>
  </Connection>
</PushButton>` | `

Apply flanger effect to Channel X



Default button visible




Button visible when active




Defines connected Channel (X = 1 .. 4) , performed action (flanger)


` |

### Flanger (FX) setting

Deprecated in Mixxx 1.11.0, use the [effects
framework](mixxxcontrols#effects_framework) instead

|                                                                                                                                                                                                          |                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Knob>
  <TooltipId>???</TooltipId>
  <NumberStates>X</NumberStates>
  <Path>knob_rotary_s%1.png</Path>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[Flanger],Y</ConfigKey>
  </Connection>
</Knob>` | `
???= lfoDelay or lfoDepth or lfoPeriod





Defines connected Channel (Flanger),
performed action (Y=lfoDelay or lfoDepth or lfoPeriod)


` |

# Useful Links

  - [Skin Color Scheme
    Architecture](https://github.com/mixxxdj/mixxx/wiki/Skin-Color-Scheme-Architecture#scheme-format) - Explains how
    color schemes work in Mixxx 1.6.0+
  - [Mixxx Skinning Guidelines](Skin%20Guidelines)
  - [Skin Color Schemes Tips and
    Tool](Skin%20Color%20Schemes%20Tips%20and%20Tool) - A "walkthrough"
    on creating schemes, includes a link to an online Javascript tool
    that will help determine correct HSVTweak values.
  - [Skin layout tutorial](Skin%20layout%20tutorial) - A walkthrough on
    creating a minimal skin, with focus on the common problems a skin
    designer will encounter when setting the layout of various skin
    elements.
  - [Skin System Changelog](skin_system_changelog) - Follow the changes
    as Mixxx evolves, and learn how to apply these changes when creating
    skins.
