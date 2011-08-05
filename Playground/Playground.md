# PlayGround

rename fullsized images scs\_tips\_? link in wiki to fullsized but
resize in wiki make reference that images are resized

# Skin Color Schemes Tips and Tool

Mixxx uses an image processor to perform manipulation on images used in
skins. By taking advantage of this, you can create different color
schemes with some degree of specificity. But, it is not intuitive and
documentation is minimal. Getting a hang of the system takes a while. It
took many days, but I figured out a lot and even made a
[tool](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)
to help me make schemes faster.

## Mixxx 1.9 Scheme Engine and Transparent PNGs

![http://www.mrfloresreads.info/remixes/images/vumeterex.jpg](http://www.mrfloresreads.info/remixes/images/vumeterex.jpg)
**The processor does not support transparency (in Mixxx 1.9).** Regular
skins can be created using transparent PNGs. This allows for some pretty
interesting layered effects, like this VU meter in one of my skins (at
right). Unfortunately, any partially transparent areas in PNGs that have
schemes applied to them become fully opaque with the applied color.
![http://www.mrfloresreads.info/remixes/images/pngex.jpg](http://www.mrfloresreads.info/remixes/images/pngex.jpg)
Fully transparent areas become opaque black. In the example at left,
imagine that the yellow circle with a dot is one of a series of PNG
images with transparency used for rotary knobs on a skin. It looks fine
until it goes through the scheme processor.

To avoid ugly results like this, you must:

  - plan your skin layout carefully 
  - do not have controls overlap other controls 
  - place labels and background images where they will not be covered by
    control edges and corners 
  - avoid transparent backgrounds in your PNGs 

### Color Declarations Affected by Schemer

**Another thing to remember** when designing a skin for scheming is that
colors explicitly set in
[QT](Skin%20Color%20Schemes%20Tips%20and%20Tool#qt)<sup>\*</sup>
elements will not be affected by the color scheme processor. For
example, you can style tool tips and library widget elements using
CSS-like declarations such as

    &lt;Style>
     QToolTip { font: 11px Lucida Grande, Lucida Sans Unicode, Arial, Verdana, sans-serif; 
     background-color: #191919; color: #CCCCCC; border: 1px solid #CCCCCC; padding: 4px; }  
    &lt;/Style>

. The colors declared here will not change with the scheme (as of Mixxx
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

[**My scheme builder
tool**](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)
allows me to input the original color used in my image and the color I
want to change it to. Then it spits out the XML code I need to use. You
input colors using hex numbers (like in web coding), which is handy
since the color codes in the skin.xml file uses those anyway and they
are easily accessible in both Gimp and Inkscape (Inkscape uses RGBA, so
you would just use the first 6 digits of the color). See below for some
examples.

## Simple Example

![http://www.mrfloresreads.info/remixes/images/crystaljellylarge.jpg](http://www.mrfloresreads.info/remixes/images/crystaljellylarge.jpg)"
title="Starting point before scheming" **Simple color manipulation** and
good planning allowed me to get five interesting variants on my first
schemed skin. I started by picking a set of colors that worked well
together using [Color Scheme
Designer](http://colorschemedesigner.com/#3G51Kw0w0w0w0), knowing that
any hue changes applied equally to all colors would result in color sets
that still worked well. I designed the layout and got it working in
Mixxx. Then I applied the schemes.

#### Hue Manipulation

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
this kind of blanket manipulation. **There is a bug in version 1.9**
that does not allow Hue values higher than 255\! Any Hue changes that
result in a number higher than 255 or lower than 0 will "wrap around".
If you add 102 to cyan (H=189), you should get a nice purple color
(H=291), but Mixxx will say, "Hey\! That number's too high\!" and
subtract 255, leaving you with orange (H=36). So when using \<HConst\>
in your schemes, **be sure not to have your colors wrap around**. My
tool above can help.

By using ***just \<HConst\>***, I was able to come up with a schemed
skin with 5 different color combinations. ([Download skin
ZIP](http://www.mrfloresreads.info/remixes/CrystalJelly1280x800-WXGA.zip))

\<div
align="center"\>[above](http://www.mrfloresreads.info/remixes/images/screenshot_schemes_large.jpg"%20rel="lightbox"%20title="Five%20schemes%20using%20just%20HConst"\>{{http://www.mrfloresreads.info/remixes/images/screenshot_schemes_small.jpg"%20border="0"%20alt=""%20align=""\>%20% A% A=====%20Complex%20Examples%20=====% ABy%20using%20various%20filters%20in%20combination,%20you%20can%20accomplish%20more%20complex%20color%20scheme%20modifications.%20The%20most%20useful%20elements%20for%20me%20are%20turning%20out%20to%20be%20\<?Min\>%20and%20\<?Max\>,%20where%20?%20is%20H,%20S,%20or%20V.%20These%20elements%20limit%20application%20of%20image%20manipulations%20to%20certain%20colors%20based%20on%20given%20Hues,%20Saturations,%20or%20Values%20or%20any%20combination%20thereof.%20Some%20examples%20should%20make%20this%20more%20clear.% A% A===%20How%20to%20Narrow%20Colors%20Affected%20===% AIn%20{{%20http://www.mrfloresreads.info/remixes/images/threedy_original.jpg}}%20this%20skin,%20I%20want%20to%20**change%20the%20colors%20of%20the%20waveforms**.%20I%20also%20want%20to%20change%20the%20FX,%20Repeat,%20and%20Headphones%20buttons%20to%20match%20the%20waveforms%20but%20not%20anything%20else.%20Fortunately,%20**I%20made%20the%20waveforms%20and%20buttons**,%20both%20dark%20and%20"lit"%20versions,%20**using%20the%20same%20Hue**%20\(2,%20almost%20pure%20red\).%20I%20want%20to%20change%20change%20it%20to%20a%20nice%20blue.%20Using%20Gimp,%20I%20changed%20a%20screen%20capture%20and%20color%20picked%20the%20new%20blue%20color%20to%20find%20that%20it%20had%20a%20Hue%20of%20210.%20So%20all%20I%20need%20to%20do%20is%20use%20\<HConst\>%20function.%20However,%20if%20I%20use%20it%20without%20any%20other%20tags,%20it%20changes%20//ALL//%20the%20colors%20and%20the%20result%20is%20yucky.%20To%20only%20change%20the%20red%20waveform%20and%20buttons,%20I%20use%20the%20\<HMin\>%20and%20\<HMax\>.%20**I%20tell%20Mixxx%20to%20only%20apply%20the%20\<HConst\>%20to%20Hues%20between%200%20and%204**%20\(in%20case%20some%20pixels%20changed%20from%20a%20pure%202%20Hue%20during%20image%20editing\).%20I%20run%20a%20second%20filter%20in%20the%20same%20scheme,%20this%20time%20limiting%20the%20change%20to%20Hues%20between%2053%20and%2057%20for%20the%20second%20waveform.%20The%20code%20I%20end%20up%20with%20is:% A\<code\>%20% A%20%20%20%20\<Scheme\>% A%20%20%20%20%20%20%20%20\<Name\>The%20Blues\</Name\>% A%20%20%20%20%20%20%20%20\<Filters\>% A%20%20%20%20%20%20%20%20%20%20%20%20\<HSVTweak\>% A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\<HMin\>0\</HMin\>% A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\<HMax\>4\</HMax\>% A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\<HConst\>206\</HConst\>% A%20%20%20%20%20%20%20%20%20%20%20%20\</HSVTweak\>% A%20%20%20%20%20%20%20%20%20%20%20%20\<HSVTweak\>% A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\<HMin\>53\</HMin\>% A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\<HMax\>57\</HMax\>% A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20\<HConst\>137\</HConst\>% A%20%20%20%20%20%20%20%20%20%20%20%20\</HSVTweak\>% A%20%20%20%20%20%20%20%20%20%20%20%20\</Filters\>% A%20%20%20%20\</Scheme\>% A\</code\>%20% AIt%20results%20in%20a%20{{http://www.mrfloresreads.info/remixes/images/threedy_blue.jpg%20}}%20skin%20with%20blue%20waveforms!%20Notice%20that%20the%20red%20Cue%20button%20has%20not%20changed.%20This%20is%20because%20I%20limited%20the%20change%20to%20//only//%20the%20reds%20used%20in%20the%20waveform%20and%20coordinated%20buttons.%20The%20Cue%20button%20has%20a%20Hue%20of%20356%20so%20it%20was%20ignored.%20\(Remember%20that%20the%20color%20spectrum%20wraps%20around;%20356%20is%20only%204%20steps%20away%20from%20pure%20red%20because%20360%20is%20the%20same%20as%200.\)%20You%20may%20notice%20that%20the%20knobs%20and%20fader%20look%20weird%20now.%20That's%20because%20I%20haven't%20finished%20converting%20the%20image%20files%20to%20non-transparent.%20Mixxx%20is%20messing%20them%20up%20as%20explained%20[[#Mixxx-1.9-Scheme-Engine-and-Transparent-PNGs).

Starting with the same original skin, **I wanted to change one waveform
to blue and the other to a complementary orange**. After applying the
same kind of transformation, I ended up with a kind of **orange that was
not deep enough**. I needed to **increase the Saturation** of the color.
In Gimp, I had increased the Saturation by 39 but in Mixxx, 39 was not
producing the same results\! That darn math again. So I made the
[**scheme builder
tool**](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool).
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

By doing this, I got
![http://www.mrfloresreads.info/remixes/images/threedy\_web2.jpg"
rel="lightbox"](http://www.mrfloresreads.info/remixes/images/threedy_web2.jpg"%20rel="lightbox")
the results I wanted. You may have noticed that if you put the color
numbers mentioned into [**my scheme builder
tool**](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool),
it actually gives a value of 89 for SConst. I used 100 to make sure it
maxed out the saturation. Saturation and Values are clipped above 255,
so I knew it wouldn't hurt to use a higher number than needed.

Using a similar method, I desaturated (using negative numbers in SConst)
all the colors except the ones used for the Play and Cue buttons. This
gave me a
![http://www.mrfloresreads.info/remixes/images/threedy\_mono.jpg](http://www.mrfloresreads.info/remixes/images/threedy_mono.jpg)
black & white skin with color Play and Cue.

#### Modify Multiple Values

In the examples above, I only modified one value at a time using
HSVTweak, but you don't have to. **You can tweak multiple values at the
same time.** This is where [**my scheme builder
tool**](http://www.mrfloresreads.info/remixes/mixxxschemeutil.html#tool)
comes in handy. To turn the waveforms and buttons into two new versions
of red, I adjusted the colors in Gimp, picked the hex color values, and
copied them into the tool. Then I cut-and-pasted the code into a new
\<Scheme\> tag and added a couple \<?Min\> and \<?Max\> tags.

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
below. The top elements are the originals, the bottom elements are with
the scheme applied. Check out the code below to see how it was done.

\<div
align="center"\>{{<http://www.mrfloresreads.info/remixes/images/mixxx_tricky_test.png>"
width="228" height="120" border="0" alt=""\>\</div\>

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
hard-coded into Mixxx. As 'jus' informed me,

    you can only change them if you [[http://mixxx.org/wiki/doku.php/#build_mixxx|build Mixxx from source]].
    Download the Mixxx source code ( see wiki link above) and replace the treeview icons in /mixxx/res/images/library/ with your custom ones while preserving the icons names and compile Mixxx.

Using this method, you can really tweak the way Mixxx looks on your
system. However, **this will not affect the way your skin looks on
someone else's system**.

-----

## QT

\* - QT is a UI framework used to build Mixxx. Most elements of the
interface can be styled using CSS within special XML tags such as
\<BgColor\>. Some elements ***must*** be styled by referencing the QT
element within \<Style\> tags. For example, to modify the borders of the
library widget, the colors of the header, or the style of the
scrollbars, you need to use the \<Style\> tags. Some CSS statements must
use QT-specific versions, such as "qlineargradient". The most useful
page I found was the
<http://doc.qt.nokia.com/latest/stylesheet-reference.html">stylesheet reference list>.\</p\>
