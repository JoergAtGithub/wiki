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

Note that the process and guidelines outlined on this page are a work in
progress. They will be updated as we learn from reviewing more mappings.

## Setting up Git

We use Git for coordinating Mixxx development. Git is software that
helps keep track of changes in files. Before you start working on your
mapping, set up git on your computer. Using git will help you keep track
of your progress on the mapping and help Mixxx developers review it.
Start by creating a [GitHub](http://github.com/) account, [forking
Mixxx](https://github.com/mixxxdj/mixxx), and cloning your fork onto
your computer.

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

### Working on your mapping in your git repository

In GNU/Linux and Mac OS X, you can directly work on your mapping in your
git repository. Mixxx automatically reloads JavaScript mapping files
when they are changed, so you can work on the JS part of the mapping
while running Mixxx to test your changes. To do this, delete the
`controllers` directory in your user preferences folder (backup any work
in progress that you do not want to lose first\!) and make a symbolic
link to the `res/controllers` directory in your git repository. For
example, if your git repository is under the "software" directory in
your home directory on GNU/Linux, run:

`ln -s ~/software/mixxx/res/controllers ~/.mixxx/controllers`

## Documenting the mapping

Post [on the forum](http://mixxx.org/forums/viewforum.php?f=7) early so
users can find your mapping and give feedback as you develop it. For new
mappings, list your controller on the [DJ Hardware
Guide](hardware%20compatibility#mappings%20in%20development) and start a
wiki page for your controller. To make a wiki page, put double brackets
around the name of your controller in the Hardware Guide, for example
\[\[My Controller\]\]. Save your edit to the Hardware Guide page, then
click on the red link in the Hardware Guide to create the new page. Add
a picture of the controller (use the syntax {{URL to picture}} to embed
a picture), a link to the manufacturer's website, a brief description, a
link to the forum thread, and links to some reviews of the controller.

If you are not very comfortable writing English, do not worry. Do your
best to write a description of the mapping on the wiki page and someone
who knows English better can work on your writing. You are also
encouraged to translate the wiki page into your native language.

Please complete the wiki page with labeled diagrams explaining how your
mapping works. In addition to helping users, this helps developers who
do not own the controller to review the mapping. If there is no diagram
readily available, ask the manufacturer for one. If they do not provide
one, take pictures of your device and label them. Upload diagrams and/or
pictures by going to the [Media Manager](?do=media) at the top right of
any wiki page and upload your file(s) to the "hardware" namespace. SVG
diagrams are preferred because they are easier to edit later.

If you are submitting a substantially updated mapping for a controller
that already has a mapping in Mixxx, create a new section on the
controller's wiki page to describe your new mapping. When your pull
request is merged, delete the description of the old mapping from the
wiki page.

## File naming convention

Please name your mapping files according to these conventions before
making a pull request to have your mapping included in Mixxx.

XML MIDI mapping files use the naming convention `{manufacturer}
{device}.midi.xml`, for example `Stanton SCS3d.midi.xml`. XML HID
mapping files use the convention `{manufacturer} {device}.hid.xml`, for
example, `Hercules DJ Console RMX.hid.xml`. JavaScript files use the
naming convention `{manufacturer}-{device}-scripts.js`, for example
`Stanton-SCS3d-scripts.js`.

## Windows Installer Update

If you add new files to the controller mappings, don't forget to update
the Windows installer to uninstall these files when uninstalling Mixxx.
You have to add your files to the list in the build/nsis/Mixxx.nsi file
here:
<https://github.com/mixxxdj/mixxx/blob/master/build/nsis/Mixxx.nsi#L394>

## Design guidelines

These are all general guidelines to keep in mind when making your
mapping. They are not strict rules.

If your controller was specifically designed for DJing and has labels on
the controls, make your mapping do what the labels say. However, you do
not need to exactly follow the labels or mappings the manufacturer made
for other software. If you think there is a better way to map it or the
manufacturer's mapping does not make sense with Mixxx, map it how you
think it should be. You are encouraged to map additional features not
included in the manufacturer's mappings. If you are mapping a controller
designed for a purpose other than DJing or a controller without labels
designed to be mapped in creative ways, try to make your mapping have
enough features that the controller could be used alone without needing
another controller to fully control Mixxx. If there are not enough
physical controls on the device to make that practical, do not worry
about it too much.

If you want to create options that users can easily customize, define
variables that control those options at the very top of your JavaScript
file with comments explaining how to set the options. Also explain how
to set these options on the wiki page for your controller.

Mappings should not blink LEDs for an extended period of time. If you
would like to implement a feature that blinks LEDs, make it an option
that users can easily disable. Define a boolean variable at the very top
of your JavaScript file (before any code or other comments) that users
can change to `false` to disable the blinking or `true` to enable it.
Put a comment above the variable definition explaining what the variable
does and how to change it.

Use the play\_indicator and cue\_indicator
[MixxxControls](MixxxControls) to illuminate play and cue button LEDs.
The behavior of these Mixxx Controls changes according to the cue mode
selected by the user in the preferences.

Mapping multiple controls (shift functions) to faders and knobs is
confusing to use. If you can, try to think of another way to map the
alternate function. This is generally not an issue with encoders that
rotate infinitely, buttons, pads, or touch strips.

## Coding conventions for Javascript

Javascript is a very flexible programming language. It has some good
features JavaScript, but there are also a number of features that have
confusing syntax and/or encourage bad programming practices. Using these
features makes it easier for bugs to go unnoticed in your code.

These coding conventions are mandatory for new Javascript code in Mixxx:

  - Do not write one-line `if` statements.
  - Always use brackets for `if` statements. Put the opening `{` on the
    same line as the conditional expression and the closing bracket `}`
    on its own line.
  - Put `else` statements on the same line as the previous closing `}`
  - All code lines that need it must end with `;`
  - Always put `var` before variable declarations to avoid accidentally
    declaring global variables
  - Do not use `==` and `!=` because these can have unexpected effects
    when comparing variables of different types. Use `===` or `!==`
    instead. If they generate errors it should be fixed in the Mixxx
    Javascript engine, not in Javascript code.
  - Use camelCase more than C-style this\_is\_variable.
  - Use 4 spaces to indent, not tab characters
  - `new` must be used when creating new objects or if JShint is fine
    with then it is OK.
  - Capitalize the first letter of constructor functions

Here is an example of good Javascript style:

    var someObject = new ShinyObject();
    
    ShinyObject.someMethod = function () {
        var someVariable = 0;
        if (something === another) {
            someVariable++;
        } else {
            someVariable--;
        }
        return someVariable;
    }

### Code checking tools

We use the automated code testing tools [JSHint](http://jshint.com/) and
[JSBeautifier](http://jsbeautifier.org/) that check for bad practices in
Javascript code. Using these tools is not for making your coding skill
look bad. They are to help you make your code even better and you
already have the basics taken care of when you create a pull request.

All Javascript files for Mixxx must start with header to make sure
JSHint doesn't gnerate errors for missing variables:

``` 
////////////////////////////////////////////////////////////////////////
// JSHint configuration                                               //
////////////////////////////////////////////////////////////////////////
/* global engine                                                      */
/* global script                                                      */
/* global print                                                       */
/* global midi                                                        */
//////////////////////////////////////////////////////////////////////// 
```

## Coding conventions for XML

Use [LibXML2](http://xmlsoft.org/)'s xmllint tool to format your XML
code. You can also use [this online
tool](http://www.freeformatter.com/xml-formatter.html) (with '2 spaces
per indent level').

Organize the order of the \<control\> and \<output\> elements in some
way that makes sense; do not keep it in the order that happened to be
autogenerated by Mixxx's MIDI Learning Wizard. In most cases, sorting by
MIDI note numbers is appropriate. This makes it easier to edit later.

For example:

    <?xml version="1.0" encoding="utf-8"?>
    <MixxxControllerPreset mixxxVersion="1.12.0+" schemaVersion="1">
      <info>
        <name>Manufacturer Product-100</name>
        <author>Template Author</author>
        <forums>http://www.mixxx.org</forums>
        <wiki>http://mixxx.org/wiki/doku.php</wiki>
      </info>
      <controller id="Manufacturer Product-100">
        <scriptfiles>
          <file filename="Manufacturer-Product-100-scripts.js" functionprefix="ManufacturerProduct100"/>
        </scriptfiles>
        <controls>
          <!-- Comment -->
          <control>
            <group>[Channel1]</group>
            <midino>0x01</midino>
            <status>0xB0</status>
            <key>play</key>
          </control>
          <control>
            <group>[Channel1]</group>
            <midino>0x02</midino>
            <status>0xB0</status>
            <key>pfl</key>
          </control>
        </controls>
        <outputs>
          <!-- Use play_indicator control object rather than play -->
          <output>
            <group>[Channel1]</group>
            <key>play_indicator</key>
            <status>0x90</status>
            <midino>0x01</midino>
            <on>0x7F</on>
            <off>0x00</off>
            <minimum>0.5</minimum>
          </output>
          <!-- PFL -->
          <output>
            <group>[Channel1]</group>
            <key>pfl</key>
            <status>0x90</status>
            <midino>0x02</midino>
            <on>0x7F</on>
            <off>0x00</off>
            <minimum>0.5</minimum>
          </output>
        </outputs>
      </controller>
    </MixxxControllerPreset>
