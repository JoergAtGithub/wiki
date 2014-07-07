# Cover Art Support

[Cover Art Support](cover_art_support)

# Report: June 29 - July 05

Last week: [June 22 - June 28](cover_art_support_r1)

## Updating cover\_art columns in tableview

As the library.cover\_art column is updated in
TrackDAO::updateCoverArt(), we could just emit the signal "trackChanged"
and it would be enough to let the BaseTrackCache knows that it needs
update the tableview. However, currently BTC is using TIOs to get the
values of each column and as the cover\_art column is not a member of
TIO, it would not be enough.

First implementations of this project was based on the use of TIO, but
we realized that it was bringing many performance issues and that
everything would work much better without it. In this way, we needed
another solution to update the BTC and basically the best idea that we
found was implement a new SIGNAL/SLOT to access
BTC::updateTrackInIndex(int trackId).

<https://github.com/cardinot/mixxx/commit/7b5be7774cbb3d780796a02edd164d4f2ce4ee2b>
