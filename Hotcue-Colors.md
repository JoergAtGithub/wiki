# Hotcue Colors

As most other Software, in Mixxx you are able to color hotcues. At the
time of writing (2019/07/08), this can be done via the Hotcues Tab in
the Track properties. Due to the limitations of most controllers, we
constrained the User to the following color selection:
[[/media/cuecolorsreference.svg|]] These are addressed internally and in
controllerscripts via sequential IDs and defined in
[predefinedcolorsset.h](https://github.com/mixxxdj/mixxx/blob/master/src/util/color/predefinedcolorsset.h)


## Controller Mapping Integration

You're a controller mapping creator and wondered how to make use of hotcue colors on your controller?
Then don't worry - we designed this feature with controller support in mind.

When it comes to hotcue buttons, there are 4 types of controllers:
1. Controllers without hotcue buttons
2. Controllers with uncolored buttons
3. Controllers with colored hotcue buttons that allow setting an arbitrary RGB color
4. Controllers with colored hotcue buttons that only allow setting certain, predefined colors

For controllers of types 1 and 2, nothing changes (obviously).

For type 3, we made the RGB color of a hotcue accessible in controller scripts, so you can go ahead and implement support for it.

If your controller mapping uses our JavaScript Components library, this is quite simple: You only need to implement the `HotcueButton::sendRGB(color)` method, that sends the 3-byte RGB color value to the controller (e.g. via a MIDI-SysEx message, depending on your hardware). If you don't use our library, you need to connect to the `[ChannelN],hotcue_X_color` control object which contains the 3-byte RGB value and send the appropriate messages to your controller whenever it changes (and the hotcue is set, i. e. `[ChannelN],hotcue_X_enabled` is not `0`).

What about type 4?
Controllers that only allow choosing from a predefined color set were probably designed that way because they were sold with a software that does not allow assigned arbitrary colors to hotcues.
You can think of these predefined colors as a list, and usually you can set the pad color of these controllers by sending the color's index in that list as MIDI value.
For example, red could be color 1, blue is color 2, yellow is color 3, green is color 4 and so on.

We added a `ColorMapper` class that you can use to establish a mapping between these IDs and and can be used to get the appropriate MIDI value for a given color.

For the more technically inclined, here's a source code example how to use it in a JavaScript controller mapping:

```javascript
var colors = new ColorMapper({
  0xFF0000: 1,  // Red
  0x0000FF: 2,  // Blue
  0xFFFF00: 3,  // Yellow
  0x00FF00: 4,  // Green
  // ...
});

// Get the MIDI value for the color "blue"
var value = colors.getValueForNearestColor(0x0000FF)

// value now equals 2
```

You can send the resulting value to your controller to set the pad to the desired color.

But what happens if you set a hotcue to a color that isn't supported by the controller?
Obviously, it's not possible to show the exact same color on your controller if the hardware simply doesn't support it - but don't worry, we've got you covered.

In this case, `ColorMapper::getValueForNearestColor()` returns the value of the color that is *most similar* to the color you put in.
As an example, the hotcue color in Mixxx could be a darker shade of blue - `ColorMapper` will simply return the color for the regular blue color in this case, because it's the best match.

```javascript
// Get the MIDI value for the color "dark blue"
var value = colors.getValueForNearestColor(0x0000AA)

// value now equals 2 (the same value as for regular "blue")
```

Seems complicated?
It doesn't have to be.
If your mapping already uses our JavaScript Components library, you don't actually need to call `ColorMapper::getValueForNearestColor()` yourself.
Just create a `ColorMapper` object and pass it to the `HotcueButton` and your colored hotcue pads should start working immediately!

We also added control objects to to make it possible assign a different color to the most recently used ("focused") hotcue from your controller, using the `[ChannelN],hotcue_focus_color_prev` and `[ChannelN],hotcue_focus_color_next` controls. For example,these COs could be mapped to the "Parameter -/+" buttons next to the hotcue pads (if applicable). 