# Creating a Sampler for Mixxx (GSoC 2010 Project)

  - Student: **Ryan Baker**
  - Mentor: **Albert Santoni**

### Abstract

For some people, myself included, mixing and DJ'ing is more than just
playing one track after the other at the same speed. For my project, I
will be writing a sampler for Mixxx that will allow users to play hits,
loops, vocals, and other samples on command. This will allow users to
add flair and creativity to their mixes. I believe this will be a major
addition to Mixxx and feel that it is a feature that many users will
appreciate.

### Sampler Specification

#### Summary and Rationale

##### Use Cases

  - DJ Bill wants to send a sample bank to his friend, DJ Jane. Being
    able to export sample banks will make it easy for Bill to share his
    sample banks with his friends.
  - DJ Ryan wants to add drum loops and one-shots into mixes. You should
    be able to control whether each sample is looped or only played once
    through.
  - DJ Adam wants to create on the fly remixes using vocal and
    instrument samples. You should be able to time-stretch the samples
    to fit the tempo of the song.
  - DJ Awesome wants to sample directly from a playing song and use this
    to create on the fly remixes and loops. You should be able to sample
    directly from a playing song.

##### Design

  - Feature ideas:
  - Simple playback (start/stop)
  - Looping
  - Time stretch / pitch adjustment

<!-- end list -->

``` 
    * How do we do tempo syncing?
* Waveform view
* Cue / Loop points (start/end)
* Saving / loading sample banks
* Sample bank management GUI (load/save/delete)
    * Reuse EngineBuffer for each sample in the bank
    * Are there any performance concerns about this?
    * Should we unify all the Reader threads?
* Sampling from playing decks
```

  - User Interface
  - How do we deal with skinning?
  - Simple/Minimal Controls

##### Work Breakdown
