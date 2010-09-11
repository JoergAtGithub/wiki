# OSC: Open Sound Control

OSC is an open protocol slated to replace MIDI.

## Summary and Rationale

Add support for OSC. This should allow next generation programs and
Monome controllers to work with Mixxx.

## Use Cases

  - DJ Bill has a Monome Ohm and he wants to Mixxx\!
  - Madjester just downloaded TouchOSC and he'd think it'd be k-rad to
    make his own TouchOSC mapping for Mixxx.
  - DJ SuperProgrammer decides he wants to hook up Mixxx with Pure Data

## Design

OSC works by connecting to URLs. The standard is that conforming
machines will send OSC messages to the URLs and the format that the
server excepts. I base this assumption on
<http://www.linuxjournal.com/content/introduction-osc>.

As such we could use this simple format:

/\[Group\]/\[Key\]

We of course would expect the typical floating point values or integer
values.

Therefore an example of many of our controls as OSC URLs:

  - /Channel1/play
  - /Channel1/rate
  - /Channel1/rate\_temp\_up

etc...

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - **YOU**
  - Phillip Whelan (Madjester)
