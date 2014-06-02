## \#1 Weekly Report

Hello,

A week has passed since Google Summer of Code '14 has started and I'm
enjoying every moment of it. With constant help from my mentor, Daniel
Schürmann, I have managed to do most of the work towards moving the
current EQ into the effect space. The newly created EQ effect behaves
exactly like the current equalizer. It uses three
EngineFilterButterworths instantiated with a sample rate which is
fetched from the engine and two corner frequencies which are obtained
from the preferences "Equalizers" menu.

Here are the steps I took in order to achieve an EQ Effect, which is
intended to be a copy of the default equalizer:

  - Create a new EqEffectGroupState class which stores three
    EngineFilterButterworth for processing the signal
  - Create a new EqEffect class which handles the processGroup method
    and contains three EngineEffectParameters and two
    ControlObjectSlaves
  - Create an EffectManifest for the current effect and add three
    parameters to it; these parameters are the knobs which are
    responsible for controlling the equalizer's low, mid and high
    filters

<!-- end list -->

``` 
       * The parameter insertion is done via EffectManifest::addParameter() which returns a reference to the newly added parameter which can be modified however we desire through its "set*" methods
* Connect the two ControlObjectSlaves to "LoEQFrequency" and "HiEQFrequency" to be able to fetch the user's frequency preferences
* Add a new ControlObjectSlave field to GroupEffectProcessor class (m_pSampleRate); this field provides the current sample rate to the effects framework
       * Initially, I and Daniel thought of creating it as a static field inside GroupEffectProcessor, but being a static field it meant its lifetime will end at the end of the program, which isn't something desirable
* Register the newly created effect with NativeBackend, using NativeBackend::registerEffect<T> method
       * registerEffect<T> method goes all the way down to EffectProcessorInstantiator::instantiate method which calls T's constructor
```

Work still to be done:

  - fix this bug <https://bugs.launchpad.net/mixxx/+bug/1209294>
  - find a way of implementing switch type parameters (needed for "kill"
    buttons)

<!-- end list -->

``` 
       * an idea would be introducing a new type of Parameter set
       * another idea would be changing the EffectParameterSlot::m_pControlValue to a more generic class which will handle both the Potmeters and the PushButtons
```

The branch I'm working on can be seen here:
[eq\_effect\_branch](https://github.com/badescunicu/mixxx/compare/eq_effect_space#diff-7ea8c4ac05a59673d876185cca4fe4dcR14)

Stay tuned for updates\!  
Nicu Badescu  
  
  
[Back to the main page\!](extending_the_effects_engine)
