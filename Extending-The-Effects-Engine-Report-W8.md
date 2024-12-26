Hello,

As you know, I am currently working on adding LV2 support to Mixxx. I
and my mentor, Daniel, thought of implementing such support by using an
external Jack host for LV2 plug ins. This had the advantage that an
external process dealt with samples processing. We could use well tested
software solutions such as Jalv, or calfjackhost (bundled with calf plug
ins). Here\[1\] is the sketch for this approach. To be able to implement
it we must make use of the Jack API directly, as shown in this\[2\]
picture. This approach is useful for the advanced user, who wants full
control of Mixxx's streams. Not only does it provide LV2 support but
also can be used for VST plug ins or Hardware effects.

However, after requesting feedback from the community, Ryan responded
and advised us to implement native LV2 support for Mixxx. The advantage
of native LV2 integration is that every user can benefit from it, it
works seamlessly with Mixxx, no tweaks are required to make it
functional. The normal user won't see a diference between native effects
and LV2 ones. The steps towards basic LV2 integration are the following
(I must thank Ryan for his detailed description):

``` 
 * Create an LV2Backend class which inherits from EffectsBackend
   * This backend class is responsible for enumerating (finding) and instantiating effects
 * Create a new class which receives an LV2 plugin manifest, parses it and obtains a Mixxx EffectManifest
   * This is an important step because Mixxx relies on EffectManifests when creating slots for effects and its parameters
 * Add an LV2 effect wrapper class
   * It has to send parameter updates to the plug in instantiation as well as processing audio samples using the plug in.
```

Below is a diagram of the LV2 architecture I'm trying to implement:  
[[/media/lv2_architecture.jpg|]]

For the first step (parsing the LV2 plugin manifest into an
EffectManifest) I'll be using lilv\[3\]. It is the recommended way for
hosts to add LV2 support. Audacity is already using it. I started to get
accustomed to lilv by writing a simple, separate program which
enumerates the available LV2 plug ins and identifies each plugins'
parameters. You can find it here\[4\]. Based on those LV2 Ports I will
create corresponding EffectParameters (currently I can create only
potmeters, since the code for buttons as effect parameters is not merged
yet; hopefully it will be soon). Here are some useful lilv functions:

  - Create the *world* which is responsible for plug in discovery
  - LilvWorld\* lilv\_world\_new();
  - Load all available plug ins
  - void lilv\_world\_load\_all(LilvWorld\*);
  - Get the loaded plug ins
  - const LilvPlugins\* lilv\_world\_get\_all\_plugins(LilvWorld\*);
  - Iterate through them
  - LILV\_FOREACH(plugins, iter, container);
  - *plugins* is a keyword, lilv's FOREACH macro takes into account this
    keyword and knows to call lilv\_*plugins*\_\* functions
  - Get the name of a plugin
  - LilvNode\* lilv\_plugin\_get\_name(const LilvPlugin\*);
  - const char\* lilv\_node\_as\_string(LilvNode\*);

Another task I worked on this week was removing the *static* keyword
from the Bessel Filters. This means that Equalizers who use Bessel
filters are now receiving frequency corners changes as well. Here\[5\]
is the branch I've worked on. As you remember, I fixed the crackles
heard during the change of frequencies for Butterworth filters. However,
those crackles were removed only in ButterworthEQEffect, because inside
EngineFilterBlock a new set of filters is created each time one of the
frequencies is changed. I refactored the EngineFilterBlock class by
moving the filter creation inside the constructor. Now, when frequency
corners are changed, we only update the filters as opposed to creating
new ones.

At Owen's suggestion, I wrote a unit test for the alias control feature.
I built Mixxx with *test=1* flag and read about Google' C++ Testing
Framework.

Yours truly,  
Nicu Badescu

\[1\] - <http://i.imgur.com/Kd7REQh.jpg>  
\[2\] - <http://i.imgur.com/m69xLKU.jpg>  
\[3\] - <http://drobilla.net/software/lilv/>  
\[4\] - <https://gist.github.com/badescunicu/44bff3b9e24fd905806c>  
[Back to the main page\!](extending_the_effects_engine)
