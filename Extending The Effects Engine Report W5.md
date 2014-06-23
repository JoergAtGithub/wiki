Hello again,

This week I started with fixing a crash in LightweightEQ, which is an
Equalizer Effect for low-performance hardware. The problem was the id's
of the effect parameters, they were not correctly set. So I have fixed
that by assigning the following ids for the knobs: "eq\_low", "eq\_mid"
and "eq\_high". On top of that, I removed dry mixing both from
LightweightEQ and EQDefault. However, I talked with Daniel and we plan
to reintroduce that to the effect which uses Bessel filters.

I am happy to inform you that I'm making progress towards my goal of
replacing the Default EQ from *enginefilterblock.cpp* with an Equalizer
Effect. I have finally managed to add switch type parameters to the
Effects framework. The last bug was a typo Daniel pointed me out in
*effectbuttonparameterslot.cpp*. I was calling *getParameter()* method
instead of *getButtonParamter()*. Prior to fixing this, the buttons were
not updating correctly, they were dependent to their corresponding knob.
All they need now is a bit of code refactoring, because some code is
duplicated, especially in *effectbuttonparameterslot.cpp* which contains
the class for handling Button parameters.

For the EQ Effect Rack I broken down my work in the following parts:

  - Add a new EffectRack (done)
  - Modify Deere skin to display that additional Rack (done)
  - Add EQ Effects to the newly created Rack
  - For this part I chose to instantiate one Effect per each deck. In
    order to achieve this, I could instantiate 4 Effects as this is the
    current maximum number of decks. But Mixxx can have an arbitrary
    number of decks, so it seemed natural for me to create a new
    EffectUnit and instantiate a new EQ Effect whenever a deck is added.
    I did this by inserting a method (*addEqualizer*) at the end of
    *PlayerManager::addDeckInner()*. This method is also responsible for
    setting the effect to be fully wet.
  - Allow aliases for controls (in progress)
  - We need to make the transition as smooth as possible and this means
    we still want to handle the newly added EQ Effects with
    *\[ChannelX\]filter\[Low/Mid/High\]*. The most interesting way of
    achieving this is to add support for control aliases, a feature
    which is requested on the bug tracker too\[1\].

You can see my work on the EQ EffectRack and switch type parameters
here\[2\].

Yours truly,  
Nicu Badescu

\[1\] - https://bugs.launchpad.net/mixxx/+bug/1273953  
\[2\] - <https://github.com/badescunicu/mixxx/compare/kill_buttons>
