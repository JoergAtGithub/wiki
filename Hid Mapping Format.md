# HID Controller Mapping File Format

***This specification is in discussion. Details may change before the
specification is finalized.***

## Introduction

Support for additional HID controllers can be added to Mixxx by creating
a new "mapping" file. This file tells Mixxx how to translate data bytes
from a controller into commands that Mixxx will understand (by mapping
the bytes onto [MixxxControls](MixxxControls) or script functions.)

The mapping files are located in the following paths:

  - Windows: C:\\Program Files\\Mixxx\\controllers
  - Linux: /usr/share/mixxx/controllers (or
    /usr/local/share/mixxx/controllers)
  - OS X: /Applications/Mixxx.app/Contents/Resources/controllers

By far, the easiest way to create a new mapping is by copying and
modifying any of the XML files that ship with Mixxx using the
information on this page. When you've finished creating your mapping,
**please send it to us** and we'll include it in Mixxx.

## Sniffing your controller

If you don't have the HID spec for your controller, first check the
manufacturer's web site under Support. Look for Manuals or User Guides.
HID specs may appear in an appendix at the back of the manual. Failing
that, you can usually sniff the data the controller sends with the
following procedure:

1.  Start Mixxx (1.11.0 and later) from a command prompt using the
    `--controllerDebug` option like so: 

<!-- end list -->

  - Linux: `user@machine:~$ mixxx --controllerDebug`
  - Windows: (v1.7.0 and later) `C:\Program Files\Mixxx>mixxx
    --controllerDebug`
  - Mac OSX: `$ open -a mixxx --args --controllerDebug`

<!-- end list -->

1.  Look at the output

<!-- end list -->

  - Watch the console output or look at the
    [Mixxx.log](troubleshooting#where_is_the_mixxxlog_file) file which
    will contain all of the HID byte packets Mixxx receives. As you
    manipulate the controller, the packets it sends will be printed to
    the screen/logged to the file. Compare subsequent packets to
    discover which button/slider/control affects what bit(s)/byte(s)
    (and the
    [endianness](http://www.google.com/url?sa=t&rct=j&q=endianness&source=web&cd=1&ved=0CDAQFjAA&url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FEndianness&ei=-pplT7v7CYL74QSy8MCjCA&usg=AFQjCNEcYWBropgp-Eoe84G6njx-XOfysg&cad=rja)
    if multiple bytes are affected.)
  - FIXME *Add example here*

<!-- end list -->

1.  Add the byte offset, bit offset, length and endianness values to a
    `<control>` block in the XML file. This is detailed in the next
    section.

## File Format

Mixxx uses a well-defined XML format to store its HID mappings. Details
are embedded in the XML example below.

### Header

The first part of the file defines the version of the mapping (for
future compatibility, as Mixxx abilities become more complex) and an
optional info tag which contains information about the preset (primarily
used for distribution of presets.)

    <?xml version="1.0" encoding="utf-8"?>
        <MixxxControllerPreset schemaVersion="0.1" mixxxVersion="1.11.0"> <!-- Schema version number to help compatibility, should the format change -->
        <info><!-- Optional - information about the preset file -->
            <name>Example HID mapping for Mixxx</name>
            <author>Sean M. Pappalardo</author>
            <description>This is an example XML HID preset for Mixxx. This description is intended for distribution and could include comments about the extent of the functionality.</description>
        </info>

### Controller definition

The core part of the file contains a definition for a single controller.
There may be multiple controllers in one file (for more complex setups).

``` 
    <controller id="controller name" type="HID"> <!-- Many controllers in one file supported. A controller should only appear once. -->
```

The "controller id" is the brand & model of the controller, e.g. "EKS
Otus".

### Controls section

``` 
      <controls> <!-- One control group -->
        <control> <!-- Several controls -->
```

If your controller can send different types of messages, you can specify
which type this `<controls>` block interprets using the following
format:

``` 
      <controls byteoffset=0 value=0x01> <!-- Optional format that specifies what value the specified byte must have in order to use this block to interpret the packet. -->
        <control>
```

#### MixxxControl

Group and key define the part of Mixxx that you want to affect. For a
list of what these values can be, see the [MixxxControls](MixxxControls)
page.

``` 
          <group>[Master]</group>
          <key>crossfader</key>
```

#### Controller control

Use one of the following examples to map the above MixxxControl to a
controller's control (knob, button, switch, pad, etc.)

##### Single-byte controls

Many controls are represented by a single byte. Here is how to define
one in the XML.

``` 
          <byteoffset>1</byteoffset> <!-- Offset from the first byte in the packet. So 1 points to the second byte in the packet. -->
          <length>1</length> <!-- Optional - Number of bytes that this control affects. The default is 1. -->
          <min>0x00</min> <!-- Optional - Lowest value of this byte when the control is at its minimum setting. The default is 0x00. -->
          <max>0xFF</max> <!-- Optional - Highest value of this byte when the control is at its maximum setting. The default is 0xFF. -->
```

##### Multiple-byte controls

Many controls are represented by multiple bytes. Here is how to define
such a control in the XML.

``` 
          <byteoffset>2</byteoffset> <!-- Offset from the first byte in the packet, regardless of endianness. So 2 points to the third byte in the packet. -->
          <length>2</length> <!-- Number of bytes that this control affects. -->
          <endian>little</endian> <!-- Optional - Little endian means the most significant byte is the last one (second in this case.) "little" is the default. -->
          <min>0x0000</min> <!-- Optional - Lowest value of these bytes when the control is at its minimum setting. 0 is the default. -->
          <max>0x01FF</max> <!-- Optional - Highest value of these bytes when the control is at its maximum setting. 0xFFFF is the default for two bytes. -->
```

##### Bit-level controls

Some controls are represented by individual bits (typically the case for
buttons.) Here is how to define them in the XML.

``` 
          <byteoffset>4</byteoffset> <!-- Offset from the first byte in the packet. So 4 points to the third byte in the packet. -->
          <bit>6</bit> <!-- Bit number in the byte (8 bits.) Bit 1 is the rightmost one, bit 8 is the leftmost (high) bit. -->
          <length>1</length> <!-- Optional - Number of bits that make up this control. A single-bit value is either on or off. 1 bit is the default. -->
```

#### Finish up

Close each `<control>` block with the following code:

``` 
        </control>
```

...and the `<controls>` block with the following (after all of the
`<control>` blocks):

``` 
      </controls>
```

### Finish up

Close the `<controller>` block with the following code:

``` 
    </controller>
```

...and the whole preset block with the following:

``` 
     </MixxxControllerPreset>
```
