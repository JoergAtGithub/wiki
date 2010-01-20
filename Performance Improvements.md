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

  - <https://bugs.launchpad.net/mixxx/1.7/+bug/410841>
  - Currently loading ~~four~~ two copies of MP3 files into memory.
    (r2509 in 1.7 removes the second copy as soon as the Analyser is
    done with it, plugging a big leak.)
  - ~~Vinyl control leaks part of the lookup table, or something like
    that when it gets deleted/recreated~~
  - SoundSource's should use memory mapped IO. Making that cross
    platform is tricky.
