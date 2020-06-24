To start a timer to flash LEDs on a controller 4 times per second
(250ms) and store the ID in an array for later you would do:

``` javascript
    MyController.timer[0] = engine.beginTimer(250,"MyController.flash()");
```

When the LEDs need to stop flashing, just do:

``` javascript
    engine.stopTimer(MyController.timer[0]);
```

This one-shot timer example causes an LED (note number 0x3A in this
case) to light up red one second after the beginTimer call: (Note the
escaped quotes in the target function call.)

``` javascript

...
    if (engine.beginTimer(1000,"MyController.lightUp(0x3A,\"red\")",true) == 0) {
        print("LightUp timer setup failed");
    }
...

MyController.lightUp = function (led,color) {
    midi.sendShortMsg(0x90, led, MyController.colorCodes[color]);
}
```

#### Closures

Remember, this is an example of what engine.beginTimer can do :

``` javascript
    function doTimer() {
        print("Executed Timer");
    }
    engine.beginTimer(200, "doTimer", 1);
```

With closures the same code can also be written as such:

``` javascript
    engine.beginTimer(200, function() { print("Executed Timer") }, 1);
```

Also since the context is being reused this same code actually works:

``` javascript
    function doMidi() {
        this.value = 1;
        engine.beginTimer(200, function() { if (this.value) print("Executed Timer"); }, 1);
    }
```

This way of using the engine timer is particularly usefull if the
callback function and the call to engine.beginTimer are used in a class
function object wich can be refactored in other projects.

#### Good usage of Timers

Now you have learned the previously exposed principles, we strongly
advise you to have some coding reflex with those timers.

When you create and start your timer, the **engine.beginTimer()**
function will return a value, different from zero if successfullly
initiated, and that will permit you to identify your timer later on in
your code :

``` javascript
   //Sets our variable to zero
   MyController.MyTimer = 0;
   
   //begin timer 
   MyController.MyTimer = engine.beginTimer(250,"MyController.flash()");
   
   if (MyController.MyTimer === 0) {
      print("The timer is not running or failed to start");
   } else {
      print("My timer is running and its ID is : " + MyController.MyTimer);
   }
```

You already know that there are two way a timer can be stopped :

  - Automatically, when the timer has ran out, the callback function is
    then called by the scripting engine.
  - Manually, by using the **engine.stopTimer()** function

In both cases the value of your timer variable is **not** reset to zero,
and if you don't do it in your code, you will never be able to know if
your timer is still running or not \! This can be a problem if you try a
to stop a timer wich is already stopped and do no longer exist (it
generates warnings internally and that can be seen in your terminal
window in debug mode (if you have started mixxx from the command line :
see [Command line
options](http://www.mixxx.org/wiki/doku.php/command_line_options)).

Example 1 of bad use :

``` javascript
   //begin a timer   
   MyController.MyTimer = engine.beginTimer(250,"MyController.ACallback()",true);
   ...
   //Later on in your code
   //begin timer : you start a timer, but maybe the previous is still in use
   MyController.MyTimer = engine.beginTimer(100,"MyController.flash()");   
```

Example 2 of bad use

``` javascript
   //begin a timer   
   MyController.MyTimer = engine.beginTimer(250,"MyController.flash()");
   //Let's say it has started successfully, MyController.MyTimer has now a value different from 0.
   
   //stop timer : 
   engine.stopTimer(MyController.MyTimer); 
   //MyController.MyTimer is still different from 0.
   
   //stop it again
   //the timer represented by the MyController.MyTimer value does no longer exist, 
   //and this generates some mess internally
   engine.stopTimer(MyController.MyTimer); 
```

How to fix this ?

  - The first reflex is to set the variable associated to the timer to
    zero, so that elsewhere if needed in your code you know if the timer
    is runnig and exist (value different from 0) or not. 
  - The variable must be set to zero in the callback function associated
    to a "one-shot" timer.
  - The variable must be set to zero just after the call to
    **engine.stopTimer**
  - **Don't** set your variable to zero in the callback function
    associated with a permanent timer \! Your timer is supposed to be
    still alive \!
  - the second reflex is to test the value of your timer variable before
    each use of **engine.beginTimer** (and stop the timer if it is still
    running just before) and before each use of **engine.stopTimer**.

Example 1 of good usage, we want to light up a LED when we press a
button of the controller and swith it off 5 seconds later. For this, we
need to use a "one shot" timer :

``` javascript
    //Initialize your timer variable to zero at the beginning of the script
    MyController.Timer = 0;
    
    ...
    
    MyController.MyButton = function(channel, control, value, status, group) {
        if (value===0x7F) {
            //Button pressed, let's light up a LED
            midi.sendShortMsg(0x90, 0x3A, 0x7F);
            
        } else {
            //Button released, let's turn off the LED within 5 seconds.
            //For this, we will use a "one shot" timer" 
            
            //1) test any pending timer 
            if (MyController.MyTimer !==0) { 
               //if the delayed action is still "programmed" (the timer is still running becaused
               //we may have pressed and release the button twice in the 5 seconds delay), 
               //we first cancel it by stopping the pending timer
               engine.stopTimer(MyController.Timer);
               //reflex :
               MyController.Timer = 0;
             }
             
             //2) safely start your timer :
             MyController.Timer = engine.beginTimer(250,"MyController.FlashOff()",true);
    };

    MyController.FlashOff = function () {
       //It is a "one-shot" timer calling this, set it's variable to zero
       MyController.Timer = 0;
       //Now it is safe to switch off the LED
       midi.sendShortMsg(0x90, 0x3A, 0x00);
    }
```

Example 2 : We want to implement a button in such a way that if we press
it loads the selected track, and if we keep it longer, it ejects the
track, for this, we need a "one shot" timer.

``` javascript
    // Part that handles the behaviour of the Load button : 
    // Long press (>500 ms) : eject the track
    // Quick press : Load the selected track
    // *****
    
    // Last Time the LOAD Btn was pressed before released
    MyController.LOADlongpress = false;
    MyController.LOADtimer = 0;

    MyController.LOADassertlongpress = function() {
        MyController.LOADlongpress = true;
        MyController.LOADtimer = 0;
    };

    MyController.LOADdown = function() {
        MyController.LOADlongpress = false;
        MyController.LOADtimer = engine.beginTimer(500, "MyController.LOADassertlongpress()", true);
    };

    MyController.LOADup = function(group) {
        if (MyController.LOADtimer !== 0) {
            engine.stopTimer(MyController.LOADtimer);
            MyController.LOADtimer = 0;
        }
        if (MyController.LOADlongpress) {
            engine.setValue(group, 'eject', true);
        } else {
            engine.setValue(group, 'LoadSelectedTrack', true);
        }
    };
    MyController.LoadBtn = function(channel, control, value, status, group) {
    //LOAD hold <500ms : load track, >500ms : eject
    if (value == DOWN) {
        MyController.LOADdown();
        } else {
        MyController.LOADup(group);
        }
    };
```

Example 3 of good usage : This example is much more complex. With one
button we want to start a led flashing, and with a second button, we
want to stop that flashing led. For this, we need two timers, one
permanent, one "one shot".

``` javascript
    //Initialize your timer variable to zero at the beginning of the script
    MyController.flashTimer = 0;
    MyController.flashOnceTimer = 0;
    MyController.num_ms_on = 0;

    // make a light flashing
    //----------------------
    // num_ms_on : number of ms the light should stay enlighted when blinking
    // num_ms_off : number of ms the light should be switched off when blinking
    MyController.flashOn = function(num_ms_on, num_ms_off) {
        //stop pending timers
        MyController.flashOff();

        // init
        MyController.num_ms_on = num_ms_on;

        // 1st flash
        // This is because the permanent timer below takes 
        // num_ms_on milisecs before first flash.
        MyController.flashOnceOn();

        // flashcount =0 means permanent flash,
        // flashcount>0 , means temporary flash, first flash already done,
        // so we don't need this part  if flashcount=1
        // permanent timer
        MyController.flashTimer = engine.beginTimer((num_ms_on + num_ms_off), "MyController.flashOnceOn()");
    };


    // stops the light flashing
    MyController.FlashOff = function() {
        // stop pending flashing effects now
        if (MyController.flashTimer !== 0) {
            engine.stopTimer(MyController.flashTimer);
            MyController.flashTimer = 0;
            MyController.num_ms_on = 0;
        }

        if (MyController.flashOnceTimer !== 0) {
            engine.stopTimer(MyController.flashOnceTimer);
            MyController.flashOnceTimer = 0;
        }

        //Turn off the LED
        midi.sendShortMsg(0x90, 0x3A, 0x00);
    };

    // Call back function (called in flashon() )
    MyController.flashOnceOn = function() {
        //Light up the LED
        midi.sendShortMsg(0x90, 0x3A, 0x7F);
        MyController.flashOnceTimer = engine.beginTimer(MyController.flashDuration, "MyController.flashOnceOff()", true);
    };

    // Call back function (called in flashOnceOn() )
    MyController.flashOnceOff = function() {
        MyController.flashOnceTimer = 0;

        //Turn off the LED
        midi.sendShortMsg(0x90, 0x3A, 0x00);
    };

MyController.MyButtonFlashOn = function(channel, control, value, status, group) {
    if (value===0x7F) {
        MyController.flashOn(200,200); 
    }
};

MyController.MyButtonFlashOff = function(channel, control, value, status, group) {
    if (value===0x7F) {
        MyController.flashOff(); 
    }
};
```
