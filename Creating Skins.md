# Creating Skins

Skins can change the look and feel of Mixxx. Some skins merely make the
program more aesthetically pleasing while others rearrange elements of
the interface, potentially making the program easier to use.

### Getting started

A skin for Mixxx is basically a folder with various images, a text file
named skin.xml, other XML template files and a [style.qss
file](/creating_skins#qss_style). The skin.xml and template files define
all the elements (widgets) of the skin, what the images are used for and
and where they are placed on screen.

Reading this page helps to understand how skins work in Mixxx‚ it will
save you time eventually.

Start a new skin by navigating to your local [Mixxx resource
folder](/creating_skins#skin_faq), duplicate the directory of the skin
you like to work on and rename it. Use the content of the new folder as
starting point for your first skin. Read this page, understand how
things were done in the skin you copied and try to work from there. If
you're familiar with HTML, then you should pretty comfortable editing
the skin.xml.

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

General structure of the skin.xml. More in-depth informations for each
element and their attributes defined in the skin.xml can be found
[here](#skinxml-in-depth-review)

| syntax | Info |
| ------ | ---- |

|                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<!--Comment-->
<!DOCTYPE skin>
<skin>
<manifest>...</manifest>
<elementname>
  <TooltipId>...</TooltipId>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <MinimumSize>W,H</MinimumSize>
  <MaximumSize>W,H</MaximumSize>
  <SizePolicy>WPolicy,HPolicy</SizePolicy>
  <options>values(depends)</options>
</elementname>
</skin>
` | `Optional comments (i.e. skin license or changelog)
Doctype declaration
Skin opening tag
Manifest describing skin properties (author, title, version, etc.)
Elements opening tag
Tooltips to display on mouse-over, available IDs are in src/skin/tooltips.cpp
Position on the screen
Size (depending on the element)
Minimum Size
Maximum Size
Size Policy
Options(depending on the element)
Elements closing tag
Skin closing tag
` |

### Skin 101

Lets have a look at this simplified example of the Mixxx user interface
(deprecated Outline skin template).  
The various elements of the skin are marked and explained below.

[[/media/skinning/creating_skins/mixxx1.9_gui_explained_outline.png|]]

[1.General](#sectiongeneral-)

  - Manifest - specifies information about the skin (title, artist,
    description, version) and allows you to set Mixxx controls when the
    skin is loaded (e.g. enable 4-deck mode).
  - Skin Colour Scheme - allows the creation of different [colour
    schemes](http://mixxx.org/wiki/doku.php/skin_colour_scheme_architecture)
    of a skin
  - Library display - Widget holds all your music information,
    playlists, search bar etc.

[2.Visual](#sectionvisual-)

  - Waveform - shows the loaded tracks waveforms near the playback
    position
  - Waveform overview - shows a waveform visualization of the whole song
  - Volume level display - shows the playback volume of the song /
    master
  - Peak indicator - shows if a songs / master volume is too high

[3.Text](#sectiontext)

  - Label (not shown) - displays a text label
  - Clock (not shown) - displays the current time
  - Track information - shows some ID3 information of the song ( Name,
    Artist )
  - BPM Information - shows the tempo of the song
  - Playing position / Time remaining - shows current playback position
    or remaining time (click to switch)
  - Pitch rate information - shows how much the song is speed up /
    slowed down (in percent)

[4.Slider](#sectionslider)

  - Channel Volume - controls the volume of the selected channel
  - Crossfader - fade between the channels
  - Pitch control - changes the tempo of a song
  - \[InternalClock\], bpm - tempo of the internal master sync clock
    (also viewable as plain text)

[5.Buttons](#sectionbuttons)

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

[6.Knobs (Rotary fader)](#sectionknobs-rotaryfader-)

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

### Skin FAQ

#### How to install a skin

Additional skins for Mixxx can be downloaded in the
[forum](http://mixxx.org/forums/viewforum.php?f=8).

    In this example we are going to install the file "NewSkin.zip"
    
    1. Close Mixxx.
    2. Download & unzip "NewSkin.zip" and copy the whole unzipped folder "NewSkin" to the corresponding path:
    
    Linux
    *************
    /usr/share/mixxx/skins/
    so you get
    /usr/share/mixxx/skins/NewSkin
    
    Note that you may get permission error while copying,
    make sure you have root privileges
    
    Windows
    *************
    C:\Program Files\Mixxx\skins
    so you get
    C:\Program Files\Mixxx\skins\NewSkin
    
    Mac OSX
    *************
    -  In the Finder, go to the Applications folder and select Mixxx.
    -  Right Click and choose "Show Package Contents" from the Action menu.
    -  goto Contents/Resources/skins
    
    or straight via Terminal
    /Applications/Mixxx.app/Contents/Resources/skins
    so you get
    /Applications/Mixxx.app/Contents/Resources/skins/NewSkin
    
    Double-check that the skin.xml is in the "NewSkin" root folder and not in a subfolder, otherwise Mixxx may throw an error when starting that skin.
    
    3. Start Mixxx , goto "Preferences-->Interface" and select "Skin-->NewSkin"
       Make sure you have "Waveform Display-->Waveform" selected
       Save preferences with OK.
    
    4. The new skin should now be displayed.
    
    5. Done.

#### The filters (e.g. blur) used in my svg files are not visible. Why ?

So you created a nice button with a drop shadow blur effect in svg
format, only to find the button is displayed without the drop shadow in
Mixxx? [Qt](https://en.wikipedia.org/wiki/Qt_\(software\)) supports the
[static features](https://www.w3.org/TR/SVGMobile12/feature.html) of SVG
1.2 Tiny. ECMA scripts and DOM manipulation are currently not supported,
see <http://doc.qt.io/qt-5/svgrendering.html>

### Skin licensing & copyright

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

### Tools

  - Free Code editors - Cross-platform ([Visual Code
    Studio](https://code.visualstudio.com/)), ([Atom](https://atom.io/))
  - Free Images editors - Online
    ([Phoenix](http://aviary.com/tools/phoenix),
    [Pixlr](http://www.pixlr.com/)), Windows
    ([Paint.net](http://www.getpaint.net/)) Mac OSX
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
on the example of **Outline** skin.  
So open up the skin.xml in the Outline folder with your favorite [text
editor](#tools) and get started :-)

## Section: General

### Skin Manifest

**New in Mixxx 1.11.0**

The skin manifest section tells Mixxx details about the skin. Some of
the details are currently unused but may be used in a future version.
Additionally we may expand the manifest to include things like
minimum-Mixxx-version required or recommended screen resolution.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<manifest>
<title>...</title>
<author>...</author>
<version>...</version>
<description>...</description>
<language>en</language>
<license>...</license>
<attributes>
  <attribute config_key="[Master],num_decks">4</attribute>
  <attribute config_key="[Master],num_samplers">16</attribute>
  <attribute config_key="[Master],num_preview_decks">1</attribute>
  <attribute config_key="[Samplers],show_samplers">1</attribute>
</attributes>
</manifest>` | `start manifest tag
Skin title
Skin author
Skin version (not the Mixxx version)
A brief description of the skin
Skin language (if language-independent, omit or put *)
Skin copyright license (e.g. Creative Commons Attribution, Share-Alike 3.0 Unported)
Begin skin attributes
Set "[Master],num_decks" ConfigKey to 4 when skin is loaded. Requires additional code per Deck in the skin.xml
Set "[Master],num_samplers" ConfigKey to 16 when skin is loaded. Requires additional code per Sampler Deck in the skin.xml
Set "[Master],num_preview_decks" ConfigKey to 1 when skin is loaded. Requires additional code for the Preview Deck in the skin.xml
Set "[Samplers],show_samplers" WidgetGroup to be visible by default. Works for existing WidgetGroups with <BindProperty>visible</BindProperty> key
End skin attributes
end manifest tag` |

**The only part of the manifest that is used in 1.11.0 is the
\<attributes\> section.** This section allows the skin to specify
changes to Mixxx controls that should be executed when the skin is
loaded. For example, Mixxx defaults to 2-decks in its mixing engine but
when you load a skin that supports 4-decks, the skin can specify that
the Control "\[Master\],num\_decks" should be set to 4 (see the above
example). This will enable a 3rd and 4th deck in Mixxx's engine for the
skin to interact with. This attribute list can change any Mixxx control
but will only take effect when the skin is loaded.

### QSS Style

To specify how skins look (for example colors and text sizes), skins use
a [Qt Style Sheet](http://doc.qt.io/qt-4.8/stylesheet.html) (QSS) file
which is similar to a [Cascading Style
Sheet](https://developer.mozilla.org/en-US/docs/Web/CSS) (CSS) file used
to specify how web pages look. The QSS file is linked to the skin XML
with a \<Style\> element that is a child of the root \<skin\> element:

    <skin>
      <manifest>
        <!-- skin manifest goes here -->
      </manifest>
    
      <Style src="skin:style.qss" src-windows="skin:style-windows.qss"
       src-mac="skin:style-mac.qss" src-linux="skin:style-linux.qss"/>
    
      <!-- rest of skin goes here -->
    </skin>

All the skins included in Mixxx name the QSS file as `style.qss` in the
root directory of the skin. Any name with the `*.qss` or `*.css` file
extension will work. Optionally, you can add up to three additional QSS
files to your skin directory, e.g. to work around platform-dependent
quirks in styling: `src-windows="..."`, `src-mac="..."` `and
src-linux="..."`

Widgets are selected in QSS by the name of their widget type (the "Mixxx
internal name" column in the table below) or by a defined name. To
define a name for a widget, use the `<ObjectName>` element. For example:

    <WidgetGroup>
      <ObjectName>SomeWidgetGroup</ObjectName>
      <Children>
        <!-- A group of widgets you want to apply style to go here -->
      </Children>
    </WidgetGroup>

This is similar to setting an `id` attribute on an element in HTML
except that multiple widgets can share the same `<ObjectName>`. To style
the above `<WidgetGroup>` in QSS, you would select it with `#`. For
example:

    #SomeWidgetGroup {
      background-color: black;
    }

Knowing what options are available to style is tricky and it involves
knowing what Qt widget the associated Mixxx widget derives from.

Handy resources:

  - [Qt Style Sheet
    Documentation](https://doc.qt.io/doc/qt-4.8/stylesheet.html)
  - [Qt Style Sheet
    Syntax](https://doc.qt.io/doc/qt-4.8/stylesheet-syntax.html)
  - [Qt Style Sheet Widget
    Reference](https://doc.qt.io/doc/qt-4.8/stylesheet-reference.html)
    -- tells you what widgets support which properties.

Here is a potentially out-of-date list of which Mixxx widgets derive
from which Qt widgets. If not listed, the widget inherits from
`QWidget`.

|  | Skin Tag        |  | Mixxx Internal Name |  | Qt Widget                   |  |
|  | --------------- |  | ------------------- |  | --------------------------- |  |
|  | WidgetStack     |  | WWidgetStack        |  | QStackedWidget              |  |
|  | WidgetGroup     |  | WWidgetGroup        |  | QGroupBox                   |  |
|  | (none)          |  | WTrackTableView     |  | QTableView                  |  |
|  | (none)          |  | WLibraryTableView   |  | QTableView                  |  |
|  | Library         |  | WLibrary            |  | QStackedWidget              |  |
|  | LibrarySidebar  |  | WLibrarySidebar     |  | QTreeView                   |  |
|  | SearchBox       |  | WSearchLineEdit     |  | QLineEdit                   |  |
|  | Spinny          |  | WSpinny             |  | QGLWidget                   |  |
|  | Visual          |  | WWaveformViewer     |  | QWidget                     |  |
|  | NumberRate      |  | WNumberRate         |  | QWidget with a QLabel child |  |
|  | NumberPos       |  | WNumberPos          |  | QWidget with a QLabel child |  |
|  | NumberBpm       |  | WNumber             |  | QWidget with a QLabel child |  |
|  | Number          |  | WNumber             |  | QWidget with a QLabel child |  |
|  | Label           |  | WLabel              |  | QWidget with a QLabel child |  |
|  | Text            |  | WTrackText          |  | QWidget with a QLabel child |  |
|  | TrackProperty   |  | WTrackProperty      |  | QWidget with a QLabel child |  |
|  | Time            |  | WTime               |  | QWidget with a QLabel child |  |
|  | Key             |  | WKey                |  | QWidget with a QLabel child |  |
|  | Splitter        |  | WSplitter           |  | QSplitter                   |  |
|  | DefineSingleton |  | WSingletonContainer |  | QWidget                     |  |
|  | EffectSelector  |  | WEffectSelector     |  | QComboBox                   |  |

### Properties Common to All Widgets

Every skin widget is declared in a block with an opening XML tag and a
closing tag. For example, this block defines a musical key widget that
shows the current key of a playing deck:

    <Key>
        <TooltipId>visual_key</TooltipId>
        <Pos>X,Y</Pos>
        <Size>W,H</Size>
        <Connection>
            <ConfigKey>[ChannelX],visual_key</ConfigKey>
        </Connection>
    </Key>

Sub-tags like the `<Size>` tag tell Mixxx how it should size, style and
layout the widget. There are certain sub-tags that are common to all
widgets and behave in the same way regardless of the widget type.

#### \<Pos\>

`<Pos>` tags tell Mixxx where to position a widget. The position is
relative to the widget's parent. For example, if the position is `0,50`
then this means position the widget 0 pixels from the horizontal
location of the parent widget and 50 pixels from the vertical location
of the widget's parent.

| Examples:                                           |                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<Pos>0,50</Pos>
<Pos>50,0</Pos>
<Pos>50,50</Pos>
` | `position 0 pixels from the horizontal position of parent, 50 pixels from the vertical position
position 50 pixels from the horizontal position of parent, 0 pixels from the vertical position
position 50 pixels from the horizontal position of parent, 50 pixels from the vertical position
` |

#### \<Size\>

`<Size>` tags tells Mixxx what size to make a widget. The size tag has a
lot of historical baggage associated with it because it has been around
since the first version of Mixxx and has a bunch of hacks added to it.

`<Size>` is formatted as the horizontal size and the vertical size
separated by a comma. You can also specify a size policy using the size
tag alone. As of Mixxx 2.00.0 there is a dedicated `<SizePolicy>` tag
for this. Simply append the SizePolicy skin abbreviation (see the table
in the `<SizePolicy>` section below) at the end of each dimension's
value.

| Examples:                                                                             |                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Size>100,50</Size>
<Size>100me,50p</Size>
<Size>100me,50</Size>
<Size>me,e</Size>
` | `100 pixels wide and 50 pixels tall.
100 pixels wide and 50 pixels tall. The horizontal size policy is MinimumExpanding and the vertical policy is Preferred.
100 pixels wide and 50 pixels tall. The horizontal size policy is MinimumExpanding.
The horizontal size policy is MinimumExpanding and the vertical size policy is Expanding. No explicit size is set.
` |

#### \<MinimumSize\>

**New in Mixxx 2.00.0**

`<MinimumSize>` tags tell Mixxx the smallest size a widget should be.
The widget will never be resized to be smaller than this size.

`<MinimumSize>` is formatted as the minimum horizontal size and the
minimum vertical size separated by a comma. A value of -1 for a
dimension means no minimum in that dimension.

| Examples:                                                                                                |                                                                                                                   |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `<MinimumSize>100,50</MinimumSize>
<MinimumSize>200,-1</MinimumSize>
<MinimumSize>-1,300</MinimumSize>
` | `minimum width 100, minimum height 50
minimum width 200, no minimum height
no minimum width, minimum height 300
` |

#### \<MaximumSize\>

**New in Mixxx 2.00.0**

`<MaximumSize>` tags tell Mixxx the largest size a widget should be. The
widget will never be resized to be larger than this size.

`<MaximumSize>` is formatted as the maximum horizontal size and the
maximum vertical size separated by a comma. A value of -1 for a
dimension means no maximum in that dimension.

| Examples:                                                                                                |                                                                                                                   |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `<MaximumSize>100,50</MaximumSize>
<MaximumSize>200,-1</MaximumSize>
<MaximumSize>-1,300</MaximumSize>
` | `maximum width 100, maximum height 50
maximum width 200, no maximum height
no maximum width, maximum height 300
` |

#### \<SizePolicy\>

**New in Mixxx 2.00.0**

`<SizePolicy>` tags tell Mixxx how widgets should grow or shrink based
on the available space. Size policy refers to the Qt
[QSizePolicy](https://doc.qt.io/qt-4.8/qsizepolicy.html#Policy-enum).

| SizePolicy       |  | Skin Abbreviation |  | What it does                                                                                                                                                                  |  |
| ---------------- |  | ----------------- |  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| Fixed            |  | f                 |  | The size in the given dimension is fixed and should not grow or shrink.                                                                                                       |  |
| Minimum          |  | min               |  | The widget size in this dimension is the minimum it should be. It can grow but will not be smaller than this.                                                                 |  |
| Maximum          |  | max               |  | The widget size in this dimension is the maximum it should be. It can shrink but will not be larger than this.                                                                |  |
| Preferred        |  | p                 |  | The widget size in this dimension is the preferred size. It can be shrunk and still be useful. It can grow but there is no advantage to it growing.                           |  |
| Expanding        |  | e                 |  | The widget size in this dimension can be shrunk and still be useful. The widget can make use of extra space in this dimension so it should receive as much space as possible. |  |
| MinimumExpanding |  | me                |  | The widget size in this dimension is the minimum it should be. The widget can make use of extra space in this dimension so it should receive as much space as possible.       |  |
| Ignored          |  | i                 |  | The widget size in this dimension is ignored. The widget will get as much space as possible.                                                                                  |  |

The `<SizeHint>` property is formatted as the skin abbreviation (from
the above table) for the horizontal size and the skin abbreviation for
the vertical size policy separated by a comma.

| Examples:                                                                                     |                                                                                                                              |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `<SizePolicy>f,min</SizePolicy>
<SizePolicy>me,me</SizePolicy>
<SizePolicy>p,f</SizePolicy>
` | `Fixed horizontal, Minimum vertical
MinimumExpanding for both horizontal and vertical
Preferred horizontal, Fixed vertical
` |

#### \<TooltipId\>

`<TooltipId>` tags indicate what tooltip Mixxx should use for the
widget. We used to embed tooltips directly into skins but then we found
this was a massive hassle to keep up to date and translate into
different languages. As a result, we have created a list of standard
tooltips that you can use in most cases.

The `<TooltipId>` tag tells Mixxx to use an existing tooltip that is
built into Mixxx. To see the list of tooltips that exist, the only
current way is to browse the
[src/skin/tooltips.cpp](https://github.com/mixxxdj/mixxx/blob/master/src/skin/tooltips.cpp)
and look at all the `add("example")` lines in the file. If you would
like to use a tooltip, you should make the TooltipId the word "example"
for the appropriate tooltip.

| Examples:                                                           |                                                                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `<TooltipId>track_artist</TooltipId>
<TooltipId>eject</TooltipId>
` | `Use the "track_artist" tooltip from the tooltip file.
Use the "eject" tooltip from the tooltip file.
` |

#### \<Tooltip\>

If no existing tooltip meets your needs, you can create a custom tooltip
using the `<Tooltip>` tag.

| Examples:                               |                                                              |
| --------------------------------------- | ------------------------------------------------------------ |
| `<Tooltip>My Custom Tooltip</Tooltip>
` | `Use the phrase "My Custom Tooltip" as the widget tooltip.
` |

Translation or internationalization of these tooltips is not currently
possible.

#### \<Connection\>

The connection block can be used to bind a ControlObject to the widget.
It binds either to the default connection or to any widget property
using the \<BindProperty\> element.  
The ControlObject value can be transformed using on or more
transformers.  
Currently supported properties:

  - `visible` Display the widget only if (transformed) \<ConfigKey\>
    equals `1`
  - `highlight`' Apply styles to the widget via qss when (transformed)
    \<ConfigKey\> equals N. QSS code: \#NameOfObject\[highlight="N"\] {
    ... }

| Examples:                                                                                                                                                                                                                                       |                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `<Connection>
  <ConfigKey>[EffectRack1_EffectUnit1],single_effect_focus</ConfigKey>
  <BindProperty>highlight</BindProperty>
  <Transform>
    <Invert/>
    <Not/>
    <Add>0.5</Add>
    <IsEqual>2</IsEqual>
  </Transform>
</Connection>
` | `

ConfigKey of the ControlObject
Widget proprty

p = -co
p = !co
p = co + 0.5
New in Mixxx 2.1: p = (co == 2)



` |

### Skin Color Scheme

Allows the creation of different color schemes, see [Color scheme
architecture](http://mixxx.org/wiki/doku.php/skin_colour_scheme_architecture)
for details

### Library display

The library manages all of your music files. This is where you can find
the tracks you want to play and load them into a deck or sampler.

The library typically consist of:

  - library sidebar: Contains different collections of music, and let
    you browse for files.
  - library table: The track list view displays the tracks in those
    collections.
  - Library searchbox: The search function filters the currently
    displayed list (e.g. a playlist, a crate, or even the whole library)
    for tracks that match your search query.

FIXME: Add code example for typical library

#### Library Sidebar

|                                     |
| ----------------------------------- |
| `<LibrarySidebar></LibrarySidebar>` |

#### Library Table

|                       |
| --------------------- |
| `<Library></Library>` |

#### Library SearchBox

|                           |
| ------------------------- |
| `<SearchBox></SearchBox>` |

## Section: Visual

### Waveform

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Visual>
  <TooltipId>waveform_display</TooltipId>
  <Channel>X</Channel>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <BgColor>#</BgColor>
  <BgPixmap>custom_background.png</BgPixmap>
  <Orientation>X</Orientation>
  <Align>X</Align>
  <SignalColor>#</SignalColor>
  <SignalLowColor>#</SignalLowColor>
  <SignalMidColor>#</SignalMidColor>
  <SignalHighColor>#</SignalHighColor>
  <SignalRGBLowColor>#</SignalRGBLowColor>
  <SignalRGBMidColor>#</SignalRGBMidColor>
  <SignalRGBHighColor>#</SignalRGBHighColor>
  <BeatColor>#</BeatColor>
  <EndOfTrackColor>#</EndOfTrackColor>
  <AxesColor>#</AxesColor>
  <PlayPosColor>#</PlayPosColor>
  <BeatHighlightColor>#</BeatHighlightColor>
  <HfcColor>#</HfcColor>
  <MarkerColor>#</MarkerColor>
  <CueColor>#</CueColor>
<Visual>

` | ``begin Visual tag
Tooltip to be displayed on mouseover, depends on selected ID`s. Make sure to select the correct ID for each key, available IDs are in //src/skin/tooltips.cpp//
Which channel the settings are connected to (X=1 or 2)
Defines the element position
Defines the element size
Color of waveform background  (until Mixxx 1.10. a default gradient was added , not for #000000)
New in Mixxx 1.10: Loads a background image and will tile it when smaller than the waveform widget
New in Mixxx 2.1: Indicates whether to display horizontal or vertical waveform ( X = "horizontal" or "vertical" ). Default is horizontal.
New in Mixxx 1.11: Show full waveform centered (default) or only bottom/top half ( X = "bottom" or "top" ) (for horizontal waveform) or only left/right half ( X = "left" or "right" ) (for vertical waveform).
Color of waveform
New in Mixxx 1.11: Colors of low frequencies in waveform. If no low/mid/high colors are provided, fallback to <SignalColor>
New in Mixxx 1.11: Colors of mid frequencies in waveform
New in Mixxx 1.11: Colors of high frequencies in waveform
New in Mixxx 2.00: Colors of low frequencies in RGB waveform. Allows separate color config for RGB waveforms, if selected in ''Preferences>Waveforms>Summery Type>RGB (GL)''
New in Mixxx 2.00: Colors of mid frequencies in RGB waveform.
New in Mixxx 2.00: Colors of high frequencies in RGB waveform
Color of beatgrid (multiple vertical lines)
New in Mixxx 1.11: Color of notification overlay displayed within the last seconds of a track
New in Mixxx 1.11: Color of static horizontal line
New in Mixxx 1.11: Color of static vertical line
Deprecated in Mixxx 1.11: Highlight color when beatgrid is near playback position
Deprecated in Mixxx 1.11: Color of horizontal line
Deprecated in Mixxx 1.11: Color center marker (single vertical line)
Deprecated in Mixxx 1.11: Color of Cuepoint marker
end Visual tag

`` |

|                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Mark>
  <Control>cue_point</Control>
  <Pixmap>custom_marker.png</Pixmap>
  <Text>CUEPOINT</Text>
  <Align>X\|Y</Align>
  <Color>#</Color>
  <TextColor>#</TextColor>
</Mark>

` | `begin Mark tag
Defines the Cuepoint, max. one cuepoint per channel
Optional: Uses an image from the skin's folder to define a custom marker, if available it overrides the default triangle
Text visible when Cuepoint is set (and no custom marker is defined)
Defines where text is positioned (X = "left" or "hcenter" or "right"; Y = "top" or "vcenter" or "bottom"). Note: "center" can be used as a shorthand for "hcenter\|vcenter".
Defines text background color
Defines text color
end Mark tag
` |

|                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `
<Mark>
  <Control>hotcue_X_position</Control>
  <Pixmap>custom_marker.png</Pixmap>
  <Text>HOTCUE X</Text>
  <Align>X\|Y</Align>
  <Color>#</Color>
  <TextColor>#</TextColor>
</Mark>

` | `begin Mark tag
max. 36 Hotcues(X=1-36), define every Hotcue for its own
Optional: uses an image from the skin's folder to define a custom marker, if available it overrides the default triangle
Text visible when Hotcue point is set (and no custom marker is defined)
Defines where text is positioned (X = "left" or "hcenter" or "right"; Y = "top" or "vcenter" or "bottom"). Note: "center" can be used as a shorthand for "hcenter\|vcenter".
Defines text background color
Defines text color
end Mark tag
` |

|                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `
<Mark>
  <Control>hotcue_X_position</Control>
  <Pixmap>custom_marker.png</Pixmap>
  <Text>HOTCUE X</Text>
  <Align>X\|Y</Align>
  <Color>#</Color>
  <TextColor>#</TextColor>
</Mark>

` | `begin Mark tag
max. 36 Hotcues(X=1-36), define every Hotcue for its own
Optional: uses an image from the skin's folder to define a custom marker, if available it overrides the default triangle
Text visible when Hotcue point is set (and no custom marker is defined)
Defines where text is positioned (X = "left" or "hcenter" or "right"; Y = "top" or "vcenter" or "bottom"). Note: "center" can be used as a shorthand for "hcenter\|vcenter".
Defines text background color
Defines text color
end Mark tag
` |

|                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `
<DefaultMark>
  <Pixmap>custom_marker.png</Pixmap>
  <Align>X\|Y</Align>
  <Color>#</Color>
  <TextColor>#</TextColor>
  <Text> %1 </Text>
</DefaultMark>

` | `begin Mark tag
Optional: Uses an image from the skin's folder to define a custom marker, if available it overrides the default triangle
Defines where text is positioned (X = "left" or "hcenter" or "right"; Y = "top" or "vcenter" or "bottom"). Note: "center" can be used as a shorthand for "hcenter\|vcenter".
Defines text background color
Defines text color
Is filled with Hotcue number when not defined by respective custom mark
end Mark tag
` |

|                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `
<Mark>
  <Control>loop_end_position</Control>
  <Pixmap>custom_marker.png</Pixmap>
  <Text>LOOP OUT</Text>
  <Align>X\|Y</Align>
  <Color>#</Color>
  <TextColor>#</TextColor>
</Mark>

` | `begin Mark tag
Defines a loops end point
Optional: Uses an image from the skin's folder to define a custom marker, if available it overrides the default triangle
Text visible when end point is set (and no custom marker is defined)
Defines where text is positioned (X = "left" or "hcenter" or "right"; Y = "top" or "vcenter" or "bottom"). Note: "center" can be used as a shorthand for "hcenter\|vcenter".
Defines text background color
Defines text color
end Mark tag
` |

|                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `
<MarkRange>
  <StartControl>loop_start_position</StartControl>
  <EndControl>loop_end_position</EndControl>
  <EnabledControl>loop_enabled</EnabledControl>
  <Color>#</Color>
  <DisabledColor>#</DisabledColor>
</MarkRange>

` | `begin MarkRange tag
\
\|---for drawing the color overlay between loop-in & loop-out, these lines are not variable
/
Defines overlay color when loop is enabled
Defines overlay color when loop is disabled
end MarkRange tag
` |

### Waveform overview

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Overview>
  <TooltipId>waveform_overview</TooltipId>
  <Channel>X</Channel>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <BgColor>#AARRGGBB</BgColor>
  <BgPixmap>custom_background.png</BgPixmap>
  <SignalColor>#</SignalColor>
  <SignalLowColor>#</SignalLowColor>
  <SignalHighColor>#</SignalHighColor>
  <SignalLowColor>#</SignalLowColor>
  <EndOfTrackColor>#</EndOfTrackColor>
  <AxesColor>#AARRGGBB</AxesColor>
  <PlayPosColor>#AARRGGBB</PlayPosColor>
  <PlayedOverlayColor>#AARRGGBB</PlayedOverlayColor>
  <Orientation>X</Orientation>
  <MarkerColor>#</MarkerColor>
  <ProgressColor>#</ProgressColor>
  <ProgressAlpha>X</ProgressAlpha>
  <Connection>
    <ConfigKey>[ChannelX],playposition</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
  </Connection>
</Overview>` | `
begin Overview tag
Tooltip to be displayed on mouseover
Which channel the settings are connected to (X=1, 2, or more, depending on the number of decks in the skin)
Defines the element position
Defines the element size
Background color. New in Mixxx 1.9.1: If <BgColor> is not provided, the background is treated as transparent. New in Mixxx 2: Support ARGB notation, e.g. ``#B3000000`` for semi transparent black
New in Mixxx 1.10: Loads a background image and will tile it when smaller than the waveform widget
Color of waveform overview
New in Mixxx 1.11: Colors of low frequencies in waveform overview. If no low/mid/high colors are provided, fallback to <SignalColor>
New in Mixxx 1.11: Colors of mid frequencies in waveform overview
New in Mixxx 1.11: Colors of high frequencies in waveform overview
New in Mixxx 1.11: Color of notification overlay displayed within the last seconds of a track
New in Mixxx 1.11: Color of static horizontal line. New in Mixxx 2: Support ARGB notation
New in Mixxx 1.11: Color of moving vertical line (playing position indicator). New in Mixxx 2: Support ARGB notation
New in Mixxx 2.1: Color of overlay for the played portion of the track. Support ARGB notation
New in Mixxx 2.1: Orientation of waveform overview. (X = "horizontal" or "vertical") Default is horizontal.
Deprecated in Mixxx 1.11: Color of vertical line
Deprecated in Mixxx 1.11 (was new in v1.10): Color of track analysis progress visualization, color defaults to the signal color if not set
Deprecated in Mixxx 1.11 (was new in v1.10): Alpha of track analysis progress visualization, default alpha is 80 out of 255

Must be same value as under <Channel> above, (X = 1 or 2)
Defines if action is performed on click on element ( true or false); Can be omitted in Mixxx >= 2.00

end Overview tag
` |

### Spinning vinyl image (Spinny)

New in Mixxx 1.10.0

|                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<Spinny>
  <TooltipId>spinny</TooltipId>
  <Channel>X</Channel>
  <Size>W,H</Size>
  <PathBackground>background.svg</PathBackground>
  <PathMask>mask.svg</PathMask>
  <PathForeground>foreground.svg</PathForeground>
  <PathGhost>foreground_ghost.svg</PathGhost>
  <ShowCover>true</ShowCover>
</Spinny>
` | `Beginn Spinny tag
Tooltip to be displayed on mouseover
Optionally, defines the appearance of the Spinny widget
Which channel the settings are connected to (X=1, 2, or more, depending on the # of decks in the skin)
Defines the element position
Defines the element size
Background image (from the skin's folder, shows as bottom layer). Sets the spinny's overall size, unless scalemode="STRETCH" is set (New in Mixxx 2.00).
New in Mixxx 2.00: Mask image (from the skin's folder, shows above the cover layer but below the foreground image.  This is often used to overlay a circular outline on top of the cover art so it appears like a round record label.
Foreground image (from the skin's folder, shows as top layer). New in Mixxx 1.11: Center the images according to their own size
Ghost Foreground image (from the skin's folder, shows as top layer on right-click)
New in Mixxx 2.00: Set to true to enable showing of covers in spinny widgets (default false). Spinny background images will only appear if there is no cover art, or if this feature is off.
End Spinny tag
` |

### Volume level display

|                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<VuMeter>
  <TooltipId>channel_VuMeter</TooltipId>
  <PathVu>active.png</PathVu>
  <PathBack>default.png</PathBack>
  <Pos>X,Y</Pos>
  <Horizontal>false</Horizontal>
  <PeakHoldSize>5</PeakHoldSize>
  <PeakHoldTime>400</PeakHoldTime>
  <PeakFallTime>80</PeakFallTime>
  <PeakFallStep>5</PeakFallStep>
  <Connection>
    <ConfigKey>[X],Y</ConfigKey>
  </Connection>
</VuMeter>

` | `begin VuMeter tag
Tooltip to be displayed on mouseover
Button/slider main image (from the skin's folder, shows as top layer)
Button/slider background image (from the skin's folder, shows as bottom layer)
Defines the element position
Orientation (false=vertical, true=horizontal)
Size of peak (in pixels); cropped from top of image defined in <PathVu>, default is 5
Time a peak is displayed (in ms), default is 400
Time a peak falls down (in ms), default is 20
Number of steps (in pixels) a peaks falls down in <PeakFallTime>, Default is 1

Defines connected Channel & Stereo-balance (X = Channel1 .. 4 or Master), (Y= VuMeter or VuMeterL or VuMeterR)

end VuMeter tag
` |

### Volume peak indicator

|                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<StatusLight>
  <TooltipId>PeakIndicator</TooltipId>
  <PathVu>active.png</PathVu>
  <PathBack>default.png</PathBack>
  <Pos>X,Y</Pos>
  <Connection>
    <ConfigKey>[X],PeakIndicator</ConfigKey>
  </Connection>
</StatusLight>

` | `begin StatusLight (Volume Peak Indicator) tag
Tooltip to be displayed on mouseover
peak indicator main image (from the skin's folder, shows as top layer)
peak indicator background image (from the skin's folder, shows as bottom layer)
Defines the element position

Defines connected Channel (X = Channel1 .. 4 or Master)

end StatusLight (Volume Peak Indicator) tag
` |

## Section: Text

### Label

|                                                                               |  |                                                                                                             |
| ----------------------------------------------------------------------------- |  | ----------------------------------------------------------------------------------------------------------- |
| `<Label>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <Text>Hello</Text>
 </Label>
` |  | `
Displays a text label.
Defines the element position
Defines the element size
The text to be displayed


` |

### Clock

New in Mixxx 1.10

|                                                                                                                                                        |  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ |  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Time>
  <TooltipId>time</TooltipId>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <ShowSeconds>false</ShowSeconds>
  <ClockFormat>24</ClockFormat>
</Time>
` |  | `
This widget displays the current time.
Tooltip to be displayed on mouseover
Defines the element position
Defines the element size
Determines, whether seconds are shown ("true") or not ("false"). Default is "false".
Deprecated as of v2.00. We display the time with a format appropriate to the chosen locale instead. Has determined, whether the time is shown in 24 hour format or 12 hour format.
"24" and "24hrs" set the format to 24 hour format. "12", "12hrs" and "12ap" set the format to
12 hour format (e.g. 1:45 am). "12AP" sets it to 12 hour format with capitalized AM/PM
(e.g. 1:45 AM). Default is "12AP". <ShowSeconds> determines, whether seconds are shown or not. Default was false.
You could set a custom format with <CustomFormat> instead of <ClockFormat>, which accepts the same expressions as QTime::toString (https://doc.qt.io/qt-4.8/qtime.html#toString)
` |

### Track information

New in Mixxx 1.9

You can replace the whole \<Text\> node with
[TrackProperty](/creating_skins#trackproperty)\`s to display more
advanced track informations.

|                                                                                                           |  |                                               |
| --------------------------------------------------------------------------------------------------------- |  | --------------------------------------------- |
| `<Text>
  <TooltipId>text</TooltipId>
  <Channel>X</Channel>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
</Text>` |  | `

Defines connected Channel (X = 1 or 2)


` |

### BPM number display

Changed in Mixxx 2.00

Use `visual_bpm` key instead `bpm`

|                                                                                                                                                                                                                                              |  |                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | ---------------------------------------------------------------------------------------------------------------- |
| `<NumberBpm>
  <TooltipId>visual_bpm</TooltipId>
  <Channel>X</Channel>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <NumberOfDigits>6</NumberOfDigits>
  <Connection>
  <ConfigKey>[ChannelX],visual_bpm</ConfigKey>
  </Connection>
</NumberBpm>` |  | `


Defines connected Channel (X = 1 .. 4)




?

Must be same value as under <Channel> above, (X = 1 or 2)



` |

### Effective musical key display

New in Mixxx 2.00

|                                                                                                                                                                                                          |  |                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | --------------------------------------------------------------- |
| `<Key>
  <TooltipId>visual_key</TooltipId>
  <Pos>X,Y</Pos>
  <Size>W,H</Size>
  <DisplayCents>true</DisplayCents>
  <Connection>
  <ConfigKey>[ChannelX],visual_key</ConfigKey>
  </Connection>
</Key>` |  | `






Display the distance to the next key

(X = 1 .. 4)



` |

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

New in Mixxx 2.1

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

New in Mixxx 2.00

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

New in Mixxx 1.9

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

New in Mixxx 1.9  
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

|                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<WidgetGroup>
  <Pos>100,200</Pos>
  <Size>w,h</Size>
  <Layout>horizontal</Layout>
  <BackPath>background.png</BackPath>
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
` | `


Layout widgets horizontally.
New in Mixxx 1.11: Loads a background image from the skin folder. Support resizing and color schemes.
Note: The style sheet is painted on top of the new background set by the <BackPath> node.










` |

The result of this is that the pushbutton and slider will be
automatically sized and laid out horizontally within the widget group.

### Splitter

New in Mixxx 1.11.0

This allows you to create a QSplitter dynamically and to control the
size of child widgets by dragging the boundary between the children.

New in Mixxx 2.10

Allows to specify which children can be collapsed

New in Mixxx 2.00

Remember splitter layout

|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| `<Splitter>
  <Pos>100,200</Pos>
  <Size>w,h</Size>
  <SplitSizesConfigKey>[$skin_name],$config_key</SplitSizesConfigKey>
  <SplitSizes>1,1,8</SplitSizes>
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
` | `  ` |

`SplitSizes` gives the proportional splits between the children of the
'Splitter'. From the example, the first 2 `WidgetGroup`s will each have
10% of the splitter size initially and the 3rd `WidgetGroup` will have
80%. There must be as many split sizes as there are children or else it
will be ignored.

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

New in Mixxx 1.11.0

|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<WidgetStack>
  <NextControl>[Channel1],hotcuepage_next</NextControl>
  <PrevControl>[Channel1],hotcuepage_prev</PrevControl>
  <Children>
    <WidgetGroup trigger="[Channel1],hotcuepage_show1"></WidgetGroup>
    <WidgetGroup trigger="[Channel1],hotcuepage_show2"></WidgetGroup>
    <WidgetGroup trigger="[Channel1],hotcuepage_show3"></WidgetGroup>
    <!-- as many regular widgets as you like in here -->
  </Children>
</WidgetStack>
` | `

Optional: Control that switches to the next widget in the stack. (will be created if doesn't exist)
Optional: Control that switches to the previous widget in the stack. (will be created if doesn't exist)

A WidgetGroup that is shown when the 'trigger' control is set to 1. (will be created if doesn't exist)
A WidgetGroup that is shown when the 'trigger' control is set to 2. (will be created if doesn't exist)
A WidgetGroup that is shown when the 'trigger' control is set to 3. (will be created if doesn't exist)




` |

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

Some examples:

  - Multiple pages of hotcue buttons.
  - A collapsed/expanded view of a deck: two children in a
    `WidgetStack`, one with the full deck widgets and one with the
    collapsed deck widgets. A single `<NextControl>` and a
    `<PushButton>` attached to that control allows the user to toggle
    between the collapsed and expanded view of the deck.
  - Tabbed UIs / Screen Sets. The entire skin could be one large
    `WidgetStack` that lets you switch the UI between different layouts.

New in Mixxx 2.00.0

If you need the stacks to remember which index they were closed with so
they can start back up in the right state, do it like this:

    <WidgetStack currentpage="[EffectRack1],current" persist="true">

The "currentpage" CO doesn't need to be defined anywhere else.

New in Mixxx 2.00.0

You can define which page to select if a group gets a hide signal.
`on_hide_select` adds a page to the stack. If this page is hidden, the
the page with the 0-based index given by on\_hide\_select will be shown.
If this value is -1, the next page on the stack will be shown.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<WidgetStack>
  <Children>
    <WidgetGroup on_hide_select="0"></WidgetGroup>
    <WidgetGroup trigger="[Channel1],hotcuepage_show1" on_hide_select="0"></WidgetGroup>
    <WidgetGroup trigger="[Channel1],hotcuepage_show2" on_hide_select="0"></WidgetGroup>
    <WidgetGroup trigger="[Channel1],hotcuepage_show3" on_hide_select="0"></WidgetGroup>
    <!-- as many regular widgets as you like in here -->
  </Children>
</WidgetStack>
` | `


First page of the stack
When any page is hidden, go back to the first page.
When any page is hidden, go back to the first page.
When any page is hidden, go back to the first page.




` |

### SizeAwareStack

New in Mixxx 2.00.0

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SizeAwareStack>
  <Children>
    <WidgetGroup>
      <MinimumSize>10,10</MinimumSize>
      <MaximumSize>10,10</MaximumSize>
      <Style>QGroupBox {background: blue;}</Style>
    </WidgetGroup>
    <WidgetGroup>
      <MinimumSize>100,10</MinimumSize>
      <MaximumSize>100,10</MaximumSize>
      <Style>QGroupBox {background: red;}</Style>
    </WidgetGroup>
    <WidgetGroup>
      <MinimumSize>200,10</MinimumSize>
      <MaximumSize>200,10</MaximumSize>
      <Style>QGroupBox {background: green;}</Style>
    </WidgetGroup>
  </Children>
</SizeAwareStack>
` | `


A WidgetGroup that is shown when the available screen estate is at least 10x10 pixel.




A WidgetGroup that is shown when the available screen estate is at least 100x10 pixel.




A WidgetGroup that is shown when the available screen estate is at least 200x10 pixel.







` |

A `SizeAwareStack` selects the best fitting widget based on available
space. It allows GUI elements to easily adopt to window size without
manual actions.The algorithm is very basic and requires children sorted
by size, smallest first.

### ComboBox

New in Mixxx 2.00.0

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

Both \<Text\> and \<Icon\> tags are optional. The order in which the
states are displayed is determined by the order they have in the xml,
not by the \<Number\> tag. What does the \<Number\> tag do?

The control object that holds the state of the combobox is determined
with the \<Connection\> tag.

### Singleton widgets

New in Mixxx 2.00.0

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

|                                                                                                                                                                             |                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `   <SingletonDefinition>
    <ObjectName>LibrarySingleton</ObjectName>
    <Children>
      <Template src="skin:library.xml"/>
    </Children>
  </SingletonDefinition>
 ` | `



The skin:prefex is replaced by the skin folder first, if this fails the current directory is used



` |

The ObjectName is used to identify this singleton elsewhere in the skin
files.

Example usage:

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

The skin system sees the Singleton tag, and any time the containing
group gets a show event, the Singleton widget is reparented to this
location in the skin. Note that if a Singleton is visible twice at the
same time, behavior is undefined and could be crashy.

### Skin Preview Image

New in Mixxx 2.1.0

To provide users a rough impression of what skins look like before they
switch to a different skin, show a preview screenshot when a skin is
selected with the combobox in `Preferences --> Interfaces --> Skin`.

The screenshoot should show skins in their default configuration. Save
as `preferences_preview_screenshot.png` in the root folder of the
corresponding skin. Is no screenshoot provided, a placeholder is
displayed.

### Launch Image

New in Mixxx 2.00.0

Mixxx features a default launch image that is shown during Mixxx
launching. It features a centered label with a progress bar below.

All elements are style-able by Qt stylesheets as shown in the example
below:

Example definition:

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

### Battery

New in Mixxx 2.1.0

A a widget to show the laptop battery status.

    <Battery>
      <BackPath>battery_background.png</BackPath>
      <!-- displayed when battery status is unknown -->
      <PixmapUnknown>battery_unknown.png<PixmapUnknown>
      <!-- displayed when battery is full -->
      <PixmapCharged>battery_charged.png</PixmapCharged>
      <!-- number of charging / discharging pixmaps -->
      <NumberStates>10</NumberStates>
      <!-- displayed when battery is charging -->
      <PixmapsCharging>battery_%1_charging.png</PixmapsCharging>
      <!-- displayed when battery is discharging -->
      <PixmapsDischarging>battery_%1_discharging.png</PixmapsDischarging>
    </Battery>

The charging/discharging pixmaps will have %1 replaced from 0 to
NumberStates - 1.

## Deprecated keys

### Main background

Deprecated in Mixxx 1.11.0, use
[WidgetGroup](creating_skins?#widgetgroup) instead

|                                                                                     |                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Background>
  <Path>background.png</Path>
  <BgColor>#</BgColor>
</Background>

` | `start background tag
Defines which image in the skins folder to use for the background. All elements are displayed over this image and its size defines the skin size (see Guidelines)
Defines a background color. Example: <BgColor>#000000</BgColor> (000000 being the hex value for black)
end background tag
` |

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

  - [Skin Colour Scheme
    Architecture](Skin%20Colour%20Scheme%20Architecture) - Explains how
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
