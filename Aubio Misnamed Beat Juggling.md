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

### Current Status

There is currently a branch at
<https://code.launchpad.net/~mixxxdevelopers/mixxx/features_beatjuggling>.

Currently it does:

  - Beat Analysis
  - Quantized loops
  - Jumping beats backwards and forwards (quantized and not...)
  - Rendering of the Beats on the Waveform

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

### Current Issues

  - TrackInfoBeats is not stored in the Database
  - Analysis takes 90%+ CPU and around 15 seconds for a typical
    Psytrance Song (not good for live performance)
  - There is no fallback implementatio to fill in TrackInfoBeats with
    SoundTouch
