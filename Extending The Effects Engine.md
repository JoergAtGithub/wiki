**Extending the Effects Engine  
Nicu Badescu  
Email: badescunicu@gmail.com  
IRC: badescunicu  
Timezone: GMT +2**

**I. Overview**

Mixxx is widely used nowadays among both amateur and professional DJs.
Growing in popularity raises the bar when it comes down to quality and
users' expectations. We must keep up with our competitors in terms of
features and performance. Currently, Mixxx lacks a couple of effects
such as Brake, Phaser, Gater or Vocal Cut whereas other major DJ Mixing
products already provide similar effects. Consequently, I find this
project very important for improving Mixxx’s visibility and keeping it
in line with the competition.

**II. High Level Design and Implementation Details**

This project consists of two parts:

1\) EQ Effect:

  - replace the current static EQ signal path with an additional
    EffectChain containing the EQ effect;
  - it is the perfect way to learn the effect framework and its
    interaction with CO;
  - the target of this part is removing this line\[1\] by moving the
    logic inside EngineEffectsManager::process method;
  - the goal of this EQ Effect is allowing the user to disable the EQ as
    well as giving the possibility to replace the EQ with other similar
    effects or other advanced implementations.

Steps to follow:

  - create a new EffectChain which contains the current EQ (EQ which is
    going to be moved into the effect domain like Ryan is suggesting in
    the Bug Description \[2\]) and a filter effect;
  - turn the Bitcrusher into a Butterworth EQ by copying the Butterworth
    signal processing to the frame created by the Bitcrusher;
  - create a new EffectChain containing EQ EffectUnits;
  - connect the current EQ controls to the new effect units;

2\) Ability to load LV2 plugins into Mixxx

**III) Tentative Timeline:**

W1 May 19th - May 25th:

  - Turn the Bitcrusher into a Butterworth EQ

W2 May 26th - June 1st:

  - Final Plan how to move EQ into the effect domain
  - Fix <https://bugs.launchpad.net/mixxx/+bug/1209294>

W3 June 2nd - June 8th:

  - Implement switch type parameters for EQ "kill" buttons

W4 June 9th - June 15th

  - Continue to work on switch type parameters for EQ "kill" buttons
  - prepare a test skin
  - test and debug

W5 June 16th - June 22nd:

  - Final Plan how to move Brake into the effect domain \[postponed\]
  - prepare for midterm
  - start working on the EQ Effect Rack (not configurable from
    preferences)
  - June 18: create a new EffectRack
  - June 19: modify a skin (Deere or Daniel’s Shade) to display that
    Rack
  - June 20: add 4 EQ Effects to the newly created Rack
  - June 21: connect each EQ to one Deck

W6 June 23rd - June 29th (Mid Term evaluation):

  - Turn the Bitcrusher into a Brake effect \[postponed\]
  - Finish the EQ Effect Rack (configure it from preferences)
  - June 22-23: modify the Rack to use legacy controls (better: allow
    aliases for controls)
  - June 24: Allow the Rack EQs to be changed from preferences
    (LigthweightEQ or EQDefault)
  - June 25-26: debug and test
  - In dlgpref.cpp: Connect the button responsible for changing the EQ
    to a slot which calls a method on m\_pEffectsManager (we have to
    store a pointer to the EffectsManager). This method is changing the
    effect which is loaded onto the EffectUnit.

<!-- end list -->

``` 
    * Static creation of check boxes [done]
    * Store a pointer to the EQ Rack and connect signals for changing the effect to a slot of that rack [done]
    * Dynamically create a drop down list of available effects to put on the EQRack [done]
    * Use a QSignalMapper to avoid duplicate code for slots [done in a simpler way]
    * Dynamic creation of drop down lists based on [Master],num_decks [done by adding a drop down list whenever a new deck is added]
    * Add labels next to the drop down lists (make them look pretty) [done]
    * Connect "[Master],num_decks" control to a slot inside dlgprefeq.cpp [done]
    * Store the user's configuration of the EQ Rack[done]
```

W7 June 30th - July 6th:

  - Evaluate LV2 hosts

W8 July 7th - July 13th:

  - Final Plan how to move LV2 effect into the effect domain

W9 July 14th - July 20th:

  - Implement LV2Manifest class
  - We will be able to obtain an EffectManifest from a LilvPlugin\*

w10 July 21st - July 27th:

  - Implement LV2Backend class
  - We will be able to see the available LV2 plug ins and cycle through
    them inside an EffectRack (using a dummy LV2 Effect wrapper class
    which is playing silence)

W11 July 28th - August 3rd:

  - Implement LV2 wrapper class

W12 August 4th - August 10th:

  - Run Calf Flanger inside Mixxx using the newly added LV2Backend
  - We will be able to actually use an LV2 plug in such as Calf Flanger
    or the knockout effect

W13 August 11th - August 17th (Final evaluation):

  - test and debug 

Information sources for LV2 support:  
<http://wiki.audacityteam.org/wiki/LV2_Support>  
<http://libregraphicsworld.org/blog/entry/lv2-1-0-released-what-is-next>  
<http://libregraphicsworld.org/blog/entry/lv2-from-developers-standpoint>  
<http://gdam.ffem.org/ladspa-doc/ladspa-4.html>  
<http://www.nongnu.org/ll-plugins/lv2pftci/>  
<https://code.google.com/p/audacity/source/browse/audacity-src/trunk/src/effects/lv2/>  
<http://lac.linuxaudio.org/2014/download/lac2014_lv2_atoms_presentation.pdf>  
<http://dev.drobilla.net/browser/trunk/jalv/src/jalv.c>

Related wiki pages:  
[EQ Effect Rack](eq_rack)  
[LV2 Support](lv2_support)

**IV. About me**

My name is Nicu Bădescu (badescunicu on IRC) and I am a sophomore at
Politehnica University of Bucharest, progressing towards a B. Sc. in
Computer Science. I am an ardent supporter of open source and
volunteering. I have been a member of ROSEdu\[3\] (Romanian Open Source
Education) since May 2013.

I have experience in C, C++, Java and Python. I have a basic
understanding of Qt and I am confident that learning how to be efficient
in this framework would not be a problem. Last semester I developed a
simple virtual catalog using Swing, so I know the main ideas behind of a
GUI.

I am very passionate about contributing to open source projects because
I love the idea that my code is going to be used by a lot of people.

Last summer I worked as a Django developer for World of USO, which is an
open source browser-based game for our faculty’s freshmen. You can see
my commits here\[4\]. I have also made a small contribution to
Mozilla\[5\]. I learned how important communication is within a
community based project and also how to use vital tools for contributing
to a project, such as git. I am comfortable using the irc, mailing lists
or hangouts for communicating with my mentor.

Regarding Mixxx, I’ve been a contributor since October 2013 and I have
successfully closed the following issues / features with the help from
the community (which is, by the way, awesome :D ):

``` 
 * Ignore preview cloumn when exporting CSV file[6]
 * Replace underscores with spaces when parsing track file name[7]
 * Drag and Drop M3U/PLS into sidebar or main track table[8]
 * Add tooltips to sidebar items[9]
 * Remember last playlist directory[10]
 * Visualize distance to a key when pitch shifting[11]
```

Taking part in GSoC 2014 for Mixxx is a great opportunity and a dream
come true for me. Working feels like playing because Mixxx lies between
two of my passions: computer programming and electronic music.

Weekly reports:

``` 
 * [[extending_the_effects_engine_report_w1|Week #1]]
 * [[extending_the_effects_engine_report_w2|Week #2]]
 * [[extending_the_effects_engine_report_w3|Week #3]]
 * [[extending_the_effects_engine_report_w4|Week #4]]
 * [[extending_the_effects_engine_report_w5|Week #5]]
 * [[extending_the_effects_engine_report_w6|Week #6]]
 * [[extending_the_effects_engine_report_w7|Week #7]]
 * [[extending_the_effects_engine_report_w8|Week #8]]
 * [[extending_the_effects_engine_report_w9|Week #9]]
 * [[extending_the_effects_engine_report_w10|Week #10]]
 * [[extending_the_effects_engine_report_w11|Week #11]]
 * [[extending_the_effects_engine_report_w12|Week #12]]
 * [[extending_the_effects_engine_report_w13|Week #13]]
```

Links:  
\[1\] -
https:*github.com/mixxxdj/mixxx/blob/master/src/engine/enginedeck.cpp\#L103  
\[2\] - https:*bugs.launchpad.net/mixxx/+bug/1299031  
\[3\] - http:*www.rosedu.org/  
\[4\] - https:*github.com/rosedu/wouso/commits?author=badescunicu  
\[5\] - https:*bugzilla.mozilla.org/show\_bug.cgi?id=965347  
\[6\] - https:*bugs.launchpad.net/mixxx/+bug/1181172  
\[7\] - https:*bugs.launchpad.net/mixxx/+bug/1254534  
\[8\] - https:*bugs.launchpad.net/mixxx/+bug/743850  
\[9\] - https:*bugs.launchpad.net/mixxx/+bug/1017034  
\[10\] - https:*bugs.launchpad.net/mixxx/+bug/1178782  
\[11\] - https://github.com/mixxxdj/mixxx/pull/215
