# Mixxx 2.1.0 Release Checklist

This process is followed when it is time for a release (after betas and
release candidates). (Everything on the pre-release [to-do
list](2.1.0_todo) must be complete.)

[Release milestone
summary](https://launchpad.net/mixxx/+milestone/2.1.0/)

1.  ✓ Ensure QA testing is complete and all tests pass.
2.  Update translations
    1.  Push and pull translations for Mixxx as described here:
        [Internationalization](Internationalization)
    2.  Push and pull transaltions for the setup as described
        here:[README-Translations.md](https://github.com/mixxxdj/mixxx/blob/master/build/wix/Localization/README-Translations.md)
3.  ✓ Update manual.
    1.  ✓ Verify that [Jenkins
        v2.1/manual-2.1-publish](https://builds.mixxx.org/job/v2.1/job/manual-2.1-publish/)
        published the latest version to <https://mixxx.org/manual/2.1/>
    2.  double check table of contents is present (run pdflatex twice)
    3.  **TODO:** Add make linkcheck to Jenkins job.
4.  Update `Help -> Send Us Feedback` link in the application
5.  Update files:
    1.  ✓ README (update version number)
    2.  ✓ LICENSE (update copyright year, version number)
    3.  ✓ CANGELOG (update copyright year, version number)
    4.  ✓ src/defs\_version.h (update VERSION)
    5.  ✓ src/defs\_urls.h (update manual URL, survey URL, etc.)
    6.  ✓ \[rryan\] Mixxx-Manual.pdf (update to latest version from
        <https://mixxx.org/manual/2.1/en/Mixxx-Manual.pdf>)
    7.  ✓ \[rryan\] Update Debian Changelog ` dch -c
        build/debian/changelog --check-dirname-level=0
        --newversion 2.1.0-0ubuntu1  `
6.  ✓ \[daschuer\] Go through Git log, update credits in
    `src/dialog/dlgabout.cpp`.
7.  Build release packages with the build server
    1.  Source Tarball
        1.  **TODO: Should we still publish source tarballs? We've been
            pointing people to GitHub for a while.**
    2.  ✓ macOS Intel
    3.  ✓ Ubuntu i386 / amd64
    4.  ✓ Windows i386 / amd64
8.  ✓ \[daschuer\] Add a git tag with a GPG signature
    (release-2.1.0)`git tag -s release-2.1.0 -m "Mixxx 2.1.0"
    git push upstream release-2.1.0`
9.  Upload packages.
    1.  ✓ \[rryan\] Run [Jenkins
        mixxx-release-publish](https://builds.mixxx.org/job/mixxx-release-publish/)
        to copy builds to <https://downloads.mixxx.org/mixxx-x.y.z/>
    2.  ✓ \[rryan\] Record SHA256sum of all packages in the [Release
        Checksums Google
        Doc](https://docs.google.com/spreadsheets/d/1E5vFa0gKf47P3LMMXpnr3JzsZ7-ENI03IgOkj9lxYQo/edit#gid=0)
        as a backup and record independent of downloads.mixxx.org (for
        forensic purposes).
    3.  Launchpad (as backup, e.g. if we exceed mirror bandwidth limits)
        1.  **TODO: Should we still do this? Haven't had download
            availability issues since enabling CloudFlare.**
            1.  \[pegasus\] I say yes. It doesn't hurt or cost anything
                to have another separate download source just in case.
        2.  Go to milestone page
        3.  Mark milestone released
        4.  Click *Add Download File* for each package
    4.  Update the Stable and Beta PPAs.
        1.  Run [Jenkins
            mixxx-2.1-release-ppa](https://builds.mixxx.org/job/v2.1/job/mixxx-2.1-release-ppa/)
            and [Jenkins
            mixxx-2.1-beta-ppa](https://builds.mixxx.org/job/v2.1/job/mixxx-2.1-beta-ppa/)
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
    4.  Take shots with clean macOS desktop. 
    5.  Crop shots for window-only.
11. Update the website
    1.  Update download page (hide beta downloads, move current release
        to previous, replace current with new links).
    2.  ✓ Update frontpage / features page / etc.
    3.  Update screenshot downloads on Press page.
    4.  Update screenshot in OpenGraph markup (so social shares have
        updated images\!)
    5.  Update credits for contributors to latest release.
    6.  ✓ Update <https://mixxx.org/manual/latest> symlink to point to
        2.1.
    7.  Update copyright date here and on the blog
12. Release announcement:
    1.  Write announcement post for [Mixxx
        Blog](http://mixxxblog.blogspot.com/) 
    2.  Cross-post to Launchpad
    3.  Cross-post to forum
    4.  Cross-post to mixxx-devel
    5.  Cross-post to Facebook
13. Launchpad Updates
    1.  Mark milestone released
    2.  Add downloads to milestone (if you didn’t do it above.)
    3.  Change "Fix committed" bugs to "Fix released"

## Mac App Store

1.  Update the app description for the Mac App Store and localize it.
    You cannot add localizations after the package has been uploaded, so
    make sure you have these ready to go.
2.  Submit application and description for review, signed with the app
    store release keys.

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
    1.  G+
    2.  [Facebook](https://www.facebook.com/Mixxx-DJ-Software-21723485212/)
        -- Boost Post ($$)
    3.  Twitter
    4.  LinkedIn Connected DJs group
    5.  Reddit r/DJs
    6.  DJTechTools Forums
    7.  TranceAddict Forums
    8.  omgubuntu.co.uk
9.  Update [SourceForge](https://sourceforge.net/projects/mixxx/) to
    point people to the newest version

## Post-Release

1.  ✓ \[rryan\] Create `2.2.x-unix` and `2.2.x-windows` branches in the
    buildserver repo.
2.  ✓ \[rryan\] Create `manual-2.2.x` branch in the manual repo.
3.  ✓ \[rryan\] Update `master` README, defs\_version.h, defs\_urls.h.
4.  Prepare Jenkins for v2.2:
    1.  ✓ \[rryan\] Create v2.2 folder for jobs.
    2.  ✓ \[rryan\] Copy manual-2.1-publish job to v2.2
    3.  ✓ \[rryan\] Copy buildserver-2.1-\* jobs to v2.2
5.  Once a `mixxxdj/mixxx` `2.2` branch exists:
    1.  Copy `mixxx-2.1-release` and `mixxx-2.1-beta-ppa` and
        'mixxx-2.1-release-ppa'' jobs from v2.1.
        1.  **NOTE:** do not run mixxx-2.2-release-ppa until ready to
            release.
