# Skin Guidelines

This page will eventually contain useful guidelines to consider when
creating skins. In the meantime, it's just a brainstorming session on
the topic.

## Resolution

Mixxx should eventually handle skins of different sizes/resolutions in
an elegant way, but in the meantime skin authors need to take the
resolution of their skin seriously. Most DJs will be using Mixxx on a
laptop, which means it'll likely have a widescreen display (with a
limited vertical resolution).

  - [Laptop Screen Resolution
    Guide](http://www.geek.com/laptop-screen-size-resolution/)

[GameGod](/User/GameGod) 21:03, 25 November 2007 (PST)

Also taking into account the window menu/title bar and the system bars,
you should think about making your skin resolution slightly less tall.
In a related note, the possibility of adding a checkbox for "Always on
top" would be nice so that wouldn't be an issue. While "Always on top"
wouldn't solve the menu bar and title bar issue, it would solve the
system bar issue. If we wanted to, we could create a menu inside of
Mixxx and be able to move it around the skin to get rid of the title
bar/menu bar entirely. [DJSynthe](/User/DJSynthe) 23:25, 25 November
2007 (CST)

### The optimal size for Skins

#### Intro

One of the biggest drawbacks of the current skinning engine (as of Mixxx
1.8) is that it **can not handle skins resolution independent**. Every
skin needs to be redrawn by hand which is a lot of work for skin
designers.

Here are some suggestions for skin designers what may be the best skin
size for the targeted screen resolution. It is based on user feedback
for skins i made and measurements on the different platforms Mixxx is
available for.

#### Goal

The goal is to have some kind of **standard** so skin designers have a
**starting point** when they start drawing a skin.

Mixxx is available for different Operations Systems (OS) - but every OS
handles the window decoration differently.

Imho the whole interface should be completely visible to the user even
when not in full screen mode. So the effective **skin dimensions depends
on the usable free space** on the OS with the biggest window decoration.
Which is Linux with the Gnome desktop environment.

#### Example

Default window decoration as seen on the *Outline Netbook 1024x768*
skin  
Notice how different the available vertical space on the screen is. |

| MacOSX                                      | Linux / Gnome                                | Linux / KDE                                | Windows XP                                   | Windows 7                                   |  |
| ------------------------------------------- | -------------------------------------------- | ------------------------------------------ | -------------------------------------------- | ------------------------------------------- |  |
| [[/media/skinning/skin_resolution_tut_osx2.png|]] | [[/media/skinning/skin_resolution_tut_gnome.png|]] | [[/media/skinning/skin_resolution_tut_kde.png|]] | [[/media/skinning/skin_resolution_tut_winxp.png|]] | [[/media/skinning/skin_resolution_tut_win7.png|]] |  |

#### Fullscreen Mode

Default window decoration for various Operating Systems

|                            |        |        |        |        |        |
| -------------------------- | ------ | ------ | ------ | ------ | ------ |
|                            | MacOSX | Gnome  | KDE    | WinXP  | Win7   |
| Taskbar Top                | 0      | 0      | 0      | 0      | 0      |
| Window Titlebar            | 0      | 0      | 0      | 0      | 0      |
| Window decoration Top      | 0      | 25     | 24     | 20     | 22     |
| Window decoration Bottom   | 0      | 0      | 0      | 0      | 0      |
| Taskbar Bottom             | 0      | 0      | 0      | 0      | 0      |
| **Horizontal decorations** | **0**  | **25** | **24** | **20** | **22** |
|                            |        |        |        |        |        |
| Window decoration left     | 0      | 0      | 0      | 0      | 0      |
| Window decoration right    | 0      | 0      | 0      | 0      | 0      |
| **Horizontal decorations** | **0**  | **0**  | **0**  | **0**  | **0**  |

#### Window Mode (Non-Fullscreen)

Default window decoration for various Operating Systems

|                            |        |         |        |        |        |
| -------------------------- | ------ | ------- | ------ | ------ | ------ |
|                            | MacOSX | Gnome   | KDE    | WinXP  | Win7   |
| Taskbar Top                | 22     | 25      | 0      | 0      | 0      |
| Window Titlebar            | 22     | 22      | 24     | 22     | 30     |
| Window decoration Top      | 0      | 25      | 24     | 20     | 22     |
| Window decoration Bottom   | 0      | 3       | 8      | 4      | 8      |
| Taskbar Bottom             | 0      | 25      | 30     | 30     | 30     |
| **Vertical decorations**   | **44** | **100** | **86** | **76** | **90** |
|                            |        |         |        |        |        |
| Window decoration left     | 0      | 3       | 4      | 4      | 8      |
| Window decoration right    | 0      | 3       | 4      | 4      | 8      |
| **Horizontal decorations** | **0**  | **6**   | **8**  | **8**  | **16** |

Note: If a window in Win7 is maximized the horizontal decoration is only
2\*4 instead 2\*8 pixel.

Max. Horizontal Pixel lost:8 (**subtract 2x8 pixel for max. Skin
width**)  
Max. Vertical Pixel lost:100 (**subtract 100 pixel for max. Skin
height**)

#### Which resolution to choose?

|                  |       |        |                 |       |        |
| ---------------- | ----- | ------ | --------------- | ----- | ------ |
| Screen Dimension | Width | Height | Skin Dimensions | Width | Height |
| Netbook          | 1024  | 600    | \=              | 1008  | 500    |
| XGA – standard   | 1024  | 768    | \=              | 1008  | 668    |
| WXGA – wide      | 1280  | 800    | \=              | 1264  | 700    |
| WXGA+ - wide     | 1440  | 900    | \=              | 1424  | 800    |
| SXGA – standard  | 1280  | 1024   | \=              | 1264  | 924    |
| SXGA+ - standard | 1400  | 1050   | \=              | 1384  | 950    |
| WSXGA+ - wide    | 1680  | 1050   | \=              | 1664  | 950    |
| UXGA – standard  | 1600  | 1200   | \=              | 1584  | 1100   |
| WUXGA – wide     | 1920  | 1200   | \=              | 1904  | 1100   |

#### Conclusion

As a skin designer you will have less work afterwards if you choose the
right dimension for your skin.  
More contribution from other users based on your good work may follow.

Have a look at the documentation on [how to create
skins](creating_skins) and start drawing ;-)  
\--- *[jus](jus@justmail.de) 2010/05/26 04:06*

## Waveform Display and Waveform Summaries

The waveform display should be central to any skin. I personally think
it's the heart of Mixxx. It's the thing you're going to be keeping an
eye on when you're DJing, along with the waveform summaries (the little
progress indicators). Skins should be designed so that the waveform and
summary are clearly visible when the DJ is several feet away from their
laptop. Quite often I've found myself having my laptop sitting in an
awkward spot, and being able to see the waveform display is key. (See
[KickAdamKegger20070405](KickAdamKegger20070405) for pics - that laptop
is miles away from my Hercules.) [GameGod](/User/GameGod) 21:03, 25
November 2007 (PST)

I also think it would be a good idea to include flashers for waveforms
for when the song is nearing an end (would be configurable in the
options). [DJSynthe](/User/DJSynthe) 23:25, 25 November 2007 (CST)

## Layout

I think artists can be fairly flexible when it comes to skin layouts.
Besides the size of the waveform display being important, many DJs have
mentioned that they like the library table/view being as big as
possible. (See the mixxx-devel archive when we were brainstorming for
the new library interface back in May 2007.) Another thing I think
people should consider is whether or not to have their layout mimic the
layout of an actual DJ mixer. If you're a DJ experimenting with Mixxx,
you'll probably find it easier to learn if the layout of the controls is
similar to a DJ mixer. (Maybe we should get some pictures of common
mixers like the Pioneer DJM-800?) That being said, mixing with digital
audio on a laptop is a bit of a paradigm shift, and there may be ways to
better organize stuff (keeping it both logical and easy to use).
[GameGod](/User/GameGod) 21:03, 25 November 2007 (PST)

## Colours

Colours are less of an issue thanks to Adam's great colour scheme
support, but there's one golden rule that should still be followed for
any default colour scheme: **Keep your skins dark\!** DJs are going to
be using Mixxx in clubs with very dim lighting, and it kills your eyes
to stare at a bright screen. The darker the skin, the easier it will be
on DJs' eyes. It's also important to keep fonts, text labels, and the
library view visible against a dark background. I'd leave this up to the
artist to figure out, but keep in mind that some fonts are way easier to
read than others when they're small. [GameGod](/User/GameGod) 21:03, 25
November 2007 (PST)

It might be a good idea to be able to change the background color when
you go into fullscreen mode (not sure if this is a windows only thing
where it fills up the rest of your screen with bright grey).
[DJSynthe](/User/DJSynthe) 23:25, 25 November 2007 (CST)

## XML File Structure

Possible ideas for future XML structures

Separate XML files:

\-Base XML-

  - declaring skin version number and minimum version of Mixxx (possibly
    in doctype)
  - declaring color scheme sets
  - declaring included resolution XML files
  - declaring buttons/knobs/sliders (names, functions, tooltips, etc)

\-Per Resolution XML-

  - sets backdrop image
  - sets locations for said named elements
  - possible new structure for anchoring images from bottom and right as
    well as top and left
  - overwrite element images for a specific resolution

[DJSynthe](/User/DJSynthe) 23:25, 25 November 2007 (CST)

## New Element Ideas

  - Sampler (8 samples?) - We already have a good idea of how the
    sampler will be incorporated into the UI, shouldn't require any
    mandatory modifications to skins [GameGod](/User/GameGod) 20:57, 21
    December 2007 (PST)
  - Tabbed Interface possibility (specifically to make low res DJ
    laptops more usable - ie Asus EEE PC 800x480) - one tab for play
    control, one for library management.

[DJSynthe](/User/DJSynthe) 23:25, 25 November 2007 (CST) + 28 Nov. 2007

## Other stuff

If you've thought of other ideas that won't fit under any of the above
headings, create a new one\! :)
