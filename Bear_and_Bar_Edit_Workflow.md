# Bear and Bar Edit Workflow

this page is intended to discuss a smooth workflow when editing betas and bars. It shall also fix requirements and point out limitations of the chooses model.  

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






       


