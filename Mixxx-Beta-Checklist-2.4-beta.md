# Mixxx Beta Checklist 2.4

This process is followed when it is time to branch out a new beta and make the main branch a new alpha 

1. ✓ Update translations
    1.  Push and pull translations for Mixxx as described here:
        [Internationalization](Internationalization)
2. Update files from Git log
    1. credits in src/dialog/dlgabout.cpp
    2. CHANGELOG.md
3. Bump the version in main to 2.5-alpha 
    1. in CMakeLists.txt
    2. in License
    3. define a new resource branch in .tx/config (It will be created online via `tx push -s`)
    4. add a new section in CHANGELOG.md 
