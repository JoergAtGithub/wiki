# Skin Colour Scheme Architecture

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

## Config File

In the [Config](Config) section a line like:

Scheme schemename

Controls the name of the scheme to be loaded although this generally
will not be modified by hand but through the preferences dialog

## Current Scheme Demo

The only skin with schemes currently is outlineSmall. If you are using
outlineSmall and latest SVN you can test it out by going to the GUI tab
of the preferences dialog and changing the scheme to something other
than the default. You may need to do a make install as the skin.xml has
changed. You should see the colours of the user interface change, for
example as in the dark scheme shown below:

[Darkskindemo.png](/Image/Darkskindemo.png)

## Skin Format

To implement schemes in a skin there needs to be a tag added along these
lines:

\<Schemes\>

    <Scheme>
     <Name>Dark Scheme</Name>
     <Filters>
      <Add>
       <Amount>36</Amount>
      </Add>
      ... Some more filters ...
     </Filters>
    </Scheme>
    ... Some more schemes ...

\</Schemes\>

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
  - HSVTweak - Manipulate hsv values, probably the most useful one
  - HMin - Minimum hue to modify
  - HMax - Maximum hue to modify
  - SMin, SMax, VMin, VMax - As above but for saturation and brightness
  - HFact, SFact, VFact - Factor to scale values by
  - HConst, SConst, VConst - Constant to add to values
