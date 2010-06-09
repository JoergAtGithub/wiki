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

## Current status

I'll update this at least weekly, to make sure I'm keeping up with what
needs done. May do a blogger on this too, never have done a blog before
though. I'm going to try to include \_everything\_ mixxx-related I do so
on days where I dink around with something other than my project I know
I didn't totally waste the day :)

  - Digging through the mixxx code base to try to further figure out
    implementation details, plus learning a bit about how sampling
    (digital represenation of analog signals) works and skimming a book
    on Qt. (sometime prior to 2-6-2010)
  - Added preferences option to dlgprefsounddlg.ui for external mixer.
    Based it on QStackedWidget, so we just move though the stack to
    select between internal/external mixer devices. 1-6-2010
  - Read through features\_hydra merge diff. Looks like a step in the
    right direction (lots of silly stuff gone from mixxxapp::mixxxapp,
    yay\!). Going to write up thoughts on preferences diag. Preferences
    diag limited in size so mixxx can run and be useful on netbooks.
    Would really like to make the audio preferences (and ideally all
    preferences) such that settings would be reverted if user doesn't
    click "OK." Would also like to make a "test" button to send either
    white noise or a sine wave to a specific channel pair on a device so
    that the user can be sure he's got the right channel going to the
    right mixer (or amp) input. dlgprefsound.cpp is a bloody mess, can't
    wait to go after it once I've got the dialog looking like I want it.
    2-6-2010
  - Quick update as I'm tired as hell: decided (final change of
    heart/mind, I promise) that I didn't want to start from the top
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
    for the interested, for comments (on what I've typed here or the
    commit, since the commit is in actuality quite short) hit me up on
    IRC or email me.
  - Ok think that's all for now. Cheers\! And I'm off to bed :) -- Bill
    7-9-2010

## Specification

### Use cases

  - DJ Joe doesn't like lugging around crates of vinyl or CDs, but
    enjoys using his vinyl turntables (or DJ CD players) and mixer. DVS
    mode will allow him to control Mixxx's playback with vinyl control,
    and then mix the outputs with his own mixer, his his own effect
    modules, etc.

### Design

Currently, the sample buffers are only accessible to EngineMaster. These
will be exposed via accessor methods so that SoundManager can choose
between the master and headphone mixes or the individual samples.
Changes made will be conscious of eventual merge of n-decks branch, i.e.
will want to look at exposing the various decks using a `CSAMPLE*
EngineMaster::getDeckByIndex(uint index);` method in place of

``` cpp-qt
CSAMPLE* EngineMaster::getDeck1();
CSAMPLE* EngineMaster::getDeck2(); // etc
```

There is, of course, an upper-bound given the finite nature of PCI
slots, USB ports, and sound cards, but a DJ could easily use four decks
(8 channels) of output (of course, there's currently only 2 inputs of
vinyl control... not sure if n-decks extends that).

  - This is all done by hydra, once it gets merged it's all golden :)

The other major aspect of the mode is UI, preferences will have to be
extended to support routing audio to an external instead of using an
internal mixer. This will likely include a bit of refactoring.

### Work breakdown structure

  - To be completed :) See
    [Work\_breakdown\_structure](https://en.wikipedia.org/wiki/Work_breakdown_structure)
  - Not really proper, but here's my version (in numbered steps\!) (aka
    milestones):

<!-- end list -->

1.  External mixer (in lp:\~bkgood/mixxx/features\_external\_mixer).
    ONLY concerned with taking deck samples and outputting them to two
    different channel pairs (same or different audio devices).
    EngineMaster will likely still apply the XF and produce headphone
    and master buffers and do all the various things it does.
    1.  Implement changes to preferences dialog. It will be easier to
        work from the top down -- make the changes, record the changes
        with soundmanger/engine, etc. Do this like the current code
        does, OR (happier version) change current code to not apply
        until user clicks OK. Committing pref changes after a window
        destroy (aka X button) or user cancel makes UI gods unhappy. As
        discussed with Albert, this may be an opportunity to do a bit of
        refactoring of the audio-related (hell, everything in mixxx is
        audio-related, but I know what I mean) preferences. May be a
        required *opportunity* as prefs dialog can't get any bigger than
        the screen of a netbook.
    2.  Engine details. Make sample buffers accessible. Other stuff, as
        it makes itself known. I don't foresee this to be complicated,
        the enginemaster code is relatively short, sweet and modular.
    3.  SOUNDMANAGER\! This will be the loads-of-fun part. Will probably
        require non-trivial refactoring of soundmanager (blah). This was
        the step I started on when I realized I'd rather start on the UI
        part, even if Qt Designer is a total bitch.
2.  DVS mode proper (whatever the hell that is):

<!-- end list -->

  - Make connected to external mixer bit.
  - Vinyl control UI could use work. Random checkbox menu item is
    random, vinyl control ought to be enabled in prefs.
  - Be able to turn off EQs, faders, FX, gains, ...
  - Skin tom foolery. May want to wait until inevitable skin refactor.
    Could take a couple of approaches in the meanwhile:

<!-- end list -->

``` 
    * Make things that don't matter disappear. Of course, since everything is positioned absolutely, no screen real estate is gained, but at least there aren't useless widgets lying around -- just useless space.
    * Load another skin. Either make it user-selectable, or just load CURRENTSKIN-dvs (hacky but user-friendly with a bit of skin hacking on our end).
* Would *love* to have a single timecode deck option.
- Single vinyl deck
* See [[single-deck_vinyl_control]]. Has implementation suggestions.
- Microphone input
* For voice-over. Really has nothing to do with DVS since any mixer worth its salt will have a mic in but mixxx needs it.
```

## Notes

  - DVS mode will probably have negligible effect on CPU usage. Some
    profiling I did
    \[<http://article.gmane.org/gmane.comp.multimedia.mixxx.devel/2998>\]
    seems to indicate the enginemaster stuff (which includes all the
    audio processing) isn't actually all that expensive.
  - Ok, the hifi eq's can eat CPU really well. May be a bug in eq
    though, as it stutters real bad on my system without ever peaking
    out my CPU.
  - [revamped\_control\_system](revamped_control_system) has an
    excellent review of the controlobject system.

### Preferences

  - Currently there's a bunch of different stuff under "Sound Hardware":
  - Audio Output

<!-- end list -->

``` 
    * Master device/channel pair
    * Headphone device/channel pair
    * Sample rate
    * Sound API
* Pitch Behaviour
    * Vinyl emulation or PITS (and disclaimer about PITS)
* Latency
    * Slider -- dynamic. Might be a nicer solution than a slider., as the current one is very jerky so doesn't really represent the continuum a slider implies. Might be nicer to use a combobox since it seems to be a pretty discrete set of values.
```

## Links

  - Branch at (fill me in)
