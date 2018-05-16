# MIDIクロック送信

Mixxx includes a "MIDI for light" script that can send MIDI clock output
for controlling lights or other MIDI synced hardware or software. The
script requires no intervention as soon as you have configured it
according to your needs. The DJ using Mixxx does not need to be
disturbed during the event.

Mixxx は、"Midi for light"
と呼ばれるスクリプトを内蔵しています。このスクリプトはLEDライトの制御を行うMIDIクロックを送信したり、その他様々のハードウェアとの同期を取るために利用されます。スクリプトは、必要に応じてすぐに介入する必要はありません。
Mixxxを使用しているDJは、イベント中に妨害する必要はありません。

To use it, have the sound card with the MIDI output port plugged in or a
virtual software MIDI output port created before starting Mixxx. Then
select the MIDI output port in Options \> Preferences \> Controllers and
load the "MIDI for light" script like a MIDI controller mapping.

このスクリプトを利用するためには、MIDI出力ポートを予め備えているサウンドカードを用意するか、もしくは、Mixxx起動前に、ソフトウェアで仮想的にMIDI出力ポートを作成してください。Mixxxを起動後に、Options
\> Prefereces \> Controolers の順にメニューをたどり、"MIDI for light"
スクリプトを、コントローラのマッピングと同じようにロードする必要があります。

## The current deck

The current deck is detected automatically. To achieve this, several
mixxx-parameter are used. These are:

  - The "crossfader"
  - All deck "volume control"
  - All deck "play/pause button"

The script must find out what mix method is used by the DJ. Use the
cross fader or the volume control? For this purpose, the cross fader is
observed. Is this more than 3 seconds in the middle position, it is
assumed that it is mixing by using the volume controls. Otherwise (the
cross fader is not in middle position): The DJ uses cross fader for
mixing.  
To prevent a over charging of the light software, high frequency deck
changes are suppressed.  
The best way to understand the automated deck change: Play a little in
mixxx while a simple light sequence, synced by beat, is running.

## Beat

Probably the most common and simplest signal. You just have to know one
thing: When running multiple decks, only to the beat of the current deck
is send.  
Tip: To get a better beat signal customize the options of "Beat
Detection" in the preferences. I use this combination.

[[/media/tutorials/midi_for_light/midi_for_light_preferences_beatdetection.png|]]

## BPM

The BPM (beats per minute) value is transferred every beat. The value
range in midi is 0 to 127. To fit BPM value in this range: 50 will
subtracted from BPM value.Example:

  - BPM = 125, then the send value is 75.
  - For BPM under 50 the send value is 0.
  - For BPM over 177 the send value is 127.

Tip: I use it for automated changing of effekt speeds. Like rotation or
macro speed.

## Deck change

If a deck change occur, a midi event is sent.

Tip: This can used to switch light sequences automatically or randomly.
Or you can put your light in a defined status

## VU (volume) meter

Here you can choose from many different signals. All refer to the master
VU meter. First distinction is mono-, left- and right channel. Next, a
distinction is made between actual and calculated values. You have the
choice.

In practice, the absolute value of VU does not generate large visible
change to the light. For more visible change use calculated values.
Calculated from the last 2 seconds.

Values with the label "meter1" to "meter4" belong together. So you can,
for example, form a real VU meter.

## MTC, midi time code

The script sends MTC based on 25 frames per second. Only full frames be
sent. No short message. By the use of full frames, a speed change
(pitch) is no problem. It is also useful when creating a light show.
Stop, forward, backward and jumps are transmitted correctly.

  - The transmitted time code is determined by the current deck.
  - Time code is transmitted only if the position (time) changes in the
    song.
  - To send time code via midi can be switched off under "personal
    setting" of the script.

## Overview MIDI Notes

| action                   | note               | value                        |
| ------------------------ | ------------------ | ---------------------------- |
| deck change              | C ( 48 / 0x30 )    | 100 / 0x64 (+new decknumber) |
| beat                     | D ( 50 / 0x32 )    | 100 / 0x64                   |
| BPM                      | E ( 52 / 0x34 )    | BPM - 50                     |
| VU mono current          | E ( 64 / 0x40 )    | 0-127 / 0x0-0x7f             |
| VU mono average min      | F ( 65 / 0x41 )    | 0-127 / 0x0-0x7f             |
| VU mono average mid      | F\# ( 66 / 0x42 )  | 0-127 / 0x0-0x7f             |
| VU mono average max      | G ( 67 / 0x43 )    | 0-127 / 0x0-0x7f             |
| VU mono average fit      | G\# ( 68 / 0x44 )  | 0-127 / 0x0-0x7f             |
| VU mono current meter 1  | A ( 69 / 0x45 )    | 0-127 / 0x0-0x7f             |
| VU mono current meter 2  | A\# ( 70 / 0x46 )  | 0-127 / 0x0-0x7f             |
| VU mono current meter 3  | B ( 71 / 0x47 )    | 0-127 / 0x0-0x7f             |
| VU mono current meter 4  | C ( 72 / 0x48 )    | 0-127 / 0x0-0x7f             |
| VU mono average meter 1  | A ( 73 / 0x49 )    | 0-127 / 0x0-0x7f             |
| VU mono average meter 2  | A\# ( 74 / 0x4a )  | 0-127 / 0x0-0x7f             |
| VU mono average meter 3  | B ( 75 / 0x4b )    | 0-127 / 0x0-0x7f             |
| VU mono average meter 4  | C ( 76 / 0x4c )    | 0-127 / 0x0-0x7f             |
| VU left current          | G\# ( 80 / 0x50 )  | 0-127 / 0x0-0x7f             |
| VU left average min      | A ( 81 / 0x51 )    | 0-127 / 0x0-0x7f             |
| VU left average mid      | A\# ( 82 / 0x52 )  | 0-127 / 0x0-0x7f             |
| VU left average max      | B ( 83 / 0x53 )    | 0-127 / 0x0-0x7f             |
| VU left average fit      | C ( 84 / 0x54 )    | 0-127 / 0x0-0x7f             |
| VU left current meter 1  | C\# ( 85 / 0x55 )  | 0-127 / 0x0-0x7f             |
| VU left current meter 2  | D ( 86 / 0x56 )    | 0-127 / 0x0-0x7f             |
| VU left current meter 3  | D\# ( 87 / 0x57 )  | 0-127 / 0x0-0x7f             |
| VU left current meter 4  | E ( 88 / 0x58 )    | 0-127 / 0x0-0x7f             |
| VU left average meter 1  | F ( 89 / 0x59 )    | 0-127 / 0x0-0x7f             |
| VU left average meter 2  | F\# ( 90 / 0x5a )  | 0-127 / 0x0-0x7f             |
| VU left average meter 3  | G ( 91 / 0x5b )    | 0-127 / 0x0-0x7f             |
| VU left average meter 4  | G\# ( 92 / 0x5c )  | 0-127 / 0x0-0x7f             |
| VU right current         | C ( 96 / 0x60 )    | 0-127 / 0x0-0x7f             |
| VU right average min     | C\# ( 97 / 0x61 )  | 0-127 / 0x0-0x7f             |
| VU right average mid     | D ( 98 / 0x62 )    | 0-127 / 0x0-0x7f             |
| VU right average max     | D\# ( 99 / 0x63 )  | 0-127 / 0x0-0x7f             |
| VU right average fit     | E ( 100 / 0x64 )   | 0-127 / 0x0-0x7f             |
| VU right current meter 1 | F ( 101 / 0x65 )   | 0-127 / 0x0-0x7f             |
| VU right current meter 2 | F\# ( 102 / 0x66 ) | 0-127 / 0x0-0x7f             |
| VU right current meter 3 | G ( 103 / 0x67 )   | 0-127 / 0x0-0x7f             |
| VU right current meter 4 | G\# ( 104 / 0x68 ) | 0-127 / 0x0-0x7f             |
| VU right average meter 1 | A ( 105 / 0x69 )   | 0-127 / 0x0-0x7f             |
| VU right average meter 2 | A\# ( 106 / 0x6a ) | 0-127 / 0x0-0x7f             |
| VU right average meter 3 | B ( 107 / 0x6b )   | 0-127 / 0x0-0x7f             |
| VU right average meter 4 | C ( 108 / 0x6c )   | 0-127 / 0x0-0x7f             |

## 極私的な設定

You can define the midi-signals they should be send. In the file
Midi\_for\_light.js is at the top a block with variables for that.
Mostly you define: Send this or not. But one variable is for setup of
the midi channel. Attention. This is global for all events these are
send by note.

あなたは送信すべき midi-signals を設定することが出来ます。Midi\_for\_light.js
のファイル内の先頭のブロックに変数亭があります。あなたが定義すべき内容はほとんど、それらのパラメータを送信するか否か、ということです。然しながら
midi-channel を設定する必要があります。ご注意ください。これは全てのイベントに対するグローバル変数であり、これらは note
を通じて送信されます。

### table personal settings

| variable                          | default value | range of validity |
| --------------------------------- | ------------- | ----------------- |
| midi\_channel                     | 1             | 1-16              |
| enable\_beat                      | true          | true/false        |
| enable\_bpm                       | true          | true/false        |
| enable\_mtc\_timecode             | true          | true/false        |
| enable\_vu\_mono\_current         | false         | true/false        |
| enable\_vu\_mono\_average\_min    | false         | true/false        |
| enable\_vu\_mono\_average\_mid    | false         | true/false        |
| enable\_vu\_mono\_average\_max    | false         | true/false        |
| enable\_vu\_mono\_average\_fit    | true          | true/false        |
| enable\_vu\_mono\_current\_meter  | false         | true/false        |
| enable\_vu\_mono\_average\_meter  | true          | true/false        |
| enable\_vu\_left\_current         | false         | true/false        |
| enable\_vu\_left\_average\_min    | false         | true/false        |
| enable\_vu\_left\_average\_mid    | false         | true/false        |
| enable\_vu\_left\_average\_max    | false         | true/false        |
| enable\_vu\_left\_average\_fit    | true          | true/false        |
| enable\_vu\_left\_current\_meter  | false         | true/false        |
| enable\_vu\_left\_average\_meter  | false         | true/false        |
| enable\_vu\_right\_current        | false         | true/false        |
| enable\_vu\_right\_average\_min   | false         | true/false        |
| enable\_vu\_right\_average\_mid   | false         | true/false        |
| enable\_vu\_right\_average\_max   | false         | true/false        |
| enable\_vu\_right\_average\_fit   | true          | true/false        |
| enable\_vu\_right\_current\_meter | false         | true/false        |
| enable\_vu\_right\_average\_meter | false         | true/false        |
