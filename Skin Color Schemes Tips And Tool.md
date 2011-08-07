# Skin Color Schemes Tips and Tool

Mixxx uses an image processor to perform manipulation on images used in
skins. By taking advantage of this, you can create different color
schemes with some degree of specificity. But, it is not intuitive and
documentation is minimal. Getting a hang of the system takes a while. It
took many days, but I figured out a lot and even made a
[tool](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)
to help me make schemes faster.

## Mixxx 1.9 Scheme Engine and Transparent PNGs

[[/media/skinning/color_scheme/scs_tips_vumeterex.jpg|scs\_tips\_vumeterex.jpg]]
**The processor does not support transparency (in Mixxx 1.9).** Regular
skins can be created using transparent PNGs. This allows for some pretty
interesting layered effects, like this VU meter in one of my skins (at
right). Unfortunately, any partially transparent areas in PNGs that have
schemes applied to them become fully opaque with the applied color.
Fully transparent areas become opaque black. In the example below left,
imagine that the yellow circle with a dot is one of a series of PNG
images with transparency used for rotary knobs on a skin. It looks fine
until it goes through the scheme processor.

[[/media/skinning/color_scheme/scs_tips_pngex.jpg|scs\_tips\_pngex.jpg]] To
avoid ugly results like this, you must:

  - plan your skin layout carefully 
  - do not have controls overlap other controls 
  - place labels and background images where they will not be covered by
    control edges and corners 
  - avoid transparent backgrounds in your PNGs 

## Color Declarations Affected by Schemer

**Another thing to remember** when designing a skin for scheming is that
colors explicitly set in
[QT](Skin%20Color%20Schemes%20Tips%20and%20Tool#qt)<sup>\*</sup>
elements will not be affected by the color scheme processor. For
example, you can style tool tips and library widget elements using
CSS-like declarations such as

    <Style>
     QToolTip { font: 11px Lucida Grande, Lucida Sans Unicode, Arial, Verdana, sans-serif; 
     background-color: #191919; color: #CCCCCC; border: 1px solid #CCCCCC; padding: 4px; }  
    </Style>

The colors declared here will not change with the scheme (as of Mixxx
1.9). For them to change, **colors must be declared using \<BgColor\>,
\<FgColor\>, \<BgColorRowEven\>, or \<BgColorRowUneven\>**, for
applicable elements.

Once you have your non-transparent image files showing up correctly in
your skin with your color declarations in appropriate tags, then you can
start scheming\!

## Color Manipulation

**Color manipulation is tricky.** But it doesn't need to be. The biggest
problem is the math. I use [Gimp](http://www.gimp.org/) for all my image
design. Gimp sets color values using a scale of 0-100 for Saturation and
Value. Mixxx uses 0-255 to represent the same range. This scale
difference made it time consuming and took too much brain work to figure
out the numbers to use to change the colors to the ones I wanted\! *I'm
a teacher on summer vacation\! My brain doesn't do math during summer\!*
Even if I had used [Inkscape](http://inkscape.org/), I would have to
contend with the math since the Hue values in Inkscape are given 0-255
but in Mixxx they are 0-359.

**To build a color scheme**, you need to tell Mixxx how to change the
colors in your images. As of Mixxx 1.9, this is all you can do, but
there may be other image manipulation options in the future. For now,
you can invert colors (complete HSV value) or just hues, you can add
values to colors, or you can add values to each color component (Hue,
Saturation, and Value). I was able to design a skin that could have
schemes (following the recommendations listed above) and I knew which
colors I wanted to use, but I was having difficulty figuring out how to
get the colors I wanted (because of the math\!), so I made a tool to
help me.

### Scheme Builder Tool

**[My scheme builder
tool](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)**
allows me to input the original color used in my image and the color I
want to change it to. Then it spits out the XML code I need to use. You
input colors using hex numbers (like in web coding), which is handy
since the color codes in the skin.xml file uses those anyway and they
are easily accessible in both Gimp and Inkscape (Inkscape uses RGBA, so
you would just use the first 6 digits of the color). See below for some
examples.

## Simple Example

[[/media/skinning/color_scheme/scs_tips_crystaljellylarge.jpg|scs\_tips\_crystaljellylarge.jpg]]
**Simple color manipulation** and good planning allowed me to get five
interesting variants on my first schemed skin. I started by picking a
set of colors that worked well together using [Color Scheme
Designer](http://colorschemedesigner.com/#3G51Kw0w0w0w0), knowing that
any hue changes applied equally to all colors would result in color sets
that still worked well. I designed the layout and got it working in
Mixxx. Then I applied the schemes.

### Hue Manipulation

After much experimentation, I figured out what I needed to do. It was so
simple\! All I had to do was add a number to the Hue value that moved it
higher or lower on the hue spectrum. But what number to add? I grabbed a
screen capture while in Mixxx using ALT-PRTSCRN on my keyboard, pasted
it as a new image in Gimp. Then I used the Colors/Hue-Saturation tool to
change the hue until I got another version I liked. Then I used the
Color Picker tool to select from an area that I knew was "pure" (not
blended with another color); the middle of a waveform is pretty safe.
Going into the Change Foreground Color dialog showed me what the new
value should be. **For example**, I wanted to change it from a
cyan-based scheme to a red-orange theme. The cyan I used in the **main
theme was Hue=189**; I wanted to **change it to Hue=4**. The
**difference was -185**, so in the skin.xml file, I used:

``` 
    <Scheme>
        <Name>Blood Orange</Name>
        <Filters>
            <HSVTweak>
                <HConst>-185</HConst>
            </HSVTweak>
        </Filters>
    </Scheme>
```

#### Hue Caveat

The **\<HConst\>-185\</HConst\>** tells Mixxx to subtract 189 from the
Hue values all the colors used in my images. This worked for me since
all the colors used were at lease Hue=189. **Be careful** when doing
this kind of blanket manipulation. **There is [a bug in
version 1.9](https://bugs.launchpad.net/mixxx/+bug/816715)** that does
not allow Hue values higher than 255\! Any Hue changes that result in a
number higher than 255 or lower than 0 will "wrap around". If you add
102 to cyan (H=189), you should get a nice purple color (H=291), but
Mixxx will say, "Hey\! That number's too high\!" and subtract 255,
leaving you with orange (H=36). So when using \<HConst\> in your
schemes, **be sure not to have your colors wrap around**. My **[scheme
builder
tool](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)**
can help.

By using ***just \<HConst\>***, I was able to come up with a schemed
skin with 5 different color combinations. ([Download skin
ZIP](http://www.mrfloresreads.info/remixes/CrystalJelly1280x800-WXGA.zip))

[[/media/skinning/color_scheme/scs_tips_screenshot_schemes_large.jpg|scs\_tips\_screenshot\_schemes\_large.jpg]]

## Complex Examples

By using various filters in combination, you can accomplish more complex
color scheme modifications. The most useful elements for me are turning
out to be \<?Min\> and \<?Max\>, where ? is H, S, or V. These elements
limit application of image manipulations to certain colors based on
given Hues, Saturations, or Values or any combination thereof. Some
examples should make this more clear.

#### How to Narrow Colors Affected

[[/media/skinning/color_scheme/scs_tips_threedy_original.jpg|scs\_tips\_threedy\_original.jpg]]
In this skin, I want to **change the colors of the waveforms**. I also
want to change the FX, Repeat, and Headphones buttons to match the
waveforms but not anything else. Fortunately, **I made the waveforms and
buttons**, both dark and "lit" versions, **using the same Hue** (2,
almost pure red). I want to change change it to a nice blue. Using Gimp,
I changed a screen capture and color picked the new blue color to find
that it had a Hue of 210. So all I need to do is use \<HConst\>
function. However, if I use it without any other tags, it changes *ALL*
the colors and the result is yucky. To only change the red waveform and
buttons, I use the \<HMin\> and \<HMax\>. **I tell Mixxx to only apply
the \<HConst\> to Hues between 0 and 4** (in case some pixels changed
from a pure 2 Hue during image editing). I run a second filter in the
same scheme, this time limiting the change to Hues between 53 and 57 for
the second waveform. The code I end up with is: \<code\> \<Scheme\>

``` 
      <Name>The Blues</Name>
      <Filters>
          <HSVTweak>
              <HMin>0</HMin>
              <HMax>4</HMax>
              <HConst>206</HConst>
          </HSVTweak>
          <HSVTweak>
              <HMin>53</HMin>
              <HMax>57</HMax>
              <HConst>137</HConst>
          </HSVTweak>
      </Filters>
  </Scheme>
```

\</code\>
[[/media/skinning/color_scheme/scs_tips_threedy_blue.jpg|scs\_tips\_threedy\_blue.jpg]]
It results in a skin with blue waveforms\! Notice that the red Cue
button has not changed. This is because I limited the change to *only*
the reds used in the waveform and coordinated buttons. The Cue button
has a Hue of 356 so it was ignored. (Remember that the color spectrum
wraps around; 356 is only 4 steps away from pure red because 360 is the
same as 0.) You may notice that the knobs and fader look weird now.
That's because I hadn't finished converting the image files to
non-transparent when I was developing this tutorial. Mixxx is messing
them up as explained
[above](#Mixxx-1.9-Scheme-Engine-and-Transparent-PNGs).

Starting with the same original skin, **I wanted to change one waveform
to blue and the other to a complementary orange**. After applying the
same kind of transformation, I ended up with a kind of **orange that was
not deep enough**. I needed to **increase the Saturation** of the color.
In Gimp, I had increased the Saturation by 39 but in Mixxx, 39 was not
producing the same results\! That darn math again. So I made the
**[scheme builder
tool](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)**.
By putting in the original hex color, 9b9336, and the color I wanted to
end up with, 9b4100, I found out that I needed to increase the
Saturation by 89, according to Mixxx's scale. However, I only wanted to
increase it for the waveform color so I used \<SMin\> and \<SMax\> to
limit it to the Saturation of that particular color, which I knew (from
the HSV Equivalent field in my tool) was 166. The code:

    <Scheme>
        <Name>Web 2.0</Name>
        <Filters>
            <HSVTweak>
                <HMin>0</HMin>
                <HMax>4</HMax>
                <HConst>227</HConst>
            </HSVTweak>
            <HSVTweak>
                <HMin>53</HMin>
                <HMax>57</HMax>
                <HConst>-30</HConst> <!-- change the yellow to orange -->
            </HSVTweak>
            <HSVTweak>
                <SMin>165</SMin>
                <SMax>166</SMax>
                <SConst>100</SConst> <!--increase it to deeper orange -->
            </HSVTweak>
        </Filters>
    </Scheme>

[[/media/skinning/color_scheme/scs_tips_threedy_web2.jpg|scs\_tips\_threedy\_web2.jpg]]
By doing this, I got the results I wanted. You may have noticed that if
you put the color numbers mentioned into **[my scheme builder
tool](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)**,
it actually gives a value of 89 for SConst. I used 100 to make sure it
maxed out the saturation. Saturation and Values are clipped above 255,
so I knew it wouldn't hurt to use a higher number than needed.

[[/media/skinning/color_scheme/scs_tips_threedy_mono.jpg|scs\_tips\_threedy\_mono.jpg]]
Using a similar method, I desaturated (using negative numbers in SConst)
all the colors except the ones used for the Play and Cue buttons. This
gave me a black & white skin with color Play and Cue.

#### Modify Multiple Values

In the examples above, I only modified one value at a time using
HSVTweak, but you don't have to. **You can tweak multiple values at the
same time.** This is where **[my scheme builder
tool](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)**
really comes in handy. To turn the waveforms and buttons into two new
versions of red, I adjusted the colors in Gimp, picked the hex color
values, and copied them into the tool. Then I cut-and-pasted the code
into a new \<Scheme\> tag and added a couple \<?Min\> and \<?Max\> tags.

    <Scheme>
        <Name>Ready</Name>
        <Filters>
            <HSVTweak>
                <HMin>0</HMin>
                <HMax>4</HMax>
                <SMin>197</SMin>
                <SMax>199</SMax>
                <HConst>0</HConst>
                <SConst>36</SConst>
                <VConst>88</VConst>
            </HSVTweak>
            <HSVTweak>
                <HMin>53</HMin>
                <HMax>57</HMax>
                <HConst>-52</HConst>
                <SConst>53</SConst>
                <VConst>-24</VConst>
            </HSVTweak>
        </Filters>
    </Scheme>

## A Tricky Example

**Using careful planning, advanced scheme transformations are
possible.** In this quick and dirty test, **I "change" the shapes of the
elements**. I used dark versions of blue agains a black background to
hide them from casual observation. Then, in the scheme, I applied color
changes targeting very specifically those colors. The results are shown
at right. The top elements are the originals, the bottom elements are
with the scheme applied. Check out the code below to see how it was
done.
[[/media/skinning/color_scheme/scs_tips_mixxx_tricky_test.png|scs\_tips\_mixxx\_tricky\_test.png]]

    <Scheme>
        <Name>Tricky</Name>
        <Filters>
            <HSVTweak>
                <HMin>29</HMin> <!-- change only orange pinstripes -->
                <HMax>31</HMax>
                <SConst>-255</SConst> <!-- take out color -->
                <VConst>-255</VConst> <!-- take out brightness -->
            </HSVTweak>
            <HSVTweak>
                <HMin>240</HMin> <!-- select only darkest blue -->
                <HMax>240</HMax> <!-- in "hidden" pinstripe -->
                <SMin>102</SMin>
                <SMax>102</SMax>
                <VMin>20</VMin>
                <VMax>20</VMax>
                <HConst>-210</HConst> <!-- change to dark orange -->
                <SConst>153</SConst>
                <VConst>46</VConst>
            </HSVTweak>
            <HSVTweak>
                <HMin>240</HMin> <!-- select only med blue -->
                <HMax>240</HMax> <!-- in "hidden" pinstripe -->
                <SMin>97</SMin>
                <SMax>97</SMax>
                <VMin>21</VMin>
                <VMax>21</VMax>
                <HConst>-210</HConst> <!-- change to med orange -->
                <SConst>158</SConst>
                <VConst>162</VConst>
            </HSVTweak>
            <HSVTweak>
                <HMin>240</HMin> <!-- select only lightest blue -->
                <HMax>240</HMax> <!-- in "hidden" pinstripe -->
                <SMin>93</SMin>
                <SMax>93</SMax>
                <VMin>22</VMin>
                <VMax>22</VMax>
                <HConst>-210</HConst> <!-- change to light orange -->
                <SConst>162</SConst>
                <VConst>211</VConst>
            </HSVTweak>
            <HSVTweak>
                <HMin>111</HMin> <!-- change only the green circle -->
                <HMax>113</HMax>
                <SConst>-255</SConst> <!-- take out color -->
                <VConst>-255</VConst> <!-- take out brightness -->
            </HSVTweak>
            <HSVTweak>
                <HMin>240</HMin> <!-- select blue in hidden square-->
                <HMax>240</HMax>
                <SMin>85</SMin>
                <SMax>85</SMax>
                <VMin>3</VMin>
                <VMax>3</VMax>
                <HConst>-128</HConst> <!-- change to lime green -->
                <SConst>170</SConst>
                <VConst>210</VConst>
            </HSVTweak>
        </Filters>
    </Scheme>

I hope I have helped you understand a little better how schemes work in
Mixxx 1.9. I will play with my schemes a little more to get them just
right. I look forward to seeing how other people scheme *their* skins\!

## Orange Widget Icons

**One final note:** The orange icons in the directory tree are
hard-coded into Mixxx. As 'jus' informed me:

> you can only change them if you [build Mixxx from
> source](http://mixxx.org/wiki/doku.php/#build_mixxx).
> 
> Download the Mixxx source code ( see wiki link above) and replace the
> treeview icons in /mixxx/res/images/library/ with your custom ones
> while preserving the icons names and compile Mixxx.

Using this method, you can really tweak the way Mixxx looks on your
system. However, **this will not affect the way your skin looks on
someone else's system**.

SIGNATURE

-----

## QT

\* - QT is a UI framework used to build Mixxx. Most elements of the
interface can be styled using CSS within special XML tags such as
\<BgColor\>. Some elements ***must*** be styled by referencing the QT
element within \<Style\> tags. For example, to modify the borders of the
library widget, the colors of the header, or the style of the
scrollbars, you need to use the \<Style\> tags. Some CSS statements must
use QT-specific versions, such as "qlineargradient". The most useful
page I found was the [stylesheet reference
list](http://doc.qt.nokia.com/latest/stylesheet-reference.html).
