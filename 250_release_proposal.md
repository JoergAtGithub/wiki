These are the proposals how we may target the problem described in [Release Strategy](Release-Strategy)

# Proposal 1 (Phase model) 

![grafik](https://github.com/mixxxdj/mixxx/assets/1777442/84557070-78ec-4147-bf0c-c631123eb4b9)

Reduced merging effort, because only two branches open in feature phase.

Only one deadline at a time (developers are not forced to choose between working on the feature they want in the version next, and spending time for the release of the actual version).


# Proposal 2 (3 Branch model) 

![grafik](https://github.com/mixxxdj/mixxx/assets/1777442/0b569dc7-1384-46f8-8ddb-944b6460ec26)

Plan for a 6 month release cycle with deadline and the exception to not release a Mixxx version with known regressions. 

Only merge mature features that do not cause known regression. This together with the short cycle will prevent endless bug fixing during the beta phase like we did for 2.4-beta. 

All branches are open all the time. This should release the pressure to contributors, because 6 month is unlike the the current 3 years in sight and such short, that it is not an issue to not meet a certain deadline. Everyone can still either work on features, bugs or polishing for a release at any time.

We will advance the main branch version immediately after a release and cut out the old alpha to a versioned branch e.g. 2.5. Before going into feature freeze and advance to beta, we decide which almost mature features are allowed to be merged during the beta period and put them on the GitHub Milestone accordingly.  

## Special case: 2.5.0 Release

The Qt6 introduction rectifies an immediately release, because distros are starting to ripping off Qt5.  

The 2.5-alpha has an reasonable small changelog and is already 9 month old. 
See https://github.com/daschuer/mixxx/blob/2.5_changelog/CHANGELOG.md

We may consider a shorten 3 month release cycle = beta phase. 

Due to the huge 2.4.0 release, the team is kind of exhausted form fixing annoyances and needs time for a implementing new shiny and challenging features. So we can effort the 60 days feature phase from Proposal 1 while 2.5-beta is already tested by users. Than we can focus on the 2.5.0 release which should be like a stroll compared to 2.4.0

All following release will keep the 6 Month cycle form this proposal