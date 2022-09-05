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
    6. upload translation sources source `tx push -s`
    7. upload the existing translations `tx push -t`
3. Create a 2.4 branch in [manual](https://github.com/mixxxdj/manual)
    1. `git checkout -b 2.4 upstream/main`
    2. `git push upstream 2.4
4. ✓ Update translations in [mixxx](https://github.com/mixxxdj/mixxx)
    1.  Push and pull translations for Mixxx as described here:
        [Internationalization](Internationalization)
5. Update files from Git log in [mixxx](https://github.com/mixxxdj/mixxx)
    1. credits in src/dialog/dlgabout.cpp
    2. CHANGELOG.md
6. Bump the version in [mixxx](https://github.com/mixxxdj/mixxx) main to 2.5-alpha 
    1. in CMakeLists.txt: Update VERSION and MIXXX_VERSION_PRERELEASE
    2. in License
    3. define a new resource branch in .tx/config (It will be created online via `tx push -s`)
    4. add a new section in CHANGELOG.md 

