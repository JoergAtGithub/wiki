# i18n/l10n and Mixxx

## Steps to Update Qt/POT templates in Mixxx branches

  - **Make a clean checkout of the branch you are in. NO EXCEPTIONS**
  - `lupdate src -recursive -extensions cpp,h,ui -ts
    res/translations/mixxx.ts`
  - `ts2po -P -i res/translations/mixxx.ts -o
    res/translations/mixxx/mixxx.pot`
  - Commit, push.

Launchpad will pick up the changes to the template automatically.

## Steps to Merge Translations (PO's) from Launchpad

  - From the branch you'd like to merge into:
  - `bzr merge lp:~mixxxdevelopers/mixxx/BRANCH_translations`
  - Replace `BRANCH` above with the branch you would like to merge
    translation from (e.g. `trunk` or `1.9`)
  - For every PO file in res/translations/mixxx/, `po2ts
    res/translations/mixxx/xx.po res/translations/mixxx_xx.ts`
  - In Bash: `for XX in res/translations/mixxx/*.po; do po2ts $XX
    res/translations/mixxx_${$(basename $XX)%.*}.ts; done`
  - For every mixxx\_xx.ts file in res/translations/, `lrelease
    res/translations/mixxx_xx.ts -qm res/translations/mixxx_xx.qm`
  - In Bash: `for XX in res/translations/mixxx_*.ts; do lrelease $XX -qm
    res/translations/${$(basename $XX)%.*}.qm; done`
  - Update res/mixxx.qrc file to add any new languages that were not
    previously present.
