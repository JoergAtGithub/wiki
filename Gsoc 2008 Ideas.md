# Google Summer of Code 2008

[Google's Summer of Code](http://code.google.com/soc/) program provides
funding for students who'd like to contribute to open source projects.
Mixxx is a good project to work on because it gives you experience
working with cross-platform development as well as writing code that's
going to power live performances (ie. stability is key).

# Ideas

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
basic types of mapping. There is a lot of scope for improvement in this
area and one or more students would be able to focus on the one(s) which
interest them the most:

  - Enhance the mapping file format to account for more complex
    controllers
  - Create a GUI for easy controller mapping for non-experts
  - Create a system for automatically downloading mappings from a
    central site when a new controller is connected

Hardware support is a key aspect of Mixxx and one which could benefit
from more dedicated attention. A successful student in this project
would put themselves in an excellent position to continue as a key
member of the Mixxx development team after GSoC, should they want to do
so.

We're currently compiling a list of ideas for potential projects from
our developers. The ideas list "is meant to introduce contributors to
your project's needs and to provide inspiration to would-be student
applicants".

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
