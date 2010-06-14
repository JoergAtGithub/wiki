# Skin Colour Scheme Architecture

  
**Color Scheme Documentation - Work in progress** ---
*[jus](jus/justmail/de) 2010/06/14 09:36*  
\---

  - Complete Scheme in-depth review
  - ~~Add screenshots~~
  - ~~Cleanup outdated content ~~ / Proof reading

## Outline

The main purpose of the filtering architecture is to allow for creation
of different colour schemes for skins. Since creating a new theme from
scratch is a lot of work and involves editing a lot of images, it's not
really very practical to do it just to create a different coloured
version of a skin.

The filtering architecture is implemented as a chain of plugins which
are queried by the user interface code as the skin is initialised. The
filter chain is configured by a series of elements in the skin's
skin.xml file.

## Technical Stuff

So the core of the structure is laid out in imgsource.h. Most filters
will be implemented as an ImgColorProcessor. Some examples are in
imgcolor.cpp. To implement a new ImgColorProcessor you need to create a
new class which implements the function doColorCorrection and performs
some color mapping. The hooks for using the filters in a skin.xml file
are in mixxxview.cpp.

The capability is also there to implement non-colour based filters by
extending ImgProcessor directly, although it's important to note that
the filter is applied to individual pixmaps as they're loaded, not to
the skin as a whole. So for example a blur filter wouldn't blur the
edges of a control outside the rectangle of the pixmap.

## Current Scheme Demo

The only skin with schemes currently is **Outline** & derivates
(outlineNetbook, outlineClose, outlineMini, outlineSmall). You can test
it out by going to the *Interface* tab of the preferences dialog and
changing the scheme to something other than the default.

[[/media/skinning/outlinenetbook_scheme_preferences.png|]]

**Default Color Scheme (Dark Mixxx) for Outline skin**  
[[/media/skinning/outlinenetbook_darkmixxx.png|]]

You should see the colours of the user interface change, for example as
in the scheme shown below.  
**Alternative Color Scheme (Summer Mixxx) for Outline skin**  
[[/media/skinning/outlinenetbook_summermixxx.png|]]

This is what the Outline skin looks like with no (a blank) scheme
applied.

**No (a blank) Color Scheme applied (Classic Mixxx) for Outline skin**  
[[/media/skinning/outlinenetbook_classicmixxx.png|]]

## Scheme Format

To implement schemes in a skin there needs to be a color scheme section
added to the skin.xml. See [Creating
Skins](creating_skins#skinxml_in-depth_reviews) for reference.

General structure of the color scheme section in skin.xml.

| syntax                                                                                                                                                                                                              | Info                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<Schemes>
  <Scheme>
   <Name>Name Scheme #1</Name>
   <Filters>
    <Add>
     <Amount>Value</Amount>
    </Add>
    ... Some more filters ...
   </Filters>
  </Scheme>
  ... Some more schemes ...
</Schemes>
` | `General color scheme opening tag so Mixxx "know"
Opening tag for scheme #1
Naming tag for scheme #1, name will be displayed in Mixxx preferences
Opening tag for filters

Filter Value

optional: add even more filters
Closing tag for filters
Closing tag for scheme #1
optional: add even more schemes 
General color scheme closing tag` |

## Scheme in-depth

FIXME

In this section all elements and the values of their keys are explained
on the example of **Outline**\`s skin.xml. So open up the skin.xml with
your favorite [text editor](creating_skins#tools) and get started

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | ----------------------------------------------- |
| `<Schemes>
    <Scheme>
    <Name>11pm (Dark Mixxx)</Name>
    <Filters>
        <Invert/>
        <HueInv/>
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
    
    <Scheme>
    <Name>5pm (Classic Mixxx)</Name>
    <Filters/>
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
</Schemes>
` |  | `Controls the name of the scheme to be loaded
` |

## Filters

The filters have only been implemented as a quick test so far. At the
moment we have (with their arguments):

  - Invert - Inverts image
  - HueInv - Sets hue to that of inverse. For example inverse followed
    by hueinv is equivalent to a hue invariant inverse.
  - Add - Adds a constant value to all colour components (clipped to
    [0-255](0-255))
  - Amount - Value to add (int)
  - ScaleWhite - Scales low saturation (\<50) colours by a factor
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
