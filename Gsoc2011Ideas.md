# Student Project Ideas for Google Summer of Code 2011

This page lists the suggested projects for students working on Mixxx as
part of [Google Summer of Code 2011](http://socghop.appspot.com/). Each
of these projects represents something that we think would make a really
big difference to our users and that we as a development team are really
excited about. For advice on how to get in touch and how to apply, you
should read [gsocadvice](gsocadvice).

## AutoDJ Improvements

The Mixxx Auto DJ mode is very simplistic -- it mixes songs from the
AutoDJ queue and crossfades them with a fixed overlap. This project aims
to spruce up AutoDJ support to be much better. In particular, the
fade-in and out points of songs should be configurable, as well as the
crossfade length. More advanced use cases could

### Deliverables

  - Implement ability for track cue-points to be designated as "Fade In"
    or "Fade Out" points.
  - Implement ability for AutoDJ crossfade interval to be adjusted 
  - Allow certain decks to be designated for Auto-DJ

## Session History Feature

Many professional DJs must report the songs they play at gigs to an
organization like ASCAP. Other DJs would simply benefit from the ability
to look at their past DJ and see a history of the songs they played.
This project aims to bring a Sessions or History feature to the Mixxx
library. This feature would show a running history of every song the DJ
played with Mixxx, grouped by "sessions" or times that Mixxx was run.

### Deliverables

  - Implement a new Library feature (section in the library) for
    displaying session history.
  - Implement a new table in the Mixxx database for storing DJ session
    history.
  - Update the Mixxx engine to send feedback about when tracks are
    loaded, unloaded and "hearable" to the Session manager, which
    records the information in the database.
  - Allow a "session" to be exported to a file in a common format (code
    to write in PLS/CUE/M3U formats is already in Mixxx)

## Advanced Library Search

The Mixxx library search feature is fairly basic. It only searches for
terms within the title, album, artist, genre tags. Furthermore, it is
pretty slow because it is implemented as a SQLite LIKE comparison with
every field it intends to search. We would like to drastically improve
this by switching to a Full-Text-Search model such as that provided by
Apache Lucene. For more information, see Wikipedia: [Full Text
Search](http://en.wikipedia.org/wiki/Full_text_search). Beyond this, we
would like to make library search box support advanced operators like
searching on Google.

Here are some examples of queries we would like to support:

  - artist:"Com Truise" Space Dust
  - Results in only songs by Com Truise with the terms space or dust in
    title/artist/album/genre/etc.
  - \-GaGa Lady 
  - Results in e.g. Ladytron, but no Lady GaGa
  - "Right Here" bpm:\>140
  - Results in tracks with the name "Right Here" and a BPM greater than
    140

### Deliverables

  - Implement Full-Text-Search
  - Support FTS indexing of album, artist, title, genre, BPM, comment,
    key, etc.
  - Implement operators for library search
  - Design a [Backus-Naur
    Form](http://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form) grammar
    for the operator language.
  - Implement support for artist, album, genre, and BPM selectors.

## Synchronization Improvements

If you've used Mixxx, you know that our SYNC button does not work very
well\! All it does is match up the BPMs of the tracks that are being
mixed. There is tons of room for improvement here. The goal of this
project is to allow two decks to be synchronized such that they actively
check whether they are in sync with the other, and make adjustments to
stay in sync. Additionally, the creation of a master sync clock for
decks to sync to would be great as well, because then the DJ could set
the master clock at e.g. 130 BPM and all the songs they load would
automatically sync to the tick of that clock.

### Deliverables

  - Implement a master-clock in the Mixxx engine
  - The master clock will have a BPM that it "beats" at.
  - Implement synchronization of decks to the master clock signals. 
  - Synchronization in this case is: 

<!-- end list -->

``` 
    * Adjusting the rate of each deck to match the master clock
    * Adjusting the "phase" or the alignment of the deck so that the beats of the deck line up with the beats of the master clock. 
* Create GUI widgets to control the master clock and assign a deck to synchronize to the master clock.
* Allow a deck to be set as the "master" deck 
* This is more open-ended -- think about the different ways to implement this and talk about it in your proposal.
* Bonus: Implement a metronome feature that ticks to the beat of the clock.
```

## Plug and Play MIDI Mode / Community MIDI Mappings

Mixxx currently supports a wide-range of hardware MIDI controllers that
DJs can use to perform with. Each supported MIDI controller has a
"mapping" file that is bundled with Mixxx, but this mapping must be
manually selected by the user before their controller works. The aim of
this project is to increase the usability for new users by automatically
selecting the correct MIDI mapping and to provide an intelligent
workflow for when an unsupported MIDI device is connected.

This project will involve a lot of time thinking about use cases,
dealing with users and understanding their requirements. It would be a
great opportunity for a student to get involved with the Mixxx
community. The student will also have the opportunity to borrow a MIDI
controller from the development team for the duration of the project.

### Deliverables

  - Implement auto-selection of MIDI mappings based on connected MIDI
    devices.
  - For unsupported devices, implement a UI and simple server-side
    functionality to:
    1.  Check mixxx.org for additional community-provided mappings.
    2.  Allow ratings and comments to be made on community-provided
        mappings.
    3.  Allow user-created mappings to be uploaded to mixxx.org.

## Something Else\!

As always with Summer of Code, you aren't limited to the suggestions
we've made here. If you've got a great idea for a project involving
Mixxx then we're looking forward to hearing about it.

**IMPORTANT: You should [contact us](gsocadvice) first to get feedback
if you're going to submit a proposal for your own project idea\!**

### Deliverables

  - Something awesome. We will work with you to define the deliverables.
