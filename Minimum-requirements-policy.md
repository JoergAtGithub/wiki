The main branch must build with the packages in the latest Ubuntu LTS which has had at least one point release. New features can be committed to the master branch which depend on packages not yet available in that Ubuntu version, but the main branch must build without the new feature until the first point release of the new Ubuntu LTS. When the first point release of a Ubuntu LTS is released, backwards compatibility hacks for older dependencies should be removed only if new Mixxx features are incompatible with those old dependencies.

Major Mixxx releases (X.Y, like 2.2) have the same minimum requirements as the minimum requirements when they were branched from the main branch. Bugfix releases (X.Y.Z, like 2.2.1) will continue supporting the same minimum requirements that the X.Y.0 release did.

Here are some background info: [Ubuntu and Fedora Support](Ubuntu-and-Fedora-Support-Policy)

This policy was collectively agreed upon in [this Zulip discussion](https://mixxx.zulipchat.com/#narrow/stream/109171-development/topic/minimum.20requirements.20policy/near/203415058).
