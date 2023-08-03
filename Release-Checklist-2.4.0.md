# Mixxx 2.4.0 Release Checklist

This process is followed when it is time for a release (after betas and
release candidates).

0. Warn press contacts 
1. Take care of the known regressions
   https://github.com/mixxxdj/mixxx/labels/regression
   Fix and merge them, or document them in the CHANGELOG? Release Notes.  
2. Release 2.3.6 
3. "Close" the 2.3 branch by target all 2.3 PRs to 2.4 
4. Update translations
    1.  Push and pull translations for Mixxx as described here:
        [Internationalization](Internationalization)
5. Take release screenshots for press page and blog post.
    1.  Deere, LateNight, Shade, Tango
    2.  Load up samplers, preview deck, etc. 
    3.  Make all the screenshots roughly uniform (same view, same tracks
        loaded, etc.)
    4.  Take screenshots of the Mixxx window itself, **not** with your
        cluttered desktop in the background.
        1.  macOS can produce particularly pretty drop-shadow
            screenshots with `Shift-Command-4` followed by the spacebar,
            then click the window to screenshot.
6. Update files from Git log 
    1. credits in `src/dialog/dlgabout.cpp`
    2. CHANGELOG.md
7. Verify 
    1. the latest version of https://github.com/mixxxdj/manual/tree/2.4 is published to <https://mixxx.org/manual/2.4/>
    2. copyright year and version number in LICENSE
    3. .github/workflows/build.yml and tools/deploy.py
    4. Check Debian Changelog and PPA destination 
8. Build release candidates:
    1.  CMakeLists.txt Update VERSION and MIXXX_VERSION_PRERELEASE
9. Perform QA testing with all release candidate binaries (Smoke Test) 
    1. macOS 
    2. Ubuntu
    3. Windows
10. Add a git tag with a GPG signature 
    1. ```git tag -s 2.4.0 -m "Mixxx 2.4.0"```  (double check identity / email you are using to tag!)
    2. ```git push --tags upstream 2.4.0```
    3.  This can be done to a commit after it has been pushed or merged
        from the release candidate PR, so wait until you're sure you're ready to tag the
        release commit.
    4.  **Once pushed, a tag is forever. Never delete a tag from a
        remote.**
11. Verify release binaries are available
    1. https://downloads.mixxx.org/releases/2.4.0/
    2. https://launchpad.net/~mixxx/+archive/ubuntu/mixxx  
12. Release
    1. Record SHA256sum of all packages in the [Release Checksums
        Google
        Doc](https://docs.google.com/spreadsheets/d/1E5vFa0gKf47P3LMMXpnr3JzsZ7-ENI03IgOkj9lxYQo/edit#gid=0)
        as a backup and record independent of downloads.mixxx.org (for
        forensic purposes).
    2. Make a release in GitHub 
    3. Update GitHub issues 
        1.  Create a 2.4.1 milestone 
        2.  Target all 2.4.0 issues that have not been fixed to 2.4.1 (or remove the milestone entirely) 
13. Manual: Remove the developer version warning https://github.com/mixxxdj/manual/pull/376 and verify it at <https://mixxx.org/manual/2.4/>    
11. Update the website
    1. Update download page:
        1.  Do this after posting the announcement forum thread so you
            can link to the announcement
        2.  hide beta downloads
        3.  move current release to previous
        4.  replace current with new links
        5.  ~~update Google Analytics labels~~
    2. Update frontpage / features page / etc.
    3. Update screenshot downloads on Press page.
    4. Update credits for contributors to latest release.
    5. Update <https://mixxx.org/manual/latest> symlink to point to
        2.3.
    7. Update copyright date here and on the blog
12. Release announcement:
    1. Discourse is updated automatically after publishing the blog post and visiting it on the website
    2. Cross-post to Zulip \#announce stream
    3. Cross-post to mixxx-devel~~
    4. Cross-post to Facebook
    5. Cross-post to Twitter
    

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
        -- Boost Post $$ (optional)
    2.  Twitter
    3.  LinkedIn Connected DJs group
    4.  Reddit r/DJs, r/Mixxx, r/linuxaudio, r/linux
    5.  DJTechTools Forums
    6.  TranceAddict Forums
    7.  omgubuntu.co.uk
    8.  YouTube channels
        1. Crossfader: https://www.youtube.com/channel/UCM4u0gp8gm99w9MXQ7ZI8Mw
        2. ~~unfa: https://www.youtube.com/user/unfa00~~ ([stepped down iiuc](https://www.youtube.com/watch?v=GHx6qyQZNjc))
    9.  librearts.org
9.  Update [SourceForge](https://sourceforge.net/projects/mixxx/) to
    point people to the newest version

## Post-Release

1.  Create 2.4 branch in mixxx manual and vcpkg 
2.  Update `main` README, CMakeList.txt for 2.5 
3.  Remove beta PPA upload in the 2.3 branch from .github/workflow/build.yml  
