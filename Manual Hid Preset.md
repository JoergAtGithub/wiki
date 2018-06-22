# HID/USB Bulk controller presets

Mixxx doesn't currently have a mapping format for HID or USB
bulk-transfer mode controllers so they must be handled entirely in
script. That said, the procedure to do so is exactly the same as for
[MIDI controllers that use scripting](midi_scripting), but you also add
an `incomingData` function to handle all input from the controller.

The steps are:

1.  [Create your script
    file](midi_scripting#setting_up_a_javascript_mapping_file). The same
    function and file naming conventions as well as init and shutdown
    function requirements apply as with MIDI scripting.
2.  The script file must also contain a function called `incomingData`.
    This will receive all data packets from the controller and is
    responsible for parsing them and taking appropriate actions based on
    which bytes change. It has the same signature as the [inboundSysex
    function in MIDI
    scripting](midi_scripting#system-exclusive_sysex_message_handing_functions).
3.  Create an XML file that tells Mixxx the name of the controller and
    which script file(s) to load, [just like with MIDI
    scripting](midi_scripting#linking_a_javascript_mapping_file_to_an_xml_mapping_file)
    but make sure to end the file name with `.hid.xml` or `.bulk.xml` as
    appropriate.

Read on for more details.

## Script file

Here is an example file containing the required elements:

    var SuperCool = {};
    
    SuperCool.init = function (ID,debugging) {
        // Do setup here
        if (debugging) print("SuperCool "+ID+" initialized!");
    }
    
    SuperCool.shutdown = function () {
        // Do shutdown steps here, like turning off all LEDs
    }
    
    SuperCool.incomingData = function(data,length) {
        // Parse packet data here & call relevant functions
    }

### Packet format

There is no standard HID packet arrangement/structure. The length and
contents (and even
[endianness](https://en.wikipedia.org/wiki/Endianness)) are completely
up to the manufacturer. For input packets, you can watch the incoming
packets in Mixxx's console output when running Mixxx with the
`--controllerDebug` command line option. For output, you can examine the
USB descriptors of the HID device to figure out what packets to send. On
Linux you can use the
[usbhid-dump](https://github.com/DIGImend/usbhid-dump) and
[hidrd-convert](https://github.com/DIGImend/hidrd) tools to show these
descriptors in a human readable format. First, identify the USB product
and vendor ID of your device with lsusb:

    $ lsusb
    Bus 001 Device 004: ID 046d:c52b Logitech, Inc. Unifying Receiver

Here the vendor ID is 046d and the product ID is c52b. Use these with
usbhid-dump:

    usbhid-dump -dVENDORID:PRODUCTID | grep -v : | xxd -r -p | hidrd-convert -o spec

Refer to this
[tutorial](http://eleccelerator.com/tutorial-about-usb-hid-report-descriptors/)
for how to interpret the information from hidrd-convert.

### Sending data to the controller

Once you know what data you want to send, simply call
`controller.send()` with:

  - An array of data bytes to send,
  - null (the second parameter is required for backwards compatibility,
    but it is actually ignored by Mixxx)
  - The HID report ID. If the controller only supports a single report
    packet, set this as 0.

<!-- end list -->

``` javascript
var byteArray = [ byte1, byte2, byte3, ..., byteN ];
controller.send(byteArray,byteArray.length, reportID);
```

## XML file

Here is an example containing everything you need. Just copy and change
the appropriate parts:

    <?xml version="1.0" encoding="utf-8"?>
    <MixxxControllerPreset schemaVersion="1" mixxxVersion="1.11+">
        <info>
            <name>SuperCool HID Controller</name>
            <author>Your Name Here</author>
            <description>HID mapping for the SuperCool controller</description>
            <devices> <!-- Optional section that Mixxx can use to auto-load presets on matching devices -->
                <!-- Get the vendor and product IDs for the controller from your operating system -->
                <product protocol="hid" vendor_id="0x1111" product_id="0x100" />
            </devices>
        </info>
        <controller id="SuperCoolHID">
            <scriptfiles>
                <file filename="SuperCool-Controller.js" functionprefix="SuperCool"/>
            </scriptfiles>
        </controller>
    </MixxxControllerPreset>

There is also an [HID Packet Parser JS](HID%20Packet%20Parser%20JS)
script in the `res/controllers` directory you can examine for parsing
hints. (If you would like to try using it directly, simply add it to the
top of the `scriptfiles` list in your XML file:)

``` 
             <file filename="common-hid-packet-parser.js" functionprefix=""/>
```

However, the structure of this library's code is messy and it may cause
as many hassles to use it as it solves.
