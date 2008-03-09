# Google Summer of Code 2008

[Google's Summer of Code](http://code.google.com/soc/) program provides
funding for students who'd like to contribute to open source projects.
It's a great opportunity to get involved in open source software, gain
valuable new experience and meet interesting people. Mixxx is a good
project to work on because it gives you experience working with
cross-platform development as well as writing code that's going to power
live performances (ie. stability is key). Also the interesting people
you'll meet will be us. And we're nice.

This page has our ideas and also some tips for applicants if we get
approved as an organisation (**Hi Leslie and GSoC team :)**)

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
different screen sizes.

A student would initially implement support for rendering SVG graphics
within the existing skin framework and would then go on to implement
support for changing the window size of Mixxx. This project might also
be a good opportunity for a more artistic student as an optional add-on
would be to design an SVG based skin to test all the code changes
thoroughly.

## Key Detection

Harmonic mixing is a technique many professional DJs use to give their
mixes an extra edge. By mixing between songs that have "compatible"
keys, a DJ can create interesting harmonies during their beatmixes. In
order for a DJ to do harmonic mixing, they generally rely on a separate
piece of software to calculate the key of the song. A project for a
prospective student is to explore algorithms for determining the key of
a song and implementing a suitable algorithm in Mixxx. Mixxx currently
performs tempo (BPM) detection on songs it loads and a student may wish
to review the BPM detection code before planning their implementation of
key detection.

## Better Support for MIDI Devices

There are hundreds of different MIDI controllers in the world, all of
which have different buttons and knobs. Mixxx currently relies on XML
files which describe how to map MIDI events to user interface elements.
At the moment these have to be created by hand and allow only the most
basic types of mapping. A successful student in this project would put
themselves in an excellent position to continue as a key member of the
Mixxx development team after GSoC, should they want to do so. *If you
want to work on this, we may be able to lend you MIDI hardware but
owning a MIDI controller would be an advantage*. We have two ideas which
we think would significantly improve support in Mixxx below but we're
happy to discuss others:

#### Support More Advanced Controllers

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

#### Better Usability

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

Of course, you might have an even cooler idea. Perhaps you played with
Mixxx for the first time and thought, "Damn these guys are really
missing X with bells on\!". Whatever your ideas are, no matter how wierd
and wonderful, we'd like to hear them. So go ahead and apply.

# Tips For Applying (PICK ME\!)

People often want to know what we're looking for in applications and
what they can do to get selected. Here are three tips.

1.  We aren't necessarily looking for experienced people. Show us that
    you're interested and motivated and we'll happily overlook gaps in
    your knowledge. Having said that, Mixxx is developed in a highly
    cross-platform way, using a lot of Qt. We also use PortAudio and
    scons. So if you know about these things it would probably be worth
    mentioning it :).
2.  Get some experience with Mixxx. If you know about Mixxx, even just
    as a user, then you'll be able to write a much better application.
    Even just downloading it and playing for half an hour will give you
    a sense of what the software is about.
3.  Show us that you have some brains. We're not looking for Einstein,
    but you should try to convince us that you're the best candidate for
    the project you're proposing. A good way to show us that you can
    think for yourself is by giving us a small project plan inside your
    application. A [work breakdown
    structure](http://en.wikipedia.org/wiki/Work_breakdown_structure)
    can be good way to communicate the scope of your project, and will
    also help you better understand your project's scope yourself. 
4.  Talk to us. We'd like to get to know you. If you're the type of
    person we like and could work with then we'll give your application
    more attention. You can contact us in a lot of ways but the
    preferred one is to come and chat to us on IRC:

<!-- end list -->

  - IRC: chat.freenode.net \#mixxx (look out especially for adam\_d and
    asantoni)
  - You can also e-mail: adamdavison --A=T-- gmail.com if you have more
    specific questions or are unable to access IRC for some reason
