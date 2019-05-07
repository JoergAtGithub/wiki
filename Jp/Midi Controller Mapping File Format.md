# MIDI コントローラ マッピングファイルフォーマット

新しい "MIDIプリセット"ファイルを作成することによって、追加のMIDIデバイスのサポートをMixxxに追加することができます。
このファイルは、Mixxxに、コントローラーからのMIDIメッセージをMixxxが理解できるコマンドに変換またはマッピングする方法を指示します。

**新しいMIDIプリセットを作成する最も簡単な方法は、// Preferences\> Controllers //にある** MIDI
Learning Wizardを使用することです。
これにより、[ユーザーコントローラマッピングフォルダ](コントローラマッピングファイルの場所＃ユーザーコントローラマッピングフォルダ)にXMLファイルが生成されます。
それから、作成したこのXMLファイル（またはMixxxに同梱されているか、[the
forum](http://mixxx.org/forums/viewforum.php?f=7)にあるXMLファイルのいずれか）を情報を使用して変更できます。
このページで
これはほとんどのコントローラーの最も基本的な機能にはうまくいきますが、ほとんどのコントローラーは完全なマッピングのためにJavaScriptで[MIDI
Scripting](MIDI%20Scripting)をある程度使用する必要があります。

MIDIの仕組みに慣れていない場合は、[MIDI Crash Course](MIDI%20Crash%20Course)
を参照してください。.

If you would like your mapping included in Mixxx, see [Contributing
Mappings](Contributing%20Mappings).

## XMLクラッシュコース

Mixxxは、MIDIマッピングを保存するために明確に定義されたXMLフォーマットを使います。
Mixxxマッピングを編集できるように、XMLの基本を学ぶのは簡単です。
Webページを定義するために使用される言語であるHTMLを知っていれば、XMLが非常に似ているのでそれは役に立ちます。

XMLはデータを記述するための言語です。それ自体では何もしませんし、定義済みの用途もありません。他の多くのプログラムには、さまざまな情報を伝えるための独自のXML使用方法があります。たとえば、Traktor
TSIコントローラマッピングファイルはXMLファイルですが、TraktorのマッピングシステムはMixxxのマッピングシステムとはまったく異なるため、TSIファイルはMixxxには意味がありません。

XMLファイルは要素の階層です。要素には山括弧で囲まれた開始タグと終了タグがあります（小なり記号（\<）と大なり記号（\>）としても知られています）。開始タグは、山括弧で囲まれた要素に名前を付けるのと同じくらい簡単です（例：
'' \<group\> ''）。開始タグには、要素に関する詳細を指定する属性を含めることもできます。たとえば、 '' \<controller
name = "Stanton SCS.3d"\> ''では、 '' name ''は '' controller ''要素の属性です。値は
'' Stanton SCS.3d ''です。終了タグには、 '' \<''の後にスラッシュが付きます（例： '' \</group\>
`）。開始タグと終了タグの間に、要素にデータまたは他の要素を含めることができます。空の要素も許可されます。空の要素には、「>」の前にスラッシュを付けます（例：`\<SelectKnob
/\>''）。

## ヘッダー

各XMLマッピングファイルは、メタデータを含むヘッダーで始まります。

``` =
<？xml version = "1.0" encoding = "utf-8"？>
    <MixxxMIDIPreset schemaVersion = "1" mixxxVersion = "1.11.0 +"> <！ - 互換性を高めるためのスキーマのバージョン番号。MIDIフォーマットが変更された場合に備えてください - >
<info>
<name> Mixxx用のMIDIプリセットの例</name>
<author>Tom Care</author>
<description>これはMixxx用のXML MIDIプリセットの例です。プリセットの範囲は、小さな機能の追加から、コントローラの完全なマッピング、複数のコントローラを使用した複雑な個人設定までです。この説明は配布を目的としており、機能の範囲に関するコメントを含めることができます。</description>
                <wiki>このコントローラマッピングを記述したMixxx wikiページへのエンコードされたURL </wiki>
                <forums>このコントローラマッピング用のMixxxディスカッションフォーラムページへのエンコードされたURL </forums>
</info>
<controller id = "controller name"> <！ -  1つのファイルに多数のコントローラがサポートされています。コントローラーは一度だけ現れるべきです - >
```

MixxxMIDIPreset要素のschemaVersion属性とmixxxVersion属性は、Mixxx
MIDIマッピングフォーマットが変更されるため、将来の互換性のために重要です。
\<info\>要素の子要素は、Mixxxコントローラ設定のマッピングに関する情報を表示するために使用されます。 ''＆
''はXMLの予約文字なので、フォーラムスレッドのURLは ''＆ ''ではなく ''＆amp;
''を使用する必要があります。 （プリセットの\<info\>セクションに名前がない場合、Mixxx
1.11以降では拡張子なしのファイル名が使用されます。）

\<controller\>要素のid属性に、コントローラのブランドとモデル（たとえば、 "Stanton SCS.3d"）を書きます。
\<controller\>要素は、以下で説明する\<controls\>要素と\<outputs\>要素のコンテナです。

## Inputs

The \<controls\> element tells Mixxx what to do with signals it receives
from your controller such as knob turns and button presses. Within the
\<control**s**\> element, put as many \<control\> elements as necessary.

``` 
        <controls> <!-- One control group -->
            <control> <!-- Several controls -->
                <group>[Master]</group>
                <key>crossfader</key>
                <status>0xB0</status> <!-- CC on channel 1 -->
                <midino>0x07</midino>
                <options>
                    <!-- all control specific options should go here - sensitivity etc. Specifics to be decided by spec -->
                </options>
            </control>
        </controls>
```

The \<group\> and \<key\> elements define the value in Mixxx that this
MIDI signal controls. The [Mixxx Controls](mixxxcontrols) page lists the
available values for these group and key elements.

The \<status\> and \<midino\> elements define the MIDI signal that Mixxx
will listen for. See the [MIDI Crash Course](MIDI%20Crash%20Course) for
a brief introduction to MIDI signals.

### Pitch controls

Some controllers send messages with a status byte of `0xEn` which, per
the MIDI standard (see the [MIDI Crash Course](MIDI%20Crash%20Course),)
are followed by two value bytes in little-endian format. These are
usually used for pitch sliders or pitch wheels. To map these controls,
do the same as above but omit the `<midino>` element.

### Input options

These are all specified with empty XML elements as children of the
\<options\> element. For example, to use the SelectKnob option, in the
XML, write:

``` 
                <options>
                    <SelectKnob/>
                </options>
```

  - **Normal**: No modifications, MIDI\_NOTE\_OFF or value == 0 is used
    as "released" and all other values as "pressed" 
  - **Script-Binding**: Bind to a MIDI script function given in the
    "key" tag. (See [MIDI Scripting](MIDI%20Scripting) for details.)
  - **SelectKnob**: For relative controls centered on 64 (0x40)
  - **Diff**: Adds the current value of a relative control to the
    previous value
  - **Invert**: Subtracts the value from 127, giving an inverted control
    (-127..0)
  - **Rot64**: For encoders sending 63 (0x3F) or 65 (0x41),
    increment/decrement of 1/16 the value
  - **Rot64inv**: For encoders sending 63 (0x3F) or 65 (0x41),
    increment/decrement of 1/16 the value but with inverted controls
  - **Rot64fast**: For encoders sending 63 (0x3F) or 65 (0x41),
    increment/decrement the value with a multiplier of 1.5
  - Button (deprecated): Ignore opcode, use value \> 0 as "pressed" 
  - **Switch**: Ignore opcode and value, all messages are used as
    "pressed"
  - **Spread64**: Exponential spread either side of 64, aka "relative"
    controller
  - **Soft-takeover**: prevents the physical control from affecting
    Mixxx until it's close to the on-screen control's position.
  - **fourteen-bit-lsb**/**fourteen-bit-msb**: 14-bit (high resolution)
    MIDI least/most significant byte. Some controls, most often pitch
    faders, send two MIDI messages so their values can be combined to
    form 127<sup>2</sup> (16,384) possible values rather than 127 for
    more precise control. *New in 1.12*

## Outputs

The \<outputs\> element defines outputs that use "short" (3-byte) MIDI
messages. Use this to control LEDs and other features of your controller
to make them react to changes in Mixxx. Within the \<output**s**\>
element, put as many \<output\> elements as necessary. Note that this
can only send either of two different values, so it is most useful for
LEDs that can only be switched on and off. For other parts of
controllers that are controlled with more than two values such as
multicolored LEDs or VU meters, you need to use [MIDI
scripting](MIDI%20scripting). Scripting is also necessary for sysex
messages.

``` 
        <outputs>
            <output>
                <group>[Channel1]</group>
                <key>play</key>
                <status>0x7F</status>  <!-- First byte sent to device -->
                <midino>0x08</midino>  <!-- Second byte -->
                <on>0x01</on>  <!-- Third byte. If not specified, 0x7F is used. -->
                <off>0x00</off> <!-- Alternate third byte. 0x00 is the default. If set to 0xFF, nothing is sent.-->
                <maximum>0.99</maximum>  <!-- Optional upper value for the Mixxx control, above which the 'off' value is sent. 1.0 is the default. -->
                <minimum>0.9</minimum>   <!-- Lower value for the Mixxx control, below which the 'off' value is sent -->
            </output>
        </outputs>
```

This allows you to send any three bytes to the MIDI controller in the
order \<status\>, \<midino\>, \<on\>/\<off\>. The \<minimum\> and
\<maximum\> elements define the range of the [Mixxx
Control](mixxxcontrols)'s values within which the \<on\> MIDI value is
sent. Outside this range, the \<off\> MIDI value is sent. If \<off\> is
set to 0xFF, no message will be sent outside the range. (Useful for LED
sequences.)

## Closing

Don't forget to close the elements that were opened at the top of the
file.

``` 
    </controller>
</MixxxMIDIPreset>
```
