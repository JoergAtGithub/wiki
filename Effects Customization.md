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
thread, classes for handling effects and chains are split into two pairs
of classes, EffectChain/EffectChainSlot and Effect/EffectSlot, but there
is not a clear separation of responsibilities between the members of
each pair. It is not clear what the role of EffectChain should be versus
EffectChainSlot. This has created a situation where state needs to be
duplicated and kept in sync between the classes of each pair, which is
overcomplicated and error-prone. Furthermore, there is a superfluous
EffectRack layer above EffectChain/EffectChainSlot which does nothing
but overcomplicate the code. This layer will be removed and what are
currently called "chains"/"units" will be renamed "racks" to align with
common English audio terminology. The ControlObjects will be renamed to
align with the new implementation and aliases will be provided for
backwards compatibility:

  - `[EffectRack1_EffectUnitX_EffectY], parameterZ` -\>
    `[EffectRackX_EffectY], parameterZ`
  - `[EqualizerRack1_[Channel1]_Effect1], parameterZ`
    -\>`[[Channel1]_EqualizerRack_Effect1], parameterZ`
  - `[QuickEffectRack1_[Channel1]_Effect1], parameterZ` -\>
    `[[Channel1]_QuickEffectRack_Effect1], parameterZ`

Before we implement new features, we will refactor the current code so
each class has a clearly defined role. From the bottom up, with changes
to the current architecture *italicized*:

  - **EffectProcessor**: an instance of a specific effect such as Echo
    or Flanger. This is an abstract base class to provide an interface
    for EngineEffectSlot to interact with the EffectProcessorImpl
    subclass without being concerned which type of effect is loaded. No
    change from the present implementation.
  - **EffectManifest**: declares the metadata for a specific type of
    effect such as Echo or Flanger. This metadata includes the effect's
    name; available parameters; and the ranges, types, and defaults of
    those parameters. No change from the present implementation.
  - **EffectsBackend**: enumerates available effect types and
    instantiates an EffectProcessor from an EffectManifest. Each
    category of effect, namely Mixxx's built-in effects and LV2 effect
    plugins, has its own EffectsBackend subclass. *Refactoring required
    to instantiate EffectProcessors instead of old Effect class.*

Every specific effect like Echo or Flanger is implemented as a pair of
an EngineEffectState subclass and an EffectProcessorImpl subclass:

  - **EngineEffectState**: an abstract base class for the state of an
    instance of an effect for one combination of input and output
    channels. This state persists across cycles of the audio engine
    thread. This will be made by *renaming EffectState*.
  - **EffectProcessorImpl\<EngineEffectState\>**: a template abstract
    base class which contains the logic for managing the
    EngineEffectStates so the implementation of specific effects like
    Echo and Flanger do not need to be concerned with memory management.
    Each effect implements a subclass of this declaring its parameters
    with an EffectManifest and containing a processChannel function with
    its DSP logic. No change from the present implementation.

<!-- end list -->

  - **EngineEffectSlot**: A place where an effect may be loaded that
    lives in the audio engine thread. It may contain an EffectProcessor
    or be empty. This class contains logic for smoothly toggling effects
    on and off without audible pops. This class will be made by
    *renaming EngineEffect*.
  - **EffectSlot**: holds the ControlObjects for interacting with skins
    and controllers in the GUI thread. Communicates state changes from
    the ControlObjects to EngineEffectSlot via the effect MessagePipe
    FIFO. Passes EffectProcessor instances to the EngineEffectSlot also
    via the MessagePipe FIFO. Decouples the set of potential effect
    parameters from the parameters exposed to skins and controllers so
    that users can hide and rearrange parameters as they prefer. This
    will be made by *combining the present Effect & EffectSlot classes*.
  - **EffectPreset**: contains a snapshot of the state of an EffectSlot
    and serializes/deserializes this to XML. This will be used both to
    create EffectRackPresets and implement [custom per-effect
    defaults](https://bugs.launchpad.net/mixxx/+bug/1740504). This will
    be a *new class*.

<!-- end list -->

  - **EngineEffectRack**: contains a chain of 3 EngineEffectSlots. This
    will be made by *renaming EngineEffectChain*.
  - **EffectRack**: holds the ControlObjects for interacting with skins
    and controllers in the GUI thread. Communicates state changes from
    the ControlObjects to EngineEffectRack via the effect MessagePipe
    FIFO. This class will be made by *combining the current EffectChain
    & EffectChainSlot classes. The old EffectRack & EngineEffectRack
    classes that don't do anything will be removed.*
  - **EqualizerRack**, **QuickEffectRack**, **OutputEffectRack**:
    EffectRack subclasses for the deck equalizers and QuickEffects plus
    the master output equalizer. When the old superfluous EffectRack
    layer is removed, these will be *reimplemented as subclasses of the
    new EffectRack class* made from consolidate the old EffectChain &
    EffectChainSlot classes.
  - **EffectRackPreset**: holds a snapshot of the state of an EffectRack
    and serializes/deserializes this state to XML. Used by
    EffectsManager to communicate with EffectRack. This will be a *new
    class*.

<!-- end list -->

  - **EffectsManager**: saves/loads XML files to a private
    QHash\<QString, EffectRackPreset\>, where the QString index is the
    user-defined name for the preset.
  - **MessagePipe**: a FIFO for communicating state changes and objects
    from the main thread to the audio engine thread without blocking.
    EffectProcessors and EffectStates are allocated on the heap in the
    main thread and pointers to them are passed on the MessagePipe to
    the EngineEffectSlots.
  - **EngineEffectsManager**: provides an interface for the rest of the
    audio engine to the
    EngineEffectRacks/EngineEffectSlots/EffectProcessors. Receives
    messages from the MessagePipe and relays them to EngineEffectRacks.
  - **WEffectRackPresetSelector**: subclass of QComboBox. On startup,
    gets a QList\<QString\> from EffectsManager for the list of
    available EffectRackPresets, where the QString is the user-defined
    name for the preset. When the user selects an EffectRackPreset,
    WEffectChainPresetSelector tells EffectManager to load it, which
    triggers EffectsManager to send the EffectRackPreset to EffectRack.
    This will be a *new class*.

Here is a sketch for a new effectrackpreset.h file:

    class EffectRackPreset {
      public:
        EffectChainPreset();
        EffectChainPreset(QDomElement savedPresetXml);
        ~EffectChainPreset();
    
        double dSuper;
        EffectChainMixMode mixMode;
    
        QDomElement toXml();
    
      private:
        QList<EffectPreset> m_effectPresets;
    };

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
