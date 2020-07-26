![NI Traktor Kontrol S2 Mk2](https://user-images.githubusercontent.com/9455094/88471094-4ab03900-ceca-11ea-8f86-53205fff7d62.jpg)

The Native Instruments Traktor Kontrol S2 Mk2 is a 2 deck all-in-one controller with an integrated audio interface. It has a pair of balanced 1/4" TRS outputs and a pair of unbalanced RCA outputs which both output the main mix, a 1/4" TRS headphone jack, and a 1/4" TRS microphone input. The microphone input is digitized and available to the computer for recording and broadcasting. The Kontrol S2 Mk2 can run with only USB bus power and an optional power supply can be connected to make the LEDs brighter and the headphone output louder.

The Kontrol S2 Mk2 can be distinguished from the Mk1 by the jog wheels. The top of the jog wheels on the Mk2 are shiny aluminum; the top of the jog wheels on the Mk1 are black. The Kontrol S2 Mk3 does not have effects knobs at the top.

# Compatibility
The Kontrol S2 Mk2 is a USB audio and HID class compliant device. It is fully compatible with Linux, Windows, and macOS. No proprietary driver is required on Linux or macOS. For Windows, download and install the latest driver from [Native Instruments' website](https://www.native-instruments.com/en/support/downloads/drivers-other-files/).

# Audio routing
Configure the Kontrol S2 Mk2's output channels 1-2 for Mixxx's main output and channels 3-4 for Mixxx's headphone output. If you want to record and/or broadcast the microphone, configure input channels 1-2 for the Microphone 1 input in Mixxx.

# Mapping
## Decks

### Jog wheels
Touch the top of the jog wheel and turn it to scratch. Move the jog wheel from the edge without touching the top to nudge the track. Hold shift and spin the jog wheel to seek quickly.

### Loop section
The encoders work differently in Mixxx than in Traktor:
  - **Left encoder**: Turning jumps forward/backwards by the beatjump size. If a loop is enabled, turning moves the loop by the beatjump size. Push and turn to adjust the beatjump size. Turning with shift adjusts the musical key. Pushing with shift resets the key to the track's default.
  - **Right encoder**: Turning halves/doubles the loop size. Turning with shift beatjumps by 1 beat forward/backward, or if a loop is enabled, moves the loop 1 beat forward/backward. Pushing (de)activates a loop. Pushing with shift reactivates a disabled loop, or if a loop is enabled, jumps to the loop in point and stops the deck.
  - **In & Out buttons**: Manually set the loop in and out points. Press and hold while moving the jog wheel to adjust the loop in or out point.

### Top pad row
The top pad row has 3 different modes.
  - **Hotcue mode**: This is the default mode when Mixxx starts. The pads control hotcues 1-4. The color of the hotcues is shown on the pads. Press an unlit button to set a new hotcue. Press a lit pad to seek to the hotcue. Press a lit pad with shift to delete the hotcue.
  - **Intro & Outro cue mode**: This mode is activated by pressing the flux button above the tempo fader. Pads 1 & 2 are used for the intro start & end cues and light up green. Pads 3 & 4 are used for the outro start & end cues and light up red.
  - **Sampler mode**: This mode is activated by the button under the Remix knob in the center of the mixer. Press an unlit pad to load the selected track in the library to the sampler. Loaded and stopped sampler pads are lit white. Press a white pad play a sampler. A playing sampler is lit magenta. Press a lit pad with shift to stop a sampler, or if it is already stopped, unload the sample.

### Transport pad row
The bottom pad row works as labelled on the controller:
  - **Sync**: Press to sync tempo. Press and hold to enable sync lock. Press again to disable sync lock. Press with shift to enable sync lock without needing to hold.
  - **Cue**: Behavior depends on the [cue mode set in the Mixxx preferences](https://mixxx.org/manual/latest/en/chapters/user_interface.html#using-cue-modes). Press with shift to seek the beginning of the track and stop.
  - **Play**: Play or pause the deck. Press with shift to toggle keylock.

### Tempo fader
Adjusts the tempo.

### Flux button
Mixxx [does not yet have a very useful flux/slip mode](https://bugs.launchpad.net/mixxx/+bug/1475303), so instead this button toggles the top pad row to the intro/outro cues. Press the button when it is lit to return the top pad row to hotcue mode.

When slip mode is implemented in Mixxx in the future, this could be changed so shift + flux button activates intro & outro mode for the pads.

## Mixer

### Deck columns
  - **Top encoder**: Controls the QuickEffect superknob for the deck. With shift, controls gain. Press to reset the QuickEffect superknob. Press with shift to reset gain. Press and turn to change the effect chain preset loaded to the QuickEffect chain (new in Mixxx 2.4).
  - **FX routing buttons**: Assign the deck to effects units 1 and 2.
  - **EQ knobs**: Adjust the high, middle, and low frequencies.
  - **Cue button**: Toggle whether the deck is routed to the prefader headphone output. With shift, toggle quantize for the deck.
  - **Fader**: Control the deck volume

### Center column
  - **Main volume knob**: Adjust the volume of the main output. This acts on the controller's audio interface output in hardware, so it is not mapped to the main mix gain knob in Mixxx (otherwise the gain would be applied twice).
  - **Remix knob**: Adjusts the gain of samplers 1-8.
  - **Remix buttons**: Toggles the top pad row of the corresponding deck to control samplers. Press when lit to return the pads to controlling hotcues.
  - **Browse encoder**: Scroll through the music library. Push to maximize the library browser on screen.
  - **Load buttons**: Load the track selected in the library to the corresponding deck. Press with shift to unload a track.
  - **Meters**: The meters show the levels for each deck.
  - **Crossfader**: Crossfade between the decks.

## Effects
The Kontrol S2 Mk2 uses the [standard Mixxx effects mapping](https://github.com/mixxxdj/mixxx/wiki/standard-effects-mapping).

## Front panel
The cue volume knob adjusts the volume of the controller's audio interface in hardware, so it is not mapped to Mixxx (otherwise the gain would be applied twice). The cue mix knob is mapped to Mixxx. The Mic Engage button toggles talkover for Microphone Input 1 in Mixxx.

# Technical details
## HID protocol
```
> usbhid-dump -d17cc:1320 | grep -v : | xxd -r -p | hidrd-convert -o xml

<?xml version="1.0"?>
<descriptor xmlns="http://digimend.sourceforge.net" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://digimend.sourceforge.net hidrd.xsd">
  <usage_page>FF01<!-- FF01h, vendor-defined --></usage_page>
  <usage>0</usage>
  <COLLECTION type="application">
    <usage>01</usage>
    <COLLECTION type="logical">
      <report_id>1</report_id>
      <usage>31</usage>
      <usage>31</usage>
      <logical_minimum>-2147483647</logical_minimum>
      <logical_maximum>2147483646</logical_maximum>
      <report_size>32</report_size>
      <report_count>2</report_count>
      <input>
        <variable/>
      </input>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <usage>02</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>1</logical_maximum>
      <report_size>1</report_size>
      <report_count>56</report_count>
      <input>
        <variable/>
      </input>
      <usage>02</usage>
      <usage>02</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>15</logical_maximum>
      <report_size>4</report_size>
      <report_count>2</report_count>
      <input>
        <variable/>
      </input>
    </COLLECTION>
    <usage>02</usage>
    <COLLECTION type="logical">
      <report_id>2</report_id>
      <usage>03</usage>
      <usage>03</usage>
      <usage>03</usage>
      <usage>03</usage>
      <usage>03</usage>
      <usage>03</usage>
      <usage>03</usage>
      <usage>03</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>15</logical_maximum>
      <report_size>4</report_size>
      <report_count>8</report_count>
      <input>
        <variable/>
      </input>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>4095</logical_maximum>
      <report_size>16</report_size>
      <report_count>23</report_count>
      <input>
        <variable/>
      </input>
    </COLLECTION>
    <usage>80</usage>
    <COLLECTION type="logical">
      <report_id>128</report_id>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>127</logical_maximum>
      <report_count>37</report_count>
      <report_size>8</report_size>
      <output>
        <variable/>
      </output>
    </COLLECTION>
    <usage>81</usage>
    <COLLECTION type="logical">
      <report_id>129</report_id>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <usage>81</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>127</logical_maximum>
      <report_count>32</report_count>
      <report_size>8</report_size>
      <output>
        <variable/>
      </output>
    </COLLECTION>
    <usage>01</usage>
    <COLLECTION type="logical">
      <report_id>240</report_id>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <usage>04</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>23</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>208</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>209</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>210</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>211</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>212</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>213</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>214</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>215</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>216</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>217</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>218</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>219</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>220</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>221</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>222</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
    <usage>D0</usage>
    <COLLECTION type="logical">
      <report_id>223</report_id>
      <usage>D1</usage>
      <logical_minimum>0</logical_minimum>
      <logical_maximum>255</logical_maximum>
      <report_size>8</report_size>
      <report_count>32</report_count>
      <feature>
        <variable/>
      </feature>
    </COLLECTION>
  </COLLECTION>
</descriptor>
```

## USB descriptors
```
> lsusb -vd 17cc:1320

Bus 001 Device 010: ID 17cc:1320 Native Instruments 
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass          239 Miscellaneous Device
  bDeviceSubClass         2 
  bDeviceProtocol         1 Interface Association
  bMaxPacketSize0        64
  idVendor           0x17cc Native Instruments
  idProduct          0x1320 
  bcdDevice            0.46
  iManufacturer          12 Native Instruments
  iProduct                7 Traktor Kontrol S2 MK2
  iSerial                13 737C9B2E
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x0154
    bNumInterfaces          6
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0x80
      (Bus Powered)
    MaxPower              480mA
    Interface Association:
      bLength                 8
      bDescriptorType        11
      bFirstInterface         0
      bInterfaceCount         3
      bFunctionClass          1 Audio
      bFunctionSubClass       0 
      bFunctionProtocol      32 
      iFunction               0 
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           0
      bInterfaceClass         1 Audio
      bInterfaceSubClass      1 Control Device
      bInterfaceProtocol     32 
      iInterface              7 Traktor Kontrol S2 MK2
      AudioControl Interface Descriptor:
        bLength                 9
        bDescriptorType        36
        bDescriptorSubtype      1 (HEADER)
        bcdADC               2.00
        bCategory               8
        wTotalLength       0x0077
        bmControls           0x00
      AudioControl Interface Descriptor:
        bLength                 8
        bDescriptorType        36
        bDescriptorSubtype     10 (CLOCK_SOURCE)
        bClockID               40
        bmAttributes            1 Internal fixed clock 
        bmControls           0x07
          Clock Frequency Control (read/write)
          Clock Validity Control (read-only)
        bAssocTerminal          0
        iClockSource           26 Internal Clock
      AudioControl Interface Descriptor:
        bLength                17
        bDescriptorType        36
        bDescriptorSubtype      2 (INPUT_TERMINAL)
        bTerminalID             2
        wTerminalType      0x0101 USB Streaming
        bAssocTerminal          0
        bCSourceID             40
        bNrChannels             4
        bmChannelConfig    0x00000000
        iChannelNames          16 Main Left
        bmControls         0x0000
        iTerminal               2 Input
      AudioControl Interface Descriptor:
        bLength                26
        bDescriptorType        36
        bDescriptorSubtype      6 (FEATURE_UNIT)
        bUnitID                10
        bSourceID               2
        bmaControls(0)     0x00000000
        bmaControls(1)     0x00000000
        bmaControls(2)     0x00000000
        bmaControls(3)     0x00000000
        bmaControls(4)     0x00000000
        iFeature               15 Output Volume Control
      AudioControl Interface Descriptor:
        bLength                12
        bDescriptorType        36
        bDescriptorSubtype      3 (OUTPUT_TERMINAL)
        bTerminalID            20
        wTerminalType      0x0301 Speaker
        bAssocTerminal          0
        bSourceID              10
        bCSourceID             40
        bmControls         0x0000
        iTerminal               5 Audio Output Terminal
      AudioControl Interface Descriptor:
        bLength                17
        bDescriptorType        36
        bDescriptorSubtype      2 (INPUT_TERMINAL)
        bTerminalID             1
        wTerminalType      0x0201 Microphone
        bAssocTerminal          0
        bCSourceID             40
        bNrChannels             2
        bmChannelConfig    0x00000000
        iChannelNames          28 Mic In (Mono)
        bmControls         0x0000
        iTerminal               3 Audio Input Terminal
      AudioControl Interface Descriptor:
        bLength                18
        bDescriptorType        36
        bDescriptorSubtype      6 (FEATURE_UNIT)
        bUnitID                11
        bSourceID               1
        bmaControls(0)     0x00000000
        bmaControls(1)     0x00000000
        bmaControls(2)     0x00000000
        iFeature               14 Input Volume Control
      AudioControl Interface Descriptor:
        bLength                12
        bDescriptorType        36
        bDescriptorSubtype      3 (OUTPUT_TERMINAL)
        bTerminalID            22
        wTerminalType      0x0101 USB Streaming
        bAssocTerminal          0
        bSourceID              11
        bCSourceID             40
        bmControls         0x0000
        iTerminal               4 Output
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       0
      bNumEndpoints           0
      bInterfaceClass         1 Audio
      bInterfaceSubClass      2 Streaming
      bInterfaceProtocol     32 
      iInterface              8 Audio Out
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       1
      bNumEndpoints           2
      bInterfaceClass         1 Audio
      bInterfaceSubClass      2 Streaming
      bInterfaceProtocol     32 
      iInterface              9 Audio Out Alt
      AudioStreaming Interface Descriptor:
        bLength                16
        bDescriptorType        36
        bDescriptorSubtype      1 (AS_GENERAL)
        bTerminalLink           2
        bmControls           0x00
        bFormatType             1
        bmFormats          0x00000001
          PCM
        bNrChannels             4
        bmChannelConfig    0x00000000
        iChannelNames          16 Main Left
      AudioStreaming Interface Descriptor:
        bLength                 6
        bDescriptorType        36
        bDescriptorSubtype      2 (FORMAT_TYPE)
        bFormatType             1 (FORMAT_TYPE_I)
        bSubslotSize            4
        bBitResolution         24
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x01  EP 1 OUT
        bmAttributes            5
          Transfer Type            Isochronous
          Synch Type               Asynchronous
          Usage Type               Data
        wMaxPacketSize     0x0100  1x 256 bytes
        bInterval               1
        AudioStreaming Endpoint Descriptor:
          bLength                 8
          bDescriptorType        37
          bDescriptorSubtype      1 (EP_GENERAL)
          bmAttributes         0x00
          bmControls           0x00
          bLockDelayUnits         2 Decoded PCM samples
          wLockDelay         0x0008
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes           17
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Feedback
        wMaxPacketSize     0x0004  1x 4 bytes
        bInterval               4
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        2
      bAlternateSetting       0
      bNumEndpoints           0
      bInterfaceClass         1 Audio
      bInterfaceSubClass      2 Streaming
      bInterfaceProtocol     32 
      iInterface             10 Audio In
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        2
      bAlternateSetting       1
      bNumEndpoints           1
      bInterfaceClass         1 Audio
      bInterfaceSubClass      2 Streaming
      bInterfaceProtocol     32 
      iInterface             11 Audio In Alt
      AudioStreaming Interface Descriptor:
        bLength                16
        bDescriptorType        36
        bDescriptorSubtype      1 (AS_GENERAL)
        bTerminalLink          22
        bmControls           0x00
        bFormatType             1
        bmFormats          0x00000001
          PCM
        bNrChannels             2
        bmChannelConfig    0x00000000
        iChannelNames          28 Mic In (Mono)
      AudioStreaming Interface Descriptor:
        bLength                 6
        bDescriptorType        36
        bDescriptorSubtype      2 (FORMAT_TYPE)
        bFormatType             1 (FORMAT_TYPE_I)
        bSubslotSize            4
        bBitResolution         24
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            5
          Transfer Type            Isochronous
          Synch Type               Asynchronous
          Usage Type               Data
        wMaxPacketSize     0x0080  1x 128 bytes
        bInterval               1
        AudioStreaming Endpoint Descriptor:
          bLength                 8
          bDescriptorType        37
          bDescriptorSubtype      1 (EP_GENERAL)
          bmAttributes         0x00
          bmControls           0x00
          bLockDelayUnits         2 Decoded PCM samples
          wLockDelay         0x0008
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        3
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass         3 Human Interface Device
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 
      iInterface              0 
        HID Device Descriptor:
          bLength                 9
          bDescriptorType        33
          bcdHID               1.10
          bCountryCode            0 Not supported
          bNumDescriptors         1
          bDescriptorType        34 Report
          wDescriptorLength     817
         Report Descriptors: 
           ** UNAVAILABLE **
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               1
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x02  EP 2 OUT
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               5
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        4
      bAlternateSetting       0
      bNumEndpoints           0
      bInterfaceClass       254 Application Specific Interface
      bInterfaceSubClass      1 Device Firmware Update
      bInterfaceProtocol      1 
      iInterface              0 
      Device Firmware Upgrade Interface Descriptor:
        bLength                             7
        bDescriptorType                    33
        bmAttributes                        7
          Will Not Detach
          Manifestation Tolerant
          Upload Supported
          Download Supported
        wDetachTimeout                    250 milliseconds
        wTransferSize                      64 bytes
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        5
      bAlternateSetting       0
      bNumEndpoints           3
      bInterfaceClass       255 Vendor Specific Class
      bInterfaceSubClass    240 
      bInterfaceProtocol      0 
      iInterface             40 iAP Interface
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x03  EP 3 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x84  EP 4 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x85  EP 5 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               6
Device Qualifier (for other device speed):
  bLength                10
  bDescriptorType         6
  bcdUSB               2.00
  bDeviceClass          239 Miscellaneous Device
  bDeviceSubClass         2 
  bDeviceProtocol         1 Interface Association
  bMaxPacketSize0        64
  bNumConfigurations      1
can't get debug descriptor: Resource temporarily unavailable
Device Status:     0x0000
  (Bus Powered)
```