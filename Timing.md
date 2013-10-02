\*\* FIXME -\> This page is under construction \<- FIXME\*\*

# Timing

This page is a collection of all timing topics inside Mixxx

## Hardware Time Sources

In Mixxx we have to deal at least with fife independent hardware time
sources:

``` 
 1. BIOS wallclock (Real time clock)
 2. CPU clock 
 3. Sound interface DAC clock 
 4. Display clock 
 5. Midi Sample rate 
 
```

Unfortunately all these clock have there own precise and are not synced.

## Intervals in Mixxx

``` 
 1. Audio interval, set by the audio buffer size ~ 1 ... 100 ms  
 2. Display refresh rate, usually 16.66 ms 
 3. Mouse sample rate, for waveform scratch usually 8 ms 
 4. Midi polling, Sample rate ? 
 
```

In Mixxx the Audio interval is the leading interval. All other intervals
must be synced with the audi interval for a perfect result. If this is
not possible, We may interpolate the used values tor reduce the jitter
due to the use of possible outdated values. For good results we need a
timestamps for these values.

## Engine Clock

The Mixxx sound engine runs at the 3. Sound interface DAC clock.

Depending on underlying sound driver architecture, Port Audio calls a
Mixxx callback for every sound buffer. ...

One call of the Audio Callback processes one Buffer at once. Control
changes are only adopted between each callback. Controls that changes
with a higher rate then the audio buffer size are lost.

## GUI Refesh

The Waveform display must be refreshed with the display refresh rate,
but the data to display are calculated with the audio update rate.

## Low latency

The control "Latency" is the time from a control command at the until
the change can be heard from the speakers. Only a middle part is
produced by Mixxx.

For best results all controls should be sampled one time within each
audio interval.
