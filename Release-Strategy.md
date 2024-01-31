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

![grafik](https://github.com/mixxxdj/mixxx/assets/1777442/bbf6b1cc-7836-4aad-adaf-ddf48f12f65c)


This leads to commits like this extreme one, committed at 2018-10-18, merged to main and not even released today. 
https://github.com/mixxxdj/mixxx/commit/052fd744c53e167148fe12ef16c2c3b6b2dfc579
This situation is particularly disheartening for contributors who take pride in their work and like to receive kudos form users. Users know a feature to be ready but are unable to enjoy its benefits due to delayed releases.

Due to the long list of new features in this long cycle, many regressions and design flaws are piling up that put a high amount of hard exhausting work to the core team polishing the release during a beta. In case of the 2.4.o release we have missed the original announced release date by awful long 6 month. Because they feel responsible for the quality there is no time to work on interesting things like shiny new feature ore challenging project.

[2.5.0 Release Proposals](250_release_proposal)

