# Mixxx Beta Checklist 2.4

This process is followed when it is time to branch out a new beta and make the main branch a new alpha 

1. Update translations in [manual](https://github.com/mixxxdj/manual)
    1.  Push and pull translations for the Manual as described here:
        [Internationalization](https://github.com/mixxxdj/manual#update-source-translations)
2. Bump the version in https://github.com/mixxxdj/manual main to 2.4
    1. source/conf.py: Update version and release
    2. define a new resource branch in .tx/config (It will be created online via `tx push -s`)
3. ✓ Update translations in [mixxx](https://github.com/mixxxdj/mixxx)
    1.  Push and pull translations for Mixxx as described here:
        [Internationalization](Internationalization)
4. Update files from Git log in [mixxx](https://github.com/mixxxdj/mixxx)
    1. credits in src/dialog/dlgabout.cpp
    2. CHANGELOG.md
5. Bump the version in [mixxx](https://github.com/mixxxdj/mixxx) main to 2.5-alpha 
    1. in CMakeLists.txt: Update VERSION and MIXXX_VERSION_PRERELEASE
    2. in License
    3. define a new resource branch in .tx/config (It will be created online via `tx push -s`)
    4. add a new section in CHANGELOG.md 

