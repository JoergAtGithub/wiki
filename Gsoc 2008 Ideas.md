# Google Summer of Code 2008

[Google's Summer of Code](http://code.google.com/soc/) program provides
funding for students who'd like to contribute to open source projects.
Mixxx is a good project to work on because it gives you experience
working with cross-platform development as well as writing code that's
going to power live performances (ie. stability is key). Summer of Code
is a great opportunity to get involved in open source software, gain
valuable new experience and meet interesting people.

# Ideas

Here are some of our ideas. Under GSoC you can either apply to work on
one of these suggestions or you can come up with an idea of your own.
Also you may like the general outline of one of our ideas but would like
to put a different spin on it, we're happy to discuss all these things.

## Scalable Skins with SVG

Mixxx currently uses bitmap skins to allow users to change the look of
the application. However this ties each skin to a specific window size.
Being able to render skin elements using SVG would allow for not only a
higher level of graphical quality but would also allow skins to fit many
different screen sizes. A student would initially implement support for
rendering SVG graphics within the existing skin framework and would then
go on to implement support for changing the window size of Mixxx. This
project might also be a good opportunity for a more artistic student as
an optional add-on would be to design an SVG based skin to test all the
code changes thoroughly.

## Better Support for MIDI Devices

There are hundreds of different MIDI controllers in the world, all of
which have different buttons and knobs. Mixxx currently relies on XML
files which describe how to map MIDI events to user interface elements.
At the moment these have to be created by hand and allow only the most
basic types of mapping. Hardware support is a key aspect of Mixxx and
one which could benefit from more dedicated attention. A successful
student in this project would put themselves in an excellent position to
continue as a key member of the Mixxx development team after GSoC,
should they want to do so. We have two ideas which we think would
significantly improve support in Mixxx given below but we'd be happy to
discuss others:

### Support More Advanced Controllers

There are all sorts of interesting controllers out there with buttons
that return wierd ranges of values or that when you hold down make other
buttons do certain things. Generally to support these you end up having
to write some small piece of C++ that maps the output properly and then
activate that from the XML somehow. This is kind of silly and means that
if you aren't willing to compile your own version of Mixxx, it's often
hard to get some features of your controller supported. The solution
we're considering is to write a simple interpreter that parses commands
in the XML file to allow simple calculations to be performed in a highly
configurable way. This isn't as scary as it sounds and would be a really
interesting piece of code to write.

### Better Usability

Some people will never write an XML text file by hand to make their
controller work. It would be really nice to have some kind of GUI which
would allow even a preliminary version of an XML mapping to be produced.
This would be a highly user interface focussed project and would be
ideal for someone who enjoys this type of work.

## Mobile Device Support

A very nice addition to Mixxx would be to auto-detect when media
players, mobile phones and mass storage devices are connected to a
computer and allow access to this music immediately from within the
library view. Then next time you're DJing at a party and someone says,
'Do you have "The Obscure Guys - Ambient Experiment \#53 (Rare Techno
Remix)"?', you can say, 'Just plug in your iPod'.

Some thought for this project would need to be put into how to detect
media devices in a platform independant way. This is a very
self-contained task and would therefore be suitable even for someone
without too much experience working on large software projects.

## Stability

For live performances, Mixxx must never-ever die. Although Mixxx is
pretty good at the moment, there's room for a more serious approach to
stability than just fixing crashes as we find them. A student could for
example write a stress testing robot for Mixxx which helps weed out
memory links and crash bugs automatically. They could also explore
possibilities for recovering from crashes automatically and quickly.
There is presumably plenty of room for clever ideas here. We offered
this project last year and had to turn down some competent people in
favour of higher priority projects but this year we're offering it again
and would encourage people to reapply if they did so in the past.

## Something Crrrazy (Your Own Ideas\!)

Of course you might think all these ideas are stupid. Perhaps you played
with Mixxx for the first time and thought, "Damn these guys are really
missing X with bells on\!". Whatever your ideas are, no matter how crazy
(those are the most fun to read anyway :)), we'd like to hear them. So
go ahead and apply.

## Your idea here

(With thorough description)

  - Scalable Vector based UI
  - Use SVG graphics, scale them, copy the way KDE games do scaling.
  - MixxxCharts
  - Collect playback stats from willing users into a DB; generate chart
    web pages by Genre, Promo tracks, and New tracks

## Adam's (no longer) Mental Notes

Not all of these may still seem like good ideas for projects in the cold
light of day...

  - More detailed MIDI controller support
  - All this state machine transformations stuff done properly... will
    write this into a real project asap
  - Rewrite the waveform display\!
  - Get LADSPA stuff finished and into GUI, don't really want to offer
    effects again...
  - Make it easier to develop skins
  - Auto-testing, crash-proofing etc etc can come around again although
    we didn't accept anyone for it last time
  - Something to do with auto-learning midi controllers or creating
    configs through some fancy UI or something
  - Support for mobile devices, ipods and phones and mass storage in
    general
  - Sampler\!
  - Kittens\!

<!-- end list -->

    * 
    * ... out of ideas for now ...

# Have a better idea?

We're all ears\! Please outline your ideas in detail in your student
application to GSoC 2008, as per [Google's
outline](http://code.google.com/soc/2008/faqs.html#0.1_student_app).
