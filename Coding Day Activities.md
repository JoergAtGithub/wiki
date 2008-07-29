# Coding Day

On Tuesday July 29th, we'll be having a day of code to get release 1.6.0
ready to go. If you want to help, hop on our IRC channel (**\#mixxx** on
Freenode) and we'll get you involved.

There's tons of stuff to do, here's a list:

  - Coding/Bug fixing obviously needs doing, visit the [launchpad
    tracker](https://launchpad.net/mixxx/) and talk to the developers
  - Testing will be needed at various points on various platforms
    throughout the day
  - Documentation needs plenty of work
  - Especially the [manual](manual) could use a lot of work
  - New website design is in progress, anyone with useful
    php/javascript/jquery skills should talk to **asantoni** (IRC)
  - Could use some new high quality skins if there are any designers out
    there

## Available Non-Coding Tasks:

  - **Test Serato CD support**. Got a CDJ? Have a CD discman or anything
    that plays CDs? Download the Serato CD wave, burn it to a CD, and
    test to see if you can control Mixxx via your CDJ or discman. 
  - The wave can be downloaded
    here:<http://rane.com/scratchlivecontrol.zip>
  - Report your findings on IRC and here:
    <https://bugs.launchpad.net/mixxx/+bug/186341>
  - **Create the massive 1.6.0 changelog**. Go through the [Mixxx
    Blog](http://mixxxblog.blogspot.com/) archives, and find the release
    announcements for 1.6.0 beta 1, 2, 3, and 4. A changelog was
    included with each release - copy and paste the changelog bullets
    from each announcement into one gigantic document. Email that to
    someone on IRC. 

<!-- end list -->

``` 
* 
```

## Available Coding Tasks:

  - **Cleanup Input Controllers Prefs**. The "Input Controllers"
    preferences pane contains unsupported (broken) mouse control stuff.
    Remove this from dlgprefmidi.cpp and dlgprefmididlg.ui and send us a
    patch.
  - **QSpinBox-\>QDoubleSpinBox in Interface Prefs**. The temporary and
    permanent pitch/rate buttons options in the interface preferences
    pane uses QSpinBox controls, which only support integer numbers. The
    value in the spinbox controls is actually divided by 1000 before
    being applied to Mixxx's engine (a value of 400 turns into a pitch
    bend of 0.4%). Your task is to change the QSpinBox controls to
    QDoubleSpinBox and remove the division by 1000, so it's WYSIWYG.
    Make your changes to dlgprefcontrols.cpp and dlgprefcontrolsdlg.ui
    and send us a patch. Please test the hell out of this before sending
    us a patch because we'd rather not break this before 1.6.0.
