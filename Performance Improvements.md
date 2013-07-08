# Performance improvements

Here we enumerate all of the areas where Mixxx can be optimized, roughly
in order of importance. The more things we can complete on this list,
the more machines Mixxx can run on, and the larger our user base.

## Thread scheduling

The most important thread is the audio callback thread. If this misses
its deadline (the latency period,) pops and clicks can be heard in the
output. As a result, it needs real-time priority, preferably with a hard
deadline matching the latency period. (And we need to make sure it runs
as succinctly and efficiently as possible so it can complete its work
within the latency period (which can ideally be as low as 1ms.) Taking
any longer would be shooting itself in the foot.)

Note that there are currently many places the callback thread does or
can call QMutex::lock(), which \*will\* block until the mutex becomes
free for locking. This cannot happen in the callback thread, it almost
guarantees a missed deadline (and consequently an underrun) at some
point in the future, even if the triggering conditions are quite rare
(but with threads, anything is possible). Here's a list (add if you find
another, I'll add the callstacks when I'm more awake):

  - CachingReader::m\_readerMutex
  - EngineBuffer::m\_engineLock
  - EngineSidechain::m\_waitLock
  - EngineWorkerScheduler::m\_mutex

Any locking of mutexes done in the callback \_must\_ be done with
QMutex::tryLock(), which does not block if the mutex is already locked.
Program logic will need to change accordingly.

**TO DO: Ensure the audio callback thread gets real-time priority when
run as a regular user.** - RJ discovered that Mixxx's requests for
real-time priority on this thread are having no effect. Running as a
regular user on Linux shows that the priority range is from 0 to 0, and
as root from 1 to 99, but it is set to 1 (the lowest) by default.
However, calling `setPriority(QThread::TimeCriticalPriority)` (while
running as root) does result in priority escalation.
*([xwax](http://www.xwax.co.uk/) has been able to solve this problem on
Linux. See the `rig_realtime` function in
[rig.c](http://github.com/yadler/xwax-yadler/blob/master/rig.c).)*

## Thread consolidation

First, [are threads
evil?](http://www.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.pdf)
The gist is that concurrent events that threads cause are wildly
unpredictable and are therefore extremely difficult to work with even in
simple cases since there are an exponential number of possible race
conditions. The paper suggests alternative proven methods that would
work better and are easier to work *with* especially in a user-facing
application like Mixxx.

Next, [read this Qt blog
post](http://blog.qt.digia.com/blog/2010/06/17/youre-doing-it-wrong/)
regarding proper use of QThread. (It's my impression that we are in fact
doing what he says not to do which is the reason for all the threads we
have.)

This [Qt wiki post](http://qt-project.org/wiki/Threads_Events_QObjects)
contains detailed information about threading in Qt.

Mixxx's current [thread list](threads).

As Mixxx's functionality grows and it's extended to work with arbitrary
numbers of resources, we need to consolidate the work to handle each
resource into a single thread. This currently needs to be done for:

  - **MIDI Device** - currently one thread per attached controller, need
    one thread to handle all MidiDevices (the MidiDeviceManager would be
    a good place to put it.)
  - **MIDI Script Engine** - currently one thread per attached
    controller, need one thread with *n* ScriptEngines in it
  - **(Caching)Reader** - currently one thread per deck, need one thread
    with *n* Readers in it
  - **VinylControl** - currently one thread per deck, need one thread
    with *n* timecode-decoders in it

### Sean's ideas:

Stepping back for a moment, what are the goals we're trying to reach? As
I see it, we want anything user-facing to respond in a hard-limited
amount of time. This includes:

  - Audio output
  - GUI
  - MIDI I/O

Of course audio needs to be processed as fast as possible, but that
varies based on the user's machine capabilities, so we have the latency
slider. So the audio needs to "refresh" within the latency period. I
suggest that 30fps is an acceptable refresh rate for anything visual
(GUI and MIDI output,) which translates to 33.3 (repeating)
milliseconds. We could have a "visual latency" slider denoted in fps as
well to help under-powered machines. Then we'd have a process() function
for each of these user-facing items that did nothing more than the bare
minimum to update their respective areas from a current snapshot of
MixxxControls. (E.g. the Audio::process() would do the real-time
processing (FX, EQ, etc.) of the current latency buffer, GUI::process()
would simply repaint the display, and MIDI::process() would send queued
messages to and receive queued messages from the controller(s).) These
must finish before the applicable latency period. If they can't, they
must defer additional work (or just abort in the case of audio) until
the next period. (And the user will want to adjust the slider up at that
point.)

So I suggest two user-facing threads: an audio one at real-time priority
and a GUI+MIDI update one (Qt's main thread) at high or normal priority.
Each would set up a timer to fire every applicable latency period that
simply called the respective process() functions. (It would be
interesting to automatically adjust the sliders up (if the user chooses)
if anything times out, i.e. another timer event arrives before process()
has returned.)

Then have a single additional thread at normal (if GUI+MIDI is high) or
lower-than-normal priority for everything else (where the MixxxControls
are actually updated,) but here too each sub-system needs a process()
function that returns as quick as it can. This means any long
CPU-hogging operations (like track analysis, DB and file I/O, script
engines) must be split into time slices.

## CPU

(Anything found that wastes CPU time should be listed here)

  - ~~Line 881 in enginebuffer.cpp process() fires
    <span class="underline">continuously</span> while Mixxx is idle:~~
    fixed by rryan

<!-- end list -->

    // Stopped. Wheel, jog and scratch controller all scrub through audio.
    rate=(wheel->get()*40.+m_pControlScratch->get()+m_jogfilter->filter(m_pJog->get()))*baserate; //*10.;
    m_pJog->set(0.);

  - Line 43 in controlobjectthreadmain.cpp eventFilter() also fires
    incessantly while idle:

<!-- end list -->

    emit(valueChanged(ce->value()));

  - Line 96 in controlpotmeter.cpp setValueFromThread() also fires very
    often while idle:

<!-- end list -->

    emit(valueChanged(m_dValue));

  - Line 107 in controlpotmeter.cpp setValueFromEngine() also fires very
    often while idle:

<!-- end list -->

    emit(valueChangedFromEngine(m_dValue));

  - EQ code takes up 50% of our current CPU usage on a Pentium 4 (with
    static EQs\! HQ eqs are even slower...)

### Time-critical code

*(Please list all time-critical code sections/functions here to be
considered for assembly language reimplementation.)*

  - EQ code - SSE-enhanced implementation is in progress in the
    [features\_hydra
    branch](https://code.launchpad.net/~mixxxdevelopers/mixxx/features_hydra)
    (unfortunately it wasn't given its own.)
  - EngineBufferScale: EngineBufferScaleLinear and EngineBufferScaleST -
    also see
    [features\_hydra](https://code.launchpad.net/~mixxxdevelopers/mixxx/features_hydra)
  - SoundDevicePortAudio - also ripe for SSE reimplementation

For reference:

  - [](http://www.agner.org/optimize/)
  - [Intel64 & IA-32
    manuals](http://developer.intel.com/products/processor/manuals/index.htm)
  - [AMD64
    manuals](http://support.amd.com/us/psearch/Pages/psearch.aspx?type=2.1&product=5.7&contentType=Tech+Doc+Processor&ostype=&keywords=&items=20)

## Memory

(Anything that wastes memory by inefficient storage (where unnecessary)
or leaks goes here)

  - ~~<https://bugs.launchpad.net/mixxx/1.7/+bug/410841>~~
  - Currently loading ~~four~~ two copies of MP3 files into memory.
    (r2509 in 1.7 removes the second copy as soon as the Analyser is
    done with it, plugging a big leak.)
  - ~~Vinyl control leaks part of the lookup table, or something like
    that when it gets deleted/recreated~~
  - SoundSource's should use memory mapped IO. Making that cross
    platform is tricky.
