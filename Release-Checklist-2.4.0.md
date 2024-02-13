# Mixxx 2.4.0 Release Checklist

This process is followed when it is time for a release (after betas and
release candidates).

1.  [x] Take care of the known regressions
   https://github.com/mixxxdj/mixxx/labels/regression
   Fix and merge them, or document them in the CHANGELOG? Release Notes.  
2.  [x] Release 2.3.6 
3.  [x] "Close" the 2.3 branch by target all 2.3 PRs to 2.4 
4.  [x] Update translations
    1.   [x] Push and pull translations for Mixxx as described here:
        [Internationalization](Internationalization)
5. [ ] Take release screenshots for press page and blog post.
    1.  [ ] Deere, LateNight, Shade, Tango
    2.  [ ] Load up samplers, preview deck, etc. 
    3.  [ ] Make all the screenshots roughly uniform (same view, same tracks
        loaded, etc.)
    4.  [ ] Take screenshots of the Mixxx window itself, **not** with your
        cluttered desktop in the background.
        1.  [ ] macOS can produce particularly pretty drop-shadow
            screenshots with `Shift-Command-4` followed by the spacebar,
            then click the window to screenshot.
6. [ ] Send out pre-announcement to the DJ press (to ensure, that they have enough time to write articles and record review videos)<br>
    Public press contacts are:
     *   [press@wearecrossfader.co.uk](mailto:press@wearecrossfader.co.uk)
     *   [editor@djtechtools.com](mailto:editor@djtechtools.com)
     *   [info@digitaldjtips.com](mailto:info@digitaldjtips.com)
     *   [redaktion@remise3.de](mailto:redaktion@remise3.de)
     *   [info@dj-lab.de](mailto:info@dj-lab.de)
7. [x] Update files from Git log 
    1. credits in `src/dialog/dlgabout.cpp`
    2. CHANGELOG.md
8. [ ] Verify 
    1. [ ] the latest version of https://github.com/mixxxdj/manual/tree/2.4 is published to <https://mixxx.org/manual/2.4/>
    2. [x] copyright year and version number in LICENSE
    3. [x] .github/workflows/build.yml and tools/deploy.py
    4. [x] Check Debian Changelog and PPA destination 
9. [x] Build release candidates:
    1.  [x] CMakeLists.txt Update VERSION and MIXXX_VERSION_PRERELEASE
10. [ ] Perform QA testing with all release candidate binaries (Smoke Test) 
    1. [x] macOS Intel
    2. [ ] macOS ARM
    3. [x] Ubuntu
    4. [x] Windows
11. [ ] Add a git tag with a GPG signature 
    1. [ ] ```git tag -s 2.4.0 -m "Mixxx 2.4.0"```  (double check identity / email you are using to tag!)
    2. [ ] ```git push --tags upstream 2.4.0```
    3. [ ] This can be done to a commit after it has been pushed or merged
        from the release candidate PR, so wait until you're sure you're ready to tag the
        release commit.
    4. [ ] **Once pushed, a tag is forever. Never delete a tag from a
        remote.**
12. [ ] Verify release binaries are available
    1. [ ] https://downloads.mixxx.org/releases/2.4.0/
    2. [ ] https://launchpad.net/~mixxx/+archive/ubuntu/mixxx  
13. [ ] Release
    1. [ ] Record SHA256sum of all packages in the [Release Checksums
        Google
        Doc](https://docs.google.com/spreadsheets/d/1E5vFa0gKf47P3LMMXpnr3JzsZ7-ENI03IgOkj9lxYQo/edit#gid=0)
        as a backup and record independent of downloads.mixxx.org (for
        forensic purposes).
    2. [ ] Make a release in GitHub 
    3. [ ] Update GitHub issues 
        1.  Create a 2.4.1 milestone 
        2.  Target all 2.4.0 issues that have not been fixed to 2.4.1 (or remove the milestone entirely) 
14. [ ] Manual: Remove the developer version warning https://github.com/mixxxdj/manual/pull/376 and verify it at <https://mixxx.org/manual/2.4/> 
15. [ ] Submit the new version to the Microsoft store
    1. [ ] Add the new features to the [description](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/add-and-edit-store-listing-info?pivots=store-installer-msix#description)
    2. [ ] Upload [screenshots](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/add-and-edit-store-listing-info?pivots=store-installer-msix#screenshots)
    3. [ ] Write a condensed version of the release notes for the [What's new in this version?](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/add-and-edit-store-listing-info?pivots=store-installer-msix#whats-new-in-this-version) section (1500 characters limit)
    4. [ ] Submit the .msi Installer as [app package](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/upload-app-packages?pivots=store-installer-msi-exe) (Note: That the verification process by Microsoft can take up to 3 working days)
16. [ ] Update the website
    1. [ ] Update download page:
        1.  [ ] Do this after posting the announcement forum thread so you
            can link to the announcement
        2.  [ ] hide beta downloads
        3.  [ ] move current release to previous
        4.  [ ] replace current with new links
    2. [ ] Update frontpage / features page / etc.
    3. [ ] Update screenshot downloads on Press page.
    4. [ ] Update credits for contributors to latest release.
    5. [ ] Update <https://mixxx.org/manual/latest> symlink to point to
        2.3.
    7. [ ] Update copyright date here and on the blog
17. [ ] Release announcement:
    1. [ ] Discourse is updated automatically after publishing the blog post and visiting it on the website
    2. [ ] Cross-post to Zulip \#announce stream
    3. [ ] Inform the press contacts (that were informed in step 6.) that the final release now happend
    4. [ ] Cross-post to mixxx-devel~~
    5. [ ] Cross-post to Facebook
    6. [ ] Cross-post to Twitter
    

## Promotion

1.  [ ] Email package maintainers
    1.  [ ] Debian/Ubuntu - <https://packages.debian.org/testing/mixxx>
    2.  [ ] Gentoo
    3.  [ ] Arch - <http://www.archlinux.org/packages/?q=mixxx>
    4.  [ ] Fedora
2.  [ ] E-mail bloggers
3.  [ ] Ask other Mixxx users to post on their blogs
4.  [ ] Send release email to everyone in the "Press Contacts" Google Doc.
5.  [ ] [Update Wikipedia](https://en.wikipedia.org/wiki/Mixxx)
6.  [ ] Update <http://screenshots.debian.net>
7.  [ ] Update software directories
    1.  [ ] ~~Freshmeat~~
        [ ] ~~[Freecode](http://www.freecode.com/projects/mixxx)~~ No longer
        maintained.
    2.  [ ] ~~OhLoh~~ [OpenHub](https://www.openhub.net/p/mixxx)
    3.  [ ] [Macupdate.com](https://www.macupdate.com/app/mac/33059/mixxx)
8.  [ ] Social Media / Forums
    1.  [ ] [Facebook](https://www.facebook.com/Mixxx-DJ-Software-21723485212/)
        -- Boost Post $$ (optional)
    2.  [ ] Twitter
    3.  [ ] LinkedIn Connected DJs group
    4.  [ ] Reddit r/DJs, r/Mixxx, r/linuxaudio, r/linux
    5.  [ ] DJTechTools Forums
    6.  [ ] TranceAddict Forums
    7.  [ ] omgubuntu.co.uk
    8.  [ ] YouTube channels
        1. [ ] Crossfader: https://www.youtube.com/channel/UCM4u0gp8gm99w9MXQ7ZI8Mw
        2. [ ] ~~unfa: https://www.youtube.com/user/unfa00~~ ([stepped down iiuc](https://www.youtube.com/watch?v=GHx6qyQZNjc))
    9.  [ ] librearts.org
9.  [ ] Update [SourceForge](https://sourceforge.net/projects/mixxx/) to
    point people to the newest version

## Post-Release

1.  [ ] Create 2.4 branch in mixxx manual and vcpkg 
2.  [ ] Update `main` README, CMakeList.txt for 2.5 
3.  [ ] Remove beta PPA upload in the 2.3 branch from .github/workflow/build.yml
