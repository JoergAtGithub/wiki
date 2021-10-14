# Mixxx Minor Release Checklist

This process is followed when it is time for a minor release to the stable branch.


1. Source updates:
    1. Update CHANGELOG.md: Add list of significant user-visible changes / bugfixes. (PROBLEM: This is *very* hard right now, requiring Core Team members to weigh in on which PRs are "significant". We need to fix this step)
    1. Update CHANGELOG.md: Also add the actual date of the previous release.
    1. Update CMakeLists.txt: Increment VERSION (Looks like `project(mixxx VERSION X.Y.Z)`)
6. Perform Smoke testing with release candidate binaries (Does it launch, does it play music)
    1. macOS 
    2. Ubuntu
    3. Windows
7. Add a git tag with a GPG signature. (Should be signed by a Core Team member).
    1. Update CHANGELOG.md with the current date and push.  
    1. ```export VERSION=X.Y.Z``` 
    1. ```git tag -s $VERSION -m "Mixxx $VERSION"```  (double check identity / email you are using to tag!)
    2. ```git push --tags upstream $VERSION```
8. Wait and Verify release binaries are available
    1. https://downloads.mixxx.org/releases/X.Y.Z/
    2. https://launchpad.net/~mixxx/+archive/ubuntu/mixxx  
9. Release
    1. Make a release in GitHub
    2. Upload *source code and executables* to the [Internet Archive Software Collection](https://archive.org/details/software)
    3. Update Launchpad
        1.  Change "Fix committed" bugs to "Fix released"
10. Website updates:
    1. Create short news blog post. This can be a short copy of the changelog updates.
    1. Update website download page.
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
    4.  Reddit r/DJs, r/Mixxx, r/linuxaudio
    5.  DJTechTools Forums
