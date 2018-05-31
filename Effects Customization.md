# Effects Customizations

*by Kshitij Gupta*

<span class="underline">Email:</span> <kgupta119@gmail.com>

### Abstract

This project focuses on the effects section of Mixxx. I will be
refactoring the effects section of Mixxx to support the integration of
*LV2* effects and implementing new features like:

  - Import/Export Effect Chains
  - Show/Hide Effect Parameters
  - Rearrange Effect Parameters
  - Set Custom Defaults and Ranges

### Architecture goal

The current architecture of the effects code is overcomplicated and
makes it easy to create bugs when adding new features. In the GUI
thread, classes for handling effects and chains are split into pairs of
classes, EffectChain/EffectChainSlot and Effect/EffectSlot, but there is
not a clear separation of responsibilities between the members of each
pair. It is not clear what the role of EffectChain should be versus
EffectChainSlot. This has created a situation where state needs to be
duplicated and kept in sync between two classes, which is
overcomplicated and error-prone. Before we can implement new features,
we will refactor the current code so each class has a clearly defined
role:

  - EngineEffectChain: does the audio processing in the engine thread
  - EffectChain: holds the ControlObjects for interacting with skins and
    controllers in the GUI thread. Communicates state changes from the
    ControlObjects to EngineEffectChain via the effect MessagePipe FIFO.
  - EffectChainPreset: holds a snapshot of the state of EffectChain.
    Used by EffectsManager to communicate with EffectChain
  - EffectsManager: saves/loads XML files to a private QHash\<QString,
    EffectChainPreset\>, where the QString index is the user-defined
    name for the preset
  - WEffectChainPresetSelector (subclass of QComboBox): On startup, gets
    a QList\<QString\> from EffectsManager for the list of available
    chain presets, where the QString is the user-defined name for the
    preset. When the user selects a chain preset,
    WEffectChainPresetSelector tells EffectManager to load it, which
    triggers EffectManager to send the EffectChainPreset to EffectChain

Here is a sketch for a new effectchainpreset.h file:

    class EffectChainPreset {
      public:
        EffectChainPreset();
        EffectChainPreset(QDomElement savedPresetXml);
        ~EffectChainPreset();
    
        double dMix;
        double dSuper;
        EffectChainMixMode mixMode;
    
        QDomElement toXml();
    
      private
        QList<EffectPreset> m_effectPresets;
    }

### Proposed Timeline

##### Week 1 (May 14 - May 20)

\<del\>During this week, I'll be working on effect blacklisting for LV2
effects. I will also start working on connecting EngineEffect\* and the
Effect\* classes if I have enough time at the end of the week.

I will be able to work during nights or early mornings during this week
because I have a workshop scheduled from May 15th to May 30th during the
days.\</del\>

I was able to add the blacklisting feature by the end of the week. A
little work was required to be done on top of it.

##### Week 2 (May 21 - May 27)

~~I aim to finish connecting EngineEffect\* classes to their
corresponding Effect\* classes during this week.~~

I spent time working on the blacklisting feature only. Due to a workshop
scheduled in college, I couldn't find much time during the weekdays. A
few segmentation faults took a lot of time during development.

Got the Effect Blacklisting branch
[merged](https://github.com/mixxxdj/mixxx/pull/1674)\!

##### Week 3-6 (May 28 - June 24)

I will focus on refactoring the effects engine architecture during this
period. The currently implemented architecture is overcomplicated and is
the reason behind many bugs and less extensibility.

I will start by discussing the architecture thoroughly. Mostly, I will
start by consolidating the EffectChain/EffectChainSlot classes and other
Effect\*/Effect\*Slot classes. Then I will proceed on to refactor how
the effects are connected to their corresponding Engine classes.

##### Week 7-8 (June 25 - July 8)

I will work on implementing importing/exporting effect chains during
these weeks.

##### Week 9-10 (July 9 - July 22)

I will work on implementing effect parameter hiding and rearrangement
during these weeks.

##### Week 11 (July 23 - July 29)

I will work on implementing custom defaults and ranges(if time allows)
programmatically.

##### Week 12-13 (July 30 - August 14)

I will implement any missed out functionality in these weeks and write
the final documentation in this period.

#### Proposed Deadlines

##### May 21

Finish working on LV2 effects branch with effect blacklisting.
([Merged](https://github.com/mixxxdj/mixxx/pull/1674))

##### June 25

Finish working on the new effects architecture.
