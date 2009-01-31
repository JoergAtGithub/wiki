# Performance improvements

Here we enumerate all of the areas where Mixxx can be optimized, roughly
in order of importance. The more things we can complete on this list,
the more machines Mixxx can run on, and the larger our user base.

## CPU

(Anything found that wastes CPU time should be listed here)

  - Line 881 in enginebuffer.cpp fires
    <span class="underline">continuously</span> while Mixxx is idle
  - Line 43 in controlobjectthreadmain.cpp also fires incessantly
  - Line 96 (or was it 107) in controlpotmeter.cpp also fires very often

## Memory

(Anything that wastes memory by inefficient storage (where unnecessary)
or leaks goes here)

  - Currently loading four copies of MP3 files into memory
