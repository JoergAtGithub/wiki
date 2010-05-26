# Creating Skins

-----

  
**Skinning Documentation - Work in progress** ---
*[jus](jus@justmail.de) 2010/05/25 17:16*  
<span class="underline">todo:</span>  
\* Cleanup Wiki syntax

  - Howto install skins
  - FAQ
  - Licensing
  - Update Skinning Guidelines
  - Proof reading

-----

  
Skins can change Mixxx\`look and feel‚ some skins merely make the
program more aesthetically pleasing while others rearrange elements of
the interface, potentially making the program easier to use.

### Getting started

A skin for Mixxx is basically a folder with various images and one text
file named skin.xml. The skin.xml defines all the elements (widgets) of
the skin, what the images are used for and and where they are placed on
screen.

Reading this page helps to understand how skins work in Mixxx‚ it will
save you time eventually.

**You can download the *ShadeDark* skin used in the following example
[here](http://mixxx.org/forums/viewtopic.php?f=8&t=918) .**

To start a new skin, copy the "ShadeDark" directory, rename it to
something else and use that as the starting point for your new skin.Look
at how things were done in ShadeDark's skin.xml and try to work from
there. If you're familiar with HTML, then you should pretty comfortable
editing the skin.xml.

Keep in mind the [Mixxx Skinning
Guidelines](http://mixxx.org/wiki/doku.php/skin_guidelines)

Images are in the .png format and Mixxx does support png transparency.
Element colors are defined in hexadecimal values.  
Element positions are defined with **X,Y** coordinates (from upper left
). Element sizes are defined with **W,H** coordinates (width,heigh).

[[/media/mixxx1.8_gui_positioning_shadedark.png|]]

### Tools

Free Text editors - Online ([Piratepad](http://piratepad.net/), [Google
Docs](http://docs.google.com/)), Windows
([Pspad](http://www.pspad.com/)), Mac OSX
([Textwrangler](http://www.barebones.com/products/textwrangler/)), Linux
(Kate, Gedit)  
Free Images editors - Online
([Phoenix](http://aviary.com/tools/phoenix),
[Pixlr](http://www.pixlr.com/)), Windows
([Paint.net](http://www.getpaint.net/),
[Gimp](http://gimp-win.sourceforge.net/) ) Mac OSX
([Pixelmator](http://www.pixelmator.com/) -trial-), Linux (Gimp,
Inkscape)  
Free color tools - Online ([Color Palette
Generator](http://bighugelabs.com/colors.php),
[Colorblender](http://www.colorblender.com/) , [Color Scheme
Designer](http://colorschemedesigner.com/))  
Free knob tools - Windows only, MacOSX & Linux via
[Wine](http://www.winehq.org/)
([Knobman](http://www.g200kg.com/en/software/knobman.html), [Knob
Render](http://www.otiumfx.com/knobrender))

### Mixxx skin overview

Lets have a look at the Mixxx user interface (with ShadeDark skin
applied). The various elements of the skin are marked.

[[/media/mixxx1.8_gui_explained_shadedark.png|]]

[1.General](#sectiongeneral-)

  - Skin Colour Scheme - not used in our example, this advance technique
    allows the creation of different [colour
    schemes](http://mixxx.org/wiki/doku.php/skin_colour_scheme_architecture)
    for skins
  - Background picture - Image file which all elements will be displayed
    on
  - Library display - Widget holds all your music information,
    playlists, search bar etc.

[2.Visual](#sectionvisual-)

  - Waveform - shows the loaded tracks waveforms near the playback
    position
  - Waveform overview - shows a waveform visualisation of the whole song
  - Volume level display - shows the playback volume of the song /
    master
  - Peak indicator‚ shows if a songs / master volume is too high

[3.Text](#sectiontext)

  - Track information - shows some ID3 information of the song ( Name,
    Artist )
  - BPM Information - shows the tempo of the song
  - Playing position / Time remaining‚ shows current playback position
    or remaining tome (can be selected im preferences)
  - Pitch rate information- shows how much the song is speed up / slowed
    down (in percent)

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
  - Pitch bend - apply a temporary pitch-bend to the tempo of a song
  - Pre-listen - sends the channel's audio to the Headphones
  - End-of-track-mode - defines behaviour when playback reaches the end
    of a track
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

# skin.xml in-depth

| General skin.xml element syntax                                                                                                                | Info                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<elementname>
<position>X,Y</position>
<size>W,H</size>
<options>values(depends)</options>
<tooltips>helpful text</tooltips>
</elementname>
` | ` Elements opening tag
Position on the screen
Size (depending on the element)
Options(depending on the element)
Tooltips to display on mouse-over
Elements closing tag  ` |

## Section: General

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

|                                                                                                                                                                                                        |                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<TableView>
    <Pos>X,Y</Pos>
    <Size>W,H</Size>
    <BgColor>#</BgColor>
    <FgColor>#</FgColor>
    <BgColorRowEven>#</BgColorRowEven>
    <BgColorRowUneven>#</BgColorRowUneven>
</TableView>` | `
Defines the elements position
Defines the elements size
Background color library widget 
Foreground color library widget 
Background color even line right library pane 
Background color uneven lines right library pane

` |

## Section: Visual

### Waveform

|                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
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
    <!--<FisheyeColor>#</FisheyeColor>-->
    <Zoom>true</Zoom>
<Visual>` | `
Tooltip to be displayed on mouse-over 
Defines which channel the settings are connected to (X = 1 or 2 )  

 
Color of waveform background (default gradient added , not for #000000)
Color of horizontal line 
Color of waveform  
Color of beatgrid (multiple vertical lines) 
Highlight color when beatgrid is near playback position 
Default color center marker (single vertical line)
Default color of Cuepoint marker 
? 
?

` |

|                                                                                                                                                               |                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ` <Mark>
        <Control>cue_point</Control>
        <Text>CUEPOINT</Text>
    <Align>Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
</Mark>  ` | `
Defines the Cuepoint , max. one cuepoint per channel 
Text visible when Cuepoint is set 
Defines where text is positioned (Y=top or center or bottom) 
Defines text background color 
Defines text color

` |

|                                                                                                                                                                    |                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Mark>
        <Control>hotcue_X_position</Control>
        <Text>HOTCUE X</Text>
    <Align>Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
</Mark>` | `
max. 32 Hotcues(X=1-32), define every Hotcue for its own 
Text visible when Hotcue point is set 
Defines where text is positioned (Y= top or center or bottom) 
Defines text background color 
Defines text color

` |

|                                                                                                                                                                         |                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<Mark>
        <Control>loop_start_position</Control>
        <Text>LOOP IN</Text>    
    <Align>Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
</Mark>` | `
Defines a loops starting point
Text visible when starting point is set
Defines where text is positioned (Y= top or center or bottom)
Defines text background color
Defines text color

` |

|                                                                                                                                                                |                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Mark>
        <Control>loop_end_position</Control>
    <Text>LOOP OUT</Text>
    <Align>Y</Align>
    <Color>#</Color>
    <TextColor>#</TextColor>
</Mark>` | `
Defines a loops end point
Text visible when end point is set
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
Defines if action is performed on klick on element ( true or false)


` |

### Volume level display

|                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
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

Graphics displayed when active
Default  graphics displayed

Orientation (false or true, means vertical or horizontal)
Size of peak cropped from top of <PathVu> grafik (in pixel)
Time a peak  is displayed (in ms)
Time a peak falls down (in ms)
Number of steps a peaks falls down in <PeakFallTime>

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

### Channel Volume

|                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SliderComposed>
    <Tooltip>Helpful text</Tooltip>
    <Handle>handle.png</Handle>
    <Slider>slider.png</Slider>
    <Pos>X,Y</Pos>
    <Horizontal>false</Horizontal>
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

### Channel Volume

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

### Play

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
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
` | `Left Click: Pause/Play, Right Click: Set cue point
Overall quantity of states the button have

First state
Default image displayed
Image displayed on mouse-down


Second state
Default image displayed
Image displayed on mouse-down


First states action
Defines connected Channel (X = 1 or 2) , performed action (play)
Defines if action is performed on klick on element (true or false)
Which mouse button must be clicked so the action is performed 

Second states action
Defines connected Channel (X = 1 or 2) , performed action (cue_set)
Defines if action is performed on klick on element (true or false)
Which mouse button must be clicked so the action is performed 


` |

### Cue

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `<PushButton>
    <Tooltip>Helpful text for all states</Tooltip>
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
` | `Go to and play (while playing), Set cue point (while stopped), Go to and stop (right-click)

` |

### Hotcue

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
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







Channel (X=1 or 2), Hotcue # (Y=1-32) & performed action (activate), 
depends on  # of Hotcues defined , see hotcue_X_position
Action is performed while playing (true) on klick on element



Action is performed while stopped (false) on klick on element
Which mouse button must be clicked so the action is performed


Channel (X=1 or 2), Hotcue # (Y=1-32) & performed action (clear)

Which mouse button must be clicked so the action is performed


` |

### Looping

|  |  |
|  |  |
|  |  |

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

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
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




Defines connected Channel (X = 1 or 2) , performed action (Y=end or start)




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

### End of track mode

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

## Skin.xsl

The skin.xsl file (contributed by Dave Jarvis) in the "skins" directory
allows you to do XSL transform which converts a Mixxx skin.xml into
HTML, to be viewed with a web browser. In plain English: it lets you
preview a skin in your web browser so you don't have to restart Mixxx
every time you make a change. Very useful if you're creating a skin.

The XSL file can be used by running xsltproc like so:

``` 
  xsltproc skin.xsl skin.xml > skin.html
```

This is what the output looks like:

[Xsltpreview.png](/Image/Xsltpreview.png)

## Useful Links

  - [Skin Colour Scheme
    Architecture](Skin%20Colour%20Scheme%20Architecture) - Explains how
    colour schemes work in Mixxx 1.6.0+
  - [Mixxx Skinning
    Guidelines](http://mixxx.org/wiki/doku.php/skin_guidelines)
