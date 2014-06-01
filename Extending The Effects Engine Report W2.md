## \#2 Weekly Report

  
Howdy,

My main target this week was fixing
[this](https://bugs.launchpad.net/mixxx/+bug/1209294) bug. What is the
deal with this bug? Well, every time one of the frequency corners was
changed from the preference page, a new **EngineFilterButterworth**
object was created. Thus, some clicks could be heard because the
previous filter state was lost and it was a slight difference in the
output samples between from the old filter and the newly created filter.
The solution to this issue is cross fading between the old output
samples and the new ones.

Here is how I tackled this problem:  
\* store a flag inside **EngineFilterButterworth** class which is set to
true if ramping is needed;

  - store the old coefficients and buffers for the two Channels;

<!-- end list -->

``` 
   * put all the values from the current coefficients array into the old array, just before the former is updated with new coefficients;
   * old buffers are initialized with current buffers, just before current buffers are zeroed (inside initBuffers method);
* when a frequency is changed, set the flag responsible for ramping to true;
* inside the process method, if the ramping flag is true, compute the old output, the new one and cross fade between them; also, set the flag to false.
```

However, it is easier said than done. I was pretty confident that my
first implementation will work, but it didn't. I was creating
dynamically a new array of MAX\_BUFFER\_LEN size which was used for
computing the old output samples. I must thank Owen for helping me out
with this. The new output samples were stored in pOutput. After cross
fading between those two, I was freeing the memory allocated for the
array. The problem with this approach is that **MAX\_BUFFER\_LEN** is
160,000. Imagine the inefficiency of allocating and freeing 160,000
numbers, multiple times per second.

The next idea came to me while analyzing
**SampleUtil::linearCrossfadeBuffers**'s code. Instead of computing and
storing the whole old buffer before cross fading, I was going to compute
it on the fly. Consequently, I needed only two numbers, one for each
channel. The formula for cross fading is : *result = final \* coef +
initial \* (1 - coef)*. This is a simple formula which has a lot of
applications, including those from the gaming industry (they use it for
linear interpolation). *coef* is a real number between 0 and 1 which is
incremented each step. As he approaches the value 1, final is fading in
and initial is fading out.

This time I was sure my code will work flawlessly. Guess what? It
didn't. I was doing a rookie mistake and Daniel helped me out. A new
**EngineFilterButterworth** was being created each time the frequency
corners changed. So my logic with buffers to store the old coefficients
was useless. I fixed this by updating each filter instead of creating a
new one.

Unfortunately, there is a case when even after ramping, a lot of
crackles can be heard. To reproduce this, turn up the mid gain. Inside
equalizer preferences, turn the low frequency all the way down and the
high frequency corner all the way up. Any suggestions are welcomed\! My
branch can be found
[here](https://github.com/badescunicu/mixxx/compare/eq_effect_space).

Cheers\!  
Nicu Badescu
