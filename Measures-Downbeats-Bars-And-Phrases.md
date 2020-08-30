# Measures, Downbeats, Bars and Phrases

**Author:** Harshit Maurya (hacksdump)

**Email:** [hmaurya999@gmail.com](hmaurya999@gmail.com)

**Mentors:** Be (Be-ing), Jan Holthuis (Holzhaus), Uwe Klotz (uklotzde)

**Related Project:**
[Downbeats-And-Phrase-Detection](https://github.com/mixxxdj/mixxx/wiki/Downbeats-And-Phrase-Detection)

# GSoC 2020 Work Product

During the community bonding period, I added cue menu to the scrolling waveform which was only available to the overview waveform. This served as an important precursor to my project since it requires interactions on the scrolling waveform, which were non-existent earlier.

[#2783](https://github.com/mixxxdj/mixxx/pull/2783) summarises that work.

With the commencement of the coding period, we decided I should begin with some UI. So I added downbeat triangles to the scrolling waveform renderer. Initially, support for 4/4 time signature was added and every fourth beat was accented with downbeat triangles.

Thanks to the presence of downbeats, we could now zoom out even further out of the scrolling waveform by displaying only the downbeats at high zoom out levels, thus reducing clutter on display and only displaying meaningful information.

This PR also introduces the new `Beat` class which encapsulates all properties a beat may store, whether it is a beat or downbeat and its index.

[#2844](https://github.com/mixxxdj/mixxx/pull/2844) summarises the initial work.

Due to the added metadata, it was necessary to start working on the data format. So I continued past work which aimed at making the `Beats` class non-polymorphic by removing `BeatMap` and `BeatGrid`. Although a polymorphic approach for containing beats of different nature sounds appropriate, `BeatMap` was mostly causing trouble with DJing operations. The past work only aimed at preserving `BeatMap` essentially moving its implementation to `Beats` class, so this could not clearly support our use case.

So I started working in another PR [#2861](https://github.com/mixxxdj/mixxx/pull/2861) starting off by fixing all broken tests, without which the core functionality of Mixxx was rendered dysfunctional. This was an important PR since we had to fixate on a Beats protocol buffer data structure with **minimal base state**.

An important refactor this PR introduced was the creation of a new `Frame` class. Earlier, Mixxx used sample positions to reference a point in the track, but the sample position is channel dependent. So I refactored a lot of existing code to use `Frame` which means the elimination of perplexing frame-sample conversions. Creating this class was a dive into building correct semantic architecture with C++. I discovered the granularity of control and what operations are considered appropriate when creating a class.

At this point, more of my work started in the direction of improving the existing code architecture and it was a great learning experience.

Using the new Beats protobuf format meant that old beat grid data could be broken when someone upgrades Mixxx to a newer version. Fortunately, `BeatFactory` provided an easy interface to write the migration path.

We took a step ahead in the direction of creating a sample independent data structure by basing the markers (BPM, Time Signature) on beat or bar indices. This facilitates the deterministic regeneration of beats from the minimal beats data.

The new beats protobuf structure was still controversial so we decided that I should start implementing UI and editing operations on top of the new beats. So we decided to merge [#2844](https://github.com/mixxxdj/mixxx/pull/2844) and [#2861](https://github.com/mixxxdj/mixxx/pull/2861) closing them in favour of [#2961](https://github.com/mixxxdj/mixxx/pull/2961). This was necessary to gain confidence in the new beats format.

I created a new widget to edit the time signature at any downbeat in the track. With this widget, we can change the time signature for any bar in the track. A similar menu was created to edit BPM at any beat in the track.

Play marker is a rendering component of the scrolling waveform and unlike other components which are modular, it was included with code where it did not belong. So I factored it out to its own renderer.

A major architectural change was the redesign of the `Beats` class inheriting from `QObject`. The earlier design was problematic since it allowed a `QObject` to be copied and any client could create `Beats` object by injecting `TrackPointer` which led to cyclic dependency and is overall bad design. So the first step was to separate the hull inheriting from `QObject` which takes care of locking in the multithreaded GUI environment and signal-slot connections. By allowing only the `Track` to create `Beats` object, the cyclic dependency could be removed and the `Track` now holds direct control over `Beats`.

Nearing the end of GSoC, I fixed a major bug which was caused due to ignoring the `BeatGrid` nature of the `Beats` and limiting ourselves to a `BeatMap`. Beats needed to be created dynamically outside the boundaries of the track and cached inside the track. This fixed DJing operations like beat jumping before the track.

I favour a test-driven approach and tried my best to create new tests for the code I added and even improved old tests to increase the range of coverage.

[#2961](https://github.com/mixxxdj/mixxx/pull/2961) is not merged as of now as we do not have a strong consensus on the Beats protobuf format. This decision cannot be arbitrary since it may break old user data. This PR also needs more seamless UX for beat grid editing, though it can be handled in another PR, this will be helpful to gain confidence in the new data structure.

## Remaining work

### In this PR

* Fix existing tests and add more tests to check old and new behaviour.
* Create a more seamless editing UX.
* Discuss more with the community and fixate on the ideal Beats protobuf data structure.
* Find and fix any remaining architectural flaws.

### Further in the project
* Create section overview widget under overview waveform and section renderer for scrolling waveform.
* Add phrase display to section display.
* Improve DJing operations aided by the new metadata.

## Journey so far

It's been a great experience working with Mixxx and I am glad to be a part of an active community that combines two of my interests. I greatly enjoyed working on my pre-GSoC PR creating `WTrackMenu` which added a menu to decks and samplers in addition to the track table. I personally use it quite often now.

The time and effort put in by my mentors into my project are really appreciable and I learnt a lot during the course of the project, be it design choices, C++ semantics or architecture planning. The architectural and data structure challenges throughout the course of the project kept me technically inspired.

I would like to thank the entire community as a whole in addition to my primary mentors for taking a huge interest in my project and adding valuable inputs to discussions and PR reviews.

# Original Proposal

This is the final
[proposal](https://drive.google.com/file/d/1Micg2kqdE-XpCIgcjb58CrZoqrgIHUnv/view?usp=sharing)
that got accepted in GSoC 2020.

-----

### Abstract

The main idea of the project is to enhance and accent the beatgrid with
more information about the track than just the beat markers. The project
will enable more interactions with the scrolling waveforms to edit the
tempo, downbeats, cues, time signature, phrases and sections. This
metadata will be backed by the analysis features with the help of the
sibling project and this metadata, of course, can be edited by the user
at will in case the analysis data is incoherent with the track.

These beatgrid editing features will be different from any other DJing
software since they are aimed at providing absolute granular control
over the beatgrid at any point in the track.

This project will display and enable the user to edit meter(time
signature), downbeats, phrases and sections in the beatgrid.

-----

#### Visual Additions

##### Section Overview widget

A new SectionOverview widget will be added under the existing
WaveformOverview widget to display track section divisions.

[[/media/image1617.png|image1617.png]]

##### Scrolling Waveform additions

**Downbeat Markers**

The downbeat markers will be more opaque than the other bar beats.

[[/media/image20-5.png|image20-5.png]]

**Bar Counter**

[[/media/image156.png|image156.png]]

**Adjustment markers**

[[/media/image20-5-5.png|image20-5-5.png]]

**Sections bands**

The sections will be displayed on the waveform as tabbed strips.

[[/media/image20.png|image20.png]]

**Phrase markers**

~~These markers define the start of a new phrase. The phrase markers
will be coloured differently and more accented than the downbeat
markers.~~

[[/media/image20-5-1.png|image20-5-1.png]]

Cleaner option

[[/media/phrasenew.png|phrasenew.png]]

Note: The start of a section implicitly indicates the start of a phrase.

-----

#### Interactions

##### Section overview

Clicking on a section will seek to the section start position.

##### Section Editor

In the edit mode, the section overview and section bands on scrolling
waveform can be edited to modify, add and remove sections. Since the
section overview is relatively small, larger quantization units will be
preferred over smaller units. Snap/Quantize behaviour will follow the
order of preference: Phrase \> Downbeat \> Beat. (Phrase quantization
will be used only if a phrase marker is close enough within a range of
few bars). For scrolling waveform, it will be beat.

The base state for the sections when no sections have been assigned
either manually or via the analyzer is a single section named INTRO
which spans throughout the audible range of the track.

**Adding a section** Click the clip/scissors icon and click within an
existing section to cut the section in two parts with the same
properties (name, color) as the earlier section. The scissors tool can
be used on the section overview and section bands on the scrolling
waveform.

**Removing a section** The section context menu has the option to delete
a section. A section can also be deleted by selecting it and pressing
the delete key afterwards. The preceding section occupies the empties
space. If it is the first section, the second section occupies the
cleared space. Sections can also be removed by dragging the section
divider from one end to the other overlapping the entire section with a
neighbouring section as a result.

**Modifying a section** The length can be adjusted by dragging the
section dividers on either the section overview widget or the section
bands on the scrolling waveforms. Their names and color can be changed
via the section context menus. This functionality is similar to the cue
context menu.

##### Beatgrid

The scrolling waveform will be powered by context-menus for every beat
on the waveform. This gives the perfect granular control over the
beatgrid for the tracks and allows editing for tracks with variable time
signatures and tempos.

**Beat context menu**

[[/media/beatmenu.png|beatmenu.png]]

**Downbeat context menu**

[[/media/dbmenu.png|dbmenu.png]]

**Time signature menu**

[[/media/rect1821-5-9.png|rect1821-5-9.png]]

**Phrase context menu** Inherit options from beat and downbeat menu (if
applicable) Added option:

  - Remove phrase marker

**Adjustment markers** Markers define ranges of user defined changes
from the previously set marker (or the default in case no marker is set
before) to the upcoming marker (or the end of the track). This will
enable us to make multiple adjustments in the track. The marker encodes
BPM and time signature information. (Time signature can only be changed
at a downbeat)

**Marker BPM context menu** Adjust BPM ahead by tapping the buttons or
setting a value in the input box.

[[/media/rect1265.png|rect1265.png]]

**Note:** Quarter note = beat and no adjustments will be allowed to this
convention.

##### Beatjump and loop

A combo box next to their controls will be added to select the jump/loop
unit. Selection options (in ascending order):

[[/media/image1617-7-2.png|image1617-7-2.png]]

-----

#### Auto DJ enhancements

Downbeats will be matched. First and last sections (need not necessarily
be called intro/outro since tracks without intro exist) will be used to
determine transition/mixing triggers instead of older intro and outro
cues.

-----

#### Breaking Changes

Since the intro and outro information will now be included with the
sections, explicit intro and outro cues will be removed along with the
editor buttons for the same.

<span class="underline">Earlier:</span> To mark the intro/outro, the
start marker was set at the starting position and end marker was placed
at the end position of the intro/outro. The enclosed segment defined the
intro/outro.

<span class="underline">Change:</span> Use the section editor or the
drag control on the scrolling waveform to mark the first and the last
sections.

-----

#### Being friends with the analyzer (future goals)

As much as this project depends on the analyzer to generate the metadata
for markers, the analyzer can also benefit from the metadata marked by
the user. For instance, precise time signature values can aid the
analyzer to find phrases and section. Thus, every edit by the user will
trigger another analysis based on the new empirical data and gather the
rest of the data so that the user does not have to edit the rest of it
manually.

### Implemetation Detail

The scrolling waveform, which currently only renders the waveform and
the tracks metadata, will be made interactive. To do so, the elements
must share common interfaces such as `WaveformItemClickable`,
`WaveformItemDraggable`.

Since the skins can be very different in a way that a skin might not
even have the buttons or panel that another one has, the scrolling
waveform context menus will be used as the primary way to adjust
beatgrid via the GUI.

#### New classes

**TimeSignature**

Members:

  - int beatsPerBar
  - int noteValue

**Section**

Members:

  - int beatOffset
  - QColor color
  - QString label
  - TrackPointer pTrack

**GridAdjustmentMarker**

Members:

  - int beatOffset
  - TimeSignature newTimeSignature
  - Bpm newBpm

## Planned Timeline

### Phase 1

In the first phase, the groundwork for subsequent work, the base for all
track metadata, that is, beats will be perfected. This will involve
setting BPM, time signature and downbeats.

**Week 1**

  - Add `Downbeat Offset` and `Time Signature` as members of the Track
    class. Initially, this data will not be persistent.
  - Add mouse pointer interaction capabilities to beats on the scrolling
    waveform. Additionally, try to create a general interface for
    functionality common to scrolling waveform elements (Currently, they
    are only rendered and can't be interacted with).
  - Add context menu to mark a beat as downbeat and set global time
    signature for the track.
  - Create tests to check downbeats and time signature data are in sync.

**Week 2**

  - Persist the data by adding time signature (single global value, not
    repeated) and downbeat offset fields to beats.proto.
  - Shift from global metadata adjustment to a marker based system.
  - Add an adjustment marker renderer.
  - Add tests to check multiple marker data.

**Week 3**

  - Implement changes to recalculate marker dependent values like
    `waveformrenderbeat`.
  - Add bar/beat counter near play marker.

**Week 4**

  - Finalize PR with granular beatgrid editing features. This PR will
    enable us to set downbeats, and arbitrary BPM and time signature via
    adjustment markers.

### Phase 2

Sections and phrases.

**Week 5**

  - Start by creating in memory sections as a member of Track. A Track
    stores a list of section dividers which demarcate the start of a new
    section. A section always clamps to a beat.
  - Add tests.

**Week 6**

  - Create a new `SectionOverviewWidget` with draggable section
    boundaries and splitting capability with scissor-like pointer.
  - Create a PR with a section overview widget displayed under the
    waveform overview with editing capabilities.

**Week 7**

  - Create a new renderer `WaveformRenderSection` to draw on scrolling
    waveform.
  - Add drag and split interactions.

**Week 8**

  - Working on section context menu to change color and label.
  - Add context menu option to downbeat/beat to mark a part of section
    as phrase demarcation.
  - Prepare a PR with new section renderer with editing and phrase
    addition capabilities.

### Phase 3

Oriented towards DJing functionality aided by the new metadata and
beatgrid editing with button controls (without context menus)

**Week 9**

  - Add loop and jump combobox selector for setting units.
  - Create a PR for the same.

**Week 10**

  - AutoDJ changes to match track downbeats during transition.
  - Create a new PR for this feature.

**Week 11**

  - Integrating results from the analyser.
  - Create a separate PR for this integration.

**Week 12**

  - Create a beatgrid editing panel with buttons mappable to controller.
  - Add controls to edit beatgrid using the current play position.
  - Create the final PR.