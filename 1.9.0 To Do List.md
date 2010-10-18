# Things to do for v1.9.0

[Open bugs targeted
for 1.9.0](https://bugs.launchpad.net/mixxx/+bugs?field.searchtext=&orderby=status&search=Search&field.status%3Alist=NEW&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.milestone%3Alist=23685&field.tag=&field.tags_combinator=ANY&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on)

### Vinyl control

  - Integrate the latest xwax release code. See
    <https://code.launchpad.net/~ywwg/mixxx/features_xwax2>

### MIDI Sub-system

  - Replace MidiCategory with MidiStatusByte permanently (see
    mididevice.cpp line 242.)
  - GUI changes:

<!-- end list -->

``` 
    * Persistent mapping preset drop-down (don't return to "..." unless Clear All is pressed. If the user tweaks the mapping, say "<custom>" or something.)
    * Also clear the list of MIDI scripts when Clear All is pressed
    * Do not commit changes to the MIDI mapping tables unless OK is pressed in the preferences window. (I.e. allow pressing the Cancel button or the X on the preferences window to restore the MIDI mappings to their previous states.)
```

### Engine

  - Position-based scratching (as opposed to the current
    velocity-based.) Script use cases:
    1.  Relative: Tell the Engine to move the track X seconds
        forward/backward over Y seconds of real time. The engine will,
        without affecting play status, play all the samples between the
        current and target positions in the specified time (stretching
        as needed) and fire a signal when it's there, optionally holding
        at the target position until given further instruction. It must
        also queue requests so it ends up at the correct position.
    2.  Absolute: Tell the Engine to move to absolute time X (in elapsed
        or remaining seconds) over Y seconds of real time. Otherwise
        same behavior as above.

### Testing

  - Update sound file test script in src/test/soundFileFormats to
    include M4A file generation
  - Test MP3/M4A/OGG/FLAC/WAVs of varying sample rates [and report
    results here](sound%20file%20testing%20matrix)
  - Add MIDI controller mappings [from the
    forums](http://www.mixxx.org/forums/viewforum.php?f=7) to the
    branch.
  - [Test MIDI mappings](Supported%20Controller%20Test%20Grid) for
    correct functionality for as many currently supported controllers as
    we can
  - Update the [Wikipedia entry](http://en.wikipedia.org/wiki/Mixxx)
  - Update [user manual](manual)
