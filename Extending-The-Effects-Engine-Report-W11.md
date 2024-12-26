Hello again,  
Last week I told you that I added the handling of Lilv library inside
`features.py`. There I set the minimum version of lilv to be 0.14.
Daniel pointed me out that Ubuntu 12.04 repositories still feature the
old lilv 0.5 version. I looked for that version of lilv and looked
inside `lilv.h`. All the functions I used for adding LV2 support to
Mixxx are there, so I changed the minimum required version of lilv to
0.5 inside `features.py`.

As a side task I implemented a 10 band Master Graphic Equalizer. The
work can be broken down on two parts:

  - Create a new effect which features 10 bandpass static filters. Their
    frequency is set up when they are created. Biquad Bandpass filters
    generated with `fidlib` are used for this effect. This new type of
    filters is based on Daniel's IIR filters refactoring\[1\].

<!-- end list -->

  - Create sliders in preferences which control the newly created
    effect's parameters.
  - These sliders' `sliderMoved` signal is connected to a slot which is
    updating the effect parameters directly, by writing requests to the
    Effect Engine.
  - The naive way of doing this is having a different slot for each
    slider:

<!-- end list -->

``` 
    * slider1' ''sliderMoved'' signal connected to ''slotSlider1''
    * slider2' ''sliderMoved'' signal connected to ''slotSlider2''
    * ...
    * slider10' ''sliderMoved'' signal connected to ''slotSlider10''
* However, a lot of code is duplicated, because there are only 2 values which differ from one slot to another. I had to find a way to have access to a couple of values inside the slot responsible for updating the state of a parameter:
    * the index of the slider which was modified --> for knowing which effect parameter to update
    * the new slider position --> for obtaining the value which needs to be set for the effect parameter (this is passed by the ''sliderMoved(int)'' signal)
* I tried to use //QSignalMapper// and map each signal with an integer representing the slider's index. Unfortunately, //QSignalMapper// works only on parameterless signals.
* The best solution was making use of QObject's dynamic properties. I used ''setProperty'' method to store the slider's index. All I had to do inside the slot now was to use the ''sender()'' method to obtain the slider which emitted the signal and get retrieve index which was previously stored as a dynamic property.
```

Here is a screenshot with the current state of the Master
EQ:[[/media/master_eq.png|]]

I have some good news about the kn0ck0out LV2 plugin. As you know from
my ninth report, it was not working as it should have, it was only
playing silence. So I contacted its maintainer, Jeremy Salwen. He was
kind enough to take a look on the code and found out that the output of
an integer division was used instead of a floating point one. Here\[2\]
you can check out the commit. I'm flattered he mentioned my name in the
commit message.

I continued my work on LV2 support by adding enumeration and button
parameters. They are based on a multi state button (two in case of a
*toggle* parameter, more than two in case of an *enumeration*
parameter). The main thing this type of parameters needed was for their
underlying value to go back to the minimum if the maximum was exceeded.
This\[3\] commit implements that behaviour. Working on this I got a
"strange" C++ error which cause was using a getter method on a const
object. All I had to do was make the getter const, because only const
methods can be called on const objects. This makes sense because
otherwise a non const method might attempt to modify the const object.

After testing some LV2 plugins and their enumeration parameters, I was
not pleased to realize Mixxx crashes chaotically when changing effects.
What made this bug hard was that I got different errors each time I ran
Mixxx and using debug mode did not help me very much. I found out that
the bug disappears if I remove the code responsible for updating lv2
parameters: `params[i] = m_parameters[i]->value().toFloat()`. `params`
is a dynamically allocated float array which is connected to lv2 plugin
instance's ports. The problem was that I allocated memory only for
*manifest.parameters.size()* and forgot to take into account
*manifest.buttonParametrs.size()*. C++ does not perform boundary
checking. Thus, sometimes the code even worked, maybe because the memory
area right next to *params* was not accessed by someone else. This bug
taught me to be more careful when allocating resources in C++.

Cheers,  
Nicu Badescu

\[1\] - <https://github.com/mixxxdj/mixxx/pull/294>  
\[2\] -
<https://github.com/jeremysalwen/kn0ck0ut-LV2/commit/7ff733d90e6c51649203ab799977a8be616f08fb>  
\[3\] -
<https://github.com/badescunicu/mixxx/commit/0a327759d4bc91f25f60059e29f222436dc9b719>  

[Back to the main page\!](extending_the_effects_engine)
