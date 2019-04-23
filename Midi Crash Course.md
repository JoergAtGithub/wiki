# MIDI Crash Course

MIDI (Musical Instrument Digital Interface) is a standard for electronic
musical devices to communicate. This page is a brief introduction to
MIDI that should explain what you need to know to [map MIDI controllers
to Mixxx](start#controller%20mapping%20documentation).

MIDI is a widely used standard that a lot of hardware and software
support. It dates back to the 1980s when it was used to make
synthesizers, samplers, and sequencers communicate. These older devices
used cables with 5-pin DIN connectors to carry MIDI signals. Most MIDI
devices today send the MIDI signals over a USB cable. Some modern
devices can also can use cables with the 5-pin DIN connectors. DJ
controllers with these 5-pin DIN connectors do not ordinarily use them
to send signals to the computer; they are used to communicate via MIDI
with other gear and the ability to use MIDI without being plugged into a
computer (although they need to be plugged into another power source
without a USB cable supplying power).

Controllers that comply with the USB MIDI class standard (also called
"class compliant" devices) do not require any special drivers. Most
controllers are USB MIDI class compliant, but not all. See the [Mixxx DJ
Hardware Guide](hardware%20compatibility) for information about
particular controllers.

Mixxx displays the numbers in MIDI signals in hexadecimal. If you are
unfamiliar with hexadecimal numbers, read [this
tutorial](http://codemastershawn.com/2014/04/03/understanding-binary-and-hex-numbers).

An explanation of the MIDI signals that your controller sends to
computers and how it reacts to MIDI signals that computers send to it
should be available from the controller manufacturer. This is likely in
a document on the product page for your controller on the manufacturer's
website or in the support section of the website. If it is not in a
separate document, it is likely at the end of the manual. Unfortunately,
not every manufacturer provides this information.

## MIDI Messages

Most MIDI messages are three bytes long. The first byte of any MIDI
message is called the **Status** byte. The first nybble (hex digit) is
the op-code and the second is the MIDI channel number. So if you have
`0x90` the op-code is `0x9` and the channel number is `0x0` (Ch 1.) The
full list of MIDI messages is below, where *n* represents the channel
number (0..F inclusive):

| Status     | Function                  | Data bytes         |                   |
| ---------- | ------------------------- | ------------------ | ----------------- |
| **0x8*n*** | **Note off**              | **Note number**    | **Note velocity** |
| **0x9*n*** | **Note on**               | **Note number**    | **Note velocity** |
| 0xAn       | Polyphonic after-touch    | Note number        | Amount            |
| **0xB*n*** | **Control/mode change**   | **Control number** | **Value**         |
| 0xC*n*     | Program change            | Program number     | (n/a)             |
| 0xD*n*     | Channel after-touch       | Amount             | (n/a)             |
| **0xE*n*** | **Pitch wheel**           | **LSB**            | **MSB**           |
| 0xF0       | System Exclusive message  | Vendor ID          | (data)            |
| 0xF1       | MIDI Time Code Qtr. Frame | (see spec)         |                   |
| 0xF2       | Song Position Pointer     | LSB                | MSB               |
| 0xF3       | Song Select               | Song number        | (n/a)             |
| 0xF4       | Undefined                 |                    |                   |
| 0xF5       | Undefined                 |                    |                   |
| 0xF6       | Tune request              | (n/a)              |                   |
| 0xF7       | End of SysEx (EOX)        | (n/a)              |                   |
| 0xF8       | Timing clock              | (n/a)              |                   |
| 0xF9       | Undefined                 | (n/a)              |                   |
| 0xFA       | Start                     | (n/a)              |                   |
| 0xFB       | Continue                  | (n/a)              |                   |
| 0xFC       | Stop                      | (n/a)              |                   |
| 0xFD       | Undefined                 | (n/a)              |                   |
| 0xFE       | Active Sensing            | (n/a)              |                   |
| 0xFF       | System Reset              | (n/a)              |                   |

The boldface entries in the table above are the messages we are most
concerned with since most DJ controllers use only these for all
functions. You'll need to consult the MIDI spec for the DJ controller
you're working with to determine which messages and note/control numbers
correspond to the DJ controller functions & LEDs. If your controller's
MIDI spec gives only note names and not numbers, [use this
table](http://www.wavosaur.com/download/midi-note-hex.php) to convert
them. To convert from decimal to hex, [use
this](http://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html).

(Note that in order to use System Exclusive messages, you will need
[MIDI Scripting](MIDI%20Scripting).)

## Typical MIDI signals used by DJ controllers

Every controller works differently, but these are some typical patterns.

### Buttons

  - When pressed: Op-code `0x9`, value of `0xf7`
  - When released: Op-code `0x9`, value of `0x00`
  - or Op-code `0x8`, value of `0x00`

### LEDs

If there's a LED behind the button, usually it can be controlled by
sending a message to the controller using the same status and note
number that the controller sends when the button is pressed. As for the
value field, for LEDs that can only be turned on or off, typically
`0x00` turns it off and `0x01` or `0x7F` turns it on. For multi-color
LEDs, the color is typically controlled by sending different values.
Which ones correspond to which colors should be in the MIDI
specification document for your controller. If they are not, you will
have to look at mappings for other DJ software, or just try a few
different values.

### Knobs & sliders

These usually send messages with an op-code of `0xB` and a value
corresponding to the absolute position of the knob or slider (between
`0x00` and `0x7F`

Endless knobs/encoders (that you can turn continuously) typically send
messages with an op-code of `0xB` and the value only indicates whether
the encoder is being turned left or right (`0x01` & `0x7F` or `0x41` &
`0x3F`)

### Jog wheels, touch strips, platters

These usually operate exactly like endless knobs/encoders above, and
they usually also send messages just like buttons above when they're
touched or released which is intended to mark when scratching begins and
ends respectively.

## Sniffing your controller with Mixxx

*First, try using the MIDI Learn functionality in the Preferences-\>MIDI
Devices window at the bottom. It will help you get many of the essential
functions mapped quickly without having to manually edit XML.*

Unfortunately, some manufacturers do not provide information about the
MIDI signals used by the controllers they make. In that case, you have
to see what signals the controller sends to be able to map it, which you
can do with Mixxx. Even if the manufacturer does provide MIDI
documentation, it may be easier to sniff your controller with Mixxx than
keep looking up numbers in the controller's documentation.

1.  Start Mixxx from a command prompt using the `--controllerDebug`
    option like so: 

<!-- end list -->

  - Linux: `user@machine:~$ mixxx --controllerDebug`
  - Windows: `C:\Program Files\Mixxx>mixxx --controllerDebug`
  - Mac OSX: `$ open -a mixxx --args --controllerDebug`

<!-- end list -->

1.  Look at the output

<!-- end list -->

  - Watch the console output or look at the
    [Mixxx.log](troubleshooting#where_is_the_mixxxlog_file) file which
    will contain all of the MIDI messages Mixxx receives. As you
    manipulate the controller, the MIDI commands it sends will be
    printed to the screen/logged to the file. Compare the status (first)
    byte in each line with the table above and note which
    button/slider/control sends what message.
  - For example, when you move a slider, you might see`Debug: [...]:
    "MIDI ch 1: opcode: B0, ctrl: 2, val: 3D" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3A" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3D" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3B" 
    Debug: [...]: "MIDI ch 1: opcode: B0, ctrl: 2, val: 3C" 
    `

In this instance, it's sending 0xB0 (which when we look at the [table
above](#midi-messages), we see that it's a Control Change message on
channel 1) We also see that the second byte, 0x02 in this case, is the
control number that was moved, and the third is the value or position of
that control, which you can ignore for the purposes of mapping.

1.  Add the byte values to a `<control>` block in the XML file

<!-- end list -->

  - Just plug the first two bytes into a `<control>` XML block for
    `<status>` and `<midino>` respectively. This is detailed on the
    [MIDI Controller Mapping File
    Format](midi_controller_mapping_file_format#inputs) page.

## Additional MIDI tools

### Linux

Open a console and issue `amidi -l`. This will list the attached MIDI
device(s) like so:

    Dir Device    Name
    IO  hw:1,0,0  SCS.3d MIDI 1

Then, to dump the data, you just issue `amidi -p hw:1,0,0 -d` (Replace
hw:1,0,0 with whatever device ID your controller shows in the list.)
You'll get output like this:

    B0 02 3D
    B0 02 3A
    B0 02 3D
    B0 02 3B
    B0 02 3C

See above for how to interpret this data.

amidi can also be used to send MIDI messages to your controller with the
-S option. Specify each byte as a hexadecimal number and separate the
bytes by spaces. For example:

    amidi -p hw:1,0,0 -S "b0 02 7f"

The program `aseqdump` works similarly, but is a bit more verbose than a
series of hexadecimal numbers:

    $ aseqdump -l
     Port    Client name                      Port name
      0:0    System                           Timer
      0:1    System                           Announce
     14:0    Midi Through                     Midi Through Port-0
     20:0    Tweaker                          Tweaker MIDI 1
     20:1    Tweaker                          Tweaker MIDI 2
    $ aseqdump -p 20:0
    Waiting for data. Press Ctrl+C to end.
    Source  Event                  Ch  Data
     20:0   Note on                 0, note 1, velocity 127
     20:0   Note off                0, note 1
     20:0   Note on                 0, note 2, velocity 127
     20:0   Note off                0, note 2
     20:0   Note on                 0, note 3, velocity 127
     20:0   Note off                0, note 3

### Windows

You can download [tail.exe](http://tailforwin32.sourceforge.net/) to
watch [mixxx.log](troubleshooting#where%20is%20the%20mixxxlog%20file) as
new messages are added or [build Mixxx](Compiling%20on%20Windows) with
`scons msvcdebug=1` and run it with the `--controllerDebug` option. This
will cause it to pop up a console window when you run it and the MIDI
messages received by your controller will be displayed there.

[MIDI OX](http://www.midiox.com/) can intercept MIDI messages from
programs other than Mixxx.

### Mac OS X

Download the free [MIDI Monitor](http://www.snoize.com/MIDIMonitor/)
utility and run it. MIDI Monitor is a utility for Mac OS X which
displays MIDI signals in a variety of formats. It can watch both
incoming and outgoing MIDI streams, and can filter them by message type
and channel.

Download the free
[MIDISimulator](http://www.macupdate.com/app/mac/35645/midisimulator)
utility and run it. MidiSimulator is a tool to test midi devices like
pianos or dj controllers. It allows you to receive and send midi events.
