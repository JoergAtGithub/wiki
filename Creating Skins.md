# Creating Skins

**Help write this page\!** If you're interested in helping others write
skins, share your knowledge and tips in the page below.

## Starting

If you crack open "C:/Program Files/Mixxx/skins/outline/skin.xml"
(/usr/share/mixxx/skins/outline/skin.xml on Linux) in a text editor,
you'll see the file that describes the layout of the default "outline"
skin. Also located in the "outline" directory is each image that's
present in the skin.

Images are in the .png format and Mixxx does support png transparency.

If you're familiar with HTML, then you should pretty comfortable editing
the *skin.xml*.

To start a new skin, I'd suggest doing is copying the "outline"
directory, renaming it to something else, and then using that as the
starting point for your new skin.

In general, look at how things were done in outline's skin.xml, and try
to work from there.

## Skin.xml

A *skin.xml* file contains a list of all the "widgets" present in each
skin, along with their positions and extra data needed to describe them.

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
