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
