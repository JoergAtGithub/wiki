# Crash Recovery For Mixxx (GSoC 2008 project)

  - Student: **Zack Elko**
  - Mentor: **Adam Davison**

### Abstract

An application such as Mixxx which I consider to be mission critical in
a lot of contexts, should never crash. But, this is software, and things
do happen. In that event, the application must be able to recover
gracefully from such an event. My initial thoughts of how to address
this issue would be to keep track of the current state of the Mixxx
session at consistent intervals so that the session could be restored
quickly upon restart after a crash. The effect would be similar to what
happens in Mozilla Firefox when the browser is exited abnormally. Of
course, Mixxx is a bit different than a web browser. Those experiencing
the music produced by a DJ using Mixxx will have had their experience
interrupted very abruptly, and to simply go from loud music to silence,
and back to loud music isn't exactly ideal (or safe). This is an area
that will require a lot of testing and tweaking to get right, but it's
one of the most important areas of the crash recovery.
