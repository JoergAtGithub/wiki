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
