# Bear and Bar Edit Workflow

this page is intended to discuss a smooth workflow when editing betas and bars. It shall also fix requirements and point out limitations of the choosen model.  

## Assumptions ##

We need to make some assumptions that will help to keep our model simple but powerful to allow certain DJ tricks while being maintainable. 

* The beat and bar annotation reflects the music like it was written on the musical sheet. Slight jitters typical for live music are ironed out to make the beats usable for looping and beat matching.  
* The BPM value used in Mixxx is defined as quarter notes per minute. This helps to compare the tempo of different tracks independent from the denominator x/4 x/8 or x/16 ...
* It does not matter if there is actually a beat at every quarter note.
* Only quarter notes beats are marked as beats. In odd time signatures the supersized beats are marked as beats.   
* Every bar (musical measure) has a constant tempo. This is not all the time true, but is close enough to the truth but still allows looping and beat matching, without introduce a yowling pitch at the follower. The follower can change the tempo at the bars which sounds OK. 
* The beat and bar detector is optimized to detect constant 4/4 bars. 
* The beat detector can take a measure template as input to detect other measures.
* The time signature consists always of a integer nominator the note count and a integer denominator a note length relative to the quarter note BPM value listed in the library.  
* The signature is used to snap the beats into.  
* In case of odd measures, the denominator can be increased to make up a finer grid to palace a beat more exactly. 
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


## supporting data structure ##

```
message Bar {
  required double frame_position = 1 [ default = 0 ];
  optional Source source = 2 [ default = ANALYZER ];
  optional int signature_nominator = 4 [ default = 4 ];  // 0 for individual set beats 
  optional int signature_denominator = 5 [ default = 4 ];  
  repeated int quarter_beats = 6; // can be empty for regular 1/4 beats   
}

```

For a 7/16 measure like above it looks like: 

```
  frame_position = 0;
  source = USER;
  signature_nominator = 7; 
  signature_denominator = 16;  
  quarter_beats[1] = 4; for 4/16    
}

```









  




 
 








       


