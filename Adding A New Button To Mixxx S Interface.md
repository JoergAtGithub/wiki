# Tutorial: Mixxx button hack

**Disclaimer:** This is not a skinning tutorial. This tutorial is just
for fun.

## Audience

If you are absolutely new to Mixxx code base and you are impatient to
hack this awesome piece of work, then you are the intended audience.

## Introduction

Mixxx has come a long way since it's early days, the code base has grown
too much in both size and complexity. This is a naive Mixxx hack which
aims at providing glimpse into Mixxx's code base.

## Aim

We'll try to add a new button to Mixxx's interface which will play the
track loaded in Channel 1.

## What you need to have/know

Nothing, just few basic things like:

1\. Compiling Mixxx from source.

2\. The root password for your Linux box.

3\. And, some coffee if you prefer.

## Let's Go\!

We'll be editing Outline800x480-WVGA interface. Steps to edit other
interfaces are same.

I am assuming that source code is in **\~/mixxx**

Alright, let's begin\!

> Where are skins?

\>

> In source code skins are at **\~/mixxx/mixxx/src/res/skins**
> 
> Installed skin files are generally at **/usr/local/share/mixxx/skins**
> or **/usr/share/mixxx/skins**
> 
> By now you must have noticed that folders have names of skins, open
> any folder and find **skin.xml**
> 
> This is the file that dictates each button it's position, function and
> other properties.

Now, since we'll be playing with Outline800x480-WVGA interface, crack
open the skin.xml file in your
**/usr/local/share/mixxx/skins/Outline800x480-WVGA**.

You might need super-user password to edit this file.

> How do buttons work?

\>

> In Mixxx, we have Control Objects (COs). Each button is hooked to a
> CO.
> 
> When ever a button is pressed a signal is triggered to Mixxx's engine
> notifying the type of event that has occurred.
> 
> Mixxx's engine knows what to do when an event is triggered.
> 
> Apart form this, there are various kinds of buttons like,
> 
> push-buttons, Play button or Looping belongs to this category.
> 
> knobs, Volume controls fall in this category, etc.
> 
> We'll learn more about COs in following sections.

In **skin.xml** find the comment:

``` 
        <!--
    ############################################################################################
    ############################################################################################
    Section: Buttons
    ############################################################################################
    ############################################################################################
    -->
```

After this comment add the following code:

    <!--
      * ***************************************
         Button- Test
      * ***************************************
        -->
        <PushButton>
            <Tooltip>This is a Test button</Tooltip>
            <Style>QToolTip { font: 11px Lucida Grande, Lucida Sans Unicode, Arial, Verdana, sans-serif;
            background-color: #191919; color: #CCCCCC; border: 1px solid #CCCCCC; padding: 4px; }
            </Style>
            <NumberStates>2</NumberStates>
            <State>
                <Number>0</Number>
                <Pressed>btn_play1.png</Pressed>
                <Unpressed>btn_play1.png</Unpressed>
            </State>
            <State>
                <Number>1</Number>
                <Pressed>btn_play1_over.png</Pressed>
                <Unpressed>btn_play1_over.png</Unpressed>
            </State>
            <Pos>100,100</Pos>
            <Connection>
                <ConfigKey>[Channel1],play</ConfigKey>
                <EmitOnDownPress>true</EmitOnDownPress>
                <ButtonState>LeftButton</ButtonState>
            </Connection>
        </PushButton>

Alright, you are done\!  
Save the changes and restart Mixxx. Find your newly added button as see
how it works.

Following explains what you've just done.

Following lines tell that the this button is a 'push-button'

``` 
    <PushButton>
        ...
    </PushButton>
```

Following lines dictates what Tooltip will show when mouse will hover
over this button.

``` 
    <Tooltip> ... </Tooltip>
    <Style>
          ...
    </Style>
```

In the following lines, **NumberStates** tells, well, number of states
this button can have. Here the sate will be either to play or to
pause.  
**State** will dictate what image will be used for a given state of
button.

> After you complete this tutorial, try changing the image name for a
> given state and see what happens.
> 
> Remember that image name must be from the folder of **skin.xml** you
> are editing.

``` 
                <NumberStates>2</NumberStates>
        <State>
            <Number>0</Number>
            <Pressed>btn_play1.png</Pressed>
            <Unpressed>btn_play1.png</Unpressed>
        </State>
        <State>
            <Number>1</Number>
            <Pressed>btn_play1_over.png</Pressed>
            <Unpressed>btn_play1_over.png</Unpressed>
        </State>
        <Pos> ... </Pos>
```

Following lines tells which CO button is attached to. **ConfigKey**
dictates the name of CO button is stringed to. Here we want to hook to
'play' of \[Channel1\].

> After completing this tutorial, try changing the channel to
> \[Channel2\] and see what happens.  
> **ButtonState** This tells which mouse button to respond to.

``` 
        <Connection>
            <ConfigKey>[Channel1],play</ConfigKey>
            <EmitOnDownPress>true</EmitOnDownPress>
            <ButtonState>LeftButton</ButtonState>
        </Connection>
```

> More about Control Objects.

\>

> **Needs to be reviewed**

\>

> For this tutorial you can easily ignore following information.
> 
> Imagine an array of mechanical levers (The Control Object).
> 
> Each lever is connected to the command center (Mixxx's engine).
> 
> A lever may have any number of states, depending on its function.
> 
> Controls are divided into groups, viz., channel, master etc.
> 
> Each group then has its own control and each control has its states.
> 
> Take a look at **ControlValueDelegate::ControlValueDelegate(...)** in
> 
> **\~/mixxx/mixxx/src/controlvaluedelegate.cpp**, this is where various
> COs are declared.
> 
> Hang on to know how these COs are used.
> 
> I'll talk about the CO we have used, i.e., **\[Channel1\],play**.
> 
> Here the group is **\[Channel1\]** and control name is **play**.
> 
> Open tthe following file to see how this CO is used
> 
> **\~/mixxx/mixxx/src/engine/enginebuffer.cpp**
> 
> In definition of constructor find the following line:

``` 
    playButton = new ControlPushButton(ConfigKey(group, "play"));
```

> Now, if you are familier with Qt's Signal Slot approach, note that
> **playButton** is connected to slot **slotControlPlay**
> 
> Find the definition of **slotControlPlay** in same file and try
> fiddling with it.
> 
> Please note that COs are not only used buttons on interface but also
> in internal functioning of Mixxx.

## What after this?

If you're up for more of a challenge, try adding a different control,
say a Knob/ControlPotmeter. Take a look at how the Knobs are created in
the skin.xml file.
