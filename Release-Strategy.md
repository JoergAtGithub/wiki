# Release Strategy 

This were our release cycles in the past 5 years: 

![grafik](https://github.com/mixxxdj/mixxx/assets/1777442/abc7a075-ec97-4642-a2a1-0287c204addb)

We have maintained three branches, that where releases on our web page as 
* Stable Version 
* Beta Snapshot
* Development Snapshot (Alpha) 

In case of Ubuntu that is linked to our [Launchpad PPAs](https://launchpad.net/~mixxx) accordingly

![grafik](https://github.com/mixxxdj/mixxx/assets/1777442/96ca8a99-87c0-43a1-ba5e-794e80848446)

This gives user a choice to use the rock solid stable version, preview the upcoming features in the beta, or help testing and polishing new features in the development branch.

In the same way contributors have the freedom to either contribute
* New features to the main branch
* Fix bugs in the stable branch
* Test, fix bugs and polish new features in the beta branch.  

The target time line for each period was discussed to be 6 to 12 month. 

# Problem

The core "problem" is that developers NEVER consider something as finished. It is always one detail missing, on last PR pending to merge. 

This is just the same in our Mixxx team. Compared to real live, where customers receive confirmations with set deadlines and project managers drive developers to meet those targets, we develop in Mixxx intentionally without this pressure. No one is forced to do specific tasks at predefined intervals. This autonomy is highly valued within our community, serving as a guarantee for exceptional quality without compromises.

Regrettably, due to the core problem of developers never feeling fully ready, there is an invisible force that tug at the time line like a rubber band. Everyone involved in a particular feature welcomes the relief when a release is postponed by a week or such, providing additional time for the last pull request in progress. What was originally discussed as a tentative date, never officially confirmed, ends up being pushed even beyond the latest initially proposed deadline.

The result is what we see in the timeline above. This heightening the pressure even more to delay a release further, because missing a deadline causes a long wait for new features to be included in the next cycle.
And as always after a release we promise to keep the next release cycle short, which has never worked out. 

This leads to commits like this extreme one, committed at 2018-10-18, merged to main and not even released today. 
https://github.com/mixxxdj/mixxx/commit/052fd744c53e167148fe12ef16c2c3b6b2dfc579
This situation is particularly disheartening for contributors who take pride in their work and like to receive kudos form users. Users know a feature to be ready but are unable to enjoy its benefits due to delayed releases.

Due to the long list of new features in this long cycle, many regressions and design flaws are piling up that put a high amount of hard exhausting work to the core team polishing the release during a beta. In case of the 2.4.o release we have missed the original announced release date by awful long 6 month. Because they feel responsible for the quality there is no time to work on interesting things like shiny new feature ore challenging project.

# Proposal 1

A effective workaround for this big problem is a short release cycle of 6 month with fixed deadlines. This should release the pressure to every contributor, because 6 month is such short that it is not a big problem to not meet a certain deadline.
Everyone can still either work on features, bugs or polishing for a release at any time. 

We should still maintain a "regession" free release, which may leads to a delay of a certain release, but we must not delay a beta, because of a "alomost" ready feature.

In the current case of 2.5-alpha it means which is already 9 month old. It needs to go immediately into the beta = feature freeze state.
The Qt6 introduction alone rectifies a immediately release. 

Then we can consider if we want to catch up with the 2.6 release and limit the alpha phase to 3 month. 


# Proposal 2

![grafik](https://github.com/mixxxdj/mixxx/assets/1777442/84557070-78ec-4147-bf0c-c631123eb4b9)


# Discussion 

For my understanding both proposals are almost compatible. We just need to make sure that the original problem is fully fixed.  

I am afraid the the 60 day will create a sprint, because everyone is eager to include the new feature. Than we have a bunch of not reviewed not polished PRs that will take another 30 days to be reviewed and merged. So it likely ends up to the Proposal 1. 

The only difference is, that we have the Qt6 release already released. I consider it as pretty stable and since there are not many features merged, there is plenty of time for polish it for a release every one at the own pace.   

See https://github.com/daschuer/mixxx/blob/2.5_changelog/CHANGELOG.md







