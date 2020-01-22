## No special states

All hotcues always have a color. Colors with the "no color" state in the
database schema currently in master will be set to the new default
color.

Pros:

  - Trivially simple to implement
  - Trivially simple for users to understand
  - No loss of information with round trip to/from Serato file tags

Cons:

  - When users change default cue color preference, Mixxx would need to
    do a mass find-and-replace if the user wants to update their old
    cues to the new setting. This database operation might be a bit
    slow, but this remains to be seen as it has not been implemented
    yet. Regardless, the potentially slow operation would only occur
    when changing the setting in the preferences window.
  - Would not maintain "no color" state from Rekordbox. The workaround
    is to set the "no color" cues from Rekordbox to how they appear by
    default in Rekordbox. It is not entirely clear how Rekordbox uses
    this "no color" state; it may only exist to support legacy CDJs that
    did not support cue colors. Mixxx currently has no way to export to
    Rekordbox's metadata format, doing so would be technically
    challenging, and no one has expressed interest in working on it.
  - Would not maintain "no color" state from VirtualDJ. However,
    VirtualDJ can also read Serato tags, so importing from/exporting to
    VirtualDJ's metadata format would not be required for
    interoperability with Mixxx if Mixxx can export to Serato tags.
