## Summary

**Status**: This specification is **in drafting**. Feel free to add
ideas to this page.

DJs may choose which track to play next according to specific
characteristics, such as BPM, key, and genre. This feature will aid in
track selection by presenting a list of potential follow-ups for the
currently playing track, filtered and ranked according to user-specified
criteria.

## Design

### Overview

The recommendations of the track suggestion feature will be available to
the user through a "Selector" option in the sidebar (and to other code,
such as the AutoDJ feature, through the **SelectorLibraryTableModel**
class). This feature should be usable whether the DJ is planning her set
in advance or choosing the next track on the fly.

First, the library will be filtered according to user-specified
criteria. The results will then be ranked based on several metrics,
which are weighted according to the DJ's preferences.

Filters allow for fuzzy matching, but they are all or nothing: either a
track matches the criteria or it is not included. This quickly narrows
down the selection of possible tracks, drawing upon metadata already
stored in Mixxx trunk and the features\_key branch such as:

  - BPM (within an adjustable range of tolerance)
  - **TODO**: Should the range be absolute or relative?
  - Key (exact match, fourth, fifth, relative minor/major)
  - Genre
  - Previously used as follow-up (taken from set history feature)

Then, once there is a small pool of tracks to judge between, we can
calculate a similarity score that measures the "closeness" of each
potential choice to the current track along a number of different
dimensions.

This score is the sum of a set of similarity functions, each of which
outputs a float between 0 and 1 inclusive, multiplied by weight
coefficients which add to 1. These weights can be specified by the user
(possibly as an ordered list, or by using sliders to determine their
relative importance). Then, the resulting similarity score will be shown
as a match percentage, and used to sort the list of followups.

Two measures of sonic similarity will be added using the Vamp plugin
architecture:

  - Energy/Intensity (see Lu et al.'s "Automatic mood detection and
    tracking of music audio signals"); plugin from [BBC Vamp
    plugins](https://github.com/bbcrd/bbc-vamp-plugins/)
  - Timbral Similarity
    [plugin](http://vamp-plugins.org/plugin-doc/qm-vamp-plugins.html#qm-similarity)

Energy can be precalculated for all tracks along with the BPM and key
analysis, and added as another column to the library table. Similarity
is just (1 - difference in energy).

The timbral similarity plugin will estimate a multivariate Gaussian
model of the MFCCs for each track in advance. Then, the symmetrized KL
divergence will be calculated on the fly, finding the distance of each
potential followup in relation to the seed track.

Finally, genre metadata will be supplemented with free-text tags derived
from online sources, including MusicBrainz and Last.FM. At analysis
time, these tags will be downloaded and stored in a table of the local
SQLite database. Then, a simple metric known as the Jaccard index (\# of
tags in common / total \# of tags for both tracks) can be calculated to
give a measure of similarity between 0 and 1, which will be added to the
overall similarity score.

### Requirements

  - Match tracks according to user-specified filters
  - Precalculate Gaussian models of track MFCCs
  - Rank the results using similarity score
  - Retrieve additional metadata (genre tags) for tracks
  - Calculate track energy, tag similarity
  - Compare (small) sets of tracks for rhythmic/timbral similarity using
    KL divergence
  - GUI Widgets
  - Selector view

<!-- end list -->

``` 
    * choose which filters are active
    * BPM range slider
* Selection criteria preference pane
    * set default filters 
    * set the relative importance of similarity functions
```

## Work Breakdown

  - Filter and Rank
  - modify **SearchQueryParser** to search for BPM range, keys in
    comparison to current track

<!-- end list -->

``` 
    * allow to search for previously-used as follow-up 
* modify **SelectorLibraryTableModel** class to rank a list of songs according to user's weighted similarity function
* Energy and Timbral Similarity Plugins
* **AnalyzerEnergy**
* **AnalyzerTimbre**
* **SimilarityDAO** class to store and retrieve timbral similarity analyses
* Tags
* **TagsDAO** to store and retrieve free-text tags
* adapt **MusicBrainzClient** to download tags as well
* create **LastFmClient** using liblastfm
* **TODO: create generic class for getting and storing data from RESTful APIs?**
* UI
* **DlgSelector**
* **DlgPrefSelector**
* Add **TrackModel** capability to context menus - "Mark as Follow-up"
```

## Comments
