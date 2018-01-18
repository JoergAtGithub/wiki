# Hercules P32 DJ

![http://www.hercules.com/fichier/h\_photo/1492/photo\_file\_p32dj\_top.png](http://www.hercules.com/fichier/h_photo/1492/photo_file_p32dj_top.png)

  - [Webseite des
    Herstellers](http://www.hercules.com/uk/advanced-controllers/bdd/p/258/hercules-p32-dj/)
  - [Herstellerseite Support und
    Downloads](https://support.hercules.com/en/product/p32dj-en/)
  - Zuordnungsdateien auf GitHub: [Hercules P32
    DJ.midi.xml](https://raw.githubusercontent.com/Be-ing/mixxx/hercules_p32_mapping/res/controllers/Hercules%20P32%20DJ.midi.xml)
    und
    [Hercules-P32-scripts.js](https://raw.githubusercontent.com/Be-ing/mixxx/hercules_p32_mapping/res/controllers/Hercules-P32-scripts.js)
    (beide Dateien im Benutzerordner der Controller speichern
    [controller mapping file locations\#user controller mapping
    folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder))
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=8132)
  - [DJTechTools
    review](http://djtechtools.com/2016/06/22/can-pads-replace-jogs-hercules-p32-dj-controller/)
  - [Digital DJ Tips
    review](http://www.digitaldjtips.com/2016/03/review-video-hercules-p32-dj-grid-pad-controller/)

Der Hercules P32 DJ ist ein kompakter DJ controller mit eingebauter
Soundkarte. Statt Jog-Wheels (Teller), hat er zwei 4 x 4 Tasten-Raster
in den Farben rot/blau/violett), jeweils pro Deck. Die Raster können für
unterschiedliche Funktionen auf vier verschiedene Ebenen geschaltet
werden.

## Kompatibilität

Der Controller ist ein Standard-USB MIDI und Audio Gerät, so dass es
ohne weitere Treiber unter GNU/Linux, Mac OS X, und Windows betrieben
werden kann. Für Windows ist es aber empfehlenswert, den Treiber ASIO
sound API zu installieren.

## Soundkarten Setup

Das Gerät hat eine eingebaute 4-Kanal Soundkarte. Es gibt 2 RCA Ausgänge
(Cinch) für den Masterausgang und einen 6mm TRS
Stereo-Kopfhöreranschluss. Die Lautstärke der Kopfhörer wird über
Knöpfe auf dem Gerät eingestellt (hardwareseitig). Diese Knöpfe
befinden sich in der Mitte des Controllers. Die Lautstärke der Kopfhörer
von Mixxx wird darüber nicht geändert. Es gibt keine Lautstärkeregler
für den Masterausgang, aber die Masterlautstärke kann über das
Betriebssystem und über Mixxx eingestellt werden. Das Gerät hat eine
voreingestelle Lautstärke am Masterausgang von 45%. Um die optimale
Lautstärke am Ausgang zu erreichen, sollte also die Lautstärke im
Betriebssystem entsprechend eingestellt werden.

Samplerrate: Bitte 48kHz einstellen, sonst kommt es zu Fehlermeldungen.

Kanal 1-2 ist der Masterausgang, Kanal 3-4 wird dem Kopfhörer
zugeordnet.

## Beschreibung der Zuordnungen

### Vom Benutzer konfigurierbare Optionen

Es gibt ein paar vom Benutzer konfigurierbare Optionen. Diese lassen
sich durch Änderungen in der Datei Hercules-P32-scripts.js durchführen
(mittels bevorzugtem Texteditor wie z.B.: Notepad, TextEdit, Kate oder
gEdit) Die betreffenden Zeilen in dieser Datei sind:

``` 
 ***loopEnabledDot**: Option, den Punkt in der LED Anzeige der Loop-Größe anzuzeigen. Abgeschaltet wird die Loop-Größe von 2-32 Takten benutzt. Dies ist hilfreich, wenn man kleine Loops (unter 2 Takten) nicht benutzt. Aktiviert werden Loops im Verhältnis 1/n benutzt (.2=halber Takt). 
 ***samplerCrossfaderAssign:** Aktiviert (true): Die Sampler auf dem linken Pad-Raster sind mit der linken Seite des Crossfaders verbunden. Genauso die rechte Seite mit dem rechten Pad-Raster.
```

### Stellregler

Die Stellregler verhalten sich nicht genau so wie auf dem Controller
markiert.

  - **Browse encoder**: durch die Bibliothek blättern. Das Drücken auf
    den Regler vergößert die Ansicht der Bibliothek. Das Drehen zusammen
    mit der Shift-Taste sendet den cue/main Mix an den Kopfhörerausgang.
    Das Drücken zusammen mit der Shift-Taste teilt das Signal an den
    Kopfhörerausgang auf: linker Kopfhörer=Vorhören des Decks, rechter
    Kopfhörerausgang=Masterausgang.

#### Mixxx 2.1

Die Zuordnungen der Stellregler in MIXXX sind nicht identisch mit den
Beschriftungen. Sie sind auf dem Controller symmetrisch, aber
unsymmetrisch zugeordnet:

  - **linker Stellregler**: Drehen halbiert oder verdoppelt die
    Loop-Größe. Zusammen mit der Shift-Taste: Taktsprünge von 1 Takt
    vor oder zurück, oder, wenn ein Loop läuft, verschiebe den Loop 1
    Takt weiter oder zurück. Drücken deaktiviert den Loop. Drücken mit
    der Shift-Taste reaktiviert einen abgeschalteten Loop oder wenn ein
    Loop gesetzt ist, springe an diese Stelle und stoppe das Deck.
  - **Rechter Stellregler am Deck (bezeichnet als Filter)**: Drehen
    stellt die Geschwindigkeit des Tracks ein oder wenn keylock
    aktiviert ist, nur das Tempo. Drücken setzt die Geschwindigkeit/das
    Tempo auf den Standard zurück. Drehen zusammen mit der Shift-Taste
    springt im Track vorwärts/rückwärts entsprechend der Takte. Wenn ein
    Loop aktiviert ist, Drehen zusammen mit der Shift-Taste verschiebt
    den Loop mit der Taktweite. Beim Halten der Shift-Taste und Drücken
    sowie Drehen des Reglers verändert die Taktweite, die in der LED
    Anzeige angezeigt wird. Nach dem Loslassen zeigt die LED Anzeige
    wieder die Loop-Größe.

#### Mixxx 2.0

  - **Loop/Tempo Regler**: Drehen stellt die Geschwindigkeit des Tracks
    ein. Drücken deaktiviert einen Loop. Bei Loops unter 1 Takt oder
    weniger bleibt dieser nur solange aktiv, wie der Regler gedrückt
    wird. Drücken zusammen mit der Shift-Taste setzt den manuellen Loop.
    Der Startpunkt wird beim Drücken gesetzt, der Endpunkt beim
    Loslassen. Drehen während die Shift-Taste gedrückt wird verschiebt
    den Loop. Wenn der Lopp auf einem Takt oder mehr läuft, wird um
    einen Takt verschoben. Ist der Loop kleiner als 1 Takt, wird er um
    diese gesamte Größe verschoben. 
  - **Filter/Move Regler**: Drehen stellt die Geschwindigkeit des Tracks
    ein oder wenn keylock aktiviert ist, nur das Tempo. Drücken stellt
    Geschwindigkeit/Tempo auf den Standard zurück. Drehen zusammen mit
    der Shift-Taste springt im Track vier Takte vorwärts/rückwärts. Beim
    Halten der Shift-Taste und Drücken sowie Drehen des Reglers wird
    selektiert, wie viele Takte gesprungen wird, die in der LED Anzeige
    angezeigt werden. Beim Loslassen des Reglers stellt sich die LED
    Anzeige zurück auf die Loop-Größe.

### Effekte

#### Mixxx 2.1

Siehe [Standard Effects Mapping](Standard%20Effects%20Mapping) zur
Benutzung der Effekte.

Wenn das Raster im SLICER Modus ist, sind die Tasten oben links den
Effekt-Decks 1-4 zugeordnet. Drücken des Kopfhörerknopfes zusammen mit
der Shift-Taste verbindet das Effekt-Deck mit dem Kopfhörerausgang
(nützlich, um vor Aktivierung des Effekts dessen Wirkung vorzuhören).
Der Kopfhörer-Knopf (PFL) muss ebenfalls in dem Deck gedückt werden, um
den Effekt im Kopfhörer zu hören.

#### Mixxx 2.0

Die Effekte werden den Decks 1 (links) und dem Deckk 2 (rechte Seite)
zugeordnet. Drücken von jeweils ON/MACRO aktiviert die Effekte auf den
Decks 1-2(4). Drehen der FX AMOUNT Knöpfe stellt die Effektparameter
ein. Per Standard werden die ersten Parameter der Effekt-Decks
eingestellt. Die anderen Parameter könne mit dem SLICER pad mode (siehe
unten) eingestellt werden. Das Drehen des Dry/Wet Knopfes um den Mix des
Soundeffektes mit dem Quelldeck zu ändern. Die Shift-Tastebenutzen, um
den alle Parameter gleichzeitig zu ändern. Der Slicer-Pad-Modus verfügt
über zusätzliche Steuerelemente für Effekte.

Die obersten drei Reihen steuern jeweils einen einzelnen Effekt in der
Effekteinheit, wodurch Sie Effektketten einrichten können. Diese sind in
der LateNight Oberfläche nicht sichtbar. Der linke Schalter steuert, ob
dieser Effekt aktiviert ist (Die gesamte Effekteinheit muss noch für ein
Deck aktiviert sein, damit sie hörbar ist). Mit der Shift-Taste werden
mit der linken Taste die Parameter des Effekts auf die Standardwerte
zurückgesetzt. Die zwei violetten Tasten in der Mitte scrollen durch
die verfügbaren Effekte. Die Schaltfläche auf der rechten Seite stellt
die Parameter-Regler ein, um die Parameter dieses Effekts zu steuern. In
der unteren Reihe wird die Effekteinheit zwischen Kopfhörer, Master-Mix,
Mikrofon 1 und Aux-Eingang 1 umgeschaltet (von links nach rechts).

### Andere Steuerungen

  - **Record knopf**: Schaltet die Aufnahme ein oder aus.
  - **Slip button**: schaltet den Slip-Modus für alle Decks ein und aus.
    Mit Shift wechseln Sie zwischen den Decks 1 und 3 auf der linken
    Seite und den Decks 2 und 4 auf der rechten Seite.
  - **Pad grid**: Verwenden Sie die Tasten Hotcue / Loop / Slicer /
    Sampler, um verschiedene Modi zu aktivieren
  - **Hotcue mode**: Drücken Sie ein unbeleuchtetes Pad, um einen Hotcue
    zu setzen. Drücken Sie ein rotes Pad, um einen Hotcue zu aktivieren.
    Drücken Sie ein rotes Pad mit Shift, um einen Hotcue zu löschen.
  - **Loop mode**: Steuern Sie manuelle Schleifen und andere
    verschiedene Funktionen. In der obersten Reihe, von links nach
    rechts, legen die Pads den Loop-In-Punkt, den Loop-Out-Punkt und den
    Loop-Loop fest (ohne die Größe zu ändern). Halten Sie die Loop- oder
    Loop-Out-Taste gedrückt, während Sie die Wellenform mit der Maus
    verschieben, um den Loop-In / Out-Punkt einzustellen (neu in Mixxx
    2.1). In der unteren Reihe verringern / erhöhen die beiden violetten
    Tasten vorübergehend die Wiedergabegeschwindigkeit, während sie für
    Beatmatching gedrückt gehalten werden. Die Schaltfläche rechts davon
    verschiebt das Beat-Gitter an die aktuelle Position.
  - **Slicer mode**: siehe oben
  - **Sampler mode**: Drücken Sie ein unbeleuchtetes Pad, um den in der
    Library ausgewählten Track auf diesen Sampler zu laden. Die Pads
    sind blau, wenn der Sampler geladen ist, aber nicht spielt, und rot,
    wenn sie abgespielt werden. Drücken Sie ein blaues Pad, um das
    Sample von seinem Cue-Punkt aus abzuspielen. Drücken Sie ein rotes
    Pad, um zum Cue-Punkt des Samples zu springen. Drücken Sie ein rotes
    Pad mit Shift, um ein spielendes Sample zu stoppen. Drücken Sie ein
    blaues Pad mit der Umschalttaste, um den Sampler zu leeren. Beachten
    Sie, dass Sampler unabhängig von Decks sind; Das linke Raster
    steuert die Sampler 1-16 und die rechten Raster steuert Sampler
    17-32.
  - **Sync**: Kurz drücken, um mit dem anderen Deck zu synchronisieren.
    Halten Sie gedrückt, um die Hauptsynchronisation zu aktivieren.
  - **Shift + sync**: umschalten der Quantisieren-Funktion
  - **Shift + cue**: Springe zum Anfang des Tracks und Stoppe
  - **Shift + play**: rückwärts Spielen (Wiedergabe umkehren) (Mixxx 2.0
    wie shift + cue)
  - **Shift + load**: leeren des Decks (auswerfen)
  - **EQ-Knöpfe, Lautstärke-Regler, crossfader, headphone button, play,
    cue, sync, and load** verhalten sich so, wie gekennzeichnet.
