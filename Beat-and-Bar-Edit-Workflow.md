# What are tempo, beat, bars and time signatures?
Tempo is the speed a passage is meant to be played. One important consequence from its definition is that it may not have been played or be perceived as it was promised. Another one is that it's an abstract and relative concept. BPM is not the same as tempo.

A beat is a unit of length. The beats per minute is then one measurement of this speed, as distance over time. When we are counting the tempo our result is always relative to the window of beats we are counting. A beat can have different lengths or duration. This is the lower number of the time signature.

Semibreve - 1 |
Minims - 1/2 |
Crotchets - 1/4 |
Quavers - 1/8 |
Semi-Quavers - 1/16 |
Dime-Semi Quavers - 1/32 |

Using different note lengths can cause a different BPM values for the same tempo. 
It is not always possible to define a "correct" way of measuring the tempo in music; a piece of music can be interpreted in different tempos.
Mathematically BPMs values of 240, 120, or 60 with the respective note lengths of 1/8, 1/4 and 1/2 would result in the exact same tempo.
However, the interpretation of musicians and thus the perception of the listener will be different from those. It's usually considered that a piece with a slower BPM will be more serene.

The analyzer will always use a quarter note as the note length to count the tempo.

A measure is a restrict space in which the beats are placed. Since the beat length is defined in relative terms we need a regular space, of a certain duration to place them. Visually it's defined as bar lines that organize the notes on sheet music.

The main purpose of the bar is to chop the music in equal lengths so that notes of different relatives beat lengths can balance each other and make melodies. The upper number of the time signature restrict how many beats are allowed inside each measure. 

A 4/4 measure means that it fits 4 crotchets. The simplest possible melody is to put 4 crotchets. A different melody is to play 1 semibreve. Another more sophisticated can be play 4 1/8 notes, 2 crochets and a minim. Music is also silence, so for every note, there is an equally sized rest. So another melody could be 1/2 rest and then 16 dime-semi-quavers. We can put any combination of notes and rest inside a measure as long as we respect that their size must, in this case, be the same of 4 crotchets. 

# What is a legacy beatgrid?

The beatgrid is an offset measured in frames and tempo measured in BPM.
With this, we can unequivocally determine every beat position, and assign any arbitrary frame to a beat index.
It is a visual representation of metronome that has a start position and clicks on BPM that is displayed on the waveform.
It's also the metronome we use for sync

The beatgrid is very good for clicking on time on tracks that were made using a metronome, ie - drum machine.

# What is beatgrid problem?

Two problems affects even tracks made with drum machines: 
* [1] Abrupt changes - the record has a passage in a different tempo.
* [2] Accelerando or ritardando parts. Machines can even make tempo changes inside a measure level.

Tracks that are played by musicians share these problems and add their owns.
* [3] The band is unintentionally falling short or running ahead of the beat, but trying to catch up to the metronome.
* [4] The performers do not care about the metronome BPM. Tempo adds a lot of expressiveness to the music. In fact, a lot of musicians such the like of Beethoven would argue that the metronome is a silly thing. In traditional sheet music, for example, the tempo is defined very vague in words that encompassed a range of BPMs, the interpreters can freely speed up and slow down the passages inside this range to emphasize particular parts of the melody. A slight faster tempo will make the music more euphoric for example. 

# What is beatmap?

The beatmap is made as series of beats positions measured in frames.
It's a visual representation of every detect beat in the waveform.
It's the metronome that counts the tempo over 12 beats and is reset every beat for sync.

# What is beatmap problems?

* [5] The noise of the analysis is not treated and the tempo value is always fluctuating.
* [6] We can not unequivocally determine any beat position or assign a frame to an arbitrary beat. We have the real distance to the next detected beat and we also have estimated distance from the computed bpm.

# What is the new -beat|rhythm-grid?

* It should overcome the problems outlined above. While also introducing bar, phrases and sections markers.
* [1] - This is trivial, we simply reset the metronome, ie -the grid, on an arbitrary frame with a new BPM.
* [2] - If the change happens on the measure level it's also easy. We reset the grid on the measure. If the tempo change happens inside a measure then is not that easy. There is no notation for that in sheet music. Also, the analyzer is unable to detect these reliable as it relies on periodicity detection. Finally, does this have any use?
* [3 and 4] - We look for the next longest sequence of beats that stays inside a tempo within a 25ms error and reset the metronome for this amount of beats in this tempo. We aligning these sequences so they start ideally on a section or a phrase but they should at least always be at least one measure long.
* [5 and 6] - We don't use the sequence of detected beats. We only use our metronomes to compute the distance from any arbitrary beat.



# Beat and Bar Edit Workflow

This page is intended to discuss a smooth workflow when editing betas and bars. It shall also fix requirements and point out the limitations of the chosen model.  

## Assumptions ##

We need to make some assumptions that will help to keep our model simple but powerful to allow certain DJ tricks while being maintainable. 

* The beat and bar annotation reflects the music like it was written on the musical sheet. Slight jitters typical for live music are smoothed out to a constant tempo within each bar to make the beats usable for looping and beat matching.  
* The BPM value used in Mixxx is defined as quarter notes per minute. This helps to compare the tempo of different tracks independent from the denominator x/4 x/8 or x/16. 
  * For instance, a 7/8 track has three normal 1/4 beats and one 1/8 beat counted 1 + 2 + 3 + 4 1. Let's assume the underlying 1/8 beat grid has 200 BPM, this would make the track sort at the library near to the fast tracks, which is probably not what we want. If we take only the real beats into account we get an average of 114,3 BPM this is also useless because no beat is in the distance of that BPM vale. 100 BPM, the tempo of 2/8 is here the suitable value that helps to match the track and can be used for looping.
  * This also helps to compare a base tempo to double or half time sections within the same track. This happens often in dubstep and drum & bass.
* Time signatures are limited to integers for the top number (beats per bar) and powers of 2 for the denominator (what counts as a beat).
  * In case of bars with fractional numbers of beats, both the numerator and denominator can be multiplied to get an integer nominator. For example, if a bar in an otherwise 4/4 track is cut 1/2 beat short, that one bar can be marked as 7/8. All the 1/8 notes in that bar will be shown on the waveform which is useful as a visual indicator that one bar is different from the ones around it.
  * [Irrational time signatures](https://en.wikipedia.org/wiki/Time_signature#Irrational_meters) can always be represented as a rational time signature with a different tempo. We will not complicate Mixxx's model of time signatures with such an obscure concept.
* Every bar (musical measure) has a constant tempo. This is not all the time true, but for slowly tempo changing tracks good enough to have no notable double beats, but it still allows looping and beat-matching without introducing an unsteady pitch at a synced follower. The follower can change the tempo at the bars which sounds OK. If a leader changes the tempo quickly the user can individually place the beats on a finer beat grid.
  * This assumption will be used to help the analyzer produce useful results.
  * The signature is used to snap the beats into.
  * Tempo is calculated from the time signature and bar length. This way the position of the beats within the bar does not matter for the calculation of tempo and they could potentially be adjusted after analysis.
* The beat and bar detector is optimized to detect constant 4/4 bars. 
* The beat detector can take a measure template as input to detect other measures. The onsets will be stored as immutable data to facilitate this so expensive computations do not need to be repeated.
* Mixxx 2.2 beats are imported as individually placed beats.    

## Workflow ##

### Constant 4/4 Track ### 

Nothing to do, the beat, bar detector is able to do everything automatically. 

### 4/4 Track with changing tempo ### 

The detector tries to follow the changes. If this fails: 
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

In case the artist only skips a fraction of a beat, you may change the denominator for a finer gids the beats are snapped to. For instance, if a 1/2 beat is skipped, the time signature will be 4/4 7/8. By default, the last beat quarter of a measure is shortened.

```
.   .   .   .   . . . . . . . .   .   .   .   .  // grid    
|   d   d   d   |   d   d   d |   d   d   d   |  // beats 
```

### Odd measures like 14/16 Tracks with shifted beats ###

sometimes beats are slightly shifted to sound interesting like:  
[Igorrr - Vegetable Soup](https://www.youtube.com/watch?v=5LN7W3EtRMg)

The beat detector fails with this track. It is detected as a 70 BPM track because only the downbeats are found and the tempo is shifting heavily. Here the user may manually annotate a first measure, which looks like a normal 7/8 measure, counted:  

```
1 + 2 + 3 + 4 1 + 2 + 3 + 4 1...
```

looking more closely beat 4 is shifted 1/16 in front.

```
1 + 2 + 3 + 4 1 + 2 + 3 + 4 1 ...
1e+a2e+a3e+4e+1e+a2e+a3e+4e+1...
```

If we look more closely we see the beat 3 shifted 1/32 to the front  
So we may switch to a 1/32 denominator if it is worth the work. 

Workflow: 

The user can set a loop and listen unit he is confident to have found a measure. 
Then he can mark the single beats. 
When done, Mixxx will use try to find a constant time signature that matches best to the betas but with the smallest denominator that is in the grange of +- 25 ms around the user set beats. 
The user can now tweak this proposal and accept it. 
Once accepted the user set beat are adjusted to the const grid. 

Now he can infer left. 

If a user recognizes a beat is always too early or too late, or he has marked the wrong beat he can change the signature. 
All beats of the whole section are temporary shifted to the nearest beat in the new git. 
If the user is confident with the decision he can store the new beat grid and is done.    


Here is the workflow of a 7/16 example where Mixx has already detected correct 1/4 beats and tempo but fails to detect the signature.   

First, the user needs to verify or adjust the downbeats. Since they are off the 1/4 grid. The user needs to switch to a 1/16 grid first. 

```
1   2   3   4   1 
1e+a2e+a3e+a4e+a1e+a 
D......D......D  
1e+a2e+1e+a2e+1e+a2e+1e+a2e+a 
```
Then place the quarter beats. 
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

It is detected as a 1/4 Track with an off beat in every second measure. 
Since it is a 1/8 track, every 1/8 note is marked as a beat.
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
* The "note_value" and the following BAR are creating a grid. All beats in-between must be exactly on the grid. 
* The LegacyBeatGrid is migrated by putting all individual beats into the BeatMap.

### possible sparse representation for reference only ###

This reflects the minimum info we need for the new model. This is only shown here as a reference for an internal data structure, Mixxx can use in the Beat Grid Editor. 

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

For a repeated 7/16 measure like above the notation of a whole track looks like: 

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
## Controversial Topic ## 

* Showing every denominator as beat vs. showing real beats. 
  * In odd time signatures the emphasized beats are marked as beats. The denominator can be increased to make up a finer grid to palace a beat more exactly.  
  * What beats are shown on the waveform and used for quantizing is determined by the bottom number of the time signature. This creates a visual indication that an 8/8 section is the double time of a 4/4 section but still the same tempo because Mixxx will calculate tempo as 1/4 notes per minute. In an x/8 track, all the 1/8 notes in that bar will be shown on the waveform which is useful as a visual indicator that one bar is different from the ones around it.
* A measure is always constant vs changing speed within a measure. 
* Individual beats off the denominator grid vs all beats are on the grid.
  * This assumption will be used to help the analyzer produce useful results. The surrounding code asserts the assumption. 
  * This assumption will be used to help the analyzer produce useful results. However, the protocol buffer format for data storage will not assume this. Every individual beat will be stored in the protobuf. 
* forward and backward compatible representation
* sparse representation  

 
## Ideas and Opinions ##

To be integrated: 

**@Be-ing**

I think showing the notes indicated by the denominator on the waveform would be useful in these cases to be a visual indication of a usual bar.

I do not think marking emphasized beats within the bar is necessary, at least for a minimum viable product. Perhaps we can consider adding it later.

As Swiftb0y and I were saying before, assuming a constant tempo within a bar is a useful generalization for analysis. But there is no need to limit the flexibility of the data storage format with this assumption.

I think it would be worth experimenting to get the analyzer to detect emphasized beats. But IMO this is the lowest priority work to do for the analyzer, so let's save that for after everything else is implemented and working well.

If we only show 1/4 notes on the waveform regardless of time signature, there is no purpose of storing the denominator of the time signature because we could double or half the number of beats to get the same result. But then we would have no indication that the track is double or half time.

**@crisclacerda**

It just clicked me, actually, we don't need the beat positions at all. If we assume that all beats are equidistant inside a measure, like we should, and have the measures boundaries we actually don't need to store beat positions.
By default, we can just assume they are quarter notes, if the user wants he can change that

On a 4/4 grid it relatively common to emphasize the first and the third beat for example.
The beat spectral difference used by the downbeat detector might be able to detect emphasized beats

**@hacksdump**

The beat grid for a track with 4/4 time signature and BPM = x will be visually the same as 4/8 time signature and BPM = x/2

Whether to mark emphasized beats within the bar:
If it is just meant to give a visual cue on emphasis, no, because our waveform should be adept enough to provide this kind of visual emphasis. If it is meant for auto DJ and looping, probably yes.

# UI mockups with data models

We'll defer phrases and sections for later revisions. We'll describe all possibilities with BPM and Time Signature here.

We'll be describing two types of data models.

1. We explicitly store every beat position.

Protobuf definition (pseudocode):

```
enum BeatType {
  BEAT
  DOWNBEAT
}

message Beat {
  double frame_position
  BeatType type [ default = BEAT ]
  TimeSignature signature
}

message Beats {
  Beat[] beats;
}
```

2. We store only the minimal sparse information and calculates the beats functionally (and cache the individual beats in memory at every update of the sparse data).

Protobuf definition (pseudocode):

```
message TimeSignatureMarker {
  int downBeatIndex
  TimeSignature signature
}

message BpmMarker {
  int downbeatIndex
  double bpm
}

message Beats {
  double firstBeatFramePosition
  int firstDownBeatIndex
  TimeSignatureMarker[] timeSignatureMarkers
  BpmMarker[] bpmMarkers
}
```

**What is a marker?**

A marker determines a beat grid value in the right direction until we encounter another marker.

This is how we calculate beatLength

`beatLength = 60 * sampleRate * (4 / timeSignatureDenominator)  / beatsPerMinute`

Let's start with a simple track (Sample rate = 100Hz). These tracks have constant BPM and only one time-signature.

To start with, let's say the analyzer recognized the track as:

Time Signature = 4/4

First Downbeat = First Beat

BPM = 60

It looks like this:

![4/4 60 BPM](https://i.imgur.com/OLLaSES.png)

Data Models for this scenario:

1. Absolute

Beats =>
```
{
beats: [
  {
    framePosition = 0
    type = DOWNBEAT
    timeSignature = 4/4
  },
  {
    framePosition = 100
    type = BEAT
    timeSignature = 4/4
  },
  {
    framePosition = 200
    type = BEAT
    timeSignature = 4/4
  },
  {
    framePosition = 300
    type = BEAT
    timeSignature = 4/4
  },
  {
    framePosition = 400
    type = DOWNBEAT
    timeSignature = 4/4
  },
  ... and so on till the end of the track
]
}
```

2. Sparse

Beats => 
```
{
  firstBeatFramePosition: 0
  firstDownBeatIndex: 0
  timeSignatureMarkers: [
    {
      downBeatIndex: 0
      timeSignature: 4/4
    }
  ]
  bpmMarkers: [
    {
      downBeatIndex: 0
      bpm: 60
    }
  ]
}
```

Now, the above track actually has BPM = 120 (it was created with audacity at 120 BPM). So the user might want to double the BPM. Let's see what this operation looks like in both data models.

![double the bpm](https://i.imgur.com/VKJXGbt.png)

1. Absolute
We need to insert new beats between the old beats.
New positions will be like:

[0, 50, 100, 150, 200]

Adjusting positions is easy but now we also need to check the beat type for each beat. An incoming beat can become a beat or a downbeat and old beats can also change their type.

Earlier:

D._._._.B._._._.B._._._.B._._._.D._._._.B._._._.B._._._.B._._._.D and so on

BPM x2:

D._.B._.B._.B._.D._.B._.B._.B._.D._.B._.B._.B._.D._.B._.B._.B._.D and so on

If we notice closely, some beats had to be converted to downbeats.

2. Sparse

Only need to change `bpmMarkers[0].bpm = 120`