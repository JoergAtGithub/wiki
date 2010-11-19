====== Hercules DJ Control Steel (page under construction)======

{{hardware:hercules_dj_control_steel.jpg?600|}} 



The Hercules DJ Control Steel is a USB MIDI controller (very similar to DJ Console RMX but without a built in sound card). It is compatible with Mixxx versions 1.6.1+herc and later. It works in Linux 32/64 bits (from kernel ~2.6.27+), Windows (XP, Vista, 7), and MAC OS X (10.4.11 (Tiger)/ 10.5.x (Leopard)/ 10.6.x (Snow Leopard) 32-bit)

=====MIDI driver=====

The midi device on the Steel is NOT USB-midi class compliant. For that reason it requires specific drivers to be working on each OS.


====MAC OS / Windows====

Drivers for MAC OS X and Windows can be found on [[http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=215&cid=1|Hercules support page]].

====Linux====
Hercules has released a common MIDI-driver for their DJ controllers. Read more on the page for [[Hercules Linux kernel module]]


===== Mapping for Mixxx =====
You need to update the mapping with following files :
[[http://slist.lilotux.net/linux/deejay/mixxx/|Link to mapping files]]
{{:hercules_dj_control_steel_top_face.png?400 |}}

===Global controls  ===
^ Control  ^ Function |
^ FX Wet/Dry Knobs (1) | Unmapped ||
^ FX Apply Select (1) | Unmapped ||
^ Cross-Fader (24) | Fades between left and right deck|
^ Vol. Main (23)| Controls output volume of your mix|
^ Balance (6)| Controls balance between left and right audio channel of your mix|
^ Scratch (7)| Toggles scratch on and off which changes the function of the deck jog wheels|
^ Up / Down (8)| Moves up and down in the library track list|
^ Up / Down (8) + Jog (18) | Rapid Track List scrolling |
^ Left / Right (8)| Moves up and down between the library sections |
^ (10), (11) | TODO |


===Deck / Channel specific controls ===
^ Control  ^ Function |
^ Cue (21)| Sets the cue point if a track is stopped and not at the current cue point \\ Stops track and returns to the current cue point if a track is playing. \\ Plays preview if a track is stopped at the cue point for as long as 
^ Stop (20) | Stop + Reset Track to beginning  |
^ Play/Pause (19)| Starts playing a loaded track if stopped. If track is currently playing it stops the track|
it's held down |
^ Cue (21) + Play (19) | Pushing Play while holding Cue will cause track to continue to play after Cue is released  (buggy)|
^ Jog wheel | Seeks forwards and backwards in a stopped track \\ Temporarily changes the playback speed for playing tracks \\ Scratches both stopped and playing tracks when scratch mode is on \\ Moves up / down in the track list if either Up or Down is held down|
^ Forward / Backward | Seeks at high speed in a track |
^ Load Deck A/B | Loads the currently selected track in the track list to the related deck |
^ Cue Select | Toggles this decks output to the monitor (headphones) on and off |
^ Pitch | Adjusts playback speed +/-10% (can be adjusted in the preferences) |
^ Sync | Automatically sets pitch so the BPM of the other deck is matched |
^ Pitch Bend- | Resets the pitch to the tracks normal playback speed (FIXME)|
^ Pitch Bend+ | TODO |
^ Bass | Adjusts the volume of a channels low frequency content (ex. bass drum) \\ Adjusts flanger period when Effect Shift is held down |
^ Medium | Adjusts the volume of a channels mid frequency content (ex. vocals) \\ Adjusts flanger delay when Effect Shift is held down |
^ Treble | Adjusts the volume of a channels high frequency content (ex. hi-hats) \\ Adjusts flanger depth when Effect Shift is held down |
^ Kill (Bass / Medium / Treble) | Toggles output of a frequency band on and off |
^ Gain | Controls a decks input volume |
^ Vol. Deck A/B | Controls a decks output volume |
^ Stop | **Deck shift** changes behavior of other controls related to this deck when held down|
^ Forward / Backward | Adjusts position of loop in/out and hot cues when a loop / hot cue button is held down |
^ Bass | Adjusts the volume of a channels low frequency content (ex. bass drum) \\ Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting \\ Adjusts flanger period when Scratch is held down |
^ Medium | Adjusts the volume of a channels mid frequency content (ex. vocals) \\ Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting  \\ Adjusts flanger delay when Scratch is held down |
^ Treble | Adjusts the volume of a channels high frequency content (ex. hi-hats) \\ Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting  \\ Adjusts flanger depth when Scratch is held down |


^ Control  ^ Default Mixxx Mapping ^

|| 1 (9) | Flanger on/off ||
|| 2 (9) | Hotcue 1 set ||
|| 3 (9) | Hotcue 2 set ||
|| 4 (9) | Reverse ||
|| 5 (9) | Hotcue 1 goto ||
|| 6 (9) | Hotcue 2 goto ||
|| 7 (9) | loop in ||
|| 8 (9) | loop exit ||
|| 10 (9) | loop out ||
|| 9,11,12 (9) | Unmapped ||





