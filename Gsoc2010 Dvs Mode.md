# Adding a digital vinyl system (DVS) / external mixer mode to Mixxx (GSoC 2010 project)

  - Student: **Bill Good**
  - Mentor: **Adam Davison**

## Abstract

Adding an external mixer mode to Mixxx will greatly improve Mixxx's
ability to act as a part of a digital vinyl system. Mixxx's current
method of achieving this involves diverting one deck to the main output,
and the other to the headphone output, allowing the two to be mixed
externally. However, no features, such as the equalizer, can be
disabled. Benefits of disabling various features include increased CPU
time for other threads, and UI recognition of unwanted features.

## More info

  - [dvs\_mode](dvs_mode) has some good ideas, as does [GSOC2010
    page](gsoc2010ideas).
  - I'm bkgood on launchpad and freenode
  - To contact me by email, use my irc name @gmail.com

## Specification

### Use cases

  - DJ Joe doesn't like lugging around crates of vinyl or CDs, but
    enjoys using his vinyl turntables (or DJ CD players) and mixer. DVS
    mode will allow him to control Mixxx's playback with vinyl control,
    and then mix the outputs with his own mixer, his his own effect
    modules, etc.

### Design

### Work breakdown structure

1.  External mixer (in lp:\~bkgood/mixxx/features\_external\_mixer).
    Only concerned with taking deck samples and outputting them to two
    different channel pairs (same or different audio devices).
    EngineMaster will likely still apply the XF and produce headphone
    and master buffers and do all the various things it does.
    1.  Implement changes to preferences dialog.
        1.  Make all audio sources and receivers configurable.
        2.  Move vinyl control input selections from the vinyl control
            pane.
            1.  Perhaps make a note on the vinyl control page telling
                users the input selections have moved.
        3.  Limit the frequency at which audio preferences are applied.
            1.  Only apply on user clicking the apply button or the OK
                button (change in behaviour, currently preferences are
                applied on selecting many different items).
    2.  Engine support
        1.  Make the deck 1 and 2 pointers accessible from EngineMaster.
            1.  features\_hydro has its own implementation
    3.  Backend support (SoundManager, SoundDevice,
        SoundDevicePortAudio)
        1.  Abstract AudioSource and AudioReceiver to hold indexes,
            update related code.
        2.  Add to SoundManager a way to keep track of audio hardware
            configuration (ConfigObject key-value system too limiting)
2.  DVS mode: (on hold until a new design materializes)
    1.  Add a vinyl control checkbox to a preferences page, in addition
        to its place in the options menu.
    2.  Make EQs, gains, faders, flanger etc. toggle-able.
    3.  Reflect disabled functionality in GUI, may not be possible with
        current skinning subsystem.
3.  External audio pass-through and microphone input
    1.  Microphone input for voice-over.
    2.  Pass-through of stereo signals into engine mixing.
    3.  See
        <https://blueprints.launchpad.net/mixxx/+spec/external-passthru>
        

## ChangeLog

I'll update this at least weekly, to make sure I'm keeping up with what
needs done. May do a blogger on this too, never have done a blog before
though. I'm going to try to include \_everything\_ mixxx-related I do so
on days where I dink around with something other than my project I know
I didn't totally waste the day :)

  - sometime prior to 20100601: Digging through the mixxx code base to
    try to further figure out implementation details, plus learning a
    bit about how sampling (digital representation of analog signals)
    works and skimming a book on Qt.
  - 20100601: Added preferences option to dlgprefsounddlg.ui for
    external mixer. Based it on QStackedWidget, so we just move though
    the stack to select between internal/external mixer devices.
  - 20100602: Read through features\_hydra merge diff. Looks like a step
    in the right direction (lots of silly stuff gone from
    mixxxapp::mixxxapp, yay\!). Going to write up thoughts on
    preferences diag. Preferences diag limited in size so mixxx can run
    and be useful on netbooks. Would really like to make the audio
    preferences (and ideally all preferences) such that settings would
    be reverted if user doesn't click "OK." Would also like to make a
    "test" button to send either white noise or a sine wave to a
    specific channel pair on a device so that the user can be sure he's
    got the right channel going to the right mixer (or amp) input.
    dlgprefsound.cpp is a bloody mess, can't wait to go after it once
    I've got the dialog looking like I want it.
  - 20100609: Quick update as I'm tired as hell: decided (final change
    of heart/mind, I promise) that I didn't want to start from the top
    (ie., UI) down and I'd much rather just build a nice and pretty
    backend, so I uncommitted my UI file change and finally figured out
    how to reflect that in LP, and then committed and pushed a new
    change set. AudioSource and Receiver now have an index attribute, to
    distinguish between different deck sources or vinyl control
    receivers. This became necessary because I changed the
    Audio{Source,Receiver}Type enums to not list discrete decks or vinyl
    control inputs as that approach will likely prove unextendable (not
    a real word) in the future, this mainly caught my eye because the
    number of CSAMPLE\*'s being allocated at runtime were hard-set to
    the number of source types (not good when you have a variable number
    of sources, and one of my goals with all this is to keep \>2 sources
    in mind, especially since another GSOC student's project uses them.
  - Will (tentatively, haven't thought all the way through this one) be
    using a QHash (hash table-based dictionary/mapping) to implement the
    assocation of Audio{Source,Receiver}'s to buffers; that's committed
    as well. 
  - Committed a couple of static methods that generate an identifying
    QString from an (new-style) Audio{S,R} (shorthand for
    Audio{Source,Receiver} I'll continue to use if I remember it as
    typing all that is a pita). These will probably get moved into their
    respective structs, which will likely become classes (not that
    there's any real difference in cpp, but whatever) with ctor's
    instead of public fields (because I want to make sure
    Audio{S,R}.index is zero if the type doesn't lend itself to
    indexing, like SOURCE\_MASTER) and some other methods: operator==
    for QHash (it needs that, plus it needs qHash(AudioSource) and
    qHash(AudioReceiver) globals defined to generate hashes), and a
    method to detect whether or not one source's or receiver's channel
    selection clashes with another (bad\!).
  - This isn't really worth mentioning as it's said plainly enough in
    the commit log but I'll paste it: Made the array of
    VinylControlProxy's a QList, so the number of instances isn't
    hardcoded. (end paste) It was previously hard-coded to 2, and there
    shouldn't be any appreciable loss in speed for the \[hopefully later
    realized\] gain.
  - What's implemented in the commit is not nearly what's in my head or
    even coded in files elsewhere on my hard-drive, as I tried to convey
    with all this senseless typing ;)
  - Commit at
    <http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2413>
  - 20100612
  - Commit
    <http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2414>

<!-- end list -->

``` 
    * Moved AudioSource and AudioReceiver to audiopath.{h,cpp}
    * Refactored the classes -- instead of having channelBase and channels as members, they now have a member object of type ChannelGroup which has this data, and also includes methods for comparing channel groups to make sure they don't clash (the method implementation in this commit is actually poorly thought out, but an updated one is in a subsequent commit). AudioSource and AudioReceiver also now have a base class AudioPath which basically just has a channel group as the type member is specific to the source or receiver distinction (**note to self: move index data member to audiopath as protected**)
* Commit http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2415
    * Added qHash fuctions (and related methods to classes) to allow QHash to get hash values for AudioSources and Receivers. Given that qHash must return an unsigned int, and working under the assumptions that an int is 4 bytes and the four unsigned int values which make up an AudioSource or receiver will normally be small and therefore easily representable using 4 1-byte values. If an int is only 2 bytes, some precision will be lost, but QHash can deal with this, with minor slowdowns.
    * ChannelGroup::clashesWith is now fixed from revision 2414.
* Commit http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2416
    * Gave EngineMaster a getDeckBuffer method to get the unmixed buffers. Required hack until hydra is merged.
* 20100617
* Commit http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2417
    * Nothing exciting, a couple of formatting fixes and commenting.
* 20100621
* Commit http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2421
    * Gave AudioPath classes some accessors.
* Commit http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2422
    * Made SoundDevice and SoundDevicePortAudio AudioPath-using. I got a little carried away with tabs-to-spaces around some code I had to modify but I hope it's all ok :)
* Commit http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2423 (this and the next commit are dated the 22th but it still feels like the 21st to my body :))
    * Beginnings of SoundManager w/AudioPath and some include/forward decs in SoundDevice.
* Commit http://bazaar.launchpad.net/~bkgood/mixxx/features_external_mixer/revision/2424
    * Rather large commit that includes some error-fixes and finished SoundManager modification to use AudioPath classes. Many of the internal structures are now QHashes or QLists, which provide a degree of extendability not previously available but shouldn't have any noticeable overhead as both data structures are implicitly shared. QHash was chosen over QMap for its faster operation.
    * The branch now compiles. Audio output is normal, and I don't see any increased CPU with htop. I need to ask someone else to check out vinyl control as I don't have a 2-channel sound card at the moment. **update: tested this with jack, seems to work.**
    * Commit has a nicer log of what was in it.
```
