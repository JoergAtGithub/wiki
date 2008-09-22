# Single-Deck Vinyl Control

## Summary and Rationale

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

Allow both players to be controlled via a single turntable with vinyl
control. At least one commercial DJ application offers this feature, and
Mixxx would be more competitive with it.

## Use Cases

  - DJ Fred only has one turntable but wants to use Mixxx's vinyl
    control feature. He needs a way to control both players with a
    single timecoded vinyl.
  - DJ Jill wants to switch to Mixxx from djDecks, but can't do so
    because she needs single-deck vinyl control.
  - DJ Laura is thinking about buying turntables and wants to experiment
    with vinyl control first. However, her parents' have an old record
    player in her basement and she wants to see what it's like with
    Mixxx.

## Design

#### Toggling Between Players

\* How does Mixxx know which player should be controlled by the
timecoded vinyl?

> Via a button on the interface and/or hotkeys. When it's depressed,
> that player receives timecode signals.

#### Preferences Dialog Considerations

  - There should probably be some "single-deck mode" checkbox in the
    vinyl control preferences that greys out the second input combo
    boxes and enables this feature. Whatever the prefs dialog
    modifications end up being, they're probably contingent on the
    "Toggling Between Players" design above.

#### Internal Changes

In soundmanager.cpp, specifically in SoundManager::setupDevices(), there
is the following snippet:

``` 
    //Initialize vinyl control
    m_VinylControl[0] = new VinylControlProxy(m_pConfig, "[Channel1]");
    m_VinylControl[1] = new VinylControlProxy(m_pConfig, "[Channel2]");
```

Each physical turntable's audio gets passed off to a VinylControlProxy
object to be processed. The VinylControlProxy/xwax/scratchlib object
then manipulates Mixxx's internal pitch and playback position. The
channel string parameter tells each VinylControlProxy object which
player it should be connected to. From that string, the VinylControl
class constructor grabs "ControlObjects" which allow it to hook into
Mixxx's various internal controls. For example, inside the
`VinylControl::VinylControl(...)` constructor, you will see:

    playPos             = new ControlObjectThread(ControlObject::getControl(ConfigKey(group, "playposition")));    //Range: 0.0 to 1.0

That "playPos" object then allows the VinylControl object change the
playback position (eg. when needle dropping) for the player specified by
"group" (which would be \[Channel1\] or \[Channel2\]).

In order to allow a single deck to control either player/channel, one
could modify VinylControl/Proxy and allow it to get the ControlObjects
for the other channel (this is the hard approach). An **easier
approach** is to keep all the VinylControl objects the way they are, and
to simply route the audio to the correct VinylControlProxy object
depending on whichever player is supposed to be controlled.

The starting point for this way would be to look at SoundManager again:

    CSAMPLE * SoundManager::pushBuffer(QList<AudioReceiver> recvs, short * inputBuffer,
                                        unsigned long iFramesPerBuffer, unsigned int iFrameSize)

This `SoundManager::pushBuffer()` function gets called when a soundcard
has given Mixxx (input) audio to be processed, like from a timecoded
vinyl. Near the end of the function, you'll see the code:

``` 
        QListIterator<AudioReceiver> devItr(recvs);
        while(devItr.hasNext())
        {
            AudioReceiver recv = devItr.next();
            if (recv.type == RECEIVER_VINYLCONTROL_ONE)
            {
                //recv.channelBase
                Q_ASSERT(recv.channels == 2); //Stereo data is needed for vinyl control
                if (m_VinylControl[0])
                    m_VinylControl[0]->AnalyseSamples(vinylControlBuffer1, iFramesPerBuffer);
            }
            if (recv.type == RECEIVER_VINYLCONTROL_TWO)
            {
                Q_ASSERT(recv.channels == 2); //Stereo data is needed for vinyl control
                if (m_VinylControl[1])
                    m_VinylControl[1]->AnalyseSamples(vinylControlBuffer2, iFramesPerBuffer);
            }
        }
```

This code demonstrates of how the "routing" of the input audio works.
Each SoundDevice object has a list of AudioReceivers in it, which you
can think of as the things that it's going to pass its input audio to.
In this code snippet, you can see that if the SoundDevice has an
AudioReceiver of type RECEIVER\_VINYLCONTROL\_ONE, then that audio will
be passed off to the first VinylControlProxy object and it will control
the first player. If we want single-deck vinyl control, we need to
modify the list of AudioReceivers inside a SoundDevice at runtime so the
soundcard controls the desired player.

If you look at SoundDevice.cpp, it looks like you can do this with
`SoundDevice::addReceiver()` and `SoundDevice::clearReceivers()`. This
is roughly the end of the string here. **As a starting point, look at
`SoundManager::setupDevices()` and check out the `addReceiver()` calls
in there.**

## Work Breakdown

This [work breakdown
structure](http://en.wikipedia.org/wiki/Work_breakdown_structure) (WBS)
outlines the work that needs to be done to complete this feature:

``` 
1. Single-deck vinyl control
  1.1 Assess existing vinyl control code
    <del>1.1.1 Write internal changes section for wiki</del>
    1.1.2. Figure out how exactly we want to make control switch from one player to another.
  1.2 Modify existing vinyl control code
    1.2.1 Read from crossfader (or whatever) ControlObject to determine which player to control.
    1.2.2 Change the AudioReceiver for the soundcard that's opened for input, depending on which player should be controlled. 
  1.3 Modify preferences dialog
    1.3.1 Add single-deck vinyl control checkbox
    1.3.2 Make the checkbox grey out the second input comboboxes. 
```

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - Josh Matthews
