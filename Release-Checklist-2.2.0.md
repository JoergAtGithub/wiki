# Mixxx 2.2.0 Release Checklist

This process is followed when it is time for a release (after betas and
release candidates). (Everything on the pre-release [to-do
list](2.2.0_todo) must be complete.)

[Release milestone
summary](https://launchpad.net/mixxx/+milestone/2.2.0/)

1.  Ensure QA testing is complete and all tests pass.
2.  \[rryan\] Update translations
    1.  Push and pull translations for Mixxx as described here:
        [Internationalization](Internationalization)
    2.  Push and pull transaltions for the WiX installer as described
        here:[README-Translations.md](https://github.com/mixxxdj/mixxx/blob/master/build/wix/Localization/README-Translations.md)
3.  \[Be\] Update manual.
    1.  Verify that [Jenkins
        v2.2/manual-2.2-publish](https://builds.mixxx.org/job/v2.2/job/manual-2.2-publish/)
        published the latest version to <https://mixxx.org/manual/2.2/>
    2.  double check table of contents is present (run pdflatex twice)
    3.  **TODO:** Add make linkcheck to Jenkins job.
4.  Update `Help -> Send Us Feedback` link in the application
5.  Update files:
    1.  ✓ README (update version number)
    2.  ✓ LICENSE (update copyright year, version number)
    3.  src/defs\_version.h (update VERSION)
    4.  src/defs\_urls.h (update manual URL, survey URL, etc.)
    5.  Mixxx-Manual.pdf (update to latest version from
        <https://mixxx.org/manual/2.2/en/Mixxx-Manual.pdf>)
    6.  Update Debian Changelog ` dch -c build/debian/changelog
        --check-dirname-level=0 --newversion 2.2.0-0ubuntu1  `
6.  Go through Git log, update credits in `src/dialog/dlgabout.cpp`.
7.  Build release packages with the build server.
    1.  macOS Intel
    2.  Ubuntu i386 / amd64
    3.  Windows i386 / amd64
8.  Add a git tag with a GPG signature (release-2.2.0)`git tag -s
    release-2.2.0 -m "Mixxx 2.2.0"
    git push --tags upstream release-2.2.0`
    1.  This can be done to a commit after it has been pushed or merged
        from a PR, so wait until you're sure you're ready to tag the
        release commit.
    2.  **Once pushed, a tag is forever. Never delete a tag from a
        remote.** 
9.  Upload packages.
    1.  Run [Jenkins
        mixxx-release-publish](https://builds.mixxx.org/job/mixxx-release-publish/)
        to copy builds to <https://downloads.mixxx.org/mixxx-x.y.z/>
    2.  Record SHA256sum of all packages in the [Release Checksums
        Google
        Doc](https://docs.google.com/spreadsheets/d/1E5vFa0gKf47P3LMMXpnr3JzsZ7-ENI03IgOkj9lxYQo/edit#gid=0)
        as a backup and record independent of downloads.mixxx.org (for
        forensic purposes).
    3.  Update Launchpad
        1.  Go to [2.2.0
            Milestone](https://launchpad.net/mixxx/+milestone/2.2.0).
        2.  Mark milestone released
    4.  Update the Stable and Beta PPAs.
        1.  Run [Jenkins
            mixxx-2.2-release-ppa](https://builds.mixxx.org/job/v2.2/job/mixxx-2.2-release-ppa/)
            and [Jenkins
            mixxx-2.2-beta-ppa](https://builds.mixxx.org/job/v2.2/job/mixxx-2.2-beta-ppa/)
            jobs.
        2.  **NOTE:** Launchpad builds its own .debs, so this does not
            depend on building packages above. The "Update files:" step
            above should be complete though (Debian changelog,
            defs\_version.h, etc.).
10. Take release screenshots for press page and blog post.
    1.  Deere, LateNight, Shade, Tango
    2.  Load up samplers, preview deck, etc. 
    3.  Make all the screenshots roughly uniform (same view, same tracks
        loaded, etc.)
    4.  Take screenshots of the Mixxx window itself, **not** with your
        cluttered desktop in the background.
        1.  macOS can produce particularly pretty drop-shadow
            screenshots with `Shift-Command-4` followed by the spacebar,
            then click the window to screenshot.
11. \[Be\] Release announcement:
    1.  Write announcement in new forum thread. For the "Post topic as"
        option below the text box to type the post, select
        "Announcement". 
    2.  Cross-post to Zulip \#announce stream
    3.  Cross-post to mixxx-devel
    4.  Cross-post to Facebook
12. Update the website
    1.  Update download page:
        1.  Do this after posting the announcement forum thread so you
            can link to the announcement
        2.  hide beta downloads
        3.  move current release to previous
        4.  replace current with new links
        5.  update Google Analytics labels
    2.  Update frontpage / features page / etc.
    3.  Update screenshot downloads on Press page.
    4.  Update screenshot in OpenGraph markup (so social shares have
        updated images\!)
    5.  Update credits for contributors to latest release.
    6.  Update <https://mixxx.org/manual/latest> symlink to point to
        2.2.
    7.  Update copyright date here and on the blog
13. Launchpad Updates
    1.  Mark milestone released
    2.  Change "Fix committed" bugs to "Fix released"

## Promotion

1.  Email package maintainers
    1.  Debian/Ubuntu - <https://packages.debian.org/testing/mixxx>
    2.  Gentoo
    3.  Arch - <http://www.archlinux.org/packages/?q=mixxx>
    4.  Fedora
2.  E-mail bloggers
3.  Ask other Mixxx users to post on their blogs
4.  Send release email to everyone in the "Press Contacts" Google Doc.
5.  [Update Wikipedia](https://en.wikipedia.org/wiki/Mixxx)
6.  Update <http://screenshots.debian.net>
7.  Update software directories
    1.  ~~Freshmeat~~
        ~~[Freecode](http://www.freecode.com/projects/mixxx)~~ No longer
        maintained.
    2.  ~~OhLoh~~ [OpenHub](https://www.openhub.net/p/mixxx)
    3.  [Macupdate.com](https://www.macupdate.com/app/mac/33059/mixxx)
8.  Social Media / Forums
    1.  [Facebook](https://www.facebook.com/Mixxx-DJ-Software-21723485212/)
        -- Boost Post ($$)
    2.  Twitter
    3.  LinkedIn Connected DJs group
    4.  Reddit r/DJs
    5.  DJTechTools Forums
    6.  TranceAddict Forums
    7.  omgubuntu.co.uk
9.  Update [SourceForge](https://sourceforge.net/projects/mixxx/) to
    point people to the newest version

## Post-Release

1.  ✓ \[rryan\] Create `2.3.x-unix` and `2.3.x-windows` branches in the
    buildserver repo.
2.  ✓ \[rryan\] Create `manual-2.3.x` branch in the manual repo.
3.  ✓ \[rryan\] Update `master` README, defs\_version.h, defs\_urls.h.
4.  Prepare Jenkins for v2.3:
    1.  ✓ \[rryan\] Create v2.3 folder for jobs.
    2.  ✓ \[rryan\] Copy manual-2.2-publish job to v2.3
    3.  ✓ \[rryan\] Copy buildserver-2.2-\* jobs to v2.3
5.  Once a `mixxxdj/mixxx` `2.3` branch exists:
    1.  Copy `mixxx-2.2-release` and `mixxx-2.2-beta-ppa` and
        'mixxx-2.2-release-ppa'' jobs from v2.2.
        1.  **NOTE:** do not run mixxx-2.3-release-ppa until ready to
            release.
