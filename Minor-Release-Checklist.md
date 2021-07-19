# Mixxx Minor Release Checklist

This process is followed when it is time for a minor release to the stable branch.


1. Source updates:
    1. Update CHANGELOG.md with significant user-visible changes / bugfixes
    1. Update CMakeLists.txt VERSION
6. Perform QA testing with release candidate binaries (Smoke Test) 
    1. macOS 
    2. Ubuntu
    3. Windows
7. Add a git tag with a GPG signature
    1. ```export VERSION=X.Y.Z``` 
    1. ```git tag -s $VERSION -m "Mixxx $VERSION"```  (double check identity / email you are using to tag!)
    2. ```git push --tags upstream $VERSION```
    3.  This can be done to a commit after it has been pushed or merged
        from the release candidate PR, so wait until you're sure you're ready to tag the
        release commit.
    4.  **Once pushed, a tag is forever. Never delete a tag from a
        remote.**
8. Verify release binaries are available
    1. https://downloads.mixxx.org/releases/2.3.0/
    2. https://launchpad.net/~mixxx/+archive/ubuntu/mixxx  
9. Release
    1.  Record SHA256sum of all packages in the [Release Checksums
        Google
        Doc](https://docs.google.com/spreadsheets/d/1E5vFa0gKf47P3LMMXpnr3JzsZ7-ENI03IgOkj9lxYQo/edit#gid=0)
        as a backup and record independent of downloads.mixxx.org (for
        forensic purposes).
    2. Make a release in GitHub 
    3.  Update Launchpad
        1.  Change "Fix committed" bugs to "Fix released"
11. Update the website
    1. Update download page:
        1.  Do this after posting the announcement forum thread so you
            can link to the announcement
        4.  replace current with new links
        5.  ~~update Google Analytics labels~~
12. Release announcement:
    1. Discourse is updated automatically after publishing the blog post and visiting it on the website
    2. Cross-post to Zulip \#announce stream
    4. Optional: Cross-post to Facebook
    5. Optional: Cross-post to Twitter
    

## Promotion

1.  Email package maintainers
    1.  Debian/Ubuntu - <https://packages.debian.org/testing/mixxx>
    2.  Gentoo
    3.  Arch - <http://www.archlinux.org/packages/?q=mixxx>
    4.  Fedora
8.  Social Media / Forums
    1.  [Facebook](https://www.facebook.com/Mixxx-DJ-Software-21723485212/)
    2.  Twitter
    3.  LinkedIn Connected DJs group
    4.  Reddit r/DJs, r/Mixxx, r/linuxaudio, r/linux
    5.  DJTechTools Forums
