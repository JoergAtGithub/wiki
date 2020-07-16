# Bear and Bar Edit Workflow

This page is intended to discuss a smooth workflow when editing betas and bars. It shall also fix requirements and point out limitations of the chosen model.  

## Assumptions ##

We need to make some assumptions that will help to keep our model simple but powerful to allow certain DJ tricks while being maintainable. 

* The beat and bar annotation reflects the music like it was written on the musical sheet. Slight jitters typical for live music are smoothed out to a constant tempo within each bar to make the beats usable for looping and beat matching.  
* The BPM value used in Mixxx is defined as quarter notes per minute. This helps to compare the tempo of different tracks independent from the denominator x/4 x/8 or x/16. 
  * For instance a 7/8 track has three normal 1/4 beats and one 1/8 beat counted 1 + 2 + 3 + 4 +. Let's assume the underlying 1/8 beat grid has 200 BPM, this would make the track sort at the library near to the fast tracks, which is probably not what we want. If we take only the real beats into account we get an average of 114,3 BPM this is also useless because no beat is in the distance of that BPM vale. 100 BPM, the tempo of 2/8 is here the suitable value that help to match track and can be used for looping.
  * This also helps to compare a base tempo to double or half time sections within the same track. This happens often in dubstep and drum & bass.
* Time signatures are limited to integers for the top number (beats per bar) and powers of 2 for the denominator (what counts as a beat).
  * What beats are shown on the waveform and used for quantizing is determined by the bottom number of the time signature. This creates a visual indication that an 8/8 section is double time of a 4/4 section but still the same tempo because Mixxx will calculate tempo as 1/4 notes per minute.
  * In case of bars with fractional numbers of beats, both the numerator and denominator can be multiplied to get an integer nominator. For example if a bar in an otherwise 4/4 track is cut 1/2 beat short, that one bar can be marked as 7/8. All the 1/8 notes in that bar will be shown on the waveform which is useful as a visual indicator that one bar is different from the ones around it.
  * [Irrational time signatures](https://en.wikipedia.org/wiki/Time_signature#Irrational_meters) can always be represented as a rational time signature with a different tempo. We will not complicate Mixxx's model of time signatures with such an obscure concept.
* Every bar (musical measure) has a constant tempo. This is not all the time true, but for slowly tempo changing tracks good enough to have no notable double beats, but it still allows looping and beat matching without introduce an unsteady pitch at a synced follower. The follower can change the tempo at the bars which sounds OK. If a leader changes the tempo quickly the user can individually place the beats on a finer beat grid.
  * This assumption will be used to help the analyzer produce useful results. However, the protocol buffer format for data storage will not assume this. Every individual beat will be stored in the protobuf.
  * The signature is used to snap the beats into.
  * Tempo is calculated from the time signature and bar length. This way the position of the beats within the bar do not matter for the calculation of tempo and they could potentially be adjusted after analysis.
* The beat and bar detector is optimized to detect constant 4/4 bars. 
* The beat detector can take a measure template as input to detect other measures. The onsets will be stored as immutable data to facilitate this so expensive computations do not need to be repeated.
* Mixxx 2.2 beats are imported as individual placed beats.    

## Workflow ##

### Constant 4/4 Track ### 

Nothing to do, the beat, bar detector is able to do everything automatically. 

### 4/4 Track with changing tempo ### 

The detector tries to follow the changes, if this fails: 
* adjust a down-beat
* Select "infer right" to start the beat detector again from this point. 

### 4/4 Track with skipped or added beats ### 

[Joan Jett - I Love Rock 'n' Roll](https://www.youtube.com/watch?v=iC8oP4Z_xPw) has a chorus of 4/4 4/4 4/4 3/4 which makes the detected down-beat shift by one. The user needs to help here. 

original:
```
|   d   d   d   |   d   d   d   |   d   d   d   |   d   d   |   d   d   d   |   d   d   d   | 
```
beat detector:
```
|   d   d   d   |   d   d   d   |   d   d   d   |   d   d   d   |   d   d   d   |   d   d   d   
```
1 step: adjust the down-beat
```
|   d   d   d   |   d   d   d   |   d   d   d   |           |   d   d   d   |   d   d   d 
```
Mixx will change the tempo of the measure. Remember that we snap the beats to the grid mad up by the signature and not to the detected beats. 
```
|   d   d   d   |   d   d   d   |   d   d   d   |  d  d  d  |   d   d   d   |   d   d   d
```
2 step: Adjust the nominator of the signature to 3 for a 3/4 measure  
```
|   d   d   d   |   d   d   d   |   d   d   d   |   d   d   |   d   d   d   |   d   d   d
```
Done 

This works in the same if the artist added a beat. 

In case the artist only skips a fraction of a beat, you may change the denominator for a finer gids the beats are snapped to. For instance if a 1/2 beat is skipped, the time signature will be 4/4 7/8. By default the last beat quarter of a measure is shorten.

```
.   .   .   .   . . . . . . . .   .   .   .   .  // grid    
|   d   d   d   |   d   d   d |   d   d   d   |  // beats 
```

### Odd measures like 7/16 Tracks with shifted beats ###

sometimes beats are slight shifted to sound interesting like:  
[Igorrr - Vegetable Soup](https://www.youtube.com/watch?v=5LN7W3EtRMg)

The beat detector fails with this track. It is detected as a 70 BPM track, because only the downbeats are found and the tempo is shifting heavily. Here the user can manually annotate a first measure. 
I would say you need a 24/32 grid with beats at 1 / 8 / 14 / 20 @ 840 1/32-BPM = 105 BPM   

Here is the workflow for a less exotic 7/16 example:  

First he can made up fine 1/16 grid which is counted:
```
1e+a2e+1e+a2e+1e+a2e+1e+a2e+a 
.............................   
```
Now set the downbeats, and adjust the tempo by selecting the number of beats in the measure. in this case 7/16 
```
1e+a2e+1e+a2e+1e+a2e1e+a2e+a 
D......D   
```
Than place the quarter beats. 
```
1e+a2e+1e+a2e+1e+a2e1e+a2e+a 
D...b..D   
```
Now press "infer right" and the beat detector will snap the measure template to the detected beats. 

Done. 

### Odd measures like 7/8 Tracks ###

[Genesis - Dance on a Volcano](https://www.youtube.com/watch?v=TBcnjx05a1s) 

This track can be counted as :
```
1 + 2 + 3 + 4 1 + 2 + 3 + 4 1 ... 
```

It is detected as a 1/4 Track with a off beats in very second measure. 
Since it is an 1/8 track, every 1/8 note is maked as beat. 
TODO ... 
  

## supporting data structure ##

### original Mixxx 2.3 ###

```
enum Source {
  ANALYZER = 0;
  FILE_METADATA = 1;
  USER = 2;
}

message Beat {
  optional int32 frame_position = 1;
  optional bool enabled = 2 [ default = true ];
  optional Source source = 3 [ default = ANALYZER ];
}

message Bpm {
  optional double bpm = 1;
  optional Source source = 2 [ default = ANALYZER ];
}

message BeatMap {
  repeated Beat beat = 1;
}

message BeatGrid {
  optional Bpm bpm = 1;
  optional Beat first_beat = 2;
}
```

### new (backwards compatible) ###

```
enum Source {
  ANALYZER = 0;
  FILE_METADATA = 1;
  USER = 2;
}

message TimeSignature {
  optional int32 beats_per_bar = 1 [ default = 4];
  optional int32 note_value = 2 [ default = 4 ];
}

message Beat {
  optional int32 frame_position = 1;
  optional bool enabled = 2 [ default = true ];
  optional Source source = 3 [ default = ANALYZER ];
  optional double frame_position_fractional = 4;
  optional Type type = 5 [ default = BEAT ];
  optional TimeSignature signature = 6;
}

message BeatMap {
  repeated Beat beat = 1;
}

message LegacyBpm {
  optional double bpm = 1;
  optional Source source = 2 [ default = ANALYZER ];
}

message LegacyBeatGrid {
  optional Bpm bpm = 1;
  optional Beat first_beat = 2;
}
```

To maintain either backward compatibility and make the most of the new Type filed and Time signature fields, we must assert the following assumptions: 
* When adjusting a beat frame_position and frame_position_fractional is written. The first is the fractional value rounded to the nearest integer. 
* The "note_value" and the following BAR are creating a grid. All beats in between must be exactly on the grid. 
* The LegacyBeatGrid is migrated by putting all individual beats into the the BeatMap.

### possible sparse representation for reference only ###

This reflects the minimum info we need for the new model. This is only shown here as reference for an internal data structure, Mixxx can use in the Beat Grid Editor. 

```
message Bar {
  required double frame_position = 1 [ default = 0 ];
  optional Source source = 2 [ default = ANALYZER ];
  // 0 for individual set beats without signature 
  // -1 END for the last Bar  
  // -2 REPEAT, for repeating the previous measure until a next beat is set 
  optional int signature_nominator = 4 [ default = 0 ];   
  optional int signature_denominator = 5 [ default = 4 ];  
  repeated int quarter_beats = 6; // can be empty for regular 1/4 beats   
}

```

For a repeated 7/16 measure like above the notation of a whole track looks like like: 

```
[
  frame_position = 0;
  source = USER;
  signature_nominator = 7; 
  signature_denominator = 16;  
  quarter_beats[1] = 4; // for 4/16
]  
[
  frame_position = 80000;
  source = USER;
  signature_nominator = -1; // REPEAT
]  
[
  frame_position = 375000;
  source = USER;
  signature_nominator = -2; // END
]    
```









  




 
 








       


