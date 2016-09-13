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
up to the manufacturer.

#### Input

You'll need to either obtain the HID spec from the manufacturer, or run
Mixxx with the `-``-controllerDebug` parameter and note which bytes
change (and how) as you operate controls. (Some HID controllers also
send data (like time stamps) even when sitting still.)

#### Output

Due to the arbitrary nature of HID packets, how to affect outputs (like
LEDs, displays, screens, etc.) is a total guessing game without the
spec. If you've not been able to get it from the manufacturer, your best
bet is to run a USB/HID packet sniffing program on an OS and DJ software
that are supported by them to see what data is transmitted from the
software to the controller and make notes.

:\!: **Warning:** Using a trial-and-error "brute force" method of
sending random bytes to the controller to see what happens is
discouraged because you may inadvertently send a "firmware update"
message and render the controller permanently inoperable short of
factory repair.

### Sending data to the controller

Once you know what data you want to send, simply call
`controller.send()` with:

  - An array of data bytes to send,
  - The number of bytes in the array (start counting at 1 or just use
    the .length property as below,)
  - (Optional) the HID report ID (0 by default.) Most controllers only
    support a single report ID (of 0) so you can ignore this.

<!-- end list -->

``` javascript
var byteArray = [ byte1, byte2, byte3, ..., byteN ];
controller.send(byteArray,byteArray.length);
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

There is also an experimental HID packet parser script in the
`res/controllers` directory you can examine for parsing hints. (If you
would like to try using it directly, simply add it to the top of the
`scriptfiles` list in your XML file:)

``` 
             <file filename="common-hid-packet-parser.js" functionprefix=""/>
```
