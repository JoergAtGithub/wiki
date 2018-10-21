====== Translating Mixxx ======

===== Introduction =====

==== Why translate ? ====
Mixxx is written and documented in English, and use English for communication between developers, maintainers and users from all countries. However, English is not the primary language of most people, and they are more comfortable with their own native language.

Translating helps to reach a wider audience, provides a better user experience, and you can DJ using Mixxx in your mother tongue.

==== What about the skills required for translating ? ====

  * Bilingual -- fluent in both written English and the language(s) you will be translating into. Casual knowledge of either one will make translating difficult for you, or make the localization you create confusing to native speakers.
  * You should be familiar with human language constructs: nouns, verbs, articles, etc., different types of each, and be able to identify variations of their contexts in English.
  * Experience in Djìng and using audio software in general -- you'll benefit from it because you already know the typical concepts and terms.

To keep your translations consistent with those of other translators, our [[https://www.transifex.com/projects/p/mixxxdj/glossary/l/en/|glossary]] helps you to get familiar with the core features of Mixxx. It contains a collection of terms with definitions, uses, and associated notes.

==== About Locales ====
Locales customize programs to languages and regional dialects. Often locales correspond to countries, as is the case with Portuguese (Portugal) and Portuguese (Brazil). The default locale of Mixxx is English (United States) (en_US).

You can do a translation for any locale, such as German (Germany) (de_DE) or German (Austria) (de_AT), to adjust for regional spelling and idioms. A locale will define how characters are sorted, how the date and time are represented, the names of the days of the week and months of the year.

===== Getting Started =====

==== I want to help translate Mixxx, what do I need to do ? ====


Learn how you can help translate content that’s on Transifex, our translations management provider. This guide will walk you through:

  * Signing up for an account
  * Joining a translation team
  * Finding and translating content

https://docs.transifex.com/getting-started/translators


==== Ok, I have my Transifex account and I am ready to get busy. How to translate then? ====

  * [[https://www.transifex.com/signin/?next=/home/|Log in]]
  * Go to the [[https://www.transifex.com/mixxx-dj-software/public/|Mixxx Translation Project Dashboard]]
  * Select from a available a projects (application, manual, website etc.)
  * Hover over a language and requesting to join the project's team.
  * Click **Join Team**, select a language and accept the CLA, finish by clicking **Join**
  * Click on the projects **Translate** button.
  * The Web Editor opens, and displays all translatable strings.
  * Click on the **Untranslated** tab to search for all strings with missing translations.
  * Select a source string from the navigation panel to the left and type your translation into the box to the right.
  * Click the **Save** button to save your translated string.
  * Congrats, you just translated your first string in Mixxx. Easy.

|   {{ :i18n:transifex_submit_translation_using_web_editor.gif |}}     |
^   **Submit a translation using the web editor**       ^

As a translator, you will be spending most of your time in the translation editor. It's the place where you can see all the text (strings) that need to be translated, submit translations, and collaborate with others. Take a look at Transifex' [[https://docs.transifex.com/translation/translating-with-the-web-editor|Introduction to the Web Editor]] to get acquainted with the basics.

Should you run into any questions about using Transifex, check out their [[https://docs.transifex.com/|support portal]].

==== How can i be notified for languages I translate? ====

You can get notified whenever the translation of a resource is modified. When watching Mixxx or one of its languages, you will receive email notifications, whenever the translation sources are updated and there is translation work to be done.

You can find the links to watch Mixxx or a specific language at the bottom of the [[https://www.transifex.com/projects/p/mixxxdj/|main project]] and language page respectively. You can also subscribe to the [[https://www.transifex.com/projects/p/mixxxdj/feed/|Mixxx translation RSS-feed]]

===== Resources =====

==== Glossaries ====

A glossary makes the translation process much easier for translators as terms have agreed-upon definitions and translations, shortening the amount of time required to translate Mixxx.

  * [[https://www.transifex.com/projects/p/mixxxdj/glossary/l/en/|Mixxx glossary]]  - The Mixxx glossary in english, translatable to your own language.
  * [[https://www.microsoft.com/Language|microsoft.com/Language]] - Search Microsoft’s terminology and glossaries in 70 languages.
  * [[https://developer.apple.com/downloads/index.action?name=localization|developer.apple.com]] - Download Apple OS X glossaries.

==== Translation memory (TM) ====

TM systems promote quality and consistency. They provide automatic suggestions based on similarities between source strings, allowing translators to leverage previous translations. Translators can use TM suggestions or adjust them to create new, more contextually appropriate translations.

  * [[https://www.transifex.com/projects/p/mixxxdj/|Mixxx TM]] - The available TM entries are under the ‘suggestions’ tab of each translatable string of your language.
  * [[http://open-tran.eu/|open-tran.eu]] - Memory Translation database of open source projects.
  * [[http://mymemory.translated.net/|mymemory.translated.net]] - The world largest collaborative translation archive.

==== Online Translation and Dictionaries ====

   * [[http://www.yourdictionary.com/|yourdictionary.com]] - The easiest to use on-line dictionary and thesaurus. Clear. Clean. Uncluttered.
   * [[http://tradukka.com/|tradukka.com]] - Translate in real time with definitions and forums for your questions.
   * [[http://www.omegawiki.org/|omegawiki.org]] - A multilingual dictionary with lexicological, terminological and thesaurus information.
   * [[http://imtranslator.net/translation/|imtranslator.net]] - Provides dictionaries and instant translation of words, phrases and texts in many languages.

==== Offline Translation software ====

If you are more comfortable translating locally on your computer, instead online in a web browser.

  * [[https://doc.qt.io/qt-5/qtlinguist-index.html|Qt Linguist]] - Provides a set of tools that speed the translation and internationalization of applications. Windows, Linux, macOS
  * [[http://www.lingoes.net/| Lingoes]] - An easy and intuitive dictionary and text translation software. Windows
  * [[http://virtaal.translatehouse.org/|Virtaal]] - A feature rich translation tool that allows you to focus on translation. Windows, Linux, macOS
  * [[http://www.kde.org/applications/development/lokalize/|Lokalize]] - A computer-aided translation system that focuses on productivity and quality assurance. Windows, Linux

===== Common Pitfalls in Translation =====

==== Ampersands (&) ====
Some texts in the translation template contain an ampersand (&) followed by one char.
This marks the letter which can be used to quickly access that particular menu or other GUI element when holding the ALT key, often called "Accelerator key".

If a string to be translated has an ampersand (&) in it, then the translation for that string should also have an ampersand in it, preferably in front of the same character. Accelerators should not show up twice in the same menu to prevent "accelerator clashes". E.g. something like "&Save" and "&Save as" won't work, but "&Save" and "Save &as" will do.

== Example ==

^ Source (English,en_US)      ^ Translation (German,de_DE)                 ^ Comment         ^
| ''&File''            | ''&Datei''                   | Pressing the shortcut **Alt+F** on the keyboard will access the **File** menu on top of the Mixxx application window. Using Mixxx with the german translation, the shortcut will be **Alt+D**.            |
==== Variables (%1,%2, ...) ===
Variables like %1, %2, %3, etc. will be replaced with actual contents on runtime of the program. The variables of the original string must all show up in the translation, Only change the variable placement inside the translation if it is necessary to adapt to the sentence structure and word order of your language.

== Example ==

^ Source (English,en_US)      ^ Translation (German,de_DE)                 ^ Comment         ^
| ''Analyzing %1/%2 %3%''            | ''Analysiere %1/%2 %3%''                   | When analyzing tracks, a progress label is displayed which shows the current track number (%1), the overall number of tracks in the analyze queue (%2) and the analysis progress of the current track (%3) in percent (%). So it becomes **Analyzing 10/15 50%** or, using Mixxx with the german translation, **Analysiere 10/15 50%**.           |

==== HTML tags (</a>, <br/>, </b>, </ul>) ====

Here and there you may encounter some small bits of HTML code in the source strings. Simply copy/paste them onto your translated string.
When translating in the Transifex Web editor, red arrows indicate that there is a newline character (Enter) in that position of the source string. Since that newline can be extremely important when the string is displayed in Mixxx being localized, translators are highly encouraged to adjust their translations as accurately as possible, by pressing the “Enter” key in the closest position possible.

== Example ==

^ Source (English,en_US)      ^ Translation (German,de_DE)                 ^ Comment         ^
| ''<a href="http://mixxx.org/">Official Website</a>''            | ''<a href="http://mixxx.org/">Offizielle Webseite</a>''                   | A link to the Mixxx website is shown in the **About** window, like **[[http://mixxx.org/|Official Website]]** or, using Mixxx with the german translation, **[[http://mixxx.org/|Offizielle Webseite]]**.
           |

====== Developers - i18n/l10n and Mixxx ======

===== Tools ====
The following tools are used to update the Mixxx translation templates and to merge updated translations submitted by translators.

**Required**
  * //lupdate// and //lrelease//, part of [[http://qt-project.org/downloads|Qt development toolkit]]
  * [[https://docs.transifex.com/client/installing-the-client|Transifex CLI- client]]

**Optional**
  * [[http://www.zsh.org/|Zsh]] (Z shell), a powerful shell that operates as both an interactive shell and as a scripting language interpreter.

==== Installation example ====

===macOS===
  * Install the [[https://www.qt.io/download|Qt development toolkit]]
  * Install the [[https://docs.transifex.com/client/installing-the-client|Transifex CLI- client]]
      * <code>sudo easy_install pip 
sudo pip install transifex-client</code>
  * Optional, install Zsh using [[https://brew.sh/|Brew]]
      * <code>brew install zsh</code>

===== Updating translation templates =====

//This procedure extracts translatable strings from Mixxx's code into QT template files (*.ts) so that Transifex' interface can present the most current strings to translators. Check the required [[https://docs.transifex.com/teams/understanding-user-roles|user permissions on Transifex]]//

  * **Make a clean checkout of the Mixxx code branch you are in. NO EXCEPTIONS**
  * Update source template
  * <code>lupdate src -recursive -noobsolete -extensions cpp,h,ui -ts res/translations/mixxx.ts</code>
  * Commit changes to HEAD
  * <code>git commit -a -m "Update Translation template. Found XXXX source text(s) (XX new and XXXX already existing)"</code>
  * Push changes to remote repository
  * <code>git push origin branchname</code>
  * If you are a maintainer, create a credetial file ~/.transifexrc
  * <code>[https://www.transifex.com]
api_hostname = https://api.transifex.com
hostname = https://www.transifex.com
password = ******
token = 
username = user
</code> 

  * Push changed *.ts template (the translation source file) to Transifex
  * <code>tx push -s</code>

Transifex will pick up the changes to the template after a short while, and notify maintainers/subscribers by email.

**TODO:** make the sconscript do this as part of a normal build so code changes that change or add strings automatically update the templates.

===== Updating translations =====

//This procedure updates Mixxx with translations (*.ts files) that have been contributed by Transifex users.//

  * Fetch all translation files from Transifex, even ones which don’t exist already locally. If the option ''-a'' isn’t included, only the files that exist locally will be updated Transifex. The working directory for these instructions is the root of the repository.
  * <code>tx pull -a -f --parallel --minimum-perc 1</code>
  * Note: If you only want to pull translations for a subset of [[https://github.com/mixxxdj/mixxx/blob/master/.tx/config|Mixxx resources]], use -l lang instead of -a. For more information see [[https://docs.transifex.com/client/pull#pulling-specific-sets-of-translation-files| Transifex docs]].
  * For every mixxx_xx.ts file in res/translations/, <code>lrelease -nounfinished res/translations/mixxx_xx.ts -qm res/translations/mixxx_xx.qm</code>
  * In ZSH: <code>for XX in res/translations/mixxx_*.ts; do lrelease -nounfinished $XX -qm res/translations/${$(basename $XX)%.*}.qm; done</code>
  * In bash: <code>for XX in res/translations/mixxx_*.ts; do lrelease -nounfinished $XX -qm ${XX/%.ts/.qm}; done</code>
  * If you are testing a translation and would like untranslated strings to show up as blank, do not give the 'nounfinished' argument to lrelease.
  * Add all new translation translation TS and QM files to Git
  * In ZSH: <code>git add res/translations/mixxx_*.(ts|qm)</code>
  * **Update res/mixxx.qrc file to add any new languages that were not previously present.**
  * Commit changes to HEAD
  * <code>git commit -m "Pull latest translations from https://www.transifex.com/mixxx-dj-software/mixxxdj/branchname/. Compile QM files out of TS files that are used by the localized app"</code>
  * Push changes to remote repository
  * <code>git push origin branchname</code>

**TODO:** make the sconscript do this as part of a normal build so Mixxx contains the latest translations.

Note: The process for updating the translations of Mixxx windows installer is documented in the [[https://github.com/mixxxdj/mixxx/blob/master/build/wix/Localization/README-Translations.md|Github branch]]
