**Die Benutzeroberfäche von Mixxx ist in englischer Sprache
beschriftet.**  
Dies ist die deutsche Übersetzung für das aktuelle [Mixxx manual
(english)](manual).

# Mixxx 1.7 Handbuch

# Inhaltsverzeichnis

1.  [Beginner\`s Guide](Beginner\`s%20Guide)
2.  [Einleitung](manual_german#introduction)
3.  [Installation](manual_german#installation)
    1.  [Windows](manual_german#windows)
    2.  [Linux](manual_german#linux)
    3.  [OS X](manual_german#os_x)
4.  [Benutzeroberfläche](manual_german#Benutzeroberfläche)
    1.  [Wiedergabesteuerung](manual_german#WiedergabesteuerunG)
    2.  [Temposteuerung](manual_german#Temposteuerung)
    3.  [Kopfhörer und Flanger](manual_german#Kopfhörer%20und%20Flanger)
    4.  [Lautstärke und
        Equalizer](manual_german#Lautstärke%20und%20Equalizer)
    5.  [Wellenform](manual_german#Wellenform)
    6.  [Waveform-Übersicht](manual_german#Waveform-Übersicht)
    7.  [Wiedergabemodus](manual_german#Wiedergabemodus)
    8.  [Master und Crossfader](manual_german#Master%20und%20Crossfader)
    9.  [Bibliothek](manual_german#Bibliothek)
5.  [Konfiguration](manual_german#konfiguration)
    1.  [Master- und
        Kopfhörer-Ausgänge](manual_german#Master-%20und%20Kopfhörer-Ausgänge)
    2.  [Latenzen](manual_german#Latenzen)
    3.  [Sampleraten](manual_german#samplerates)
    4.  [Sound APIs](manual_german#sound_apis)
    5.  [Vinyl Steuerung](manual_german#Vinyl%20Steuerungl)
6.  [DJing mit Mixxx](manual_german#djing_mit_mixxx)
    1.  [Tracks laden](manual_german#Tracks%20laden)
    2.  [Wellenform](manual_german#Wellenform)
    3.  [Beatmatching und
        Mixen](manual_german#Beatmatching%20und%20Mixen)
    4.  [Vorhören](manual_german#Vorhören)
7.  [Keyboard und
    Controller](manual_german#Keyboard%20und%20Controller).
    1.  [Keyboard Shortcuts](manual_german#Keyboard%20Shortcuts).
    2.  [MIDI-Controller](manual_german#MIDI-Controller).
8.  [Mitmachen](manual_german#mitmachen).

# Einleitung

Mixxx ist eine für DJ\`s entwickelte Software die das Mixen von
Audiodateien ermöglicht. Mixxx unterstützt die Wiedergabe von MP3, OGG,
FLAC sowie WAVE Dateien. Mixxx kann mit diversen DJ MIDI-Controllern
sowie Plattenspielern und Timecode Vinyls gesteuert werden.

# Installation

## Windows

Windows Nutzer installieren Mixxx per Doppelklick auf die ausführbahre
Mixxx Installationdatei. Das Setup-Programm führt dann durch den
Installationsvorgang. Mixxx ist lauffähig auf Windows XP und Vista, 32
und 64 bit. (Sollte auch auf Windows 2000 laufen.)

## Linux

Linux Nutzer finden Mixxx in der Paketverwaltung der Distribution Ihrer
Wahl. **Ubuntu** Nutzer können beispielsweise Mixxx über das Menü
*Programme-\>Hinzufügen/Entfernen...* installieren. Ist Mixxx nicht als
Paket für ihre Distribution vorhanden kann es aus den Quelldateien
kompiliert werden. Details zur Kompilierung von Mixxx sind zu finden
unter: [Compiling on Linux](Compiling%20on%20Linux).

## OS X

OS X (Intel) Nutzer installieren Mixxx durch das Mounten des Mixxx
Disk-Images (dmg) per Doppelklick. Dann das Mixxx Bundle per Drag\&Drop
in den Ordner *Programme* ziehen. Mixxx läuft auf Intel Mac unter OS
10.4 und höher.

# Benutzeroberfläche

[[/media/manual/mixxx-overview.png|]]

Die Benutzeroberfläche von Mixxx ist schlicht gestaltet, so das sie beim
live DJing einfach zu bedienen ist. Dieser Abschnitt beschreibt die
wichtigsten Merkmale der Oberfläche.

## Wiedergabesteuerung

|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_playback.png|]] | Diese Steuerelemente ermöglichen es einen Track wiederzugeben, zu pausieren oder die Wiedergabe anderweitig zu beeinflussen. Der "REV" Button lässt den Track während der Wiedergabe rückwärts laufen. Ist die Wiedergabe gestoppt und wird der "CUE" Button gedrückt, so wird ein Cuepunkt an der aktuellen Wiedergabeposition gesetzt. Er wird als (weisse) Linie auf der Wellenform dargestellt. Wird der "CUE" Button gedrückt wenn die Wiedergabe läuft, so springt der Track zum Cuepunkt und stoppt. Wird der "CUE" Button dann gedrückt gehalten, startet die Wiedergabe vorläufig, der Track springt erst zurück zum Cuepunkt und stoppt wenn der Button wieder losgelassen wird. Dieser Cue-Modus ist als "CDJ" bekannt, er kann in den Einstellungen unter *Interface-\>Default cue behaviour* geändert werden. |

## Temposteuerung

<table>
<tbody>
<tr class="odd">
<td><img src="/manual/uioverview/ui_tempo.png" /></td>
<td>Diese Steuerelemente ermöglichen es die Wiedergabe eine Tracks zu verlangsamen oder zu beschleunigen. Es wird oft für das <a href="manual_german#Beatmatching und Mixen">Beatmatching</a> beim Mixen von Tracks benutzt. Der "RATE" Regler verändert das Tempo eines Tracks wenn er bewegt wird. Der "PERM" Buttom ermöglicht eine Feineinstellung der Änderungen , der "TEMP" Button bewirkt eine vorrübergehende Änderung de Tempos solange er gedrückt ist.<br />
Mit welchen Werten die "PERM" und "TEMP" Buttons jeweils das Tempo eines Tracks beeinflussen, kann in den Einstellungen unter <em>Options-&gt;Preferences-&gt;Interface</em> festgelegt werden. Basiered auf den berechneten BPM versucht der "SYNC" Button automatisch das Tempo des Tracks in einem Kanal mit das Tempo des Tracks in dem anderen Kanal zu syncronisieren.</td>
</tr>
</tbody>
</table>

## Kopfhörer und Flanger

|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_headphone.png|]] | Ist der "HEADPHONE" Button aktiviert, sendet er das Audiosignal des jeweiligen Kanals an das Ausgabegerät, welches in den Einstellungen unter *Sound Hardware-Headphones* gewählt wurde. Dieses Feature wird meistens beim [Vorhören](manual_german#Vorhören) und [Beatmatching](manual_german#Beatmatching%20und%20Mixen) genutzt. Der "FLANGER" Button aktiviert den intergrierten Flanger Effekt auf dem gewählten Kanal. Ein Flanger erzeugt einen "Pseudo-Stereo" Effekt und kann dem Mix zusätzliche Tiefe geben wenn er diskret eingesetzt wird. |

## Lautstärke und Equalizer

|                                      |                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_voleq.png|]] | Der "VOL" Regler kontrolliert die Lautstärke des jeweiligen Kanals. Der "GAIN" Regler bringt extra Verstärkung um z.B. bei leisen Tracks die Lautstärke an die des Tracks auf dem anderen Kanal anzupassen. Die "HIGH", "MID" und "LOW" Regler funktionieren als Equalizer für den entsprechenden Kanal. Sie reduzieren oder erhöhen die hohen, mittleren und tiefen Frequenzen entsprechend. |

## Wellenform

|                                         |                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_waveform.png|]] | Die Wellenform Anzeige zeigt die Wellenformen der geladenen Tracks nahe ihrer aktuellen Wiedergabeposition. Bei Tracks mit gewisser Dynamik sind die einzelnen Beats zu erkennen. Wird ein Cuepunkt gesetzt, wird er als (weisse) Linie auf der Wellenform dargestellt. Durch Klicken und Ziehen auf der Wellenform kann der Track durchsucht werden. |

## Wellenform-Übersicht

|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_woverview.png|]] | Die Wellenform-Übersicht liefert wesentliche Informationen über den geladenen Track des jeweiligen Kanals. Von Rechts nach Links sind das: Tempo des Tracks in BPM, aktuelle Wiedergabeposition und die Laufzeit des Tracks. Am interessantesten ist aber die Darstellung des Tracks als Wellenform - nützlich um z.B. Pausen zu sehen um nicht beim DJing davon überrascht zu werden. Außerdem kann man durch einen Klick in die Wellenform innerhalb des Tracks an einen beliebige Position springen. |

## Wiedergabemodus

<table>
<tbody>
<tr class="odd">
<td><img src="/manual/uioverview/ui_endoftrack.png" /></td>
<td>Der Wiedergabemodus ("End of Track" Modus) definiert, wie sich Mixxx` verhält wenn das Ende eines Tracks erreicht wird. Verändert wird der Wiedergabemodus durch Klick auf das Symbol um zwischen den drei verfügbaren Optionen zu wechseln. Jeder Kanal hat seinen eigenen Wiedergabemodus der unabhängig voneinander geändert werden kann.<br />
<strong>Stop</strong> macht nichts weiter sobald der Track beendet ist, möglich wäre einen neuen Track in den Kanal zu laden oder rückwärts durch den aktuellen Track zu scrollen. <strong>Loop</strong> geht zurück zum Anfang des gerade beendeten Tracks und spielt ihn nochmals. <strong>Next</strong> lädt und spielt automatisch den nächsten Track in der Wiedergabeliste/Bibliothek.</td>
</tr>
</tbody>
</table>

## Master und Crossfader

<table>
<tbody>
<tr class="odd">
<td><img src="/manual/uioverview/ui_master.png" /></td>
<td>Mit dem "Crossfader" (Bildmitte) kann flüssig zwischen den beiden Kanälen hin- und her geblendet werden, ausserdem definiert er was aus dem Master-Ausgang zu hören ist. Wird der Crossfader ganz nach links geschoben ist nur Kanal 1 zu hören, ist er ganz nach rechts geschoben so ist nur Kanal 2 zu hören. Jede Position dazwischen ergibt ein Mix aus den beiden Kanälen.(Hinweis: Die tatsächliche Lautstärke der einzelnen Kanäle bei Bewegen des Crossfaders wird über die "Crossfader Curve" eingestellt. Diese findet man in den Einstellungen unter <em>Crossfader</em>.<br />
Der "VOLUME" und "BALANCE" Regler kontrollieren die Laufstärke und Stereo-Balance des Master-Ausgangs. Der "PRE/MAIN" Regler kontrollirt was im Kopfhörer-Ausgang zu hören ist. Dieser Regler funktioniert wie der Crossfader, nur wird hier zwischen Master und Cue (Vorhören) hin- und her geblendet. Ist "PRE/MAIN" ganz nach links gedreht kann nur das Cue-Signal gehört werden, nützlich um z.B. Tracks vorzuhören. Der "HEADVOL" Regler kontrolliert die Lautstärke des Kopfhörer-Signals.<br />
Der "DEPTH","DELAY" und "LFO" Regler kontrollieren den Flanger. Bei diesem Effekt wird das Eingangssignal mit einer verzögerten Kopie gemixt, was zu Interferenzen führt und eine Art Kammfilter-Effekt ergibt. Wird nun das Ausgangssignal des Effekts wieder in in der Eingang geleitet, kann der Effekt verstärkt werde. In Mixxx wird die Intensität des Effekts vom Ausgangssignal zurück in den Eingang geleitet und kann mit dem "DEPTH" Regler angepasst werden.Der "DELAY" Regler gibt die eigentlichen Wert der Verzögerung an. Innerhalb des Effekts wird dieser Wert nochmals durch ein LFO (low frequency oscillator) moduliert, der entsprechend mit dem "LFO" Regler kontrolliert wird.<br />
Wenn sich das Ganze zu technisch anhört, einfach mit den verschiedenen Parametern experimentieren und hören wie es den Sound beeinflusst.</td>
</tr>
</tbody>
</table>

## Bibliothek

<table>
<tbody>
<tr class="odd">
<td><img src="/manual/uioverview/ui_library.png" /></td>
<td>Die Bibliothek verwaltet alle Ihre Musikdateien. Dort befinden sich die Tracks, welche Sie abspielen und in einen der Kanäle laden können. Alternativ können auch Tracks aus einem externen Dateimanager auf die Wellenform Anzeige gezogen werden. Die Bibliothek bietet verschiedene Ansichten, welche über das Auswahlmenü oben links verändert werden können.<br />
Die zweite Ansichtsoption ist "Play Queue" (Warteschlange), der wie eine Wiedergabeliste für die Tracks funktioniert die als nächstes gespielt werden sollen. Der "Browse" Modus arbeitet grundsätzlich wie ein Dateimanager und sollte selbst erklärend sein. Im "Playlists" Modus können selbst erstellte Wiedergabelisten geladen und angezeigt werden. Außerdem gibt es eine Suchfunktion, die aktuelle Ansicht wird in Echtzeit gefiltert. Die Hauptansicht ist die "Library", sie zeigt alle in der Bibliothek vorhandenen Tracks an. Um diese Ansicht nutzen zu können muss erst eine Bibliothek angelegt werden, das wird beim ersten Start von Mixxx erledigt.<br />
Falls Ihre Bibliothek wiederhergestellt werden muss, da bespielsweise Dateien hinzugefügt oder verschoben wurden, kann dass in der Menüleiste unter <em>Library-&gt;Rescan Library</em> gemacht werden.<br />
Um einen Track in einen Player zu laden, ihn einfach auf Wellenform Anzeige ziehen oder das Kontextmenü benutzen (Rechtsklick auf einem Track). Das Kontextmenü ermöglich es Tracks zur Warteschlange ("Play Queue") oder Wiedergabelisten ("Playlist") hinzuzufügen ( die Wiedergabeliste muss vorher angelegt werden). Zu guter Letzt kann über das Kontextmenü auf die Eigenschaften ("Properties") eines Tracks zugegriffen werden um ID3 Tags zu überprüfen oder die BPM manuell zu ermitteln.</td>
</tr>
</tbody>
</table>

# Konfiguration

Beim ersten Start fragt Mixxx nach dem Verzeichnis welches Ihre Audio
Bibliothek enthält. Das Verzeichnis wird gescannt und die dort gefunden
Audiodateien werden in Mixxx\` interner Bibliothek indiziert. Das
Verzeichnis kann jederzeit in den Einstellungen unter *Library and
Playlists* geändert werden.

Mixxx' Einstellungen befinden sich unter *Options-\>Preferences*.

Mixxx versucht beim Start eine geeignete Soundkarte für die Wiedergabe
auzuwählen. Welche Soundkarte ausgewählt wurde, kann in den
Einstellungen unter *Sound Hardware* überprüft werden.

## Master- und Kopfhörer-Ausgänge

Mixxx verfügt über zwei Audio Pfade: den **Master-Ausgang** und den
**Kopfhörer-Ausgang**. Der DJ sollte die Lautsprecher an den
Master-Ausgang angeschlossen haben, während die Kopfhörer an den
Kopfhörer-Ausgang angeschlossen werden. Der Kopfhörer-Anschluss ist
optional, er kann beispielsweise für das
[Vorhören](manual_german#Vorhören) benutzt werden.

Um die Master- und Kopfhörer-Ausgänge zu konfigurieren, öffnen Sie die
Einstellungen unter *Sound Hardware*. Um einen Kopfhörer-Ausgänge
einrichten zu können, ist entweder eine Soundkarte mit mind. 4 Ausgängen
( 2 Stereo Ausgänge , wie bei 5.1 Soundkarten ) *oder* zwei separate
Stereo-Soundkarten erforderlich. Unter "Channel" kann man die Kanäle
wählen, aus denen das Audiosignal ausgegeben wird (und ggf. externe
Lautsprecher angeschlossen werden).

<span class="underline">**Beispiel Konfigurationen**</span>

**Einzelnes Audiogerät (4 Kanal Soundkarte)**

    Master Gerät:     Echo Digital AudioFire4   Channels: 1/2
    Kopfhörer Gerät:  Echo Digital AudioFire4   Channels: 3/4

**Mehrere Audiogeräte (Zwei Stereo Soundkarten)**

    Master Gerät:     Billig USB Audio          Channels: 1/2
    Kopfhörer Gerät:  SoundBlaster Live!        Channels: 1/2

## Externe Mixer benutzen

Momentan hat Mixxx keinen speziellen Modus um das Signal von einem
einzelnen Kanal an einen separaten Ausgang zu schicken (was benötigt
wird wenn externe Mixer benutzt werden). Dafür gibt es aber einen
einfachen Trick. Den Crossfader und auch den "Pre/Main" Regler komplett
nach links bewegen. Jetzt mit dem "HEADPHONES" Button auf Kanal 2 das
Vorhören aktivieren. Auf diese Weise wird Kanal 1 (Channel 1) auf dem
Master-Ausgang und Kanal 2 (Channel 2) auf dem Kopfhörer-Ausgang
ausgegeben. Nun sollten der Master-Ausgang (Kanal 1) und auch der
Kopfhörer-Ausgang ( Kanal 2) der Soundkarte mit Kanal 1 und Kanal 2 des
externen Mixers verbunden werden.

## Latenzen

Die Latenz in Mixxx gibt an, wie lange das Audiosignal benötigt um auf
Änderung zu reagieren. Beispielsweise gibt eine Latenz von 36
Millisekunden (ms) an, das Mixxx 36 ms benötigt um eine laufende
Wiedergabe zu stoppen nachdem der "PLAY/Pause" Button gedrückt wurde.
Generell gilt, je geringer die Latenz, desto schneller reagiert Mixxx.
Latenzen zwischen 36-64 ms sind akzeptabel wenn Mixxx mit Keyboard,Mouse
oder Midi-Controller benutzt wird. Eine Latenz von unter 16 ms ist bei
der Verwendung von Timecode Medien empfohlen, Mixxx reagiert sonst zu
träge.

Um die Latenz optimal einzustellen, verringern Sie in den Einstellungen
unter *Sound Hardware* den "Latency" Regler. Experimentieren Sie ein
wenig mit den Einstellungen, Mixxx sollte **\*ohne Kratzen, Knacken und
Aussetzer im Audiosignal** stabil läuft. Das Ändern der [Sound
API](#sound-apis) zu ASIO unter Windows oder JACK unter Linux kann ,
abhängig von der Hardware Konfiguration , die Latenz reduzieren.

Bedenken Sie das **niedrigere Latenzen bessere Soundkarten und
schnellere CPUs erfordern** und das **Null-Latenz ( 0ms ) ein Mythos
ist** (obwohl Mixxx mit Latenzen \< 10ms arbeiten kann).

### Tips zu Latenzen unter Linux

Latenzen unter Linux sind ein recht komplexes Thema, für detaillierte
Informationen wird empfohlen die [Jack FAQs
(Englisch)](http://jackaudio.org/faq) zu lesen, speziell den Abschnitt
"How should I configure my Linux 2.6 Operating System?". Weitere
nützliche Ressourcen sind der Linux Realtime Guide und [Gentoo's
Dokumentation zu dem
Thema](http://www.gentoo.org/proj/en/desktop/sound/realtime.xml).

Wird ALSA benutzt, sollte als erstes versucht werden in den
Einstellungen den "Master Output" auf "default" zu setzen anstatt eine
bestimmte Hardware. (Auf einem Testsystem mit integrierter
Intel-Soundkarte machte das einen großen Unterschied.) Der Nachteil
dieser Methode ist, dass der Systemsound ( wie eventuell aktivierte KDE
Beeps) mit in Mixxx\` Mastersignal einfließt und auch entsprechend
ausgegeben wird.

Eine zweite Möglichkeit die Latenzen auf dem System zu reduzieren ist
die Benutzung eines Realtime-Kernel. Nutzen Sie bisher einen binären
Kernel, reicht oft bereits die Installation eines Realtime-Kernels über
Ihre Paketverwaltung (sofern diese einen Realtime-Kernel bereitstellt).
Ist dies nicht der Fall, laden Sie die Kernel Quellen und den
entsprechenden Realtime-Patch für Ihre Kernel Version. Der Patch ist
[hier](http://www.kernel.org/pub/linux/kernel/projects/rt/) zu finden.
Den Patch in das Kernel-Verzeichnis entpacken, den Patch ausführen und
dann den Kernel wie gewohnt konfigurieren/installieren.

Grundsätzlich gibt es zwei Möglichkeiten die Realtime Unterstützung zu
aktivieren. Die erste und einfachste Option ist die Nutzung des
Realtime-lsm Moduls. Hierbei muß lediglich das Kernel-Modul mit dem
Paketmanager installiert werden. Danach kann das Modul geladen werden
und bestimmten Nutzern/Gruppen durch entsprechende uid/gid Einstellungen
die Realtime Berechtigungen gewährt werden.(Beispiel: "modprobe realtime
gid=18" gibt auf meinem System der audio Gruppe Realtime
Berechtigungen). Leider ist diese Methode veraltet und funktioniert seit
Linux Kernel Version 2.6.24 nicht länger. In aktuellen Kernels muss
*rlimits* mit PAM benutzt werden um Realtime Priorität zu aktivieren.
(Hinweis: Das ist auch die bevorzugte Methode für ältere 2.6 Kernel
welche u.U. immer noch mit dem Realtime-lsm Moduls funktioniert.) Um die
Methode zu nutzen, einfach /etc/security/limits.conf editieren:

Beispiel: /etc/security/limits.conf

    *               hard    rtprio      0
    *       soft    rtprio          0
    @audio   -  rtprio     99
    @audio   -  memlock    unlimited
    @audio   -  nice      -19

Die mit \* beginnenden Zeilen definieren die Stardard Werte. Das "@" in
@audio zeigt PAM an das audio eine Gruppe ist. Die Berechtigungen können
auch pro Nutzer definiert werden, dann einfach ohne das"@" schreiben.

Es kann auch der neue BFS Scheduler von Con Kolivas benutzt werden.
Dieser Scheduler wurde für CPUs mit einer geringen Anzahl logischer
Kerne (1-16) geschrieben. Dadurch können wesentlich geringere Latenzen
für solche Setups erreicht werden.

Das FAQ für den BFS Scheduler ist zu finden unter:
<http://ck.kolivas.org/patches/bfs/bfs-faq.txt>. Die Launchpad Seite für
ein PPA von Darxus ist zu finden unter:
<https://launchpad.net/~darxus/+archive/bfsbfq>.

## Sampleraten

Die Samplerate (Abtastrate) einer Soundkarte bezeichnet die Häufigkeit,
mit der ein Audiosignal abgetastet wird. Da die meisten Audiodateien mit
einer Samplerate von 44100 Hz codiert sind, bringt das Erhöhen der
Samplerate in Mixxx selten verbesserte Audioqualität. Eine höhere
Samplerate kann in den Einstellungen unter *Sound Hardware* eingestellt
werden. Bedenken Sie das ein Erhöhen der Samplerate die CPU Last und
wahrscheinlich die geringstmöglich erreichbare Latenz erhöht.

## Sound APIs

Mixxx unterstützt diverse Sound APIs unter Windows, OS X und Linux. Eine
Sound API ist a Tool welches Mixxx benutzt um mit Soundkarten zu
interagieren. Einige Soundkarten haben Treiber, die mit bestimmten Sound
APIs geringere Latenzen ermöglichen. Deshalb können verschiedene APIs in
den Einstellungen unter *Sound Hardware* ausgewählt werden.

Unter Windows ist meist **ASIO** die API mit der geringsten Latenz.
Unter OS X ist **CoreAudio** die beste Wahl , unter Linux bieten
**JACK** oder **ALSA** die beste Kompatibilität und Leistung. Linux
Nutzer die JACK nutzen wollen, sollten **sicherstellen das der *jackd*
daemon läuft bevor Mixxx gestartet wird** sonst kann JACK nicht als
Sound API in den Einstellungen ausgewählt werden.

## Vinyl Steuerung

Die Vinyl Steuerung ermöglicht die Wiedergabe von Tracks in Mixxx mit
Hilfe eines echten Platten- oder CD-Spielers. Es hört und fühlt sich an
als ob man seine ganze digitale Musiksammlung auf Vinyl hat. Viele DJs
bevorzugen das typische Gefühl von Vinyl, die Vinyl Steurung ermöglicht
es gleichzeitig von den Vorzügen digitalen Audios zu profitieren.

Die Vinyl Steuerung kann in den Einstellungen unter *Vinyl Control*
konfiguriert werden.

Weitere Informationen über die Vinyl Steuerung in Mixxx und unterstützte
Hardware befindet sich auf der [Vinyl control wiki page](vinyl_control).

[[/media/manual/preferences/vinylcontrol.png|]]

### Auswahl Eingabegerät

Mixxx kann mit max. 2 Decks und Timecode Vinyls oder Timecode CDs
gesteuert werden. Wählen Sie in den "Deck 1" und "Deck 2" Auswahlmenüs
die Soundkarte(n), an welche die Decks angeschlossen sind. Im "Channel
selection" Auswahlmenü wählen Sie die Kanäle entsprechend so wie die
Decks an die Soundkarte(n) angeschlossen sind.

Mixxx unterstützt die Vinyl Steuerung durch eine Soundkarte mit mind. 4
Eingängen (2 Stereo Eingänge) *oder* durch zwei separate Soundkarten mit
je 2 Eingängen (1 Stereo Eingang). erforderlich. Für die Vinyl Steuerung
müssen Stereo Line-In Stecker benutzt werden, Mono- oder
Mikrofon-Stecker funktionieren nicht.

### Vorverstärker

Viele Plattenspieler liefern nur ein unverstärktes Phono-Signal welches
zu einem Line-Signal verstärkt werden muss. Normalerweise erledigt ein
Mixer diese Verstärkung, wenn Sie aber das unverstärkte Phono-Signal
direkt aus dem Plattenspieler in die Soundkarte schicken kann Mixxx die
Verstärkung übernehmen. Mit dem "Turntable Input Preamp" Regler kann die
Vorverstärkung des Phono-Signals eingestellt werden.

### Timecode Konfiguration

Verschiedene Timecode Medien können benutzt werden um Mixxx zu steuern.
Wählen Sie im "Vinyl Type" Menü aus welche Art von Timecode-Vinyl oder
Timecode-CD Sie benutzen wollen.

Mit der "Lead-in Time" Einstellung kann ein Bereich am Beginn der Vinyls
eingestellt werden, in welchem der Timecode ignoriert wird. Das ist
nützlich wenn der Timecode sehr nah an der Kante beginnt, was das
Back-Cueing am Anfang eines Tracks manchmal schwierig macht und die
Nadel des Plattenspielers herunterrutschen läßt. Wird eine "Lead-in
Time" von 20 Sekunden oder mehr eingestellt hat man also mehr Platz auf
dem Vinyl zum Cueing. Es ist auch hilfreich wenn das Vinyl am Beginn
abgenutzt ist und nicht mehr zuverlässig funktioniert - einfach die
"Lead-in Time" bis zu einem Bereich erhöhen der intakt ist. Die "Lead-in
Time" kann so schrittweise erhöht werden und die Vinyls bleiben länger
benutzbar.

### Timecode Modus

Mixxx unterstützt drei Arten von Steuerung auf *allen* unterstützten
Timecode-Medien. Der "Absolute" Modus sendet Tempo und Position des
Timecodes an Mixxx und ermöglicht so das Suchen innerhalb eines Track
(needle dropping) mit dem Vinyl oder der CD. Der "Relative" Modus
berechnet die aktuelle Postion des Timecodes relativ zum Startpunkt und
beeinflusst nur das Tempo der Wiedergabe in Mixxx. Es ist also nicht
möglich einen Track im "Relative" Modus zu durchsuchen. Der "Scratch"
Modus ist eine erweiterte Version des "Relative" Modus speziell für die
FinalScratch Vinyls. Der "Scratch" Modus verbessert die Performance beim
Scratchen geringfüging, aber nicht für die von Hause aus besseren
Timecode-Medien wie Serato. Die "Needle-skip Prevention" erkennt kleine
Änderungen in der Position der Nadel und ignoriert sie, die
Wiedergabeposition springt dadurch nicht wenn jemand versehentlich an
den Plattenspieler stößt. Das kann im Livebetrieb hilfreich sein,
verringert aber gleichzeitig die Reaktionsgeschwindigkeit beim
Scratchen. Demnach sollte die "Needle-Skip Prevention" beim Scratchen
ausgeschaltet sein.

### Signal Qualität

Eine funktionierende Vinyl Steuerung hängt von einer guten
Signalqualität ab. Viele Faktoren können die Signalqualität
beeinflussen, am wichtigsten ist aber dass die korrekte Lautstärke des
Timecode Signal. Is es zu laut oder zu leise wird die Vinyl Steuerung
nicht zuverlässig funktionieren. Es kommt zum Verlust von
Positionsdaten, dadurch verhält sich z.B. der "Absolute" Modus wie der
"Relative" Modus. Weitere Informationen zur Verbesserung der
Signalqualität und zur Behebung von Fehlern befinden sich auf der [vinyl
control wiki page](vinyl_control).

Mixxx stellt die Qualität des Timecode Signals in Echtzeit als ein Paar
von Diagrammen dar. Die zwei Diagramme entsprechen den Eingabegeräten
"Deck 1" und "Deck 2". Der linke Balken in einem Diagramm zeigt den
Gesamtstatus des *Timecodesignals* an. Ein grüner Balken mit der
Aufschrift "OK\!" bedeutet das alles gut funktioniert. Die anderen
beiden Balken in dem Diagramm stellen das unbearbeitete Stereosignal
dar, welches von den Plattenspielern/CD-Playern kommt. Ein gutes Signal
wird als ein Paar von schwankenden grünen Balken angezeigt, der eine
geht hoch während der anderer runtergeht (out-of-phase). Rote Balken
zeigen eine zu hohe oder zu niedrige Signalstärke an, die Einstellung
"Turntable Input Preamp" kann die Signalstärke anheben.

# DJing mit Mixxx

Mixxx sollte für erfahrene DJs und auch Einsteiger einfach zu bedienen
sein. Die Benutzeroberfäche orientiert sich an Hardware DJ-Mixern,
beinhaltet aber auch weitere Elemente um die Praxistauglichkeit zu
erhöhen (z.B. die paralle Darstellung der Wellenformen).

## Tracks laden

Tracks können auf verschiedene Weise einen der beiden Player geladen
werden:

  - Per Rechtsklick in der Bibliothek (im "Library" Modus): Ein
    Rechts-Klick auf einen Track in der Bibliothek gibt einem u.a. die
    Möglichkeit diesen per "Load in Player 1" oder "Load in Player 2"
    in den jeweiligen Player zu laden.
  - Per Drag-and-Drop aus der Bibliothek (im "Library" Modus): Wird ein
    Track per Drag-and-Drop aus der Bibliothek auf eine Wellenform
    Anzeige gezogen, wird er in dem jeweiligen Player geladens.
  - Per Drag-and-Drop aus einem externen Dateimanager: Wird ein Track
    per Drag-and-Drop aus einem externen Dateimanager heraus auf eine
    Wellenform Anzeige gezogen, wird er in dem jeweiligen Player
    geladens. Das funktioniert auch mit anderen Anwendungen unter
    manchen Betriebssystemen. Zum Beispiel kannn unter OSX ein Track auf
    diese Weise aus iTunes heraus in Mixxx geladen werden.

## Wellenform

Es gibt zwei grosse **Wellenform Anzeigen** in Mixxx, welche die
Wellenform der Tracks zeigen die gerade gespielt werden. Hilfreich um
Details in Tracks , wie Steigerungen oder Pausen, im Voraus zu erkennen.
Die Anzeigen sind parallel zueinander angeordnet um das Beatmatching zu
erleichtern, so kann mann auch durch das Anordnen der in beiden
Wellenformen sichtbaren Beats die Tracks syncron laufen lassen. Durch
Klicken und Ziehen auf eine Wellenform kann ein Track in beide
Richtungen durchsucht werden. Die Anzeige der Wellenform wird dabei in
Echtzeit aktualisiert. Es git zwei kleinere Elemente mit der
**Wellenform-Übersicht** . Diese zeigen die Hüllkurve des gesamten
Tracks und sind nützlich für den DJ um z.B. Pausen auf einen Blick zu
erkennen. Vinyl DJs wird das bekannt vorkommen, denn auch auf Vinyl
können stille Abschnitte entsprechend erkannt werden. Eine nützliche
Sache beim Mixen on-the-fly.

## Beatmatching und Mixen

Als **Beatmatching** bezeichnet man das taktgenaue Synchronisieren des
Tempos zweier Tracks.

In Mixxx kann das **Tempo** von zwei Tracks angepasst werden indem der
jeweiligen "RATE" Regler bewegt wird. Die **Phase** der Beats kann durch
Klicken und Ziehen auf die jeweilige Wellenform verändert werden, das
Tempo wird so vorubergehend bei einem Track vermindert bis die Beats
passen.// Die "TEMP" Buttons ermöglichen auch eine vorübergehende
Änderung des Tempos (Nudging). Sie können benutzt werden um die Beats
vorwärts oder rückwärts zu "schieben" um sie zu syncronisieren.

Zwei Tracks sind "beatmatched", sobald das Tempo und die Beats der
beiden yncronisiert sind sie. Ein "perfektes" Beatmatching is nahezu
unmöglich - es werden immer kleinste Tempounterschiede sein.// Ein DJ
der fit ist hält seine Ohren offen und hört ob die Beats auseinander
driften. In dem Fall hat man diesen typischen "Double Bass Kick" Sound
und lasche Kicks, da diese driften auseinander driften. Wenn dass
passiert können die Beats mit ein paar Klicks auf den entsprechenden
"TEMP" Button wieder syncronisiert werden. Und jetzt fange an und mache
TIESTO neidisch\!

## Vorhören

Beim Vorhören (Headphone Cueing) hört der DJ den nächsten Track in
seinem Kopfhörer ab bevor er live gespielt wird. Mixxx ermöglicht dem DJ
das Audiosignal von beiden Kanälen vorzuhören indem der jeweilige
"HEADPHONE" Button aktiviert wird. Durch das Vorhören kann der DJ die
Geschwindigkeit des nächsten Tracks an den aktuellen Track anpassen
bevor er sie mit Hilfe des Crossfaders mixt.

## Einen Mix aufnehmen

Mixxx's Master Signal kann folgendermaßen in Echtzeit als Audiodatei
(unkomprimierte lineare PCM WAV (RIFF)) aufgenommen werden :

1.  In der Menüleiste , "Options" klicken
2.  "Record Mix" klicken
3.  Speicherort und Dateiname angeben, dann "OK" klicken
4.  Mixxx beginnt erst dann mit der Aufnahme wenn 2 Sekunden Sound zu
    hören sind. Um auch die ersten 2 Sekunden aufzunehmen - einfach die
    "PLAY" Taste , dann sofort "CUE" oder "PAUSE" drücken, 2 Sekunden
    warten und mit dem Mixen beginnen. Eine eventuelle Pause am Anfang
    der Aufnahme kann nachträglich mit einem Audio Editor wie
    [Audacity](http://audacity.sourceforge.net/) entfernt werden.

# Keyboard und Controller

## Keyboard Shortcuts

[[/media/mixxx.gif|]]

Durch Shortcuts können Sie Mixxx mit der Tastatur steuern. Die Shortcuts
sind in einer Textdatei gespeichert die Sie frei verändern können.

Linux: /usr/share/mixxx/keyboard/Standard.kbd.cfg

MacOS X: \<Mixxx Bundle\>/keyboard/Standard.kbd.cfg

Windows: \<Mixxx Verzeichnis\\keyboard\\Standard.kbd.cfg

## MIDI-Controller

MIDI-Controller sind externe Hardware-Geräte die verwendet werden um
Audio-Anwendungen wie Mixxx zu steuert. Viele DJs bevorzugen das
"Hands-on"-Gefühl eines MIDI-Controller bei der Verwendung mit Mixxx,
weil es sich ähnlich anfühlt wie ein echtes Mischpult und
Plattenspieler.

Folgende MIDI Geräte werden unterstützt (Stand Mixxx 1.7.0):

  - Hercules DJ Console MK2
  - Hercules DJ Console MP3
  - Hercules DJ Console RMX
  - Hercules DJ Control Steel 
  - Hercules DJ Console Mac Edition
  - Stanton SCS.3d 
  - Stanton SCS.1m
  - Mixman DM2 
  - Tascam US-428
  - M-Audio X-Session Pro
  - M-Audio Xponent
  - Evolution X-Session
  - Ecler NUO4
  - FaderFox DJ2
  - Vestax VCI-100
  - Numark Total Control
  - Behringer BCD3000 (\*bisher ohne Jog-Wheel Unterstützung)
  - Akai MPD24

Vor dem Kauf eines Controllers für die Verwendung mit Mixxx lesen Sie
bitte unsere Wiki Seite zur [Hardware
Kompatibilität](http://www.mixxx.org/wiki/doku.php/hardware_compatibility).
Sie enthält die aktuellste Dokumentation zu den einzelnen von Mixxx
unterstützten Controller und ihrer Beschränkungen. Die Unterstützung für
die Geräte variiert je nach Betriebssystem, also stellen Sie sicher das
die Dokumentation gelesen wurde.

# Mitmachen

Mixxx ist ein Gemeinschafts-Projekt vieler DJs weltweit. Ohne die
Mitwirkung dieser DJs würde Mixxx nicht existieren. Wir suchen ständig
weitere Mitwirkende.

Wenn Sie interessiert sind am Mixxx Projekt mitzumachen, senden Sie eine
Email an unsere [Developer Mailing
Liste](http://www.mixxx.org/support.php) oder schauen Sie in unserem IRC
channel (\#mixxx on Freenode) vorbei.

Wenn Sie Interesse an Programmierung (C++) haben:

  - Werfen Sie einen Blick auf unsere Specs/Projects Seite im Mixxx Wiki
    und schauen ob Ihnen etwas ins Auge fällt. Wenn Sie etwas davon
    programmieren wollen - nur zu\!
  - Wir sind immer bereit als Mentor zur Verfügung zu stehen oder neuen
    Programmierern zu helfen.
  - Werfen Sie einen Blick auf den Bug Tracker vorbei und versuchen
    einen Bug zu fixen\!
  - Senden Sie Patches an Adam, Albert oder mixxx-devel\!

Kein Interesse an Programmierung? Es gibt es trotzdem viele
Möglichkeiten unserem Projekt zu helfen:

  - Testen von Mixxx\` Beta- und Trunk-Versionen um sicherzustellen das
    neue Features und Bugfixes in jedem Fall funktionieren. 
  - Erstellen von Mappings für bisher nicht von Mixxx unterstützten
    MIDI-Controller. Erweiterte Funktionalität erfordert etwas
    Javascript-ähnliche Programmiersprache.
  - Helfen Fragen im Forum zu beantworten.
  - Mixxx promoten - Wenn Sie ein Blog haben, schreiben Sie Artikel über
    Mixxx. Bloggen Sie über neue Releases wenn sie erscheinen. Jede
    Erwähnung im Netz oder in der Zeitung hilft das Projekt größer zu
    machen.
  - Schicke uns ein paar Fotos bei einem Gig mit Mixxx\!
