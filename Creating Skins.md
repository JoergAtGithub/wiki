# Creating Skins

Skins can change the look and feel of Mixxx. Some skins merely make the
program more aesthetically pleasing while others rearrange elements of
the interface, potentially making the program easier to use.

### Getting started

A skin for Mixxx is basically a folder with various images and one text
file named skin.xml. The skin.xml defines all the elements (widgets) of
the skin, what the images are used for and and where they are placed on
screen.

Reading this page helps to understand how skins work in Mixxx‚ it will
save you time eventually.

**You can download the most recent source file for the *"Outline*" skin
used in the following example from
[Launchpad](http://bazaar.launchpad.net/~mixxxdevelopers/mixxx/trunk/files/head:/mixxx/res/images/templates/),
which is our project management platform.** The file is GPL-licensed and
free available in SVG format for use with
[Inkscape](/creating_skins#tools).

Start a new skin by navigating to your local [Mixxx resource
folder](/creating_skins#skin_faq), duplicate the "Outline" directory and
rename it. Use the content of the new folder as starting point for your
first skin. Read this page, understand how things were done in Outline's
skin.xml and try to work from there. If you're familiar with HTML, then
you should pretty comfortable editing the skin.xml.

Keep in mind the [Mixxx Skinning
Guidelines](http://mixxx.org/wiki/doku.php/skin_guidelines)

### Things to know

##### Positioning

Images are in the .png format and Mixxx does support png transparency.
Element colors are defined in hexadecimal values.  
Element positions are defined with **X,Y** coordinates (from upper left
). Element sizes are defined with **W,H** values (width,heigh).

[[/media/skinning/creating_skins/mixxx1.9_gui_positioning_outline.png|]]

##### Structure

General structure of the skin.xml. More in-depth informations for each
element and their attributes defined in the skin.xml can be found
[here](#skinxml-in-depth-review)

| syntax                                                                                                                                                                                                                                | Info                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<!--Comment-->
<!DOCTYPE skin>           
<skin>
<elementname>
<tooltips>helpful text</tooltips>
<Style>..</Style>
<position>X,Y</position>
<size>W,H</size>
<options>values(depends)</options>

</elementname>           
</skin>
` | ` Optional comments (i.e. skin license or changelog)
Doctype declaration so Mixxx "know"
Skin opening tag
Elements opening tag
Tooltips to display on mouse-over
Style (depends on the element)
Position on the screen
Size (depending on the element)
Options(depending on the element)
Elements closing tag
Skin closing tag  ` |

### Skin 101

Lets have a look at the Mixxx user interface (with Outline skin
applied). The various elements of the skin are marked and explained
below.

[[/media/skinning/creating_skins/mixxx1.9_gui_explained_outline.png|]]

[1.General](#sectiongeneral-)

  - Skin Colour Scheme - allows the creation of different [colour
    schemes](http://mixxx.org/wiki/doku.php/skin_colour_scheme_architecture)
    of a skin
  - Background picture - Image file which all elements will be displayed
    on
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

[5.Buttons](#sectionbuttons)

  - Play - plays / pauses a song
  - Cue - places a Cue-point at the current position
  - Hotcue - places a Hotcue-point at the current playback position
  - Looping - places start- and endpoint of a loop , enables the loops
    playback
  - Reverse play - toggles reverse playback during regular playback
  - Fast forward/rewind - seeks trough a song fast in both directions
  - Beat sync - automatically match the tempo between two songs
  - Pitch adjustment - apply fine adjustment to the tempo of a song
  - BPM tap - sets the bpm to the average value of the last 4 taps
  - Key lock - activate pitch-independent time stretch
  - Pitch bend - apply a temporary pitch-bend to the tempo of a song
  - Pre-listen - sends the channel's audio to the Headphones
  - Repeat - repeats track if you go past the end or before the start
  - FX (Flanger) - enables a effect on the selected channel
  - Frequency Kill - cuts the high, mid and low frequencies

[6.Knobs (Rotary fader)](#sectionknobs-rotaryfader-)

  - Master Volume - controls the volume and of the master output
  - Balance - controls the balance (stereo distribution) of the master
    output
  - FX (Flanger) settings - controls the different flanger effect
    parameter
  - Headphone volume - controls the volume of the headphone output
  - Headphone mix - controls what you hear on the headphone output
  - Gain - apply extra amplification to a song
  - Channel filter - perform equalization on the high, mid and low
    frequencies

[7.Special nodes (not displayed)](#special-nodes-)

  - TrackProperty - pull advanced informations from tracks and display
    them
  - WidgetGroup - make a group of relatively positioned widgets

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
    
    Doublecheck that the skin.xml is in the "NewSkin" root folder and not in a subfolder, otherwhise Mixxx may throw an error when starting that skin.
    
    3. Start Mixxx , goto "Preferences-->Interface" and select "Skin-->NewSkin"
       Make sure you have "Waveform Display-->Waveform" selected
       Save preferences with OK.   
    
    4. The new skin should now be displayed.
    
    5. Done.

#### How to resize a skin

As of Mixxx 1.9 it is not possible to resize a skin automatically, Mixxx
can not handle skins resolution independent. Every skin needs to be
redrawn by hand. The [Outline skin
template](/creating_skins#getting_started) guides you and helps to makes
it easier.  
Example: Your skin is 1024×768 but your screen is 1280×1024. When going
into fullscreen Mixxx will fill your screen around the 1024×768 used by
the skin with the skin\`s background color. This background color is
defined in skin.xml using the \<*Horizontal\>* key . See [Main
background](#main-background).  
So if you would like to have your skin fill the whole screen ( i.e. to
have more space for the library), you need another variant of your skin
for 1280×1024.  
Also see the [Skin guidelines](/skin_guidelines).

#### How to change the size of the library

Same thing as with resizing a skin , as of Mixxx 1.9 it is not possible
to resize the library automatically. You need another variant of your
skin  
Also see the [Skin guidelines](/skin_guidelines).

#### How to change the players orientation (vertical or horizontal)

As of Mixxx 1.9 this is not possible. You can change the orientation of
Volume level display & Fader using the \<*Horizontal\>* key. See
[Channel volume](#channel-volume).

#### How to change the font size or color for the text (i.e. artist)

Use the \<*Style\>* key and Qt Style Sheets to define text attributes.
See [Track information](#track-information).

#### How to change the font size or font color for the playlist

Use the \<*Style\>* key and Qt Style Sheets to define text attributes.
See example. See [Library display](#library-display)

#### How to change the size or color of the waveform

The values are defined in skin.xml using the \<*Pos\>* and
\<*SignalColor\>* key. See [Waveform](#waveform).

#### How to use a custom symbol for markers ( i.e. Hotcues)

Custom symbols for markers can be defined for Hotcues, Cues , LoopIn and
LoopOut in skin.xml using the \<*Pixmap\>* key. See
[Waveform](#waveform).  
Notice that your custom markers only show up in the big waveforms.

#### How to use sliders instead of knobs ( i.e. for eq\`s )

~~All elements that are sliders could be knobs an vis a vis. Think of
some house hardware mixers , sometimes you have no channel line fader
(slider) but rather rotary fader (knobs).  
Same for EQ\`s , they could be slider instead knobs.~~ Is that really
possible?FIXME

### Skin licensing & copyright

The principles on licensing found [on the Creative Common
Wiki](http://wiki.creativecommons.org/Before_Licensing) apply for other
licenses too.

If you are going to make a skin from scratch , think about which license
to choose for your work. Make sure you have **the rights** to apply the
license.  
Popular choices are [GPL](http://www.gnu.org/licenses/gpl.html) and
[Creative Common](http://creativecommons.org/) license.

**The skins license must be compatible with the
[DebianFreeSoftwareGuidelines](http://wiki.debian.org/DFSGLicenses) or
they can not be distributed with Mixxx. **  
If you are going to make a skin based on others work, make sure you
comply with their license terms. If you are not sure, why not ask the
original author?

It is a good idea to put the license terms of your skin as a comment on
top of the skin.xml (see examples).

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | ------------------------- |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Example CC by-sa 3.0 licensed skin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  | Example GPL licensed skin |
| `<!--
Name / Version of your skin, Skin for Mixxx 1.9.x
www.mixxx.org
Copyright (C) 2011 you name , your@email.adress
    
based on the "Name of the original skin"
Copyright (C) 2011 name of the original author, authors@email.adress
  
This file is part of the "Name of your skin" Skin for Mixxx 1.9.x
"Name of your skin" is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported license.
http://creativecommons.org/licenses/by-sa/3.0/
     
You are free:
to Share - to copy, distribute and transmit the work
to Remix - to adapt the work
        
Under the following conditions:
Attribution - You must attribute the work in the manner specified by the author or licensor 
(but not in any way that suggests that they endorse you or your use of the work).

Share Alike - If you alter, transform, or build upon this work, you may distribute 
the resulting work only under the same or similar license to this one.
-->` | `<!--
Name / Version of your skin, Skin for Mixxx 1.9.x
www.mixxx.org
Copyright (C) 2011 you name , your@email.adress

based on the "Name of the original skin"
Copyright (C) 2011 name of the original author, authors@email.adress

This file is part of "Name of your skin".
"Name of your skin" is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

http://www.gnu.org/licenses/gpl.html
-->


` |  |                           |

Further reads:

  - [Which CC license to choose](http://creativecommons.org/choose/)
  - [Non-commercial licenses vs open
    licenses](http://www.appropedia.org/Non-commercial_licenses_vs_open_licenses)
  - [Frequently Asked Questions about the GNU
    GPL](http://www.gnu.org/licenses/gpl-faq.html) 

### Tools

  - Free Text editors - Online ([Piratepad](http://piratepad.net/),
    [Google Docs](http://docs.google.com/)), Windows
    ([Pspad](http://www.pspad.com/)), Mac OSX
    ([Textwrangler](http://www.barebones.com/products/textwrangler/)),
    Linux (Kate, Gedit)
  - Free Images editors - Online
    ([Phoenix](http://aviary.com/tools/phoenix),
    [Pixlr](http://www.pixlr.com/)), Windows
    ([Paint.net](http://www.getpaint.net/),
    [Gimp](http://gimp-win.sourceforge.net/) ) Mac OSX
    ([Pixelmator](http://www.pixelmator.com/) -trial-), Linux (Gimp,
    Inkscape)
  - Free color tools - Online ([Color Palette
    Generator](http://bighugelabs.com/colors.php),
    [Colorblender](http://www.colorblender.com/) , [Color Scheme
    Designer](http://colorschemedesigner.com/))
  - Free knob tools - Windows only, MacOSX & Linux via
    [Wine](http://www.winehq.org/)
    ([Knobman](http://www.g200kg.com/en/software/knobman.html), [Knob
    Render](http://www.otiumfx.com/knobrender))
  - Convert a Mixxx skin.xml into HTML to be viewed with a web browser -
    Windows, MacOSX & Linux ([XSL
    Helper](/creating_skins#convert_a_mixxx_skinxml_into_html))

# Skin.xml in-depth review

In this section all elements and the values of their keys are explained
on the example of **Outline** skin.  
So open up the skin.xml in the Outline folder with your favorite [text
editor](#tools) and get started :-)

## Changes

### Mixxx 1.9.1

  - Extended Mixxx to support now 36 [hotcues](creating_skins#hotcue)
    (was 32 between Mixxx 1.8.0-1.9.0)

### Mixxx 1.9.0

  - added [advanced styling options](/creating_skins#library_display)
    for library
  - added [TrackProperty](/creating_skins#trackproperty) node
  - added [WidgetGroup](/creating_skins#widgetgroup) node
  - added [BPM tap](/creating_skins#bpm_tap) button
  - added [Key lock](/creating_skins#key_lock) button
  - added [Repeat](/creating_skins#repeat) button
  - removed [End of track mode](/creating_skins#end_of_track_mode)
    button

## Section: General

### Skin Colour Scheme

Allows the creation of different color schemes, see [Color scheme
architecture](http://mixxx.org/wiki/doku.php/skin_colour_scheme_architecture)
for details

### Main background

|                                                                                       |                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Background>
    <Path>background.png</Path>
    <BgColor>#</BgColor>
</Background>` | `The size of this image defines the skins overall size, see Guidelines
Defines the background picture all the elements will displayed on
Defines a background color ( Example: # = #000000) 
#00000 is hex value for black` |

### Library display

New in Mixxx 1.9.0  
You can use [Qt Style
Sheets](http://doc.qt.nokia.com/latest/stylesheet.html) to customize the
appearance of the library widget like:

``` 
  * Custom images for splitter and checkboxes in library
  * Custom images for branch triangle in treeview
  * Visual feedback when searchbox has focus
  * General appearance of text and buttons in library & tooltips
```

See also [Qt Style Sheets
Examples](http://doc.qt.nokia.com/latest/stylesheet-examples.html) and
the [Spartan Skin for
Mixxx 1.9](http://mixxx.org/forums/viewtopic.php?f=8&t=1812) as
blueprint, it makes heavy use of Qt Style Sheets.

|                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<TableView>
    <Style>...</Style>
    <Pos>X,Y</Pos>
    <Size>W,H</Size>
    <BgColor>#</BgColor>
    <FgColor>#</FgColor>
    <BgColorRowEven>#</BgColorRowEven>
    <BgColorRowUneven>#</BgColorRowUneven>
</TableView>` | `
Defines the appearance of the library widget
Defines the elements position
Defines the elements size
Background color library widget (i.e. background color search widget)
Foreground color library widget (i.e. text in "Analyze" widget)
Background color even line right library pane 
Background color uneven lines right library pane


` |

## Section: Visual

### Waveform

|                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<Visual>
    <Tooltip>Helpful text</Tooltip>
    <Channel>X</Channel>
    <Pos>X,Y</Pos>
    <Size>W,H</Size>
    <BgColor>#</BgColor>
    <HfcColor>#</HfcColor>
    <SignalColor>#</SignalColor>
    <BeatColor>#</BeatColor>        
    <BeatHighlightColor>#</BeatHighlightColor>
    <MarkerColor>#</MarkerColor>
    <CueColor>#</CueColor>
<Visual>` | `
Tooltip to be displayed on mouse-over. Use the "&#10;" entity (without quotes) for line break
Defines which channel the settings are connected to (X = 1 or 2 )  

 
Color of waveform background (default gradient added , not for #000000)
Color of horizontal line 
Color of waveform  
Color of beatgrid (multiple vertical lines) 
Highlight color when beatgrid is near playback position 
Default color center marker (single vertical line)
Default color of Cuepoint marker 

` |

|                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ` <Mark>
        <Control>cue_point</Control>
        <Pixmap>custom_marker.png</Pixmap>
        <Text>CUEPOINT</Text>
    <Align>Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
</Mark>  ` | `
Defines the Cuepoint , max. one cuepoint per channel 
Optional: Defines a custom marker for given element, if available it overrides the default triangle
Text visible when Cuepoint is set (and no custom marker is defined)
Defines where text is positioned (Y=top or center or bottom) 
Defines text background color 
Defines text color

` |

|                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Mark>
        <Control>hotcue_X_position</Control>
        <Pixmap>custom_marker.png</Pixmap>
        <Text>HOTCUE X</Text>
    <Align>Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
</Mark>` | `
max. 36 Hotcues(X=1-36), define every Hotcue for its own 
Optional: Defines a custom marker for given element, if available it overrides the default triangle
Text visible when Hotcue point is set (and no custom marker is defined)
Defines where text is positioned (Y= top or center or bottom) 
Defines text background color 
Defines text color

` |

|                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Mark>
        <Control>loop_start_position</Control>
        <Pixmap>custom_marker.png</Pixmap>
        <Text>LOOP IN</Text>    
    <Align>Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
</Mark>` | `
Defines a loops starting point
Optional: Defines a custom marker for given element, if available it overrides the default triangle
Text visible when starting point is set (and no custom marker is defined)
Defines where text is positioned (Y= top or center or bottom)
Defines text background color
Defines text color

` |

|                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Mark>
        <Control>loop_end_position</Control>
        <Pixmap>custom_marker.png</Pixmap>
    <Text>LOOP OUT</Text>
    <Align>Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
</Mark>` | `
Defines a loops end point
Optional: Defines a custom marker for given element, if available it overrides the default triangle
Text visible when end point is set (and no custom marker is defined)
Defines where text is positioned (Y= top or center or bottom)
Defines text background color
Defines text color

` |

|                                                                                                                                                                                                                                                              |                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `<MarkRange>
        <StartControl>loop_start_position</StartControl>
        <EndControl>loop_end_position</EndControl>
        <EnabledControl>loop_enabled</EnabledControl>
    <Color>#</Color>    
    <DisabledColor>#</DisabledColor>
  </MarkRange>` | `Draws a color overlay between loop-in & loop-out



Defines overlay color when loop is active
Defines overlay color when loop is in-active

` |

### Waveform overview

|                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Overview>
    <Tooltip>Helpful text</Tooltip>
    <Channel>X</Channel>
    <Pos>X,Y</Pos>
    <Size>W,H</Size>
    <BgColor>#</BgColor>
    <SignalColor>#</SignalColor>
    <MarkerColor>#</MarkerColor>
    <Connection>
    <ConfigKey>[ChannelX],playposition</ConfigKey>
    <EmitOnDownPress>false</EmitOnDownPress>
    </Connection>
</Overview>` | `

Which channel the settings are connected to (X= 1 or 2)


Background color
Color of waveform overview
Color of vertical line (playing position indicator)

Must be same value as under <Channel> above, (X = 1 or 2)
Defines if action is performed on click on element ( true or false)


` |

### Volume level display

|                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<VuMeter>
    <Tooltip>Helpful text</Tooltip>
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
</VuMeter>` | `

Button/slider main image = top layer
Button/slider background image = bottom layer

Orientation (false or true, means vertical or horizontal)
Size of peak cropped from top of <PathVu> grafik (in pixel) / Default is 5
Time a peak is displayed (in ms) / Default is 400
Time a peak falls down (in ms) / Default is 20
Number of steps a peaks falls down in <PeakFallTime> / Default is 1

Defines connected Channel & Stereo-balance (X = Channel1 or Channel2 or Master),
(Y= VuMeter or VuMeterL or VuMeterR)

` |

### Volume peak indicator

|                                                                                                                                                                                                                                             |                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `<StatusLight>
    <Tooltip>Helpful text</Tooltip>
    <PathVu>active.png</PathVu>
    <PathBack>default.png</PathBack>
    <Pos>X,Y</Pos>
    <Connection>
    <ConfigKey>[X],PeakIndicator</ConfigKey>
    </Connection>
</StatusLight>
` | `





Defines connected Channel (X = Channel1 or Channel2 or Master)


` |

## Section: Text

### Track information

New in Mixxx 1.9  
You can replace the whole \<Text\> node with
[TrackProperty](/creating_skins#trackproperty)\`s to display more
advanced track informations.

|                                                                                                                                                                                           |  |                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Text>
    <Tooltip>Helpful text</Tooltip>
    <Channel>X</Channel>
    <Pos>X,Y</Pos>
    <Size>W,H</Size>
    <Style>font; bg-color; color; text-align; padding;
    </Style>
</Text>` |  | `

Defines connected Channel (X = 1 or 2)


Uses CSS. Example=font: bold 13px/15px Lucida Grande, Lucida Sans Unicode, 
Arial, Verdana, sans-serif; background-color: transparent; color: #0099FF; 
text-align: left; padding-left: 1%;
` |

### BPM number display

|                                                                                                                                                                                                                                                                                                                           |  |                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | -------------------------------------------------------------------------------------------------------------- |
| `<NumberBpm>
    <Tooltip>Helpful text</Tooltip>
    <Channel>X</Channel>
    <Pos>X,Y</Pos>
    <Size>W,H</Size>
    <Style>font; bg-color; color; text-align; (padding);
    </Style>
    <NumberOfDigits>6</NumberOfDigits>
    <Connection>
    <ConfigKey>[ChannelX],bpm</ConfigKey>
    </Connection>
</NumberBpm>` |  | `

Defines connected Channel (X = 1 or 2)




?

Must be same value as under <Channel> above, (X = 1 or 2)


` |

### Playing position / Time remaining

|                                                                                                                                                                                                                                                                                                                                    |  |                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | -------------------------------------------------------------------------------------------------------------- |
| `<NumberPos>
    <Tooltip>Helpful text</Tooltip>
    <Channel>X</Channel>
    <Pos>X,Y</Pos>
    <Size>W,H</Size>
    <Style>font; bg-color; color; text-align; (padding);
    </Style>
    <NumberOfDigits>6</NumberOfDigits>
    <Connection>
    <ConfigKey>[ChannelX],playposition</ConfigKey>
    </Connection>
</NumberPos>` |  | `

Defines connected Channel (X = 1 or 2)




?

Must be same value as under <Channel> above, (X = 1 or 2)


` |

### Pitch rate display

|                                                                                                                                                                                                                                                                                                                                     |  |                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | -------------------------------------------------------------------------------------------------------------- |
| `<NumberPos>
    <Tooltip>Helpful text</Tooltip>
    <Channel>X</Channel>
    <Pos>X,Y</Pos>
    <Size>W,H</Size>
    <Style>font; background-color; color; text-align; (padding);
    </Style>
    <NumberOfDigits>6</NumberOfDigits>
    <Connection>
    <ConfigKey>[ChannelX],rate</ConfigKey>
    </Connection>
</NumberPos>
` |  | `

Defines connected Channel (X = 1 or 2)




?

Must be same value as under <Channel> above, (X = 1 or 2)


` |

## Section: Slider

### Channel Volume

|                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SliderComposed>
    <Tooltip>Helpful text</Tooltip>
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



` |

### Crossfader

|                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SliderComposed>
    <Tooltip>Helpful text</Tooltip>
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
Slider background image the <Handle> moves left  and righ on

Orientation (false or true, means vertical or horizontal)

Use always default value



` |

### Pitch control

|                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SliderComposed>
    <Tooltip>Helpful text</Tooltip>
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

Defines connected Channel (X = 1 or 2 )



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

### Play

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text for both states</Tooltip>
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


First states action
Defines connected Channel (X = 1 or 2) , performed action (play)
Defines if action is performed on down-click on element (true or false)
Which mouse button must be clicked so the action is performed 

Second states action
Defines connected Channel (X = 1 or 2) , performed action (cue_set)
Defines if action is performed on down-click on element (true or false)
Which mouse button must be clicked so the action is performed
 

` |

### Cue

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<PushButton>
    <Tooltip>Helpful text for all states</Tooltip>
    <NumberStates>1</NumberStates>
    <State>
    <Number>0</Number>
    <Pressed>pressed.png</Pressed>
    <Unpressed>unpressed.png</Unpressed>
    </State>
    <State>
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
</PushButton> 
` | `
Go to and play (while playing), Set cue point (while stopped), Go to and stop (right-click)









Defines connected Channel (X = 1 or 2) , performed action (cue_default)
Defines if action is performed on down-click on element (true or false)
Which mouse button must be clicked so the action is performed 
Hint: Default cue behavior can be changed in Mixxx preferences

Defines connected Channel (X = 1 or 2) , performed action (cue_gotoandstop)
Defines if action is performed on down-click on element (true or false)
Which mouse button must be clicked so the action is performed 


` |

### Hotcue

**Hint**: Hotcues can utilize more functions in the *\<ConfigKey\>* then
shown in this example. See [MIDI Controller Mapping File
Format](midi_controller_mapping_file_format#ui_midi_controls_and_names)
for details

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text for all states</Tooltip>
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


Channel (X=1 or 2), Hotcue # (Y=1-36) & performed action (clear)

Which mouse button must be clicked so the action is performed


` |

### Looping

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text</Tooltip>
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text</Tooltip>
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<PushButton>
    <Tooltip>Helpful text</Tooltip>
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text for all states</Tooltip>
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text for all states</Tooltip>
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text for all states</Tooltip>
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text for all states</Tooltip>
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text for all states</Tooltip>
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

### Prelisten / Monitoring

|                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text</Tooltip>
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
Headphone prelisten for Channel X



Default button visible




Button visible when active




Defines connected Channel (X = 1 or 2) , performed action (beatsync)


` |

### BPM tap

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>...</Tooltip>
    <Style>...</Style>
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
and sets the bpm of the deck to that valu








Defines connected Channel (X = 1 or 2) , performed action








` |

### Key lock

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text</Tooltip>
        <Style>...</Style>
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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text</Tooltip>
    <Style>...</Style>
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














Defines connected Channel (X = 1 or 2) , performed action



` |

### End of track mode

**Abandoned in Mixxx 1.9.0, use the [Repeat](creating_skins#repeat)
button instead**

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<PushButton>
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
` | `
End of track mode control (see manual)



Button visible in STOP mode




Button visible in NEXT mode




Button visible in LOOP mode




Defines connected Channel (X = 1 or 2) , performed action (TrackEndMode)


` |

### FX (Flanger)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<PushButton>
    <Tooltip>Helpful text</Tooltip>
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




Defines connected Channel (X = 1 or 2) , performed action (flanger)


` |

### Frequency Kill

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text</Tooltip>
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
Cuts the high, mid and low frequencies on Channel X



Default button visible




Button visible when active




Defines connected Channel (X = 1 or 2), 
performed action (Y= filterHighKill or filterMidKill or filterLowKill)



` |

## Section: Knobs (RotaryFader)

### Master volume & balance

|                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<Knob>
    <Tooltip>Helpful text</Tooltip>
    <NumberStates>X</NumberStates>
    <Path>knob_rotary_s%1.png</Path>
    <Pos>X,Y</Pos>
    <Connection>
    <ConfigKey>[Master],Y</ConfigKey>
    </Connection>
</Knob>` | `
You need X single knobs where #(X/2)+1 is the 0-state. 
Example: X=41 states (270 degree rotation / 40 knobs + the 0-state) . 
You need 20 knobs rotate from -135 degree to 0 degree, one knob 0 degree (default knob visible) ,  
20 knobs rotate from -135 degree to 0 degree

Defines connected Channel (Master) , performed action (Y=volume or balance)


` |

### Flanger (FX) setting

|                                                                                                                                                                                                                           |                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `<Knob>
    <Tooltip>Helpful text</Tooltip>
    <NumberStates>X</NumberStates>
    <Path>knob_rotary_s%1.png</Path>
    <Pos>X,Y</Pos>
    <Connection>
    <ConfigKey>[Flanger],Y</ConfigKey>
    </Connection>
</Knob>` | `





Defines connected Channel (Flanger),
performed action (Y=lfoDelay or lfoDepth or lfoPeriod)

` |

### Headphone volume and mix

|                                                                                                                                                                                                                           |                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `<Knob>
    <Tooltip>Helpful text</Tooltip>
    <NumberStates>X</NumberStates>
    <Path>knob_rotary_s%1.png</Path>
    <Pos>X,Y</Pos>
    <Connection>
    <ConfigKey>[Flanger],Y</ConfigKey>
    </Connection>
</Knob>` | `





Defines connected Channel (Master), performed action (Y=headVolume or headMix)


` |

### Channel filter and gain

|                                                                                                                                                                                                                      |                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `<Knob>
    <Tooltip>Helpful text</Tooltip>
    <NumberStates>X</NumberStates>
    <Path>knob_rotary_s%1.png</Path>
    <Pos>X,Y</Pos>
    <Connection>
    <ConfigKey>[X],Y</ConfigKey>
    </Connection>
</Knob>
` | `





Defines connected Channel (X = 1 or 2), 
performed action (Y= pregain or filterHigh or filterMid or filterLow)

` |

## Special nodes

Check out the [Spartan Skin for
Mixxx 1.9](http://mixxx.org/forums/viewtopic.php?f=8&t=1812) as
blueprint, it makes use of these special nodes.

### TrackProperty

New in Mixxx 1.9  
Replace the [Text](/creating_skins#track_information) node with
TrackProperty\`s to display more advanced track informations. You can
display more than one TrackProperty node in a skin. |\<code=xml\>
\<TrackProperty\>

``` 
    <Tooltip>...</Tooltip>
    <Style>...</Style>
    <Property>...</Property>
    <Channel>X</Channel>
    <Pos>x,y</Pos>
    <Size>a,b</Size>
 </TrackProperty>
```

\</code\>|`



The "Property" field can be any of:
artist, title, album, genre, year, track_number, times_played, comment,
bpm, bpmFormatted, duration, durationFormatted

bpm will be the full precision number (i.e. 1.333333333) while
bpmFormatted is to 3 decimal places (1.333),
duration is the duration in seconds, while durationFormatted is the
duration in hh:mm:ss.xx format. 
`|

### WidgetGroup

New in Mixxx 1.9  
It is probably cumbersome to have to give the absolute positions of
every node in the tree. WidgetGroups allow to make a group of relatively
positioned widgets. You can display more than one WidgetGroup node in a
skin.

|                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<WidgetGroup>
  <Pos>100,200</Pos>
  <Size>w,h</Size>
  <Children>
    <PushButton>
      <Pos>0,0</Pos>
    </PushButton>
    <SliderComposed>
      <Pos>20, 0</Pos>
    </SliderComposed>
    <!-- as many regular widgets as you like in here -->
  </Children>
</WidgetGroup>
` | `


<size> is optional, this will limit the size so that any part of a 
child widget outside of the size rectangle is not shown


In that example, the PushButton child will be at 0,0 relative to its parent, 
or the absolute position 100,200. 
The SliderComposed widget will be at 20,0 relative to its parent or 120,200. 





` |

# Convert a Mixxx skin.xml into HTML

The skin.xsl file (contributed by Dave Jarvis) in the "skins" directory
allows you to do XSL transform which converts a Mixxx skin.xml into
HTML, to be viewed with a web browser. In plain English: it lets you
preview a skin in your web browser so you don't have to restart Mixxx
every time you make a change. Very useful if you're creating a skin.

The XSL file can be used by running xsltproc like so:

``` 
  xsltproc skin.xsl skin.xml > skin.html
```

This is what the output looks like (plain Outline skin with no color
scheme applied)

[[/media/skinning/creating_skins/mixxx1.9_xsl_skin.html.png|]]

# Useful Links

  - [Skin Colour Scheme
    Architecture](Skin%20Colour%20Scheme%20Architecture) - Explains how
    colour schemes work in Mixxx 1.6.0+
  - [Mixxx Skinning
    Guidelines](http://mixxx.org/wiki/doku.php/skin_guidelines)
