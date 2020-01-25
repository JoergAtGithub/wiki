**color cues**

In Mixxx 2.3 alpha the user can explicit select "no color" for hot cues.
This state adds some complexity to the cue color feature and is
unnatural for the user and unhandy for skins and mappings.

That's why we have decided to drop the "no color" state in the revamped
implementation.

However, the "no color" state is already there, if we migrate hot cues
from Mixxx 2.2, Recordbox and VirtualDJ. So we need to decide how to do
this migration from this "no color" state to a model that does not have
it.

Each possible solution has implications to the usability and possible
use cases. So let's have look on them

**Use Cases**

**1 Color = Cue Type**

This is the mayor use case of the color feature. Users may give a color
a meaning and color the cues accordingly. The user will probably start
with one meaning and a color that indicates it. The user may for
instance use Yellow fro "Bridge End" and use it for some tracks. All
other existing cues and and new cues set in Mixxx will left default.
This will change step by step for every track which is prepared and
every new meaning which is defined. Especially with large libraries this
will likely never be finished. All default cue are displayed with a
color that has the fixed meaning "meaning undecided".

The user may decide which color is used for the "meaning undecided" or
"default" state, because a color picked by the developers may have
already a different meaning for the user, using other tools side by side
with Mixxx.

**2 Colored controllers**

The user does not have a concept like in use case 1) he just want make
use of the color feature to distinguish cue buttons from other buttons
on his controller.

He might not be confident with the color picked by the developers during
migration, because the color might be already in use for other features
in the mapping. So the user may wish to select the color he is used to
from Mixxx 2.2 or other tools.

Traktor uses Green for Hotcues and older CDJs are using Orange.

**3 Number = Cue Type**

On systems without colored cue buttons it is common to use the cue
number as type. This way a "Bridge End" cue is always on the same
position and easy accessible for every track. If the user decided to
support that by color, he will give each cue number a special color.

This is default in Serato and Engine Prime.

**4 Color by deck**

This is useful for hardware or Gui implementation where the button /
Deck assignment is unclear or switchable. It can also be a design
aspect. This can be used for example for a drum pad like use case from
different tracks.

VirtualDJ has this feature.

**5 No use (Skin default)**

For users migrating from Mixxx 2.2, new cue button color might be
distracting since the selected default color may look foreign. Here it
would be nice, if we allow to keep the original Mixxx 2.2 colors and not
bother the user until he is ready to use cue colors.

This is the default for hot cues in current Mixxx master.

This feature works well only if the controller has no colored hot cue
pads, because the skin default may look ugly on controllers. Once a
controller with colored cue buttons is present the user may swith to use
case 2)

**6 Use Recordbox cues**

Recordbox users want to use an USB stick with Mixxx and Recordbox and
their CDJ. It can be expected that all the features working, without
loosing the memory cue / hot cue separation and the "no color" state of
the cues during using the stick on different systems.

Moving memory cues are to hotcue buttons or wise versa, after editing
the memory stick with Mixxx is not probably also not acceptable.

**7 R/W cues to file Metadata**

Serato saves cue info into file metadata. Users may want to read an
write this data to exchange cue info with Serato or other software able
to read this data.

In case of third party tracks a color mapping is essentially.

**8 Sharing of cue points**

User may want to share metadata with other databases. The other database
may have colored cue or not. In most of them (like aoide), cue colors
are optional. The user liked to have control how colors are
imported/exported. A color mapping is Required to not mess up the color
scheme or palette of the sharing pair.

**9 Migrating cues + palette**

When moving from other tools the user might want to continue the palette
from the other tool. Here Mixxx need to replace the build in platte with
the external one. The user may wish to adopt colors from the existing
cues to the new palette. This is required to keep the colors
distinguishable. Mixxx's default palette is optimized for being
distinguishable. If tracks with off palette colors are imported the
colors may become ambiguous, which might be undesired.

**Migration Strategy**

Coming from Mixxx 2.2 all cues have skin defined colors. We should allow
to migrate to any of the above use cases without mayor quirks and at any
time.

In the meantime we need to decide for an intermediate solution that does
not prevent using one of the desired use cases. We may also consider to
allow changing the use case after a longer period if using.

The intermediate solution should not be disacting, in a way that's the
user cannot continue Mixxx as usually after update to 2.3. For instance,
a migration dialog is undesired.

**One possible solution**

One possible solution is implemented in
<https://github.com/mixxxdj/mixxx/pull/2398>

It uses black (0) in the database color as indicator that the user has
not selected a color. This color is replaced on the fly with the
selected default, which can be off palette color to keep the
intermediate state or plette color which replaces the 0 color in the
database color as well. The 0 replacement is an implementation detail of
the DAO class. For the rest of Mixxx and from the user perspective cues
have always a color.

The user has the option to select a palette color for default (1;2) if
he likes to get immediately rid of the default state. He may alternative
select the skin color (default), a off palette default color or cue
color by number, if he wants to postpone the decision of a suitable
default color.

**Other solution**

Other solutions are possible. Here some ideas:

We may use a useful color e.g.: orange or white during "no color" cues
migration. Since Mixxx is able to distinguish the selected default color
form other colors different use cases are still possible. This can be
also used to treated also as "no color" for the Recordbox roundtrip.

If a user likes cue by color or skin color 3)/4)/5) we can simply ignore
the color saved in the database.

A mass replace solution will also allow most if the cases above. Hover
we should keep in mind that we migrate to alternative colors first
before swapping colors. This might take some time especially in case of
aoide where cues are track properties or if the cue colors are saved in
file tags.

In case of file tags we may save an additional cue at an invisible
position that indicates the default color.

**Conclusion**

For every proposed solution, we may consider the impact on the use cases
above. Finally we will have a good solution.
