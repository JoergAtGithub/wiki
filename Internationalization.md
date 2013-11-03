# Translating Mixxx

FIXME **Work in progress-** --- *[jus](jus) 2013/07/21*

## Introduction

### Why translate ?

Mixxx is written and documented in English, and use English for
communication between developers, maintainers and users from all
countries. However, English is not the primary language of most people,
and they are more comfortable with their own native language.

Translating helps to reach a wider audience, provides a better user
experience, and you can DJ using Mixxx in your mother tongue.

### About Locales

Locales customize programs to languages and regional dialects. Often
locales correspond to countries, as is the case with Portuguese
(Portugal) and Portuguese (Brazil). The default locale of Mixxx is
English (United States) (en\_US).

You can do a translation for any locale, such as German (Germany)
(de\_DE) or German (Austria) (de\_AT), to adjust for regional spelling
and idioms. A locale will define how characters are sorted, how the date
and time are represented, the names of the days of the week and months
of the year.

## Getting Started

### I want to help translate Mixxx, what do I need to do ?

You need a translator account to access
[Transifex](https://www.transifex.com/), our translation site. Sign up
for a free translator account or use your existing social network
credentials to login <https://www.transifex.com/signin/?next=/signup/#>.

### What about the skills required for translating ?

  - Bilingual -- fluent in both written English and the language(s) you
    will be translating into. Casual knowledge of either one will make
    translating difficult for you, or make the localization you create
    confusing to native speakers.
  - You should be familiar with human language constructs: nouns, verbs,
    articles, etc., different types of each, and be able to identify
    variations of their contexts in English.
  - Experience in Djìng and using audio software in general -- you'll
    benefit from it because you already know the typical concepts and
    terms.

To keep your translations consistent with those of other translators,
our
[glossary](https://www.transifex.com/projects/p/mixxxdj/glossary/l/en/)
helps you to get familiar with the core features of Mixxx. It contains a
collection of terms with definitions, uses, and associated notes.

### Ok, I have my Transifex account and I am ready to get busy. How to translate then?

[Log in](https://www.transifex.com/signin/?next=/home/), go to the
[Mixxx Translation Project
Overview](https://www.transifex.com/projects/p/mixxxdj/) and request
access to a translation team for the language(s) you want to translate
(German in this example). One of the developers or translation
coordinators will approve your request. You should get an e-mail answer
within 48 hours that you have been accepted to the team for the
requested language.

|                                                     |
| --------------------------------------------------- |
| [[/media/i18n/transifex_join_a_translation-team.gif|]]    |
| **Request to join a translation team on Transifex** |

Now that you have been accepted to the translation team, you are ready
to to translate Mixxx from English to your language.

  - Go to the [Mixxx Translation Project
    Overview](https://www.transifex.com/projects/p/mixxxdj/)
  - Click on your team's language, you will see available “language
    resources” to be translated.
  - Click on a available resource to proceed.
  - A pop-up window opens, click the **Translate Now** button.
  - The Web Editor opens, and displays all translatable strings.
  - Click on the **Untranslated** tab to search for all strings with
    missing translations.
  - Select a source string from the navigation panel to the left and
    type your translation into the box to the right.
  - Click the **Save** button to save your translated string.
  - Congrats, you just translated your first string in Mixxx. Easy.

|                                                              |
| ------------------------------------------------------------ |
| [[/media/i18n/transifex_submit_translation_using_web_editor.gif|]] |
| **Submit a translation using the web editor**                |

As a translator, you will be spending most of your time in the
translation editor. It's the place where you can see all the text
(strings) that need to be translated, submit translations, and
collaborate with others. Take a look at Transifex' [Introduction to the
Web
Editor](http://support.transifex.com/customer/portal/articles/972120-introduction-to-the-web-editor)
to get acquainted with the basics.

Should you run into any questions about using Transifex, check out their
[support
portal](http://support.transifex.com/customer/portal/topics/414107-translators/articles).

### How can i be notified for languages I translate?

You can get notified whenever the translation of a resource is modified.
When watching Mixxx or one of its languages, you will receive email
notifications, whenever the translation sources are updated and there is
translation work to be done.

You can find the links to watch Mixxx or a specific language at the
bottom of the [main
project](https://www.transifex.com/projects/p/mixxxdj/) and language
page respectively. You can also subscribe to the [Mixxx translation
RSS-feed](https://www.transifex.com/projects/p/mixxxdj/feed/)

## Resources

### Glossaries

A glossary makes the translation process much easier for translators as
terms have agreed-upon definitions and translations, shortening the
amount of time required to translate Mixxx.

  - [Mixxx
    glossary](https://www.transifex.com/projects/p/mixxxdj/glossary/l/en/)
    - The Mixxx glossary in english, translatable to your own language.
  - [microsoft.com/Language](https://www.microsoft.com/Language) -
    Search Microsoft’s terminology and glossaries in 70 languages.
  - [developer.apple.com](https://developer.apple.com/downloads/index.action?name=localization)
    - Download Apple OS X glossaries.

### Translation memory (TM)

TM systems promote quality and consistency. They provide automatic
suggestions based on similarities between source strings, allowing
translators to leverage previous translations. Translators can use TM
suggestions or adjust them to create new, more contextually appropriate
translations.

  - [Mixxx TM](https://www.transifex.com/projects/p/mixxxdj/) - The
    available TM entries are under the ‘suggestions’ tab of each
    translatable string of your language.
  - [open-tran.eu](http://open-tran.eu/) - Memory Translation database
    of open source projects.
  - [mymemory.translated.net](http://mymemory.translated.net/) - The
    world largest collaborative translation archive.

### Online Translation and Dictionaries

``` 
 * [[https://www.transifex.com/projects/p/mixxxdj/|Mixxx Auto Translate]] - Click ‘Machine Translation’ next to the ‘Submit’ button of the translatable string of your language.
 * [[http://www.yourdictionary.com/|yourdictionary.com]] - The easiest to use on-line dictionary and thesaurus. Clear. Clean. Uncluttered.
 * [[http://tradukka.com/|tradukka.com]] - Translate in real time with definitions and forums for your questions.
 * [[http://www.omegawiki.org/|omegawiki.org]] - A multilingual dictionary with lexicological, terminological and thesaurus information.
 * [[http://imtranslator.net/translation/|imtranslator.net]] - Provides dictionaries and instant translation of words, phrases and texts in many languages.
```

### Offline Translation software

If you are more comfortable translating locally on your computer,
instead online in a web browser.

  - [Qt Linguist](http://qt-project.org/doc/qt-4.8/linguist-manual.html)
    - Provides a set of tools that speed the translation and
    internationalization of applications. Windows, Linux, MacOS X FIXME
    <sup>Add DL Links to standalone Linguist binaries</sup>
    *\[\[|jus\]\] 2013/07/21*
  - [Lingoes](http://www.lingoes.net/) - An easy and intuitive
    dictionary and text translation software. Windows
  - [Virtaal](http://virtaal.translatehouse.org/) - A feature rich
    translation tool that allows you to focus on translation. Windows,
    Linux, MacOS X
  - [Lokalize](http://www.kde.org/applications/development/lokalize/) -
    A computer-aided translation system that focuses on productivity and
    quality assurance. Windows, Linux

## Common Pitfalls in Translation

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

  - lupdate and lrelease, part of [Qt development
    toolkit](http://qt-project.org/downloads)
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
