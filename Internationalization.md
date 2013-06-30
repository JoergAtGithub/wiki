# Translating Mixxx

FIXME **Work in progress-** --- *[jus](jus) 2013/06/30 09:03*

## Introduction

### Recommended skills for Translators

  - Computer experience -- being able to comfortably use the tools
    required in the translation process, like looking up difficult words
    in online dictionaries.
  - Experience in Djìng and using audio software -- you'll benefit from
    it because you already know the typical concepts and terms.
  - Bilingual -- fluent in both written English and the language(s) you
    will be translating into. Casual knowledge of either one will make
    translating difficult for you, or make the localization you create
    confusing to native speakers.
  - You should be familiar with human language constructs: nouns, verbs,
    articles, etc., different types of each, and be able to identify
    variations of their contexts in English.

### About Locales

Locales customize programs to languages and regional dialects. Often
locales correspond to countries, as is the case with Portuguese
(Portugal) and Portuguese (Brazil).

You can do a translation for any locale, such as German (Germany)
(de\_DE) or German (Austria) (de\_AT), to adjust for regional spelling
and idioms. A locale will define how characters are sorted, how the date
and time are represented, the names of the days of the week and months
of the year.

The default locale of Mixxx is English (United States) (en\_US).

## Special characters

### Ampersands (&)

Some texts in the translation template contain an ampersand (&) followed
by one char. This marks the letter which can be used to quickly access
that particular menu or other GUI element when holding the ALT key,
often called "Accelerator key".

If a string to be translated has an ampersand (&) in it, then the
translation for that string should also have an ampersand in it,
preferably in front of the same character. Accelerators should be unique
per menu (e.g. something like "\&Save" and "\&Save as" won't work, but
"\&Save" and "Save \&as" will do).

##### Example

| Source (English,en\_US) | Translation (German,de\_DE) | Comment                                                                                                                                                                                        |
| ----------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `&File`                 | `&Datei`                    | Pressing the shortcut **Alt+F** on the keyboard will access the **File** menu on top of the Mixxx application window. Using Mixxx with the german translation, the shortcut will be **Alt+D**. |

### Variables (%1,%2, ...)

Variables like %1, %2, %3, etc. will be replaced with actual contents on
runtime of the program. The variables of the original string must all
show up in the translation, Only change the variable placement inside
the translation if it is necessary to adapt to the sentence structure
and word order of your language.

##### Example

| Source (English,en\_US) | Translation (German,de\_DE) | Comment                                                                                                                                                                                                                                                                                                                                 |
| ----------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Analyzing %1/%2 %3%`   | `Analysiere %1/%2 %3%`      | When analyzing tracks, a progress label is displayed which shows the current track number (%1), the overall number of tracks in the analyze queue (%2) and the analysis progress of the current track (%3) in percent (%). So it becomes **Analyzing 10/15 50%** or, using Mixxx with the german translation, **Analysiere 10/15 50%**. |

### HTML tags (\</a\>, \<br/\>, \</b\>)

Here and there you may encouter some small bits of HTML code in the
source strings. Simply copy/paste them onto your translated string.

##### Example

| Source (English,en\_US)                            | Translation (German,de\_DE)                           | Comment                                                                                                                                                                                                 |
| -------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<a href="http://mixxx.org/">Official Website</a>` | `<a href="http://mixxx.org/">Offizielle Webseite</a>` | A link to the Mixxx website is shown in the **About** window, like **[Official Website](http://mixxx.org/)** or, using Mixxx with the german translation, **[Offizielle Webseite](http://mixxx.org/)**. |

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
  - Add all new translation translation TS and QM files to Git
  - In ZSH: `git add res/translations/mixxx_*.(ts|qm)`
  - **Update res/mixxx.qrc file to add any new languages that were not
    previously present.**
  - Commit, push.

**TODO:** make the sconscript do this as part of a normal build so Mixxx
contains the latest translations.
