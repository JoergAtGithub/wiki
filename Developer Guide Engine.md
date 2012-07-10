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
the callback thread is in danger of causing user-audible skips (called
*xruns* or *buffer under-runs*) in the output audio.

# The Callback Buffer

The goal of the callback thread is to fulfill the operating system's
request for the next buffer of audio to play out the computer's
speakers. The length of this buffer depends on the latency and
samplerate settings the user has configured their soundcard at
(configurable in the Mixxx Sound Hardware preferences).

At a latency of `X` milliseconds and a samplerate of `Y` samples per
second per channel, and stereo channels the number of samples that Mixxx
must generate to fill the buffer is given by this simple relationship:
`X * Y * 2`.

For example:

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

``` c++
typedef float CSAMPLE;
class EngineObject : public QObject {                                                                                                                       
    Q_OBJECT                                                                                                                                                
  public:                                                                                                                                                     
    EngineObject();                                                                                                                                         
    virtual ~EngineObject();                                                                                                                                
    virtual void process(const CSAMPLE *pIn, const CSAMPLE *pOut, const int iLen) = 0;                                                                                                                                                                                                   
};
```

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

## Mixing Channels

`EngineMaster` supports mixing multiple streams of audio together. To
add a channel of audio to `EngineMaster` you must create an
`EngineChannel` class that represents your channel of audio. For
example, decks use the `EngineDeck`, samplers use the `EngineSampler`
class, and microphones use the `EngineMicrophone` class. All 3 of these
are children of `EngineChannel`. To add a sampler or deck or microphone
to `EngineMaster` you call the `addChannel` method on `EngineMaster`.

As you will find in `mixxx.cpp`:

``` C++
EngineMicrophone* pMicrophone = new EngineMicrophone("[Microphone]"); 
m_pEngine->addChannel(pMicrophone);
```

This registers an `EngineMicrophone` class with the `EngineMaster`. When
mixing the master and headphone outputs, `EngineMaster` will query the
`EngineMicrophone` that is created for whether it is active, and if so,
ask it to `process` itself to generate audio. Once `EngineMicrophone`
generates audio, `EngineMaster` will mix that audio into the master
output.

# EngineChannel

`EngineChannel` is the interface that all audio channels must implement
to integrate with `EngineMaster`.

The following methods are used by `EngineMaster` to determine how to mix
the `EngineChannel`:

  - `isActive()` -- if this method returns true then the `EngineChannel`
    is asked to produce audio via its `process` method.
  - `isPFL()` -- if this method returns true then the result of the
    `process` call will be mixed into the engine PFL (pre-fader listen,
    headphone) output. 
  - `isMaster()` -- if this method returns true then the result of the
    `process` call will be mixed into the engine master output.
  - `getOrientation()` -- the return of this method determines what
    orientation this `EngineChannel` has. Orientations can be the
    left-side of the crossfader, the center (not affected by the
    crossfader), and right side of the crossfader.
