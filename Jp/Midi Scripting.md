将来的にたくさんのMIDIコントローラーのサポートを受けるため、Mixxxは（v1.7.0から）MIDIスクリプティングを提案しました。これはMIDIコントロールを
[QtScript](http://doc.trolltech.com/4.5/qtscript.html)([Javascript](http://en.wikipedia.org/wiki/JavaScript_syntax)
/
[ECMAScript](http://www.ecma-international.org/publications/standards/Ecma-262.htm)と同じものと考えて良いです）で割当し、Mixxxの機能
ライブラリファイルに備えられた機能に自由に一つ一つMIDIマッピングを有効にするアイデアです。
ユーザー制作機能は色々な機能を実装でき、MIDIイベント情報を一つのコントローラーのボタンに実装すると同時に、
他の [Mixxx
properties(“controls”)](mixxxcontrols)のコントロール値を変更し、Mixxxの挙動を変えることができ（例えば[scratching](midi_scripting#scratching))、
LEDの複雑な表示シーケンス、テキスト表示の信号をコントローラーのディスプレイに送信したり、[4デッキコントローラーを2デッキコントローラーで切り替えたりできます](midi_scripting#turning_a_2_deck_controller_into_a_4_deck_controller)。

もしあなたがMixxxに内蔵されているマッピングをあなた好みのマッピングにしたければ、[Contributing
Mappings](contributing_mappings)ページのコーディングガイドラインをご覧ください。

JavaScriptは複雑な機能をWebページにプログラミングするのに不可欠です。たくさんのチュートリアルがありますが、[W3Schools](http://www.w3schools.com/js/default.asp)はプログラミングを今までしたことがない人を
対象としています。しかし理解するにはHTMLも理解しておかなければなりません。その言語はWebページを書くのに使われています。HTMLはかなりシンプルで簡単に学習でき、基本です。
それと似たXML、その言語はMixxxの[MIDI controller mapping file
format](midi_controller_mapping_file_format)として使われています。
[付加的な例](midi_scripting#additional_examples)の項の下の方は、少々、またはプログラミングに詳しくない人を対象にしています。この例は一般的な使用法で構成とメンテナンスされているMIDIスクリプティングの一番最初の助けです。これが作れると簡単にあなたや他の人のコードをすぐに編集できるようになります。

もしあなたがいくらかのプログラミングの経験があるのなら、あなたは多分JavaScriptの基本はすぐに簡単に学べるでしょう。 Mozilla
Developer
NetworkはJavaScriptプログラミングの有用なリソースがあり、JavaScriptそれ自身がWebを成してると考えてるからです。とはいえ、その考えはプログラマ経験者の人々にはとても浅はかな考えです。

\* [Language basics crash
course](https://developer.mozilla.org/en-US/Learn/Getting_started_with_the_web/JavaScript_basics#Language_basics_crash_course)
\* [JavaScript
Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_Types)
, は更に徹底したチュートリアル \* [JavaScript
Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)

このページの一番下にある[最後の例](midi_scripting#turning_a_2_deck_controller_into_a_4_deck_controller)、JavaScriptの主要な機能をふんだんに使います。これはいくつかMDN
JavaScript Referenceへのリンクのついたコメントを所持しています。
これは経験のあるプログラマなら高速で言語の基本を把握することができるでしょう。

ここにいくつかJavaScriptを深く知るための資料を掲載します:

\* [MDN’s A Re-Introduction To
JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)
\* [Douglas Crockford’s JavaScript
website](http://javascript.crockford.com/) \* [Douglas Crockford on
JavaScript – Act III: Function the
Ultimate](http://yuiblog.com/blog/2010/02/24/video-crockonjs-3/) \*
[Private Members in
JavaScript](http://javascript.crockford.com/private.html) \*
[JavaScript: The Definitive
Guide](http://shop.oreilly.com/product/9780596805531.do)

もしMIDIについて知りたいのであれば[MIDIクラッシュコース](midi_crash_course)を見てください。

**Tip** :
もしすでにMixxxマッピングが各メーカーのコントローラーやあなたのコントローラー向けに作られていたら、例のマッピングを見ていただけると幸いです。
コントローラーは類似したタイプの信号を送ることが好まれます（しかしそれらは多分難しい）。

**Tip** :
あなたのスクリプトをテストしたいときは、Mixxxxを再起動しないでください。いつもあなたがファイルを保存するとき、Mixxxは再読み込みしています。これで開発とテストを高速に切り替えられます。

### JavaScriptマッピングをセットアップ

#### JavaScriptマッピングファイルをXMLマップファイルとリンクさせる

全てのJavaScriptファイルは
[XMLマッピングファイル]([midi_controller_mapping_file_format)と同梱することを望みます。
あなたのOSの[コントローラーマッピングファイルの場所](controller_mapping_file_locations)を確認して、マッピングファイルを配置します。

スクリプトは明示的に読み込みます。デバイスのXMLファイルの \<controller\> タグの直下に以下の句を追記します。:

``` xml
  <scriptfiles>
      <file filename="Manufacturer-model-scripts.js" functionprefix="MyController"/>
  </scriptfiles>
```

‘functionprefix’属性はJavasScriptのオブジェクトを明示し、JavaScriptファイルでは init と
shutdown メソッドがMixxxの起動時と終了時に呼び出されます。 （例によってユーザーはMixxxを起動と終了します）。

''`'' タグはいくつも追加することができますが、functionprefix’属性は一つに統一して指定しなければいけません。
全てが読み込まれるとコントローラーが有効になります。

標準の機能スクリプトファイルは common-controller-script.js
で呼ばれ、常時呼び出され、全てのコントローラーの一般的な機能を呼び出します。[[midi_scripting#available_common_functions|利用できる一般関数]]にこれらの機能の情報が見れます。


=== スクリプトファイルヘッダー ===

スクリプトにあなたのコントローラーのオブジェクトを宣言します。以下のようになります:

<code javascript>
var MyController = {};
</code>

そして、 ''MyController'' はXMLファイルの’functionprefix’に入力した値であれば何でも交換できます。
この新しく宣言したJavaScriptの値を再びコントローラーに送ります。（この例だと、 ''MyController''
を呼びます）そして空のオブジェクトが割り当てられます。

このオブジェクトのプロパティが”init”や”shutdown”を定義し構成した機能を呼び出すでしょう。（JavaScriptではメソッドオブジェクトはプロパティで、この値は関数です）。
これら空っぽですが、文鎮になってるコントローラーに状態やLEDのライティングの制御をするプログラムを書いてやれば、役に立たつことができます。
大体のコントローラーはMIDI信号を送り、それをコントローラーに送り返すこともできます。もしあなたのコントローラーかコレができれば、
Mixxxが起動した際にinit関数で信号を送ってMixxxの状態とコントローラーの状態をマッチングする助けになります。コントローラーの設計がSeratoのためにされていれば、[[serato_sysex|Serato
sysex]]メッセージを送ることができます。

例えば、起動時にコントローラーの40個のLEDを点灯させるためにMIDIノート番号1の40個に値0x7fを送信して点灯し、
更に値0x00を送信するスクリプトはこうなります：

<code javascript>
var MyController = {};

MyController.init = function (id, debugging) {
// turn on all LEDs
for (var i = 1; i <= 40; i++) { // Repeat the following code for the
numbers 1 through 40
// see
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for
midi.sendShortMsg(0x90, i, 0x7f);
}
}

MyController.shutdown = function() {
// turn off all LEDs
for (var i = 1; i <= 40; i++) {
midi.sendShortMsg(0x90, i, 0x00);
}
}
</code>
init関数のIDパラメーターはXMLファイルから来る ''controller id'' 属性です。
それぞれのコントローラーの詳細をプリントすることができます。''debugging''
パラメーターは、 ユーザーが –mididebug パラメーターをコマンドラインで指定すると’true’になります。

**Note** : グローバル変数を使うより、コントローラーオブジェクトのプロパティを定義したほうが（ ''MyController''
サンプルの場合）他のスクリプトをロードした時に 衝突を起こさないでしょう。

=== MIDI信号をJavaScript関数にリンクさせる ===

関数とMIDI信号をリンクさせるには、XMLファイルの<control>要素の<key>タグの中に完全な関数名を入れ、
<options>ブロックの中に<Scritpt-Binding/>と入れます。こんな感じです：

<code xml>
<control> <!-- Pitch slider -->
<group>[Master]</group>
<key>StantonSCS3d.pitchSlider</key>
<status>0xB0</status>
<midino>0x04</midino>
<options>
<Script-Binding/>
</options>
</control>
</code>

<group>の値は困ったことに、スクリプトの関数では使えませんが、静かに確実にXMLパーサーがエラーを必要とします。
これはエクストラパラメーター機能が大体解決します（v1.8から）（これはマルチデッキコントローラーで役に立ちます。
なぜなら、これしか必要としない関数は<group>だけで、かつ適切に反応するからです）
タグやオプションがない場合は、熟考のうえでほかのそれらの上に表示されます。そう、あなたはこれらから解放されます。

デバイスコントロールが制御するときは、名前を付けられたスクリプト関数が呼び出されます。この関数は決心してどのアクションを
取ればいいかMIDI信号を送り、Mixxxのコントロールに変換し、MIDI信号をコントローラーのLEDに送り返すか、と同時にデバックメッセージを出力します。

//2.1の新機能// : <key>要素の値がJavaScriptの断片だった場合、JavaScriptのコードとして評価します。


==== Mixxxマッピングプログラミング with JavaScript ====
=== MIDI入力ハンドリング関数 ===
[[midi_scripting#linking_midi_signals_to_javascript_functions|関数とコントローラのXMLファイルのリンク]]が通ったら、以下が順序付けられます。

- MIDIチャンネル（0x00 = チャンネル 1 〜 0x0F = チャンネル16,）
- コントロール・ノート番号（2バイト）
- コントロールの値（3バイト）
- MIDI状態バイト（Note (0x9#), Control Change (0xB#), Pitch (0xE#）etc.）
- Mixxxコントロールグループ（XMLファイルからの<group>の値）

これに従い、関数は以下のようになります:

<code javascript>
ControllerName.functionName = function (channel, control, value, status,
group) {
// your custom code goes here
}
</code>

**Note** :
これらはJavaScriptで、[[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object|オブジェクト]]です。
このコードは他の言語では定義されていない機能です；このプロパティ定義は
[[midi_scripting#script_file_header|ControllerNameオブジェクト]]の functionName
で、関数をあてがうのに 右に = 記号をつけます。 MyController.functionName
は変更可能で、別の関数をいつでも割り当て直すことができ、MIDI信号を受け取った時でも変更可能です。

パラメーターを切ることも可能で、必要のないパラメーターを除くことが可能ですが、パラメーターの順番は変わりません。 例えば、 ''status''
や ''group'' が要らない場合は、このようにハンドラーを書くことができます。

<code javascript>
ControllerName.functionName = function (channel, control, value) {
// your custom code goes here
}
</code>

==== 値の読み込みとMixxxの設定 ====

スクリプト関数のチェックができたら、Mixxxの操作をする値を読み書きします：

<code javascript>
engine.getParameter(string group, string key);
engine.setParameter(string group, string key, double newValue);
engine.getValue(string group, string key);
engine.setValue(string group, string key, double newValue);
</code>

Mixxxの操作する値を確認するには、 ''engine.getParameter()'' を ''group'' と ''key''
を使ってMixxxの各コントロールを呼び出します。
呼び出せるリストは[[mixxxcontrols|こちら]]にあります。例えば:
<code javascript>
var currentValue = engine.getParameter("[Channel1]", "rate");
</code>
値は簡単に設定でき、 ''engine.setParameter()'' を ''group'' と ''key''
を指定し、新しい値を設定します。こんな感じで:
<code javascript>
engine.setParameter("[Channel1]", "rate", 0.5);
</code>
''engine.getParameter'' と ''engine.setParameter'' は0から1までの値で働きます。古い
''engine.getValue'' と ''engine.setValue'' 関数の値は
[[mixxxcontrols|MixxxControls]] のページに表でまとめられています。 ''パラメーター'' 関数は
エフェクトのパラメーターで絶対に使うべきで、なぜなら、別のエフェクトはそれぞれ別の幅を持っているためです。

**Note** : このスクリプトが動作するのは、計算ができ固定的な値で一つの関数が複数の場合で動く時で、一つのコントローラーが
Mixxxの複数の仮想デッキを扱う時などです（これを実行するときは ''currentDeck'' と ''currentValue''
を定義しましょう）：
<code javascript>
engine.setValue("[Channel"+currentDeck+"]", "rate",
(currentValue+10)/2);
</code>

**Tip** : Mixxxではトグルの状態はバイナリで、 ''script.toggleControll(string group,
string key)'' 関数を使うことで簡略化できます。

==== コントローラーにLEDなどの状態変化信号を送る ====

3バイトの”短い”信号と”長い”任意の長さのシステムエクスクルージブをコントローラーに送ることができ、以下の関数を使います:
<code javascript>
midi.sendShortMsg(status, byte2, byte3);
midi.sendSysexMsg(data, length);
</code>
ついでに、これらは仮想的な全てのMIDI信号を送ることができます。（LEDを点灯させる、ディスプレイを変更する、etc.）

短い信号は、 ''midi.ShortMsg()'' 関数を以下と呼び出します。

* MIDI状態バイト
* 2番目のデータバイト
* 3番目のデータバイト

これらは完全に合わせなければならなく（かつ、あなたのMIDIコントローラーのスペックにも）、
使えるバイトも限定されています。（状態は通常 0x90, 0x80,
か 0xB0)例として：
<code javascript>
midi.sendShortMsg(0x90,0x11,0x01); // This might light an LED
</code>

システムエククルージブ信号は ''midi.sendSysexMsg()'' 関数を以下の様に使います。:

* データバイト配列を常時　0xF0 から初め 0x7F で終わらせます。
* バイト配列は0xF0と0x7Fに内包されます（１番初めからカウントさせるには .length プロパティを使います）。
<code javascript>
var byteArray = [ 0xF0, byte2, byte3, ..., byteN, 0xF7 ];
midi.sendSysexMsg(byteArray,byteArray.length);
</code>

もう一度、これらは完全に合わせなければならなく（かつ、あなたのMIDIコントローラーのスペックにも）、
影響を与えるのに使えるバイトも限定されています。

**Tip** : もし自動的にMixxxの挙動の変更をハンドルしてでMIDI信号をコントローラーに送れば、
あなたのコントローラーのLEDと他のプロパティをMixxxと同期でき、Mixxxをキーボードやマウス、
もしくは他のコントローラーで巧みに操作することができます。

**Tip** :
ひとつの説明すると、あなたのコントローラーがMIDI信号をコンピューターに送信し、コンピューターはMIDI信号にどのように反応するか
は、コントローラーメーカーによるものです。あなたのコントローラーのドキュメントやプロダクトページやメーカーのウェブサイトに
載っていることが好ましいです。もしそれらはドキュメントと離れていたら、マニュアルの最後の方にあるでしょう。

**Tip** :
[[midi_scripting#storing_commonly_used_midi_codes_in_js_objects|よく使うMIDIコードをJavaScriptオブジェクトに備える]]

==== Mixxxの自動応答 ====

この章のポイントは、スクリプトの関数はコントローラーの返答を巧みに扱うことに限定しています。
それらは自動的に返答しMixxxの値を変更し、あなたがSyncボタンをスクリーンでクリックしたら、
コントローラーも同期するようにしたいでしょう。この関数を使うとできます：

* **engine.connectControl**(control group, control name, script function
name) - Mixxxコントロールシグナルとスクリプトの関数を繋げます。trueが返されると、コネクションが成功したことを意味します
* **engine.connectControl**(control group, control namo, script function
name, **true**) - '',true''
をつけると、Mixxxのコントロールシグナルとスクリプトの関数を切断します。trueが返されると、切断が成功したことを意味します。
**Note** : スクリプトの関数名は文字列で引用してください。

* **engine.trigger**(control group, control name) -
簡単にMixxxのシグナルが発火した場合にスクリプトの関数を呼び出し、値を更新します。もし変更できなければ、LEDの状態を強制的に変更します。
できればengine.trigger()はJavaScriptの関数のトリガーに限定し、XMLのリフレッシュ出力には使わないでください。

接続された関数は3つのパラメーターを送ります：新しいMixxxコントロール、グループ、Mixxxコントロール名です。以下はコネクトした関数の例です:
<code javascript>
MyController.syncLED = function (value, group, control) {
midi.sendShortMsg(byte 1, byte 2, value * 127); // see above section for
an explanation of this example line
}
</code>

**Tip** : もし3つのパラメーターを提供したくない場合は、無名関数を使います。
<code javascript>
// Pass one parameter '1000' to my callback
engine.connectControl("[Master]", "volume", function(value) {
MyController.syncLED(1000); });
</code>

=== 例 ===
固定同期状態を仮想デッキからMyController.syncLEDを呼び出したい場合はこうします:
<code javascript>
engine.connectControl("[Channel"+MyController.currentDeck+"]",
"sync_enabled", "MyController.syncLED");
</code>

ボリュームLEDの同期をしたい場合は、engine.trigge()を呼び出します:
<code javascript>
engine.trigger("[Channel"+MyController.currentDeck+"]", "sync_enabled");
</code>

もしLEDの同期を変更したい場合は（例えばスイッチングモード）、Mixxxから”sync_enabled”を切断します。このように:
<code javascript>
engine.connectControl("[Channel"+MyController.currentDeck+"]",
"sync_enabled", "MyController.syncLED",true);
</code>

ハードウェアコントロールからスクリーンのパラメーターを大きく反映する場合は,soft-takeoverを使いましょう。
この機能が有効の間、巧みにthe control on the hardware will
have no effect until the position of the hardware control is close to
that of the software, at which point it will take over and、いつもの制御ができます。
ソフトウェアに影響を与えず、有効・無効はMixxxControlが独立して制御します。
典型的には、あなたのコントローラーのコントロールは物理的な限界の間で動きます（例えば、ノブやスライダー）、soft-takeoverを
スクリプト関数の init() で有効にするとそれらから解放されます。

とてもシンプルに使えます:
<code javascript>
engine.softTakeover(string group, string key, bool enable);
</code>

soft-takeoverをチャンネル1のピッチに有効化します:
<code javascript>
engine.softTakeover("[Channel1]", "rate", true);
</code>

そして、無効化します:
<code javascript>
engine.softTakeover("[Channel1]", "rate", false);
</code>

**Tip** :
これらの機能はスクリプト内にengine.setValue()を巧みに使っている時に動作します。XMLファイル内では動作しません。
**New for 2.0** :
もしMixControlsの絶対的なコントロールの変更（物理的な最大と最小位置）を制御する関数をsoft-takeoverで有効化したいなら、
あなたはsoft-takeoverの状態をあなたのタイミングでリセットしたいでしょう。その際にはこの関数が使えます:
<code javascript>
engine.softTakeoverIgnoreNextValue("[Channel1]", "rate");
</code>

==== スクラッチとジョグホイール ====

典型的に、ジョグホイールはスクラッチができ上面を触れると動作し、サイド面を触れると 一時的にピッチが（スピードアップ/スローダウン
プレイバック）し、ターンテーブルのようになります。
Mixxxでは簡単にスクラッチとジョグホイールの情報を（+1/-1で）送れます。
（他の幅でも動作します）有効化する関数は:
<code javascript>
engine.scratchEnable(int deck, int intervalsPerRev, float rpm, float
alpha, float beta, bool ramp);
engine.scratchTick(int deck, int interval);
engine.scratchDisable(int deck, bool ramp);
bool engine.isScratching(int deck);
</code>

これはどのように使うかというと：

- スクラッチを開始したい時に engine.scratchEnable() を以下の情報と呼びます:
* スクラッチしたい仮想デッキ番号
* 確定したMIDIコントロール（回転インターバル、大抵は128)
* 0%時のピッチスピード（回転インターバル毎分（RPM）は大抵33+1/3だと楽です）
* [[http://en.wikipedia.org/wiki/Alpha_beta_filter|アルファ・ベータフィルタ]]
係数（スリップマット効果のイメージと一緒です）
* アルファ値フィルタ（初めの1/8（0.125）とターンの初め）
* ベータ値フィルタ（初めのアルファ値/32とターンの初め）
* Mixxxに求めるランプデッキスピードダウンか即座に止めるか。（TRUEであればランピング、こちらがデフォルト）
- どこまでMIDIコントロールを動かすか、呼ぶには ''engine.scratchTick()'' を以下の情報と呼びます：
* スクラッチを行う仮想デッキ番号
* 移動量（典型的には1”tick”なら前へ、-1”tick”なら戻ります）
- スクラッチを行った時に（ホイールを離した時が望ましい,） engine.scratchDisable()
を仮想デッキと呼び、スクラッチを終え、Mixxxに求める通常再生へのランプデッキスピードアップか、即座に再生を行います。（通常はスピンバックした勢いからのランプです）

ここに一般的な例を載せます。’scratchnigExample.js’タブをクリックすると、このファイルをあなたのエディタで見ることができます。

<file javascript scratchnigExample.js>
// The button that enables/disables scratching
MyController.wheelTouch = function (channel, control, value, status,
group) {
if ((status & 0xF0) === 0x90) { // If button down
//if (value === 0x7F) { // Some wheels send 0x90 on press and release,
so you need to check the value
var alpha = 1.0/8;
var beta = alpha/32;
engine.scratchEnable(MyController.currentDeck, 128, 33+1/3, alpha,
beta);
} else { // If button up
engine.scratchDisable(MyController.currentDeck);
}
}

// The wheel that actually controls the scratching
MyController.wheelTurn = function (channel, control, value, status,
group) {
// --- Choose only one of the following!

// A: For a control that centers on 0:
var newValue;
if ((value - 64) > 0) {
newValue = value-128;
} else {
newValue = value;
}

// B: For a control that centers on 0x40 (64):
var newValue = value - 64;

// --- End choice

// In either case, register the movement
if (engine.isScratching(MyController.currentDeck)) {
engine.scratchTick(MyController.currentDeck, newValue); // Scratch!
} else {
engine.setValue('[Channel'+MyController.currentDeck+']', 'jog',
newValue); // Pitch bend
}
}
`

そして！　ボタン・タッチセンサーとホイールのスクリプト関数を[ここで書いているよう](midi_scripting#linking_midi_signals_to_javascript_functions)マップに割り当てれば、様々なトラックで行うことができます。

### 時間動作

コントローラーかMixxxを定期的に操作したい時があるでしょう。時間動作 （原文:Timed reactions) は
20マイクロ秒計ってくれます。これがその関数です：

**engine.beginTimer**(millisecondes, “functon”, one-shot) -
タイマーをスタートし、関数を（望まれればパラメーターも）定期的に（もし one-shot
がfalseまたは無ければ）、 もしくは1回だけ（もし one-shot
がtrueであれば）指定したミリ秒（1/1000秒）実行します。これは一つのタイマーのIDを
返し、この値はもしリピーティングタイマーを停止したいときにすぐに停止できます。

**Tip** : この関数は必ずクォート（’）で囲んでください。

**engine.stopTimer**(timer ID) - 指定されたタイマーを停止します。

あなたはタイマーの生成とストップがいくつも作れますが、オペレーションシステムの限界に依存します。
覚えておきましょう。実行したタイマーはすぐに止めましょう。（全てのパフォーマンスやフリーケンシーに影響を与えます）

**けっしてbusy-waitループを使わないでください！　常にタイマーを使いましょう！**
ループは問題ないですが、遅延します。それらはMixxxのシャッターができます）

[script timers](script_timers)のページを見ると、タイマーの他の概要や良い例がわかるでしょう。

### スピンバックとブレイクエフェクト

前進もしくは後退ブレイク効果を有効・無効にするには2つの関数を使って行えます。engine.brake()のすぐ後に
engine.spinback()を呼ぶのが標準的な設定のスピンバックです。

``` javascript
brake(int deck, bool activate, [float factor], [float rate])
spinback(int deck, bool activate, [float factor], [float rate])
```

\* **deck** - 行うデッキ番号です。例: 1 \* **activate** - trueで有効、falseで無効 \*
**factor** （オプション） - どれだけのスピードでデッキを停止させるかです。最初の値は1でそこから値を落としていきます。 \*
**rate** （オプション） - 最初のデッキの再生スピードです。”1”が通常のスピードで、”-10”が10倍速逆再生です。

例：

``` javascript
MyControllerPrefix.brake_button = function(channel, control, value, status, group) {
    var deck = parseInt(group.substring(8,9)); // work out which deck we are using
    var activate = value > 0;

    if (activate) {
        engine.brake(deck, true); // enable brake effect
    } else {
        engine.brake(deck, false); // disable brake effect
    }
}
```

``` javascript
MyControllerPrefix.spinback_button = function(channel, control, value, status, group) {
    var deck = parseInt(group.substring(8,9)); // work out which deck we are using
    engine.brake(deck, value > 0, 1.2, -10); // start at a rate of -10 and decrease at a factor of 1.2
}
```

``` javascript
MyControllerPrefix.spinback_button = function(channel, control, value, status, group) {
    var deck = parseInt(group.substring(8,9)); // work out which deck we are using
    engine.spinback(deck, value > 0, 2.5); // use default starting rate of -10 but decrease speed more quickly
}
```

このエフェクトはXMLにマッピングすることができ、 script.spinback か script.brake と書きます。

``` xml
<control>
    <group>[Channel1]</group>
    <key>script.spinback</key>
    <status>0x90</status>
    <midino>0x04</midino>
    <options>
        <Script-Binding/>
    </options>
</control>
```

### オブジェクトのプロトタイプの増やし方

**String**. prototype.**toInt** - 文字列をアスキーバイト配列に変換します。このように使います。`“Test
string”.toInt()`

## 利用できる一般関数

このリストは alvays-loaded と common-controller-scripts.js ファイルのものです：

\* **nop**() - なにもない（なにも制御していない）空の関数です。エラーの代替として使えます。 \*
**secondstominutes**(seconds) - 大量の秒を MM:SS フォーマットで返す関数です。 \*
**script.toggleControl**(group, [control](mixxxcontrols)) -
バイナリ操作の状態をトグルする関数です。 \*
**script.midiDebug**(channel, control, value, status, group) -
値をプリントする関数です。あなたの関数のどこでも呼びだされ、MIDIの値を関数に取り込みます。あなたのXMLの\<key/\>タグにコレを入れると、動作します。
\* **script.midiPitch**(LSB, MSB, status) -
意図して他のスクリプトから呼び出すと、MIDIピッチコントロールと対応するMixxxのピッチスライダーの値（”rate”コントロール）が返って来ます。
もしこれらの値をコントロールしたい場合は、1行で呼び出すことが可能です。

``` javascript
engine.setValue("[Channel"+deck+"]","rate",script.midiPitch(control, value, status));
```

\* **script.crossfaderCurve**(value, min, max) -
クロスフェーダーのカーブベースの相対的コントロールの値を設定します。（0\~127がデフォルト、minとmaxで最大値と最小値を変更可能）
\* **script.absoluteLin**(value, low, high, min, max) -
相対的なコントロールの値を取得し（0\~127がデフォルト、minとmaxで最大値と最小値を変更可能）、Mixxxコントロール
に合わせたlowのhighの間で線形比例したのデッキボリュームもしくはLFO深度を返します。
返された値はMixxxのコントロールに代入することができます。
\* **script.absoluteLinInverse**(value, low, high, min, max) -
上記とは逆の関数です。MIDIの値をコントローラーに送り返す時に役に立ちます。 \*
**script.absoluteNonLin**(value, low, mid, high, min, max) -
相対的なコントロールから値（0\~127がデフォルト、minとmaxで最大値と最小値を変更可能）を取得し、
非線形でlowとmidとhighを通る相対的な値が返されます。Mixxxコントロールではイコライザー（EQ）やマスターボリュームで使われます。
返された値はMixxxのコントロールに代入することができます。 \*
**script.absoluteNonLinInverse**(value, low, mid, high, min, max) -
上記とは逆の関数です。MIDIの値をコントローラーに送り返す時に役に立ちます。 1.12の新機能 \*
**bpm.tapButton**(deck) -
タップボタンを押した時にいつでも呼び出すことができます。8タップの平均とデッキで設定しているBPMの値から
ピッチレンジを大きく反応させます。（この機能はトラックがBPM値を持っていないと使えません。）もし2回目の動作が行われたら、前の記録は消されます。

# システムエクスクルーシブメッセージ受信時の関数

SysEx信号を受信する関数があります。以下が必要です。：

\- 生データバイトの配列 - 配列の長さ

関数は以下の様に使います。：

``` javascript
ControllerName.inboundSysex = function (data, length) {
    ...
}
```

関数を移譲するときは、XMLマップの\<controls\>部を設定します。：

``` xml
<control>
    <status>0xf0</status>
    <group>[Master]</group>
    <key>ControllerName.inboundSysex</key>
    <options>
        <Script-Binding/>
    </options>
</control>
```

バイトをコントローラーが受信しどのような振る舞いをするかはユーザーマニュアルかメーカーに問い合わせてください。
もしコントローラーが別のSysEx信号を送信してきた場合は、関数を一つ作り、受信し通信する動作をさせましょう。

**Note** :
いくつかのコントローラーはMIDI標準を破った情報を送ります。例えば、最高ビット数を無視した状態バイト（0xF9とか）などです。
Linuxでは最近のバージョンのALSA（2012年12月以降の）はそれらのようなバイトを自動的に標準的な2ニブル分解し、2バイトに送信しています。
例えば 0xF0 0x97 0x30 0xF7 は \*0xF0 0x09 0x07 0x03 0x00
0xF7\*と変換しています。詳しくはALSAのドキュメントをご覧ください。

# 付加的な例

この章ではいくつかの例を上げてあなたの後押しをします。最初はシンプルに、次第に複雑な物になっていきます。

### ボタンを押した時

MIDIボタンは通常押した時は0x7F（127）を送信し、離した時は0x0（0）を送信します。
したがって、JavaScript関数でボタンが押されたら実行されるようにするには、この関数を書き、ボタンが押された時の処理を書き、関数で囲みます。
状態の値を確認する関数を書くとしたらこうです。：

``` javascript
MyController.someButton = function (channel, control, value, status, group) {
    if (value === 127) {
        // do something when this button is pressed
    }
}
```

### 新しいスケールを確立する

リレイティブモード（タッチストリップ）のピッチスライダーの感度を下げたい場合：（XMLの\<group\>は適切に割り当てられています）

``` javascript
MyController.pitchSlider = function (channel, control, value, status, group) {   // Lower the sensitivity of the pitch slider
    var currentValue = engine.getValue(group,"rate");
    engine.setValue(group,"rate",currentValue+(value-64)/128);
}
```

**IMPORTANT NOTE** : 関数の中で変数を宣言するときは必ず”var”を最初に付けましょう。もしこれを忘れると、
変数はグローバルになり、容赦なく他の別の名前の変数やスクリプトファイルの変数にも影響を与えます。

### よく使うMIDIコードをJavaScriptオブジェクトに備える

よく使うコードは[JavaScriptオブジェクト](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)を作っておきましょう。あなたのコードは読みやすくなり編集しやすくなります。JavaScriptオブジェクトは色んな型の変数の固まりです（関数や他のオブジェクトも含みます）。
このケースでは他言語のハッシュテーブルに似ています。例えば、あなたがMIDIノートのボタンとMIDIの値、LEDの色とMIDIの値をまとめておくときはこうでしょう：

``` javascript
MyController.buttons = {
    '[Channel1]': { // an object within another object
        'play': 0x01,
        'cue': 0x02,
        'sync': 0x03
    },
    '[Channel2]': {
        'play': 0x04,
        'cue': 0x05,
        'sync': 0x06
    }
}

MyController.colorCodes = {
    'off': 0x00,
    'red': 0x01,
    'green': 0x02,
    'blue': 0x03
}
```

この状態でLEDの色を緑に変えるコードを書く時に、対応したLEDのMIDIの番号を直接書くより、LEDの階層から緑を選択した方が簡単ですし、
オブジェクトのプロパティを見たい場合も簡単です。このようにすると簡単に書け、簡単に読むことができます。簡単に読めるコードはあなたが
コードを見返して思い出す時の助けになります。他の人がコードを改良するときの助けにもなります。例えば、トラックを再生すると[自動的に反応して変更](midi_scripting#automatic_reactions_to_changes_in_mixxx)する関数はこのように書けます。（play\_indicatorに関しては[Mixxx
Control](mixxxcontrols)で）：

``` javascript
MyController.playButtonLED = function (value, group, control) {
    midi.sendShortMsg(
                      0x90,
                      MyController.buttons[group].play, // an object's properties can be referenced through either SomeObject.property or SomeObject[property]
                                                        // but with the [] brackets, property can be a variable or other code
                      (value === 1) ? MyController.colorCodes.green : MyController.colorCodes.off
                      // The above line is a shortcut that means: "If value is 1, then send MyController.colorCodes.green; otherwise, send MyController.colorCodes.off"
                      // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
                     )
}
```

比べてみましょう:

``` javascript
MyController.playButtonLED = function (value, group, control) {
    if (group === '[Channel1]') {
        if (value === 0x7F) {
            midi.sendShortMsg(0x90, 0x01, 0x02)
        } else {
            midi.sendShortMsg(0x90, 0x01, 0x00)
        }
    } else if (group === '[Channel2]') {
        if (value === 0x7F) {
            midi.sendShortMsg(0x90, 0x04, 0x02)
        } else {
            midi.sendShortMsg(0x90, 0x04, 0x00)
        }
    }
}
```

この2つの例は同じ事を行っていますが、最初の方は直感的で、なぜなら、コードの見通しがよく、簡素に書かれています。
MyController.buttons と MyController.colorCodes
オブジェクトは後のコードと比べると番号を参照するのを助けてくれました。
MIDIコードを別のものに編集したい時も、オブジェクトの1行を変えるだけなので、編集も簡単です。

**Tip** : あなたのコントローラーがどのようなMIDI信号を送っているか確認するには、コントローラーのメーカー次第です。
あなたのコントローラーのドキュメントやプロダクトページやメーカーのWebサイトに載っていることが好ましいです。もしドキュメントに無ければ、
マニュアルの最後の方に書いていることがあります。

### 変更（シフト）ボタンとレイヤーマッピング

多くのコントローラがシフトボタンを一緒に押すと別のMIDI信号を送ります。このケースではJavaScriptは必要なく、XMLで事足ります。
しかし、もしこのケースに該当しない場合、シフトボタンを押した時か同時押しが有効の時、JavaScriptが必要となります。この章は高難易度です。

#### 状態遷移を値で記録する

一つのアプローチとしてはブーリアン（true/false）変数を宣言し、トラックごとボタンの変更を補完する方法です。
XMLファイルでは変化するボタンの関数のトグルし、変数に状態を確認し、代入します。例えば：

``` javascript
MyController.shift = false;

MyController.shiftButton = function (channel, control, value, status, group) {
// Note that there is no 'if (value === 127)' here so this executes both when the shift button is pressed and when it is released.
// Therefore, MyController.shift will only be true while the shift button is held down
MyController.shift = ! MyController.shift; // '!' inverts a boolean (true/false) value
}

MyController.someButton = function (channel, control, value, status, group) {
if (value === 127) { // only do stuff when the button is pressed, not when it is released
    if (MyController.shift) {
        // do something when this button and the shift button are both pressed
    } else {
        // do something else when this button is pressed but the shift button is not pressed
        }
    }
}
```

このアプローチは簡単な例です。もしMycontroller.shiftをチェックする多数の関数を作れば、それはやっかいなもので、
特にもし2つ以上のモードがあるコントロールであれば、トラックを常に管理するのは難しく、常に問題が起きます。

#### MIDIインプットを割り当て直す

別のアプローチとして、別のレイヤーを関数ごとに分ける方法があります。その理由は[MIDI入力ハンドリング関数](midi_scripting#midi_input_handling_functions)
では変数を割り当て直し、
関数をシフトボタンが押された場合の動作を割り当て直すことができるからです。もし複雑な操作をして振る舞いを変更したければ、
それはMIDI入力ハンドリング関数グループで一つのオブジェクトにまとめると良いでしょう。

``` javascript
// A container for the functions of the active layer.
// In the XML file, map the MIDI input handling functions to
// properties of this object, for example, MyController.activeButtons.buttonA
MyController.activeButtons = {};

MyController.unshiftedButtons = {
    buttonA = function (channel, control, value, status, group) {
        //code to be executed when buttonA is pressed without shift
    },
    buttonB = function (channel, control, value, status, group) {
        //code to be executed when buttonB is pressed without shift
    }
};

MyController.shiftedButtons = {
    buttonA = function (channel, control, value, status, group) {
        //code to be executed when buttonA is pressed with shift
    },
    buttonB = function (channel, control, value, status, group) {
        //code to be executed when buttonB is pressed with shift
    }
};

MyController.init = function(id, debugging) {
    MyController.activeButtons = MyController.unshiftedButtons;
}

MyController.shiftButton = function (channel, control, value, status, group) {
    // This function is mapped to the incoming MIDI signals for the shift button in the XML file
    if (value === 127) { // shift button pressed
        engine.connectControl(group, key, true); // disconnect callbacks for unshifted layer
        MyController.activeButtons = MyController.shiftedButtons;
        engine.connectControl(group, key); // connect callbacks for shifted layer
    } else { // shift button released
        engine.connectControl(group, key, true); // disconnect callbacks for shifted layer
        MyController.activeButtons = MyController.unshiftedButtons;
        engine.connectControl(group, key); // connect callbacks for unshifted layer
    }
}
```

#### 4デッキコントローラーを2デッキコントローラーで切り替える

魔法のようなMIDIスクリプティングです。2デッキのコントローラーで4デッキコントローラーのセッティングに対応する例です。
この例は複雑です。もし新しいプログラミングなら、上記の例に挑戦して理解して取り組むことをオススメします。もしこのコードに問題があれば、
[フォーラム](http://mixxx.org/forums/viewforum.php?f=3)で問い合わせてください。
これらはたくさんの問題が凝縮した一つの例です。

全てのMIDIコントロールは何らかの値でデッキを切り替え、XMLマッピングファイルでは、関数はplayButton関数がスクリプトにあるとし、
再生は’group =
Mycontroller.deck\[group\]’とします。XMLファイルの\[Channnel1\]が\<group\>属性に使われていれば、デッキ1と3、
\[Channel2\]の場合はデッキ2と４とします。デッキの切り替え1と3、2と4の切り替えボタンの関数はdeckToggleButton関数とします。

‘deckToggleExample.js’ラベルタブをクリックすると、ファイルをダウンロードし、ファイルをあなたのテキストエディタで開きます。

``` javascript
function MyController() {}
MyController.init = function () {
    // Set up the controller to manipulate decks 1 & 2 when this script is loaded (when Mixxx starts or you save an edited script file)
    // The MyController.initDeck function is defined below.
    MyController.initDeck('[Channel1]')
    MyController.initDeck('[Channel2]')
}
MyController.shutdown = function() {}

MyController.deck = {
    // a hash table (technically an object) to store which deck each side of the controller is manipulating
    // The keys (object properties) on the left represent the <group> elements in the XML mapping file.
    // The values on the right represent which deck that set of mappings in the XML file is currently controlling.
    // These values are toggled between [Channel1]/[Channel3] and [Channel2]/[Channel4] by the deckToggleButton function below.
    // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer
    '[Channel1]': '[Channel1]',
    '[Channel2]': '[Channel2]'
}
MyController.buttons = { // a hash table that stores the MIDI notes that correspond to LED backlit buttons
    '[Channel1]': {
        'deckToggle': 0x01
        // Add any other LEDs for decks 1/3 here
    },
     '[Channel2]': {
        'deckToggle': 0x02
        // Add any other LEDs for decks 2/4 here
    }
}
MyController.buttons['[Channel3]'] = MyController.buttons['[Channel1]'] // Copy [Channel1] to [Channel3]
MyController.buttons['[Channel4]'] = MyController.buttons['[Channel2]'] // Copy [Channel2] to [Channel4]

MyController.channelRegEx = /\[Channel(\d+)\]/ // a regular expression used in the deckToggleButton function below
// This extracts the number from the strings '[Channel1]' ... '[Channel4]' so we can do math with that number
// see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp
MyController.deckToggleButton = function (channel, control, value, status, group) {
    if (value) { // only execute the below code when the button is pressed but not when it is released
        // First, get the number out of the string '[Channel1]' ... '[Channel4]'
        var deckNumber = parseInt( // convert string to an integer number variable
                         MyController.channelRegEx.exec( // execute the regular expression
                             MyController.deck[group] // on this string
                         )[1] // Get the string that matches the part of the regular expression inside the first group of parentheses in the regular expression
                              // which is (\d+)
                              // this matches any number of digits
                      )
        if (deckNumber <= 2) {
            deckNumber += 2 // This is a shortcut for 'deckNumber = decknumber + 2'
        } else {
            deckNumber -= 2 // This is a shortcut for 'deckNumber = decknumber - 2'
        }
        MyController.deck[group] = '[Channel' + deckNumber + ']'
        MyController.initDeck(MyController.deck[group]) // Initialize the new deck. This function is defined below.
    }
}

MyController.initDeck = function (group) { // This function is not mapped to a MIDI signal; it is only called by this script in the init and deckToggleButton functions
// Execute code to set up the controller for manipulating a deck
// Putting this code in a function allows you to call the same code from the script's init function and the deckToggleButton function without having to copy and paste code

// Figure out which deck was being controlled before so automatic reactions to changes in Mixxx (see above) can be disabled for that deck
var disconnectDeck = parseInt(MyController.channelRegEx.exec(group)[1])
if (disconnectDeck <= 2) {
    disconnectDeck += 2
} else {
    disconnectDeck -= 2
}
MyController.connectDeckControls('[Channel'+disconnectDeck+']', true) // disconnect old deck's Mixxx controls from LEDs. This function is defined below.
MyController.connectDeckControls(group) // connect new deck's Mixxx controls to LEDs

// Toggle LED that indicates which deck is being controlled
midi.sendShortMsg(
    0x90,
    MyController.buttons[group]['deckToggle'],
    (disconnectDeck > 2) ? 0x7f : 0x00 // If the condition in parentheses is true, send 0x7f; otherwise, send 0x00
                                       // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
   )
}

MyController.connectDeckControls = function (group, remove) { // This function is not mapped to a MIDI signal; it is only called by this script in the initDeck function below
    // This function either connects or disconnects automatic reactions to changes in Mixxx (see wiki section above), depending on the value of the 'remove' parameter
    // Putting this in its own function allows the same code to be reused for both connecting and disconnecting
    // This is particularly helpful when the list of Mixxx controls connected to LEDs is long

    remove = (typeof remove !== 'undefined') ? remove : false // If the 'remove' parameter is not passed to this function, set remove = false
    var controlsToFunctions = { // This hash table maps Mixxx controls to the script functions (not shown in this example) that control LEDs that react to changes in those controls
        'play': 'MyController.playButtonLED',
        'sync_enabled': 'MyController.syncLED',
        'pfl': 'MyController.headphoneLED'
        // ... and any other functions that react to changes in Mixxx controls for a deck
    }

    for (var control in controlsToFunctions) { // For each property (key: value pair) in controlsToFunctions, control = that property of controlsToFunctions
                                               // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in
        engine.connectControl(group, control, controlsToFunctions[control], remove)
        if (! remove) { // '!' means "not"; it inverts the value of a boolean (true/false)
            engine.trigger(group, control)
        }
    }
}

MyController.playButton = function (channel, control, value, status, group) {
    group = MyController.deck[group] // Change the value of the group variable to the deck we actually want to manipulate based on the state of the deck toggle button
    if (value) {
        // toggle whether the deck is playing
        engine.setValue(group, 'play', ! (engine.getValue(group, 'play')
    }
}
```
