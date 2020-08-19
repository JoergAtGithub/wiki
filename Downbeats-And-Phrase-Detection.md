# Rhythm Detector

**Student:** Cristiano Lacerda (cristiano.lacerda@usp.br)  
**Mentor:** Daniel Schürmann  
**Related Project:**
[measures\_downbeats\_bars\_and\_phrases](measures_downbeats_bars_and_phrases)  

## Summary

**Status:** Working on it (If you have any thoughts on this please join the
discussion on
[Zulip](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/Rhythm.20Detector))

# What is rhythm?

In daily life "rhythm" is used to refer to patterns of temporal distributions of events. More strictly in music, rhythm refers to the explicit division of time into recurrent and periodic intervals of space.

Rhythm are together with melody and harmony the most prominent characteristics of music, but the rhythm is by far the one that offers the biggest incentive and easiest way to interact physically with the music and play the biggest role when mixing tracks together.

# What defines the perception of the rhythm

![RhythmElements](https://user-images.githubusercontent.com/61819301/90592196-5e924680-e1bb-11ea-9ddc-54188f89fee4.png)

# What are tempo and beat?

Tempo is the speed a passage of music is meant to be played. It's an abstract and relative concept. A beat is a unit of length, it's the smallest unit that we perceive rhythm, ie: a regular pattern of change, of a music record. The beat is what one would intuitively tap the foot or nod the head. 

Beats per minute is then a empirical measurement of this speed, as distance (beats) over time (minutes). When we are counting the BPM our result is always relative to the window of beats we are counting and to the relative length of the beat, determined by the denominator in a time signature. 

Semibreve - 1 |
Minims - 1/2 |
Crotchets - 1/4 |
Quavers - 1/8 |
Semi-Quavers - 1/16 |
Dime-Semi Quavers - 1/32 |

Using different note lengths can cause a different BPM values for the same tempo. 
It is not always possible to define a "correct" way of measuring the tempo in music; a piece of music in one tempo can be interpreted in different BPMs. Mathematically BPMs values of 240, 120, or 60 with the respective note lengths of 1/8, 1/4 and 1/2 will result in the exact same tempo. A piece in 3/4 can be easily rewritten in 3/8 simply by halving the length of the notes and doubling the BPM.
However, the interpretation of musicians and thus the perception of the listener can be different. It's usually considered that a piece with a lower BPM will be perceived as being more serene because a musician is usually more prone to applying legato on longer (faster) notes than on short (slower) notes. 

Using different windows to count the beats can also cause the different BPM values for the same tempo. Let's consider that we have counted 12 beats over the course of 6 seconds. To get the BPM we use the formula: (12 * 60) / 6 = 120 BPM. Now let's suppose we use 6 beats to count the tempo in this same 12 beats window but in two discrete steps. We count the first 6 beats on 2 seconds: (6 * 60) / 2 = 180 BPM. The other group of 6 beats take us another 4 seconds to count: (6 * 60) / 4 = 90 BPM. If we try to simply compute the arithmetic mean our BPMs, we got (90 + 180) / 2 = 135. This would be the same of one single window of 6 beats, that skip the first 2 beats and the last 4 beats, in this case we count the first 4 beats in 1.33 seconds and take an additional 1.33 seconds to count the next 2 beats, this gives us: (6 * 60) / 2.66... = 135. Since BPM is a speed measure, if we want to know the total distance we traveled we need to use the harmonic mean: 2/((1/90) + (1/180)) = 120 BPM, which was the original tempo we counted our 12 beats.

What is the true tempo of this passage? One could argue that it is 120 BPM, but that certainly is misleading because it does not consider that there is a tempo change in this region. To avoid missing any tempo changes one could consider only counting the tempo on a 2 beat window, but that can be even more misleading since small tempo deviations will be very prominent. It's impossible to expect that a musician, no matter how proficient in his instrument will always hit a note with perfect timing, but it's reasonable to expect that on average he will. Even if the track was recorded with a drum machine, there is also swing, which is making some notes shorter or longer on purpose, and many other articulations that a composer (written) and a performer (improvised) can throw that changes the length and/or the start and end positions of single notes, this will create a momentary perception of change in the played speed, even when the tempo has remained constant. 

There is no definitive or correct answer for that question. Indeed, this detail alone adds an enormous amount of complexity to the problem of beat tracking and tempo estimation. When computationally analyzing or critically listening to an audio record, all that can be used to determine the beat potions are the instants that the notes are being hit, this can create only a perception of the playing speed. However, what is of interest in most cases is the hidden "ground truth" as annotated on a sheet music or represented in digital symbolic file. The beat does not exists in the physical world, ie: air vibrations, perceived as sound. In western notation such articulations that change the perception of speed are tightly standardized, but nothing forbidden a composer or performer to invent a new one if he wishes. Computer musicians also have unlimited freedom to create on their DAWs any kind of articulations. For this reason, even extraordinarily trained individuals like professional drummers and conductors, whose have the responsibility of indicating the beat positions, for a band or an orchestra, will not always agree on "correct" beat position or "local" tempo value for an recorded music.

# The problem of automatic tempo detection and beat tracking

Since we can not always define what is the true local tempo, the performance evaluation of beat tracking algorithms is a research problem on it's own, with several metrics proposed and used simultaneously at MIREX for example. The implementations are then tuned to achieve the highest score in some or all of these metrics, but for our use case of beat matching music together these metrics are not very useful.

For the purpose of mixing tracks together, we need to turn tempo detection into an optimization problem: the correct BPM is the one which leads for the longest sequence of detected beats to be in phase while two adjacent BPM values have the smaller possible difference. The longest sequence serves the purpose of allowing smooth(long) transitions and the smallest BPM difference allows the warping of the audio to sound unnoticeable.

# What are bars and time signatures?

The bottom number of the time signature is the relative beat length. As a speed with beat units, the BPM is used it to determine the distance of two beats, ie: their lengths; or their duration, in an absolute unit: seconds, or milliseconds. The upper number of the time signature is called the beats per bar. As the name suggests it defines how many beats should be inside each measure. After we know the absolute beat length of the beat we can simply multiple that by the beats per bar, to determine the bar length. The main purpose of the time signature is to define the length of beats and bars, in relative terms, and with the BPM in a absolute unit of time.

A measure is the restrict space in which the beats are placed. Since the beat length is defined as a relative fractions, we need a regular space, of a certain duration to place them. That's the bar or measure. Visually, it's defined as bar lines that organize the notes on sheet music. The main purpose of the bar is to chop the music in equal lengths so that notes of different fractional duration can balance each other to make melodies. 

A 4/4 measure means that it fits 4 crotchets. At a 120 BPM it means that each beat will be 0.5 seconds long. And that we have 4, 0.5s long beats in a bar, and thus a 2 seconds measure. The simplest possible melody is to play 4 crotchets of 0.5 seconds each. A different melody is to play 1 semibreve, or one note for the whole 2 seconds. Another more sophisticated melody can be played as 2 1/8 notes (2 * 0.25 = 0.5) and 1 crochets (1 * 0.5 = 0.5) and one minim (1 * 1 = 1), all totaling 2 seconds. Music is also silence, so for every note, there is an equally sized rest. So another melody could be a 1/2 rest (1 * 1 = 1) and then 16 dime-semi-quavers (16 * 0.0625 = 1) also totaling 2 seconds. We can put any combination of notes and rests inside a measure as long as we respect the size defined by the time signature, in this case, that is the same of 4 crotchets that at 120 BPM means 2 seconds. 

On a 3/4 measure also in 120 BPM, our beats are still 0.5 seconds long, but our measure is only 1.5 seconds. A 7/8 signature also at 120 BPM means that our beat is 0.25 seconds and that the measure allows 7 of these inside, and thus are 1.75 seconds.

# The problem of automatic time signature and bar detection

The time signature is used to describe the meter of the music, or the metrical hierarchy in which the music is divided. The problem is that a time signature does not uniquely describe a metrical structure.
A 12/8 signature means that there are 4 beats that are further divided into 3 beats. A 9/8 signature means that there are 3 beats that are then further divided into 3 beats. Since the time signature does not define how the beats are subdivided, this means that we can write the exact same music as 4 measures of 9/8 or one single measure in 12/8 with a third of the BPM.
Extracting a time signature from audio is then not only a structural problem but also a semantic one. 

# The meter of the music

In music time is divided into temporal units. The beat also called the "tactus" is the most prominent one, but it is not the only. We have already saw that the measure is a higher level in which the beats are grouped. Lower than the beat there is the "tatum" which is the shortest unit, described by the shortest note used in the music, the tatums are grouped to form the beats. The BPM is nothing more than the pulse rate of the beat, but all metrical levels have a pulse rate. 
More importantly is that the perception of rhythm is created by the grouping of the beats into strong and weak units. This hierarchical and layered structure called meter defines how this grouping occurs.

# Simple, compound; duple, triple and quadruple meters

A duple meter is made of 2 beats, similarly a triple meter of 3 beats, quadruple meter of 4 beats and so on.

In a simple meter the beats are divided into groups of 2, in a compound meter the beats are divided into groups of 3.
The meter implies our strong beats. In a duple meter every 2 beats is accented, in a compound meter every 3. Also every first beat of the meter is made even stronger (ie: downbeat), So on a simple quadruple meter, the first of every 4 beats is the (**S**)strongest, but the third beat is also (s)strong while the 2 and 4 are (w)weak. There is a strong correlation between the time signature and the meter but it's not always possible to unequivocally map one to another.

A simple duple meter is traditionally written as 2/4. 1 group of 2 quarters. (**S**,w|**S**,w)

A simple triple meter is traditionally written as 3/4. 1/2 group of 2 quarters. (**S**,w,s|**S**,w,s)

A simple quadruple meter is traditionally written as 4/4. 2 groups of 2 quarters. (**S**,w,s,w|**S**,w,s,w) 

These are the only meters that can be simple. Although the quarter note is usually used to describe simple meters this can be any note length.

Next, are the compound meters, which are usually written in eight note length, but again this can be any note.

A 6/8 time signature, has 6 eight notes, which could be the same as a 3/4. But these are actually different organization of beats. The 3/4 time signature is reserved for grouping 3 beats that can be divided into 2 eights each, while the 6/8 represents 2 groups of 3 eight beats. (**S**,w,w,s,w,w|)

A 9/8 signature is a compound triple. 3 groups of 3 eights notes (**S**,w,w,s,w,w,s,w,w|)

A 12/8 time signature is a compound quadruple. 4 groups of 3 eights notes (**S**,w,w,s,w,w,s,w,w,s,w,w|)


# Odd and (n)tuples meters

In a odd meter the beats are divided into compound and simple divisions that can happen in any order. The most common are the quintuple and septuple meters.

A 5/n time signature means the beats can be divided into 1 compound and 1 simple division. (**S**,w,s,w,w|)(**S**,w,w,s,w|) are both valid quintuple meters for example.

A 7/n time signature means that there are 2 simple and 1 compound division. (**S**,w,s,w,s,w,w|)(**S**,w,w,s,w,s,w|)(**S**,w,s,w,w,s,w|)

Despite the name a (even-n)tuple can also be an odd meter, that's why they are also called complex meters.
A 8/n time signature for example means 2 compound and 1 simple division.
A 10/n time signature for example means 2 compound and 2 simple division. 

A complex meter can be made with any beats per bar that is not reserved for a simple or compound meter, with any beat length. 

A complex meter is also called an additive meter and in fact can be written as two consecutive bars with different time signature. A 7/8 bar for example can be the same as one 6/8 bar followed by a 4/4 bar.

# The problem of automatic meter detection

The metric structure of a music piece can be estimated by looking into the periodicity of the notes. The first step is then to compute the onset detection function. The second step is to transform the time representation of the onsets to the frequency domain. The most used transform are the discrete Fourier transform (DFT) and the auto correlation function (ACF). The result of this transformations have been called beat spectrum, rhythmgram or tempogram by different authors. In this representation it's easy to observe that the salient peaks relates to the pulse of the metric levels, but it's also easy to see that not all prominent peaks are related to these pulses, which is the first obstacle to retrieve the metrical information from the tempogram.

Some authors have proposed to multiple the tempogram obtained with the DFT with the one obtained from the ACF. Since the DFT adds harmonics at the integer multiples of the metric pulse rates while the ACF add sub-harmonics. So multiplying them pair-wise will result only in the peaks that appears on both tempograms which should better relate to the metric pulse rates.

The final step is picking the peaks of this new tempogram, since not all peaks relate to the metric structure, a musicology smart algorithm needs to be devised. The basic constrain is that each metric level pulse rate is a an integer ratio of the adjacent level. 

# The problem of the frequency transforms

The tempogram has proved to be a robust tool for finding the metrical level pulse rate but it's useless to find the phase of these pulses. We can determine for example that the beat rate is 120bpm and that the measure rate is 30bpm, but we can not possible determine where are the beats or the bar lines.

# Rhythm Analyzer Architecture

A high level data flow that overview of the rhythm analyzer interacts with Mixxx:

![Rhythm Analyzer](https://user-images.githubusercontent.com/61819301/90569473-536ff400-e184-11ea-9480-6adfc7d451c1.png)

A detailed data flow of the internals working of the rhythm analyzer:

![RhythmAnalyzerDataFlow](https://user-images.githubusercontent.com/61819301/90569626-96ca6280-e184-11ea-904e-0f67ba673e13.png)


# Final month schedule:

Week 1: Finish working on the tempo detection as an optimization problem - Improve phase correction algorithm so that two bpms adjacent bpm values are less than 5% apart. Finish working on removing arrhythmic regions - Use the onsets energy to detect regions that lack strong percussive sounds.

Week 2: Use freely available C++ tempogram implementation on the analyzer. Implement the proposed multiplication of ACF and DFT to improve it's robustness.

Week 3: Implement musically informed peek-picking algorithm to extract the metric level pulse rates.

Week 4: Use Chordino to output chord changes, try to align the measure pulse rate to chord changes.  

Meanwhile polish #2930 so it's ready to merge.
