# Tutorial: Adding a new button to Mixxx

**Warning:** This page is a work-in-progress/stream-of-consciousness
jumble.

## Introduction

## Step 1 - Edit the Skin file

Crack open the skin.xml file in your **Mixxx/skins/outlineSmall** folder
on Windows, or **/usr/share/mixxx/skins/outlineSmall** on Linux.

Paste the following code in after "**\</Background\>**":

``` 
 <PushButton>
  <Tooltip>n00b button</Tooltip>
  <NumberStates>1</NumberStates>
  <State>
   <Number>0</Number>
   <Pressed>sync-on-Ch1.png</Pressed>
   <Unpressed>sync-off-Ch1.png</Unpressed>
  </State>
  <Pos>56,181</Pos>
  <Connection>
   <ConfigKey>[[Channel1]],noob</ConfigKey>
   <EmitOnDownPress>true</EmitOnDownPress>
   <ButtonState>LeftButton</ButtonState>
  </Connection>
 </PushButton>
```

\<Add explanation of what the above does here\>

## Step 2 - Create the ControlPushButton

Now we actually need to do some coding. Each element of Mixxx's UI is
associated with a ControlObject, all of which are subclassed. For
example, the ControlPushButton object is a subclass of ControlObject.
ControlObjects are used throughout Mixxx because they provide a
thread-safe way of reading and storing data/states, and as you will see,
they're very easy to use.

Open up **enginebuffer.cpp**, and find the lines (near line 64) that
say:

``` 
 // Play button
 playButton = new ControlPushButton(ConfigKey(group, "play"), true);
 connect(playButton, SIGNAL(valueChanged(double)), this, SLOT(slotControlPlay(double)));
 playButton->set(0);
```

After these lines, add:

``` 
 // n00b button
 noobButton = new ControlPushButton(ConfigKey(group, "noob"), true);
 connect(noobButton, SIGNAL(valueChanged(double)), this, SLOT(slotControlNoob(double)));
 noobButton->set(0);
```

Now, scroll down to the end of the file, and let's create the event
handler for the button press. Paste in the following code:

``` 
 void EngineBuffer::slotControlNoob(double)
 {
     // Pops up a messagebox when the button is pressed
     if (noobButton->get()==1.)
        QMessageBox::warning(0, "Mixxx Warning","n00b button pressed!");
 }
```

You may also need to add the following to the top of the file:

``` 
 #include <qmessagebox.h>
```

Lastly, let's add the prototypes for the function that we just created
to **enginebuffer.h**. Open up **enginebuffer.h** and paste in the
following code, underneath the line that says "public slots:":

``` 
 void slotControlNoob(double);
```

## Step 3 - Recompile Mixxx

Run **scons** or compile using MSVC. After that, run your new Mixxx
executable and play with your new button\!

## Step 4 - Beyond the ControlPushButton

If you're up for more of a challenge, try adding a different control,
say a Knob/ControlPotmeter. Take a look at how the Knobs are created in
the skin.xml file, and see if you can figure out how to integrate a new
ControlPotmeter into enginebuffer.cpp.

'Hint' In order to read the value from the a ControlObject, you just
need to do something like:

``` 
 float value = potmeter->get();
```
