## Overview

Creating a new skin from scratch is a lot of work and involves editing a lot of
images - not very sensible when merely creating a different colored version of
a skin. The color filtering architecture in Mixxx makes it easy to create
a differently colored version of a skin.

## Tips and Tools

For a "walkthrough" on creating schemes, see [Skin Color Schemes Tips
and Tool](Skin%20Color%20Schemes%20Tips%20and%20Tool). It also contains
a link to an online Javascript tool that will help determine correct
HSVTweak values.

## Color Scheme Demo

Mixxx comes pre-loaded with several skins, some of which support color
schemes.

How to change a skin and the skins color scheme in Mixxx:

  - Go to `Options` -\> `Preferences` -\> Interface`
  - Select one of the skins like in the picture below 
  - Select a scheme from the drop down menu and click *Apply*/*OK*

If you select a skin that does not support color schemes, the *Scheme*
drop-down menu is grayed out.

**Default Color Scheme (Classic) for Shade skin (Depicted here for Mixxx
2.3)**  
[[/media/skinning/color_scheme/capture_2019-02-17_09-35-53_am.png|]]

**Alternative Color Scheme (Dark) for Shade skin (Depicted here for
Mixxx 2.3)**  
[[/media/skinning/color_scheme/capture_2019-02-17_09-36-35_am.png|]]  

## Technical Stuff

There are two basic techniques of color changing implemented:
* color filtering, for changing the colors of pixmaps
* a color schema [style sheet](https://github.com/mixxxdj/mixxx/wiki/Creating-Skins#qss-style)  

Additionally, you can use [variables](https://github.com/mixxxdj/mixxx/wiki/Creating-Skins#using-variables) to make widget templates use different source images, for example configuring pushbutton icons. Check [skin.xml](https://github.com/mixxxdj/mixxx/blob/2.3/res/skins/LateNight/skin.xml#L122) of the LateNight skin in Mixxx 2.3: schemes adjust waveform colors, font sizes and many other aspects of skin widgets.

The color filtering architecture is implemented as a chain of plugins
which are queried by the user interface code as the skin is initialised.
The filter chain is configured by a series of elements in the skin's
[skin.xml](creating_skins#skinxml_in-depth_reviews) file.

So the core of the structure is laid out in [src/skin/imgsource.h](https://github.com/mixxxdj/mixxx/blob/main/src/skin/imgsource.h).
Most filters
will be implemented as an ImgColorProcessor. Some examples are in
[src/skin/imgcolor.cpp](https://github.com/mixxxdj/mixxx/blob/main/src/skin/imgcolor.cpp). To implement a new ImgColorProcessor you need to create a
new class which implements the function doColorCorrection and performs
some color mapping. The hooks for using the filters in a skin.xml file
are in [src/skin/colorschemeparser.cpp](https://github.com/mixxxdj/mixxx/blob/main/src/skin/colorschemeparser.cpp).

The capability is also there to implement non-color based filters by extending
ImgProcessor directly, although it's important to note that the filter is
applied to individual pixmaps as they're loaded, not to the skin as a whole. So
for example a blur filter wouldn't blur the edges of a control outside the
rectangle of the pixmap.


### Scheme Format

To implement schemes in a skin there needs to be a color scheme section
added to the skin.xml. See [Creating
Skins](creating_skins#skinxml_in-depth_reviews) for reference.

General structure of the color scheme section in skin.xml.
``` xml
<Schemes>     // General color scheme opening tag to tell Mixxx the skin supports color schemes
    <Scheme>  // Opening tag for Scheme#1 (default scheme)
        <Name>11pm (Dark Mixxx)</Name> // Scheme name
        <Filters>     // Opening tag for color filters
            <Invert/> // Invert filter, inverts the skins original images (i.e. white to black)
            <HueInv/> // Hue Invert Filter, sets hue to that of the inverted images
            <Add>     // Look at the "Filters" section for the specific filters and their arguments
                <Amount>50</Amount> // Filter value
            </Add>
            <ScaleWhite>
                <Amount>1.5</Amount>
            </ScaleWhite>
            <Add>
                <Amount>-50</Amount>
            </Add>
        </Filters>    // Closing tag for color filters
    </Scheme>
    
    <Scheme> // Another scheme
        <Name>5pm (Classic Mixxx)</Name>
        <Filters/>    // blank filter,the skins original images too be shown
    </Scheme>
    
    <Scheme>
        <Name>8pm (Summer Sunset Mixxx)</Name>
        <Filters>
            <HSVTweak>
                <SMin>100</SMin>
                <VFact>0.7</VFact>
                <HFact>0.3</HFact>
            </HSVTweak>
            <HSVTweak>
                <SMax>50</SMax>
                <HFact>0</HFact>
                <HConst>50</HConst>
                <SConst>120</SConst>
                <VConst>-10</VConst>
            </HSVTweak>
        </Filters>
    </Scheme>
    
    <Scheme>
        <Name>3am (Still Awake Mixxx)</Name>
        <Filters>
            <Invert/>
            <Add>
                <Amount>50</Amount>
            </Add>
            <ScaleWhite>
                <Amount>1.5</Amount>
            </ScaleWhite>
            <Add>
                <Amount>-50</Amount>
            </Add>
        </Filters>
    </Scheme>
</Schemes>      // general closing tag for color schemes
```


### Filters

The filters have only been implemented as a quick test so far. At the
moment we have (with their arguments):

  - Invert - Inverts image
  - HueInv - Sets hue to that of inverse. For example inverse followed
    by hueinv is equivalent to a hue invariant inverse.
  - Add - Adds a constant value to all color components (clipped to
    [0-255](0-255))
  - Amount - Value to add (int)
  - ScaleWhite - Scales low saturation (\<50) colors by a factor
  - Amount - Factor to multiply by (float)
  - HSVTweak - Manipulate the Hue Saturation Value (HSV values),
    probably the most useful one
  - HMin - Minimum hue to modify
  - HMax - Maximum hue to modify
  - SMin, SMax, VMin, VMax - As above but for saturation and brightness
  - HFact, SFact, VFact - Factor to scale values by
  - HConst, SConst, VConst - Constant to add to values

You can experiment in your [Image editor](creating_skins#tools) to get
the "right" values for the filters or try the [Color Scheme
Designer](http://colorschemedesigner.com/) online.