# Effects Customizations

*by Kshitij Gupta*

<span class="underline">Email:</span> <kgupta119@gmail.com>

*mentor: Be*

## GSoC 2018 recap

It has been a great experience to work with Mixxx for this summer. I
learned a lot through the summer. I focused mostly on the
maintainability of code during the entire summer, from a clean git
history to a better architecture. It helped me sharpen my programming
skills and also made me more confident to work with C++ and the Qt
framework.

I give a special thanks to my mentor *Be* for all the code reviews,
discussions and all the help during the summer.

### Work done

The work done during the summer can be found in the following pull
requests:

  - [Effect Blacklisting PR](https://github.com/mixxxdj/mixxx/pull/1674)

<!-- end list -->

  - [Effects Refactoring PR](https://github.com/mixxxdj/mixxx/pull/1705)

### Future work

The GUI for effect parameters and importing/exporting effect chains is
yet to be implemented. The new naming of classes is also not finalized,
and requires more discussions with the community. I aim to complete them
before release 2.2.0 so that it is thoroughly tested before release
2.3.0

## Original proposal

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
    subclass without EngineEffectSlot being concerned which type of
    effect is loaded. No change from the present implementation.
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
an EffectProcessorState subclass and an EffectProcessorImpl subclass:

  - **EffectProcessorState**: an abstract base class for the state of an
    instance of an effect for one combination of input and output
    channels. This state persists across cycles of the audio engine
    thread. This will be made by *renaming EffectState*.
  - **EffectProcessorImpl\<EffectProcessorState\>**: a template abstract
    base class which contains the logic for managing the
    EngineEffectStates so the implementation of specific effects like
    Echo and Flanger do not need to be concerned with memory management.
    Each effect implements a subclass of this declaring its parameters
    with an EffectManifest and containing a processChannel function with
    its DSP logic. No change from the present implementation.

<!-- end list -->

  - **EngineEffect**: A wrapper around EffectProcessor with some common
    contains logic for smoothly toggling effects on and off without
    audible pops. No change from current implementation.
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
    EffectProcessors and EffectProcessorStates are allocated on the heap
    in the main thread and pointers to them are passed on the
    MessagePipe to the EngineEffectSlots.
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

## Proposed Timeline

Some changes were made to the proposed timeline:

  - Effect Parameter Hiding and Rearrangement was implemented before
    working on importing/exporting effect chains because the order also
    needs to be stored.

##### Week 1 (May 14 - May 20)

During this week, I'll be working on effect blacklisting for LV2
effects. I will also start working on connecting EngineEffect\* and the
Effect\* classes if I have enough time at the end of the week.

I will be able to work during nights or early mornings during this week
because I have a workshop scheduled from May 15th to May 30th during the
days.

##### Week 2 (May 21 - May 27)

I aim to finish connecting EngineEffect\* classes to their corresponding
Effect\* classes during this week.

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

## Weekly Blog

##### Week 1

I was able to add the blacklisting feature by the end of the week. A
little work was required to be done on top of it.

##### Week 2

I spent time working on the blacklisting feature only. Due to a workshop
scheduled in college, I couldn't find much time during the weekdays. A
few segmentation faults took a lot of time during development. The plan
for effect refactoring was also discussed thoroughly towards the end of
the week.

Got the Effect Blacklisting branch
[merged](https://github.com/mixxxdj/mixxx/pull/1674)\!

##### Week 3

During this week, We came up with the plan to keep *Preset* classes. I
worked on consolidating the highly convoluted EffectChain and
EffectChainSlot classes. After going through numerous segfaults, I was
able to push changes.

##### Week 4

The Effect was not being added to the engine properly and hence I fixed
those issues during the week and made changes in accordance with the
code reviews. We also came up with the new naming of classes, and had
discussions regarding the same with the community.

##### Week 5

I successfully removed the EffectChainManager and the EngineEffectRack
layer in the engine in this week and had discussions on removing the
EffectRack layer.

##### Week 6

I worked on removing the superfluous EffectRack layer. I faced many
cyclic dependency issues and learned to deal with them after the removal
of EffectChainManager layer which acted as an interface over
EffectChainSlot class.

##### Week 7

I was a little busy in presentations at my college and hence could take
out less time to work on my project. I successfully managed to remove
the EffectRack layer and get the software working without any errors. I
parallelly started working on importing/exporting chains, which I pushed
on a different branch which can be merged onto the effects\_refactoring
branch once everything else is done.

##### Week 8

We discussed on refactoring EffectInstantiator which was tightly coupled
with the loading of effects. I worked on consolidating Effect and
EffectSlot classes and implemented a new flow for loading effects into
slots.

##### Week 9

I successfully consolidated Effect and EffectSlot classes during this
week in accordance with the code reviews. I also faced numerous issues
with upgrading Qt.

##### Week 10

I removed the EffectParameter class abstraction over
EffectManifestParameter. I also changed the way assertions were
implemented for EffectParameters to ensure valid ranges. I also worked
on renaming various classes in the entire codebase.

##### Week 11

After long discussions, We decided to reimplement the EffectParameter
class. I worked reimplementing the EffectParameter class to be
compatible with effect parameter hiding and rearrangement. Also, I
worked on renaming the classes(EffectKnobParameter classes) again.

##### Week 12

I implemented effect parameter hiding and re-arrangement without
reloading the effects to the default state during this week.

##### Week 13

*(Ongoing...) I am working on custom ranges, defaults in
EffectParameters and importing/exporting of effect chains.*
