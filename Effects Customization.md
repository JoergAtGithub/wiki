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
common English audio terminology. For the ControlObjects, what is
currently called "\[EffectRack1\_EffectUnitX\_EffectY\], parameterZ"
will be renamed to "\[EffectRackX\_EffectY\], parameterZ" and what is
"\[EqualizerRack1\_\[Channel1\]\_Effect1\], parameterZ" will be renamed
to "[custom per-effect
defaults](/Channel1]_EqualizerRack_Effect1],%20parameterZ"%20\(the%20old%20names%20will%20be%20aliased%20for%20backwards%20compatibility\).%20Before%20we%20implement%20new%20features,%20we%20will%20refactor%20the%20current%20code%20so%20each%20class%20has%20a%20clearly%20defined%20role.%20From%20the%20bottom%20up/% A% A%20%20*%20**EffectProcessor**/%20an%20instance%20of%20a%20specific%20effect%20such%20as%20Echo%20or%20Flanger.%20This%20is%20an%20abstract%20base%20class%20to%20provide%20an%20interface%20for%20EngineEffectSlot%20to%20interact%20with%20the%20EffectProcessorImpl%20subclass%20without%20being%20concerned%20which%20type%20of%20effect%20is%20loaded.%20No%20change%20from%20the%20present%20implementation.% A%20%20*%20**EffectManifest**/%20declares%20the%20metadata%20for%20a%20specific%20type%20of%20effect%20such%20as%20Echo%20or%20Flanger.%20This%20metadata%20includes%20the%20effect's%20name;%20available%20parameters;%20and%20the%20ranges,%20types,%20and%20defaults%20of%20those%20parameters.%20No%20change%20from%20the%20present%20implementation.% A%20%20*%20**EffectsBackend**/%20enumerates%20available%20effect%20types%20and%20instantiates%20an%20EffectProcessor%20from%20an%20EffectManifest.%20Each%20category%20of%20effect,%20namely%20Mixxx's%20built-in%20effects%20and%20LV2%20effect%20plugins,%20has%20its%20own%20EffectsBackend%20subclass.% A% AEvery%20specific%20effect%20like%20Echo%20or%20Flanger%20is%20implemented%20as%20a%20pair%20of%20an%20EngineEffectState%20subclass%20and%20an%20EffectProcessorImpl%20subclass/% A%20%20*%20**EngineEffectState**/%20an%20abstract%20base%20class%20for%20the%20state%20of%20an%20instance%20of%20an%20effect%20for%20one%20combination%20of%20input%20and%20output%20channels.%20This%20state%20persists%20across%20cycles%20of%20the%20audio%20engine%20thread.%20This%20will%20be%20made%20by%20renaming%20EffectState%20to%20EngineEffectState.% A%20%20*%20**EffectProcessorImpl\<EngineEffectState\>**/%20a%20template%20abstract%20base%20class%20which%20contains%20the%20logic%20for%20managing%20the%20EngineEffectStates%20so%20the%20implementation%20of%20specific%20effects%20like%20Echo%20and%20Flanger%20do%20not%20need%20to%20be%20concerned%20with%20memory%20management.%20Each%20effect%20implements%20a%20subclass%20of%20this%20declaring%20its%20parameters%20with%20an%20EffectManifest%20and%20containing%20a%20processChannel%20function%20with%20its%20DSP%20logic.%20No%20change%20from%20the%20present%20implementation.% A% A%20%20*%20**EngineEffectSlot**/%20A%20place%20where%20an%20effect%20may%20be%20loaded%20that%20lives%20in%20the%20audio%20engine%20thread.%20It%20may%20contain%20an%20EffectProcessor%20or%20be%20empty.%20This%20class%20contains%20logic%20for%20smoothly%20toggling%20effects%20on%20and%20off%20without%20audible%20pops.%20This%20class%20will%20be%20made%20by%20renaming%20EngineEffect.% A%20%20*%20**EffectSlot**/%20holds%20the%20ControlObjects%20for%20interacting%20with%20skins%20and%20controllers%20in%20the%20GUI%20thread.%20Communicates%20state%20changes%20from%20the%20ControlObjects%20to%20EngineEffectSlot%20via%20the%20effect%20MessagePipe%20FIFO.%20Passes%20EffectProcessor%20instances%20to%20the%20EngineEffectSlot%20also%20via%20the%20MessagePipe%20FIFO.%20Decouples%20the%20set%20of%20potential%20effect%20parameters%20from%20the%20parameters%20exposed%20to%20skins%20and%20controllers%20so%20that%20users%20can%20hide%20and%20rearrange%20parameters%20as%20they%20prefer.%20This%20will%20be%20made%20by%20combining%20the%20present%20Effect%20&%20EffectSlot%20classes.% A%20%20*%20**EffectPreset**/%20contains%20a%20snapshot%20of%20the%20state%20of%20an%20EffectSlot%20and%20serializes/deserializes%20this%20to%20XML.%20This%20will%20be%20used%20both%20to%20create%20EffectRackPresets%20and%20implement%20[[https///bugs.launchpad.net/mixxx/+bug/1740504)

  - **EngineEffectRack**: contains a chain of 3 EngineEffectSlots. This
    will be made by renaming EngineEffectChain.
  - **EffectRack**: holds the ControlObjects for interacting with skins
    and controllers in the GUI thread. Communicates state changes from
    the ControlObjects to EngineEffectRack via the effect MessagePipe
    FIFO. This class will be made by combining the current EffectChain &
    EffectChainSlot classes.
  - **EqualizerRack**, **QuickEffectRack**, **OutputEffectRack**:
    EffectRack subclasses for the deck equalizers and QuickEffects plus
    the master output equalizer. When the old superfluous EffectRack
    layer is removed, these will be reimplemented as subclasses of the
    new EffectRack class made from consolidate the old EffectChain &
    EffectChainSlot classes.
  - **EffectRackPreset**: holds a snapshot of the state of an EffectRack
    and serializes/deserializes this state to XML. Used by
    EffectsManager to communicate with EffectRack.

<!-- end list -->

  - **EffectsManager**: saves/loads XML files to a private
    QHash\<QString, EffectRackPreset\>, where the QString index is the
    user-defined name for the preset
  - **MessagePipe**: a FIFO for communicating state changes and objects
    from the main thread to the audio engine thread without blocking.
    EffectProcessors and EffectStates are allocated on the heap in the
    main thread and pointers to them are passed on the MessagePipe to
    the EngineEffectSlots.
  - **EngineEffectsManager**: provides an interface for the rest of the
    audio engine to the
    EngineEffectRacks/EngineEffectSlots/EffectProcessors. Receives
    messages from the MessagePipe and relays them to EngineEffectRacks
  - **WEffectRackPresetSelector**: subclass of QComboBox. On startup,
    gets a QList\<QString\> from EffectsManager for the list of
    available EffectRackPresets, where the QString is the user-defined
    name for the preset. When the user selects an EffectRackPreset,
    WEffectChainPresetSelector tells EffectManager to load it, which
    triggers EffectsManager to send the EffectRackPreset to EffectRack

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
