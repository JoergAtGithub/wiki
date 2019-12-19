### 1\. MIXXX support

Traktor uses XML to store metadata. Currently MIXXX imports the
filenames, but not the cue points.

  - MIXXX user request: <https://bugs.launchpad.net/mixxx/+bug/1475416>
  - MIXXX patch: <https://github.com/mixxxdj/mixxx/pull/1411>
  - MIXXX other formats:
    <https://mixxx.org/wiki/doku.php/other_programs_cue_storage_formats>

### 2\. Alternatives

There are several programs that are able to achieve this conversion. The
most complete programs are proprietary and for MacOS only. Windows users
and/or opensource is a lot more limited.

##### Proprietary programs:

  - [Rekord Buddy](http://nextaudiolabs.com/): two way sync between
    Traktor, RekordBox, Serato libraries. MacOS Only
  - [DJ Conversion Utility(DJCU)](https://sellfy.com/p/emUY/): Two way
    conversion from Traktor and Serato To/From Rekordbox.One way
    conversion from Virtual DJ to Rekordbox. One way conversion from
    Rekordbox to iTunes, djay Pro 2. The out put from one conversion
    step can serve as input for the next without the use of Rekordbox in
    between. With the aid from another app the Denon Conversion Utility
    (DeCU) DJCU can convert from all its source platforms to Denon Prime
    as well. MacOS Only
  - [CrossDJ](http://www.mixvibes.com/cross-dj-software-mac-pc/):
    Imports Traktor, exports Rekordbox. PC and Mac

##### Open Source programs (PC and Mac):

  - [alzadude
    converter](https://github.com/digital-dj-tools/dj-data-converter/releases):
    TK-\>RB conversion. Language Clojure. in active development as of
    jan 2019.
  - [ErikMinekus
    converter](https://github.com/ErikMinekus/traktor-scripts/blob/master/rekordbox-export.py):
    TK-\>RB conversion. Language is Python.
  - [Psobot traktor](https://github.com/psobot/traktor): Auto-generate
    cues for traktor XML. Language: Python 

### 3\. Cues shifted in time issue

All the above converters, and probably MIXXX in the future, are
susceptible to the following issue: For some mp3s, all cues will be
shifted in time for a constant number of samples. This issue depends on
the actual decoder definition of the 00:00:00 time point ( [more info
here](https://www.youtube.com/watch?v=Vl4nbvYmiP4))

Example: [[/media/crossdj_-_cues_shifted_in_time.png|]]

Only some converters specifically address this issue. Known successes
are:

  - [Rekordbuddy2 June
    beta 2.1.0(557)](https://forums.next.audio/t/traktor-rekordbox-cues-shifted-in-time-2/593):
    does conversion and correction in a single go
  - [DJCU](https://youtu.be/MAObe2e7qx4): does conversion and correction
    in a single step. DJCU uses the most advanced shift correction in
    the business. The Denon Conversion also has the automatic shift
    correction build in.

The other converters have been confirmed to be affected by this issue.

update: some research hints this issue is correlated with the specific
LAME encoder version:
<https://github.com/digital-dj-tools/dj-data-converter/issues/3>

### 4\. MacOS virtual Machine on Windows

Some Windows users are able to convert their collections using MacOS
VMs. The simplest method uses a full import/export to an external drive.
This is dramatically slow. A faster method uses an internal network
share, but it requires manipulation of the XML libraries. That extra
step can be made manually, or be scripted as well.

  - [Installing a MacOS VM in
    win 10](https://saintlad.com/install-macos-sierra-in-virtualbox-on-windows-10)
  - [using Rekordbuddy + external
    drive](https://www.reddit.com/r/Beatmatch/comments/52dvst/how_to_transfer_your_windowsbased_dj_library_from/)
  - [using DJCU + network
    drive](https://www.dropbox.com/s/4tyyi3me9tpm2uk/Windows%20Collection%20conversion%20whitepaper.pdf):
    note: this still requires a manual step
  - [bash scripts to run Rekorbuddy2 inside a
    VM](https://github.com/pestrela/music_scripts): fully automated
    process
