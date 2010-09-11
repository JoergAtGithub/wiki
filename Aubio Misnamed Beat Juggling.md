## Summary

**Status**: There is a branch which has most of these features
implemented. Testing is still needed.

Mixxx has BPM detection but not beat detection. Beat detection would
allow us to do man cool tricks including:

  - Jump from beat to beat
  - Quantize Effects
  - Create Beat Quantized loops
  - Do full Automatic Beat Syncing
  - Beat Smashing/Splicing (ala Aphex Twin)

## Current Status

There is currently a branch at
<https://code.launchpad.net/~mixxxdevelopers/mixxx/features_beatjuggling>.

Currently it does:

  - Beat Analysis
  - Quantized loops
  - Jumping beats backwards and forwards (quantized and not...)
  - Rendering of the Beats on the Waveform

Tracked beats are now saved in the database as a column in library as a
loooooooong bitmap of integers.

## Design

Analyzed beats are stored in a TrackInfoBeats class. The class
declaration is the following:

    class TrackInfoBeats {
     public:
        TrackInfoBeats(TrackInfoObject *);
        ~TrackInfoBeats();
        
        void addBeatSeconds(double);
        
        double findNextBeatSeconds(double) const;
        double findPrevBeatSeconds(double) const;
        QList<double> findBeatsSeconds(double, double) const;
        
        int getBeatCount() const;
        int dumpBeats() const;
        
        void addBeatSample(int);
        int findPrevBeatSample(int) const;
        int findNextBeatSample(int) const;
        int findBeatOffsetSamples(int sample, int offset) const;
        QList<int> findBeatsSamples(int, int) const;
        
     private:
        /** Find the Samples Index */
        int sampleIndex(int) const;
        
        /** Sample Rate for this song */
        int m_iSampleRate;
        /** Sample count for this song */
        int m_iTrackSamples;
        /** Duration of the entire song in seconds */
        double m_dDuration;
        /** 10 second index (in samples) */
        QList<int> m_beatIndex;
        /** Map of all the beats in samples */
        QMap<int, int> m_beats;
    };

You can see it at:
<http://bazaar.launchpad.net/~mixxxdevelopers/mixxx/features_beatjuggling/annotate/head:/mixxx/src/trackinfobeats.h>

Each beat is mapped in m\_beats using the sample offset to point to
itself. m\_beatIndex works as a sparse index for the first beat sample
offset in a certain range.

This may not be the best way to implement this but in essence it was the
fastest way I thought of being able to do a lookup for a range of sample
offsets. The algorithm for a lookup is such:

  - Take your starting offset of interest and make them modulo to what
    is used to generate m\_beatIndex.
  - Get the matching sample offset from m\_beatIndex (it's a direct
    lookup).
  - Lookup the resulting offset in m\_beats (direct lookup again from
    our indirect index).
  - Forward track through m\_beats until you reach or exceed your end
    offset to get all desired sample offsets.

## Current Issues

  - ~~TrackInfoBeats is not stored in the Database~~ Implemented in the
    latest changes.
  - Analysis takes 90%+ CPU and around 15 seconds for a typical
    Psytrance Song (not good for live performance).
  - There is no fallback implementation to fill in TrackInfoBeats with
    SoundTouch.

## Notes

  - We could easily avoid the CPU and time penalty for analysis by only
    using aubio in the analysis section.
  - Although the implementation so far deals with beat detection and
    quantization aubio also does other forms of analysis.
  - We could color waveforms on peaks (onset detection)
  - We could color waveforms according to pitch (pitch detection)
