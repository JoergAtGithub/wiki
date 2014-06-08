Hello again,

I am glad to inform you that I got my first pull
request[\[1](https://github.com/mixxxdj/mixxx/pull/270)\] merged this
week. It was a glitch inside *EngineFitlerButterworth8Band's* process
method. When it was called with specific frequency corners, a constant
unbearable crackling could be heard.

While I was testing if the ramping after *setFrequencyCorners* is
working properly I stumbled upon that issue. I have immediately filed a
bug[\[2](https://bugs.launchpad.net/mixxx/+bug/1326001)\] on Launchapd.
Here is how you could reproduce it:

  - go to preferences -\> equalizers;
  - disable "Use static Equalizers";
  - set Low Shelf EQ to minimum and High Shelf EQ to maximum;
  - play a track and turn up the knob responsible for EQ's "Mid" gain.

I started looking for the source of the problem. As Daniel suggested, it
could have been some sort of overflow inside the *process* method.
Throughout the code, we were using *CSAMPLE* (which is a typedef for
*float*) to represent coefficients and buffers. The problem was that
fidlib's *fid\_design\_coef* function returns an array whose type is
*double*. So we were initializing a CSAMPLE array with double values.
Consequently, precious information was lost during this cast.

The solution was to use *double* instead of *CSAMPLE* for representing
the information we need for the filter. Anyway, a performance issue
arose and we should pay attention to such kind of problems because
responsiveness is very important to real time processing software. So I
placed a timer inside *\_process\*pass* functions to test the before and
after patch performance. Here are the results:

*My notebook (with RT Scheduling disabled):* *Without the patch:*
Stat("\_processBandpass()","count=2.10739e+06,sum=1.89391e+09ns,average=898.699ns,min=461ns,max=422348ns,variance=1.01698e+06ns^2,stddev=1008.45ns")

*With the patch:*
Stat("\_processBandpass()",count=2.61939e+06,sum=2.50817e+09ns,average=957.538ns,min=477ns,max=663356ns,variance=1.04328e+06ns^2,stddev=1021.41ns")

*Asus eeePC with RT Scheduling enabled:* *Without the patch:*
Stat("\_processBandpass()","count=3.43757e+06,sum=8.52755e+09ns,average=2480.69ns,min=1467ns,max=138215ns,variance=1.43556e+06ns^2,stddev=1198.15ns")

*With the patch:*
Stat("\_processBandpass()","count=1.85549e+06,sum=4.71517e+09ns,average=2541.2ns,min=1536ns,max=131022ns,variance=1.88703e+06ns^2,stddev=1373.69ns")

As you can see, the difference is not significant and it is a small
price to pay for solving an annoying issue.

Another pull request[\[3](https://github.com/mixxxdj/mixxx/pull/268)\] I
have opened this week is about porting the static Equalizer as a
separate effect. This EQ is useful for computers with poor hardware
since it is not so CPU demanding. Therefore, LightweightEQ seemed a good
name for such an Equalizer. While I was working at this effect, Daniel
pointed out that I can use *fidlib* for computing the coefficients
needed for this EQ. This is something I hope to do in the following
week.

A topic which is harder than I thought and which has been taking me
quite some time is implementing switch type parameters for the effects
framework. As a reminder, I need them for EQ's kill buttons. I noticed
every effect has an *EffectParameter* list which stores information
about each parameter. *EffectParameterSlot* is responsible for
instantiating a *ControlEffectKnob* for an *EffectParameter*. The
problem with *ControlEffectKnob* is that it behaves only as a
*ControlPotmeter* and we need it to behave like a *ControlPushButton*
too. I tried to create a different list of "button parameters" for each
effect and create a new class (*EffectButtonParameterSlot*) which
instead of *ControlEffectKnob* features a *ControlPushButton*. The
problem with this approach is that a lot of code is duplicated and
currently I haven't managed to make it work properly, because the
buttons are not updating as they should. I suspect it is a problem with
the "request-response" update mechanism. I hope that by the end of the
next week, with the community's help, I'll come to a resolution
regarding this topic.

Here is the basic flow when creating an effect parameter slot:

EffectsManager::setupDefaults ---\>  
EffectRack::addEffectChainSlot ---\>  
EffectChainSlot::addEffectSlot ---\>  
EffectSlot::EffectSlot (constructor) ---\>  
EffectSlot::addEffectParameterSlot ---\>  
EffectParameterSlot::EffectParameterSlot (constructor) ---\>  
ControlEffectKnob::ControlEffectKnob (constructor)

Yours truly,  
Nicu Badescu

\[1\] - https:*github.com/mixxxdj/mixxx/pull/270  
\[2\] - https:*bugs.launchpad.net/mixxx/+bug/1326001  
\[3\] - https://github.com/mixxxdj/mixxx/pull/268  

[Back to the main page\!](extending_the_effects_engine)
