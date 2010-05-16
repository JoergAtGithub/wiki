**This work in progress is a English-German translation for the current
[Mixxx manual](manual). Missing Translation are maked with
~~striked-trough text~~.**

# Inhaltsverzeichnis

1.  [Beginner's Guide](Beginner's%20Guide)
2.  [Einleitung](manual#introduction)
3.  [Installation](manual#installation)
    1.  [Windows](manual#windows)
    2.  [Linux](manual#linux)
    3.  [OS X](manual#os_x)
4.  [User Interface Overview](manual#user_interface_overview)
    1.  [Playback Controls](manual#playback_controls)
    2.  [Tempo Controls](manual#tempo_controls)
    3.  [Headphone and Flanger](manual#headphone_and_flanger)
    4.  [Lautstärke und Equalizer](manual#volume_and_eq)
    5.  [Wellenform](manual#waveform)
    6.  [Waveform-Übersicht](manual#waveform_overview)
    7.  [End of Track Modus](manual#end_of_track_mode)
    8.  [Master and Crossfader
        Controls](manual#master_and_crossfader_controls)
    9.  [Library](manual#library)
5.  [Konfiguration](manual#configuration)
    1.  [Master and Headphone
        Outputs](manual#master_and_headphone_outputs)
    2.  [Latenzen](manual#latency)
    3.  [Sampleraten](manual#samplerates)
    4.  [Sound APIs](manual#sound_apis)
    5.  [Vinyl Control](manual#vinyl_control)
6.  [DJing with Mixxx](manual#djing_with_mixxx)
    1.  [Loading Tracks](manual#loading_tracks)
    2.  [Waveform Displays](manual#waveform_displays)
    3.  [Beatmatching and Mixing](manual#beatmatching_and_mixing)
    4.  [Headphone Cueing](manual#headphone_cueing)
7.  [Keyboard und Controller](manual#keys_and_hardware_controllers).
    1.  [Keyboard Shortcuts](manual#keyboard_shortcuts).
    2.  [MIDI-Controller](manual#midi_controllers).
8.  [Mitmachen](manual#mitmachen).

# Einleitung

Mixxx ist eine für DJ\`s entwickelte Software die das live Mixen von
Songs ermöglicht. Mixxx unterstützt die Wiedergabe von MP3, OGG, FLAC
sowie WAVE Dateien. Mixxx kann mit diversen DJ MIDI-Controllern sowie
Plattenspielern und Timecode Vinyls gesteuert werden.

# Installation

## Windows

Windows Nutzer installieren Mixxx per Doppelklick auf die ausführbahre
Mixxx Installationdatei. Das Setup-Programm führt dann durch den
Installationsvorgang. Mixxx ist lauffähig auf Windows XP und Vista, 32
und 64 bit. (Sollte auch auf Windows 2000 laufen.)

## Linux

Linux Nutzer finden Mixxx in der Paketverwaltung der Distribution Ihrer
Wahl. **Ubuntu** Nutzer können beispielsweise Mixxx über das
*Programme-\>Hinzufügen/Entfernen...* Menü installieren. Ist Mixxx nicht
als Paket für ihre Distribution vorhanden kann es aus den Quelldateien
kompiliert werden. Details zur Kompilierung von Mixxx sind zu finden
unter: [Compiling on Linux](Compiling%20on%20Linux).

## OS X

OS X (Intel) Nutzer installieren Mixxx durch das Mounten des Mixxx
Disk-Image (dmg) per Doppelklick. Dann das Mixxx Bundle per Drag\&Drop
in den Ordner *Programme* ziehen. Mixxx läuft auf Intel Mac unter OS
10.4 und höher.

# Übersicht Benutzeroberfläche

[[/media/manual/mixxx-overview.png|]]

Die Benutzeroberfläche von Mixxx ist schlicht gestaltet, so das sie beim
live DJing einfach zu bedienen ist. Dieser Abschnitt beschreibt die
wichtigsten Merkmale der Oberfläche.

## Playback Controls

|                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_playback.png|]] | ~~The Steuerelemente für die Wiedergabe ermöglichen playback controls allow you pause, play, and otherwise manipulate the playback of a song. The REV button toggles reverse playback when pressed during regular playback. When playback is stopped, pressing the CUE button places a cue-point at the current position on the waveform. A cue-point is marked by a white vertical line in the waveform view. If the CUE button is pressed during playback, the song will seek to the cue-point and stop. Holding down the CUE button while the song is positioned on the cue-point will result in the song temporarily playing back, and seeking back to the cue-point upon release of the CUE button. This describes the "CDJ Mode" cue behaviour, which is modifiable in the preferences under *Interface-\>Default cue behaviour*.~~ |

## Tempo Controls

|                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_tempo.png|]] | ~~The tempo controls allow you to slow down and speed up a song. This is frequently useful for [beatmatching](manual#beatmatching_and_mixing) songs when mixing. The RATE slider changes the tempo of a song when it is moved. The PERM buttons apply fine adjustment to the RATE slider, and the TEMP buttons apply a temporary pitch-bend when depressed. The amount by which the PERM and TEMP buttons alter the pitch of the track can be changed in the *Options-\>Preferences-\>Interface* menu. The SYNC button attempts to automatically match the tempo of the song in the corresponding channel with tempo of the song in the other channel, based on the calculated BPM.~~ |

## Headphone and Flanger

|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_headphone.png|]] | ~~When toggled, the HEADPHONE button sends the selected channel's audio to the *Headphones* output audio device selected in the preferences under *Sound Hardware*. This feature is commonly used when [headphone cueing](manual#headphone_cueing) and [beatmatching](manual#beatmatching_and_mixing). The FLANGER button enables a built-in flanger effect on the selected channel. A flanger effect applies a "sweeping" sound to the channel and can add extra depth to a mix when used tactfully.~~ |

## Lautstärke und Equalizer

|                                      |                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_voleq.png|]] | Der "VOL" Regler kontrolliert die Lautstärke des jeweiligen Kanals. Der "GAIN" Knopf bringt extra Verstärkung um z.B. bei leisen Tracks die Lautstärke an die des Tracks auf dem anderen Kanal anzupassen. Die "HIGH", "MID" und "LOW" Knöpfe funktionieren als Equalizer für den entsprechenden Kanal. Sie reduzieren oder erhöhen die hohen, mittleren und tiefen Frequenzen entsprechend. |

## Wellenform

|                                         |                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_waveform.png|]] | ~~The waveform display shows the loaded tracks' waveforms near the playback position. On songs with certain dynamics, the waveform displays will visibly show the beats in the song. When a cue mark is placed, it is drawn on the waveform as a vertical white line. Clicking and dragging on a waveform allows you to seek through a song.~~ |

## Wellenform-Übersicht

|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_woverview.png|]] | Die Wellenform-Übersicht liefert wesentliche Informationen über den geladenen Track des jeweiligen Kanals. Von Rechts nach Links sind das: Tempo des Tracks in BPM, aktuelle Wiedergabeposition und die Laufzeit des Tracks. Am interessantesten ist aber die Darstellung des Tracks als Wellenform - nützlich um z.B. Pausen zu sehen um nicht beim DJing davon überrascht zu werden. Außerdem kann man durch einen Klick in die Wellenform innerhalb des Tracks an einen beliebige Position springen. |

## End of Track Modus

|                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[/media/manual/uioverview/ui_endoftrack.png|]] | Der "End of Track" Modus definiert, wie sich Mixxx\` verhält wenn das Ende eines Tracks erreicht wird. Verändert wird der "End of Track" Modus durch Klick auf das Symbol um zwischen den drei verfügbaren Optionen zu wechseln. Jeder Kanal hat seinen eigenen "End of Track" Modus der unabhängig voneinander geändert werden kann. **Stop** macht nichts weiter sobald der Track beendet ist, möglich wäre einen neuen Track in den Kanal zu laden oder rückwärts durch den aktuellen Track zu scrollen. **Loop** geht zurück zum Anfang des gerade beendeten Tracks und spielt ihn nochmals. **Next** lädt und spielt automatisch den nächsten Track in der Wiedergabeliste/Bibliothek. |

## Master and Crossfader Controls

|                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [[/media/manual/uioverview/ui_master.png|]] | ~~The crossfader (in the center of the picture) enables you to smoothly fade between the two channels and defines what you hear through the master output. When set all the way to the left, only channel 1 is heard, and set to the right, only channel 2 will be heard. Every position in between gives you the mixed output of both channels. (Note: The actual volume of each channel depends on the crossfader curve, defined in the *Crossfader* preferences pane.) The Volume and Balance knobs control the volume and the balance (stereo distribution) of the master output. The Pre/Main knob controls what you hear on the headphone output. It works like the crossfader but instead of crossfading between channel 1 and 2, it crossfades between the Master and Cueing signal. If the Pre/Main knob is set to the left, one only hears the cueing signal, which can be useful for prelistening tracks. The HeadVol knob controls the volume of the headphone output. The Depth, Delay and LFO knobs control the flanger. A flanger is an effect that mixes the input signal with a delayed copy of itself which leads to interferences in the signal and creates a comb-filter like effect. By routing the output of the effect back into the input (feedback), this effect can be enhanced. In Mixxx, the volume of the output signal that is routed back into the input can be controlled with the depth knob, which controls the intensity of the effect. The delay knob sets the initial value for the delay length. Inside the effect however, this value is not constant but modulated by an LFO (low frequency oscillator), controllable with the corresponding knob. If this is too technically for you just play around with it and see how the different parameters affect the sound. :)~~ |

## Library

<table>
<tbody>
<tr class="odd">
<td><img src="/manual/uioverview/ui_library.png" /></td>
<td><del>The library manages all your music files. This is where you can find the tracks you want to play and load them into a channel. Alternatively, you can also use your external filemanager and drop files onto the waveform display. The Library offers different viewing modes that can be switched with the combobox in the upper left corner. The second available viewing mode is the Play Queue which is like a playlist for the tracks you plan to play next. The Browse mode basically works like a usual file-manager and should be self explaining. In the Playlist mode, you can view and load playlists you've created. There is also a search function that filters the current view in realtime. The main viewing mode is the library view, which shows all files in your library. One must first create a library to use this view, but this will be done automatically during the first time Mixxx is run. If you want to rebuild your library (for example because you added or moved files) you can do this with \\Library-&gt;Rescan Library<br />
in the menu. To load a track into a player, you can either simply drag it to the waveform display or use the context menu (right-click on a track). The context menu also allows you to add a track to the play queue or a playlist (the playlist must be created first). Lastly, the context menu allows one to access a song's properties to check ID3 tags or set the BPM of the track manually.</del></td>
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

## Master and Headphone Outputs

\<del\>Mixxx has two audio paths: The **Master** output and the
**Headphones** output. The Master output is what a DJ should have
connected to their main speakers, while the Headphones output should be
connected to their personal headphones. The headphone output is
optional, and can be used for [Headphone Cueing](#headphone-cueing).

To configure the Master and Headphones outputs, enter Mixxx's
preferences and select the *Sound Hardware* pane. In order to select a
headphone device, either a soundcard with at least 4 channels of output
(two stereo outputs, as featured on 5.1 soundcards) *or* two separate
stereo soundcards is required. The output channel mapping, which
determines the physical jack on the soundcard that the audio comes out
of, can be selected under "Channel".\</del\>

<span class="underline">**Example Soundcard Configurations**</span>

**Single audio device (4 Channel Soundcard)**

    Master device:    Echo Digital AudioFire4   Channels: 1/2
    Headphone device: Echo Digital AudioFire4   Channels: 3/4

**Dual audio devices (Two Stereo Soundcards)**

    Master device:    ElCheapo USB Audio        Channels: 1/2
    Headphone device: SoundBlaster Live!        Channels: 1/2

## Using External Mixers

~~Currently, Mixxx has no special mode for routing the output of a
single deck to a separate output, which is what you need when using an
external mixer. However, this behaviour can be achieved with a simple
trick. Move the crossfader all the way to the left and turn the
"Pre/Main" knob all the way left as well. This will give you only the
pre-listen signal on the headphone output. Now, enable Cueing for the
second channel by toggling channel 2's HEADPHONE button. With this
setup, channel 1 will be playing on the master output and channel 2 will
be playing on the headphone output. The master and headphone outputs of
your soundcard should then be plugged into channel 1 and channel 2 of
your external mixer.~~

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

\<del\>The first thing to try if using ALSA is to set your Master output
hardware to just "default" instead of specific hardware. (This made a
huge difference on a test system with integrated Intel soundcard.) The
drawback to this is that system sounds (KDE beeps and such) will now be
mixed in and will come out the main output.

The second thing one can try to reduce system latency is getting a
realtime kernel. If you're using a binary kernel, this might be as
simple as installing a realtime enabled kernel with your package manager
(if your package system offers one of course). Otherwise download kernel
sources and the realtime patch for your kernel version. The patch can be
found [here](http://www.kernel.org/pub/linux/kernel/projects/rt/). Untar
the patch to your kernel source directory, apply it and
configure/install the kernel as usual.\</del\>

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
mit der das Audiosignal abgetastet wird. Da die meisten Audiodateien mit
einer Samplerate von 44100 Hz codiert sind, bringt das Erhöhen der
Samplerate in Mixxx selten verbesserte Audioqualität. Eine höhere
Samplerate kann in den Einstellungen unter *Sound Hardware* eingestellt
werden. Bedenken Sie das ein Erhöhen der Samplerate die CPU Last erhöht
und wahrscheinlich die geringstmöglich erreichbare Latenz erhöht.

## Sound API

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

## Vinyl Control

\<del\>Vinyl control allows a user to manipulate the playback of a song
in Mixxx using a real turntable as a controller. In effect, it simulates
the sound and feel of having your digital music collection on vinyl.
Many DJs prefer the tactile feel of vinyl, and vinyl control allows that
feel to be preserved while retaining the benefits of using digital
audio.

You can configure vinyl control through the *Vinyl Control* pane in the
preferences.

More information about Mixxx's vinyl control and supported hardware
configurations is available on the [vinyl control wiki
page](vinyl_control).\</del\>

[[/media/manual/preferences/vinylcontrol.png|]]

### Input Device Selection

Mixxx kann mit max. 2 Decks und Timecode Vinyls oder Timecode CDs
gesteuert werden. Wählen Sie in den "Deck 1" und "Deck 2" Auswahlmenüs
die Soundkarte(n), an welche die Decks angeschlossen sind. Im "Channel
selection" Auswahlmenü wählen Sie die Kanäle entsprechend so wie die
Decks an die Soundkarte(n) angeschlossen sind.

~~Mixxx supports vinyl control input through a single soundcard with
4-channels of input (two stereo line-in jacks), or through two separate
soundcards which each have 2-channels of input (a single stereo line-in
jack). Vinyl control requires the use of stereo line-in jacks - Mono or
microphone inputs will not work.~~

### Plattenspieler Vorverstärker

Viele Plattenspieler liefern nur ein unverstärktes Phono-Signal welches
zu einem Line-Signal verstärkt werden muss.Normalerweise erledigt ein
Mixer diese Verstärkung, wenn Sie aber Ihr unverstärktes Phono-Signal
direkt aus dem Plattenspieler in die Soundkarte schicken kann Mixxx die
Verstärkung übernehmen. Mit dem "Turntable Input Preamp" Regler kann die
Vorverstärkung des Phono-Signals eingestellt werden.

### Vinyl Konfiguration

Verschiedene Timecode Medien können benutzt werden um Mixxx zu steuern.
Wählen Sie im "Vinyl Type" Menü aus welche Art von Timecode-Vinyl oder
CD Sie benutzen wollen.

Mit der "Lead-in Time" Einstellung kann ein Bereich am Beginn der
Vinyls/CDs eingestellt werden, in welchem der Timecode ignoriert wird.
Das ist nützlich wenn der Timecode sehr nah an der Kante beginnt, was
das Back-Cueing am Anfang eines Tracks manchmal schwierig macht und die
Nadel des Plattenspielers herunterrutschen läßt. Wird eine "Lead-in
Time" von 20 Sekunden oder mehr eingestellt hat man also mehr Platz auf
dem Vinyl zum Cueing. Es ist auch hilfreich wenn das Timecode-Vinyl am
Beginn abgenutzt ist und nicht mehr zuverlässig funktioniert - einfach
die "Lead-in Time" bis zu einem Bereich erhöhen der intakt ist. Die
"Lead-in Time" kann so schrittweise erhöht werden und die Vinyls bleiben
länger benutzbar.

### Control Mode

~~Mixxx supports three control types on *all* of the timecodes we
support. "Absolute Mode" provides Mixxx with both pitch and position
information from the timecode, and allows you to seek by needle dropping
on your vinyl or seeking on your CDJ. "Relative Mode" takes the position
to be relative to your deck's starting point, and only controls the
pitch in Mixxx. It is not possible to seek using your deck in relative
mode. "Scratch Mode" is an enhanced version of relative mode, and only
applies to FinalScratch vinyl. Scratch mode improves performance
slightly while scratching, but is not necessary for better performing
timecodes like Serato. Finally, "Needle-skip Prevention" allows Mixxx to
detect and ignore small changes in needle position, such as when you've
accidentally bumped your turntable. This can be advantageous in a live
performance environment, but the downside is that it reduces
responsiveness during scratching. Consequently, disabling needle-skip
prevention is recommended for scratch performances.~~

### Signal Qualität

\<del\>A successful vinyl control setup hinges on good signal quality.
Many factors can affect signal quality, but the most important one is
ensuring the volume level of your timecode signal is moderate. A signal
that is too loud or too quiet will cause adverse performance, often
characterized by a loss of position data causing absolute mode to behave
like relative mode. For more information on improving signal quality and
troubleshooting, please see the [vinyl control wiki
page](vinyl_control).

Mixxx represents your timecode signal quality as a pair of real-time bar
graphs. The two graphs correspond to your "Deck 1" and "Deck 2" input
devices. The left-most column in each graph represents the overall
status of the *timecode signal*. A full bar with an "OK\!" indicates
everything is working well. The latter two columns in the graph
represent the raw, unprocessed stereo signal coming from your decks. A
good signal will appear as a pair of fluctuating green bars, each of
which will be out of phase. Red bars indicate the volume is too low or
two high, and the "Turntable Input Preamp" setting can be adjusted to
boost the volume.\</del\>

# DJing mit Mixxx

Mixxx sollte für erfahrene DJs und auch Einsteiger einfach zu bedienen
sein. Die Benutzeroberfäche orientiert sich an Hardware DJ-Mixern,
beinhaltet aber auch weitere Elemente um die Praxistauglichkeit zu
erhöhen (z.B. die paralle Darstellung der Wellenformen).

## Tracks laden

Tracks können auf verschiedene Weise in den Player geladen werden: ~~ \*
Per Rechtsklick the library track table: Right-clicking on a track in
the table will present the options "Load in Player 1" and "Load in
Player 2", among others. Making either selection will load a track into
a player. \* Drag-and-drop from library track table:
Dragging-and-dropping a song from the track table onto a waveform
display will load a track into a player. \* Drag-and-drop from external
file browser: Dragging-and-dropping a song from an external file browser
directly onto a waveform display in Mixxx will load that song. This
function is also known to work on some platforms with other
applications. For example, on OS X, dragging-and-dropping a track from
iTunes onto one of Mixxx's waveform displays will load that song into a
player.~~

## Waveform displays

\<del\>There are two main **waveform displays** in Mixxx that are used
to display the waveform of the songs you are mixing. These are useful
because they allow you to see features in a song (like a breakdown)
before you hear them. The waveform displays are aligned parallel to each
other in order to make beat matching easier, as it is possible to
beatmatch visually by aligning the beats that appear in each waveform.

Clicking and dragging on a waveform allows you to seek through a song in
both directions. The waveform display is updated in realtime upon
seeking. There are two smaller **waveform summary** displays located
adjacent to the main waveform displays. These smaller displays show the
waveform envelope of the entire song, and are useful because they allow
DJs to see breakdowns far in advance. Vinyl DJs will find this familiar
because quiet sections of songs can be visually distinguished when
looking at a vinyl record, and this is a useful tool when planning your
mixes on-the-fly.\</del\>

## Beatmatching und Mixen

Als **Beatmatching** bezeichnet man das taktgenaue Synchronisieren des
Tempos zweier Tracks. \<del\> In Mixxx kann das **Tempo** von zwei
Tracks angepasst werden indem der jeweiligen "RATE" (Playback Rate)
Regler bewegt wird. You can adjust the **phase** of the beats by
clicking-and-dragging on either waveform display to temporarily slow
down one of the songs until the beats are aligned. Die "TEMP"(Temporary
Pitch Bend) Buttons ermöglichen die vorübergehende Anpassung des Tempos.
So kann can also be used to momentarily adjust the playback rate,
allowing you to "shuffle" the beats in a song forwards or backwards, so
they can be aligned with another song.

Once the tempos are matched and the beats aligned between two songs,
they are said to be beatmatched. A "perfect" beatmatch is near
impossible - there will always be some tiny difference in the playback
rates. A keen DJ will keep his or her ears open and listen for the beats
drifting out of alignment. This has a distinct "double bass kick" sound
which is often preceded by the kick weakening in intensity (as the two
kicks drift out of phase). When this happens, the beats can be realigned
by simply tapping one of the temporary pitch bend buttons a few times in
the appropriate direction. Now get out there and make Tiesto
jealous\!\</del\>

## Headphone Cueing

Mit dem Headphone Cueing (Vorhören) hört der DJ den nächsten Track in
seinem Kopfhörer ab bevor er live gespielt wird. Mixxx ermöglicht dem DJ
das Audiosignal von beiden Kanälen vorzuhören indem der jeweilige
"HEADPHONE" Button aktiviert wird. Durch das Headphone Cueing kann der
DJ die Geschwindigkeit des nächsten Tracks an den aktuellen Track
anpassen bevor er sie mit Hilfe des Crossfaders mixt.

## Einen Mix aufnehmen

Mixxx's Master Signal kann folgendermaßen in Echtzeit als Audiodatei
(unkomprimierte lineare PCM WAV (RIFF)) aufgenommen werden :

1.  In der Menüleiste , "Options" klicken
2.  "Record Mix" klicken
3.  Speicherort und Dateiname angeben, dann "OK" klicken
4.  Mixxx beginnt erst dann mit der Aufnahme wenn 2 Sekunden Sound zu
    hören sind. Um auch die ersten 2 Sekunden aufzunehmen - einfach die
    PLAY Taste , dann sofort CUE (oder PAUSE ) drücken, 2 Sekunden
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
unterstützten Controller und ihrer Beschränkungen . Die Unterstützung
für die Geräte variiert je nach Betriebssystem, also stellen Sie sicher
das die Dokumentation gelesen wurde.

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
