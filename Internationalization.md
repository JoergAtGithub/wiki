# i18n/l10n and Mixxx

## Steps to Update Qt/POT templates in Mixxx branches

  - **Make a clean checkout of the branch you are in. NO EXCEPTIONS**
  - `lupdate src/\*\*/\*\* -ts res/translations/mixxx.ts`
  - `ts2po -P res/translations/mixxx.ts >
    res/translations/mixxx/mixxx.pot`
  - Commit, push.

Launchpad will pick up the changes to the template automatically.

## Steps to Merge Translations (PO's) from Launchpad

  - From the branch you'd like to merge into:
  - `bzr merge lp:~mixxxdevelopers/mixxx/BRANCH_translations`
  - Replace `BRANCH` above with the branch you would like to merge
    translation from (e.g. `trunk` or `1.9`)
