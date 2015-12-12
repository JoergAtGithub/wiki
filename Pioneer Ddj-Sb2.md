# Pioneer DDJ-SB2

This page based on DDJ-SB manual. Thanks.

[[/media/hardware/pioneer-ddj-sb2_1.jpg|]]

``` 
 *[[http://www.pioneerdj.com/en/product/controller/ddj-sb2/black/overview/|Manufacturer's product page]]
 *[[http://mixxx.org/forums/viewtopic.php?f=7&t=7509&p=26782#p26782|Forum thread]]
 *[[https://github.com/dg3nec/mixxx/tree/DDJ-SB2/res/controllers]]
```

The Pioneer DDJ-SB2 is an all-in-one 4 deck USB MIDI controller with a
built in soundcard. Mixxx allows it to control 4 decks. It is compatible
with Mixxx since version 1.12.

## Drivers

### Windows

Windows Vista, Windows 7 and Windows 8 are supported. You can download
the latest drivers and firmware from
<http://www.pioneerdj.com/en/product/controller/ddj-sb2/black/support/#info>.

**<span class="underline">IMPORTANT for Windows users</span>**: If you
are having issues getting both sound outputs to work properly, please
try using a different Sound API (see the Preferences menu).

### Mac OS X & Linux

No information. If anyone knows more, edit this page.

## User Options

In the file Pioneer-DDJ-SB2-scripts.js are some options.

    ///////////////////////////////////////////////////////////////
    //                       USER OPTIONS                        //
    ///////////////////////////////////////////////////////////////
    
    // If true the sync button blinks with the beat, if false led is lit when sync is enabled.
    PioneerDDJSB2.blinkingSync = true;
    
    // If true, the vinyl button activates slip. Vinyl mode is then activated by using shift.
    // Allows toggling slip faster, but is counterintuitive.
    PioneerDDJSB2.invertVinylSlipButton = false;
    
    // Sets the jogwheels sensivity. 1 is default, 2 is twice as sensitive, 0.5 is half as sensitive.
    PioneerDDJSB2.jogwheelSensivity = 1.0;
    
    // Sets how much more sensitive the jogwheels get when holding shift.
    // Set to 1 to disable jogwheel sensitivity increase when holding shift.
    PioneerDDJSB2.jogwheelShiftMultiplier = 20;
    
    // Time per step (in ms) for pitch speed fade to normal
    PioneerDDJSB2.speedRateToNormalTime = 200;
    
    // If true Level-Meter shows VU-Master left & right. If false shows level of channel: 1/3  2/4 (depending active deck)
    PioneerDDJSB2.showVumeterMaster = false;
    
    // Cut's Level-Meter low and expand upper. Examples:
    // 0.25 -> only signals greater 25%, expanded to full range
    // 0.5 -> only signals greater 50%, expanded to full range
    PioneerDDJSB2.cutVumeter = 0.5;
    
    // If true VU-Level twinkle if AutoDJ is ON.
    PioneerDDJSB2.twinkleVumeterAutodjOn = true;
    
    // If true, by release browser knob jump forward to "position". 
    PioneerDDJSB2.jumpPreviewEnabled = true;
    PioneerDDJSB2.jumpPreviewPosition = 0.5;

## Usage

### Library browsing

The controls for library browsing can be found in the center top of the
controller.

| Control                                  | Function                                                           |
| ---------------------------------------- | ------------------------------------------------------------------ |
| Rotary knob                              | Track selection                                                    |
| Load buttons                             | Loads currently highlighted track to the corresponding deck        |
| Pushing rotary knob                      | Loads currently highlighted track to the preview deck and plays it |
| Pushing rotary knob again without rotate | Stop play preview deck                                             |
| Shift + rotary knob                      | Library section selection                                          |
| Shift + pushing rotary knob              | toggle expanding library section                                   |

Pushing rotary knob "release" jumps forward. Can be configured in user
options.

Addition function not belongs to library:

  - Shift & load left -\> toggle effekts view in/out
  - Shift & load right -\> toggle sampler view in/out

### Switching between decks

Press the deck button. It lights when deck 3-4 is active.

### Volume, equalizers & filters

Between the decks the usual faders, crossfader and EQ knobs can be
found. A filter knob is also available.

Knobs are available for the master and headphones level. These are
functional but are not reflected in Mixxx, as they control the
controller's soundcard directly.

The filter fade button allows to use the crossfader in an innovative way
that fades accross songs through filtering instead of fading.

The TRIM knob controls the gain.

### Jogwheels, tempo & vinyl mode

When a deck is paused, the jogwheel allows you to browse through a
track. If you want to browse faster, hold shift while using the
jogwheel.

When a deck is playing, using the jogwheel allows you to temporarily
change the tempo of the playing track. Again, holding shift exaggerates
this effect.

The tempo slider allows changing the tempo of each deck. This normally
changes the pitch of a track, you can make the pitch stay constant by
pressing the "key lock / tempo range" button. Additional with SHIFT "key
lock / tempo range" button the slider will fade slowly to 0. Fadingspeed
can be set in otions.

Vinyl mode makes the jogwheels emulate the way turntables work. Vinyl
mode can be toggled by pressing the "vinyl / slip" button. Touching the
outer plastic ring of the jogwheel will make it behave as with vinyl
mode off. Touching the metal disc simulates touching the vinyl record,
so just putting your hand on it will stop the "vinyl". You can scratch
in a similar way as with turntables in vinyl mode.

### Slip mode

By pressing shift + "vinyl / slip" you can toggle slip mode. When
entering slip mode, Mixxx remembers what point exactly of the track
should be playing even if, for example, you scratch or make a loop. This
allows to return to the original pace of the track.

### Pads - lower row

The play and cue pads should be self-explaining. The sync pad toggles
master sync for a deck, which tries to beatmatch the deck with the
others, and also syncs the tempo between them, even when the tempo of
one deck is changed.

Additional functions can be accessed by holding shift

| Control      | Function                                                                                              |
| ------------ | ----------------------------------------------------------------------------------------------------- |
| Shift + play | Plays the track in reverse and enables slipping (see slip mode)                                       |
| Shift + cue  | Brakes the track as if the power of the motor on a turntable was turned off                           |
| Shift + sync | Enables quantize mode (this makes most actions, e.g. setting the cue point, fall to the nearest beat) |

### Pads - hot cue mode

In hot cue mode the upper row of pads control the hotcues. Pressing a
pad that is not lit sets a hotcue. Pressing a pad that is lit makes the
track jump and play from that hotcue. Pressing a pad while holding shift
deletes that hotcue.

You can control a set of 4 more hotcues by pressing shift + hot cue. The
hot cue button will start blinking. The pads will behave in the same
way, but controlling hotcues 5 to 8.

### Pads - auto loop mode

Pressing the pads in auto loop mode will make loops of a specific length
measured in beats.

| Control       | Function     |
| ------------- | ------------ |
| Pad 1         | 1 beat loop  |
| Pad 2         | 2 beat loop  |
| Pad 3         | 4 beat loop  |
| Pad 4         | 8 beat loop  |
| Shift + pad 1 | 16 beat loop |
| Shift + pad 2 | 32 beat loop |
| Shift + pad 3 | 64 beat loop |

### Pads - manual loop mode

This mode will make the pads control looping in the way labeled on them.

| Control       | Function                    |
| ------------- | --------------------------- |
| Pad 1         | Set loop in                 |
| Pad 2         | Set loop out                |
| Pad 3         | Toggles loop                |
| Pad 4         | Halve loop length           |
| Shift + pad 4 | Double loop length          |
| Shift + pad 1 | Move loop one beat backward |
| Shift + pad 2 | Move loop one beat forward  |

### Pads - sampler mode

In sampler mode the sampler can be controlled. To load a file into a
sampler, first press the sampler button while holding shift, so that the
sampler button starts blinking. Now pressing a pad will load the
currently highlighted track on the library into the corresponding
sampler. Pressing a pad while holding shift will eject the sample.

To play samples, press the sampler button without holding shift (it
should not blink). Pressing a pad will start playing the corresponding
sample, pressing a pad while holding shift will stop it.

### Pads - loop roll (shift + auto loop)

By pressing the auto loop button while holding shift (it should start
blinking) you can make loop rolls. This mode combines auto loops with
slip mode. The pads will start a loop in the current position with a
determinate beat length while simultaneously enabling slip mode, so that
when releasing the pad the track will continue playing as if the loop
never happened.

| Control       | Function              |
| ------------- | --------------------- |
| Pad 1         | 1/16th beat loop roll |
| Pad 2         | 1/8th beat loop roll  |
| Pad 3         | 1/4th beat loop roll  |
| Pad 4         | 1/2 beat loop roll    |
| Shift + pad 1 | 1 beat loop roll      |
| Shift + pad 2 | 2 beat loop roll      |
| Shift + pad 3 | 4 beat loop roll      |
| Shift + pad 4 | 8 beat loop roll      |

### Pads - kill (shift + manual loop)

By pressing the manual loop button while holding shift (it should start
blinking) you can make the pads behave as kill switches.

| Control | Function  |
| ------- | --------- |
| Pad 1   | Kill low  |
| Pad 2   | Kill mid  |
| Pad 3   | Kill high |
| Pad 4   | Mute      |

### Effects

Over the jogwheels there are sections allowing to control effects 1 & 2.

Turning the knobs will control the mix of an effect.

Turning the knobs while holding one of the three FX buttons will control
the first, second or third parameter of an effect, respectively.

If holding shift when using the knobs the "super" parameter can be
controlled.

Pressing FX buttons toogles output On/Off.

| Button  | Output    |
| ------- | --------- |
| 1       | Deck 1    |
| shift 1 | Deck 3    |
| 2       | Headphone |
| shift 2 | Master    |
| 3       | Deck 2    |
| shift 3 | Deck 4    |

You can choose between effects by entering "kill mode" and using pads 1
and 2 while holding shift.

### Auto DJ

Start/stop Auto DJ: Button shift & DECK 4. If at user optins enabled,
the CH-Level LED's are twinkle.

Skip Track: Button shift & DECK 3.

### Channel fader start

By moving a channel fader up from the very bottom while holding shift
when a deck is paused, the deck will start playing. Moving the fader
back to the bottom without releasing shift stops the deck and moves it
back to its original position.
