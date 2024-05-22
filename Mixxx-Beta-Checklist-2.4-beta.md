# Mixxx Beta Checklist 2.4

This process is followed when it is time to branch out a new beta and make the main branch a new alpha 

1. Update translations in [manual](https://github.com/mixxxdj/manual)
    1.  Push and pull translations for the Manual as described here:
        [Internationalization](https://github.com/mixxxdj/manual#update-source-translations)
2. Bump the version in https://github.com/mixxxdj/manual main to 2.5
    1. create a new Project on Transiflex "Mixxx DJ manual 2.5"
    2. source/conf.py: Update version and release
    3. edit the .tx/config file to point to the new project "mixxx-dj-manual-25"
    4. `git commit -a -m"Bump version to 2.5"`
    5. `git push upstream main`
    6. upload translation sources source and the existing translations `tx push -s -t`
3. Create a 2.4 branch in [manual](https://github.com/mixxxdj/manual)
    1. `git checkout -b 2.4 upstream/main~1`
    2.  edit the .tx/config file github_version to the new branch 2.4
    3. `git commit -a -m"Redirect \"Edit on GitHub\" links to the new branch"`
    4. `git push upstream 2.4`
4. ✓ Update translations in [mixxx](https://github.com/mixxxdj/mixxx)
    1.  Push and pull translations for Mixxx as described here:
        [Internationalization](Internationalization)
5. Update files from Git log in [mixxx](https://github.com/mixxxdj/mixxx)
    1. credits in src/dialog/dlgabout.cpp
    2. CHANGELOG.md
6. Bump the version in [mixxx](https://github.com/mixxxdj/mixxx) main to 2.5-alpha. Required to avoid two concurrent 2.4 versions in two branches.  
    1. in CMakeLists.txt: Update VERSION and MIXXX_VERSION_PRERELEASE
    2. in License
    3. define a new resource branch in .tx/config (It will be created online via `tx push -s`)
    4. add a new section in CHANGELOG.md 
7. Add a git tag with a GPG signature 
    1. ```git tag -s 2.5-alpha -m "Mixxx 2.5-alpha"```  (double check identity / email you are using to tag!)
    2. ```git push --tags upstream 2.5-alpha```
    3.  This can be done to a commit after it has been pushed or merged
        from the release candidate PR, so wait until you're sure you're ready to tag the
        release commit.
    4.  **Once pushed, a tag is forever. Never delete a tag from a
        remote.**
8. Create a new branch [2.4](https://github.com/mixxxdj/mixxx/tree/2.4) from the commit before changing the version number
9. Polish the 2.4-alpha for beta tests 
10. Prepare a News PR announcing the new 2.4-beta version  
11. Bump the version in [2.4](https://github.com/mixxxdj/mixxx/tree/2.4) to 2.4-beta 
    1. in CMakeLists.txt: Update VERSION and MIXXX_VERSION_PRERELEASE
    2. in License
12. Add a git tag with a GPG signature 
    1. ```git tag -s 2.4-beta -m "Mixxx 2.4-beta"```  (double check identity / email you are using to tag!)
    2. ```git push --tags upstream 2.4-beta```
    3.  This can be done to a commit after it has been pushed or merged
        from the release candidate PR, so wait until you're sure you're ready to tag the
        release commit.
    4.  **Once pushed, a tag is forever. Never delete a tag from a
        remote.**
13. Publish the News Post 
14. Update the download page 
14. Publish at social media 