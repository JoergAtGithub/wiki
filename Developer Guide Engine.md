# Introduction to Mixxx's Engine

The mixing engine is the part of Mixxx that is in charge of resampling,
amplifying, clipping, and mixing the audio from decks and samplers into
a master and headphone output.

# The Callback Thread

Hundreds of times per second, the operating system's audio API requests
a certain number of audio samples from Mixxx. This request is delivered
to the `SoundManager` class via an operating system callback (see
[SoundManager (OS audio interface)](developer_guide_soundmanager)).
`SoundManager` in turn requests that Mixxx's engine produce and mix
together the next buffer of audio.

The operating system callback requesting samples from Mixxx is running
in what we call the callback thread. This is usually a realtime thread
and is performance sensitive. Doing any kind of I/O or locking of
mutexes in this thread is highly discouraged. Anything that can block
the callback thread is in danger of causing user-audible skips in the
output audio.

# The Callback Buffer

The goal of the callback thread is to fulfill the operating system's
request for the next buffer of audio to play out the computer's
speakers. The length of this buffer depends on the latency and
samplerate settings the user has configured their soundcard at
(configurable in the Mixxx Sound Hardware preferences).

At a latency of `X` milliseconds and a samplerate of `Y` samples per
second per channel, and stereo channels the number of samples that Mixxx
must generate to fill the buffer is given by this simple relationship:

``` c++
double latency = 0.001; // 1 millisecond
int sampleRate = 44100; // 44.1 thousand samples per second (kHz)
int numChannels = 2; // stereo, 2 channels 
int samples_per_buffer = sampleRate * latency * numChannels;
```

At a latency of 1 millisecond, the operating system will request buffers
of audio every 1 millisecond or 1000 times per second.

# EngineObject

Almost all mixing components in the engine follow the EngineObject
interface. This interface is very simple:

    typedef float CSAMPLE;
    class EngineObject : public QObject {                                                                                                                       
        Q_OBJECT                                                                                                                                                
      public:                                                                                                                                                     
        EngineObject();                                                                                                                                         
        virtual ~EngineObject();                                                                                                                                
        virtual void process(const CSAMPLE *pIn, const CSAMPLE *pOut, const int iLen) = 0;                                                                                                                                                                                                   
    };

As you can see, this interface contains only one interesting method,
`process`. `process` takes a buffer of `CSAMPLE` values as input and a
buffer of `CSAMPLE` values to output, and a number of samples `iLen`.
The `EngineObject` processes the input audio in `pIn`, doing whatever
work it is that it is designed to, and writes the resulting output to
`pOut`.

Almost all components of the mixing engine implement this interface. The
benefit is that the mixing engine is modular and you can mix and match
different mixing components together to get the desired chain of audio
processing hooked up.

NOTE: By convention if `pIn` and `pOut` are equal, it is required that
the `EngineObject` should do its work in-place.

# EngineMaster

`EngineMaster` is the master class that drives the entire mixing engine.
`SoundManager` calls `EngineMaster` directly to request that the next
buffer of audio be generated.

`EngineMaster`, like most engine classes, is an `EngineObject` and all
of its interesting work is done in its `process` method.
