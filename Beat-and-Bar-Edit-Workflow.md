# What are tempo, beat, bars and time signatures?
Tempo is the speed a passage is meant to be played. One important consequence from its definition is that it may not have been played or be perceived as it was supposed. Another one is that it's an abstract and relative concept. BPM is not the same as tempo.

A beat is a unit of length. The beats per minute is then one measurement of this speed, as distance over time. When we are counting the tempo our result is always relative to the window of beats we are counting. A beat can have different lengths or duration. This is the lower number of the time signature.

Semibreve - 1 |
Minims - 1/2 |
Crotchets - 1/4 |
Quavers - 1/8 |
Semi-Quavers - 1/16 |
Dime-Semi Quavers - 1/32 |

Using different note lengths can cause a different BPM values for the same tempo. 
It is not always possible to define a "correct" way of measuring the tempo in music; a piece of music in one tempo can be interpreted in different BPMs. Mathematically BPMs values of 240, 120, or 60 with the respective note lengths of 1/8, 1/4 and 1/2 would result in the exact same tempo.A piece in 3/4 can be easily rewritten in 3/8 simply by halving the length of the notes and doubling the BPM.
However, the interpretation of musicians and thus the perception of the listener will be different from those. It's usually considered that a piece with a lower BPM will be perceived as being more serene because a musician is usually more prone to applying legato on longer (faster) notes than on short (slower) notes. 

A measure is a restrict space in which the beats are placed. Since the beat length is defined in relative terms we need a regular space, of a certain duration to place them. Visually it's defined as bar lines that organize the notes on sheet music. The main purpose of the bar is to chop the music in equal lengths so that notes of different relatives beat lengths can balance each other and make melodies. 

The upper number of the time signature restrict how many beats are allowed inside each measure. This means that with the lower number of the time signature together with the BPM we determine the beat length. Once we have a established beat length we use the upper number of the time signature to determine the bar length. 

A 4/4 measure means that it fits 4 crotchets. On a 120 BPM it means that each beat will be 0.5 seconds long. And that we have 4, 0.5s long beats in a measure and thus a 2 seconds measure. The simplest possible melody is to play 4 crotchets of 0.5 seconds each. A different melody is to play 1 semibreve, or one note for the whole 2 seconds. Another more sophisticated can be play 4 1/8 notes (4 * 0.25 = 1) and 2 crochets (2 * 0.5 = 1) totaling 2 seconds. Music is also silence, so for every note, there is an equally sized rest. So another melody could be 1/2 rest (1 * 1 = 1) and then 16 dime-semi-quavers (16 * 0.0625 = 1) also totaling 2 seconds. We can put any combination of notes and rests inside a measure as long as we respect that their size must, in this case, be the same of 4 crotchets in 120 BPM or 2 seconds. 

On a 3/4 measure also in 120 BPM, our beats are also 0.5 long, but our measure now is only 1.5 seconds. A 7/8 signature means that our beat is now 0.25 seconds and a measure that fit 7 of these beats are so 1.75 seconds.

# Legacy architecture

## BeatGrid

The beatgrid is an offset measured in frames and tempo measured in BPM.
With this, we can unequivocally determine every beat position, and assign any arbitrary frame to a beat index.
It is a visual representation of metronome that has a start position and clicks on BPM that is displayed on the waveform.
It's also the metronome we use for sync

The beatgrid is very good for clicking on time on tracks that were made using a metronome, ie - drum machine.

### BeatGrid operations

Scale - multiply the bpm by an integer ratio. Multiplying a bpm value does not change the perception of tempo. Effectively this add or remove beats. Their position and lengths will be different but the relative distance will still the same. This reset the metronome to a different interpretation of the same tempo in the same instant.

Translate - Change the first beat offset. Effectively changes the position of every beat without changing it's length. This reset the metronome in the same tempo in a new instant.

Set BPM - Effectively changes the length of every beat and also the position of every beat but the first. This is a reset the to metronome in a new tempo in the same instant.

BPM around position - Control used for sync. It's always the same metronome.

Find the nearest beat - Used for quantizing when clicking on the waveform and also for cue and looping control. It's computed unequivocally from the first beat offset and the BPM. 

### BeatGrid limitations

Two problems affect even tracks made with drum machines: 
* [1] Abrupt changes - the record has a passage in a different tempo.
* [2] Accelerando or ritardando parts. Machines can even make tempo changes inside a measure level.

Tracks that are played by musicians share these problems and add theirs owns.
* [3] The band is unintentionally falling short or running ahead of the beat, but trying to catch up to the metronome.
* [4] The performers do not care about the metronome BPM. Tempo adds a lot of expressiveness to the music. In fact, a lot of musicians such the like of Beethoven would argue that the metronome is a silly thing. In traditional sheet music, for example, the tempo is defined very vague in words that encompassed a range of BPMs, the interpreters can freely speed up and slow down the passages inside this range to emphasize particular parts of the melody. This is what happens on symphony where the band is following a human conductor that might deviate from the tempo to add expressiveness rather than a fixed metronome. This also usually happens on rock and pop records where the chorus might be played in slightly faster to make it fell for euphoric.

## BeatMap

The beatmap is the series of all detected beats positions in frames.
It's a visual representation of every detect beat in the waveform.
It's the metronome that counts the tempo over 12 beats and is reset every beat for sync.

### BeatMap operations

Scale - multiply the bpm by an integer ratio. Multiplying a bpm value does not change the perception of tempo. Effectively this add or remove beats. This behave odd in beatmap, the global average bpm only is scaled to compute a new beat length that is used to created shift all beats?

Translate - Change all the beats offsets by the a fixed amount. Since the beats do not have the same length and distance in beatmap this effectively changes the position and the length of every beat. This creates a new the metronome for all beats in a new tempo and instant for sync. In the visual representation all beats are shifted.

BPM around position - Control used for sync. It computes the bpm on 12 beats centered in that position.

Find nearest beat - Used for quantazing when clicking on the waveform and also for cue and looping control. Computed either by the real detected beat or from the beat length computed from the bpm around position.

### BeatMap limitations

* [5] The noise of the analysis is not treated and the tempo value is always fluctuating.
* [6] We can not unequivocally determine any beat position or assign a frame to an arbitrary beat. We have the real distance to the next detected beat and we also have estimated distance from the computed bpm.

# New architecture

The new representation should not be a strict as beatgrid to not allow any tempo change. But it should also not be as loose as beatmap to allow any tempo deviation.

## What is the adaptive beatgrid?

A grid is usually defined as horizontal and perpendicular lines, uniformly spaced, used to help you find a particular thing or place, in a map, chart, or any other region by the means of a system of coordinates.

In Mixxx the grid is unidimensional structure of perpendicular uniformly spaced lines that are used to find a particular beat.
The system of coordinates it's use to unequivocally find any beat is a offset, used to determine it's start position, a BPM value and a time signature that are used to determine the length of our uniformly spaced lines. 

Unlike legacy beatgrid to support tempo changes, during the course of a single track we allow our grid to be described by a different set of coordinates at any arbitrary places. This means that although our grid is made of uniformly spaced perpendicular lines, this restricted, well defined space is allowed to change during track.

Mixxx will try to automatic align and describe the played beats by the longest grid (offset, bpm and time signature) that are in phase with the music. 

Having long sequences described by a single set of coordinates makes sync easy by stretching only that region to match the beats of another track.

If a track has a rhythm that Mixxx can not find any particular pattern the grid is defined by a different set of coordinates on every beat, this means that in this extreme case we still allow any beat to happen anywhere and have any length eventually regressing to the map representation rather than grid. On the other extreme case if a track has been made by drum machine and does not have any tempo change our adaptive grid is pretty much the same of the legacy beat grid.

With this we should be able to solve the problems outlined above by smart resetting - adapting - the coordinates and the offset we use to define the grid.

* [1] - This is trivial, we simply reset the metronome, ie -the grid, on any arbitrary offset with a new BPM.
* [2] - If the change happens on the measure level we reset the grid on the measure. If the tempo change happens inside a measure we reset the grid on a beat length. That means that inside that measure we are going to have beats described by a different set of coordinates, this means beats and bars will have different lengths and local tempo which adds complexity for syncing them.
* [3 and 4] - We look for the next longest sequence of beats that stays inside a tempo within a 25ms error and reset the grid for that offset, tempo and time signature. We try align these sequences so they represent a section, a phrase or at least a measure.
* [5 and 6] - We don't use the sequence of detected beats. We only use our grid coordinates to compute the position of any arbitrary beat.

### Adaptive grid operations

**These operations are used to define an adaptive region of our grid. These create, update and delete the "adaptive grid markers" that let Mixxx know when it should adapt it's grid (offset) and which coordinates (bpm, time signature) to use:**

Create a new grid region - Allows to set a new BPM and time signature in a any arbitrary position that becomes the first beat offset. By default this is also the first downbeat offset, the user/analyzer can easily change that by the set downbeat operation. The fact that this creates a beat on this arbitrary position implies that if this is not set on previously defined beat, we are not only setting the coordinates for the following region of our adaptive grid, but we are also changing the previously beat length, and thus changing the local tempo for that beat. This also implies that we have added a tempo change inside the previous measure and changed it's length as well. 

Create a grid for one measure - Allows to manually create an adaptive grid region of one bar, by defining a time signature together with the beats that define two consecutive downbeats. Mixxx will automatically determine the BPM of this region and the user can easily use the update operation to make this adaptive grid longer in any direction.

Update grid region boundaries - Allows to use an already defined "adaptive grid markers" to include more beats to the left or right, or to simply change the offset of the first beat, and thus all beat positions. To add beats to the left we change the current marker offset, to add beats to the right we change the next marker offset. If the new offset is not divisible by the beat length defined by the BPM, all beat positions change, otherwise we just add or remove new beats. (maybe split in two separate operations?)

Delete grid region - Allows to remove a segment of our adaptive grid. Effectively makes the grid described by an earlier "adaptive grid markers" longer by using it to describe the following region as well. 

**These operations are used to edit the coordinates that are used to find beats and downbeats inside the boundaries of one adaptive grid region without changing the region itself - ie: the BPM, time signature and the first downbeat offset measured in beats:**

Scale - multiply the BPM by an integer ratio, this does not change the tempo though, as we changed to a new equivalent BPM. Effectively this add or remove beats in a fixed ratio. This will change their positions and length but some beats will fall perfectly in the place previously occupied by another beat. This means that our downbeat positions (measured in frames by the beat our index point) and indices (which beats are downbeats) will be changed. If the scale ratio is not divisible by the numerator in the time signature this might add "ghost" downbeats in this region. 

Set BPM - This is used for small corrections of the BPM value. Effectively changes the position of every beat but the first.

Set time signature - A change in the numerator only will change which the beats that are the downbeats, without changing the beat positions. A change in the denominator only will change all (but the first) beat positions and thus the downbeats positions as well, while keeping the same beats as downbeats. Changing both will change both. Effectively changes the length of every measure (upper number) and the beat length (lower number).

Set downbeat - Shift all downbeat positions in this part of grid. Effectively this changes which beats are downbeat without changing their positions.

**The operations are used by other features of Mixxx:**

BPM at position - Returns the BPM that describes the grid that our beat is currently in.

Find nearest beat - Find the closest beat position using the grid coordinates - bpm, time signature and offset, that describes the region we are looking for that beat.

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
### Controversial Topics

* Showing every denominator as beat vs. showing real beats. 
  * In odd time signatures the emphasized beats are marked as beats. The denominator can be increased to make up a finer grid to palace a beat more exactly.  
  * What beats are shown on the waveform and used for quantizing is determined by the bottom number of the time signature. This creates a visual indication that an 8/8 section is the double time of a 4/4 section but still the same tempo because Mixxx will calculate tempo as 1/4 notes per minute. In an x/8 track, all the 1/8 notes in that bar will be shown on the waveform which is useful as a visual indicator that one bar is different from the ones around it.
* A measure is always constant vs changing speed within a measure. 
* Individual beats off the denominator grid vs all beats are on the grid.
  * This assumption will be used to help the analyzer produce useful results. The surrounding code asserts the assumption. 
  * This assumption will be used to help the analyzer produce useful results. However, the protocol buffer format for data storage will not assume this. Every individual beat will be stored in the protobuf. 
* forward and backward compatible representation
* sparse representation  

 
### Ideas and Opinions

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

## UI mockups with data models

We'll defer phrases and sections for later revisions. We'll describe all possibilities with BPM and Time Signature here.

We'll be describing two types of data models.

1. We explicitly store every beat position. BPM is calculated as `60 * sampleRate * (4 / timeSignatureDenominator) * distancBetweenBars`

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

Problem: How to accurately mark beat positions of bars with accelerating or decelerating tempo?

**What is a marker?**

A marker determines a beat grid value in the right direction until we encounter another marker.

This is how we calculate beatLength

`beatLength = 60 * sampleRate * (4 / timeSignatureDenominator) / beatsPerMinute`

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

`D._._._.B._._._.B._._._.B._._._.D._._._.B._._._.B` and so on

BPM x2:

`D._.B._.B._.B._.D._.B._.B._.B._.D._.B._.B._.B._.D` and so on

If we notice closely, some beats had to be converted to downbeats.

2. Sparse

Only need to change `bpmMarkers[0].bpm = 120`

As a next step, let's change the time signature to 3/4

![change signature](https://i.imgur.com/nFQ2kQt.png)

1. Absolute

No change in beat positions.

Change in beat types is needed.

Earlier:

`D._.B._.B._.B._.D._.B._.B._.B._.D._.B._.B._.B._.D` and so on

After changing time signature to 3/4:

`D._.B._.B._.D._.B._.B._.D._.B._.B._.D._.B._.B._.D` and so on

2. Sparse

Only need to change `timeSignatureMarkers[0].signature = 3/4`