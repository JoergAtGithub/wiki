# Single-Deck Vinyl Control

## Summary and Rationale

**Status**: This feature is implemented in Mixxx v1.11.

Allow both players to be controlled via a single turntable with vinyl
control. At least one commercial DJ application offers this feature, and
Mixxx would be more competitive with it.

## Use Cases

  - DJ Fred only has one turntable but wants to use Mixxx's vinyl
    control feature. He needs a way to control both players with a
    single timecoded vinyl.
  - DJ Laura is thinking about buying turntables and wants to experiment
    with vinyl control first. However, her parents have an old record
    player in her basement and she wants to see what it's like with
    Mixxx.

## Design

#### Toggling Between Players

  - How does Mixxx know which player should be controlled by the
    timecoded vinyl?

Single deck mode works by setting both decks to use the same audio
input. The DJ then alternates activating vinyl control on one deck, then
the other. This feature is designed so that when deck control is
disabled, playback continues without interruption.

It is theoretically possible to mess up and activate vinyl control for
both players, and thus have vinyl input affect two decks at once, but in
practice it's easy to turn off control on one deck, and on on the other.

It is also possible to forget that you've changed the pitch on the
turntable, and reenable control on an old deck. The playback speed
suddenly changes, with disastrous DJ-fail results. Just don't do that.

#### Indicating Active Deck

With the new vinyl code, there is a special vinyl status light that can
indicate much important state information. A solid green indicates
"active," for instance. With single deck mode, the DJ looks for which
deck has an active indicator lit. The indicators should be large and
prominent, making it easy to see at a glance which deck is active.

#### Preferences Dialog Considerations

  - Setting up single-deck mode is as simple as choosing the same sound
    device as the input for both decks. There is no special "single
    deck" button needed.

#### Internal Changes

1.  I enabled the ability for two decks to share an input
2.  I added enable/disable buttons for each deck
3.  I ensured that playback would continue once vinyl control was turned
    off

Basically I rewrote a lot of stuff.

## Team

If you're interested in helping to code this feature, sign up your name
below:

  - Owen Williams (is actively working on this issue in his tree:
    lp:\~ywwg/mixxx/features\_xwax2)
