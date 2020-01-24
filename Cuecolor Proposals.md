Previously, in Mixxx 2.1, cue colors were [stored in the database as an
RGB value](https://github.com/mixxxdj/mixxx/pull/992), however there was
no support for using these colors in skins and controller mappings and
there was no way to set them in the GUI. When support for editing cue
colors was added for Mixxx
2.3[\[1](https://github.com/mixxxdj/mixxx/pull/1830)\][\[2](https://github.com/mixxxdj/mixxx/pull/2016)\],
the database representation was changed to be an integer index in a
hardcoded palette of colors. At this time, a special default "no color"
value was added, in which case the displayed color of a cue depended on
the skin. Using a hardcoded palette turned out to be
[problematic](https://github.com/mixxxdj/mixxx/pull/2119#issuecomment-539347901)
when importing cues from other software, namely Rekordbox, because other
software does not use the same palette as Mixxx. So the decision was
made unanimously to switch back to storing the color as an RGB value.

The present question is whether we should maintain the "no color" state
from the database format that used the hardcoded color palette. That
format was committed to master and used by some developers for some
months, but it was never released.

Open pull requests regarding this:
[\#2345](https://github.com/mixxxdj/mixxx/pull/2345),
[\#2399](https://github.com/mixxxdj/mixxx/pull/2399),
[\#2398](https://github.com/mixxxdj/mixxx/pull/2398)

\======= No special states =======

All hotcues always have a color. There is no "no color"/"default color"
state.

Users can set a single default color that is assigned to newly created
hotcues in the preferences. It will also be possible to define a list of
default colors instead, such that:

  - the first list entry is assigned to a new hotcue at hotcue slot \#1
  - the second list entry is assigned to a new hotcue at hotcue slot \#2
  - ...
  - the nth list entry is assigned to a new hotcue at hotcue slot \#n
  - the first list entry is assigned to a new hotcue at hotcue slot
    \#n+1
  - the second list entry is assigned to a new hotcue at hotcue slot
    \#n+2
  - ...

Since there is no `is_default_color` flag, it is not possible to
distinguish hotcues whose color has been set by the "default color"
preference at creation time and hotcues whose color has been manually
set by the user (e.g. via the Cue Menu Popup).

If the user wants to mass-replace cue colors, a tool will be provided to
replace all cues of one color to a new color.

### Migration

Colors with the "no color" state in the database schema currently in
master will be set to the new default color. Ideally, this would be
"white" since white is not an actual color (and thus transports the
previous "no color" state) and also looks good in all skins.

If a user does not want to use the cue color feature but dislikes the
default color and wants to restore the exact cue button color as in
previous versions of Mixxx, the color-mass-replace tool can be used to
replace the default color with the previous button color of the skin in
use manually.

### Pros & Cons of this approach

#### Pros

  - Trivially simple to implement
  - Trivially simple for users to understand
  - No loss of information with round trip to/from Serato file tags
  - Find-and-replace tool would also be useful if the user wants to
    change the colors of cues they have manually set the color of.

#### Cons

  - By default, the look of hotcue buttons with previously uncolored
    hotcues will change (e.g. red hotcue buttons in the LateNight skin
    will turn white), but the original look can be restored using the
    mass-color-replace tool (see above).
  - Would not maintain "no color" state from Rekordbox. However,
    Rekordbox always shows "memory cues" (what Mixxx calls "hot cues",
    although Rekordbox has a different meaning for "hot cue") as orange.
    That is regardless of the color palette the user has chosen in
    Rekordbox's preferences; changing that color palette does not
    automatically change the colors of cues. It seems that no useful
    information would be lost if Mixxx converts Rekordbox's "no color"
    to orange when importing to Mixxx. It is not clear why the "no
    color" state exists in Rekordbox; it may only exist to support
    legacy CDJs that did not support cue colors. Mixxx currently has no
    way to export to Rekordbox's metadata format, doing so would be
    technically challenging, and no one has expressed interest in
    working on it.
  - Would not maintain "no color" state from VirtualDJ. However,
    VirtualDJ can also read Serato tags, so importing exporting to
    VirtualDJ's metadata format would not be required for
    interoperability with Mixxx if Mixxx can export to Serato tags. To
    import metadata from VirtualDJ, Mixxx would either need to assume
    the color of VirtualDJ's "no color" cues or read [VirtualDJ's
    nonColoredPoi
    setting](https://www.virtualdj.com/manuals/virtualdj/interface/decks/decksadvanced/pads.html)
    to determine how VirtualDJ would show them. Without Mixxx
    maintaining a "no color" state, cues imported from VirtualDJ and
    exported back to VirtualDJ (potentially through Serato tags) would
    lose the "no color" state and not change colors when the user
    changes the nonColoredPoi setting in VirtualDJ.
