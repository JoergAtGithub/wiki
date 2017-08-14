# JB Systems dj-kontrol 3

![https://jb-systems.eu/media/catalog/product/cache/19/image/1600x1600/9df78eab33525d08d6e5fb8d27136e95/3/8/382-1.jpg](https://jb-systems.eu/media/catalog/product/cache/19/image/1600x1600/9df78eab33525d08d6e5fb8d27136e95/3/8/382-1.jpg)

  - [Hersteller Seite](https://jb-systems.eu/de/dj-kontrol-3)
  - [Forum Eintrag (Mapping
    Download)](https://www.mixxx.org/forums/viewtopic.php?f=7&t=9281)

Dieser DJ Controller besitzt eine 2 Kanal Soundkarte mit symetrischen
XLR Ausgang oder unsymetrischen RCA (Chinch) Ausgang, welcher mit einem
Schalter umgeschaltet werden kann. Der Controller wird über USB mit dem
Computer verbunden und ist so einsatzbereit. Es wird jedoch empfohlen,
das zusätzliche 5V 1A Netzteil ebenfalls zu verwenden, um die Stabilität
zu garantieren. (wenn zb. die USB Stromversorgung einbricht)

## Benutzung

Lade die .zip Datei aus dem Forum herunter (Link oben), .zip entpacken
und dann die zwei Datein (.js / .xml) in den Mixxx / Controllers Ordner
kopieren.

  - Linux: \~/.mixxx/controllers
  - Windows: %USERPROFILE%\\Local Settings\\Application
    Data\\Mixxx\\controllers
  - Mac OS X: \~/Library/Application Support/Mixxx/controllers

Starte Mixxx

  - Manchmal blockiert unter Linux das Programm pulseaudio die
    Verwendung der Soundkarte in Mixxx.
  - Dazu im Terminal Mixxx mit: "pasuspender mixxx" starten

In Mixxx:

1.  Options-\>Einstellungen-\>Sound Hardware:

<!-- end list -->

  - Sound API: ALSA
  - Sample Rate: 48000Hz
  - Output / Master / JB Systems DJ-Kontrol 3: USB Audio / Channels 3 -
    4
  - Output / Headphones / JB Systems DJ-Kontrol 3: USB Audio / Channels
    1 - 2

<!-- end list -->

1.  Options-\>Einstellungen-\>Controllers:

<!-- end list -->

  - Haken: Enabled
  - In der Liste mit den Vorgaben (Presets) den richtigen auswählen

Nun sollte der Controller in Mixxx funktionieren.

## Mapping

[[/media/jbs_dj-kontrol_3_mapping2.png|]]

1.  Select Knop
2.  Load to Deck 1
3.  Load to Deck 2
4.  Back 
5.  Deck Gain
6.  EQ High
7.  EQ Mid
8.  EQ Low
9.  Deck Volume Fader
10. Mic Volume
11. Mic Input
12. Crossfader
13. Crossfader Curve Select
14. CUE Mix
15. CUE Volume
16. Kopfhörer Ausgang
17. CUE Pre-fader listening (Pfl) Deck 1
18. CUE Pre-fader listening (Pfl) Deck 2
19. Master (Output) Volume
20. Set Cue
21. Cue
22. Play/Pause
23. Jogwheel
24. Scratch
25. SYNC
26. Loop In
27. Loop Out (Exit)
28. Reloop
29. 2-Beat Loop
30. 4-Beat Loop
31. 8-Beat Loop
32. Halve Loop
33. Double Loop
34. Pitch range
35. Speed-/Pitch Fader
36. Pitch Bend +/-
37. Hot-Cue, löschen mit Shift
38. Shift Mode
39. Needle Drop Sensor
40. Key
41. Effect on/off
42. Effect select
43. Effect Parameter 1
44. Effect Parameter 2
45. USB Port
46. RCA unsymetrischer Ausgang
47. XLR symetrischer Ausgang
48. Schalter zw. XLR/RCA
49. externes Netzteil

-----

### Jogwheel Funktionen

  - Scratch Mode An: Berührung auf Oberseite - Scratch
  - Scratch Mode An: Berührung an der Seitenkante - pitchbend
  - Scratch Mode Aus: immer pitchbend
  - Shift Mode An: Loop Move

### Spezielle Funktionen

  - Parameter 1 Knob steuert dry/wet
  - Parameter 1 Shift Knob (Filter) steuert den Super Knob
  - Parameter 2 Knob steuert den ersten Parameter des gewählten Effects
  - Pitch Fader sind invertiert (hoch = + , runter = -)
  - Shift drücken zum Aktivieren und nochmal drücken zum Deaktivieren

### (noch) keine Funktion

  - Xfader Curve Btn
  - Pitch Lock Btn
  - S.Start Btn
  - Zoom Push Btn
  - Reverse Btn
  - Jogwheel Led Animationen
