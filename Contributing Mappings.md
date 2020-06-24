# Contributing Mappings

The more choice users have for devices to use with Mixxx, the better.
There are many DJ controllers on the market and most of them aren't very
cheap. The Mixxx developers do not have resources to get every
controller out there and map it, so the community generally relies on
users to contribute mappings. We try to make mapping as easy as
possible, but making a complete mapping typically takes some technical
skill beyond what many users have. So, getting a controller that doesn't
have a Mixxx mapping yet and making a mapping is a great way to
contribute to Mixxx if you have some technical skill but may not know
C++.

Controller mappings are written in
[XML](MIDI%20controller%20mapping%20file%20format) and
[JavaScript](MIDI%20scripting). While mappings can be made with just
XML, most controllers will require some JavaScript to make a complete
mapping. Some controllers will require a mapping mostly or completely
written in JavaScript. Both XML and JavaScript are fairly
straightforward and easy to learn. Using JavaScript to map your
controller could be a good introduction to programming. If you are
unfamiliar with MIDI, refer to the [MIDI Crash
Course](MIDI%20Crash%20Course) page.

For someone with prior programming experience, writing an initial
mapping for a controller can be done in a few days. However, you will
likely want to change some of your initial design decisions as you use
the mapping, especially if you do not have much experience using DJ
controllers. Refining the design is a gradual process that takes
experimentation and revising. You are encouraged to seek feedback from
users on the [Mixxx forum](http://mixxx.org/forums/viewforum.php?f=7) as
you develop the mapping.

The processes and guidelines on this page are to ensure that new
mappings included in Mixxx are quality, complete, and documented. This
gives users the most choice and the ability to make their own informed
decisions about what equipment to get for using Mixxx.

This page is a continual work in progress and is updated as we learn
from reviewing more mappings.

## Using Git with your mapping

### Setting up Git

We use Git for coordinating Mixxx development. Git is software that
helps keep track of changes in files. Before you start working on your
mapping, it is recommended (but not necessary) to set up git on your
computer. Using git will help you keep track of your progress on the
mapping and help Mixxx developers review it. If you have already
finished your mapping, that's okay, just add your finished mapping files
in one commit. Start by creating a [GitHub](http://github.com/) account,
[forking Mixxx](https://github.com/mixxxdj/mixxx), and cloning your
forked git repository onto your computer.

Make a new git branch (run `git checkout -b new_branch_name` from within
your git repository). Make changes to your mapping and commit them when
your changes work. Before making any commits, configure git to use your
name and email in your commits. See the [Using Git](Using%20Git) wiki
page for more information. Please prefix your git commit messages with
the name of your controller so others can easily tell what the commits
are for after your changes are merged. For example, a good commit
message could look like:  
`Hercules P32: push browse encoder to maximize/minimize library`

#### Working on your mapping in your git repository

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

#### Working on your mapping and other branches simultaneously

Refer to instructions on the [Using
Git](Using%20Git#Working%20on%20mappings%20and%20skins%20separately%20from%20other%20changes)
page.

### Submitting your mapping for review

When your mapping is complete, [documented on the
wiki](#Documenting-the-mapping), and you are ready to submit your
mapping for inclusion in Mixxx, make a pull request on GitHub. Make sure
that the target branch of mixxxdj/mixxx for your pull request is the
branch that you started your git branch from (if it isn't, you'll see
commits unrelated to your mapping included in your pull request).

Although we try not to let pull requests linger without review, keep in
mind that Mixxx is a volunteer project and someone will review your pull
request when they have time available. Mappings will be reviewed to
check that they follow the
[\#design-guidelines](#design-guidelines),-[\#coding-conventions-for-JavaScript](#coding-conventions-for-JavaScript),-[\#coding-conventions-for-XML](#coding-conventions-for-XML),-to-check-that-the-mapping-is-[documented
well on the wiki](#documenting-the-mapping), and to look for potential
bugs. To update your mapping in response to reviewers' comments, edit
your file(s), make a new git commit, and push your git commit. The new
commit(s) will automatically show up in the pull request.

### After your mapping is merged

You are encouraged to join the
[Mixxx-devel](https://lists.sourceforge.net/lists/listinfo/mixxx-devel)
email list to stay involved with Mixxx and keep your mapping up to date
with new Mixxx features.

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

You do not need to explain how Mixxx works; explain how the controller
affects Mixxx. Feel free to link to the [Mixxx
manual](http://mixxx.org/manual/latest/). For example, to document a
sync button, you do not need to explain how master sync works; just
write that the button toggles master sync.

If you are not very comfortable writing English, do not worry. Do your
best to write a description of the mapping on the wiki page and someone
who knows English better can work on your writing. You are also
encouraged to write the wiki page in your native language in addition to
English. You can translate a wiki page by clicking the button for your
language at the bottom right of the wiki page.

Please complete the wiki page with labeled diagrams explaining how your
mapping works. Look at the pages for other controllers on the [DJ
Hardware Guide](hardware%20compatibility#controller%20mappings) for
examples (many controllers are not documented. Contributing a new,
documented mapping helps fix that =) ). In addition to helping users,
this helps developers who do not own the controller to review the
mapping. If there is no diagram readily available, ask the manufacturer
for one and permission to upload it to the Mixxx wiki. If they do not
provide one, take pictures of your device and label them. Upload
diagrams and/or pictures by going to the [Media Manager](?do=media) at
the top right of any wiki page and upload your file(s) to the "hardware"
namespace. SVG diagrams are preferred because they are easier to edit
later. If the manufacturer only provides a PDF diagram, you can open the
PDF in [Inkscape](https://inkscape.org/) to convert it to SVG and label
it.

If you are submitting a substantially updated or different mapping for a
controller that already has a mapping in Mixxx, create a new section on
the controller's existing wiki page to describe your new mapping. When
your pull request is merged, delete the description of the old mapping
from the wiki page if your mapping replaces the old one.

### Microphone inputs

Some controllers have integrated microphone inputs. On some devices, the
input signal is available to the computer, but on others it is not.
Which way the device works is important to users who want to record or
broadcast and should be documented on the controller's wiki page. You
can test out whether the microphone input is available to the computer
by going to Mixxx's Sound Hardware preferences, clicking the Input tab,
and check whether the controller's sound card appears as an option for
inputs to select.

When the input signal is not available to computer, it is mixed in
hardware with the main output without being digitized and routed to the
computer. This has the advantage of not introducing the latency of
routing the signal through an analog-to-digital converter, through the
computer, and back out through the sound card's digital-to-analog
converter (and saving the manufacturer the expense of putting an
analog-to-digital converter in thousands of devices). However, users
cannot record or broadcast using the microphone input on the controller.
They would have to plug the microphone into a different sound card to
record or broadcast the microphone signal. The sound card built into
computer motherboards often has one microphone input jack, typically a
1/8" TS or TRS jack, often colored pink and labeled with a microphone
icon, that can be used for this purpose.

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
You have to add your files to the list in the
[build/nsis/Mixxx.nsi](https://github.com/mixxxdj/mixxx/blob/master/build/nsis/Mixxx.nsi#L394)
file in the Mixxx source tree. If you are updating a mapping that is
already in Mixxx, this is not necessary.

## Design guidelines

These are all general guidelines to keep in mind when making your
mapping. They are not strict rules.

If your controller was specifically designed for DJing and has labels on
the controls, make your mapping do what the labels say. However, you do
not need to exactly follow the labels or mappings the manufacturer made
for other software. If you think there is a better way to map it or the
manufacturer's mapping does not make sense with Mixxx (or just does not
make sense), map it how you think it should be. You are encouraged to
map additional features not included in the manufacturer's mappings,
*but not at the expense of excluding functionality the controller is
labeled for*.

Focus your mapping on functionality that is useful to have easy, quick
access to while mixing. It is okay to leave parts of Mixxx unmapped that
are not changed frequently while mixing; you do not need to map
everything. The user can still use their mouse and keyboard to access
functions not mapped on the controller.

### User configurable options

If you want to create options that users can easily customize, define
variables that control those options at the very top of your JavaScript
file with comments explaining how to set the options. Also explain how
to set these options on the wiki page for your controller.

Try to add as few options as necessary. If you think you should add more
options, reconsider your design first. Only use an option where there is
not one best way to do it.

### Blinking LEDs

Mappings should not blink LEDs for an extended period of time. If you
would like to implement a feature that blinks LEDs, make it an option
that users can easily disable. Define a boolean variable at the very top
of your JavaScript file (before any code or other comments) that users
can change to `false` to disable the blinking or `true` to enable it.
Put a comment above the variable definition explaining what the variable
does and how to change it.

#### Play and cue button LEDs

Use the play\_indicator and cue\_indicator
[MixxxControls](MixxxControls) to illuminate play and cue button LEDs.
These are the controls that the buttons on screen respond to, so the
controller's LEDs will match what is on screen. The behavior of these
Mixxx Controls changes according to the [cue
mode](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
selected by the user in the preferences. If the user does not want
blinking LEDs, they can choose a cue mode in Mixxx's preferences that
doesn't have them.

The [Components JS\#PlayButton](Components%20JS#PlayButton) and
[Components JS\#CueButton](Components%20JS#CueButton) objects in
Components JS can take care of these details for you.

### Level meter LEDs

Level meters on the controller should match the meters on screen. Red
LEDs should only be lit when the signal is clipping, indicated by the
`PeakIndicator` [Control](MixxxControls). Yellow LEDs on the
controller's level meters should light up only when the meters on screen
are in the yellow region.

### Layering & Shift functions

Mapping parts of a controller to do different actions in different
conditions can be a powerful way to get more out of a limited set of
controls. However, a mapping can be confusing to use if it is
overcomplicated.

Mapping multiple controls (shift functions) to faders and knobs is
confusing to use. If you can, try to think of another way to map the
alternate function. This is not as much of an issue with encoders that
rotate infinitely, buttons, pads, or touch strips.

For shift modes that are only active while a button is held down, avoid
making LEDs change when the shift button is pressed. It can be
distracting and confusing if the user presses the shift button to access
one alternate function and at the same time LEDs flicker for an
unrelated part of the controller. If the shift button only affects a
specific part of the controller (for example the effects buttons),
changing LEDs when it is pressed is okay if the button will only be
pressed for one specific purpose. For layers that stay activated after a
button is pressed, somehow make the controller clearly indicate which
layer is active.

### Sampler buttons

Sampler buttons should behave as follows:

  - Press when no sample is loaded: LoadSelectedTrack
  - Press when a sample is loaded: cue\_gotoandplay. This allows samples
    to be replayed repeatedly from their cue point without the user
    having to stop the sample first.
  - Shift + press: If sample is playing, stop it. If a sample is loaded
    but not playing, eject it.

If your controller can turn the sampler buttons multiple colors, use
those to distinguish between a sampler that is loaded but not playing, a
sampler that is playing, and (if you have enough colors available) a
sampler that is playing and looping.

The [Components JS\#SamplerButton](Components%20JS#SamplerButton) object
in Components JS will can take care of these details for you a

### Main & Headphone gain knobs

Controllers have knobs for the main and headphone outputs that work in a
variety of different ways. On some devices, these only act on the sound
hardware, on others they send MIDI or HID signals, and on some they do
both. To encourage users to use the best [gain
staging](http://mixxx.org/manual/latest/chapters/djing_with_mixxx.html#djing-gain-staging)
possible with the equipment, it is important that this behavior is
documented on the controller's wiki page and mapped in an optimal way.
As explained in the [gain
knob](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-gain-knob)
section of the manual, the software gains in Mixxx should be the last
resort for adjusting the level of the output signals. Deck gain knobs
should be mapped to Mixxx's deck gains though.

On some controllers, these knobs only control the volume of the
controller's integrated sound card and no MIDI or HID signals are sent
to the computer. In that case, there is nothing to map, but this should
still be documented on the wiki so users don't get confused when the
knobs on screen don't move.

On other controllers, these knobs affect the integrated sound card's
output and the controller also sends MIDI or HID signals when the knobs
are turned. In this case, the signals should *not* be mapped to the
software gains in Mixxx, otherwise the knobs will adjust the gain both
on the controller's sound card and in Mixxx.

Some controllers have integrated sound cards that do not have knobs or
buttons on the device that control the sound card's outputs, but the
sound card's outputs can be controlled through the [operating system
mixer](operating%20system%20mixer) program. In that case, MIDI/HID
signals for these functions should *not* be mapped to the software gains
in Mixxx. Unfortunately, there is no reliable, cross-platform way for
Mixxx to access the controls accessible to the OS' mixer program, so
these controls cannot be mapped to control the sound card. Users should
be directed to the [operating system mixer](operating%20system%20mixer)
wiki page for instructions on how to adjust their output levels.
Although this is less convenient than mapping the software gains in
Mixxx, it makes a substantial difference to the sound quality users will
hear from Mixxx.

## Coding conventions for Javascript

Javascript is a very flexible programming language. It has some good
features, but there are also a number of features that have confusing
syntax and/or encourage bad programming practices. Using these features
makes it easier for bugs to go unnoticed in your code. Having guidelines
about coding style makes code in Mixxx easier to read and more
consistent.

These coding conventions are mandatory for new Javascript code in Mixxx:

  - Do not use `==` and `!=` because these can have unexpected results
    when comparing variables of different types. Use `===` or `!==`
    instead.
  - Assign variables to [function
    expressions](https://www.sitepoint.com/function-expressions-vs-declarations/)
    rather than using function declaration syntax. Function declaration
    syntax obscures the fact that functions are objects and can create
    [unexpected results because of
    hoisting](https://javascriptweblog.wordpress.com/2010/07/06/function-declarations-vs-function-expressions/).
  - Use 4 spaces to indent, not tab characters.
  - Always put `var` before variable declarations to avoid accidentally
    declaring global variables.
  - Do not write one-line `if` statements or one-line functions.
  - Always use brackets for `if` statements. Put the opening `{` on the
    same line as the conditional expression and the closing bracket `}`
    on its own line.
  - Put `else` statements on the same line as the previous closing `}`
  - For defining functions in object literals, put the opening `function
    (parameters) {` line on the same line as the property name, then
    indent the function body 4 spaces. Put the closing `}` at the same
    indention level as the object properties.
  - Put `,` after the last property of object literals to avoid errors
    when adding more properties in the future.
  - All code lines that need it must end with `;`
  - Use camel case (thisVariableName) rather than C-style variable
    naming (this\_variable\_name).
  - Use `new` must be used when creating new objects, except for object
    literals.
  - Capitalize the first letter of constructor functions.

Here is an example of good Javascript style:

    var someObject = new ShinyObject();
    
    var anotherObject = {
        someFunction: function (parameter) {
            return parameter++;
        },
        anotherFunction: function (parameter) {
            return parameter--;
        },
    }
    
    ShinyObject.someMethod = function (someParameter) {
        var someVariable = someParameter + 2;
        if (someVariable === 5) {
            return anotherObject.someFunction(someVariable);
        } else {
            return anotherObject.anotherFunction(someVariable);
        }
    }

### Code checking tools

We use the automated code testing tools [JSHint](http://jshint.com/) and
[JSBeautifier](http://jsbeautifier.org/) that check for bad practices in
JavaScript code. You can copy and paste your JS code onto those web
pages to use them or you can use them locally on your computer with
Node.js. Using these tools is not for making your coding skill look bad;
they are to help you make your code even better. If you use these, you
will already have the basics taken care of when you submit a pull
request.

JSHint can also be helpful if Mixxx says there is an error in your
JavaScript code but Mixxx's error message does not make it clear what
the issue is.

All Javascript files for Mixxx must start with header to make sure
JSHint doesn't generate errors for missing variables:

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
code. xmllint can also be helpful if there is a syntax error in your XML
file. Alternatively, you can use [this online
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
