# EQ Rack

This part of the project aims at replacing the current static EQ signal
path with an additional EffectRack which contains EQ Effects for each
deck.

This has the following consequences:

  - completely remove `EngineFilterBlock` class because we are passing
    the responsibility to `EngineEffectsManager`
  - allow the user to disable the EQ as well as give the possibility to
    replace the EQ with other similar effects or other advanced EQ
    implementations.

Below is a drawing of the current EQ approach (left) and how it will
look after we ditch processing from `EngineFilterBlock`:

![http://oi59.tinypic.com/98t7pd.jpg](http://oi59.tinypic.com/98t7pd.jpg)  
  

### Developer's point of view

These are the main ideas behind the EQ Rack:

  - another EffectRack is added which dynamically gets populated with
    EffectChains, each time the control responsible for the number of
    decks is changed

<!-- end list -->

``` 
    * throughout the code the dedicated EQ Rack is known to be the last Rack from the EffectsManager
    * Mixxx can have an arbitrary number of decks, so it seemed natural to create a new EffectUnit and instantiate a new EQ Effect whenever a deck is added. I did this by inserting a method (addEqualizer) at the end of PlayerManager::addDeckInner(). This method is also responsible for setting the effect to be fully wet.
* each EffectChain contains only one EffectSlot, is set to fully wet and is active on a specific [Channel];
* skins don't need to be modified because aliases are created dynamically when the number of decks is changed
    * The best way of controlling the EQ Effect Rack and maintaining compatibility with skins and controllers was adding support for control aliasing. The correct way of using aliases is to create them after the controls to which they are pointing have been instantiated. This leads to two possible ways of registering aliases. Either you create an alias right after the original control has been created or you put the desired aliases inside ''MixxxMainWindow::createCOAliases'' method which I have introduced. It gets called just before loading the skin and before initializing the controllers.
    * example: "[Channel3],filterLow" is an alias for "[EffectRackY_EffectUnit3_Effect1],parameter1", where Y is the index of the last Effect Rack (the EQ Rack)
    * "[Channel3],filterMid" is an alias for "[EffectRackY_EffectUnit3_Effect1],parameter2"
    * "[Channel3],filterHigh" is an alias for "[EffectRackY_EffectUnit3_Effect1],parameter3"   
```

Following this approach it is easy to add a Master EQ which can be
activated or deactivated for Master output.

  
  
\==== User's point of view ====

The Equalizer preferences menu has changed. Inside it, the user can can
choose which EQ Effect should be active on each Deck.

The “Bypass” check box is responsible for disabling or enabling EQ
processing. is equivalent to loading an empty effect on the EQ Effect
spot for each Deck.

A nice feature is offering the advanced user the possibility to load any
available effect on the EQ Effect spot. This is done via “Show all
effects” check box.

The user EQ experience is enhanced because each deck can have a
different effect loaded on it. For example, Butterworth8EQ can be loaded
on Deck1 and Filter can be loaded on Deck 2.

![http://oi62.tinypic.com/2vnfgjk.jpg](http://oi62.tinypic.com/2vnfgjk.jpg)
