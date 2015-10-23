# Contributing Mappings

Making a mapping for a controller is a great way to contribute to Mixxx
for users who have some technical skill but do not know C++. Controller
mappings are written in
[XML](MIDI%20controller%20mapping%20file%20format) and
[JavaScript](MIDI%20scripting). While mappings can be made with just
XML, most controllers will require some JavaScript to make a complete
mapping. Both XML and JavaScript are fairly straightforward and easy to
learn. Using JavaScript to map your controller could be a good
introduction to programming. If you are unfamiliar with MIDI, see the
[MIDI Crash Course](MIDI%20Crash%20Course) page.

## Setting up Git

We use Git for coordinating Mixxx development which is software that
helps keep track of changes in files. Before you start working on your
mapping, set up git on your computer. Using git will help you keep track
of your progress on the mapping and help Mixxx developers review it.
Start by creating a [GitHub](http://github.com/) account and [forking
Mixxx](https://github.com/mixxxdj/mixxx). On GNU/Linux and Mac OS X, you
can directly work on your mapping in your git repository. Mixxx
automatically reloads JavaScript mapping files when they are changed, so
you can work on the JS part of the mapping while running Mixxx to test
your changes. To do this, delete the `controllers` directory in your
user preferences folder (backup any work in progress that you do not
want to lose first\!) and make a symbolic link to the `res/controllers`
directory in your git repository. For example, if your git repository is
under the "software" directory in your home directory on GNU/Linux, run:

`ln -s ~/software/mixxx/res/controllers ~/.mixxx/controllers`

Make a new git branch (run `git checkout -b new_branch_name` from within
your git repository). Make changes to your mapping and commit them when
your changes work. Before making any commits, configure git to use your
name and email in your commits. See the [Using Git](Using%20Git) wiki
page for more information. Please prefix your git commit messages with
the name of your controller so others can easily tell what the commits
are for after your changes are merged.

When your mapping is complete and you are ready to submit your mapping
for inclusion in Mixxx, make a pull request on GitHub. If this is your
first contribution to Mixxx, you will be asked to sign the contributor
agreement. This agreement gives the Mixxx team permission to distribute
your mapping with Mixxx under the GNU GPL v2 license with an exception
allowing it to be distributed in the Mac App Store provided that the
source code is made available on the Mixxx website under the GPL.

## Documenting the mapping

Post [on the forum](http://mixxx.org/forums/viewforum.php?f=7) early so
users can find your mapping and give feedback as you develop it. Also,
list your controller on the [DJ Hardware
Guide](hardware%20compatibility#mappings%20in%20development) and start a
wiki page for your controller. To make a wiki page, put double brackets
around the name of your controller in the Hardware Guide, for example
\[\[My Controller\]\]. Save your edit to the Hardware Guide page, then
click on the red link in the Hardware Guide to create the new page. Add
a picture of the controller (use the syntax {{URL to picture}} to embed
a picture), a link to the manufacturer's website, a brief description, a
link to the forum thread, and links to some reviews of the controller.

Please complete the wiki page with labeled diagrams explaining how your
mapping works. In addition to helping users, this helps developers who
do not own the controller to review the mapping. If there is no diagram
readily available, ask the manufacturer for one. If they do not provide
one, take pictures of your device and label them. Upload diagrams and/or
pictures by going to the [Media Manager](?do=media) at the top right of
any wiki page and upload your file(s) to the "hardware" namespace. SVG
diagrams are preferred because they are easier to edit later.

## Design guidelines

These are all general guidelines to keep in mind when making your
mapping. They are not strict rules.

If your controller was specifically designed for DJing and has labels on
the controls, make your mapping do what the labels say. However, you do
not need to exactly follow the labels or mappings the manufacturer made
for other software if you think there is a better way to map it or their
mapping does not make sense with Mixxx. You are encouraged to map
additional features not included in the manufacturer's mappings. If you
are mapping a controller designed for a purpose other than DJing or a
controller without labels designed to be mapped in creative ways, try to
make your mapping have enough features that the controller could be used
alone without needing another controller to fully control Mixxx. If
there are not enough physical controls on the device to make that
practical, do not try to make such a complicated mapping that it is
difficult to use.

Controllers should not be made to blink LEDs for an extended period of
time. If you would like to implement a feature that blinks LEDs, make it
an option that users can easily disable. Define a boolean variable at
the very top of your JavaScript file that users can change to `false` to
disable the blinking or `true` to enable it. Put a comment next to the
variable definition explaining what the variable does and how to change
it.
