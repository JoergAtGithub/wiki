# Profiling

Profiling is a method for analyzing the performance characteristics of a
program. There are a variety of types of profilers out there
(instrumentation, statistical, emulation, etc.).

## Statistical Profilers

Statistical profilers work by using operating system provided hooks to
stop the program being profiled at a fixed sampling interval (typically
1ms or shorter). Every time the program is stopped the profiler takes a
backtrace of every thread. This gives the profiler a snapshot of what
the program was doing at that instant. The profiler tabulates the number
of times a given piece of code appears in a sample to give you an
estimate of how "expensive" a function is in relation to the rest of the
tasks the program is performing.

### What can statistical profiling tell you?

  - The number of times the program counter was on a given line of code
    during a sample.
  - The relative CPU burden of different tasks a program performs by
    comparing the number of samples that fall within two execution
    paths.
  - The various code paths taken by a particular execution tree in your
    program. (i.e. -- "Hey I didn't realize this code somehow called
    QVector::expensiveCopy\!"). 
  - Usually a profiler can connect the source code with the assembly 

### What can't statistical profiling tell you?

  - How expensive a function is in absolute terms (i.e. how long a
    function takes to complete, statistics about methods that Mixxx's
    performance timers might provide, etc.).
  - The full set of functions that are called by another function (if
    they don't appear in a sample then they will appear to not exist to
    the profiler).

## Tools

### GProf (Linux, BSD, Mac OS X)

### LTTNG (Linux only)

### XCode / Instruments (Mac OS X only)

### Valgrind

### Callgrind / KCacheGrind

### Mutrace
