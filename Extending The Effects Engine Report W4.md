Hello,

It was a busy week at university because I had my last exam on Friday
and after that I had to pack my things and move back home. Thankfully,
school is over and I can focus entirely on Mixxx from now on.  
  
I talked with Daniel about the software design for switch type
parameters. I proposed this\[1\] design and I thought that instead of
creating a ControlEffectKnob in EffectParameterSlot we can create either
a ControlPushButton or a ControlPotmeter, based on manifest's
ControlHint. Unfortunately this is not possible, as my mentor pointed me
out, because of two reasons:

``` 
 * The skin is setting all connections when it is loaded. It cannot connect to a ControlObject which will be created afterwards
 * The effect change is processed during the audio callback and we shouldn't use new() and delete() inside this function because they have an unpredictable execution time
```

So we settled for the design which uses two separate lists of
EffectParameters: one for knobs and one for buttons (switch parameters).
After fixing a couple of typos in my implementation it is now working
and it is updating the EffectParameters accordingly.  
  
I had to introduce a new field in EffectsRequest::MessageType enum
(SET\_PARAMETER\_BUTTON\_PARAMETERS) to be able to extract the
EffectParameter from the corresponding QList (knobs or buttons) inside
EngineEffect::processEffectsRequest(). However, it still has a problem.
Even though it is correctly updating the values which are processed by
the framework, it doesn't display the same values in the GUI.

I have also fixed the master conflicts for the EQ Default branch\[2\].
It is now using memcpy and memset for copying and initializing buffers
and coefficients. I have also commented out the RBGW Mix, because Daniel
found some issues with the involved filters.

\[1\] ![controlparameter.jpg](controlparameter.jpg) \[2\] -
<https://github.com/mixxxdj/mixxx/pull/267/files>
