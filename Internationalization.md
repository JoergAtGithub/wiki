# Translators

FIXME **Work in progress-** --- *\[\[|jus\]\] 2013/02/03 16:13*

## Ampersands (&)

Some texts in the translation template contain an ampersand (&). This
marks the letter which can be used to quickly access that particular
menu or other GUI element. For example "\&File" means that pressing
*Alt+F* on the keyboard can be used to access the *File* menu on top of
the Mixxx application window.

If a string to be translated has an ampersand (&) in it, then the
translation for that string should also have an ampersand in it,
preferably in front of the same character. In our example, it might be
translated to "\&Datei" in German.

# Developers - i18n/l10n and Mixxx

Required tools to update translations are:

  - lupdate and lrelease, part of qt development toolkit
  - po2ts and ts2po, part of [Translate
    Toolkit](http://translate.sourceforge.net/wiki/toolkit/index)

## Updating translation templates

*This procedure extracts translatable strings from Mixxx's code into
template files (Qt/POT) so that Launchpad's interface can present the
most current strings to translators.*

  - **Make a clean checkout of the Mixxx code branch you are in. NO
    EXCEPTIONS**
  - `lupdate src -recursive -extensions cpp,h,ui -ts
    res/translations/mixxx.ts`
  - `ts2po -P -i res/translations/mixxx.ts -o
    res/translations/mixxx/mixxx.pot`
  - Commit, push.

Launchpad will pick up the changes to the template automatically.

**TODO:** make the sconscript do this as part of a normal build so code
changes that change or add strings automatically update the templates.

## Updating translations

*This procedure updates Mixxx with translations (PO files) that have
been contributed by Launchpad users.*

  - For every PO file in res/translations/mixxx/, `po2ts
    res/translations/mixxx/xx.po res/translations/mixxx_xx.ts`
  - In ZSH: `for XX in res/translations/mixxx/*.po; do po2ts -i $XX -o
    res/translations/mixxx_${$(basename $XX)%.*}.ts; done`
  - For every mixxx\_xx.ts file in res/translations/, `lrelease
    res/translations/mixxx_xx.ts -qm res/translations/mixxx_xx.qm`
  - In ZSH: `for XX in res/translations/mixxx_*.ts; do lrelease
    -nounfinished $XX -qm res/translations/${$(basename $XX)%.*}.qm;
    done`
  - If you are testing a translation and would like untranslated strings
    to show up as blank, do not give the 'nounfinished' argument to
    lrelease.
  - Add all new translation translation TS and QM files to Bazaar
  - In ZSH: `bzr add res/translations/mixxx_*.(ts|qm)`
  - **Update res/mixxx.qrc file to add any new languages that were not
    previously present.**
  - Commit, push.

**TODO:** make the sconscript do this as part of a normal build so Mixxx
contains the latest translations.
