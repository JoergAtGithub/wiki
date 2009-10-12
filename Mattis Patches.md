In the interest of speeding up the merging process as much as possible I
am documenting the work of merging Matti's patches here.

I have created a branch, from mixxx-1.7 called 1.7-matti
(lp:\~mixxxdevelopers/mixxx/1.7-matti). The launchpad URL is:
<https://code.launchpad.net/~mixxxdevelopers/mixxx/1.7-matti>

##### Category \#1 (bugfixes)

| Patch                                        | Description                                                                                  | Status                       |
| -------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------- |
| mixxx-1.7.0-fixDirCols.patch                 | Resize the Columns for Directory Browsing                                                    | COMMITTED by: Phillip Whelan |
| mixxx-1.7.0-fixDnD.patch                     | Fix to DnD for reordering playlists (?)                                                      | \*UNTESTED\*                 |
| mixxx-1.7.0-fixFlacUnicode.patch             | Treat FLAC metadata as UTF8                                                                  | COMMITTED by: Albert Santoni |
| mixxx-1.7.0-fixM3UparserComment.patch        | Ignore Comments (lines that start with '\#') in M3U Files                                    | \*UNTESTED\*                 |
| mixxx-1.7.0-fixPLimporterCaseSensitive.patch | Make the comparison for M3U and PLS filename extensions case insensitive                     | \*UNTESTED\*                 |
| mixxx-1.7.0-fixLoopMode.patch                | Do absolute seeking instead of relative seeking when reaching the end of a file in NEXT mode | COMMITTED by: phillip whelan |
| mixxx-1.7.0-fixPlayButton.patch              |                                                                                              | \*UNTESTED\*                 |
| mixxx-1.7.0-playlistMutexLocking.patch       |                                                                                              | \*UNTESTED\*                 |
| mixxx-1.7.0-checkExistWhenGettingNext.patch  |                                                                                              | \*UNTESTED\*                 |
| mixxx-1.7.0-fixQ3textstream.patch            |                                                                                              | \*UNTESTED\*                 |
| mixxx-1.7.0-fixTrComboBox.patch              |                                                                                              | \*UNTESTED\*                 |

##### Category \#2 (FEATUREFIX)

  - mixxx-1.7.0-fixRateEngine.patch
  - mixxx-1.7.0-fixCueRecallOnNext.patch

##### Category \#3 (FEATURES)

  - mixxx-1.7.0-mixxxClient.patch
  - mixxx-1.7.0-playHistory.patch
  - mixxx-1.7.0-restoreState.patch 
  - mixxx-1.7.0-randomizeQueue.patch
  - mixxx-1.7.0-savePlayqueue.patch
  - mixxx-1.7.0-detectSilence.patch

##### Unsorted

  - mixxx-1.7.0-popFirstInQueue.patch
  - mixxx-1.7.0-queueWDclick.patch
  - mixxx-1.7.0-sendBottomPlayQueue.patch
  - mixxx-1.7.0-sendTopPlayQueue.patch
  - mixxx-1.7.0-takeFirstInQueue.patch
  - mixxx-1.7.0-unselectWDclick.patch
  - mixxx-1.7.0-addMixxxviewToTableview.patch
  - mixxx-1.7.0-addPrependToTrackModel.patch 
  - mixxx-1.7.0-addTakeFirstToTrackModel.patch 
  - mixxx-1.7.0-allowDuplicateTracksInPls.patch
  - mixxx-1.7.0-alternatePlay.patch
  - mixxx-1.7.0-atQueueEndPickRandom.patch 
  - mixxx-1.7.0-changePushBMouseEvent.patch
  - mixxx-1.7.0-changeRestoreStateForPlayHistory.patch
  - mixxx-1.7.0-failsafePlayqueue.patch
  - mixxx-1.7.0-fixPlaylistAppend.patch
  - mixxx-1.7.0-fixPlaylistImportName.patch
  - mixxx-1.7.0-fixPlaylistsRemove.patch
  - mixxx-1.7.0-fixShowPl.patch
  - mixxx-1.7.0-fixSplash.patch
  - mixxx-1.7.0-fixTablemodelIndexPrivacy.patch
  - mixxx-1.7.0-fixTableViewEditing.patch
