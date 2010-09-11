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

/Control/\[Group\]/\[Key\]

We of course would expect the typical floating point values or integer
values.

Therefore an example of many of our controls as OSC URLs:

  - /Channel1/play
  - /Channel1/rate
  - /Channel1/rate\_temp\_up

We prepend Control in the path so we can separate it from other possible
entry points, ie: a direct to MIDI Script connection. This MIDI Script
connection would look something like:

/Script/\[Channel\]/

That's all I got for that. The problems here are many:

  - MIDI Script has no global state
  - You can have duplicate machines hooked up

One way around them would be to include the name of the device's
instance itself in the path but that could be quite brittle. I'm sure
Sean can provide some insight here.

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - **YOU**
  - Phillip Whelan (Madjester)
