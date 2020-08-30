# Measures, Downbeats, Bars and Phrases

**Author:** Harshit Maurya (hacksdump)

**Email:** [hmaurya999@gmail.com](hmaurya999@gmail.com)

**Mentors:** Be (Be-ing), Jan Holthuis (Holzhaus), Uwe Klotz (uklotzde)

**Related Project:**
[Downbeats-And-Phrase-Detection](https://github.com/mixxxdj/mixxx/wiki/Downbeats-And-Phrase-Detection)

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
