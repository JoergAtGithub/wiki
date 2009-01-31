# Performance improvements

Here we enumerate all of the areas where Mixxx can be optimized, roughly
in order of importance. The more things we can complete on this list,
the more machines Mixxx can run on, and the larger our user base.

## CPU

(Anything found that wastes CPU time should be listed here)

  - Line 881 in enginebuffer.cpp process() fires
    <span class="underline">continuously</span> while Mixxx is idle:

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

## Memory

(Anything that wastes memory by inefficient storage (where unnecessary)
or leaks goes here)

  - Currently loading four copies of MP3 files into memory
  - Vinyl control leaks part of the lookup table, or something like that
    when it gets deleted/recreated \~\~\~\~
