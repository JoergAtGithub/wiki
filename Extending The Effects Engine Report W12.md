Hello,

As you know from the last report, button and enumeration parameters were
using a multi state button for cycling through its states. The downside
of this was that the user had no visual feedback of which option is he
going to choose. Also, he couldn't skip skip through the states, they
were incremented by one each time the button was pressed.

I managed to solve this issue by creating another widget, called
`WEffectPushButton` which is borrowing code for acting like a push
button from `WPushButton` widget and code for obtaining information
about the loaded effect from the `WEffectParameter`. A new tag for
buttons used inside the effects framework was introduced,
`EffectPushButton`. It shall be used by skin developers when they create
a new skin. Inside `legacyskinparser.cpp` a new method for parsing the
newly added tag was introduced: `parseEffectPushButton`.

It is responsible for setting up the required connection, as well as
creating a new WEffectPushButton object. This new widget acts the same
when the user left clicks it: cycles through the states. But it has a
different behaviour on right click: opens a small menu with all options
available for that parameter. QMenu was used for this, along with a
QActionGroup which acts like a container for QAction entries, allowing
us to make the QAction exclusive (only one can be checked at a given
time). Here is an image of the output, using a modified Deere skin:

![http://oi59.tinypic.com/6gh6yu.jpg](http://oi59.tinypic.com/6gh6yu.jpg)

Another issue with LV2 effects was that some of them had a lot of
parameters (up to 60) and they can't possibly fit inside a skin. So the
solution I came up with was letting the user select which parameters are
displayed inside the skin. This is done via an LV2 preferences menu
which displays all the discovered LV2 plugins as buttons. Those which
are not available are shown as disabled push buttons. Upon clicking an
effect, its parameters are displayed as check boxes and the user can set
the active parameters.

This was achieved by introducing a list inside EffectManifest which acts
like a function which job is to map a parameter slot to the index of the
effect's active parameter for that slot. For example, if we want
effect's parameters 4, 7 and 10 to be active, the mapping function would
be: `f[0] = 4, f[1] = 7 and f[2] = 10`. This function was built on
demand, whenever a new `EffectManifestParameter` was added to an
`EffectManifest`.

While working on this, I got an "index out of bounds" and it took me
quite a while to figure out what was the problem. Inside
`EffectParamterSlot::loadEffect` method it was possible to ask for a
parameter which did not exist. It was the caller's responsibility to
ensure the parameter was returned and not NULL. Well, in this case, the
mapping function did not have any value for the requested parameter slot
number, because it was greater than the number of real parameters. So I
replaced `Effect::getParameter` and `Effect::getButtonParameter` methods
with `Effect::getParameterForSlot` and
`Effect::getButtonParamterForSlot`. These new methods perform an upper
bound check and retrieve the proper EffectParameter by using the mapping
function provided by the EffectManifest. Here is how the LV2 preferences
menu currently looks:

![http://oi60.tinypic.com/xni5c0.jpg](http://oi60.tinypic.com/xni5c0.jpg)

I also worked on the Graphic EQ effect. Daniel added a `pauseFilter()`
method which I had to use when a filter was paused or restarted. This
resets the buffers and sets m\_doRamping and m\_doStart flags to true.
In order to avoid resetting the buffers each time the `process` method
is called and the filter is paused, I had to introduce a new flag,
`m_isPaused`. Here\[1\] you can check the commit which introduces that
flag. Another addition to Graphic EQ effect is the dynamic updated of
the filters if the sample rate is changed. It cycles through the band
filters and calls `setFrequencyCorners` on each one with the new value
of sample rate.

Today is the suggested pencils down date. I am happy with my progress
and I will spend the last week of GSoC removing debug comments across
the code I wrote and trying to create a better GUI for the LV2
preferences.

Cheers,  
Nicu Badescu

\[1\] -
<https://github.com/badescunicu/mixxx/commit/8ce1b54885d637ad9a35ce82d9eded9ccb885ffd>  
  
[Back to the main page\!](extending_the_effects_engine)
